#정수 리스트 num_list와 정수 n이 주어질 때, num_list의 첫 번째 원소부터 마지막 원소까지 n개 간격으로 저장되어있는 원소들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
def solution(num_list, n):
    answer = []
    for i in num_list[0::n]:
        answer.append(i)
    print(answer)
    return answer

def check(num_list,n):
    if not(5<= len(num_list) <=20):
        return False 
    elif not( 1<= n <=4):
        return False
    for i in num_list:
        if not(1<= i <=9):
            return False
    return True
    

num_list = [4, 2, 6, 1, 7, 6]
n = 4
if check(num_list,n):
    solution(num_list,n)

