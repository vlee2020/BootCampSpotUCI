// from data.js
var tableData = data;

// Table body reference
var tbody = d3.select("tbody");

tableData.forEach((ufoSighting) => {
    var row = tbody.append("tr");
    Object.entries(ufoSighting).forEach(([key,value]) => {
        // console.log(key,value);
        var cell = row.append("td");
        cell.text(value);
    });
});

// loop through table
function displayData(ufo){ 
    tbody.text("")
    ufo.forEach(function(ufo_sighting){
    new_tr = tbody.append("tr")
    Object.entries(ufo_sighting).forEach(function([key, value]){
        new_td = new_tr.append("td").text(value)	
    })
})}

// Part 2: Use a date form in the HTML document and write JavaScript code that will listen for events and search through..
        // the date/time column to find rows that match user input.

    var filterButton = d3.select("#filter-btn");              // Select the button
    
    filterButton.on("click", function() {                     // Create Event handler "filterButton"
        d3.event.preventDefault();
    
        var inputElementDate = d3.select("#datetime");
        var inputElementCity = d3.select("#city");
        var inputElementState = d3.select("#state");
        var inputElementCountry = d3.select("#country");
        var inputElementShape = d3.select("#shape");
        var inputElementDuration = d3.select("#duration");
 

        var inputValueDate = inputElementDate.property("value");
        var inputValueCity = inputElementCity.property("value");
        var inputValueState = inputElementState.property("value");
        var inputValueCountry = inputElementCountry.property("value");
        var inputValueShape = inputElementShape.property("value");
        var inputValueDuration = inputElementDuration.property("value");

        var filteredTable = tableData.filter(sighting => {
            return (sighting.datetime === inputValueDate || !inputValueDate) &&
                    (sighting.city === inputValueCity || !inputValueCity) &&
                    (sighting.state === inputValueState || !inputValueState) &&
                    (sighting.country === inputValueCountry || !inputValueCountry) &&
                    (sighting.shape === inputValueShape || !inputValueShape) &&
                    (sighting.durationMinutes === inputValueDuration || !inputValueDuration)
        })
        
    displayData(filteredTable);

    });