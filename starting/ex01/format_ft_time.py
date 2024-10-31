from datetime import datetime 
import time

# Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
a = datetime.now()
print("Seconds since January 1, 1970: " + str(time.time()) + " or " + str(format(time.time(), "e")) + " in scientific notation")
print(a.strftime("%b %d %Y"))
