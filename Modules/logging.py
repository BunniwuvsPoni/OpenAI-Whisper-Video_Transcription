# Function: Logging
def log(logfilepath, logmessage):
    import logging

    # "w" overwrites instead of the default behaviour of append
    logging.basicConfig(filename=logfilepath,
                        level=logging.DEBUG,
                        format='%(asctime)s %(message)s',
                        filemode="a")
    
    logging.debug(logmessage)

# Function: Current Time
def time():
    from datetime import datetime

    return datetime.now()

# Function: Convert Time to String
def time_to_string(time):
    # Convert datetime to string using strftime()
    date_time_str = time.strftime("%Y-%m-%d %H:%M:%S")

    return date_time_str