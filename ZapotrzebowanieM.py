# -*- coding: utf-8 -*-
print("Podaj płeć:(K/M)")
Plec = input()
if(Plec == 'm' or Plec == 'M'):
	S = 5
elif(Plec == 'k' or Plec == 'K'):
	S = -161
print("podaj wagę:")
Masa = input()
print("podaj wzrost:")
Wzrost = input()
print("podaj wiek:")
Wiek = input()
print("podaj aktywność")
Aktywnosc = input()
Zapotrzebowanie = (10*int(Masa)+6.25*int(Wzrost)-5*int(Wiek)+S)*float(Aktywnosc)
print("Twoje zapotrzebowanie to "+str(Zapotrzebowanie)+" kalorii")
