from fonction import fac, exp

print("Welcome!")
print("This program calculates the total number of combinations ")
print("or arrangements possible considering your parameters,")
print("and the winning probability in a random draw.")

print(" ")

n = int(input("Write the total number of items: "))
while n < 0 : 
    print("The total cannot be negative")
    n = int(input("Write the total number of items: "))

k = int(input("Write the number of items to draw: "))
while k < 0 : 
    print("The number of items to draw cannot be negative")
    k = int(input("Write the number of items to draw: "))

repetition = int(input("Write 1 to get with repetition and 0 to get without repetition: "))
while repetition not in {0,1}:
    repetition = int(input("Please, enter 0 or 1: ")) 

order = int(input("Write 1 to consider the order and 0 to not consider the order: "))
while order not in {0,1}:
    order = int(input("Please, enter 0 or 1: "))

print(" ")

print("Your choices")
print("--------------------------------------")
print(f"{'The total number of items:':25} {n}")
print(f"{'The number of items drawn:':25} {k}")
if repetition == 0 : 
    print(f"{'Repetition:':25} NO")
else : 
    print(f"{'Repetition:':25} YES")

if order == 0 : 
    print(f"{'Order:':25} NO")
else : 
    print(f"{'Order:':25} YES")

print(" ")

if n == k and repetition == 0:
    print("Permutation")
    print("Formula : n! ")
elif order == 0:
    if repetition == 0:
        print("Combination without repetition")
        print("Formula : n! / (k! × (n-k)!)")
    else:
        print("Combination with repetition")
        print("Formula : (n+k-1)! / (k! × (n-1)!)")
else:
    if repetition == 0:
        print("Arrangement without repetition")
        print("Formula : n! / (n-k)!")
    else:
        print("Arrangement with repetition")
        print("Formula : n^k")



if k > n and repetition == 0:
    nb = 0  
else : 
    if repetition == 0 : 
        if order == 0 : 
            nb = fac(n) / (fac(k) * fac(n-k))
        else : 
            nb = fac(n) / fac(n-k)

    else : 
        if order == 0 :
            nb = fac(n+k-1) / (fac(k) * fac(n-1))
        else : 
            nb = exp(n,k) 

print(" ")

print("Results")
print("--------------------------------------")
if nb == 0:
    print("The total number of possibilities is 0")
    print("This scenario is impossible due to k > n without repetition")
else : 
    print(f"The total number of possibilities is {int(nb)}")
    print(f"And so, the winning probability is {1/nb:.8%}")