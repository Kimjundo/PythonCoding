# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    
    answer = answer /len(numbers)
    print(answer)
    return answer


numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
count = 0 
for i in numbers:
    if (0 < i < 1000):
        count += 1


if(bool(count) and 0 < len(numbers) < 1000 ):
    solution(numbers)

