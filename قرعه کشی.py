from random import*
name = ['Adam','Adrian','Alan','Alexander','Andrew','Anthony','Austin','Benjamin','Blake','Boris','Brandon','Brian','Cameron','Carl','Charles','Christian','Christopher','Colin','Connor','Dan','David','Dominic','Dylan','Edward','Eric','Evan','Frank','Gavin','Gordon','Harry','Ian','Isaac','Jack','Jacob','Jake','James','Jason','Joe','John','Jonathan','Joseph','Joshua','Julian','Justin','Keith','Kevin','Leonard','Liam','Lucas','Luke','Matt','Max','Michael','Nathan','Neil','Nicholas','Oliver','Owen','Paul','Peter','Phil','Piers','Richard','Robert','Ryan','Sam','Sean','Sebastian','Simon','Stephen','Steven','Stewart','Thomas','Tim','Trevor','Victor','Warren','William','Abigail','Alexandra','Alison','Amanda','Amelia','Amy','Andrea','Angela','Anna','Anne','Audrey','Ava','Bella','Bernadette','Carol','Caroline','Carolyn','Chloe','Claire','Deirdre','Diana','Diane','Donna','Dorothy','Elizabeth','Ella','Emily','Emma','Faith','Felicity','Fiona','Gabrielle','Grace','Hannah','Heather','Irene','Jan','Jane','Jasmine','Jennifer','Jessica','Joan','Joanne','Julia','Karen','Katherine','Kimberly','Kylie','Lauren','Leah','Lillian','Lily','Lisa','Madeleine','Maria','Mary','Megan','Melanie','Michelle','Molly','Natalie','Nicola','Olivia','Penelope','Pippa','Rachel','Rebecca','Rose','Ruth','Sally','Samantha','Sarah','Sonia','Sophie','Stephanie','Sue','Theresa','Tracey','Una','Vanessa','Victoria','Virginia','Wanda','Wendy','Yvonne','Zoe']
winner = []
j = -1
for i in name:
    j = j+1
print(j,"people registered")
for i in range(3):
    r = randint(0,j)
    winner.append(name[r])
print("******************************")
print("Winner are",winner[0],winner[1],winner[2],".")
print("******************************")
