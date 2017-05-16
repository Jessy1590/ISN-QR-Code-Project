#Auteur: Jessy Sengulen
#Thème : Script pour Qrcode Creator
#Version : 1.0
#Date de la dernière Mise à Jour : 21/03/2017


#Script avec indication :

#Initialisation
import sys
from PIL import Image
a = input("Bonjour ! Voici un programme permettant de coder un mot/phrase ou autre en Qrcode ! Ce programme a été réalisé par Jessy Sengulen. Vous êtes sur la version 1.0 datant du 21/03/2017. Pour commencer quel est le mot, phrase, numéro, texte ou autre à coder ? Attention : Celui-ci ne peux contenir que 19 caractères Unicode")

#Fonction pour le mask création Qr code
def f(x):
    if x==1:
        x=0
        return x
    elif x==0:
        x=1
        return x

#Transforme le mot en Binaire
C= list()
for i in range(0,len(a)):
    if ord(a[i])>=256:
        print("Un caractère inscris dans cet objet n'est pas reconnu ! Le Qrcode n'a pas pu se construire ! Merci de réessayer !")
        sys.exit(0)
    C.append(ord(a[i]))
G = len (a)



#Modifie le code pour que le format correspond
FORMAT= list()
if G<=19:
    if G<=8:
        FORMAT = [0,0,1,0,0,1,1,1,0,1,1,1,1,1,0]
        while G!=8:
            G = len (C)
            C.append(32)
        Q = "L"
    elif G<=12:
        FORMAT = [0,1,1,0,0,0,0,0,1,1,0,1,0,0,0]
        while G!=12:
            G = len (C)
            C.append(32)
        Q = "M"
    elif G<=15:
        FORMAT = [1,0,1,0,0,0,1,0,0,1,0,0,1,0,1]
        while G!=15:
            G = len (C)
            C.append(32)
        Q = "Q"
    elif G<=18:
        FORMAT = [1,1,1,0,0,1,0,1,1,1,1,0,0,1,1]
        while G!=18:
            G = len (C)
            C.append(32)
        Q = "H"
else:
    FORMAT = []


#Crée la liste du code en binaire et une liste pour le codeur et une pour le Qrcode
Y = list()
H = ""
for i in range(0,len(C)):
    if C[i]>=128:
        C[i] = C[i]-128
        Y.append(0)
        H = H + "0"
    else:
        Y.append(1)
        H = H + "1"
    if C[i]>=64:
        C[i] = C[i]-64
        Y.append(0)
        H = H + "0"
    else:
        Y.append(1)
        H = H + "1"
    if C[i]>=32:
        C[i] = C[i]-32
        Y.append(0)
        H = H + "0"
    else:
        Y.append(1)
        H = H + "1"
    if C[i]>16:
        C[i] = C[i]-16
        Y.append(0)
        H = H + "0"
    else:
        Y.append(1)
        H = H + "1"
    if C[i]>=8:
        C[i] = C[i]-8
        Y.append(0)
        H = H + "0"
    else:
        Y.append(1)
        H = H + "1"
    if C[i]>=4:
        C[i] = C[i]-4
        Y.append(0)
        H = H + "0"
    else:
        Y.append(1)
        H = H + "1"
    if C[i]>=2:
        C[i] = C[i]-2
        Y.append(0)
        H = H + "0"
    else:
        Y.append(1)
        H = H + "1"
    if C[i]>=1:
        C[i] = C[i]-1
        Y.append(0)
        H = H + "0"
    else:
        Y.append(1)
        H = H + "1"
    H = H + "//"



#Tag Longueur Qrcode
LONGEUR = list()
while G!=0:
    LONGEUR.append(G%2)
    G = int(G/2)
while len(LONGEUR)<8:
    LONGEUR.insert(0,0)
print(LONGEUR)
Y = Y + [0,0,0,0]
print(len(Y))
while len(Y)<=200:
    Y = Y + [1]


#Final réponse pour codeur
print("L'objet à coder est ",a," Son code est donc ",Y)
print("Version concaténer du code",H)
print(" Le Format du Qr code est donc ",FORMAT," La version du code d'erreur est donc ",Q," et le bouton depart est 0100 et le end est 0000")
print("Merci d'avoir utilisé notre programme ! Si vous désirez le code en version photo, merci d'entrer la fonction qrcode() ensuite celui-ci sera disponible au repertoire C de votre ordinateur")



#Préparation de l'image





