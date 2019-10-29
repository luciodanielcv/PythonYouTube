

friends = [ "Luigui", "Jerry", "Davinci", "Karen", "Pet" ]

lucky_numbers = [ 4, 8, 15, 34, 3]

print( friends )
print( "One of my friends is " + friends[-1])

friends.append( "Pierre" )
friends.extend( lucky_numbers )


friends.insert( 1, "Kelly" )
print( friends )
