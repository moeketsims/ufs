# Production pipeline: how to make it, and what it costs

*Researched 3 Oct 2026. Currency at an assumed R18 = US$1 — re-quote at the time of commissioning.*

> **How this was verified.** Vendor sites were mostly unreachable from the research container. Claims rest on search-engine summaries of the cited pages, or on GitHub-hosted code and changelogs that were read in full. **UNVERIFIED** marks anything not tied to a retrieved source (Kling, Higgsfield, Metashape, Polycam, Houdini and Mapbox pricing among them). Tier totals are estimates built from the cited line items.

## Site facts that shape the plan

- The Bloemfontein campus is **~264 ha** (≈650 acres) ([Strategic Development Plan](https://www.ufs.ac.za/docs/librariesprovider8/default-document-library/strategic-development-plan-ufs-bloemfontein-campus.pdf?sfvrsn=2)) — large for a single capture.
- Hero asset: the **Main Building** (1909, former National Monument).
- **Airspace:** the whole main campus is ~8.6–9.1 km from New Tempe aerodrome and inside the Bloemfontein CTR — drone work needs a licensed operator with ATC coordination (see `04-permissions-and-regulations.md`).
- Google 3D coverage of Bloemfontein is probable but unconfirmed, and its licence limits use in a promotional film (see `02-geospatial-data.md`).

## 1. Geospatial engine route (Unreal + Cesium)

**Unreal Engine licensing**

- Rendering linear content (film, broadcast) is royalty-free ([EULA change log](https://www.unrealengine.com/eula-change-log/unreal)).
- Non-game organisations with **> US$1M annual revenue** need the seat-based Unreal Subscription, **US$1,850/seat/year** (≈R33k); free for students, educators and organisations under US$1M ([Engadget](https://www.engadget.com/epic-will-charge-non-game-developers-1850-per-seat-to-use-unreal-engine-162015997.html), [Epic](https://www.unrealengine.com/blog/we-are-updating-unreal-engine-twinmotion-and-realitycapture-pricing-in-late-april)). **Whether a university marketing department counts as "education" is unclear** — confirm with Epic, or contract a studio under the threshold.
- Third-party sites report that from 27 May 2026 the subscription no longer bundles Twinmotion or RealityScan (RealityScan ≈US$1,250/yr above the threshold) — not confirmed on Epic's site.

**Versions that matter**

- **UE 5.7** (Nov 2025): Movie Render Graph improvements, per-layer EXR metadata for compositing ([Epic](https://www.unrealengine.com/news/unreal-engine-5-7-is-now-available)).
- **UE 5.8** (Jun 2026): **MetaHuman Crowd** (Experimental) — Mass-driven crowds that swap full MetaHumans near camera for instanced meshes further away, scaling to thousands ([MetaHuman](https://www.metahuman.com/news/metahuman-5-8-is-now-available), [80.lv](https://80.lv/articles/populate-your-ue5-8-worlds-with-metahuman-crowds)). The in-engine route to "activity".

**Cesium for Unreal** — free, open source; v2.30.0 (1 Oct 2026, UE 5.6+); Gaussian-splat 3D Tiles since v2.24.0; GeoJSON/vector overlays since v2.27.0 ([CHANGES.md](https://github.com/CesiumGS/cesium-unreal/blob/main/CHANGES.md)). Cesium ion Commercial: US$149/mo individual (includes 5,000 Google 3D Tiles sessions/month) or US$524/mo team ([pricing](https://cesium.com/platform/cesium-ion/pricing/)).

**Google Photorealistic 3D Tiles** — cost is negligible for a film (1,000 root requests/month free, then ~US$6 per 1,000; one request ≈ a 3-hour session) ([billing](https://developers.google.com/maps/documentation/tile/usage-and-billing)). The constraint is the licence: on-screen credits, no export/caching/offline use, and promotional videos only for "experiences you build" ([policies](https://developers.google.com/maps/documentation/tile/policies)). The mesh is good from the air and poor at street level.

**Blender alternatives** — [blosm](https://github.com/vvoovv/blosm/wiki/Import-of-Google-3D-Cities) (imports Google 3D Tiles and OSM; Premium adds texture baking) and [BlenderGIS](https://github.com/domlysz/BlenderGIS) (OSM, SRTM, basemaps). Importing Google tiles saves them as local geometry — treat as unsafe for a published film. OSM massing is safe but looks like data blocks, not the real campus.

## 2. Google Earth Studio

Free (by application, Chrome only); attribution watermarked on every frame. Allowed for film, documentary, news and education; **not** for "promotional films, advertisements or commercials" ([FAQ](https://www.google.com/earth/studio/faq/), [Geo guidelines](https://about.google/brand-resource-center/products-and-services/geo-guidelines/)). Fine for previs or a non-promotional educational piece; probably not for a recruitment film.

## 3. Capture route: photogrammetry and Gaussian splats

**Software**

- **RealityScan** (formerly RealityCapture): 2.2 released 24 Jun 2026 (AMD GPU support; 2.1 added LiDAR/SLAM import). Free for students, educators and organisations under US$1M ([RealityScan 2.2](https://www.realityscan.com/news/realityscan-2-2-is-here-with-full-amd-gpu-support-download-today)).
- **Postshot** (local splat training): Indie €26/mo or €204/yr, commercial use allowed; free tier is non-commercial and watermarked ([radiancefields](https://radiancefields.com/platforms/postshot)).
- **gsplat** (Apache-2.0) is safe for commercial work; the **original Inria 3DGS code and its derivatives (incl. 4DGaussians' rasterizer) are non-commercial** ([Inria licence](https://github.com/graphdeco-inria/gaussian-splatting/blob/main/LICENSE.md)).
- Metashape, Polycam, KIRI pricing: **UNVERIFIED**.

**Rendering splats** — no native Unreal support yet ([forum](https://forums.unrealengine.com/t/official-support-for-gaussian-splat-rendering/1767323)). Plugins: [XGRIDS LCC](https://github.com/xgrids/LCC-3DGS-Unreal-Plugin) (UE 5.1–5.8, Sequencer, Cesium, relighting in Pro), Volinga (UE 5.8, 4D splats — [radiancefields](https://radiancefields.com/volinga-adds-4d-gaussian-splatting-to-unreal-engine)), Postshot UE plugin (beta), [XV3DGS](https://github.com/xverse-engine/XV3DGS-UEPlugin) (Apache-2.0, UE 5.0–5.4), Cesium splat 3D Tiles. Luma's UE plugin looks abandoned. Blender: [KIRI 3DGS Render](https://github.com/Kiri-Innovation/3dgs-render-blender-addon). Web: [SuperSplat](https://github.com/playcanvas/supersplat), [Spark](https://github.com/sparkjsdev/spark).

**Moving people as 4D splats** need synchronised multi-camera rigs — impractical for campus crowds. Use filmed plates or MetaHumans.

**Capture effort (estimates)** — with a DJI Mavic 3 Enterprise class drone (2.66 cm GSD at 100 m; Smart Oblique) ([heliguy](https://www.heliguy.com/blogs/posts/how-to-conduct-mapping-missions-with-the-dji-mavic-enterprise-3/)):

| Target | Images | Field time | Processing |
|---|---|---|---|
| Whole Bloemfontein campus (264 ha), nadir only, 80/70 % overlap | ~3,000 | ~1 day | 1–2 days |
| Whole campus with oblique façade passes | ~9,000–15,000 | 1–2 days | 1–3 days on a workstation |
| One landmark (e.g. Main Building) | 300–1,000 drone + 200–500 ground | 2–4 hours | hours |

## 4. Live-action route

- **SA rates:** drone half-day R8k–R18k, full day R15k–R35k, plus R2k–R5k for controlled airspace; drone + ground crew R20k–R55k/day ([AVL](https://audiovisuallab.co.za/journal/drone-videography-south-africa-corporate/)). Premium brand films R90k–R150k+; corporate videos R25k–R120k ex VAT ([AVL costs](https://audiovisuallab.co.za/journal/corporate-video-production-cost/)).
- **The "digital twin" look is mostly a compositing craft:**
  1. Match-move drone plates and align the Unreal/Cesium camera to them; transition wireframe or massing → photoreal footage (wipe, dissolve, scan-line).
  2. Lay data overlays (labels, people-flow, heat maps) onto real footage using Movie Render Graph EXR layers in Nuke, Resolve or After Effects.
  3. Point-cloud or splat → footage reveals.

## 5. Generative AI video

**Current models (examples):** Veo 3.1 (4–8 s clips to 1080p, first/last frame, up to 3 reference images, extension to 141 s, SynthID watermark, children blocked — [Gemini cookbook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_Veo.ipynb)); Sora 2 / 2 Pro (4–20 s — [OpenAI cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/sora/sora2_prompting_guide.ipynb)); Runway (routes gen4.5, Veo 3.1, Seedance and others; `aleph2` video-to-video — [SDK](https://github.com/runwayml/sdk-python)); Luma Ray3.14 (native 1080p, Jan 2026). Kling and Higgsfield (a multi-model aggregator): **UNVERIFIED**. Commercial-use terms per platform: **UNVERIFIED** — check each.

**Where it helps:** mood boards and previs; generic B-roll inserts; **stylising real footage via video-to-video** (the most defensible use — the geometry comes from the camera); extending a real drone still by a few seconds.

**Where it fails:** no model knows UFS's real geometry — unseen façades get invented, signage garbles, shots drift and don't stay consistent. **Not suitable for depicting a heritage building accurately.**

**Ethics:** synthetic "students" in recruitment material can mislead; label AI shots, keep SynthID/C2PA provenance, and don't generate likenesses of real staff or students. EU AI Act Art. 50 disclosure duties may apply if distributed in the EU (**UNVERIFIED**).

## 6. Data-driven "activity"

- **Layers:** people-flow from the timetable (the on-the-hour lecture changeover — see `03`), Wi-Fi association counts or access-control data, traffic and parking, energy per building, sun and shadow studies (`data/sun-times.csv`).
- **Tools:** Unreal Niagara + Cesium GeoJSON overlays; [Kepler.gl](https://github.com/keplergl/kepler.gl) and [deck.gl](https://github.com/visgl/deck.gl) (MIT; TripsLayer; Tile3DLayer).
- **The bottleneck is data access, not tools.** Wi-Fi and access logs are personal information — aggregate and anonymise (POPIA). The timetable alone is enough for a convincing, privacy-safe flow.

## Comparison

| Approach | Realism of the real campus | Activity / people | Effort | Indicative cost | Key licence caveat |
|---|---|---|---|---|---|
| UE + Cesium + Google 3D Tiles | Medium aerial; poor at street level | None by itself | Low–medium | Tiles ≈ free; ion US$149/mo; UE seat US$1,850/yr if not exempt | Credits on screen; no caching; promo scope unclear |
| Cesium terrain + OSM buildings | Low (massing) — good for a stylised "data" look | None | Low | Free–low | Attribution (ODbL) |
| Blender + blosm / BlenderGIS | Medium (Google) or low (OSM) | Manual | Medium | Free; Premium paid | Imported Google tiles ≈ extraction → risky |
| Google Earth Studio | Medium aerial | None | Very low | Free | No promotional use; watermark |
| Drone photogrammetry + splats | **High** for captured buildings | Static | Medium–high | Drone R8k–R35k/day; Postshot €204/yr | SACAA; avoid Inria code |
| Live action | **Highest** | Real people | Medium | R20k–R55k/day; brand film R90k–R150k+ | Airspace; POPIA releases |
| MetaHuman Crowd (UE 5.8) | n/a | Synthetic crowds | Medium | Included with UE | Experimental |
| Generative AI video | Low for a real place | Good for generic crowds | Low | Credits (**UNVERIFIED**) | Disclosure; platform ToS |
| Data viz (Niagara, Kepler.gl, deck.gl) | Abstract overlay | True to data | Medium | Free (MIT) | POPIA on personal data |

## Recommended tiers

**1. Prototype — 1–2 weeks, roughly R30k–R80k (≈US$1.7k–4.5k)**

- UE 5.8 + Cesium for Unreal for aerial establishing shots (Google tiles in the prototype only).
- Postshot splats of 1–2 landmarks from a half-day licensed drone shoot plus ground photos.
- A people-flow mock-up from the real lecture timetable (Niagara or Kepler.gl).
- Generative AI for mood frames only; Earth Studio for internal previs.
- Crew: one Unreal/technical artist, a contracted SACAA-licensed drone operator, an editor.

**2. Showcase film — 1–3 months, roughly R250k–R700k (≈US$14k–39k)**

- Hero visuals from real capture: 2–4 live-action days (drone, gimbal, hyperlapse) + splats/photogrammetry of 5–10 landmarks rendered in Unreal (LCC or Volinga).
- Context and transitions from Cesium terrain and massing (or Google tiles only with written permission).
- Activity: real people on camera (with releases), MetaHuman Crowd for synthetic wides, data overlays from aggregated real data.
- Generative AI only for labelled video-to-video stylisation.
- Crew: producer/director, DoP, licensed drone pilot, photogrammetry/splat technician, 1–2 Unreal artists, compositor/colourist, sound.

**3. Full digital twin + film — 6+ months, roughly R1.5M–R5M+ (≈US$80k–280k)**

- Campus-wide oblique survey (10k+ images, ground control for survey accuracy) → 3D Tiles, plus hero-building splats streamed through Cesium; merge with UFS Facilities CAD/BIM.
- Live data: building-management energy, Wi-Fi occupancy, parking — aggregated for POPIA.
- Outputs: an interactive twin (Unreal and/or web via CesiumJS, deck.gl, SuperSplat) with the film rendered from the same scene. Survey benchmarks run US$10–150+ per acre ([skyebrowse](https://www.skyebrowse.com/news/posts/drone-survey-cost)). An interactive app changes the Unreal licensing position and Google tile costs scale with users.

## Open questions and risks

1. Does Google's "promotional video" allowance cover a stand-alone film? Ask Google, or keep Google tiles to previs.
2. Earth Studio's promotional ban probably rules it out for marketing.
3. Unreal licence status for UFS (education vs. > US$1M revenue), or outsource to a studio under the threshold.
4. Real Google 3D coverage and quality over the campus.
5. Airspace approvals (CTR, New Tempe) and UFS's own drone rules.
6. POPIA releases for filmed students; anonymising any Wi-Fi/access data.
7. Heritage sensitivity of the Main Building — and AI "hallucinating" a monument.
8. Gaussian splats relight poorly and depend on third-party plugins tracking UE versions.
9. Non-commercial research code (Inria 3DGS/4DGS) must stay out of paid work.
10. AI disclosure and provenance; provider terms for Kling/Higgsfield unverified.
11. Exchange-rate and price volatility.
