from datetime import datetime
import pytz

def time_zone_convertor(time_str, from_tz, to_tz, time_format="%Y-%m-%d %H:%M:%S"):
    try:
        from_timezone = pytz.timezone(from_tz)
        to_timezone = pytz.timezone(to_tz)
        naive_time = datetime.strptime(time_str, time_format)
        localized_time = from_timezone.localize(naive_time)
        converted_time = localized_time.astimezone(to_timezone)
        return converted_time.strftime(time_format)
    except Exception:
        return f'Error'