#место для твоего кода
def extract_datetime(data):
    print(len(data))
    data = data.split(', ')
    test_data = data[1].split(' ')
    test = int(test_data[1][:2])

    if test >= 18:
        return 'Вечер'
    elif test >= 12:
        return 'День'
    else:
        return 'Утро'

print(extract_datetime('Thu Jul 30, 2020 21:25 UTC'))
Tue Feb 05, 2019