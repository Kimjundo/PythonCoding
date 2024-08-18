#문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    total = 0
    current_number = ""
    
    for char in my_string:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                total += int(current_number)
                current_number = ""
    
    if current_number:
        total += int(current_number)
    
    return total

# 테스트
my_string = "aAb1B2cC34oOp"
result = solution(my_string)
print(f"'{my_string}'안의 모든 자연수들의 합: {result}")

