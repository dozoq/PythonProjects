# -*- coding: utf-8 -*-
import random

End = False
while(End != True):
	print(u"Witamy w menu, wybierz jedną z opcji: \n 1.Gramy! \n 2.Wyjdź z gry")
	Choice = int(input())
	if(Choice == 1):
		MagicNumber = int(random.random() * 500)
		Guess = 0
		while(Guess != MagicNumber):
			print(u"ustrzel magiczną liczbę(0-500)!:")
			Guess = int(input())
			if(Guess == MagicNumber):
				print(u"Brawo! Strzał w dziesiątkę! to właśnie liczba "+str(MagicNumber))
			elif(Guess > MagicNumber):
				print(u"Nie Tak daleko kowboju!")
			elif(Guess < MagicNumber):
				print(u"Trochę więcej wiary!")
	if(Choice == 2):
		End = True
	