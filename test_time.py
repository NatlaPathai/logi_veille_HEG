import datetime
from dateutil.parser import parse

pub_date = ["23.3.2026","12.3.2026","Mon, 13 Apr 2026 09:49:39 +0000","2026-04-27T05:25:01.000Z","Wed, 11 Feb 2026 10:01:12 +0100"]

pub_date_clean = []

for date in pub_date :
    clean = parse(date)
    pub_date_clean.append(clean)

print(pub_date_clean)