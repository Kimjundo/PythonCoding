# #정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.
# def solution(n, numlist):
#     answer = []
#     count = n
#     num = []
#     for j in range(len(numlist)):
#         num.append(count)
#         count += n
#     j = 0
#     for i in numlist:
#         for j in num:
#             if i == j:
#                 answer.append(i) 
        
#     print(answer)
#     return answer


# numlist = [1, 9, 3, 10, 13, 5]
# n = 5

# if not(1 <= n <= 10000) and not(1 <= len(numlist) <= 10000):
#     print("n의 범위를 벗어났습니다.")
# for i in numlist:
#     if not(1<=  i <= 1000000):
#         print("numlist의 범위를 벗어났습니다.")
#         break

# solution(n, numlist)
def solution(n, numlist):
    return [num for num in numlist if num % n == 0]

# 입력값 검증
def validate_input(n, numlist):
    if not (1 <= n <= 10000):
        print("n의 범위를 벗어났습니다.")
        return False
    if not (1 <= len(numlist) <= 10000):
        print("numlist의 길이가 범위를 벗어났습니다.")
        return False
    if any(not (1 <= num <= 1000000) for num in numlist):
        print("numlist의 요소 중 범위를 벗어난 값이 있습니다.")
        return False
    return True

# 테스트
n = 5
numlist = [1, 9, 3, 10, 13, 5]

if validate_input(n, numlist):
    result = solution(n, numlist)
    print(result)