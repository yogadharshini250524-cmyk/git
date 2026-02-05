print("""  ____  _    _ ______  _____ _____   _______ _    _ ______ 
 / ___|| |  | |  ____|/ ____/ ____| |__   __| |  | |  ____|
| |  _ | |  | | |__  | (___| (___      | |  | |__| | |__   
| | |_|| |  | |  __|  \___ \\___ \     | |  |  __  |  __|  
| |__| | |__| | |____ ____) |___) |    | |  | |  | | |____ 
 \____| \____/|______|_____/_____/     |_|  |_|  |_|______|
              |__   __| |  | |  ____|                          
                 | |  | |__| | |__                             
                 | |  |  __  |  __|                            
                 | |  | |  | | |____                           
                 |_|  |_|  |_|______|                          
  _   _ _    _ __  __ ______ _____   ______ _____ 
 | \ | | |  | |  \/  |  ____|  __ \ / ____/ ____|
 |  \| | |  | | \  / | |__  | |__) | (___| (___  
 | . ` | |  | | |\/| |  __| |  _  / \___ \\___ \ 
 | |\  | |__| | |  | | |____| | \ \ ____) |___) |
 |_| \_|\____/|_|  |_|______|_|  \_\_____/_____/ 
Guess The Number Game!""")
def guessthenumber():
    import random
    chance=5
    number=random.randint(1,100)
    print("You have 5 chances to guess the number between 1 to 100")
    for i in range(chance):
        guess=int(input("Enter your guess: "))
        if guess<number:
            print("Your guess is too low")
        elif guess>number:
            print("Your guess is too high")
        else:
            print("Congratulations! You guessed the number correctly.")
            break
    else:
         print(f"Sorry, you've used all your chances. The correct number was {number}.")

while input("Do you want to play Guess The Number? (yes/no): ").lower() == "yes":
    guessthenumber()
else:
    print("Thank you for playing Guess The Number. Goodbye!")
    