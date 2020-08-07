
from datetime import date
import time
today = date.today()
today = str(today)
import urllib.request
data = urllib.request.urlretrieve("https://gtfsrt.api.translink.com.au/GTFS/SEQ_GTFS.zip", 'Z:/Data/GTFS Static/GTfS Static/GTFS Static'+today + '.zip')
t = time.time()
print('yes')
while True:
    if time.time()-t >3600:
        print('yes')
        t = time.time()
        try:
            today1 = date.today()
            today1 = str(today1)
            if today1!= today:
                data = urllib.request.urlretrieve("https://gtfsrt.api.translink.com.au/GTFS/SEQ_GTFS.zip", 'C:/Users/n10680535/OneDrive - Queensland University of Technology/Jupyter/GTfS Static/GTFS Static '+today + '.zip')
                print('saved')
                today = today1
            else:
                print('same', time.time())
        except:
            continue
       






