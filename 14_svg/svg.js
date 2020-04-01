//Emily Zhang and Elizabeth Doss (Team Waffle Bikes)
//SoftDev1 pd1
//K#14 -- Ask Circles [Change || Die] While Moving, etc.
//2020-03-31

var pic = document.getElementById("vimage");
var btn = document.getElementById("clear");
var mov = document.getElementById("mov");
var stop = document.getElementById("stopbtn");
var color = document.getElementById("rainbowfy")

var dx = 1;
var dy = 1;
var ani;
var dxList = [];
var dyList = [];

var clear = function(e){
  while (pic.lastChild){
    pic.removeChild(pic.lastChild);
  }
};


var draw = function(e){
  if (e.target == pic){
    var x = e.offsetX;
    var y = e.offsetY;
    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", "20");
    c.setAttribute("fill", "blue");
    c.setAttribute("stroke", "black");
    c.addEventListener('click', change);
    pic.appendChild(c);
    dxList.push(1);
    dyList.push(1);
  }
};

var change = function(e){
  //console.log(e);
  if (e.target.getAttribute("fill") == "blue"){
    e.target.setAttribute("fill", "cyan");
  }
  else{
    var x = Math.floor(Math.random() * pic.getAttribute("width"));
    var y = Math.floor(Math.random() * pic.getAttribute("height"));
    e.target.setAttribute("cx", x);
    e.target.setAttribute("cy", y);
    e.target.setAttribute("fill", "blue");
  }
}

var move = function(e){
  window.cancelAnimationFrame(ani);
    for (i = 0; i < pic.children.length; i++){
    child = pic.children[i];
    x = parseInt(child.getAttribute("cx"));
    y = parseInt(child.getAttribute("cy"));
    if (x-20 <= 0 || x+20 >= 500){
      dxList[i] = -dxList[i];
    }
    if (y-20 <= 0 || y+20 >= 500){
      dyList[i] = -dyList[i];
    }
    x += dxList[i];
    y += dyList[i];
    child.setAttribute("cx", x);
    child.setAttribute("cy", y);
  }
  ani = window.requestAnimationFrame(move);
}

var cancel = function(e){
  window.cancelAnimationFrame(ani);
}

var rainbow = function(e){
  for (i = 0; i < pic.children.length; i++){
    child = pic.children[i];
    var randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);
    console.log(randomColor);
    child.setAttribute("fill", randomColor);
  }

}

btn.addEventListener('click', clear);
pic.addEventListener('click', draw);
mov.addEventListener('click', move);
stop.addEventListener('click', cancel);
color.addEventListener('click', rainbow);
