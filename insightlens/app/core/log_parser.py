from __future__ import annotations
import re, json, datetime as dt
from typing import Iterable

APACHE_RE = re.compile(r"^(?P<ip>\S+) \S+ \S+ \[(?P<ts>[^\]]+)\] \"(?P<method>\S+) (?P<path>\S+) [^\"]+\" (?P<status>\d{3}) (?P<size>\d+|-) \"[^\"]*\" \"[^\"]*\" (?P<latency>\d+\.\d+)")
SYSLOG_RE = re.compile(r"^(?P<mon>\w{3})\s+(?P<day>\d{1,2})\s+(?P<time>\d{2}:\d{2}:\d{2})\s+(?P<host>\S+)\s+(?P<proc>[^:]+):\s+(?P<msg>.*)")

MONTHS = {m:i+1 for i,m in enumerate(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]) }

def parse_lines(lines: Iterable[str], source: str) -> list[dict]:
    out = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        row = {"text": line, "source": source, "level": None, "ts": None, "extra": {}}
        # JSON log
        if line.startswith("{"):
            try:
                j = json.loads(line)
                row["level"] = j.get("level")
                row["ts"] = j.get("ts")
                row["extra"] = {k:v for k,v in j.items() if k not in ("level","ts")}
            except json.JSONDecodeError:
                pass
        # Apache
        m = APACHE_RE.match(line)
        if m:
            g = m.groupdict()
            row["level"] = "INFO" if g.get("status") and int(g["status"]) < 400 else "ERROR"
            row["ts"] = _apache_ts_to_iso(g["ts"])
            row["extra"].update({k:g[k] for k in ("method","path","status","latency")})
        # Syslog
        sm = SYSLOG_RE.match(line)
        if sm:
            sg = sm.groupdict()
            row["level"] = "INFO" if "error" not in sg["msg"].lower() else "ERROR"
            row["ts"] = _syslog_to_iso(sg)
            row["extra"].update({"process": sg["proc"], "host": sg["host"]})
        out.append(row)
    # Fill missing ts with now
    now_iso = dt.datetime.utcnow().isoformat() + "Z"
    for r in out:
        if r["ts"] is None:
            r["ts"] = now_iso
        if r["level"] is None:
            r["level"] = "INFO"
    return out

def _apache_ts_to_iso(s: str) -> str:
    # 20/Oct/2025:10:06:05 +0000
    day, mon, rest = s.split("/", 2)
    mon_num = MONTHS.get(mon, 1)
    year_time, _tz = rest.split(" ")
    year, time = year_time.split(":", 1)
    iso = f"{year}-{mon_num:02d}-{int(day):02d}T{time}Z"
    return iso

def _syslog_to_iso(g: dict) -> str:
    mon_num = MONTHS.get(g["mon"], 1)
    year = dt.datetime.utcnow().year
    return f"{year}-{mon_num:02d}-{int(g['day']):02d}T{g['time']}Z"
