from datetime import datetime

today = datetime.date(datetime.now())
format_date = str(today.strftime("%d/%m/%Y"))
salling_date = format_date


today_total = [(20.0,), (10.0,), (20.0,)]
today_total = ([tup[0] for tup in today_total])
print(today_total)
total = 0

for i in range(0, len(today_total)):
    num = float(today_total[i])
    total = float(total + num)

print(total)