#Fonction pour l'enregistrement de l'image Qrcode sur C:\Users\Public\Pictures\QRCODE.png
def qrcode():
    E = list()
    E = list()
    E = [0,0,0,0,0,0,0,1,FORMAT[0],f(Y[123]),f(Y[122]),f(Y[121]),f(Y[120]),1,0,0,0,0,0,0,0]
    E = E + [0,1,1,1,1,1,0,1,FORMAT[1],Y[125],Y[124],Y[119],Y[118],1,0,1,1,1,1,1,0]
    E = E + [0,1,0,0,0,1,0,1,FORMAT[2],f(Y[127]),f(Y[126]),f(Y[117]),f(Y[116]),1,0,1,0,0,0,1,0]
    E = E + [0,1,0,0,0,1,0,1,FORMAT[3],Y[129],Y[128],Y[115],Y[114],1,0,1,0,0,0,1,0]
    E = E + [0,1,0,0,0,1,0,1,FORMAT[4],f(Y[131]),f(Y[130]),f(Y[113]),f(Y[112]),1,0,1,0,0,0,1,0]
    E = E + [0,1,1,1,1,1,0,1,FORMAT[5],Y[133],Y[132],Y[111],Y[110],1,0,1,1,1,1,1,0]
    E = E + [0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0]
    E = E + [1,1,1,1,1,1,1,1,FORMAT[6],f(Y[109]),f(Y[108]),f(Y[83]),f(Y[84]),1,1,1,1,1,1,1,1]
    E = E + [FORMAT[14],FORMAT[13],FORMAT[12],FORMAT[11],FORMAT[10],FORMAT[9],0,FORMAT[8],FORMAT[7],1,1,1,1,FORMAT[7],FORMAT[6],FORMAT[5],FORMAT[4],FORMAT[3],FORMAT[2],FORMAT[1],FORMAT[0]]
    E = E + [f(Y[183]),f(Y[182]),f(Y[181]),f(Y[180]),f(Y[167]),f(Y[166]),0,f(Y[165]),f(Y[164]),f(Y[135]),f(Y[134]),f(Y[107]),f(Y[106]),f(Y[61]),f(Y[60]),f(Y[59]),f(Y[58]),f(Y[13]),f(Y[12]),f(Y[11]),f(Y[10])]
    E = E + [Y[195],Y[184],Y[179],Y[178],Y[169],Y[168],1,Y[163],Y[162],Y[137],Y[136],Y[105],Y[104],Y[63],Y[62],Y[57],Y[56],Y[15],Y[14],Y[9],Y[8]]
    E = E + [f(Y[187]),f(Y[186]),f(Y[177]),f(Y[176]),f(Y[171]),f(Y[170]),0,f(Y[161]),f(Y[160]),f(Y[139]),f(Y[138]),f(Y[103]),f(Y[102]),f(Y[65]),f(Y[64]),f(Y[55]),f(Y[54]),f(Y[17]),f(Y[16]),f(Y[7]),f(Y[6])]
    E = E + [Y[189],Y[188],Y[175],Y[174],Y[173],Y[172],1,Y[159],Y[158],Y[141],Y[140],Y[101],Y[100],Y[67],Y[66],Y[53],Y[52],Y[19],Y[18],Y[5],Y[4]]
    E = E + [1,1,1,1,1,1,1,1,0,f(Y[143]),f(Y[142]),f(Y[99]),f(Y[98]),f(Y[69]),f(Y[68]),f(Y[51]),f(Y[50]),f(Y[21]),f(Y[20]),f(Y[3]),f(Y[2])]
    E = E + [0,0,0,0,0,0,0,1,FORMAT[8],Y[145],Y[144],Y[97],Y[96],Y[71],Y[70],Y[49],Y[48],Y[23],Y[22],Y[1],Y[0]]
    E = E + [0,1,1,1,1,1,0,1,FORMAT[9],f(Y[147]),f(Y[146]),f(Y[95]),f(Y[94]),f(Y[73]),f(Y[72]),f(Y[47]),f(Y[46]),f(Y[25]),f(Y[24]),LONGEUR[7],LONGEUR[6]]
    E = E + [0,1,0,0,0,1,0,1,FORMAT[10],Y[149],Y[148],Y[93],Y[92],Y[75],Y[74],Y[45],Y[44],Y[27],Y[26],LONGEUR[5],LONGEUR[4]]
    E = E + [0,1,0,0,0,1,0,1,FORMAT[11],f(Y[151]),f(Y[150]),f(Y[91]),f(Y[90]),f(Y[77]),f(Y[76]),f(Y[43]),f(Y[42]),f(Y[29]),f(Y[28]),LONGEUR[3],LONGEUR[2]]
    E = E + [0,1,0,0,0,1,0,1,FORMAT[12],Y[153],Y[152],Y[89],Y[88],Y[79],Y[78],Y[41],Y[40],Y[31],Y[30],LONGEUR[1],LONGEUR[0]]
    E = E + [0,1,1,1,1,1,0,1,FORMAT[13],f(Y[155]),f(Y[154]),f(Y[87]),f(Y[86]),f(Y[81]),f(Y[80]),f(Y[39]),f(Y[38]),f(Y[33]),f(Y[32]),0,0]
    E = E + [0,0,0,0,0,0,0,1,FORMAT[14],Y[157],Y[156],Y[85],Y[84],Y[83],Y[82],Y[37],Y[36],Y[35],Y[34],1,0]
    imNew=Image.new("1",(21,21))
    imNew.putdata(E)
    imNew.save("D:\Programmation\Qrcode.png")
    
    
