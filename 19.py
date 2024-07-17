#정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2+1):
        answer.append(numbers[i])
    print(f"{numbers}의 {num1}번째 인덱스부터 {num2}번째 인덱스까지 자른 정수 배열은 {answer}를 리턴 합니다.")
    return answer

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num1 = int(input("첫번째 인덱스를 입력하세요: "))
num2 = int(input("두번째 인덱스를 입력하세요: "))

for i in numbers:
    if 0 <= i <= 1000:
        pass
        # 그냥 numbers의 원소 확인 구문 
    else:
        print("범위를 벗어났습니다.")
        break
if 0<= num1 <= num2 <= len(numbers):
    solution(numbers, num1, num2) 
else:
    print("인덱스의 범위를 벗어났습니다.")
