#정수 num1과 num2가 주어질 때, num1과 num2의 합을 return하도록 soltuion 함수를 완성해주세요.
def solution(num1, num2):
    answer = num1 - num2
    print(f"num1 의 값 :{num1} num2 의 값 :{num2}, {num1} - {num2} = {answer} ")
    return answer

num1 = int(input("num1 의 값을 입력 해주세요"))
num2 = int(input("num2 의 값을 입력 해주세요"))
if( - 50000 < num1 < 50000 and -50000 < num2 < 50000 ):
    solution(num1,num2)
else:
    print("범위를 벗어나 입력 하셨습니다")

