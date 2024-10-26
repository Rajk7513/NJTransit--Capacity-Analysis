from datetime import datetime

def time_in_range(current_time, start, end):
    """Helper function to check if current_time is between start and end times."""
    time_format = "%H:%M"
    current = datetime.strptime(current_time, time_format)
    start_time = datetime.strptime(start, time_format)
    end_time = datetime.strptime(end, time_format)
    return start_time <= current <= end_time
