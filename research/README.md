# UFS cinematic "digital twin" film — research pack

*Prepared 3 Oct 2026. Question: is a fully cinematic, digital-twin-style film of the University of the Free State campuses and their activity doable, and what data do we need?*

## Short answer: yes, with one design choice up front

It is doable, and most of the data either exists or can be captured in a few days. What it **cannot** be is a film built mainly from Google's 3D city data: Google's terms forbid caching or extracting its 3D tiles and limit promotional use, and Google Earth Studio bars promotional films outright. Its 3D coverage also probably stops short of Qwaqwa. So the realistic route is **capture-led**:

1. **Real footage** (drone + ground) of the campuses and their people — the "cinematic" half.
2. **Our own 3D capture** (drone photogrammetry + Gaussian splats) of the hero buildings and spaces — the "digital twin" half. We own this data outright.
3. **Free open data** for the wider context — terrain, city massing, imagery — credited in the end titles.
4. **Data-driven activity overlays** from the lecture timetable and calendar (and, if UFS agrees, aggregated occupancy data) — people-flow, sun studies, time-of-day.
5. **Compositing** ties it together: wireframe → photoreal reveals, model → footage transitions, overlays on real plates.

Generative AI fits only at the edges: mood boards and labelled stylisation of real footage. It cannot depict a real heritage building accurately.

## The constraint that shapes the shoot

Both Bloemfontein campuses sit **inside the Bloemfontein control zone**, and the whole main campus is **~9 km from New Tempe aerodrome** (inside the 10 km limit). Drone work must be done by a SACAA-licensed commercial operator (UASOC + RPC) with ATC coordination, plus written UFS permission. A student or hobbyist cannot legally fly it. Qwaqwa appears to be uncontrolled airspace.

## Decisions needed before going further

1. **Who is it for?** A UFS recruitment/brand film (promotional) vs. a documentary, educational or research piece. This decides whether Google Earth Studio fly-ins are allowed at all.
2. **Is UFS's Department of Communication and Marketing on board?** Their written permission is required for any commercial filming, use of the UFS name, logo and buildings, and doubles as landowner consent for drones.
3. **Scope:** Bloemfontein first, or all three campuses (Bloemfontein, South Campus, Qwaqwa) from the start?
4. **Tier:** prototype (1–2 weeks, ~R30k–R80k), showcase film (1–3 months, ~R250k–R700k) or full interactive twin + film (6+ months, R1.5M+). See `05-production-pipeline.md`.
5. **AI policy:** whether any synthetic people or generated shots are acceptable, and how they're labelled.

## The data we need — and where it stands

| Layer | What | Source | Status |
|---|---|---|---|
| **Where things are** | Landmark positions (17 points incl. all three campus points) | UFS GPS guides, Waze | **In hand** — [`data/landmarks.csv`](data/landmarks.csv), [`.geojson`](data/landmarks.geojson) |
| | Building footprints and names | OSM; UFS campus map + building-number list | Query ready ([`scripts/ufs-campus.overpassql`](scripts/ufs-campus.overpassql)); not run here (network blocked); UFS PDFs to collect |
| | Missing points: Equitas, Red Square, Gates 2–4, residences, South Campus and Qwaqwa footprints | UFS Estates; recce | **Gap** |
| **What it looks like** | Photoreal 3D of hero buildings and spaces | Own drone photogrammetry + Gaussian splats | **Must capture** (licensed operator) |
| | Campus-wide 3D | Own oblique drone survey; Google 3D Tiles only for previs | **Must capture** / licence-gated |
| | Architectural detail, materials | UFS Estates drawings or BIM; recce | **Request** |
| | Aerial orthophoto | NGI national aerial photography; Esri Wayback for change history | **Order / check licence** |
| **The wider setting** | Terrain (Naval Hill, Maluti escarpment) | Copernicus GLO-30, NASADEM (30 m, free) | **Free download** |
| | City massing | Overture / Microsoft / OSM buildings (free) | **Free download** |
| **The life** | Academic calendar 2026–27, events, graduations, sport | UFS calendar PDF, news | **Researched** — [`03-activity-and-atmosphere.md`](03-activity-and-atmosphere.md); get the full 2027 PDF |
| | Daily rhythm | 50-minute periods 07:10–19:00, changeover on the hour | **In hand**; full timetable/venue bookings = **request** |
| | Occupancy or Wi-Fi counts | UFS ICT / Protection Services, aggregated | **Request** (POPIA) |
| | Real people and moments | Live-action shoot with releases | **Must film** |
| **Light and weather** | Sunrise, sunset, golden and blue hour, sun elevation for all three campuses, Nov 2026 – Dec 2027 | Computed | **In hand** — [`data/sun-times.csv`](data/sun-times.csv) |
| | Climate by month | Climate summaries (Bloemfontein); SAWS (Qwaqwa) | Bloemfontein **in hand**; Qwaqwa **gap** |
| **Look and identity** | Brand colours, logo rules | UFS Vision 130 manual (2023), 2025 anniversary marks | **Researched**; logos from UFS |
| | Existing UFS footage and photo archive | UFS DCM; YouTube/Flickr audit | **Request / audit** |
| **Permissions** | Filming, drones, airspace, releases, music, sport rights | See checklist | **To do** — [`04-permissions-and-regulations.md`](04-permissions-and-regulations.md) |

