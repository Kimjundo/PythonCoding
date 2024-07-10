#정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    max = 0
    for i in numbers:
        for j in numbers:
            if i != j:
                if max < i*j:
                    max = i*j
    answer = max
    print(answer)
    return answer

numbers = [2,4,5,9,55,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 ]

solution(numbers)