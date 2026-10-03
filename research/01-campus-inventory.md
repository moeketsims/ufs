# Campus inventory: what exists, where, and what changed

*Researched 3 Oct 2026.*

> **How this was verified.** Full pages could not be opened from the research container, so facts come from search-engine summaries of the cited pages. Coordinates come mainly from UFS's own GPS pocket guide and GPS Gateway Guide (DMS converted to decimal), cross-checked against Waze place listings (agreement within ~10–100 m). Building materials and architectural style are **not** stated unless a source gave them — a physical recce is needed. Machine-readable points: [`data/landmarks.csv`](data/landmarks.csv) / [`data/landmarks.geojson`](data/landmarks.geojson).

## 1. The three campuses

| Campus | Location | UFS GPS point | Size | Character |
|---|---|---|---|---|
| **Bloemfontein (main)** | 205 Nelson Mandela Drive, Park West [S15] | Visitors Centre −29.107376, 26.187284; academic core ≈ −29.1105, 26.1865 (derived) | **264.29 ha** (four erven plus a farm portion) [S14] | Bounded by Nelson Mandela Drive (north) and Koos van der Walt Street (west) [S14]. Runs ~2 km east–west from the Main Gate to Shimla Park. Historic core (Main Building, Abraham Fischer) ringed by newer residences, lecture buildings and sports fields [S3]. 26,000+ students [S15]. |
| **South Campus** | Oliver Tambo Road (M30), Rocklands, Bloemfontein [S16] | −29.181819, 26.216364 | **UNVERIFIED** | Began in the 1980s as a Vista University satellite; part of UFS since 2004. "Nestled in the hills overlooking" Bloemfontein. Capacity ~4,000 students; lecture rooms, auditorium, library, administration [S16]. First residence June 2016: 270 beds, R57m, UFS's first with grey-water recycling [S18]. |
| **Qwaqwa** | Kestell Road, Phuthaditjhaba, eastern Free State [S19][S21] | −28.486241, 28.823281 | **UNVERIFIED** | At the foot of the Maluti Mountains among sandstone ridges [S19]. Established 1982; part of UFS since 2003 [S20]. Home of the Afromontane Research Unit [S19]. Student numbers conflict: 5,400+ (prospectus) vs ~3,800 [S19][S20]. |

## 2. Bloemfontein campus layout (derived from the coordinates)

Distances from the Main Building, computed from `data/landmarks.csv`:

- **Main Gate (Gate 1)** on Nelson Mandela Drive — north-east corner, ~670 m from the Main Building. The arrival shot.
- **Gate 5 (DF Malherbe)** and the **Visitors Centre** — ~350 m north, beside the **Agriculture Building**. All visitors enter here.
- **Thakaneng Bridge** (~240 m) and the **Sasol Library** (~320 m) sit ~90 m apart to the north-west: the main pedestrian hub.
- **Physics** and **Abraham Fischer** are ~115 m away; the **Centenary Complex** ~200 m south-east; the **Callie Human Centre** ~350 m south-east; the **Odeion** ~440 m east.
- **Shimla Park** is ~1.5 km west in the sports precinct.

## 3. Landmark inventory (Bloemfontein)

