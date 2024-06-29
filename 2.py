# 정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    
    return num1 / num2

num1 = int(input("num1 의 값을 입력 하시오"))

num2 = int(input("num2 의 값을 입력 하시오"))
if 0 <num1 < 100 and 0< num2 <100 :
    print("num1 의값 :"+num1+"num2의 값 :"+num2+solution(num1,num2))
else:
    print("0~100까지만 입력해 주세요, 범위를 벗어났습니다.")
    num1 = int(input("num1 의 값을 입력 하시오"))
    num2 = int(input("num2 의 값을 입력 하시오"))
