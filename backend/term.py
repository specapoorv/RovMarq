import os
import pty
import threading
import time
class SSHSession():
    pass

# class SSHManager:
#     global ssh_orin
#     ssh_orin = SSHSession(
#         host="10.42.0.253",
#         user="orin",
#         password="anveshak"
#     )

#     time.sleep(2) #for ssh to happen properly


class SSHSession:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.authenticated = False

        self.pid, self.fd = pty.fork()

        if self.pid == 0:
            # Child: exec ssh
            os.execvp(
                "ssh",
                [
                    "ssh",
                    f"{user}@{host}",
                    "-o", "StrictHostKeyChecking=no",
                    "-o", "UserKnownHostsFile=/dev/null",
                ]
            )
        else:
            # Parent
            threading.Thread(target=self._reader, daemon=True).start()

    def _reader(self):
        buffer = b""
        while True:
            try:
                data = os.read(self.fd, 1024)
                if not data:
                    break

                buffer += data
                text = buffer.decode(errors="ignore").lower()

                # Detect password prompt
                if "password:" in text and not self.authenticated:
                    self._send_password()
                    buffer = b""
                    continue

                # Detect successful login
                if "$ " in text or "# " in text:
                    self.authenticated = True

                # Optional: log
                # print(text, end="")

            except OSError:
                break

    def _send_password(self):
        time.sleep(0.2)  # small delay for safety
        os.write(self.fd, (self.password + "\n").encode())

    def run(self, cmd):
        if not cmd.endswith("\n"):
            cmd += "\n"
        os.write(self.fd, cmd.encode())

    def close(self):
        try:
            os.close(self.fd)
        except OSError:
            pass
