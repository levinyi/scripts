import sys
sys.path.append('/cygene/script/python_SMS')
import psutil
import time
from sms import textbelt


# 监控进程的PID
pid = int(sys.argv[1])

# 轮询间隔（秒）
poll_interval = 60

# 进程是否仍在运行
process_running = True

# 循环检查进程是否仍在运行
while process_running:
    # 检查进程是否仍在运行
    if not psutil.pid_exists(pid):
        process_running = False
        print("Process has ended. Sending SMS notification.")

        # 发送短信
        # Using SMS module.
        textbelt()
        # Using email module
        print("SMS notification sent.")

    # 等待一段时间后再次检查进程是否仍在运行
    time.sleep(poll_interval)
print("Over!")
