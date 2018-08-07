age = [55,55,55]
print("My age is {0}, {1}, or {2}.".format(age[0],age[1],age[2]))
print('My age is %d' % age[1])

for i in range(0,13):
    print("No. %2d squared is %4d and cubed is %6d" %(i,i**2,i**3))
print()

print("Pi is approx {0:50.50}".format(22/7))
print()

for i in range(0,13):
    print("No. {0:<2} squared is {1:<4} and cubed is {2:<6}".format(i,i**2,i**3))

for i in range(0,13):
    print("you can do it Finsam!")