import random
loses=0
score=0
print('''
--------------------------------------
  Welcome To Rock Paper Scissor Game
--------------------------------------
''')
while True:
    a=input(">> Enter Your Guess or Quit: ")
    x=a.lower()
    if x=="quit":
        if score==0:
            a1="Times!"
        else:
            a1="Times!"
        print("\n Thanks for playing the Game. You Won",score,a1)
        exit()
    def rps_game(user,loses,score):
        output=["rock","paper","scissor"]
        if user not in output:
            print("\nEnter a valid guess")
        else:
            print("\n3..2..1.. GO")
            value=random.randint(0,2)
            print(output[value])
            if "rock"==x and "paper"==output[value]:
                print("Congratulations You won!!! \n")
                score+=1
            elif "paper"==x and "scissor"==output[value]:
                print("Congratulations You won!!! \n")
                score+=1
            elif "scissor"==x and "rock"==output[value]:
                print("Congratulations You won!!! \n")
                score+=1
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
            