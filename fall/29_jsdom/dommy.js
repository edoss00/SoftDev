//Elizabeth Doss
//SoftDev1 pd1
//K#29 -- Sequential Progression III
//2019-12-12

var changeheading = function(e) {
  var h = document.getElementById("h");
  //console.log(this);
  h.innerHTML = this.innerHTML;
}

var changeback = function(e) {
  var h = document.getElementById("h");
  h.innerHTML = "Hello World!";
}

var removeItem = function(e) {
  //console.log(e);
  this.remove();
};

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++){
  lis[i].addEventListener('mouseover', changeheading);
  lis[i].addEventListener("mouseout", changeback);
  lis[i].addEventListener("click", removeItem);
}

var additem = function(e) {
  ////gets ordered list of items, creates a new element, appends it to the ordered list
  var list = document.getElementById("thelist");
  //console.log(list);
  var item = document.createElement("li");
  item.addEventListener('mouseover', changeheading);
  item.addEventListener("mouseout", changeback);
  item.addEventListener("click", removeItem);
  item.innerHTML = "WORD";
  //console.log(lis);
  lis = document.getElementsByTagName("li");
  list.appendChild(item);
}

var button = document.getElementById("b");
button.addEventListener("click", additem);

var fib = function(n){
    if(n == 0) return 0;
	if (n == 1) return 1;
    return fib(n-1)+fib(n-2);
};

var addfib = function(e) {
	//console.log(e);
	var fiblist = document.getElementById("fiblist");
    //console.log(list);
    var item = document.createElement("li");
	var newFib = fiblist.getElementsByTagName("li").length;
	item.innerHTML = fib(newFib);
	f = document.getElementsByTagName("li");
	fiblist.appendChild(item);
};

var counter = 0;
var fibs = [0,1];

var fib2 = function(n) {
	counter++;
	if (n < 2){
		return fibs[n];
	} 
	else{
		fibs.push(fibs[n-1] + fibs[n-2]);
		//console.log(fibs);
		return fibs[n];
	}
}
		
var addfib2 = function(e) {
	////appends fib numbers to ordered list using dynamic programming
	//console.log(e);
	var fiblist = document.getElementById("fiblist");
    //console.log(list);
    var item = document.createElement("li");
	var newFib = fib2(counter);
	item.innerHTML = newFib;
	f = document.getElementsByTagName("li");
	fiblist.appendChild(item);
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addfib)