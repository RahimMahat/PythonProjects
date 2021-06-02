import random

def play():
    print("Let's play Rock,Paper,Scissors.......")
    user = input ("What's your choice: 'r' for rock, 'p' for paper, 's' for scissors : ")
    computer = random.choice(['r','p','s']) #random.choice will pick any of the given choice but for multiple choices you have to give them into
    print(f"The choice of computer is {computer}")

    if user == computer:
        return "It's a Tie"
    # r > s, s > p, p > r #here we set the rules in new function and call it in next line
    if is_win(user, computer): #This is equivalent to: if is_win(user,computer) == True:
        return 'You Won!'

    return 'You lost!'   #for saving the trouble of writing else we can directly write this is this statement can fit into else statement
def is_win(player, opponent):
    # return true if player wins
    #  we're gonna apply the rule: r > s, s > p, p > r
    if (player == 'r' and opponent =='s') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())