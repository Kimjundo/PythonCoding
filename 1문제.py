# 두수의차 정수 num1 과 num2 가 주어질때, num1에 서 num2를 뺀 값을 return 하도록 solution함수를 완성 하시오
def solution(num1, num2):
    answer = num1 - num2
    return answer 
num1 = int(input('num1을 입력해 주세요'))
num2 = int(input('num2을 입력해 주세요'))


print(num1 + num2 + solution(num1,num2))
