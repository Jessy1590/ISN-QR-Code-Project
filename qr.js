a = prompt('Quel mot ?', '');
var c = document.getElementById('myCanvas');
var ctw = c.getContext('2d');
ctw.fillStyle = 'black';
function download_image() {
  var canvas = document.getElementById('myCanvas');
  canvas.toBlob(function (blob) {
	saveAs(blob, 'qrcode.png')
  }, 'image/png')
}
function f(x) {
  if (x == 0) {
	var x = 1;
	return x;
  } 
  else if (x == 1) {
	var x = 0;
	return x;
  }
}
var Y = [];
for (i = 0; i < a.length; i++) {
  var T = a[i]
  if (T.charCodeAt(0) >= 256) {
	alert('Un caractère inscris dans cet objet n\'est pas reconnu ! Le Qrcode n\'a pas pu se construire ! Merci de réessayer !');
	window.stop();
  }
  var W = T.charCodeAt(0);
  var M = W.toString(2);
  var L = M.split('')
  while (L.length <= 7) {
	L.unshift(0)
  }
  for (var j = 0; j <= 7; j++) {
	Y.push(L[j])
  }
}
var FORMAT = [1,1,0,1,1,1,0,0,0,0,0,1,0,0,0]
/* 	Mask 	1 = (row + column) mod 2 == 0                                    --> FORMAT = [1,1,0,1,1,1,0,0,0,0,0,1,0,0,0]
Mask 	0 = (row) mod 2 == 0                                                 --> FORMAT = [0,0,0,1,1,0,1,0,0,0,0,1,1,0,0]	
Mask	1 = (column) mod 3 == 0                                              --> FORMAT = [0,0,0,0,0,1,0,0,1,0,1,0,1,0,1]
Mask	3 = (row + column) mod 3 == 0                                        --> FORMAT = [0,0,0,0,1,1,1,0,1,1,0,0,0,1,0]
Mask	4 = (floor(row/2)+floor(column/3)) mod 2== 0                         --> FORMAT = [0,0,1,1,0,0,1,1,1,0,1,0,0,0,0]
Mask	5 = ((row * column) mod 2) + ((row * column) mod 3) == 0             --> FORMAT = [0,0,1,1,1,0,0,1,1,1,0,0,1,1,1]
Mask	6 = (((row*column) mod 2)+((row*column) mod 3)) mod 2 == 0           --> FORMAT = [0,0,1,0,0,1,1,1,0,1,1,1,1,1,0]
Mask	7 = (((row+column) mod 2)+((row*column) mod 3)) mod 2 == 0           --> FORMAT = [0,0,1,0,1,1,0,1,0,0,0,1,0,0,1]
*/
FORMAT.reverse()
var G = a.length;
var M = G.toString(2);
var L = M.split('')
while (L.length < 8) {
  L.unshift(0)
}
for (var j = 7; j >= 0; j--) {
  Y.unshift(L[j])
}
Depart = [0,1,0,0]
for (var j = 3; j >= 0; j--) {
  Y.unshift(Depart[j])
}
if (G==0){
	Y = []
}
while (Y.length <= 200) {
  Y.push(0);
}

var E = [0,0,0,0,0,0,0,1,FORMAT[0],1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,FORMAT[1],1,1,1,1,1,0,1,1,1,1,1,0,0,1,0,0,0,1,0,1,FORMAT[2],1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,FORMAT[3],1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,FORMAT[4],1,1,1,1,1,0,1,0,0,0,1,0,0,1,1,1,1,1,0,1,FORMAT[5],1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,FORMAT[6],1,1,1,1,1,1,1,1,1,1,1,1,FORMAT[14],FORMAT[13],FORMAT[12],FORMAT[11],FORMAT[10],FORMAT[9],0,FORMAT[8],FORMAT[7],1,1,1,1,FORMAT[7],FORMAT[6],FORMAT[5],FORMAT[4],FORMAT[3],FORMAT[2],FORMAT[1],FORMAT[0],1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,FORMAT[8],1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,FORMAT[9],1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,FORMAT[10],1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,FORMAT[11],1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,FORMAT[12],1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,FORMAT[13],1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,FORMAT[14],1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

for (var i = 0; i <= 441; i++) {
	  var x = i * 10;
	  var y = 0;
	  while (x > 209) {
		x = x - 210;
		y += 10;
	  }
	  if (f(E[i]) == 1) {
		ctw.fillRect(x, y, 10, 10)
	  }
	}
function MASK(x,y){
	if ((y/10)%2==0){
		return 1
	}
	else{
		return 0
	}
}
for (var w = 0; w <=300 ; w++) {
	var g = w%2
	var o = w
	if (0<=w && w<=22 && g==0){
		y = 200
		x = 200
		while(o!=0){
			y-=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (1<=w && w<=23 && g==1){
		x = 190
		y = 200
		while(o!=1){
			y-=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (24<=w && w<=46 && g==0){
		x = 180
		y = 90
		while(o!=24){
			y+=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (25<=w && w<=47 && g==1){
		x=170
		y = 90
		while(o!=25){
			y+=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (48<=w && w<=70 && g==0){
		x=160
		y = 200
		while(o!=48){
			y-=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (49<=w && w<=71 && g==1){
		x=150
		y = 200
		while(o!=49){
			y-=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (72<=w && w<=94 && g==0){
		x=140
		y = 90
		while(o!=72){
			y+=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (73<=w && w<=95 && g==1){
		x=130
		y = 90
		while(o!=73){
			y+=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (96<=w && w<=120 && g==0){
		x=120
		y = 200
		while(o!=96){
			y-=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (97<=w && w<=121 && g==1){
		x=110
		y = 200
		while(o!=97){
			y-=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (148<=w && w<=172 && g==0){
		x=100
		y = 80
		while(o!=148){
			y+=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (149<=w && w<=173 && g==1){
		x=90
		y = 80
		while(o!=149){
			y+=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (122<=w && w<=134 && g==0){
		x=120
		y = 50
		while(o!=122){
			y-=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (123<=w && w<=135 && g==1){
		x=110
		y = 50
		while(o!=123){
			y-=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (136<=w && w<=146 && g==0){
		x=100
		y = 0
		while(o!=136){
			y+=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (137<=w && w<=147 && g==1){
		x= 90
		y = 0
		while(o!=137){
			y+=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (174<=w && w<=180 && g==0){
		y = 120
		x = 80
		while(o!=174){
			y-=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (175<=w && w<=181 && g==1){
		x = 70
		y = 120
		while(o!=175){
			y-=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (182<=w && w<=188 && g==0){
		y = 90
		x = 50
		while(o!=182){
			y+=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (183<=w && w<=189 && g==1){
		x = 40
		y = 90
		while(o!=183){
			y+=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (190<=w && w<=196 && g==0){
		y = 120
		x = 30
		while(o!=190){
			y-=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (191<=w && w<=197 && g==1){
		x = 20
		y = 120
		while(o!=191){
			y-=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (198<=w && w<=204 && g==0){
		y = 90
		x = 10
		while(o!=198){
			y+=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else if (199<=w && w<=205 && g==1){
		x = 0
		y = 90
		while(o!=199){
			y+=10
			o-=2
		}
		if(MASK(x,y)==0){
			if (f(Y[w]) == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
		else {
			if (Y[w] == 0) {
				ctw.fillRect(x, y, 10, 10)
			}
		}
	}
	else{
		break;
	}
}