#머쓱이는 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 2022년 기준 선생님의 나이 age가 주어질 때, 선생님의 출생 연도를 return 하는 solution 함수를 완성해주세요
def solution(age):
    year = 2022 
    answer = ( year - age) + 1
    print("2022년 기준 "+str(age)+"살 이므로 "+str(answer)+"년생 입니다.")
    return answer

age = int(input("나이를 입력해 주세요"))
if 0 < age < 120:
    print(solution(age))
else:
    print("0~120세 정도의 나이만 입력해 주세요")
