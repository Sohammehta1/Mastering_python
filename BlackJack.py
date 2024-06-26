import random 

cards  = {}

for i in range(2,12):
    cards[i]=4
# print(cards)

def dealCard()->int:
    
    while True:
        card = random.randint(2,11)
        if cards[card]!=0:
            cards[card]-=1
            return card

def play_game():
    user_cards, comp_cards = [], []
    user_sum, comp_sum = 0, 0

    for _ in range(2):
        user_cards.append(dealCard())
        if sum(user_cards) == 22:
            user_cards[1] = 1

    user_sum = sum(user_cards)
    print(f"Your cards are: {user_cards} and your sum is {user_sum}")

    for _ in range(2):
        comp_cards.append(dealCard())

    comp_sum = sum(comp_cards)
    print(f"Dealer's latest card is: {comp_cards[1]}")

    while True:
        choice = input("What would you like to do (h)it/(s)tand: ").lower()
        if choice == 'h':
            user_cards.append(dealCard())
            user_sum = sum(user_cards)
            if user_sum > 21:
                ace_found = False
                for i in range(len(user_cards)):
                    if user_cards[i] == 11:
                        user_cards[i] = 1
                        ace_found = True
                        break
                if not ace_found:
                    print(f"Player sum exceeds 21({user_sum}), Dealer wins")
                    print(f"Dealer's cards: {comp_cards}")
                    return
            print(f"Your cards: {user_cards}")
            print(f"Your sum is: {user_sum}")
        else:
            if user_sum == 21:
                print(f"Since user sum is 21, user wins automatically")
                print(f"Dealer's cards: {comp_cards}")
                return

            while comp_sum < 17:
                comp_cards.append(dealCard())
                comp_sum = sum(comp_cards)

            if comp_sum > 21:
                ace_found = False
                for i in range(len(comp_cards)):
                    if comp_cards[i] == 11:
                        comp_cards[i] = 1
                        ace_found = True
                        break
                if not ace_found:
                    print(f"Dealer's sum exceeds 21({comp_sum}), player wins")
                    print(f"Dealer's cards: {comp_cards}")
                    return

            if comp_sum > user_sum:
                print(f"Dealer's sum is greater than player's sum: {comp_sum} > {user_sum}")
                print(f"Dealer's cards: {comp_cards}")
                return

            if comp_sum < user_sum:
                print(f"Player's sum is greater than dealer's sum: {user_sum} > {comp_sum}")
                print(f"Dealer's cards: {comp_cards}")
                return

            print("It's a tie!")
            return

    return


                                       

    return

choice = 'y'
while choice == 'y':
    choice  = input("Would you like to play a game of black jack y/n : ")
    if choice =='y':
        play_game()
    