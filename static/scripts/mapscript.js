var citymap = {
  chicago: {
    center: {lat: 41.878, lng: -87.629},
    population: 2714856,
    color: "#FF0000"
  },
  newyork: {
    center: {lat: 40.714, lng: -74.005},
    population: 8405837,
    color: "#00FFFF"
  },
  losangeles: {
    center: {lat: 34.052, lng: -118.243},
    population: 3857799,
    color: "#008000"
  },
  vancouver: {
    center: {lat: 49.25, lng: -123.1},
    population: 603502,
    color: "#008000"
  }
};

var actualRadius = 0;

// console.log("saving radius of " + document.getElementById('radius').value);

  // if (document.getElementById('radius') !== null) {
  //   actualRadius = document.getElementById('radius').value;
  // }



function initMap() {
  // Create the map.
  console.log("radius is " + actualRadius);
  var styledMapType = new google.maps.StyledMapType(
    [{
      featureType: 'administrative',
      stylers: [{"visibility": 'off'}]
    },
    {
      featureType: 'road',
      stylers: [{"visibility": 'off'}]
    }],
              {name:'Styled Map'}
  );
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: {lat: 37.090, lng: -95.712},
    mapTypeId: 'styled_map'
  });

  map.mapTypes.set('styled_map', styledMapType);
  map.setMapTypeId('styled_map');

  google.maps.event.addListener(map, 'click', function(event) {
   placeMarker(event.latLng);
  });
  google.maps.event.addListener(map, 'idle', function() {
         clusters = loadClusters();
         for (var i = 0; i < clusters.length; i ++) {
            var currCluster = clusters[i];
            var location = currCluster.location;
            var latlng = new google.maps.LatLng(location[0], location[1]);
            var marker = new google.maps.Marker({
            position: latlng,
          });
      }
    });
  var currMarker = null;
  var currCircle = null;
  function placeMarker(location) {
    if (currMarker !== null) {
      currMarker.setMap(null);
    }
    if (currCircle !== null) {
      currCircle.setMap(null);
    }
      var marker = new google.maps.Marker({
          position: location,
          map: map
      });
      currMarker = marker;
      currCircle = new google.maps.Circle({
        strokeColor: "#00FFFF",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#00FFFF",
        fillOpacity: 0.35,
        map: map,
        center: location,
        editable: true,
        radius: 10
      });
  }

  // Construct the circle for each value in citymap.
  // Note: We scale the area of the circle based on the population.
  /*for (var city in citymap) {
    // Add the circle for this city to the map.
    var cityCircle = new google.maps.Circle({
      strokeColor: citymap[city].color,
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: citymap[city].color,
      fillOpacity: 0.35,
      map: map,
      center: citymap[city].center,
      radius: Math.sqrt(citymap[city].population) * 100
    });
  }*/
}
