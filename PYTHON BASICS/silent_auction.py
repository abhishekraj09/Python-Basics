import os
def find_winner(bidder_details):
    highest_bid=0
    winner=""
    for bidder in bidder_details:
        bidder_price=bidder_details[bidder]
        if  bidder_price>  highest_bid:
            highest_bid =bidder_price 
            winner=bidder
    print(f"here is the list of all the bidder: {bidder_details}")
    print(f"The  winner is {winner} with a bid price of { highest_bid}")

bidder_data={}
end_of_bidding= False
while not end_of_bidding:
    name = input( "what is ur name: ")
    price = int(input("what is ur bid: "))
    bidder_data[name] = price
    more_bidder=input("Are there more bidder? type 'yes' or 'no' :").lower()
    if more_bidder == 'no':
        end_of_bidding = True
        find_winner(bidder_data)
    elif more_bidder=='yes':
        os.system('cls')



