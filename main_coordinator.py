# main.py
import sys
from threading import Thread
import time
import rclpy
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from frontend.Qwindow import MainWindow            # Ui logic
from backend.bridge import ROSQtBridge             #ROSQt bridge
from PySide6.QtCore import QTimer
import subprocess
import os

# from backend.async_db_writer import InfluxDBWriter   #Async DB writer
# from backend.fetchers.gps import gpsFetcher

def launch_ffplay0_and_arrange():
    # 1️⃣ Launch the alias from bash/zsh
    #Assuming 'view_cam_orin' is available in your shell
    print("launching ffplay")
    proc = subprocess.Popen(
        ["bash", "-ic", "view_cam_xavier", "0", "5000"],  # '-i' for interactive so alias works
    )
    # proc = subprocess.Popen(
    #     ["ffplay", "-fflags", "nobuffer", "-flags", "low_delay", "/dev/video0", "-window_title", "XCAM1"]
    # )
     
    time.sleep(2)  # tweak if needed
    print("finding window")
    wid_list = os.popen('xdotool search --name "udp://10.42.0.51:5000"').read().split()
    if not wid_list:
        print("FFPLAY window not found!")
        return
    wid = wid_list[0]
    print(f"FFPLAY window id: {wid}")

    i3_command = f'[id={wid}] move container to workspace 2, floating enable, resize set 550 300, move position 650 600'
    subprocess.run(["i3-msg", i3_command])

def launch_ffplay2_and_arrange():
    # 1️⃣ Launch the alias from bash/zsh
    #Assuming 'view_cam_orin' is available in your shell
    print("launching ffplay")
    proc = subprocess.Popen(
        ["bash", "-ic", "view_cam_xavier", "2", "5001"],  # '-i' for interactive so alias works
    )
    # proc = subprocess.Popen(
    #     ["ffplay", "-fflags", "nobuffer", "-flags", "low_delay", "/dev/video0", "-window_title", "XCAM1"]
    # )
     

    time.sleep(2)  # tweak if needed

    wid_list = os.popen('xdotool search --name "XCAM1"').read().split()
    if not wid_list:
        print("FFPLAY window not found!")
        return
    wid = wid_list[0]
    print(f"FFPLAY window id: {wid}")

    i3_command = f'[id={wid}] move container to workspace 2, floating enable, resize set 550 300, move position 650 600'
    subprocess.run(["i3-msg", i3_command])

def main():
    rclpy.init()
    app = QApplication(sys.argv)
    window = MainWindow()
    bridge = ROSQtBridge()  # subscribes to all topics

    # influx_writer = InfluxDBWriter(
    #     influx_url="http://localhost:8086",
    #     token="X2g3gxwO9AlpnQOVZ3GKDYgO8T2XJpIY75FG0WOx8GSUjxYzw1N__IGqT0Q2HU4DvLF5RmUHpZOOatROjNeCuA==",
    #     org="anveshak",
    #     bucket="rover_data",
    #     flush_interval=1.0
    # )
    # influx_writer.start()  # start writer thread

    bridge.gps_updated.connect(window.update_gps)
    bridge.yaw_updated.connect(window.update_yaw)
    bridge.odom_updated.connect(window.update_odom)
    # bridge.latency_updated.connect(window.update_latency)
    bridge.steering_angles.connect(window.ui.roverwheelwidget.set_wheel_angles)
    bridge.mode_updated.connect(window.update_mode)
    bridge.config_updated.connect(window.update_config)
    bridge.twist_updated.connect(window.update_twist)
    bridge.encoder_angles_updated.connect(window.update_encoder_angles)
    bridge.start_csv_watcher("waypoints.csv")
    bridge.csv_changed.connect(window.load_waypoints)
    bridge.frequency_updated.connect(window.update_frequency)
    bridge.noise_updated.connect(window.update_noise)
    bridge.toast_signal.connect(window.show_toast)
    window.send_signal.connect(bridge.send_handler)
    window.kill_signal.connect(bridge.kill_handler) #for kill switch
    window.colour_signal.connect(bridge.colour_override_handler)
    window.autolog_signal.connect(bridge.autolog_handler)
    window.brightness_signal.connect(lambda cam, val: bridge.cam_setting_handler(cam, "brightness", val))
    window.contrast_signal.connect(lambda cam, val: bridge.cam_setting_handler(cam, "contrast", val))
    window.zoom_signal.connect(lambda cam, val: bridge.cam_setting_handler(cam, "zoom", val))
  
    refresh_timer = QTimer()
    refresh_timer.setInterval(1000)  # ms (adjust if needed)
    refresh_timer.timeout.connect(window.load_waypoints)
    refresh_timer.start()

    # #async writing 
    # bridge.gps_updated.connect(lambda lat, lon: influx_writer.enqueue({
    # "latitude": lat,
    # "longitude": lon
    # }))

    # bridge.imu_data_received.connect(lambda msg: influx_writer.enqueue({
    # "roll": msg.orientation.x,
    # "pitch": msg.orientation.y,
    # "yaw": msg.orientation.z
    # }))

    # bridge.battery_updated.connect(lambda val: influx_writer.enqueue({"battery": val}))
    # bridge.latency_updated.connect(lambda val: influx_writer.enqueue({"latency": val}))
    # bridge.can_status.connect(lambda val: influx_writer.enqueue({"can_status": val}))

    # #fetching for graphs
    # # --- GPS fetcher ---
    # gps_fetcher = gpsFetcher(
    #     influx_url="http://localhost:8086",
    #     token="X2g3gxwO9AlpnQOVZ3GKDYgO8T2XJpIY75FG0WOx8GSUjxYzw1N__IGqT0Q2HU4DvLF5RmUHpZOOatROjNeCuA==",
    #     org="anveshak",
    #     bucket="rover_data", 
    #     poll_interval=1.0
    # )

    # # gps_fetcher.gps_fetched.connect(lambda latitude, longitude: print(f"Fetched GPS -> lat: {latitude}, lon: {longitude}"))

    # gps_fetcher.start()

    ros_thread = Thread(target=rclpy.spin, args=(bridge,), daemon=True)
    ros_thread.start()

    # --- Show GUI ---
    window.show()

    # --- Execute Qt event loop ---
    exit_code = app.exec()

    # --- Cleanup on exit ---
    print("Shutting down...")
    # influx_writer.stop()
    bridge.destroy_node()
    rclpy.shutdown()
    sys.exit(exit_code)


if __name__ == "__main__":
    #launch_ffplay0_and_arrange()
    #launch_ffplay2_and_arrange()
    main()
