#정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1

    print(f"{array} 에서 {n}의 개수는 {answer}개 입니다.")
    return answer

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(input(" 숫자를 입력해 주세요"))
for i in array:
    if not (0 <= i <= 1000):
        print("범위를 벗어났습니다.")
        break



if ( 1< len(array) < 100) and (0 <= n <= 1000):
    solution(array, n)
else:
    print("범위를 벗어났습니다.")
