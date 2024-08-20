# 에러 코드 모음

## 1. 에러 코드: `ErrorCode1`
- **설명**: 에러 코드에 대한 간단한 설명
- **발생 원인**: 이 에러가 발생하는 이유를 기술
- **해결 방법**: 이 에러를 해결하는 방법 또는 예제 코드

```python
# 관련 코드 예시
if not variable:
    raise ValueError("Error occurred")

1. 에러 코드 

for i in array:
    if not(0 <= array <= 1000):
        print("배열의 값의 범위가 벗어났습니다.")
        break

** 설명 **  TypeError: '<=' not supported between instances of 'int' and 'list'

**발생 원인** : array가 리스트 로 지정되어 있었는데 '<=' 연산자는 리스트 의 값을 비교를 못하기 때문에 발생 

**해결 방법 ** : array 를 i 값으로 바꾸면 된다.

for i in array:
    if not(0 <= i <= 1000):
        print("배열의 값의 범위가 벗어났습니다.")
        break

2. 에러 코드 

elif i == array[i+1]:
    print("배열에 동일한 값이 존재 합니다.")
    break

** 설명 ** IndexError: list index out of range

** 발생 원인 ** : 리스트 안에 동일 값을 비교 하는 for 문을 돌리려고 하는데 마지막 인덱스 을 초과 해서 비교를 하기 때문에 이런 에러가 발생 

** 해결 방법 ** Python 에서 중복 리스트 를 없애고 싶으면 set 을 사용해 없애 버리자 

array =  [1,8,6]
array = set(array)
array = list(array)

3. 에러 코드 

answer.append(min,max)

** 설명 **  TypeError: list.append() takes exactly one argument (2 given)

** 발생 원인 ** : 리스트 안에 2개의 값을 바로 넣고 싶었는데 2개는 안된다는 오류 였다. 

** 해결 방법 ** 각각 1개씩 나눠서 넣어 줬다.

answer.append(min)
answer.append(max)