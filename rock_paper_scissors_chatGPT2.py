# حل اخر
import random

def play():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        # Get user input
        user_choice = input("Choose (rock, paper, scissors): ").strip().lower()

        # Validate input
        while user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            user_choice = input("Choose (rock, paper, scissors): ").strip().lower()

        # Get computer choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        # Display choices
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    play()
# ____________________________________________________________________________________________
import random  # استيراد مكتبة random لاستخدام الاختيار العشوائي

# دالة تشغيل اللعبة
def play():
    print("مرحبًا بك في لعبة حجر، ورقة، مقص!")

    while True:  # حلقة تكرار لتكرار اللعبة حتى يختار اللاعب الخروج
        # طلب إدخال من المستخدم
        user_choice = input("اختر (rock, paper, scissors): ").strip().lower()

        # التحقق من صحة الإدخال باستخدام حلقة تكرار
        while user_choice not in ['rock', 'paper', 'scissors']:
            print("خيار غير صالح، حاول مرة أخرى.")
            user_choice = input("اختر (rock, paper, scissors): ").strip().lower()

        # اختيار الكمبيوتر عشوائيًا
        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        # عرض اختيارات المستخدم والكمبيوتر
        print(f"اختيارك: {user_choice}")
        print(f"اختيار الكمبيوتر: {computer_choice}")

        # تحديد الفائز
        if user_choice == computer_choice:
            print("تعادل!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("أنت الفائز!")
        else:
            print("الكمبيوتر فاز!")

        # سؤال المستخدم إذا كان يريد اللعب مرة أخرى
        play_again = input("هل تريد اللعب مرة أخرى؟ (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("شكرًا للعب! إلى اللقاء.")
            break  # إنهاء الحلقة والخروج من اللعبة

# التأكد من تشغيل اللعبة فقط إذا تم تنفيذ الملف مباشرة
if __name__ == "__main__":
    play()

# #🧠 شرح عام للكود:

# الكود يبدأ بتحية اللاعب.

# يدخل المستخدم اختياره، ويُتحقّق من صحته.

# الكمبيوتر يختار بشكل عشوائي.

# يتم مقارنة الاختيارات لتحديد الفائز.

# تُعرض النتيجة على الشاشة.

# يتم سؤال المستخدم إذا كان يريد اللعب مرة أخرى.

# إذا أجاب بـ "yes"، تعاد الجولة.

# إذا كتب "no" أو أي شيء آخر، تنتهي اللعبة برسالة وداع.

# هل تودين أن نضيف عداد للنقاط أو واجهة رسومية بسيطة؟

