import time
from PIL import Image
from random import *
pic=Image.open ("C:\\Users\\Sengulen Jessy\\Documents\\Application\\QRcode.png")
picn=Image.open ("C:\\Users\\Sengulen Jessy\\Documents\\Application\\QRcode.png")
L=21
h=21
M1=pic.getpixel((2,8))
M2=pic.getpixel((3,8))
M3=pic.getpixel((4,8))
E1=pic.getpixel((8,19))
E2=pic.getpixel((8,20))
E1=E1[0]
E2=E2[0]
if E1==255 and E2==255 :
      EC_LVL="H"
      Damage_max="30%"
if E1==255 and E2==0 :
      Damage_max="25%"
      EC_LVL="Q"
if E1==0 and E2==255 :
      Damage_max="15"
      EC_LVL="M"
if E1==0 and E2==0 :
      EC_LVL="L"
      Damage_max="7%"
print ("Mask type=",M1[0],M2[0],M3[0])
print ("Error correction level",EC_LVL,"Max Damage readable :",Damage_max)
if M1[0] == 0 and M2[0] == 0 and M3[0] == 0 :
      print ("Mask 1 Detected")
if M1[0] == 0 and M2[0] == 0 and M3[0] == 255 :
      print ("Mask 2 Detected")
if M1[0] == 0 and M2[0] == 255 and M3[0] == 0 :
      print ("Mask 3 Detected")
if M1[0] == 0 and M2[0] == 255 and M3[0] == 255 :
      print ("Mask 4 Detected")
if M1[0] == 255 and M2[0] == 0 and M3[0] == 0 :
      print ("Mask 5 Detected")
if M1[0] == 255 and M2[0] == 0 and M3[0] == 255 :
      print ("Mask 6 Detected")
if M1[0] == 255 and M2[0] == 255 and M3[0] == 0 :
      print ("Mask 7 Detected")
if M1[0] == 255 and M2[0] == 255 and M3[0] == 255 :
      print ("Mask 8 Detected")
