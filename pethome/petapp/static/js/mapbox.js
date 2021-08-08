mapboxgl.accessToken = 'pk.eyJ1IjoiY2F5bGFrYmlsaXNpbWNpIiwiYSI6ImNrcnMwemxmYjVwaXUycHA4N3BudHVncmsifQ.dBbSWrGXesEchgDjQwrX5Q';
var map = new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [27.513357117814053, 40.98823851310837],
      zoom: 13
});
       
var geocoder = new MapboxGeocoder({
    accessToken: mapboxgl.accessToken,
    marker: {
      color: 'orange'
     },
    mapboxgl: mapboxgl
    });
       
map.addControl(geocoder);