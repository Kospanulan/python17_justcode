
from datetime import datetime, timezone, timedelta

current_datetime = datetime.now()

# current_utc_datetime = str(datetime.utcnow())
current_utc_datetime = datetime.now(tz=timezone.utc)

print(f"{str(current_datetime) = }")
print(f"{str(current_utc_datetime) = }")








# print(f"{str(current_datetime) = }")
