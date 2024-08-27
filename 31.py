#정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱합니다. 그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.
def solution(arr):
    answer = []
    for i in arr:
        if   50 <= i and i % 2 == 0  :
            answer.append(int(i / 2))
        elif  not(i % 2 == 0) and i < 50 :
            answer.append( 2 * i)
        else:
            answer.append(i)
    print(answer)
    return answer

def check(arr):
    if not(1 <= len(arr) <= 1000000):
        return False
    for i in arr:
        if not(1 <= i <= 100):
            return False 
    return True




arr = [1, 2, 3, 100, 99, 98]
if check(arr):
    solution(arr)