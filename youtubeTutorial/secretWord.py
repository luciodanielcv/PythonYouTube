

secret_word = "secret"
guess = ""
guessed = False
attempts = 1

while not(guessed) and attempts <= 3:
    print( "Attempt " + str( attempts ) )
    guess = input( "Enter the secret word: ")
    if secret_word.lower() == guess.lower():
        guessed = True
    attempts += 1

if guessed:
    print( "You win!")
else:
    print( "Game over!" )
