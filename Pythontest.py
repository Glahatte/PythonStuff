Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name= input('Grayson')
print("welcome", name)
SyntaxError: multiple statements found while compiling a single statement
>>> name=input('grayson')
grayson
>>> print("Welcome", name)
Welcome 
>>> name=input('grayson')
grayson
>>> print("welcome", name"_
      
SyntaxError: EOL while scanning string literal
>>> print ('welcome', name)
welcome 
>>> while True:
  output = ""
  num = int(input("enter a integer: "))

  if num == 0:
    exit()

  for i in range(1, num+1):
    output += "{}".format(i)
    if i != num:
      output += "+"
  output += " = {}".format(sum(range(num+1)))
  print (output)

  
enter a integer: 5
1+2+3+4+5 = 15
enter a integer: 7
1+2+3+4+5+6+7 = 28
enter a integer: 100
1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19+20+21+22+23+24+25+26+27+28+29+30+31+32+33+34+35+36+37+38+39+40+41+42+43+44+45+46+47+48+49+50+51+52+53+54+55+56+57+58+59+60+61+62+63+64+65+66+67+68+69+70+71+72+73+74+75+76+77+78+79+80+81+82+83+84+85+86+87+88+89+90+91+92+93+94+95+96+97+98+99+100 = 5050
enter a integer:  
