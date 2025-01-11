import pyautogui
import time

def main():
    print("\n마우스 좌클릭 타이머입니다. 분:초 형태로 여러 시간을 입력하세요 (예: 1:30). '그만'을 입력하면 모든 입력된 시간마다 마우스 좌클릭을 실행합니다.\n")

    time_list = []
    start = (356, 518)  # 재생버튼 위치
    Next = (730, 591) # 다음버튼 위치치

    while True:
        user_input = input("시간 입력 (분:초 또는 '그만'): ").strip() # ex)0:02, 16:02

        if user_input.lower() == '그만':
            print("입력된 모든 시간에 대해 마우스 좌클릭을 실행합니다.")
            # 재생생
            pyautogui.moveTo(start) # 재생버튼으로 이동
            time.sleep(3)
            pyautogui.click() #재생버튼 클릭릭
            print("재생")


                
            for idx, time_str in enumerate(time_list, start=1):
                try:
                    minutes, seconds = map(int, time_str.split(':'))
                    total_seconds = minutes * 60 + seconds + 8
                    print(f"{idx}번째 시간 {minutes}분 {seconds}초 대기 중...")
                    time.sleep(total_seconds)  # 입력된 시간만큼 대기

#첫 번째 클릭릭
                    if Next:
                        pyautogui.moveTo(Next) #다음버튼으로 이동            
                    pyautogui.click()
                    print(f"{idx}번째 시간에 첫 번째 마우스 좌클릭이 실행되었습니다.")

                    # 지정된 좌표로 이동
                    pyautogui.moveTo(start)
                    time.sleep(5)  # 3초 대기

                    # 두 번째 클릭
                    pyautogui.click()
                    print(f"{idx}번째 시간에 지정된 좌표에서 두 번째 마우스 좌클릭이 실행되었습니다.")

                    # 원래 위치로 돌아가기
                    if Next:
                        pyautogui.moveTo(Next)
                        print(f"{idx}번째 작업 후 원래 위치로 복귀했습니다.\n")

                except ValueError:
                    print(f"잘못된 시간 형식: {time_str}. 이 시간을 건너뜁니다.\n")
            print("모든 작업이 완료되었습니다. 프로그램을 종료합니다.")
            break

        try:
            minutes, seconds = map(int, user_input.split(':'))
            time_list.append(user_input)
            print(f"{minutes}분 {seconds}초가 목록에 추가되었습니다.\n")
        except ValueError:
            print("잘못된 입력입니다. 분:초 형식으로 다시 입력해주세요. (예: 1:30)\n")

if __name__ == "__main__":
    main()
