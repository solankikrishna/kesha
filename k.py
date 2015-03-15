num = 10
to_guess=True
while to_guess:
    guess=int(input("guess the number"))
    if guess==num:
        print("right")
        to_guess=False
    elif guess<num:
        print("lesser")
    else:
        print("larger")


