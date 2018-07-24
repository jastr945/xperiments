'use strict';

var coordinates = [];
var i;
var marker;


$(document).ready(function() {

  // Rendering a map
  var mapProp = {
      center: new google.maps.LatLng(36.7783, -119.4179),
      zoom: 6,
  };
  var map = new google.maps.Map(document.getElementById("map"), mapProp);
  console.log("Map is displayed.");

  // Displaying markers based on the list of coordinates
  function getMarkers(myList) {

    for (i = 0; i < myList.length; i++) {
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(myList[i][4], myList[i][5]),
        map: map
      });

      var infowindow = new google.maps.InfoWindow();

      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent("<p>" + myList[i][0] + "<br />" + "Address: " + myList[i][1] + "<br />" + "Website: " + myList[i][2]+ "<br />" + myList[i][3] + "</p>");
          infowindow.open(map, marker);
        }
      })(marker, i));
    };
    console.log("Markers are displayed.");
  }

  // Closing the info window
  $("#gotit").click(function(e) {
    $("#info").addClass("invisible");
  });

  // Getting data from California Coastal Commission Cleanup Day API upon click
  $("#getMarkers").click(function(e) {
      $(this).addClass("invisible");
      e.preventDefault();
      $.ajax({
        url: "https://api.coastal.ca.gov/ccd/v1/locations",
        type: "GET",
        success: function(res) {
          jQuery.each(res, function(index, itemData) {
            console.log("Getting coordinates.", itemData);
            if (itemData.address === null) {
              itemData.address = "No address provided.";
            };
            if (itemData.website === null) {
              itemData.website = "No website provided.";
            };
            coordinates.push([itemData.site_name, itemData.address, itemData.website, itemData.how_to_register, itemData.latitude, itemData.longitude]);
          });
          getMarkers(coordinates);
        }
      });
  });
});
