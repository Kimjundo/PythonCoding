#영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    vowels = "aeiou"
    answer = ""
    ls = ""
    for char in my_string:
        if char not in vowels:
            answer += char
        else:
            ls += char
    print(f"{my_string} 에서  모음 {ls} 를 제거한 {answer} 를 retrun 합니다.")
    return answer

   
my_string = "bus"
if ( 1 <= len(my_string) <= 1000):
    solution(my_string)
else:
    print("문자열의 길이가 맞지 않습니다.")