| # | Name | Type | Lat, lon | Confidence (method) | Built / architect | Visual notes / why film it | Source |
|---|---|---|---|---|---|---|---|
| 1 | **Main Building** (Bldg 1: blocks 1A–1D) | Heritage administration/academic; former National Monument | −29.11064, 26.18644 | Med-high (Waze). SAHO's 29°6'0"S 26°10'48"E is ~1 km off — don't use it | Cornerstone 19 Dec 1907 (Sir Hamilton Gould-Adams); opened 16 Oct 1909; architect **Frank Taylor**; north wing 1915, south wing 1929; National Monument 7 Oct 1983 | Hero establishing shot; the university's visual origin. Materials/style **UNVERIFIED** (recce) | [S1][S2][S6][S22] |
| 2 | **Red Square** | Central plaza | ≈ −29.110, 26.187 | Low (described as "in front of the Main Building") | **UNVERIFIED** | Modern urban landscaping, water-wise garden, shade trees. First-year welcomes, Gateway gatherings. Crowd/activity shots | [S12][S13] |
| 3 | **Former M.T. Steyn statue site** (Main Building forecourt) | Removed memorial | at #1 | Low | Council voted to relocate 23 Nov 2018; moved to the War Museum, June 2020 (heritage permit) | Older Street View or 3D data may still show it | [S32][S33][S34][S71] |
| 4 | **Abraham Fischer Residence** ("Vishuis", Bldg 102) | Men's residence; former National Monument | −29.11161, 26.18602 | High (UFS guide) | Frank Taylor; opened 16 Oct 1909 by Abraham Fischer; National Monument 27 Dec 1985; oldest UFS residence | Design matches the Main Building. Pair for "1909 origins" | [S3][S4][S7] |
| 5 | **Equitas Building** (Bldg 44; formerly C.R. Swart) | Law faculty | not found | — | Renamed under the council-approved name changes | Square with a pond in front | [S6][S37][S35] |
| 6 | **Former C.R. Swart statue / pond** | Removed memorial | at #5 | — | Pulled down 22–23 Feb 2016 | Part of the campus's transformation history | [S35][S36] |
| 7 | **Thakaneng Bridge** (Bldg 131) | Student centre | −29.10975, 26.18423 | High (UFS guide; Waze agrees) | Architect **UNVERIFIED** (Roodt has a project page) | Busiest student-life space; time-lapse | [S6][S8][S26][S28] |
| 8 | **UFS-Sasol Library** (Bldg 60) | Main library | −29.10968, 26.18329 | High (UFS guide) | Opened 20 Sep 1983 (medium confidence) | Faces the Bridge; 24-hour book drop | [S6][S29] |
| 9 | **Odeion** (Bldg 46) | Music venue | −29.11081, 26.19100 | High (UFS guide; Waze agrees) | **UNVERIFIED** | Visitor parking; interior music sequence | [S6][S7][S24] |
| 10 | **Callie Human Centre** (Bldg 19) | Multipurpose hall | −29.11299, 26.18879 | High (UFS guide; Waze agrees) | **UNVERIFIED** | Graduations and Varsity Netball (see `03`) | [S6][S7][S25] |
| 11 | **Centenary Complex** (Bldg 101) | Lecture / exhibition | −29.11235, 26.18705 | High (UFS guide) | Year **UNVERIFIED** (name suggests the 2004 centenary) | Echoes the Main Building; Open Day venue | [S3][S6][S7][S31] |
| 12 | **Agriculture Building** (Bldg 10) | Faculty | −29.10842, 26.18750 | High (UFS guide) | **UNVERIFIED** | By Gate 5 | [S6][S7][S10] |
| 13 | **Physics Building** (Bldg 4) | Faculty | −29.11057, 26.18526 | High (UFS guide) | **UNVERIFIED** | Next to the Main Building | [S9] |
| 14 | **Kovsiekerk / Kopanong Auditorium** (Bldg 145) | NG church (Gemeente Kovsiekampus) / auditorium | −29.10586, 26.18878 | Medium (plots north of the Main Gate latitude — check the fence line) | Completed 1981 | Corner of DF Malherbe Ave and Nelson Mandela Dr; Kovsie Extravaganza venue | [S6][S7][S30] |
| 15 | **Shimla Park** (Bldg 74) | Rugby stadium | −29.10856, 26.17142 | Med-high (UFS guide; Waze ~90 m away) | Capacity **UNVERIFIED** | Varsity Cup Monday night matches; floodlit aerials | [S7][S27] |
| 16 | **Gate 1 — Main Gate** | Entrance | −29.10757, 26.19239 | High (Waze; Physics dept page) | — | Open 24/7 | [S9][S10][S23] |
| 17 | **Gate 2 — Roosmaryn** | Entrance | not retrieved | — | — | Mon–Fri 06:00–18:00 | [S10][S51] |
| 18 | **Gate 3 — Wynand Mouton Avenue** | Entrance | not retrieved | — | — | Open 24/7 | [S5][S10] |
| 19 | **Gate 4 — Furstenburg Road** | Entrance | not retrieved | — | — | Mon–Fri 06:00–18:00 | [S10] |
| 20 | **Gate 5 — DF Malherbe** | Visitor entrance | −29.107501, 26.186805 | High (UFS maps page) | — | Open 24/7; visitors must use it | [S8][S11] |
| 21 | **Visitors Centre** | Reception | −29.107376, 26.187284 | High (UFS maps page) | — | Issues temporary access cards | [S8][S11] |
| 22 | **DF Malherbe House**, Graduandi Lane — Institute for Reconciliation and Social Justice | Institute | not found | — | Founded 2010 | Linked to the Reitz aftermath | [S39][S40] |
| 23 | **Toa Mageuzi residence** (formerly Reitz) | Residence | not found | — | Renamed 25 Nov 2022 | Kiswahili: "towards transformation" | [S40][S41][S42] |
| 24 | **Modular Lecturing Space & Assessment Centre** | Teaching | not found | — | Completed ~2021 after 22 months | Modern teaching building | [S46] |
| 25–30 | Swimming pool, tennis courts, netball courts, taxi rank, Institutional Advancement (Graduandi Rd), Protection Services | Sport / transport / admin | not retrieved (Waze places exist) | — | — | Taxi rank = commuter flows; Protection Services = access and permits | [S47]–[S53] |
| 31 | **DBSA-funded residences** (Student Residence Project Phase 3) | Residences | site **UNVERIFIED** | — | Operational by July 2026 | Probably missing from current 3D/satellite data | [S66][S67] |

