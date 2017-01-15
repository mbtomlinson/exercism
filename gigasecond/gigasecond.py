from datetime import datetime, timedelta

def add_gigasecond(datetime_input):
    datetime_output = datetime_input + timedelta(0,1000000000)
    return datetime_output
