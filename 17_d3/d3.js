// The Riftbreakers
// SoftDev pd1
// K17 -- Deeper into D3
// 2020-04-03

//transition fade to black
d3.select("body").transition()
    .style("background-color", "lightgray");

// Data for bar chart
var data = [4, 8, 15, 16, 23, 42];

// Create an empty (detached) chart container.
const div = d3.create("div")
  // Apply some styles to the chart container.
  .style("font", "10px sans-serif")
  .style("text-align", "right")
  .style("color", "white");

// Scaling bars to proper pixle width
x = d3.scaleLinear()
    .domain([0, d3.max(data)])
    .range([0, 420])

// Define the initial (empty) selection for the bars.
const bar = div.selectAll("div")
  .data(data)
  .join("div")
    .style("background", "steelblue")
    .style("padding", "3px")
    .style("margin", "1px")
    .style("width", d => `${x(d)}px`)
    .text(d => d);

// Bind this selection to the data (computing enter, update and exit).
const barUpdate = bar.data(data);

// Join the selection and the data, appending the entering bars.
const barNew = barUpdate.join("div");

// Return the chart container.
console.log(div.node());

document.getElementById("chart").appendChild(div.node());
