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
    // Refactor 1st solution to use Arrow Functions
    // tableData.forEach((ufoSighting) => {
    //     var row = tbody.append("tr");
    //     Object.entries(ufoSighting).forEach(([key,value]) => {
    //         // console.log(key,value);
    //         var cell = row.append("td");
    //         cell.text(value);
    //     });
    // });

// Part 2: Use a date form in the HTML document and write JavaScript code that will listen for events and search through..
        // the date/time column to find rows that match user input.

    var button = d3.select("#filter-btn");              // Select the button
    var form = d3.select(form);                         // Select the form
    
    button.on("click", refreshTable);                       // Create event handler for button
    form.on("submit", refreshTable);                        // Create event handler for form


    // Create the event handler function "runEnter" for the form
    function refreshTable() {
        
        d3.event.preventDefault();                          // Prevent the page from refreshing
        var inputElement = d3.select("#datetime");          // Select the input element and get the raw HTML node
        var inputValue = inputElement.property("value");    // Get the value property of the input element
    
        console.log(inputValue);
    
        var filteredData = tableData.filter(ufoSighting => ufoSighting.datetime === inputValue);

        console.log(filteredData);
        
        $
        ("#ufo_table tr").remove();                        // Remove all the rows in the table
        //Update table with filtered data
        filteredData.forEach((ufoSighting) => {
            var row = tbody.append("tr");
            Object.entries(ufoSighting).forEach(([key,value]) => {
                // console.log(key,value);
                var cell = row.append("td");
                cell.text(value);
            });
        });

    };



// LEVEL 2 (Optional) 
        // Using multiple input tags and/or select dropdowns, write JavaScript code so that the
        // user can set multiple filters and search for UFO sightings using the following criteria
        // based on the talbe columns:  date/time, city, state, country, and/or shape

    
