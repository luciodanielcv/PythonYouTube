

#Open the file
#Modifiers "r" for reading
#Modifiers "a" for append
employee_file = open( "employees.txt", "r" )

#Print and read the file
print( employee_file.readable() )

#I commented this .read() since it reads the whole file and moves
#the cursor to the EOF
#print( employee_file.read() )

#To read as an array use the method .readlinessssss()
#print( employee_file.readlines() )

for employee in employee_file.readlines():
    print( employee )

#print( employee_file.readline() )
#print( employee_file.readline() )

employee_file.close()

#Done!
print( "Done!")


