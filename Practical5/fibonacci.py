# inital settings
nterms = 13
n1 = 1
n2 = 1
count = 2
while count < nterms:
    nth = n1 + n2
# reset the number
    n1 = n2
    n2 = nth
    count += 1
    print(nth)
