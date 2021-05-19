import random
w = 1
while w==1:
    print("")
    print("                     * * * * * * * * * * *")
    print("                     *                   *")
    print("                     *  Guess the number *")
    print("                     *                   *")
    print("                     * * * * * * * * * * *")
    mini = int(input("Enter a minimum: "))
    maxi = int(input("Enter a maximum: "))
    answer = random.choice(range(mini,maxi))
    if((maxi-mini)/20)!=int((maxi-mini)/20):
        loop = int((maxi-mini)/20)+1
    else:
        loop = int((maxi-mini)/20)
    print("You have",loop,"choice")
    print("Guess the number from",mini,"to",maxi)
    finish = 0
    while finish==0:
        for i in range(loop):
            guess = int(input())
            if (guess==answer):
                print("Hooray!! your answer is true")
                print("")
                print("                     * * * * * * * * * * *")
                print("                     *                   *")
                print("                     *     You win !!    *")
                print("                     *                   *")
                print("                     * * * * * * * * * * *")
                print("")
                finish=1
            elif(guess!=answer)&(loop>1):
                print("Your guess is wrong :( ")
                if(answer>guess):
                    print("The answer is greater than",guess)
                else :
                    print("The answer is lower than",guess)
                if(loop-1!=0):
                    loop = loop-1
                    print("You have",loop,"choice") 
            else:
                print("")
                print("                     * * * * * * * * * * *")
                print("                     *                   *")
                print("                     *     You lose !!   *")
                print("                     *                   *")
                print("                     * * * * * * * * * * *")
                print("")
                print("The answer is",answer)
                finish=1
            if(finish==1):
                retry = input("Do you want to retry? yes or no?")
                if(retry=="yes"):
                    w = 1
                elif(retry=="no") :
                    print("Goodbye!!")
                    w=0

