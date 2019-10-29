
#Open the file
#Modifiers "r" for reading
#Modifiers "a" for append
# Modifier "w" overwrites or creates a new file
employee_file = open( "employees.txt", "r+" )

#Print and read the file
employee_file.write( "\nThomas - HR" )
employee_file.write( "\nDave - Trainings" )

#print( employee_file.readable() )

employee_file.close()

#Done!
print( "Done!")


