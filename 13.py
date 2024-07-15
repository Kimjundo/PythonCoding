#머쓱이는 할머니께 생신 축하 편지를 쓰려고 합니다. 할머니가 보시기 편하도록 글자 한 자 한 자를 가로 2cm 크기로 적으려고 하며, 
#편지를 가로로만 적을 때, 축하 문구 message를 적기 위해 필요한 편지지의 최소 가로길이를 return 하도록 solution 함수를 완성해주세요.
def solution(message):
    count = 0   
    for i in message: 
        if (i.isalpha() == True) or i == " " or i == "!" or i == "~":
            count += 1
        else:
            print(f"{i}는 올바른 문자가 아닙니다.")
            return 0
            
    return print(message+f"의 글자수가 {count}개로 최소 가로 {count*2}cm 의 편지가 필요 합니다.")


message = "I love you~"

if  1<= len(message) <= 50:
    solution(message)
else:
    print("메세지의 길이가 너무 깁니다.")