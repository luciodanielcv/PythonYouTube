


def translate( phrase ):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "G"    
            else: 
                translation += "g"
        else:
            translation += letter
    return translation

the_phrase = input( "Enter a phrase: ")

print( "Translation = " + translate( the_phrase ) )



