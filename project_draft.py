import random
# game introduction
print("Welcome to CoinGame!")
print("Pick up good coins and skipping bad coins earn 10 points!")
print("Pick up bad coins and skipping good coins lose 5 points!")
 # press enter to pick up the coin
print("Press enter to continue.")

# when randomly output a coin, press "enter" to pick up and go through the next coin output
# press "backspace" to pass the coin, also go through the next coin


def badcoin():
    side = 3
    for i in range(3):
        for j in range(3):
            if(i == 0 or i == 2 or j == 0 or j == 2):
                print('*', end = ' ')
            else:
                print('X', end = ' ')
        print()

def goodcoin():
    side = 3
    for i in range(3):
        for j in range(3):
            if(i == 0 or i == 2 or j == 0 or j == 2):
                print('*', end = ' ')
            else:
                print('O', end = ' ')
        print()


user_choice = input()
times = 8
score = 0

for _ in range(times):
    pickup_choice = random.randint(0,1)
    if pickup_choice == 0:
        goodcoin()

        user_choice = input("Press a + enter to pick up the coin. Or, press enter to pass.")
        if user_choice == "a":
            score = score + 10 
        elif user_choice != "a":
            score = score - 5
            

    elif pickup_choice == 1:
        badcoin()
        user_choice = input("Press a + enter to pick up the coin. Or, press enter to pass.")
        if user_choice == "a":
            score = score - 5
        elif user_choice != "a":
            score = score + 10

print("----Game Over----")
print("Your score is: " + str(score))


# pick up coins

# socre records



