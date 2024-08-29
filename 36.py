#정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.
#num_list	                  result
#[12, 4, 15, 46, 38, -2, 15]	5
#[13, 22, 53, 24, 15, 6]	   -1
#입출력 예 설명
#입출력 예 #1
#5번 인덱스에서 음수가 처음 등장하므로 5를 return합니다.

#입출력 예 #2
#음수가 없으므로 -1을 return합니다.
def solution(num_list):
    answer = 0
    count = 0
    for i in num_list:
        
        if i < 0 :
            answer = count
            print(answer) 
            return answer
        elif i >= 0  :
            answer = -1 
        count += 1 
    print(answer)
    return answer

def check(num_list):
    if not(5<= len(num_list) <= 100):
        return False
    for i in num_list:
        if not( -10<= i <= 100):
            return False
    return True


num_list = [13, 22, 53, 24, 15, 6]

if check(num_list):
    solution(num_list)

