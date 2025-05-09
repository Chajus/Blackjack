# Blackjack Program

import random

print("This is a black jack game. \nYou will be playing against a computer (also known as the dealer)\nHow much will you deposit")

print("1. $1")
print("2. $5")
print("3. $10")
print("4. $20")
print("5. $50")
print("6. $100")
print("7. To start playing")

money = 0

def deal_cards():
    cards = {2: 2, 3: 3, 4: 4, 5: 5, 6:6, 7:7, 8:8, 9:9, 10: 10, "J": 10, "Q": 10, "K": 10, "A": 11}
    return random.choice(list(cards.values()))

def calculate_total(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    
    return total

def play_blackjack():

    global money

    while money > 0:

        bet = int(input("How much will you like to bet? "))

        if bet > money:
            print("You cannot bet more than your current balance")
            continue
        
        money -= bet
        print(f"Your new balance is ${money}")

        player = [deal_cards(), deal_cards()]
        dealer = [deal_cards(), deal_cards()]

        print(f"Your cards: {player} (total: {sum(player)})")
        print(f"Dealer shows: {dealer[0]}")

        while calculate_total(player) < 21:
            choice = input("Hit or Stand? (H / S ): ")
            if choice.lower() == "h":
                player.append(deal_cards())
                print(f"Your cards: {player} (total: {sum(player)})")
                
            elif choice.lower() == "s":
                print(f"Player decided to stand. Players cards are {player}")
                break
            else:
                print("Invalid choice. Please enter H or S")

            if sum(player) > 21:
                print("Player busted. Dealer wins")
                return

        print()
        print(f"Dealer cards: {dealer} (total : {sum(dealer)})")

        while calculate_total(dealer) < 17:
            dealer.append(deal_cards())
            print(f"Dealer hits: {dealer} (total: {sum(dealer)})")

        player_total = sum(player)
        dealer_total = sum(dealer)

        if calculate_total == 21:
            print("Blackjack! You win!")
            money += bet * 2.5
            continue

        if dealer_total > 21:
            print("Dealer busted. You win")
            money += bet * 2
        elif dealer_total > player_total:
            print("Dealer wins. You lose your bet")
            continue
        elif dealer_total < player_total:
            print("Player wins.")
            money += bet * 2
        else:
            print("It's a tie. Return the bet")
            money += bet

        play_again = input("Do you want to play again? (Y / N): ")
        if play_again != "y":
            print("Thanks for playing.")
            break

while True:

    user = int(input("Enter an amount you'd like to deposit: "))

    if user == 1:
        print("You have deposited $1")
        money += 1
        print(f"Your total is ${money}")

    elif user == 2:
        print("You have deposited $5")
        money += 5
        print(f"Your total is ${money}")

    elif user == 3:
        print("You have deposited $10")
        money += 10
        print(f"Your total is ${money}")

    elif user == 4:
        print("You have deposited $20")
        money += 20
        print(f"Your total is ${money}")

    elif user == 5:
        print("You have deposited $50")
        money += 50
        print(f"Your total is ${money}")

    elif user == 6:
        print("You have deposited $100")
        money += 100
        print(f"Your total is ${money}")
    
    elif user == 7:
        if money == 0:
            print("You did not deposit any money")
        else:
            print(f"You are ready to play. Total amount deposited is ${money}")
            play_blackjack()
            break

    else:
        print("Invalid response. Try again")
        continue