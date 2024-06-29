#정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    if num1 == num2:
        answer = 1
        print("num1 의 값은" +str(num1)+"num2가"+str(num2) +"이므로 같습니다. 따라서"+str(answer)+"을 return 합니다.")
        return answer
    else:
        answer = -1
        print("num1 의 값은" +str(num1)+"num2가"+str(num2) +"이므로 틀립니다.. 따라서"+str(answer)+"을 return 합니다.")
        return answer

num1 = int(input("num1 의 값을 입력 하시오"))
num2 = int(input("num2 의 값을 입력 하시오"))
if 0 <num1 < 10000 and 0< num2 <10000  :
     print(solution(num1,num2))
else:   
    print("0~10000까지만 입력해 주세요, 범위를 벗어났습니다.")
    num1 = int(input("num1 의 값을 입력 하시오"))
    num2 = int(input("num2 의 값을 입력 하시오"))