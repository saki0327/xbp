import random
choices ={"グー","",""}

print("")
print("0:グー、１：チョキ、２：パー")

while True:
    user_choice =int(input("あなたの選択を入力してください(0, 1, 2) : "))
    computer_choice = random.randint(0,2)

    print(f"あなた：{choices[user_choice]},コンピュータ: {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("引き分けです")
    elif (user_choice == 0 and computer_choice == 1) or \
        (user_choice == 1 and computer_choice == 2) or \
        (user_choice == 3 and computer_choice == 0):
        print ("あなたの勝ち")