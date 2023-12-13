from datetime import datetime

date_1 = '24/7/2021 11:13:08.230010'
date_2 = '24/7/2021 11:14:18.333338'
date_format_str = '%d/%m/%Y %H:%M:%S.%f'
start = datetime.strptime(date_1, date_format_str)
end =   datetime.strptime(date_2, date_format_str)
# Get interval between two datetimes as timedelta object
diff = end - start
# Get the interval in minutes
diff_in_minutes = diff.total_seconds() / 60
print('Difference between two datetimes in minutes:')
print(diff_in_minutes)