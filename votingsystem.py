nominee1 = ("Enter name of first nominee1:")
nominee2 = ("Enter name of first nominee2:")

nm1_votes=0
nm2_votes=0

voter_id= [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)


while True:
    if voter_id == []:
        print("voting session is over")
        if nm1_votes>nm2_votes:
            percent=(nm1_votes/no_of_voter)*100
            print(nominee1,"has won the election with",percent,"% of votes")
            break
        
        elif nm2_votes>nm1_votes:
            percent=(nm2_votes/no_of_voter)*100
            print(nominee2,"has won the election with",percent,"% of votes")
            break
        else:
            print("Both have equal no of votes")
            break

    


    voter =int(input("Enter your voter_id: "))
    if voter in voter_id:
        print("You are a voter")
        voter_id.remove(voter)
        print("-----------------------------------")
        print("To give vote to",nominee1,"Press 1")
        print("To give vote to",nominee2,"Press 2")
        print("------------------------------------")
        vote =int(input("Enter ypu prvious vote: "))
        if vote == 1:
            nm1_votes +=1
            print(nominee1,"Thank you to your importnt vote")
        elif vote == 2:
            nm2_votes +=1
            print(nominee2,"Thank you to your importnt vote")
        elif vote > 2:
            print("Check your pressed key")
        else :
            print("You are not voter")