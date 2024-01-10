from datetime import datetime, timezone, timedelta

current_utc_datetime = datetime.now(tz=timezone.utc)

str_datetime = datetime.strftime(current_utc_datetime, '%d-%m-%Y %H:%M:%S.%f %z')

print(f"{str_datetime = }")
print(f"{str(current_utc_datetime) = }")

