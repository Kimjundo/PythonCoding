#정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    answer = []
    count = 0
    for i in numbers:
        if -10000 < i < 10000:
            count += 1
        else:
            print(f"{i}가 범위를 벗어났습니다.")
            return 0 
    if count == len(numbers):
        for i in numbers:
            answer.append(i*2)
            
    return print(answer)


numbers = [1,2,3,4,5]

if 1<= len(numbers) <= 1000:
    print(numbers)
    solution(numbers)