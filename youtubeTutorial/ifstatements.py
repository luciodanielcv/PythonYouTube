

is_male = False
is_tall = True

if is_male and is_tall:
    print( "It is male and tall" )
elif is_male and not(is_tall):
        print( "It is male and not tall")
elif not(is_male) and is_tall:
    print( "It is not male but tall")
else:
    print( "Else statement")
    print( "It is female" )
print( "Always printed since it is not part of the if-else statement")


print( "End")

#Whatch out for the 'elif' instead of 'elseif'
