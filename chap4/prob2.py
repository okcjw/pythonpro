import random

hero_hp = random.randrange(50,101)
monster_hp = random.randrange(50,101)
phase = 0

print("hero HP:", hero_hp, "monster HP:", monster_hp)    

while hero_hp > 0 and monster_hp > 0:
    hero_atk = random.randrange(-10,20)
    monster_atk =random.randrange(-10,20)
    
    if hero_atk <= 0 and monster_atk <= 0:
        print("hero(HP:" + str(hero_hp) + ", attack:" + str(hero_atk) + ") fail <-> monster(HP:" +str(monster_hp) + ", attack:" + str(monster_atk) + ") fail")

    elif hero_atk >= 0 and monster_atk <= 0:
        monster_hp -= hero_atk
        print("hero(HP:" + str(hero_hp) + ", attack:" + str(hero_atk) + ") success <-> monster(HP:" + str(monster_hp) + ", attack:" + str(monster_atk) + ") fail")
    
    elif hero_atk <= 0 and monster_atk >= 0:
        hero_hp -= monster_atk
        print("hero(HP:" + str(hero_hp) + ", attack:" + str(hero_atk) + ") fail <-> monster(HP:" + str(monster_hp) + ", attack:" + str(monster_atk) + ") success")
   
    elif hero_atk >= 0 and monster_atk >= 0:
        hero_hp -= monster_atk
        monster_hp -= hero_atk
        print("hero(HP:" + str(hero_hp) + ", attack:" + str(hero_atk) + ") success <-> monster(HP:" + str(monster_hp) + ", attack:" + str(monster_atk) + ") success")
   
    phase+=1

print("-------------------------------------------------------------------")
print("Total phase: " + str(phase) + ",")

if hero_hp > 0 :
    print("Hero Win!!!!")
if monster_hp > 0 :
    print("Monster Win!!!!")
