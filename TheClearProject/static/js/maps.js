var map;
var Markers = {};
var infowindow;
//var stations = 0;
var beaches = [
    ['Bondi Beach', -33.890542, 151.274856, 0],
    ['Coogee Beach', -33.923036, 151.259052, 1],
    ['Cronulla Beach', -34.028249, 151.157507, 2],
    ['Manly Beach', -33.80010128657071, 151.28747820854187, 3],
    ['Maroubra Beach', -33.950198, 151.259302, 4]
];
var origin = new google.maps.LatLng(beaches[0][1], beaches[0][2]);

function myMap() {
  var styles = [

       // Hide Google's labels
       {
           featureType: "all",
           elementType: "labels",
           stylers: [
               {visibility: "off"}
           ]
       },
       // Hide roads
       {
           featureType: "road",
           elementType: "geometry",
           stylers: [
               {visibility: "simplified"}
           ]
       }
   ];

  var mapOptions = {
    zoom: 8,
    center: origin
  };

  map = new google.maps.Map(document.getElementById('googleMap'), mapOptions);

	infowindow = new google.maps.InfoWindow();

  // function load_stations(){
  //   $.getJSON("/station_info", function(data) {
  //     stations = data;
  //     alert(stations[0].sponsor);
  //   });
  // };
  //
  // load_stations();
//  alert(stations[1].sponsor);

  var jsonIssues = {};
  $.ajax({
      url: "/station_info",
      async: false,
      dataType: 'json',
      success: function(data) {
          stations = data;
      }
  });

  //alert(stations[1].sponsor);
  var length = parseInt(stations.length);

  //hardcoded 9 in to test, but should be length.
  for(i = 0; i < 9; i++) {
    var position = new google.maps.LatLng(stations[i].latitude, stations[i].longitude);
    var image = "https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";
    //var image = "/img/waterGreen.png";
    var marker = new google.maps.Marker({
			position: position,
			map: map,
      styles: styles,
      icon: image,
		});

    //Ensures legit descriptions are displayed.
    var descrip = "";

    descrip += "<p><strong>Description:</strong> ";
    descrip += stations[i].description;
    descrip += "</p>";

    //Converts 0-3 into user-readable format
    var status_readable;

    if (stations[i].status == 0){
      status_readable = "Excellent condition!";
    };

    if (stations[i].status == 1){
      status_readable = "Beginning to show signs of breakdown.";
    };

    if (stations[i].status == 2){
      status_readable = "Frequently malfunctioning.";
    };

    if (stations[i].status == 3){
      status_readable = "Disrepair.";
    };

    var content_each = "";
    content_each += "<h6 align='center' style='border:3px solid black'>";
    content_each += stations[i].sponsor;
    content_each += "</h5>";

    content_each += "<p align = 'center'><i>";
    content_each += stations[i].station_type;
    content_each += "</i></p>";

    content_each += "<p><strong>Status:</strong> ";
    content_each += status_readable;
    content_each += "</p>";

    content_each += descrip;

    content_each += '<a href= "/login" class="btn btn-danger btn-xs">Help this station</a>';

		google.maps.event.addListener(marker, 'click', (function(marker, i) {
			return function() {
				infowindow.setContent(content_each);
				infowindow.setOptions({maxWidth: 200});
				infowindow.open(map, marker);
			}
		}) (marker, i));
		Markers[stations[i].station_id] = marker;
	}

	locate(0);

}

function locate(marker_id) {
	var myMarker = Markers[marker_id];
	var markerPosition = myMarker.getPosition();
	map.setCenter(markerPosition);
	google.maps.event.trigger(myMarker, 'click');
}

google.maps.event.addDomListener(window, 'load', initialize);
