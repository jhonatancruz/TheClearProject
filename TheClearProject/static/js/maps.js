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
  var map = new google.maps.Map(mapCanvas, options);

  setMarkers(map);

};

function setMarkers(map){
  var beaches = [
      ['Bondi Beach', -33.890542, 151.274856, 4],
      ['Coogee Beach', -33.923036, 151.259052, 5],
      ['Cronulla Beach', -34.028249, 151.157507, 3],
      ['Manly Beach', -33.80010128657071, 151.28747820854187, 2],
      ['Maroubra Beach', -33.950198, 151.259302, 1]
  ];

  for (var i = 0; i < beaches.length; i++ ){
    var beach = beaches[i];
    var marker = new google.maps.Marker({
        position: {lat: beach[1], lng: beach[2]},
        animation: google.maps.Animation.DROP,
        map:map


    });

    marker.setmap(map);

    var infowindow = new google.maps.InfoWindow({
      content: beach[0]
    })
  };

  marker.addListener('click', function() {
    infowindow.open(map, marker)
  });


  // marker.setMap(map);
  // var infowindow = new google.maps.InfoWindow({
  //   content: "Sup!"
  // });
  //
  // marker.addListener('click', function() {
  //       infowindow.open(map, marker)
  // });

}
