//Elizabeth Doss
//SoftDev1 pd1
//K27 -- Sequential Progression
//2019-12-10 

var helloworld = function() {
	return("hello world");
};

var fact = function() {
	n = factBut.getAttribute('val');
	if (n < 2){
		return 1;
	}
	return n * (fact(n - 1));
};

//V1
var fibonacci = function(n,a=0,b=1) {
	while (n > 1){
		c = a;
		a = b;
		b = c+b;
		n-=1;
	}
	return a;
};

//V2
var fib = function(n) {
	if (n == 0) return 0;
	if (n == 1) return 1;
	return fib(n-1) + fib(n-2)
};

var gcd = function(x,y){
	r = x % y;
	while (r != 0){
		x = y;
		y = r;
		r = x % y;
	}
	return y;
}

var students = ["Alice","Bob","Charlie","Devin","Elsa", "Fred", "George"];

var randomStudent = function(){
	i = Math.floor(Math.random() * students.length)
	return students[i];
}



//HTML
var factBut = document.getElementByID('fa');
factBut.addEventListener('click', fact);

