#사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분입니다. 사분면은 아래와 같이 1부터 4까지 번호를매깁니다.
# x 좌표와 y 좌표가 모두 양수이면 제1사분면에 속합니다.
# x 좌표가 음수, y 좌표가 양수이면 제2사분면에 속합니다.
# x 좌표와 y 좌표가 모두 음수이면 제3사분면에 속합니다.
# x 좌표가 양수, y 좌표가 음수이면 제4사분면에 속합니다.
# x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다. 좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수를 완성해주세요.
def solution(dot):
    answer = 0
    for i in dot:
        if not (-500 < dot[0] < 500)  or not (-500 < dot[1] < 500):
            print("범위를 벗어났습니다.")
            break
        elif dot[0] > 0 and dot[1] > 0:
            print("1사분면")
            answer = 1
            break
        elif dot[0] < 0 and dot[1] > 0:
            print("2사분면")
            answer = 2
            break
        elif dot[0] < 0 and dot[1] < 0:
            print("3사분면")
            answer = 3
            break
        elif dot[0] > 0 and dot[1] < 0:
            print("4사분면")
            answer = 4
            break
    return answer

num1 = int(input("x좌표를 입력해 주세요"))
num2 = int(input("y좌표를 입력해 주세요"))

dot = [num1, num2]
if len(dot) == 0:
    print("값을 넣어주세요")
else:
    solution(dot)