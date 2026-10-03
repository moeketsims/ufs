"""Sunrise, sunset, golden and blue hour for the UFS campuses.

Writes research/data/sun-times.csv for the 1st and 15th of every month
from Nov 2026 to Dec 2027. All times are SAST (Africa/Johannesburg, UTC+2).

    pip install astral==3.2
    python research/scripts/sun_times.py
"""

import csv
import datetime as dt
from pathlib import Path
from zoneinfo import ZoneInfo

from astral import LocationInfo, Observer
from astral.sun import SunDirection, blue_hour, elevation, golden_hour, noon, sun

TZ = ZoneInfo("Africa/Johannesburg")

# GPS points published by UFS (gps-gateway-guide.pdf, the South Campus page
# and the 2016 Qwaqwa profile); the Bloemfontein point is the Visitors
# Centre, see research/data/landmarks.csv. Observer elevation is left at 0:
# astral treats it as height above the visible horizon, and the campuses sit
# on plateaus, not above them. Qwaqwa's real sunrise and sunset can be later
# and earlier than listed where the Maluti peaks block the horizon.
CAMPUSES = {
    "Bloemfontein": (-29.107376, 26.187284),
    "South Campus": (-29.181819, 26.216364),
    "Qwaqwa": (-28.486241, 28.823281),
}

OUT = Path(__file__).resolve().parents[1] / "data" / "sun-times.csv"


def dates():
    d = dt.date(2026, 11, 1)
    while d <= dt.date(2027, 12, 15):
        yield d
        yield d.replace(day=15)
        d = (d.replace(day=1) + dt.timedelta(days=32)).replace(day=1)


def hhmm(t):
    return t.astimezone(TZ).strftime("%H:%M")


def main():
    rows = []
    for name, (lat, lon) in CAMPUSES.items():
        loc = LocationInfo(name, "South Africa", "Africa/Johannesburg", lat, lon)
        obs = Observer(latitude=lat, longitude=lon)
        for d in dates():
            s = sun(obs, date=d, tzinfo=TZ)
            gm = golden_hour(obs, d, SunDirection.RISING, tzinfo=TZ)
            ge = golden_hour(obs, d, SunDirection.SETTING, tzinfo=TZ)
            bm = blue_hour(obs, d, SunDirection.RISING, tzinfo=TZ)
            be = blue_hour(obs, d, SunDirection.SETTING, tzinfo=TZ)
            n = noon(obs, d, tzinfo=TZ)
            rows.append({
                "campus": loc.name,
                "date": d.isoformat(),
                "blue_hour_am": f"{hhmm(bm[0])}-{hhmm(bm[1])}",
                "sunrise": hhmm(s["sunrise"]),
                "golden_hour_am": f"{hhmm(gm[0])}-{hhmm(gm[1])}",
                "solar_noon": hhmm(n),
                "noon_sun_elevation_deg": round(elevation(obs, n), 1),
                "golden_hour_pm": f"{hhmm(ge[0])}-{hhmm(ge[1])}",
                "sunset": hhmm(s["sunset"]),
                "blue_hour_pm": f"{hhmm(be[0])}-{hhmm(be[1])}",
                "daylight_h": round((s["sunset"] - s["sunrise"]).total_seconds() / 3600, 2),
            })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} rows to {OUT}")


if __name__ == "__main__":
    main()
