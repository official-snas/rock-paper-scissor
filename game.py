import random
loses=0
score=0
print('''
--------------------------------------
  Welcome To Rock Paper Scissor Game
--------------------------------------
''')
while True:
    a=input(">> Enter Your Guess(rock,paper,scissors,Quit): ")
    x=a.lower()
    if x=="quit":
        if score==0:
            a1="Times!"
        else:
            a1="Times!"
        print("\n Thanks for playing the Game. You Won",score,a1)
        exit()
    def rps_game(user,loses,score):
        output=["rock","paper","scissors"]
        if user not in output:
            print("\nEnter a valid guess")
        else:
            print("\n3..2..1.. GO")
            value=random.randint(0,2)
            print("Your guess =",user)
            print("The guess of the cpu =",output[value])
            if "paper"==x and "rock"==output[value]:
                print("Congratulations You won!!! \n")
                score+=1
            elif "scissors"==x and "paper"==output[value]:
                print("Congratulations You won!!! \n")
                score+=1
            elif "rock"==x and "scissors"==output[value]:
                print("Congratulations You won!!! \n")
                score+=1
            elif x==output[value]:
                print("Tie! Once more")
            else:
                if loses>0:
                    print("You lost again but don't give up keep trying!\n")
                else:
                    print("You lost \n")
                    loses+=1
        b=[loses,score]
        return b
    b=rps_game(x,loses,score)
    loses=b[0]
    score=b[1]
            