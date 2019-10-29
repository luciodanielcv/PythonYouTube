

def max_num( num1, num2, num3 ):
    if( num1 >= num2 and num1 >= num3 ):
        print( str(num1) + " is the max number" )
    elif( num2 >= num1 and num2 >= num3 ):
        print( str(num2) + " is the max number" )
    elif( num3 >= num1 and num3 >= num2 ):
        print( str(num3) + " is the max number" )

print(max_num( 8, 3, 9) ) 

# Other comparison operators are !=, ==, <= 
# The same as in Java. 
# Remember the and, or and not are diferent jeje.

