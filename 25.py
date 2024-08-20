#문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.
# https://codechacha.com/ko/python-lower-upper/ 참고 사이트 
def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    print(answer)
    return answer


my_string = "cccCCC" 

for i in my_string:
    if i == " ":
        print(" 공백 이 존재 합니다.")
    elif 1< len(my_string) <= 1000:
        solution(my_string)
        break

