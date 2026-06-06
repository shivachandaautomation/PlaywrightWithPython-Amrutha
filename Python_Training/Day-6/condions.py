# Syntax of the if Statement
# if condition:
#     statement(s)  

marks = 90
if marks >= 90:
    print("Grade A")


# Syntax of the if-else Statement
# if condition: 
#    statement(s)
# else:
#    statement(s)

marks = 30
if marks < 40:
    print("Fail")    
else:
    print("Pass")

# # Syntax of the if-elif-else Statement
# if condition1:
#   statement(s)
# elif condition2:
#  statement(s)

marks = 45
if marks < 40:
    print("Fail") 
elif marks < 60:
    print("Grade C")
else:
    print("Grade A")

# 
# Syntax of the Nested if Statement
# if condition1:
#   statement(s)
# #   if condition2:
# #     statement(s)
#  
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
    if marks >= 80:
        print("Excellent")
else:
    print("Grade C")
         