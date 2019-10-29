

try:
    number = int( input("Enter an integer: " ) )
    print( "Number: " + str( number ) )
except ZeroDivisionError:
    print( "Divided by zero" )
except ValueError as err:
    print( err )
except:
    print( "Something wrong happened!" )




