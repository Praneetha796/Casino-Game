from coin_toss import coin_toss
from dice_game import dice_game
from guessing_game import guessing_game
from lottery import lottery
from password_generator import password_generator
from rock_paper_scissors import rock_paper_scissors
while True:
    print("\n ==== Quantum Casino===")
    print("1. coin_toss")
    print("2. dice_game")
    print("3. guessing_game")
    print("4. lottery")
    print("5. password_generator")
    print("6. rock_paper_scissors")
    print("7. Exit")

    choice=input("Enter your choice: ")   
    if choice=="1":
        coin_toss()
    elif choice=="2":
        dice_game()
    elif choice=="3":
        guessing_game()
    elif choice=="4":
        lottery()
    elif choice=="5":
        password_generator()
    elif choice=="6":
        rock_paper_scissors()
    elif choice=="7":
        print("Thanks for playing! ")  
        break 
    else:
        print("Wrong Choice")                     

