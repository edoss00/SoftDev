// Elizabeth Doss
// SoftDev1 pd1
// K08 -- What is it saving the screen from?
// 2020-02-13

var startButton = document.getElementById('start');
var stopButton = document.getElementById('stop');
var movie = document.getElementById('dvd');
var canv= document.getElementById('canvas');
var contx=canv.getContext('2d');

//animate
var r = 10;
var i = true;
var ani;

//bounce
var logo = new Image()
logo.src = "dvd.jpg"
var x = Math.floor(Math.random()*350);
var y = Math.floor(Math.random()*450);
var dx = 1;
var dy = 1;
var ani2;
var running = false;

contx.strokeRect(0,0,600,600);
startButton.addEventListener('click',animate);
stopButton.addEventListener('click',stop);
movie.addEventListener('click',startBounce);

function stop(){
  window.cancelAnimationFrame(ani);
  window.cancelAnimationFrame(ani2);
  x = Math.floor(Math.random()*350);
  y = Math.floor(Math.random()*450);
  dx = 1;
  dy = 1;
}

function animate(){
    window.cancelAnimationFrame(ani);
    contx.clearRect(0,0,600,600);
    contx.strokeRect(0,0,600,600);
    contx.beginPath()
    contx.arc(300, 300, r, 0, 2 * Math.PI);
    contx.fill();
    //console.log(r)
    if(r == 300 || r == 5){
      i = !i
    }
    if (i){
      r += 5
    } else {
      r -= 5
    }
    ani = window.requestAnimationFrame(animate);
}

function startBounce(){
  x = Math.floor(Math.random()*350);
  y = Math.floor(Math.random()*450);
  dx = 1;
  dy = 1;
  bounce();
}

function bounce(){
  window.cancelAnimationFrame(ani2);
  contx.clearRect(0,0,600,600);
  contx.drawImage(logo,20,100,480,300,x,y,200,100)
  contx.strokeRect(0,0,600,600);
  if (x == 0 || x+200 == 600){
    dx = -dx;
  }
  if (y == 0 || y+100 == 600){
    dy = -dy;
  }
  x += dx;
  y += dy;
  ani2 = window.requestAnimationFrame(bounce);
}
