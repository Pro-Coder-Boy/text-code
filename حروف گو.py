#حروف بزرگ
captall_a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#حروف کوچک
small_a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
w=1
while(w==1):
    c_s = input("Do you want captall alphabet or small alphabet?")
    if(c_s=="captall"):
        n = int(input("Enter the number of alphabet: "))
        while(n<1)or(n>25):
            n = int(input("Enter the vaild number of alphabet: "))
        print(captall_a[n-1])
    elif(c_s=="small"):
        n = int(input("Enter the number of alphabet: "))
        while(n<1)or(n>25):
            n = int(input("Enter the vaild number of alphabet: "))
        print(small_a[n-1])
