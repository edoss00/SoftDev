//Jenny Huang and Elizabeth Doss (Team ThisCodeIsSick)
//SoftDev1 pd1
//K#13 -- Ask Circles [Change || Die]
//2020-03-30

var pic = document.getElementById("vimage");
var btn = document.getElementById("clear");

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
  }
};

var change = function(e){
  // console.log(e);
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

btn.addEventListener('click', clear);

pic.addEventListener('click', draw);