for y in range (6):
      for x in range (4):
            X=x+9
            Y=y
            if M1[0] == 0 and M2[0] == 0 and M3[0] == 0 :
                  if X%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((x+9,y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 0 and M3[0] == 255 :
                  if (X+Y)%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((x+9,y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 255 and M3[0] == 0 :
                  if (X+Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((x+9,y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 255 and M3[0] == 255 :
                  if Y%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((x+9,y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 0 and M3[0] == 0 :
                  if ((X*Y)%3+X*Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((x+9,y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 255 and M3[0] == 0 :
                  if (Y/2+X/3)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((x+9,y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 0 and M3[0] == 255 :
                  if ((X*Y)%3+X+Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((x+9,y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 255 and M3[0] == 255 :
                  if (X*Y)%2+(X*Y)%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((x+9,y),(color,color,color,255))
                        
for y in range (2):
      for x in range (4):
            X=x+9
            Y=y+7
            if M1[0] == 0 and M2[0] == 0 and M3[0] == 0 :
                  if X%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 0 and M3[0] == 255 :
                  if (X+Y)%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 255 and M3[0] == 0 :
                  if (X+Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 255 and M3[0] == 255 :
                  if Y%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 0 and M3[0] == 0 :
                  if ((X*Y)%3+X*Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 255 and M3[0] == 0 :
                  if (Y/2+X/3)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 0 and M3[0] == 255 :
                  if ((X*Y)%3+X+Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 255 and M3[0] == 255 :
                  if (X*Y)%2+(X*Y)%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))

for y in range (4):
      for x in range (6):
            X=x+0
            Y=y+9
            if M1[0] == 0 and M2[0] == 0 and M3[0] == 0 :
                  if X%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 0 and M3[0] == 255 :
                  if (X+Y)%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 255 and M3[0] == 0 :
                  if (X+Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 255 and M3[0] == 255 :
                  if Y%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 0 and M3[0] == 0 :
                  if ((X*Y)%3+X*Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 255 and M3[0] == 0 :
                  if (Y/2+X/3)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 0 and M3[0] == 255 :
                  if ((X*Y)%3+X+Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 255 and M3[0] == 255 :
                  if (X*Y)%2+(X*Y)%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))

for y in range (4):
      for x in range (14):
            X=x+7
            Y=y+9
            if M1[0] == 0 and M2[0] == 0 and M3[0] == 0 :
                  if X%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 0 and M3[0] == 255 :
                  if (X+Y)%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 255 and M3[0] == 0 :
                  if (X+Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 255 and M3[0] == 255 :
                  if Y%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 0 and M3[0] == 0 :
                  if ((X*Y)%3+X*Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 255 and M3[0] == 0 :
                  if (Y/2+X/3)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 0 and M3[0] == 255 :
                  if ((X*Y)%3+X+Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 255 and M3[0] == 255 :
                  if (X*Y)%2+(X*Y)%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))

for y in range (8):
      for x in range (12):
            X=x+9
            Y=y+13
            if M1[0] == 0 and M2[0] == 0 and M3[0] == 0 :
                  if X%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 0 and M3[0] == 255 :
                  if (X+Y)%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 255 and M3[0] == 0 :
                  if (X+Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 255 and M3[0] == 255 :
                  if Y%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 0 and M3[0] == 0 :
                  if ((X*Y)%3+X*Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 255 and M3[0] == 0 :
                  if (Y/2+X/3)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 0 and M3[0] == 255 :
                  if ((X*Y)%3+X+Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 255 and M3[0] == 255 :
                  if (X*Y)%2+(X*Y)%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))

for y in range (6):
      for x in range (2):
            X=x+9
            Y=y+13
            if M1[0] == 0 and M2[0] == 0 and M3[0] == 0 :
                  if X%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 0 and M3[0] == 255 :
                  if (X+Y)%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 255 and M3[0] == 0 :
                  if (X+Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 0 and M2[0] == 255 and M3[0] == 255 :
                  if Y%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 0 and M3[0] == 0 :
                  if ((X*Y)%3+X*Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 255 and M3[0] == 0 :
                  if (Y/2+X/3)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 0 and M3[0] == 255 :
                  if ((X*Y)%3+X+Y)%2==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
            if M1[0] == 255 and M2[0] == 255 and M3[0] == 255 :
                  if (X*Y)%2+(X*Y)%3==0 :
                        Pix=pic.getpixel((X,Y))
                        color=((Pix[0]%2)*-1+1)*255
                        picn.putpixel((X,Y),(color,color,color,255))
print ("Mask removed")
picn.save("C:\\Users\\Sengulen Jessy\\Documents\\Application\\No mask.png")
EnCode=[]
for y in range (2,0,-1):
      for x in range (2,0,-1):
            Lpix=picn.getpixel((x+18,y+18))
            Vpix=((Lpix[0]%2)*-1+1)
            EnCode.append(Vpix)
            if EnCode==[0,1,0,0] :
                  code="Byte -> Readable"
            else :
                  code="Unreadable"
print ("Encoding type :",EnCode,": Mode =",code)

Lenght=0
Case=128
LenghtCode=[]
for y in range (4,0,-1):
      for x in range (2,0,-1):
            Lpix=picn.getpixel((x+18,y+14))
            Vpix=((Lpix[0]%2)*-1+1)
            LenghtCode.append(Vpix)
            Lenght+=int(Vpix*Case)
            Case/=2
print ("LenghtCode",LenghtCode,": Lenght =",Lenght)
CaractereCode=[]
CaractereN=0
sens=-1
y=15
X=19
TxtList=""
for pos in range (Lenght) :
      Case=128
      CaractereN=0
      for Haut in range (0,4):
            y=y+sens
            X+=2
            for long in range (2,0,-1) :
                  X+=-1
                  if X>=14 and y==8 :
                        X+=-2
                        y+=1
                        sens=1
                  if (X<14 and X>8) and y==6 :
                        y+=sens
                  if y==21 :
                        X+=-2
                        y+=-1
                        sens=-1
                  if y==-1 :
                        X+=-2
                        y+=1
                        sens=1
                  Lpix=picn.getpixel((X,y))
                  Vpix=((Lpix[0]%2)*-1+1)
                  CaractereCode.append(Vpix)
                  CaractereN+=int(Vpix*Case)
                  Case/=2
                  picn.putpixel((X,y),(255,0,0,255))
      TxtList+=(chr(CaractereN))
for Haut in range (0,2):
      y=y+sens
      X+=2
      for long in range (2,0,-1) :
            X+=-1
            if X>=14 and y==8 :
                  X+=-2
                  y+=1
                  sens=1
            if (X<14 and X>8) and y==6 :
                  y+=sens
            if y==21 :
                  X+=-2
                  y+=-1
                  sens=-1
            if y==-1 :
                  X+=-2
                  y+=1
                  sens=1
            Lpix=picn.getpixel((X,y))
            Vpix=((Lpix[0]%2)*-1+1)
            CaractereCode.append(Vpix)
            Case/=2
            picn.putpixel((X,y),(255,0,0,255))
if CaractereCode!=[0,0,0,0]:
      print ("error end")
picn.save("C:\\Users\\Sengulen Jessy\\Documents\\Application\\net.png")
print ("saved")
print (TxtList)




picn.putpixel((X,y),(255,0,0,255))
picn.save("C:\\Users\\Sengulen Jessy\\Documents\\Application\\net.png")
time.sleep(0.4)
