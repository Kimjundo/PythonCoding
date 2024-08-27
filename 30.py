# 정수가 담긴 리스트 num_list가 주어질 때, 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    answer = 0
    sum = 0
    print(len(num_list))
    if 11<= len(num_list):
        for i in num_list:
            sum += i
    elif len(num_list) <= 10:
        sum = 1
        for i in num_list:
            sum *= i
    elif sum > 2147483647:
        return False
    print(sum)
    return sum




def check(num_list):
    if not(2 < len(num_list) <= 20):
        return False
    for i in num_list:
        if not(i <= i <= 9):
            return False
    return True


num_list = [2, 3, 4, 5]

if check(num_list):
    solution(num_list)