#머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.
def solution(n):
    
    answer = int(n / 7) + 1
    return print(f"{n}명이 피자를 먹기 위해 필요한 피자의 수는 {answer} 입니다.")   

n = int(input("숫자를 입력해 주세요 "))

if 1<= n <= 100:
    solution(n)
else:
    print("범위를 벗어났습니다.")