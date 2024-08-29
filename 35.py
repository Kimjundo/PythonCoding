# 정수 리스트 num_list와 정수 n이 주어질 때, 
# num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠 n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.
#입출력 예 설명
#입출력 예 #1

#[2, 1, 6]에서 첫 번째 이후의 원소는 [1, 6]이고 첫 번째까지의 원소는 [2]입니다. 두 리스트를 이어 붙이면 [1, 6, 2]가 됩니다.
#입출력 예 #2

#[5, 2, 1, 7, 5]에서 세 번째 이후의 원소는 [7, 5]이고 세 번째까지의 원소는 [5, 2, 1]입니다. 두 리스트를 이어 붙이면 [7, 5, 5, 2, 1]가 됩니다.
def solution(num_list, n):
    answer = []
    for i in num_list[n::]:
        answer.append(i)
    for j in num_list [:n:]:
        answer.append(j)
    
    print(answer)
    return answer


def check(num_list,n):
    if not(2<= len(num_list) <= 30):
        return False
    elif not(1<= n <= len(num_list)):
        return False
    for i in num_list:
        if not(1<= i <=9):
            return False
    return True    
    
        
    


num_list = [5, 2, 1, 7, 5]
n = 3 

if check(num_list, n):
    solution(num_list,n)