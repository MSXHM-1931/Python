import time
import sys

def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        sys.stdout.write(f"\r剩余时间: {remaining} 秒   ")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r时间到!           \n")

if __name__ == "__main__":
    try:
        seconds = int(input("请输入倒计时时间（秒）: "))
        countdown_timer(seconds)
    except ValueError:
        print("请输入有效的整数秒数。")
