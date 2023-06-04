
from datetime import datetime as dt, timedelta 
def nearest(items):   
    new = []
    #pivot1 = dt.strptime(pivot, '%Y-%m-%d %H:%M:%S')  
    now = dt.now()
    for i in items:
        z = dt.strptime(i, '%Y-%m-%d %H:%M:%S')  
        new.append(z)   
   
    return min(new, key=lambda x: (x>now, abs(x-now)) )
   # time_diff = np.abs([date - pivot for date in items])