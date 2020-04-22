// Amanda "Amber" Chen, Elizabeth Doss (Team The Riftbreakers)
// SoftDev2 pd1
// K18 -- Come Up For Air
// 2020-04-20


var render = document.getElementById('render');
var transition = document.getElementById('transition');
var rendered = false
var svg, x, y;
// Number of datapoints
var n = 14;
var i = 0;
var s = 1960;

var show = function(e){
  if (!rendered){
    // console.log(gdp)
    var graph = document.getElementById('linegraph');
    // console.log(graph)

    // console.log(graph)
    // var dataset = gdp.slice(i, i + 10);
    var datasety = d3.range(n).map(function(d) { return {"year": gdp[i+d][0], "value": gdp[i+d][1]} })
    console.log(datasety[0].year)

    // Creates proper margins to fit in window
    var margin = {top: 50, right: 50, bottom: 50, left: 100}
      , width = window.innerWidth - margin.left - margin.right-20 // Use the window's width
      , height = window.innerHeight - margin.top - margin.bottom - 150; // Use the window's height - int to accomodate header

    // Add SVG to the page with proper margins
    svg = d3.select("#linegraph").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Creates proper x and y scale for axis
    x = d3.scaleLinear()
        .domain([s,s+n-1]) // x axis only contains the points we will observe
        .range([0, width]);
    svg.append("g")
        .attr("class", "xaxis")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x)); // Create an axis component on bottom
    // console.log([s,s+n-1])

    y = d3.scaleLinear()
        .domain([d3.min(datasety, function(d) { return d.value; }), d3.max(datasety, function(d) { return d.value; })])
        .range([height, 0]);
    svg.append("g")
        .attr("class", "yaxis")
        .call(d3.axisLeft(y)); // Create an axis component on left
    // console.log([0, d3.max(datasety, function(d) { return d.value; })])

    // Append path, bind the data, and call line generator
    svg.append("path")
        .datum(datasety) // Binds data to the line
        .attr("class", "line")
        .attr("d", d3.line()
          .x(function(d) { return x(d.year) })
          .y(function(d) { return y(d.value) }))
          .attr("stroke", "steelblue")
          .attr("stroke-width", 1.5); // Calls the line generator
    // Creates a circle for each datapoint
    svg.selectAll(".dot")
        .data(datasety)
      .enter().append("circle")
        .attr("class", "dot")
        .attr("cx", function(d) { return x(d.year) })
        .attr("cy", function(d) { return y(d.value) })
        .attr("r", 5);
    rendered = true
  }
}

var change = function(e){
  console.log(s)
  if (s < 2002){
    s += 14;
    i += 14;
  } else {
    s = 1960;
    i = 0;
  }
  var datasety = d3.range(n).map(function(d) { return {"year": gdp[i+d][0], "value": gdp[i+d][1]} })
  console.log(datasety)

  x.domain([s,s+n-1]);
  svg.select(".xaxis")
    .transition()
    .duration(3000)
    .call(d3.axisBottom(x));
  console.log([s,s+n-1])

  y.domain([d3.min(datasety, function(d) { return d.value; }), d3.max(datasety, function(d) { return d.value; })]);
  svg.select(".yaxis")
    .transition()
    .duration(3000)
    .call(d3.axisLeft(y));

  var u = svg.selectAll(".line")
    .datum(datasety);

  u
    .enter().append("path")
      .datum(datasety)
      .attr("class", "line")
      .merge(u)
      .transition()
      .duration(3000)
      .attr("fill", "none")
      .attr("d", d3.line()
        .x(function(d) { return x(d.year) })
        .y(function(d) { return y(d.value) }))
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5);

  var v = svg.selectAll(".dot")
    .data(datasety);

  v
    .enter().append("circle")
    .attr("class", "dot")
    .merge(v)
    .transition()
    .duration(3000)
    .attr("cx", function(d) { return x(d.year) })
    .attr("cy", function(d) { return y(d.value) })
    .attr("r", 5)
    .attr("fill", "steelblue");
}
//
//
// //NEEDS TO BE UPDATED FOR OUR DATAAAAAAAAAAAAAAAAAAAAAA
// //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// var dataset = d3.range(n).map(function(d) { return {"y": d3.randomUniform(0,25)() } })
//
//
//

render.addEventListener('click', show);
transition.addEventListener('click', change);
