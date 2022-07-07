from datetime import datetime

def printable_datetime():
    now = datetime.now()
    return now.strftime("%m-%d-%Y %H-%M-%S")
