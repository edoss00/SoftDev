// Elizabeth Doss
// SoftDev1 pd1
// K06 -- Dot Dot Dot
// 2020-02-06

var clearButton = document.getElementById('clear');
var canv= document.getElementById('playground');
var contx=canv.getContext('2d');
var x=0;
var y=0;

contx.strokeRect(0,0,600,600);

clearButton.addEventListener('click',clear);

function clear(){
    console.log('clear');
    contx.clearRect(0,0,600,600);
    contx.strokeRect(0,0,600,600);
}


canv.addEventListener("click", draw);
function draw(event) {
    var r = 5;
    console.log(event.clientX +",",event.clientY);
    //dot
    contx.beginPath()
    contx.arc(event.clientX - 8, event.clientY - 8, r, 0, 2 * Math.PI);
    contx.fill();
    //line
    if (x != 0){
      contx.beginPath();
      contx.moveTo(x,y);
      contx.lineTo(event.clientX-8,event.clientY-8);
      contx.stroke()
    }
    x=event.clientX-8;
    y=event.clientY-8;


}
