#Fahrenheit To Celsius

fahrenheit = int(input("Please enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))

#Celsius to Fahrenheit

celsius = int(input("Please enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))