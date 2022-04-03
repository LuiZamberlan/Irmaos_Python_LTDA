import pytz
from datetime import datetime

brz = pytz.timezone('America/Sao_Paulo')
datetime_brz = datetime.now(brz)
timeformat = datetime_brz.strftime("%Y:%H:%M:%S")
print(timeformat)
