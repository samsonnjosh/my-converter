from math import*


#####function  prompts the user to enter his/her name and says hi to them
def greet_user(name):
    
    print("\n Hello " + name.upper() + " !")##display te name in caps
name= input("\n Please input your name: ") ##get the name as input from the user
greet_user(name)

## asks the user to choose which operation they want to perform ##

operation= input("\n Choose the operation you wanna perform (reply with number 1,2,3,4 or 5) \n 1. metric convertion\n 2. Hours to seconds \n 3. Meters to kilometers \n 4. Distance to speed \n 5. gallon convertion\n \n Operation Number: ")
gradeError= 'Sorry ' + name.upper() + ', your input is Out of range!'
###### I use the IF statement to choose among the 5 operations to perform ######
if operation == "1":
    print ("\n METRIC CONVERSION\n")

types = {
    "k": 1000,
    "h": 100,
    "da": 10,
    "": 1,
    "d": 0.1,
    "c": 0.01,
    "m": 0.001
}

def convert(from_unit_type, to_unit_type, value):
    from_type_units = types[from_unit_type]
    to_type_units = types[to_unit_type]

    new_value = value * (from_type_units / to_type_units)
    print ("Welcome to Sam's Unit Converter")
    cat = input ("Which category would you like to convert? [k,m,h,dm,c]")

    unit1 = input ("Which unit would you like to convert from: ")
    unit2 = input ("Which unit would you like to convert to: ")
    num1 = input ("Enter your value: " )
    print(convert(unit1, unit2, float(num1)))

print("\n Thats all, " + name + ".")

if operation == "2":

    print('\nCONVERTING HOURS TO MINUTES\n')

    hours = float(input('Enter time in Hours: '))
    print( str(hours) + ' hrs = ' + str(hours*60) + ' minutes')
    print("\n Thats all, " + name + ".")

elif operation == "3":
    print('\nCONVERTING METERS TO KILOMETERS\n')

    meters = float(input('Enter length in Meters: '))
    print( str(meters) + 'm = ' + str(meters/1000) + ' kms')
    print("\n Thats all, " + name + ".")

elif operation == "4":
    print('\nCONVERTING DISTANCE TO SPEED\n')

    distance = float(input('Enter distance in kilometers: '))
    time = float(input('Enter time in hrs: '))
    
    print( 'speed used = ' + str(distance/time) + ' km/h')
    print("\n Thats all, " + name + ".")



elif operation == "5":
    print('\nCONVERTING GALLON TO LITRES\n')

    gallon = float(input('Enter  the number of gallons: '))
    
    print( 'litres used = ' + str(gallon*3.78) + 'l')
    print(convert(unit1, unit2, float(num1)))




    