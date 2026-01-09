import os
import pty
import threading
import time
import select
import re


class SSHSession:
    def __init__(
        self,
        host,
        user,
        password,
        on_output=None,
        on_error=None,
        on_status=None,
    ):
        self.host = host
        self.user = user
        self.password = password

        self.on_output = on_output or print
        self.on_error = on_error or print
        self.on_status = on_status or print

        self.authenticated = False
        self.alive = True

        self.on_status(f"[SSH] Connecting to {user}@{host} ...")

        self.pid, self.fd = pty.fork()

        if self.pid == 0:
            # Child: exec ssh
            os.execvp(
                "ssh",
                [
                    "ssh",
                    f"{user}@{host}",
                    "-tt",
                    "-o", "StrictHostKeyChecking=no",
                    "-o", "UserKnownHostsFile=/dev/null",
                    "-o", "LogLevel=ERROR",
                ],
            )

        # Parent
        threading.Thread(target=self._reader, daemon=True).start()

    # -----------------------------------------------------

    def _reader(self):
        buffer = b""

        while self.alive:
            try:
                r, _, _ = select.select([self.fd], [], [], 0.1)
                if not r:
                    continue

                data = os.read(self.fd, 4096)
                if not data:
                    self.on_status("[SSH] Connection closed")
                    break

                buffer += data
                text = buffer.decode(errors="ignore")

                # ---- password prompt ----
                if not self.authenticated and re.search(r"password:", text, re.I):
                    self._send_password()
                    buffer = b""
                    continue

                # ---- successful login ----
                if not self.authenticated and re.search(r"[$#] $", text):
                    self.authenticated = True
                    self.on_status("[SSH] Authenticated successfully")
                    buffer = b""
                    continue

                # ---- error detection ----
                if self._looks_like_error(text):
                    self.on_error(f"[SSH ERROR] {text.strip()}")

                else:
                    # Normal command output
                    self.on_output(text.rstrip())

                buffer = b""

            except OSError:
                self.on_status("[SSH] Reader thread terminated")
                break

    # -----------------------------------------------------

    def _send_password(self):
        time.sleep(0.2)
        os.write(self.fd, (self.password + "\n").encode())

    # -----------------------------------------------------

    def _looks_like_error(self, text: str) -> bool:
        error_keywords = [
            "error",
            "failed",
            "no such file",
            "command not found",
            "permission denied",
            "cannot",
            "not recognized",
        ]
        lower = text.lower()
        return any(k in lower for k in error_keywords)

    # -----------------------------------------------------

    def run(self, cmd: str):
        if not self.authenticated:
            self.on_status("[SSH] Cannot run command: not authenticated")
            return

        if not cmd.endswith("\n"):
            cmd += "\n"

        self.on_status(f"[SSH CMD] {cmd.strip()}")
        os.write(self.fd, cmd.encode())

    # -----------------------------------------------------

    def close(self):
        self.alive = False
        try:
            os.close(self.fd)
        except OSError:
            pass
