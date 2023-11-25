## Mohsen Pourdehghan

print('Hi players, pick your favourite animal from blow, The player who chooses a more powerful animal wins')


print('L: Lion | D: Dog | C: Cat | E: Elephant | M: Mouse')


animList= ['l','d','c','e','m']
powerList= [4, 3, 2, 5, 1]


p1= input('"Player 1" select your animal: ')

while p1 != 'l' and p1 != 'd' and p1 != 'c' and p1 != 'e' and p1 != 'm' :
    p1= input('"Player 1" your input is not in the list! try again: ')
    
p2= input('"Player 2" select your animal: ')

while p2 != 'l' and p2 != 'd' and p2 != 'c' and p2 != 'e' and p2 != 'm' :
    p2= input('"Player 2" your input is not in the list! try again: ')

p3= input('"Player 3" select your animal: ')

while p3 != 'l' and p3 != 'd' and p3 != 'c' and p3 != 'e' and p3 != 'm' :
    p3= input('"Player 3" your input is not in the list! try again: ')


p1_score= 0
p2_score= 0
p3_score= 0



if p1 == 'e' :
    index = animList.index(p1)
    power = powerList[index]
    p1_score= power

elif p1 == 'l':
    index = animList.index(p1)
    power = powerList[index]
    p1_score= power

elif p1 == 'd':
    index = animList.index(p1)
    power = powerList[index]
    p1_score= power

elif p1 == 'c':
    index = animList.index(p1)
    power = powerList[index]
    p1_score= power
    
elif p1 == 'm':
    index = animList.index(p1)
    power = powerList[index]
    p1_score= power

else:
    print('your input is not in the list! try again')




if p2 == 'e' :
    index = animList.index(p2)
    power = powerList[index]
    p2_score= power

elif p2 == 'l':
    index = animList.index(p2)
    power = powerList[index]
    p2_score= power

elif p2 == 'd':
    index = animList.index(p2)
    power = powerList[index]
    p2_score= power

elif p2 == 'c':
    index = animList.index(p2)
    power = powerList[index]
    p2_score= power
    
elif p2 == 'm':
    index = animList.index(p2)
    power = powerList[index]
    p2_score= power




if p3 == 'e' :
    index = animList.index('e')
    power = powerList[index]
    p3_score= power


elif p3 == 'l':
    index = animList.index(p3)
    power = powerList[index]
    p3_score= power


elif p3 == 'd':
    index = animList.index(p3)
    power = powerList[index]
    p3_score= power


elif p3 == 'c':
    index = animList.index(p3)
    power = powerList[index]
    p3_score= power

    
elif p3 == 'm':
    index = animList.index(p3)
    power = powerList[index]
    p3_score= power




if p1_score == p2_score == p3_score:
    print('\n=== Draw! ===')

elif p1_score > p2_score and p1_score > p3_score :
    print('\n=== Player 1 is the winner, because his animal is stronger. ===')

elif p2_score > p1_score and p2_score > p3_score :
    print('\n=== Player 2 is the winner, because his animal is stronger. ===')

elif p3_score > p2_score and p3_score > p1_score :
    print('\n=== Player 3 is the winner, because his animal is stronger. ===')
