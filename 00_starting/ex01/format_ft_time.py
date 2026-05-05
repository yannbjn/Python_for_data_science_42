import time
from datetime import datetime

#get time
epoch_time = time.time()

print(f"Seconds since January 1, 1970: {epoch_time:,.4f} or {epoch_time:.2e} in scientific notation")

current_date = datetime.now()
print(current_date.strftime("%b %d %Y"))