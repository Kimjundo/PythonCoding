#정수 배열 numbers와 정수 n이 매개변수로 주어집니다. numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성해 주세요.
def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        if answer > n:
            print(answer)
            return answer
            
    

def check(numbers, n):
    sum = 0
    if not(1<= len(numbers) <= 100):
        return False 
    for i in numbers:
        sum += i
        if not(1<= i <=100):
            return False 
    if not ( 0<= n <sum ):
        return False
    return True



numbers = [58, 44, 27, 10, 100]
n = 139
if check(numbers, n):
    solution(numbers,n)