**Not verified:** Paradys experimental farm (the campus does include an 8.52 ha portion of the farm Bloemfontein 654 [S14]); named gardens or heritage trees; current public art. A 2023 academic article on campus sculptures is the best lead for a public-art list [S35].

### Residences (Bloemfontein)

- **Count conflicts:** 36 residences [S41] vs 23 (see `03-activity-and-atmosphere.md`). Confirm with Housing and Residence Affairs.
- **Colleges** [S44] — Central: Akasia, Kagiso, Karee, Soetdoring, Wag-'n-Bietjie. South: Armentum, Emily Hobhouse, Marjolein, Kestell, Lehakwe, Villa Bravado. West: Abraham Fischer, Conlaurês, Imperium, Outeniqua, Harmony.
- **Junior residences list** [S45] (may be dated) — ladies: Akasia, Emily Hobhouse, Kestell, Madelief, Roosmaryn, Soetdoring, Vergeet-My-Nie, Wag-'n-Bietjie, Welwitschia, Harmony, Lehakwe (formerly NJ van der Merwe, renamed 2021 [S43]); men: Abraham Fischer, Armentum, Beyers Naudé, Karee, Khayalami, Tswelopele, Villa Bravado.
- Five residences were renamed in Nov 2022; only Reitz → Toa Mageuzi is confirmed [S41][S42].

## 4. Institutional facts

