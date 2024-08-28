#정수 리스트 num_list와 정수 n이 주어질 때, num_list의 첫 번째 원소부터 n 번째 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list, n):
    answer = []
    for i in num_list[0:n]:
        answer.append(i)
    print(f"{num_list}의 첫번째 원소 부터 {n} 까지의 모든 원소는 {answer} 입니다.")
    return answer

def check(num_list,n):
    if not(2 <= len(num_list) <= 30):
        return False
    elif not(1<= n <= len(num_list)):
        return False
    for i in num_list:
        if not( 1<= i <=9):
            return False
    return True
        
    

num_list = [2, 1, 6]
n = 1 
if check(num_list,n):
    solution(num_list,n)