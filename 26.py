#정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(array):
    answer = []
    max = 0 
    max_count = 0
    for i in array:
        if i > max:
            max = i
        

    for j in array:
        if j == max:
            break
        max_count += 1


    answer.append(max)
    answer.append(max_count)
    print(answer)
    return answer


array =  [1, 8, 3]
array = set(array)
array = list(array)
for i in array:
    if not(0 <= i <= 1000):
        print("배열의 값의 범위가 벗어났습니다.")
        break
    elif not(1 <= len(array) <= 100):
        print("배열의 길이가 범위를 벗어났습니다. ")
        break
    
solution(array)