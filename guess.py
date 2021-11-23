import random 
def guess(x):
    n=x
    random_number=random.randint(1 ,n)
    guess=0
    while guess!=random_number:
        guess=int(input(f"guess the number between 1 and {x}"))
        if guess<random_number:
            print("sorry!!! guess again too low")
        elif guess>random_number:
            print("sorry!! guess again too high")

    print("yayyyy!!!!!! you guessed the number")
def computer_guess(x):  
    low=1
    high=x
    feedback=""
    while feedback!='c':
        guess=random.randint(low,high)
        feedback=input(f"id {guess} too high(h),too low (l) or correct (c)")
        if feedback=='h':
            high=guess-1
        elif feedback =='l':
            low=guess+1
    print(f"yayyyy!! computer guessed your number,{guess}")


computer_guess(10)
