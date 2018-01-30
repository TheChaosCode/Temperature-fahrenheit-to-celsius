print "This program converts degrees Fahrenheit to Celsius or vice versa."
loop=1
while loop==1:
    option=raw_input("For converting from degrees Fahrenheit to Celcius, type 1. For converting Celcius to Fahrenheit, type 2. Then hit enter.")

    if option=="1":
        tempf = input("Enter temperature in Fahrenheit: ")
        tempc = (tempf - 32.)*5./9.
        print tempf, "degrees Fahrenheit is", tempc, "degrees Celcius."
        encore=raw_input("Would you like to perform another conversion? If yes, type y and hit enter: ")
        if encore=='y':
            loop=1
        else:
            loop=0

    elif option=="2":
        tempc = input("Enter temperature in Celsius: ")
        tempf = (tempc*9./5.)+32.
        print tempc, "degrees Celcius is", tempf, "degrees Fahrenheit."
        encore=raw_input("Would you like to perform another conversion? If yes, type y and hit enter: ")
        if encore=='y':
            loop=1
        else:
            loop=0

    else:
        print "Wrong input given."
        loop=1

print "Thank you for using this program. Have a nice day."
