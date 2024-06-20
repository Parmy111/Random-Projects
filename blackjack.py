import random
playerIn = True
dealerIn = True
#create deck of cards
#create player/dealer hand
#deal the cards
#check the total
#check for winner
winner = False
deckOfCards = [2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10, 2,3,4,5,6,7,8,9,10,
               "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A"]
playerHand = []
dealerHand = []
#deal the cards
def dealCards(turn):
    card = random.choice(deckOfCards)
    turn.append(card)
    deckOfCards.remove(card)
    
#check the total
def total(turn):
    total = 0
    face = ["J", "Q", "K"]
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total
#check for winner
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]
for _ in range(2):
    dealCards(playerHand)
    dealCards(dealerHand)
while playerIn or dealerIn:
    print(f"The dealer had {revealDealerHand()} and X")
    print(f"You have {playerHand} for a total of {total(playerHand)}")
    if playerIn:
        stayOrHit = input("1: Stay \n 2: Hit \n")
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCards(dealerHand)
    if stayOrHit == "1":
        playerIn = False
    else:
        dealCards(playerHand)
    if total(playerHand) >= 21:
        break
    if total(dealerHand) >= 21:
        break
if total(playerHand) == 21:
    print(f"You had {total(playerHand)} and the dealer had {total(dealerHand)}")
    print("YOU WIN YOU GOT BLACKJACK!!!")
elif total(playerHand) > 21:
    print(f"You had {total(playerHand)}")
    print("You lose and the dealer wins :(")
elif total(dealerHand) == 21:
    print(f"You had {total(playerHand)} and the dealer had {total(dealerHand)}")
    print("You lose and the dealer wins :(")
elif total(dealerHand) > 21:
    print(f"You had {total(playerHand)} and the dealer had {total(dealerHand)}")
    print("You WIN! and the dealer LOSES :D")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"You had {total(playerHand)} and the dealer had {total(dealerHand)}")
    print("You lose and the dealer wins :(")
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"You had {total(playerHand)} and the dealer had {total(dealerHand)}")
    print("You WIN! and the dealer LOSES :D")