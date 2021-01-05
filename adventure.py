import random
#Hero Classes
class warrior (object):
    health = 50
    strength = 10
    defence = 10
    magic = 1

class wizard (object):
    health = 125
    strength = 7
    defence = 7
    magic = 10

class elf (object):
    health = 100
    strength = 5
    defence = 10
    magic = 7

# Enemy Classes

class goblin (object):
    name = "Goblin"
    health = 20
    strength = 2
    defence = 2
    loot = random.randint(0,2)

class bat (object):
    name = "Bat"
    health = 10
    strength = 1
    defence = 3
    loot = random.randint(0,2)

class troll (object):
    name = "Troll"
    health = 30
    strength = 5
    defence = 1.5
    loot = random.randint(0,2)

class boss(object):
    name = "boss"
    health = 150
    strength = 50
    defence = 50
    
def gameOver(character, score):
    if character.health < 1:
        print("You have no health left")
        print("Thanks for playing...")
        print("You have scored...", score)
        
        writeScore(score)

        file=open("score.txt","r")

        for line in file:
            xline = line.split(",")
            print(xline[0], xline[1])

        exit()
        

def writeScore(score):
    file = open("score.txt","a")
    name = input("Type your name...")
    file.write(str(name))
    file.write(",")
    file.write(str(score))
    file.write(",")
    file.write("\n")
    file.close()


def heroselect():
    print ("Select your hero!")
    selection = input("1. Warrior \n2. Wizard \n3. Elf \n")
    if selection == "1":
        character = warrior
        print ("You have selected the warrior...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Magic - ", character.magic)
        return character

    elif selection == "2":
        character = wizard
        print ("You have selected the wizard...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Magic - ", character.magic)
        return character

    elif selection == "3":
        character = elf
        print ("You have selected the elf...These are their stats...")
        print ("Health - ", character.health)
        print ("Strength - ", character.strength)
        print ("Defence - ", character.defence)
        print ("Magic - ", character.magic)
        return character

    else:
        print("Only press 1, 2 or 3")
        heroselect()

def enemyselect(goblin,bat,troll):
    enemyList = [goblin,bat,troll]
    chance = random.randint(0,2)
    enemy = enemyList[chance]
    return enemy

def loot():
    loot = ["potion", "sword", "shield"]
    lootChance = random.randint(0,2)
    lootDrop = loot[lootChance]
    return lootDrop

def lootEffect(lootDrop, character):
    if lootDrop == "potion":
        character.health = character.health + 20
        print ("you drink the potion, increasing your health by 20!")
        print ("Your health is now", character.health)
        return character

    elif lootDrop == "sword":
        character.strength = character.strength + 2
        print ("you swap your sword for the newer, much sharper one!")
        print ("Your strength has been increased by 2")
        print ("your new strength is now", character.strength)
        return character

    elif lootDrop == "shield":
        character.defence = character.defence + 2
        print ("you swap your shield for the newer, much stronger one!")
        print ("Your defence has been increased by 2")
        print ("your new strength is now", character.defence)
        return character

    
    
def battlestate(score):
    enemy = enemyselect(goblin,bat,troll)
    print("a wild", enemy.name, "has appeared!")
    print ("you have 3 options...")
    while enemy.health > 0 :
        choice = input("1. Sword\n2. Magic \n3. RUN!")

        if choice == "1":
            print ("You swing your sword, attacking the", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                print ("You hit the enemy, their health is now....", enemy.health)

                if enemy.health > 1:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gameOver(character, score)
                    

                else:
                    if enemy.name == "Goblin":
                        enemy.health = 20
                        score = score + 10
                        

                    elif enemy.name == "Bat":
                        enemy.health = 10
                        score = score + 5
                        

                    elif enemy.name == "Troll":
                        enemy.health = 30
                        score = score + 15
                        

                    print ("You have defeated the", enemy.name)
                    print ("looks like it dropped something!")
                    lootDrop = loot()
                    print ("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return score
                    break
            else:
                print("Your sword slips from your grasp, you fumble and miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health - enemy.strength
                print("You now only have", character.health, "remaining")
                gameOver(character, score)


        elif choice == "2":
            print ("You cast a spell, attacking the", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.magic
                print ("You hit the enemy, their health is now....", enemy.health)

                if enemy.health > 0:
                    character.health = character.health - (enemy.strength / character.defence)
                    print ("The", enemy.name, "takes a swing, it hits you leaving", character.health)
                    gameOver(character, score)

                else:
                    if enemy.name == "Goblin":
                        enemy.health = 20
                        score = score + 10
                        

                    elif enemy.name == "Bat":
                        enemy.health = 10
                        score = score + 5
                        

                    elif enemy.name == "Troll":
                        enemy.health = 30
                        score = score + 15
                        

                    print ("You have defeated the", enemy.name)
                    print ("looks like it dropped something!")
                    lootDrop = loot()
                    print ("you got a", lootDrop)
                    lootEffect(lootDrop, character)
                    return score
                    break
            else:
                print("You slip when casting your spell, you fumble and miss!")
                print("The", enemy.name, "hits you for full damage")
                character.health = character.health - enemy.strength
                print("You now only have", character.health, "remaining")
                gameOver(character, score)


        elif choice == "3":
            print("you try to run....")
            runchance = random.randint(1,10)
            if runchance > 4:
                print ("you got away unscratched!")
                break
            else:
                print ("You try to run but slip and fall")
                print ("You try to defend but cannot, the enemy hits you for full damage...")
                character.health = character.health - enemy.strength
                print ("Your health is now", character.health)
                gameOver(character, score)

        else:
            print ("number not allowed, please only type 1, 2 or 3...")
        

def BossBattleState(score):
    enemy = boss
    



score = 0
character = heroselect()
score = battlestate(score)
print(score)
score = battlestate(score)
print(score)
score = battlestate(score)
print (score)
score = battlestate(score)
print(score)
score = battlestate(score)
print(score)
score = battlestate(score)
writeScore(score)
            
                        
                
                


    



    
