
import numpy as np

np.prime = []
np.prime1 = []
np.primetwin = []
np.primetwin1 = []
def find_primenumber(x):
    for i in range(2,x+1):
        np.prime.append(i)
    while True:
        try:
            latest = np.prime[0]
        except:
            break
        for t in np.prime:
            if t == np.prime[0]:
                np.prime1.append(t)
            if t % latest ==  0 :
                np.prime.remove(t)  
    return np.prime1


def find_primetwins(x):
    cool2 = 0
    fail = 0
    np.primetwin = find_primenumber(x)
    
    for i in np.primetwin:
        try:
            if i+2 == np.primetwin[cool2+1]:
                np.primetwin1.append(i)
                np.primetwin1.append(i+2)
                cool2 += 1
            else:
                cool2 += 1
                fail += 1
        except:
                return np.primetwin1


minus1 = 1           


def the_programm(x):
    minus1 = 1
    cool_loop = []      
    for i in range(1,x+1):
            loop = []
            loop.append(1)
            cool3 = True
            while cool3:
                
                while True:
                    if i%2 == 0:
                        i /= 2
                    else:
                        for z in loop:
                            if z == i:
                                cool_loop.append(i)
                                cool3 = False
                        loop.append(i)
                        break
                i *= 3
                i += minus1
                minus1 *= -1
                
                for z in loop:
                    if z == i:
                        cool_loop.append(i)
                        break
                loop.append(i)
    return cool_loop



def restore_loop(x):
    full_loop = []
    add = []
    minus1 = 1
    duplicate= []
    for v in range(80):
        while True:
            if x%2 == 0:
                x /= 2
                if x not in full_loop:
                    
                    full_loop.append(x)
            else:
                if x not in full_loop:
                    full_loop.append(x)
                break
        x *=3
        x += minus1
        minus1 *= -1
    

    for i in add:

        full_loop.append(i)
                       
    return full_loop

        
        
another_list = []
counter = 0   
list = the_programm(100)
jaj = find_primetwins(100)

for i in list:
    if i != 1:
        another_list.append(restore_loop(i))
        
for list1 in another_list:
    for i in list1:
        if i in jaj:
            counter += 1
            good = True
            break
        else:
            good = False
print (another_list)
print(good)
print (len(another_list))
print(counter)
          
            
        

            
