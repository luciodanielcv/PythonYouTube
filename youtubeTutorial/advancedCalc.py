

firstNum = float( input( "Enter first number: " ) )
secondNum = float( input( "Enter second number: " ) )
op = input( "Enter the operator required: " )
result = "fail"

if op == "+":
    print( firstNum + secondNum )
    result = firstNum + secondNum
elif op == "-":
    print( firstNum - secondNum )
    result = firstNum - secondNum
elif op == "/":
    print( firstNum / secondNum )
    result = firstNum / secondNum
elif op == "*":
    print( firstNum * secondNum )
    result = firstNum * secondNum
else:
    print( "Invalid operation")

if not( result == "fail" ):
    print( "Operation requested was: (" + str(firstNum) + " " + op + " " + str(secondNum) + ") equals " + str(result ) ) 