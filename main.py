celsiusTemp = input("Enter your temperature in Celsius: \n")
nctemp = int(celsiusTemp) * 9
ncbftemp = int(nctemp)/5
fTemp = ncbftemp + 32
print("The temperature in degree fahrenheit is " + str(fTemp) + "°F")