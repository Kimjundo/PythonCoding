#정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    answer =  num1 / num2
    print("num1 의 값은" +str(num1)+"num2가"+str(num2) +"이므로 "+str(num1) +"을"+str(num2)+"나눈 나머지"+str(answer)+"을 return 합니다.")
    return answer

num1 = int(input("num1 의 값을 입력 하시오"))
num2 = int(input("num2 의 값을 입력 하시오"))
if 0 <num1 < 100 and 0< num2 <100 :
     print(solution(num1,num2))
else:   
    print("0~10000까지만 입력해 주세요, 범위를 벗어났습니다.")
