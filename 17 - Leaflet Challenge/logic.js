queryURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

// Perform a GET request to the query URL
d3.json(queryURL, function(data) {
  createFeatures(data.features);
});

function createFeatures(earthquakeData) {

  // Define a function we want to run once for each feature in the features array
  // Give each feature a popup describing the magnitude, place and time of the earthquake
  // Create a GeoJSON layer containing the features array on the earthquakeData object
  // Run the onEachFeature function once for each piece of data in the array
  var earthquakes = L.geoJSON(earthquakeData, {
    onEachFeature: function(feature, layer) {
      layer.bindPopup("<h3>Magnitude: " + feature.properties.mag +"</h3><h3>Location: "+ feature.properties.place +
        "</h3><hr><p>" + new Date(feature.properties.time) + "</p>");
    },
      
    pointToLayer: function (feature, latlng) {
      return new L.circle(latlng,
        {radius: getRadius(feature.properties.mag),
        fillColor: getColor(feature.properties.mag),
        fillOpacity: .6,
        color: "white",
        stroke: true,
        weight: .8
    })
  }
});

  // Sending our earthquakes layer to the createMap function
  createMap(earthquakes);
}

function createMap(earthquakes) {

  var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "light-v10",
    accessToken: API_KEY
  });

  // Create overlay object to hold our overlay layer
  var overlayMaps = {
    Earthquakes: earthquakes
  };

  // Create our map, giving it the streetmap and earthquakes layers to display on load
  var myMap = L.map("map", {
    center: [33.7175, -117.8311],
    zoom: 5,
    layers: [lightmap, earthquakes]
  });

  //set up the legend
  var legend = L.control({position: 'bottomright'});
  legend.onAdd = function() {
  
  //create a legend element
  var div = L.DomUtil.create('div', 'legend');

  //create labels and values to find colors
  var labels = ["0-1", "1-2", "2-3", "3-4", "4-5", "5+"];
  var grades = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5];

  //create legend html
  div.innerHTML = '<div><strong>Magnitude</strong></div>';
  for(var i = 0; i < grades.length; i++) {
      div.innerHTML += '<i style = "background:' + getColor(grades[i]) + '">&nbsp;</i>&nbsp;&nbsp;'
      + labels[i] + '<br/>';
    };
    return div;
  };

  //add legend to map
  legend.addTo(myMap);
}


//Create color range for the circle diameter 
function getColor(magnitude) {
  if (magnitude<1) {
    return "gray"}
  else if (magnitude<2) {
     return "skyblue"}
  else if (magnitude<3) {
     return "lightgreen"}
  else if (magnitude<4) {
     return "yellow"}
  else if (magnitude<5) {
     return "orange"}
  else if (magnitude>=5) {
     return "red"}
  else {
     return "black"}
 };  

 
//Change the magnitude of the earthquake by a factor of 20,000 for the radius of the circle. 
function getRadius(value){
  return value*20000
}
  
