// Elizabeth Doss
// SoftDev1 pd1
// K07 -- They lock us in the tower whenever we get caught
// 2020-02-11

var startButton = document.getElementById('start');
var stopButton = document.getElementById('stop');
var canv= document.getElementById('canvas');
var contx=canv.getContext('2d');
var r = 10;
var i = true;

contx.strokeRect(0,0,600,600);
startButton.addEventListener('click',start);

function stop(){
  startButton.addEventListener('click',start);
  window.cancelAnimationFrame(ani);
}


function start(event){
  startButton.removeEventListener('click',start);
  stopButton.addEventListener('click',stop);
  ani = window.requestAnimationFrame(animate);
}

function animate(){
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
