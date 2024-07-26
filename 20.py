#순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 
# 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = 0
    num = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j == n:
                num.append((i, j))
                
                answer += 1
    
    pairs = ", ".join([f"({i},{j})" for i, j in num])
    print(f"n이 {n}이므로 곱이 {n}인 순서쌍은 {pairs} 개수는 {answer}입니다.")
    return answer   

n = 20
if 1 <= n <= 100000:
    solution(n)
else:
    print("n의 범위를 벗어났습니다.")