## Best windows (Nov 2026 – Oct 2027)

- **Dec 2026 and late Jun – early Jul 2027 (breaks):** empty campus — best for drone survey and 3D capture.
- **Feb – Mar 2027:** registration, Gateway welcome, Varsity Cup Monday nights at Shimla Park, storm skies — maximum life.
- **Apr – May 2027:** autumn graduations (Callie Human Centre), Open Days, clean warm light.
- **Jul 2027:** Vrystaat Arts Festival on campus; crisp winter light; possible Maluti snow at Qwaqwa.
- Build in contingency days: protests closed or disrupted campuses in Feb and Oct 2025.

## Suggested next steps

1. Answer the decisions above.
2. Open Google Earth's 3D coverage layer over Park West/Universitas, South Campus and Phuthaditjhaba (2 minutes, settles coverage).
3. Run the OSM query to see how well the campus is mapped.
4. Approach UFS DCM (news@ufs.ac.za) with a one-page project brief; ask for Estates drawings, the 2027 calendar, the media archive and an introduction to the MAGIC drone group or Geography department.
5. Get quotes from two or three licensed drone operators with controlled-airspace approval.
6. Prototype on one landmark: Main Building + Red Square + Thakaneng Bridge — a splat capture, a timetable-driven people-flow, and a 30-second model-to-footage transition.

## Files

| File | Contents |
|---|---|
| [`01-campus-inventory.md`](01-campus-inventory.md) | Campuses, 31 landmarks, residences, institutional facts, what changed since 2016 |
| [`02-geospatial-data.md`](02-geospatial-data.md) | Every 3D, map, terrain and imagery source with coverage and licence for video |
| [`03-activity-and-atmosphere.md`](03-activity-and-atmosphere.md) | Calendar, events, daily rhythm, climate, light, 12-month shoot calendar |
| [`04-permissions-and-regulations.md`](04-permissions-and-regulations.md) | Drone law, airspace, UFS rules, POPIA, music, heritage, permissions checklist |
| [`05-production-pipeline.md`](05-production-pipeline.md) | Tools, capture effort, AI video, costed tiers, risks |
| [`data/landmarks.csv`](data/landmarks.csv) / [`.geojson`](data/landmarks.geojson) | Landmark coordinates with confidence and source |
| [`data/sun-times.csv`](data/sun-times.csv) | Sun times for all three campuses (SAST) |
| [`scripts/sun_times.py`](scripts/sun_times.py) | Regenerates the sun table (`pip install astral==3.2`) |
| [`scripts/ufs-campus.overpassql`](scripts/ufs-campus.overpassql) | OpenStreetMap extract for the campuses (untested) |

## How reliable this is

- The research ran from a cloud container whose network policy blocked direct access to most sites (ufs.ac.za, openstreetmap.org, Google, SACAA). Most facts therefore come from **search-engine summaries of the cited pages**, not full reads, and the session's web-search allowance ran out near the end.
- Every document marks unconfirmed claims **UNVERIFIED**. Treat dates, prices and licence readings as "check before you commit"; nothing here is legal advice.
- Computed items (sun times, distances between landmarks and to aerodromes) were calculated locally from the cited coordinates and cross-checked against the research reports.
- Known conflicts are flagged where they occur: Bloemfontein residence count (23 vs 36), Qwaqwa student numbers (~3,800 vs 5,400+), December 2027 graduation dates.
