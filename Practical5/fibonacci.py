# set how mant numbers I want to get and the first two numbers 
nterms = 13
n1 = 1
n2 = 1
# count how many numbers I already have
count = 2
while count < nterms:
    nth = n1 + n2
# reset the number for the loop
    n1 = n2
    n2 = nth
    count += 1
# print the result
    print(nth)
