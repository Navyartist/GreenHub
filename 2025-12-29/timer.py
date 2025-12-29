import tkinter as tk


# 타이머 앱
# ==레이아웃==
# 0:00:00 ~ 99:59:59까지 카운트되는 시간 표시 라벨 1개 grid(row=1, column=0)
# "button1(name='초기화', gird(row=1, column=0)
# "button2(name='컨트롤', state: '시작'/'정지'/'재시작'), grid(row=1, column=1)) 버튼 2개로 구성된다.

# "button2(state='시작')"을 누르면 초기상태 0:00:00에서 시간이 흐른다.
# 이후 "button2(state='시작')"은 "button2(state='정지')"으로 바뀐다.
# "button1"을 누르면 시간 표시 라벨의 시간이 0:00:00으로 초기화되고 다시 흐른다.
# "button2(state='정지')"를 누르면 시간 표시 라벨의 시간이 멈춘다.
# "button2"의 state는 '정지'에서 '재시작' 으로 바뀐다.
# 시간 표시 라벨의 시간이 정지한 상태에서 "button2" (state='재시작')를 누르면 시간 표시 라벨의 시간이 다시 흐르기 시작한다.