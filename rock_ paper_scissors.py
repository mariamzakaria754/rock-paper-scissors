### Requirments

# start the game
# Ask the player to make a move (R, P, S)
# PC would select a move randomly
# PC == player -> tie
# (player == P and PC == Rock ) or (player == R and PC == Scissors ) or (player ==S and PC == Paper)
## User won/ you win
# Any other case 
## PC lose/ you lose
import random;

print("start the game")

user =input("What will you choose? 'r' for Rock , 'p' for Paper, or 's' for Scissors \n ?")

PC = random.choice(['r', 'p', 's'])

print("User Played : " + user)

print("PC Played : " + PC)

if PC == user :
    print(" It's a tie !")
    
elif ( user == 'P' and PC == 'r' ) or ( user == 'r'and PC == 's' ) or ( user == 's' and PC == 'p' ) :
    print("you win! ")

else:
    print("you lose! ")
#_________________________________________________________________________________________________    
#i want this documentation  in this code 
import random

# بداية اللعبة
print("start the game")

# طلب من اللاعب اختيار بين الحجر (r) أو الورقة (p) أو المقص (s)
user = input("What will you choose? 'r' for Rock , 'p' for Paper, or 's' for Scissors \n ?")

# الكمبيوتر يختار عشوائيًا بين الحجر، الورقة أو المقص
PC = random.choice(['r', 'p', 's'])

# عرض ما اختاره اللاعب
print("User Played : " + user)

# عرض ما اختاره الكمبيوتر
print("PC Played : " + PC)

# تحقق إذا كان الاختيارين متساويين (تعادل)
if PC == user:
    print("It's a tie!")  # إذا كان التعادل بين اللاعب والكمبيوتر
    
# تحقق إذا كان اللاعب فاز بناءً على القواعد:
#  - الحجر يهزم المقص
#  - المقص يهزم الورقة
#  - الورقة تهزم الحجر
elif (user == 'p' and PC == 'r') or (user == 'r' and PC == 's') or (user == 's' and PC == 'p'):
    print("you win!")  # إذا فاز اللاعب

# إذا كانت أي من الحالات السابقة غير صحيحة، فهذا يعني أن الكمبيوتر فاز
else:
    print("you lose!")  # إذا خسر اللاعب
