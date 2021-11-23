import random
def play():
    user=input("enter your choice R for rock P for paper S scissors\n")
    computer=random.choice(['r','p','s'])
    if user==computer:
        return "it's tie"
    if is_win(user,computer):
        return "you won!!!!!!!!!"
    return "you lost ^-^"
def is_win(player,opponent): #r>s,s>p,p>r
    if (player=='r' and opponent=='s')or (player=='s'and opponent=='p') or (player=='p' and opponent =='r'):
      return True

print(play())
