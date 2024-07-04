#정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
def solution(n):
    answer = 0
    n += 1
    for i in range(n):
        if i % 2 == 0:
            answer += i
            print(f" {i} +", end="")
            
    print(f" = {answer}")
    return answer

n = int(input("숫자를 입력해 주세요 1000이하의 숫자만 가능"))

if 0 < n < 1000:
    solution(n)
else:
    print("범위를 벗어 났습니다.")
