import pyautogui
import time

print("Ctrl+C를 눌러 프로그램을 종료하세요.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"현재 마우스 위치: X={x}, Y={y}", end="\r")  # 실시간 출력
        time.sleep(0.1)  # 0.1초 간격으로 갱신
except KeyboardInterrupt:
    print("\n프로그램 종료")
