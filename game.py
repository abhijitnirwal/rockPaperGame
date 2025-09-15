import random

#print game headline 
print("\t\t\t ROCK-PAPER-SCISSOR GAME")

#taking user name input
print()
username = input("Enter your Name : ")
print()

#create variables to store match status
computer_winning = 0
user_winning = 0

# choose difficulty
mode = input("Choose difficulty (easy / moderate / hard): ").lower()
print()

# --- Difficulty functions ---
def easyPlay(user_move):
    return random.choice(['rock', 'paper', 'scissor'])

def moderatePlay(user_move):
    if random.random() < 0.3:
        if user_move == 'rock': return 'paper'
        elif user_move == 'paper': return 'scissor'
        else: return 'rock'
    else:
        return random.choice(['rock', 'paper', 'scissor'])

def hardPlay(user_move):
    if random.random() < 0.7:
        if user_move == 'rock': return 'paper'
        elif user_move == 'paper': return 'scissor'
        else: return 'rock'
    else:
        return random.choice(['rock', 'paper', 'scissor'])


# play again function
def playAgain():
    again = input("\nWanna play More (yes/no) : ").lower()
    if again in ['yes', 'y']:
        print()
        rockPaperScissor()
    elif again in ['no', 'n']:
        return
    else:
        print("Invalid Input")
        playAgain()

# main game function
def rockPaperScissor():
    options = ['rock', 'paper', 'scissor']
    
    global username
    global computer_winning
    global user_winning
    global mode

    print("Options:\n1. Rock\n2. Paper\n3. Scissor\n")

    user_move = input("Enter your move (name or number): ").lower().strip()
    print()

    # Allow numbers as input
    if user_move in ['1', 'rock']:
        user_move = 'rock'
    elif user_move in ['2', 'paper']:
        user_move = 'paper'
    elif user_move in ['3', 'scissor', 'scissors']:
        user_move = 'scissor'
    else:
        print("Invalid choice! Please try again.")
        rockPaperScissor()
        return

    # choose computer move based on difficulty
    if mode == "easy":
        computer = easyPlay(user_move)
    elif mode == "moderate":
        computer = moderatePlay(user_move)
    elif mode == "hard":
        computer = hardPlay(user_move)
    else:
        print("Invalid difficulty selected! Defaulting to easy.")
        computer = easyPlay(user_move)

    # Game logic
    if computer == user_move:
        print(f"Computer Move : {computer}")
        print("Match Tie")
    elif (user_move == 'rock' and computer == 'scissor') or \
         (user_move == 'paper' and computer == 'rock') or \
         (user_move == 'scissor' and computer == 'paper'):
        print(f"Computer Move : {computer}")
        print(f"{username} win")
        user_winning += 1
    else:
        print(f"Computer Move : {computer}")
        print("Computer win")
        computer_winning += 1

    playAgain()


# start game
rockPaperScissor()
print()

print("\t----Match Results----")
print()

print(f"Computer Winnings = {computer_winning}")
print(f"{username} Winnings = {user_winning}")

if computer_winning > user_winning:
    print("\nBetter Luck Next Time")
elif computer_winning == user_winning:
    print("\nBoth played Well")
else:
    print("\nWell Played")