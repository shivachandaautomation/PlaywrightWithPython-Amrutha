# Python loops allow us to execute a statement or group of statements multiple times.
# for
# while
# for iterating_var in sequence:
#      statement(s)

# Example of a for loop
# for number in range(5):
#     print(number)

# statement = '''
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# '''
# for char in statement:
#    if char not in 'aeiou':
#       print (char, end='')

# numbers = (34,54,67,21,78,97,45,44,80,19)
# total = 0
# for num in numbers: 
#   print(total)
#   total += num
# print ("Total =", total)


# total = total + num  # total += num
# total = total - num  # total -= num
# total = total * num  # total *= num
# total = total / num  # total /= num
# total = total % num  # total %= num
# total = total ** num # total **= num


#  searches for prime numbers from 10 to 20.
#For loop to iterate between 10 to 20
# for num in range(10, 20):  
#    #For loop to iterate on the factors 
#    for i in range(2,num): 
#       #If statement to determine the first factor
#       if num%i == 0:      
#          #To calculate the second factor
#          j=num/i          
#          print ("%d equals %d * %d" % (num,i,j))
#          #To move to the next number
#          break 
#       else:                  
#          print (num, "is a prime number")
#          break


# for count in range(6):
#    print ("Iteration no. {}".format(count))
# else:
#    print ("for loop over. Now in else block")
# print ("End of for loop")

########################################################
# while expression:
#    statement(s)
# Example of a while loop
count = 0
while count < 5:
    print(count)
    # count += 1
