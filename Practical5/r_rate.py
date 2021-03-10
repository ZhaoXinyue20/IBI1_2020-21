# set some basic values
n1 = 84
count = 0
nterms = 5
# set r rate by users
print ("r is")
r = input()
# calculate
while count < nterms:
  nth = n1*(r+1)
  n1 = nth
  count += 1
print('r rate is', r ,'total patients are', nth)

