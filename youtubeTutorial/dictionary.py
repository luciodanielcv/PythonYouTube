

monthConversion = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "Jun",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}


#Prints none
print( monthConversion.get("Luv" ) )

#Prints default value which is "Not a valid key"
print( monthConversion.get("Luv", "Not a valid key" ) )


