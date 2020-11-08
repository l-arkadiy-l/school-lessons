seconds = int(input('Введите количество секунд, прошедших с начала суток: '))
minutes = seconds // 60
print('количество полных минут, прошедших с начала суток: {}'.format(minutes))
hours = seconds // 3600
print('количество полных часов, прошедших с начала суток: {}'.format(hours))
seconds_last = seconds % 60
print('количество секунд, прошедших с начала последней минуты: {}'.format(seconds_last))
last_hours = seconds % 3600
print('количество секунд, прошедших с начала последнего часа: {}'.format(last_hours))
last_minutes = minutes % 60
print('количество полных минут, прошедших с начала последнего часа: {}'.format(last_minutes))
