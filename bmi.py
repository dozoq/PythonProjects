# -*- coding: utf-8 -*-
print("Wprowadź wzrost w metrach:")
wzrost = float(input())
print("Wprowadź wagę:")
waga = int(input())
bmi = waga/(wzrost**2)
print("Twoje BMI to: "+str(round(bmi,1)))
if(bmi > 40):
	print("Posiadasz otyłość 3 stopnia")
elif(bmi > 35):
	print("Posiadasz otyłość 2 stopnia")
elif(bmi > 30):
	print("Posiadasz otyłość 1 stopnia")
elif(bmi > 26.5):
	print("posiadasz nadwagę")
elif(bmi > 24):
	print("posiadasz lekką nadwagę")
elif(bmi > 18.5):
	print("posiadasz normalną wagę")
else:
	print("posiadasz niedowagę")
