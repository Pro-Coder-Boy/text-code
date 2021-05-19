from random import*
w = 1
guess = []
p = 0.
citiesother = ["newyork","mosqo","washington"]
citiesiran = ["alborz","ardebil","bushehr","azarbaijan","esfehan","fars","gilan","golestan","hamedan","hormozgan","ilam","kermanshah","kerman","khuzestan","kordestan","lorestan","markazi","mazandaran","khorasan","qazvin","qom","semnan","sistan","tehran","yazd","zanjan"]
while w==1:
    print("")
    print("                     * * * * * * * * * * * * *")
    print("                     *                          *")
    print("                     *    Guess the City     *")
    print("                     *                          *")
    print("                     * * * * * * * * * * * * *")
    retry = []
    country = input("the city of iran or other country?")
    while ((country!="iran") and (country!="other")):
        country = input("iran or other?")
    if (country=="iran"):
        answer = citiesiran[randint(0,len(citiesiran)-1)]
    elif (country=="other"):
        answer = citiesother[randint(0,len(citiesother)-1)]        
    for q in range(len(answer)):
        retry.append("_")
    loop = len(answer)
    while (loop!=0):
        print("You have",loop,"choice")
        print(retry)
        print("Guess one of the cities")
        guess = input()
        while (guess==""):
            guess = input()       
        if (guess==answer):
            print("Hooray!!")
            print("")
            print("                     * * * * * * * * * *  *")
            print("                     *                       *")
            print("                     *     You win !!      *")
            print("                     *                       *")
            print("                     * * * * * * * *  * * *")
            print("")
            break
        elif ((guess[0] in answer) and (len(guess)==1)):
            for k in range(len(retry)):
                if (answer[k]==guess):
                    retry[k] = guess
            loop = loop +1
            for o in range(len(retry)):
                if (retry[o] ==answer[o]):
                    p = p + 1
                else:
                    p = 0
                    break
            if (p==len(answer)):
                print(retry)
                print("Hooray!!")
                print("")
                print("                     * * * * * * * * * *  *")
                print("                     *                      *")
                print("                     *     You win !!     *")
                print("                     *                      *")
                print("                     * * * * * * * *  * * *")
                print("")
                break    
        elif ((guess[0]!=answer)or(guess!=answer)):
            print("Your guess is wrong :( ") 
        if (loop-1==0):
                print("")
                print("                     * * * * * * * * * * * *")
                print("                     *                       *")
                print("                     *      You lose !!     *")
                print("                     *                       *")
                print("                     * * * * * * * * * * * *")
                print("")
                print("The answer is",answer)
                break
        loop = loop - 1 
    tring = input("Do you want to retry? yes or no?")
    if (tring=="yes"):
        w = 1
    elif (tring=="no") :
        print("Goodbye!!")
        w=0

