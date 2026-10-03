# Geospatial and 3D data: what exists and what you may do with it

*Researched 3 Oct 2026.*

> **How this was verified.** Most official sites (Google, Cesium, OSM, ufs.ac.za, NGI) could not be opened from the research container. Claims come from search-engine summaries of the cited pages, except GitHub-hosted docs and changelogs, which were read in full. Later topics (NGI, LiDAR, Street View, some pricing) rest on background knowledge and are marked **UNVERIFIED**. Nothing here is legal advice — get licence questions confirmed in writing.

## The headline

**The licence question decides the data stack, not the resolution.** Google's 3D city mesh is the quickest way to a photoreal aerial of Bloemfontein, but its terms forbid caching or extracting it and limit promotional videos, and Google Earth Studio's terms bar promotional films outright. If the film is a UFS recruitment or brand piece, **plan on capturing your own 3D data** (drone photogrammetry plus Gaussian splats) and use Google only for internal previs. If it is a genuinely documentary or educational piece, Earth Studio fly-ins with on-screen attribution are probably allowed.

## Summary table

| Source | Type | Resolution | UFS coverage | Access & cost | Licence for a public video |
|---|---|---|---|---|---|
| [Google Photorealistic 3D Tiles](https://developers.google.com/maps/documentation/tile/3d-tiles-overview) | Photogrammetric mesh (OGC 3D Tiles) | City-block scale; "melts" at street level | **Bloemfontein probably covered** (in Google's SA list per one snippet + community list); campus edges and South Campus **UNVERIFIED**. **Qwaqwa not listed** → likely flat terrain + imagery | API key + billing; 1,000 root-tileset requests/month free, then ~US$6 per 1,000 ([billing](https://developers.google.com/maps/documentation/tile/usage-and-billing)) | **Restrictive** — no caching/offline/extraction; promotional videos must be short and about *your app*; on-screen Google attribution ([policies](https://developers.google.com/maps/documentation/tile/policies)) |
| [Google Earth Studio](https://www.google.com/earth/studio/faq/) | Browser animation tool on Google Earth 3D | Same as Google Earth; JPEG frame sequences | Same 3D source | Free; apply for access; Chrome only | Films, documentaries, TV, education OK with attribution (watermarked). **No promotional films or ads** ([attribution](https://earth.google.com/studio/docs/attribution/)) |
| [Cesium ion](https://cesium.com/learn/ion/content-usage-and-attribution-guide/) — World Terrain, OSM Buildings, Bing/Google 2D imagery | Terrain, extruded OSM buildings, imagery | World Terrain in SA **UNVERIFIED** (~30 m class) | Global | Community plan free (non-commercial); Commercial US$149/mo individual, US$524/mo team | Video OK with visible attribution (end credits fine); no offline use without a licence; Google layers keep Google's terms |
| OpenStreetMap | Footprints, paths, trees, names | As mapped | Qwaqwa campus polygon exists ([way 404094260](https://mapcarta.com/W404094260)); Bloemfontein detail **UNVERIFIED** | Free | ODbL — a rendered film is a "Produced Work": credit "© OpenStreetMap contributors" |
| [Microsoft Global ML Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints) | Footprints, some heights | ML from 2014–2024 imagery | South Africa covered (big Aug-2024 update: 1.5M SA edits) | Free | CDLA Permissive 2.0 |
| [Google Open Buildings v3 / 2.5D Temporal](https://github.com/google/earthengine-catalog) | Footprints / raster heights | 50 cm source (v3); 4 m effective, 2016–2023 (2.5D) | Africa covered; SA specifically **UNVERIFIED** | Free (Earth Engine / GCS) | CC BY 4.0 (2.5D: CC BY 4.0 or ODbL) |
| [Overture Maps buildings](https://github.com/OvertureMaps/docs) | Conflated footprints with `height` | Mixed (OSM first, then Esri, then ML) | Global | Free GeoParquet | ODbL |
| Copernicus GLO-30 | **Surface** model (buildings and trees baked in) | 30 m | Global | Free | Free with attribution |
| ALOS AW3D30 v4.1 | Surface model | 30 m | Global | Free | [JAXA terms](https://earth.jaxa.jp/en/data/policy/) |
| NASADEM / SRTM GL1 | Terrain model | 30 m | Global | Free | Any purpose |
| NGI (Chief Directorate: National Geo-spatial Information) | Aerial orthophotos; DEM | ~0.25–0.5 m; DEM ~25 m (**UNVERIFIED**) | National (**UNVERIFIED**) | Order from [NGI](http://www.ngi.gov.za) / [CDNGI portal](https://cdngiportal.co.za); historically low/no cost (**UNVERIFIED**) | **UNVERIFIED** |
| LiDAR for Mangaung | Point cloud | — | **None found** (**UNVERIFIED** as a negative) — ask Mangaung Metro GIS and UFS Geography | — | — |
| [Esri World Imagery Wayback](https://github.com/Esri/wayback) | 2D imagery + every version since 2014 | Sub-metre | Global | Free app | Esri terms; broadcast rights **UNVERIFIED** |
| Sentinel-2 | Multispectral | 10 m | Global | Free | Copernicus open licence |
| Vantor (ex-Maxar) / Airbus Pléiades Neo | Very high-res satellite | 30 cm | On request | ~US$15–30/km² archive, minimum orders (**UNVERIFIED**) | Per order; check broadcast rights |
| [UFS 360° tours](https://www.ufs.ac.za/prospective/VirtualExperience/undergraduate-360-view) / [virtual orientation](https://www.ufs.ac.za/virtualorientationbfn/) | Panoramas | — | All three campuses | Web | UFS copyright — ask |
| **Your own drone + ground capture** | Photogrammetry, Gaussian splats | 1–3 cm GSD | Whatever you capture | See `05-production-pipeline.md` | **You own it** (needs SACAA-compliant operator + UFS permission) |

## Notes per source

### Google Photorealistic 3D Tiles

- **Coverage:** Google advertises 2,500+ cities in 49 countries. One search snippet listed South African cities including Bloemfontein, Cape Town, Durban, East London, Johannesburg/Pretoria, Newcastle, Gqeberha and Rustenburg; a second search didn't reproduce it, so treat Bloemfontein as **probable, not certain**. A community list also names Bloemfontein ([fandom](https://list.fandom.com/wiki/List_of_3D_locations_in_Google_Earth)). **Check the "3D coverage" layer in Google Earth over the Universitas/Park West area and South Campus before relying on it.**
- **Qwaqwa** is not listed; published Google Earth figures of the campus credit 2D satellite imagery ([ResearchGate](https://www.researchgate.net/figure/Google-Earth-image-of-the-UFS-QwaQwa-campus-CNES-Airbus-DigitalGlobe-4-993m-camera_fig2_333741735)).
- **Policies** ([Map Tiles policies](https://developers.google.com/maps/documentation/tile/policies); [Maps Platform ToS §3.2.3](https://cloud.google.com/maps-platform/terms)): no caching, extraction or offline use; Google logo and data-provider attribution on screen; your own 3D objects only if not derived from the tiles. Promotional videos are allowed only for "experiences you build", reported as short (≤30 s) and marked as promotional. **A stand-alone cinematic UFS film is outside or at best on the edge of these terms — get Google's written permission before using tiles in final frames.**
- **Tooling:** Cesium for Unreal shows the required credits; Movie Render Queue works (disable LOD transitions; an older loading bug was fixed in v1.29) ([Cesium tutorial](https://cesium.com/learn/unreal/unreal-photorealistic-3d-tiles/)).
- **Other risks:** tiles update over time and can't be locked, so re-renders may not match ([Cesium forum](https://community.cesium.com/t/google-photorealistic-3d-tiles-changed-over-time-is-there-any-way-to-lock-or-preserve-previous-data/44682)). Importing tiles into Blender (e.g. via blosm) stores them as local geometry — very likely "extraction" under the ToS. Treat it as unsafe for a published film.

### Google Earth Studio

- Still live in 2026 with no shutdown announced. (Separately, the Google Earth **Pro desktop** download ends 25 June 2027 — [Android Police](https://www.androidpolice.com/google-earth-pro-desktop-app-going-away-in-2027/).)
- Every frame carries "Google Earth" plus imagery-provider attribution; Google doesn't license removal.
- Allowed: "news broadcasts, television shows, films, documentaries, music videos, and any educational purposes". Prohibited: "promotional films, advertisements or commercials, including anything used specifically to sell or promote a product, business, or organization" ([Geo guidelines](https://about.google/brand-resource-center/products-and-services/geo-guidelines/)).

### Cesium

- **Cesium for Unreal** is free and Apache-2.0. Latest **v2.30.0 (1 Oct 2026)**, supports UE 5.8; **streams Gaussian-splat 3D Tiles (`KHR_gaussian_splatting`) since v2.24.0 (Mar 2026)**; vector-tile/GeoJSON overlays since v2.27.0 ([CHANGES.md](https://github.com/CesiumGS/cesium-unreal/blob/main/CHANGES.md), read in full).
- Cesium ion: videos allowed with visible attribution; Community plan is non-commercial only; Bing imagery available via ion until 2028; Google 2D tiles added Oct 2025 ([blog](https://cesium.com/blog/2025/10/02/introducing-google-maps-2d-tiles/)). Bentley acquired Cesium in Sept 2024.

### OpenStreetMap

- Not queryable from the research container. Check how well the Bloemfontein campus is mapped by running [`scripts/ufs-campus.overpassql`](scripts/ufs-campus.overpassql) at [overpass-turbo.eu](https://overpass-turbo.eu), or the quick bounding-box test `way[building](-29.118,26.170,-29.100,26.198);out tags;`.
- ODbL attribution: "© OpenStreetMap contributors" in the credits ([OSMF guidelines](https://osmfoundation.org/wiki/Licence/Attribution_Guidelines)).

### Building footprints and heights

- **Microsoft:** heights are per-building neural-net estimates; −1 where unknown. CDLA Permissive 2.0 per Microsoft's README (Overture lists it under ODbL — follow Microsoft's README).
- **Google Open Buildings v3:** 1.8B detections in Africa, Latin America, the Caribbean, South and South-East Asia (inference May 2023). **2.5D Temporal:** annual 2016–2023 height raster, 0–100 m.
- **Overture:** best single source for footprints with `height`; warns ML footprints are less precise "in the Global South".
- Use these for **distant city massing**, not campus hero buildings.

### Elevation

- GLO-30 and AW3D30 are **surface** models — fine for far landscape (Naval Hill, the Maluti escarpment behind Qwaqwa), wrong for campus ground. NASADEM/SRTM are 30 m terrain.
- SA higher-res options (NGI 25 m DEM, Stellenbosch SUDEM 5 m) are **UNVERIFIED**. For campus ground, use your own drone DSM.

### Imagery

- **NGI** recurring national colour aerial photography (~0.25–0.5 m) is the best free/cheap backdrop drape if the licence allows broadcast — confirm with NGI. **Mangaung Metro GIS** may hold newer municipal aerials.
- **Esri Wayback** is useful for seeing what changed (e.g. the 2026 residences) and choosing imagery dates.

### Existing UFS 3D and on-campus partners

- UFS publishes 360° tours of all three campuses and a Bloemfontein virtual orientation. No UFS digital twin, Matterport, Sketchfab model or campus LiDAR was found (**UNVERIFIED** as a negative). Street View coverage on campus **UNVERIFIED**.
- **MAGIC** drone-imaging group (R11m Merensky grant) — [Polity](https://www.polity.org.za/article/ufs-magic-lab-the-go-to-geological-drone-imaging-group-in-south-africa-2022-03-29).
- **Geography department** UAV photogrammetry research — [doi:10.1177/03091333221101057](https://doi.org/10.1177/03091333221101057).

### Capture-it-yourself software (read on GitHub unless marked)

- [gsplat](https://github.com/nerfstudio-project/gsplat) (Apache-2.0, v1.6.0), [Nerfstudio](https://github.com/nerfstudio-project/nerfstudio) (Apache-2.0), [Brush](https://github.com/ArthurBrussee/brush) (Apache-2.0), [OpenDroneMap](https://github.com/OpenDroneMap/ODM) (AGPL-3.0; orthophotos, DSMs, meshes, 3D Tiles).
- **Avoid the original Inria 3DGS code for paid work** — non-commercial only ([licence](https://github.com/graphdeco-inria/gaussian-splatting/blob/main/LICENSE.md)).
- Renderers: [XScene UE plugin](https://github.com/xverse-engine/XScene-UEPlugin) (Apache-2.0), [KIRI Blender add-on](https://github.com/Kiri-Innovation/3dgs-render-blender-addon) (GPL-2.0), Cesium for Unreal (splat 3D Tiles).
- RealityScan, Metashape, Pix4D, DJI Terra, Postshot pricing: see `05-production-pipeline.md`.

## Recommended data stacks

**(a) Fast and cheap (days, ~US$0–150)**

1. Decide whether the film is promotional (see the README).
2. *Documentary/educational:* Google Earth Studio fly-ins (Bloemfontein city approach; Qwaqwa mountain approach), attribution kept, cutting to real drone and ground footage for everything at campus scale.
3. *Promotional:* no Google pixels in the final film. Cesium for Unreal + Cesium ion Commercial (one month, US$149) for terrain and imagery, credited; or a stylised "data" look in Blender with Blosm using OSM/Overture footprints and GLO-30 terrain. Google tiles for previs only.

**(b) High fidelity (weeks; cost is mostly drone crew and compute)**

1. Commission SACAA-compliant drone photogrammetry of all three campuses: nadir + oblique at 2–3 cm GSD, with RTK or ground control. Partner with MAGIC or Geography if possible.
2. Process in RealityScan (licensed if UFS is over the revenue threshold), Metashape Pro or DJI Terra; OpenDroneMap as a free fallback.
3. Capture hero spaces (Main Building, Red Square, Thakaneng Bridge, Qwaqwa landmarks) and key interiors as Gaussian splats (Postshot or gsplat).
4. Assemble in UE 5.8: Cesium for Unreal for geo-placement and splat 3D Tiles; GLO-30/AW3D30 context terrain; NGI orthophoto drape (licence permitting); Overture/Microsoft massing for distant city blocks.
5. You then own the data: cache it, modify it, re-render it freely.
