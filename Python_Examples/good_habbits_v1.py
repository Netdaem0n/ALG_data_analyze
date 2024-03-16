import datetime

data = 12320384728466254240

print(format(data, ",.2f")) # 12,320,384,728,466,253,824.00
print(format(data, ",.2e")) # 1.23e+19
print(f'{data = }') # data = 12320384728466254240

now_time = datetime.datetime.now()
print(now_time) # 2024-03-16 19:20:30.274904
print(f"{now_time: '%d.%m.%y'}") # '16.03.24'
