# Get Input
s = raw_input('Number Limit')
n = int(s)

print "FizzBuzz counting up to {}".format(n)

def FizzBuzzLogic(num=100): #default n = 100
  if num % 3 == 0 and num % 5 == 0:   #mod 3 & 5 then "FizzBuzz""
    print "FizzBuzz"
  elif num % 5 == 0:   # mod 5 then "Buzz"
    print "Buzz"
  elif num % 3 == 0:   # mod 3 then "Fizz"
    print "Fizz"
  else:   # otherwise "num"
    print num

#Run loop from 1 to n
for number in range(1,n):
  FizzBuzzLogic(number)