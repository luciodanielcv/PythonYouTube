


print( "Exponent a number to a specific power" )

num = int( input( "Enter the base number: " ) )
pow = int( input( "Enter the power number: ") )

print ( num + pow )

def raise_to_power( num, pow ):
    result = 1
    for index in range( pow ):
        result = result * num
    return result



print( "Having " + str(num) + "raise to the power " + str(pow) +  " is: " + str( raise_to_power(num, pow ) ) )
