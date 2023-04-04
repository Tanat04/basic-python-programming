def priorityName(level):
    if level == 1:
        return "Low"
    elif level == 2:
        return "Medium"
    elif level == 3:
        return "High"
    else:
        return "N/A"
    
from datetime import datetime
def getTime():
    now = datetime.now()
    return now.strftime("%d/%m/%y %H:%M:%S")
