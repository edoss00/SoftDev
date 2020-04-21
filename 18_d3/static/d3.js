// Creates proper margins to fit in window
var margin = {top: 50, right: 50, bottom: 50, left: 50}
  , width = window.innerWidth - margin.left - margin.right-20 // Use the window's width
  , height = window.innerHeight - margin.top - margin.bottom - 150; // Use the window's height - int to accomodate header

// Number of datapoints
var n = 8;
// Start value x
var s = 50 //temp

// Creates proper x and y scale for axis
var xScale = d3.scaleLinear()
    .domain([s,s+n]) // x axis only contains the points we will observe
    .range([0, width]);

var yScale = d3.scaleLinear()
    .domain([0, 25]) // 25 trillion is a reasonable value to use as maximum GDP
    .range([height, 0]);

// Create a line with the datapoints
var line = d3.line()
    .x(function(d, i) { return xScale(i+s); }) // x values of line
    .y(function(d) { return yScale(d.y); }) // y values of line





//NEEDS TO BE UPDATED FOR OUR DATAAAAAAAAAAAAAAAAAAAAAA
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
var dataset = d3.range(n).map(function(d) { return {"y": d3.randomUniform(0,25)() } })





// Add SVG to the page with proper margins
var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Call the x and y axis in group tags
svg.append("g")
    .attr("class", "x axis")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(xScale)); // Create an axis component on bottom

svg.append("g")
    .attr("class", "y axis")
    .call(d3.axisLeft(yScale)); // Create an axis component on left

// Append path, bind the data, and call line generator
svg.append("path")
    .datum(dataset) // Binds data to the line
    .attr("class", "line")
    .attr("d", line); // Calls the line generator

// Creates a circle for each datapoint
svg.selectAll(".dot")
    .data(dataset)
  .enter().append("circle")
    .attr("class", "dot")
    .attr("cx", function(d, i) { return xScale(i+s) })
    .attr("cy", function(d) { return yScale(d.y) })
    .attr("r", 5);
