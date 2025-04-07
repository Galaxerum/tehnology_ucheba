def convert_to_12_hour_format(hours, minutes):
    if hours < 12:
        period = "AM"
    else:
        period = "PM"

    if hours == 0:
        hours_12 = 12
    elif hours > 12:
        hours_12 = hours - 12
    else:
        hours_12 = hours
    minutes_str = f"{minutes:02}"

    return f"{hours_12}:{minutes_str} {period}"


print(convert_to_12_hour_format(14, 30))  # выводит "2:30 PM"
print(convert_to_12_hour_format(0, 45))  # выводит "12:45 AM"
