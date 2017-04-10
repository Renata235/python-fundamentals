from datetime import datetime, timedelta, date, time

print datetime.now()
print datetime.now().strftime('%H - %i - %s')
data1 = datetime(1990, 8, 1, 0,0,0)
data2 = datetime(1990, 8, 1, 1,1,0)
print datetime(1990, 8, 1, 0,0,0).strftime('%d/%b/%Y')
print datetime.now() + timedelta(
    days=4,
    seconds=1231,
    milliseconds=123,
    minutes=21,
    hours=4,
    weeks=1
)

if (data1 - data2).total_seconds() > 3600:
    print 'prazo expirado'
else:
    print 'dentro do prazo'
