// from data.js
var tableData = data;

// Table body reference
var tbody = d3.select("tbody");

console.log(tableData);
// LEVEL 1 - PART 1: Write code that appends a table to your web page and then adds new rows of data for each UFO sighting
// 2 solutions taught

// Part 1: Solution #1
// Loop thru the tableData and console.log each UFO sighting
    // tableData.forEach(function(ufoSighting) {
    //     console.log(ufoSighting);

    //     // Use d3 to append one table row 'tr' for each UFO sighting
    //     var row = tbody.append("tr");

    //     // Use 'Object.entries' to console.log each UFO sighting entry
    //     Object.entries(ufoSighting).forEach(function([key,value]) {
    //         console.log(key,value);

    //     // Use d3 to append 1 cell per UFO sighting value in the ufoSighting object
    //     var cell = row.append("td");
    
    //     // Use d3 to append a cell to the row for each value in the ufoSighting object
    //     cell.text(value);
    //     });
    // });

// Part 1: Solution #2  
    //Refactor 1st solution to use Arrow Functions
    tableData.forEach((ufoSighting) => {
        var row = tbody.append("tr");
        Object.entries(ufoSighting).forEach(([key,value]) => {
            // console.log(key,value);
            var cell = row.append("td");
            cell.text(value);
        });
    });

// Part 2: Use a date form in the HTML document and write JavaScript code that will listen for events and search through..
        // the date/time column to find rows that match user input.

    var filterButton = d3.select("#filter-btn");              // Select the button
    
    filterButton.on("click", function() {                     // Create Event handler "filterButton"
        d3.event.preventDefault();
    
        var inputElement = d3.select("#datetime");
        var inputValue = inputElement.property("value");
        var filteredTable = tableData.filter(sighting => sighting.datetime === inputValue);
    
        // Repeat part1: solution 2 however this time reference the filteredTable variable created above
        d3.selectAll("td").remove();                           // Be sure to remove existing data
        filteredTable.forEach(function(sighting) {
            var row = tbody.append("tr");
            Object.entries(sighting).forEach(function([key, value]) {
                var cell = row.append("td");
                cell.text(value);
            });
        });
    });
    

// LEVEL 2 (Optional) 
        // Using multiple input tags and/or select dropdowns, write JavaScript code so that the
        // user can set multiple filters and search for UFO sightings using the following criteria
        // based on the talbe columns:  date/time, city, state, country, and/or shape