- **Founded** 1904 in Bloemfontein as **Grey University College**, with six humanities students [S55][S56].
- **Names:** Grey University College (1904–35) → University College of the Orange Free State (1935–50) → University of the Orange Free State / Universiteit van die Oranje-Vrystaat (1950–2001) → **University of the Free State** (2001–) [S55].
- **Motto:** *In Veritate Sapientiae Lux* — "In truth is the light of wisdom" [S55].
- **Size (2025 profile):** 39,639 students (3% distance), **5,018 staff**, 3 campuses, 7 faculties [S60].
- **"Kovsies"** comes from the 1935–50 abbreviation UKOVS. In 2020 the SRC asked for it to be dropped over its exclusionary origins; management agreed to meet them [S57][S58]. The Kovsie brand is still in use [S62].
- **Brand:** red Pantone 187 (≈ #A71930), navy Pantone 2768 (#0F204B), Cool Grey 8C [S62][S64][S72]. Orange was replaced by "cherry red" in the late 1990s [S62]. Current marks: Vision 130 manual (2023) [S63] and 2025 anniversary-logo guidelines [S65].

## 5. What has changed — why existing 3D or satellite data may be stale

1. **2026:** DBSA-financed residences (520 beds across Bloemfontein and Qwaqwa) operational by July 2026 [S66][S67] — site to confirm with University Estates.
2. **~2021:** Modular Lecturing Space & Assessment Centre [S46].
3. **Names and signage:** C.R. Swart → Equitas [S37]; building name review (2021) [S38]; NJ van der Merwe → Lehakwe (2021) [S43]; five residences renamed incl. Reitz → Toa Mageuzi (2022) [S41]; Vision 130 and 2025 anniversary branding [S63][S65].
4. **Statues removed:** C.R. Swart (2016) [S36]; M.T. Steyn (2020) [S32].
5. **Other 2023–2026 construction:** none found, but searches ran out — treat as **UNVERIFIED**, not "none". Ask UFS Estates.

## 6. Visual references

UFS "Places and Spaces" Pinterest board [S68]; Getty Images (~3,300 UFS photos) [S69]; UFS 360° virtual tours of all three campuses ([undergraduate 360 view](https://www.ufs.ac.za/prospective/VirtualExperience/undergraduate-360-view)).

## Gaps to close

- Footprint, size and centre for South Campus and Qwaqwa; coordinates for Equitas, Red Square, Gates 2–4, residences and sports facilities.
- Materials and style per building (recce or UFS Estates drawings); Shimla Park capacity.
- Current public art; the other four 2022 residence renames; any 2023–2026 construction.

## Sources

- [S1] [SAHO: Main Building](https://sahistory.org.za/place/university-free-state-main-building-bloemfontein)
- [S2] [artefacts.co.za: Main Building](https://www.artefacts.co.za/main/Buildings/bldgframes.php?bldgid=7732)
- [S3] [SAHO: Abraham Fischer residence](https://sahistory.org.za/place/abraham-fischer-mens-residence-university-free-state-bloemfontein)
- [S4] [UFS: Abraham Fischer home](https://www.ufs.ac.za/residences/residences/abraham-fischer-home)
- [S5] [UFS campus map (PDF)](https://www.ufs.ac.za/docs/default-source/maps/ufs-campus-map.pdf?Status=Master&sfvrsn=a1a37420_3)
- [S6] [UFS maps and locations (building numbers)](https://www.ufs.ac.za/docs/librariesprovider31/default-document-library/maps-and-locations-5.pdf?sfvrsn=2)
- [S7] [UFS pocket guide (GPS)](https://www.ufs.ac.za/docs/librariesprovider31/default-document-library/pocket-guide.pdf?sfvrsn=2)
- [S8] [UFS GPS Gateway Guide](https://www.ufs.ac.za/docs/default-source/ufs-news-list/gps-gateway-guide.pdf?sfvrsn=d031b721_2)
- [S9] [Physics department location](https://www.ufs.ac.za/natagri/departments-and-divisions/physics-home/general/location)
- [S10] [UFS gates (2014)](https://apps.ufs.ac.za/media/dl/userfiles/documents/News/2014/2014_10/Hekke-A4.pdf)
- [S11] [Access to the Bloemfontein campus](https://www.ufs.ac.za/visitors/visitors-centre/general/access-to-the-bloemfontein-campus)
- [S12] [Bloemfontein campus page](https://www.ufs.ac.za/supportservices/departments/international-affairs/unlisted-pages/ufs-campuses/bloemfontein-campus)
- [S13] [Gateway Bloemfontein 2025 programme](https://www.ufs.ac.za/docs/registrationlibraries/2025-documents/gateway-bloem-campus-2025-programme-updated.pdf?sfvrsn=59381720_1)
- [S14] [Strategic Development Plan, Bloemfontein campus](https://www.ufs.ac.za/docs/librariesprovider8/default-document-library/strategic-development-plan-ufs-bloemfontein-campus.pdf?sfvrsn=2)
- [S15] [Bloemfontein campus prospectus](https://www.ufs.ac.za/docs/default-source/ufs-news-list/prospectus-ufs-bloemfontein-campus.pdf?sfvrsn=3831b721_2)
- [S16] [South Campus page](https://www.ufs.ac.za/supportservices/departments/international-affairs/unlisted-pages/ufs-campuses/south-campus)
- [S18] [Bloemfontein Courant: first South Campus residence](https://www.bloemfonteincourant.co.za/first-residence-ufs-south-campus/)
- [S19] [Qwaqwa campus prospectus](https://www.ufs.ac.za/docs/default-source/ufs-news-list/prospectu-ufs-qwaqwa-campus.pdf?sfvrsn=3631b721_2)
- [S20] [coursematch: UFS campuses](https://coursematch.co.za/blog/exploring-the-campuses-of-ufs-bloemfontein-qwaqwa-and-south)
- [S21] [ufs24: Qwaqwa campus](https://ufs24.co.za/university-free-state-qwaqwa-campus/)
- [S22]–[S27], [S47]–[S54] Waze place listings for the Main Building, Gate 1, Odeion, Callie Human Hall, Thakaneng Bridge, Shimla Park, sports facilities, taxi rank, Gate 2, Institutional Advancement, Protection Services and Visitors Centre (waze.com/live-map)
- [S28] [Roodt: Thakaneng Student Centre](https://roodt.blinkin.co.za/ufs-thakaneng-student-centre/)
- [S29] [UFS library guide](https://ufs.libguides.com/c.php?g=1347744)
- [S30] [Kopanong ministry](https://www.kopanongministry.org/meetkopanong)
- [S31] [KovsieX Open Day (TikTok)](https://www.tiktok.com/@kovsiex/video/7397402594039106822)
- [S32] [News24: M.T. Steyn statue removed (2020)](https://www.news24.com/SouthAfrica/News/university-of-free-state-removes-statue-of-boer-republic-president-mt-steyn-20200630)
- [S33] [OFM: decision to relocate M.T. Steyn statue](https://www.ofm.co.za/article/local-news/267674/ufs-decides-to-relocate-mt-steyn-statue)
- [S34] [UFS: relocation to the War Museum](https://www.ufs.ac.za/templates/news-archive/media-release/2020/june/ufs-to-proceed-with-relocation-of-the-mt-steyn-statue-to-the-war-museum-in-bloemfontein?NewsItemID=7822)
- [S35] [Campus sculptures article (2023)](https://www.tandfonline.com/doi/full/10.1080/02560046.2023.2169728)
- [S36] [TimesLIVE: C.R. Swart statue (2016)](https://www.timeslive.co.za/news/south-africa/2016-02-23-university-of-free-states-cr-swart-statue-has-fallen/)
- [S37] [News24: names at UFS to change (2016)](https://www.news24.com/SouthAfrica/Local/Express-News/names-at-ufs-to-change-20160322)
- [S38] [Building name review project (2021)](https://www.ufs.ac.za/templates/news-archive/campus-news/2021/august/bloemfontein-campus-building-name-review-project-underway)
- [S39] [Institute for Reconciliation and Social Justice](https://www.ufs.ac.za/institute/the-institute-for-reconciliation-and-social-justice-home/general/contact-us)
- [S40] [UFS humanities news](https://www.uv.ac.za/humanities/news?NewsItemID=996)
- [S41] [Council approves five residence name changes (2022)](https://www.ufs.ac.za/templates/news-archive-item/campus-news/2022/december/ufs-council-approves-name-changes-of-five-residences-on-the-bloemfontein-campus)
- [S42] [The Free Stater: Reitz renamed](https://thefreestater.co.za/2022/12/02/ufs-renames-infamous-reitz-four-other-residences-at-campus/)
- [S43] [NJ van der Merwe renamed Lehakwe House](https://www.ufs.ac.za/templates/news-archive/campus-news/2021/march/nj-van-der-merwe-residence-renamed-lehakwe-house?NewsItemID=2720)
- [S44] [Residence life: residences](https://www.ufs.ac.za/residences/housing-and-residence-affairs/residence-life/residences)
- [S45] [Junior accommodation](https://www.ufs.ac.za/residences/housing-and-residence-affairs/information/junior-accommodation/information)
- [S46] [Modular Lecturing Space (2021)](https://www.ufs.ac.za/templates/news-archive/campus-news/2021/june/new-ufs-modular-lecturing-space-and-assessment-centre-building)
- [S55] [Wikipedia: University of the Free State](https://en.wikipedia.org/wiki/University_of_the_Free_State)
- [S56] [Drum: UFS founded (today in history)](https://www.news24.com/drum/news/today-in-history-university-of-free-state-is-founded-20170728)
- [S57] [News24: Kovsies name (2020)](https://www.news24.com/news24/ufs-management-to-meet-with-src-after-call-to-discontinue-use-of-kovsies-20200629)
- [S58] [IOL: Kovsies name (2020)](https://www.iol.co.za/news/south-africa/university-in-talks-with-src-over-kovsies-name-outrage-50109617)
- [S60] [UFS in figures](https://www.ufs.ac.za/about-the-ufs/ufs-in-focus/ufs-in-figures)
- [S62] [Corporate identity elements](https://www.ufs.ac.za/docs/default-source/all-documents/01-corporate-identity-elements.pdf?sfvrsn=3697b921_0)
- [S63] [Vision 130 brand manual (2023)](https://www.ufs.ac.za/docs/narrativeandbrandguidelineslibraries/brand-guidelines/vision-130-brand-manual---2023.pdf?Status=Master&sfvrsn=690e2c20_3)
- [S64] [SRC brand manual (2020)](https://www.ufs.ac.za/docs/default-source/-branding/ufs-src-brand-manual-2020-04.pdf?sfvrsn=3aa46220_3)
- [S65] [Anniversary logo guidelines (2025)](https://www.ufs.ac.za/docs/narrativeandbrandguidelineslibraries/brand-guidelines/anniversary-logo-guidelines-2025.pdf?sfvrsn=bd5ced20_1)
- [S66] [Business Day: purpose-built residences (Jul 2026)](https://www.businessday.co.za/news/2026-07-20-watch-how-purpose-built-residences-are-helping-university-of-the-free-state-students-succeed/)
- [S67] [Engineering News: student accommodation (Jul 2026)](https://www.engineeringnews.co.za/article/student-accommodation-transforms-the-future-for-young-south-africans-2026-07-16)
- [S68] [Pinterest: UFS Places and Spaces](https://za.pinterest.com/kovsies/ufs-places-and-spaces/)
- [S69] [Getty Images: University of the Free State](https://www.gettyimages.com/photos/university-of-free-state)
- [S71] [National Museum: removal of the Steyn statue](https://nationalmuseumpublications.co.za/burning-heritage-issues-the-removal-of-the-president-steyn-statue/)
- [S72] [Education branding guidelines](https://www.ufs.ac.za/docs/default-source/-branding/education-branding-guidelines.pdf?sfvrsn=3e056a20_8)
