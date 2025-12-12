import src.practics as prac
import os

print(prac.greet_Return("itsname"))
print(prac.greet_nonReturn("itsname-var"))

result = dir(os) # python 내장 라이브러리- 내장모듈 
print(result)

# 파이썬 내장라이브러리 뭐있는지 조사하기
# 처음보는 함수를 그냥 사용해본다
# 리턴 없는/있는 함수 구분 연습
# 오늘 미션: 세상에 없는 자판기 만들기
#   함수: 자판기 그 자체
#   매개변수(입력) : 돈넣는곳
#   리턴 : 상품배출구
#   프린트: print() 자판기 화면에 불이 들어오는 것

print(prac.routine())