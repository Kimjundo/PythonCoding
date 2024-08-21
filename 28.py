#알파벳으로 이루어진 문자열 myString이 주어집니다. 모든 알파벳을 소문자로 변환하여 return 하는 solution 함수를 완성해 주세요.

def solution(myString):
    answer = myString.lower()
    print(answer)
    return answer

def checklist(mystring):
    if 1<= len(mystring) <= 10000 or mystring.isalpha() == True:
        return True


myString ="aBcDeFg"

if checklist(myString):
    solution(myString)