user_A= input("Choose one option among SNAKE, WATER AND GUN: ")
user_B=input("Choose one option among SNAKE, WATER AND GUN: ")

def game(A,B):
    A=A.lower()
    B=B.lower()
    valid_choices=["gun","snake","water"]
    if A not in valid_choices or B not in valid_choices:
        return "invalid input"

    if (A==B):
        winner="tie" 
    elif (A=="snake" and B=="water") or (A=="water" and B=="gun") or (B=="snake" and A=="gun"):
        winner=A
    else:
        winner=B
     
    return winner

result=game(user_A,user_B)
print(f" The result of this game is {result} ")
