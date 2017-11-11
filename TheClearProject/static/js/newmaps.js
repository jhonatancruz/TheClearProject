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
       center: {lat: 37.4236, lng: -122.1619}, // Stanford, California
       disableDefaultUI: true,
       mapTypeId: google.maps.MapTypeId.ROADMAP,
       maxZoom: 14,
       panControl: true,
       styles: styles,
       zoom: 13,
       zoomControl: true
   };
  var myCenter = new google.maps.LatLng(51.508742,-0.120850);
  var mapCanvas = document.getElementById("googleMap");
  var map = new google.maps.Map(mapCanvas, options);

  var marker = new google.maps.Marker({position:myCenter});
  marker.setMap(map);

  var infowindow = new google.maps.InfoWindow({
    content: "Hello!"
  });

  marker.addListener('click', function() {
        infowindow.open(map, marker)
  });

};
