 
 
var x = 0;
var y = 12;
var z = 0;
 


function getRandomInt (min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function getRandomOpr(a){
  var b = "+";
  if (a != null){
   b = a;
  }
 
   return a; 
}

x = getRandomInt (x,y);
y = getRandomInt(x,y);


