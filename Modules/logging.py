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
    from timeit import default_timer

    return default_timer()