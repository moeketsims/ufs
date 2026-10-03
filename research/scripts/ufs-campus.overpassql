/*
  OpenStreetMap extract for the UFS campuses: buildings, paths, trees,
  green spaces, amenities and heritage features inside every OSM polygon
  tagged amenity=university whose name mentions "Free State".

  Run at https://overpass-turbo.eu (paste, Run, Export > GeoJSON), or:
    curl -s --data-urlencode data@research/scripts/ufs-campus.overpassql \
      https://overpass-api.de/api/interpreter > research/data/osm-ufs.json

  Not run from the research container (its network policy blocks
  overpass-api.de). Check the result count before relying on it.
  OSM data is (c) OpenStreetMap contributors, ODbL.
*/
[out:json][timeout:120];
(
  way["amenity"="university"]["name"~"Free State|Vrystaat",i];
  relation["amenity"="university"]["name"~"Free State|Vrystaat",i];
)->.uni;
.uni map_to_area->.campus;
(
  .uni;
  nwr["building"](area.campus);
  nwr["highway"](area.campus);
  nwr["natural"~"tree|tree_row|wood|scrub"](area.campus);
  nwr["landuse"~"grass|forest"](area.campus);
  nwr["leisure"](area.campus);
  nwr["amenity"](area.campus);
  nwr["historic"](area.campus);
  nwr["tourism"](area.campus);
  nwr["memorial"](area.campus);
  nwr["artwork_type"](area.campus);
);
out geom;
