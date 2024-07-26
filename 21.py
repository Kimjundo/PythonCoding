#개미 군단이 사냥을 나가려고 합니다. 개미군단은 사냥감의 체력에 딱 맞는 병력을 데리고 나가려고 합니다. 장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력을 가지고 있습니다. 
# 예를 들어 체력 23의 여치를 사냥하려고 할 때, 일개미 23마리를 데리고 가도 되지만, 장군개미 네 마리와 병정개미 한 마리를 데리고 간다면 더 적은 병력으로 사냥할 수 있습니다. 
# 사냥감의 체력 hp가 매개변수로 주어질 때, 사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지를 return하도록 solution 함수를 완성해주세요.
def solution(hp):
    mp = hp
    sum = 0
    count = 0
    count1 = 0
    count2 = 0
  
    for i in range(1,int(hp) + 1): 
        if mp <=0:
            break
        if  5  <= mp:
            mp -= 5
            count +=1
        elif 3<= mp <5:
            mp -= 3
            count1 +=1
        elif mp <3:
            mp -= 1
            count2 +=1
       
    sum = count + count1 + count2
    print(f"hp가 {hp} 이므로 , 장군 개미 {count}마리, 병정 개미 {count1} 마리, 일개미 {count2} 마일 로 사냥 할수 있습니다. 따라서 {sum} 을 리턴 합니다.") 
    return sum


hp = int(input("hp를 입력 하세요"))

if 0 <= hp <= 1000:
    solution(hp)
else:
    print("hp 범위를 잘못 입력 하셨습니다.")
  