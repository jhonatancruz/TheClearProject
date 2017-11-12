var map;
var Markers = {};
var infowindow;

var beaches = [
    ['Bondi Beach', -33.890542, 151.274856, 0],
    ['Coogee Beach', -33.923036, 151.259052, 1],
    ['Cronulla Beach', -34.028249, 151.157507, 2],
    ['Manly Beach', -33.80010128657071, 151.28747820854187, 3],
    ['Maroubra Beach', -33.950198, 151.259302, 4]
];


function myMap() {
  let styles = [

       // Hide Google's labels
       {
           featureType: "all",
           elementType: "labels",
           stylers: [
               {visibility: "on"}
           ]
       },
       // Hide roads
       {
           featureType: "road",
           elementType: "geometry",
           stylers: [
               {visibility: "off"}
           ]
       }
   ];

   // Options for map
   // https://developers.google.com/maps/documentation/javascript/reference#MapOptions
  let options = {
       center: {lat:  -0.3609324, lng: 35.9782985}, // Kenya
       disableDefaultUI: true,
       mapTypeId: google.maps.MapTypeId.ROADMAP,
       maxZoom: 14,
       panControl: true,
       styles: styles,
       zoom: 8,
       zoomControl: true
   };
  var myCenter = {lat:  -0.3609324, lng: 35.9782985};// new google.maps.LatLng(-0.3609324,35.9782985);
  var mapCanvas = document.getElementById("googleMap");
  map = new google.maps.Map(mapCanvas, options);

  setMarkers(map);

};

function setMarkers(map){

  infowindow = new google.maps.InfoWindow(); //{
  //  content: beach[0]
  //});

  for (i = 0; i < beaches.length; i++ ){
    var beach = beaches[i];
    var marker = new google.maps.Marker({
        position: {lat: beach[1], lng: beach[2]},
        animation: google.maps.Animation.DROP,
        map:map,
    });

    //marker.setmap(map);
    google.maps.event.addListener(marker, 'click', (function(marker, i){
      return function(){
        infowindow.setContent(beach[i][0]);
				infowindow.setOptions({maxWidth: 200});
				infowindow.open(map, marker);
      }
    }) (marker, i));
    Markers[beaches[i][3]] = marker;

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

  //marker.addListener('click', function() {
    //infowindow.open(map, marker)
  //});


  // marker.setMap(map);
  // var infowindow = new google.maps.InfoWindow({
  //   content: "Sup!"
  // });
  //
  // marker.addListener('click', function() {
  //       infowindow.open(map, marker)
  // });
