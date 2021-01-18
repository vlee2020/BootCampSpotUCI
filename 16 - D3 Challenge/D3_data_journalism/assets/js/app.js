// Set up chart parameters: height, width, margins
// Create a SVG container
// Read in a csv, or json d3.csv or d3.json
    // Parse the data.  Cast all neccessary data as numbers or datetime objects
    // Create scales
    // Create axes
    // Append axes to our SVG group and place them appropriately using transform
    // Create generator function (line, pie, bar)
    // Use the generator functions to create our SVG path


// Step 1: Setup chart parameters: height, width, margins
var svgWidth = 825;
var svgHeight = 550;


var margin = {     // svg borders setup
  top: 40,
  right: 40,
  bottom: 80,
  left: 100
};

var width = svgWidth - margin.left - margin.right;    //chart width  
var height = svgHeight - margin.top - margin.bottom;  //chart height  

// Step 2: Create a SVG wrapper (aka container)
var svg = d3.select("#scatter")
  .append("svg")                // Append an SVG that will hold the chart
  .attr("class", "chart")
  .attr("width", svgWidth)      // Shift chart based on left/right margins
  .attr("height", svgHeight);   // Shift chart based on top/bottom margins

// Append an svg group
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Step 3: Read in csv file (data.csv) using d3.csv
d3.csv("assets/data/data.csv").then(function(stateData) {

    // Step 4: Parse/Cast all necessary data as integer values
    stateData.forEach(function(d) {
      d.smokes = +d.smokes;           
      d.obesity = +d.obesity;
      d.healthcare = +d.healthcare;
      d.poverty = +d.poverty;
      d.age = +d.age;
      d.income = +d.income
    });

    // Step 5: Create the scales for our chart
    var xLinearScale = d3.scaleLinear()
      .domain([d3.min(stateData, d => d.poverty * .9),     // multiply by value less than 1
               d3.max(stateData, d => d.poverty * 1.05)])  // multiply by value greater than 1
      .range([0, width]);

    var yLinearScale = d3.scaleLinear()
      .domain([d3.min(stateData, d => d.healthcare *.8), 
               d3.max(stateData, d => d.healthcare) * 1.1])
      .range([height, 0]);

    // Step 3: Create axis functions
    // ==============================
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Step 4: Append Axes to the chart
    // ==============================
    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

    chartGroup.append("g")
      .call(leftAxis);

    // Step 5: Create Circles
    // ==============================
    var circlesGroup = chartGroup.selectAll("circle")
    .data(stateData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.poverty))
    .attr("cy", d => yLinearScale(d.healthcare))
    .attr("r", "12")
    .attr("class", "stateCircle")
 
    // Step 6: Initialize tool tip
    // ==============================
    var toolTip = d3.tip()
      .attr("class", "d3-tip")
      .offset([-8,0])
      .html(function(d) {
        return (`${d.state}<br>Poverty: ${d.poverty}%<br>No Healthcare: ${d.healthcare}%`);
      });

      // Step 7: Create tooltip in the chart
      // ==============================
      chartGroup.call(toolTip);
  
      // Step 8: Create event listeners to display and hide the tooltip
      // ==============================
      circlesGroup.on("click", function(data) {
        toolTip.show(data, this);
      })
        // onmouseout event
        .on("mouseout", function(data, index) {
          toolTip.hide(data);
        });
  
      // Appending state abbreviations to each circle plot
      chartGroup.append("text")
        .attr("class", "stateText")
        .selectAll("tspan")
        .data(stateData)
        .enter()
        .append("tspan")
          .attr("x", function(d){return xLinearScale(d.poverty - 0);
          })
          .attr("y", function(d){return yLinearScale(d.healthcare - 0.2);
          })
          .text(function(d){return d.abbr});

      // Create axes labels
      chartGroup.append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 0 - margin.left + 40)
        .attr("x", 0 - (height / 1.5))
        .attr("dy", "1em")
        .attr("class", "axisText")
        .text("Without Healthcare (%)");
  
      chartGroup.append("text")
        .attr("transform", `translate(${width / 2.5}, ${height + margin.top + 15})`)
        .attr("class", "axisText")
        .text("In Poverty (%)");
    }).catch(function(error) {
      console.log(error);
    });
