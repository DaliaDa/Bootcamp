#Fahrenheit To Celsius

fahrenheit = float(input("Please enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit, celsius))

#Celsius to Fahrenheit

celsius = float(input("Please enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))