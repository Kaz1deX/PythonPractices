import csv
import datetime
import matplotlib.pyplot as plt


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


# id, task, variant, group, time
messages = load_csv(
    'D:\Games\GitHub\PythonPractices\Homeworks\HomeWork_3\messages.csv')

# id, message_id, time, status
checks = load_csv(
    'D:\Games\GitHub\PythonPractices\Homeworks\HomeWork_3\checks.csv')

# task, variant, group, time, status, achievements
statuses = load_csv(
    'D:\Games\GitHub\PythonPractices\Homeworks\HomeWork_3\statuses.csv')

message_counts = {i: 0 for i in range(7)}
checks_counts = {i: 0 for i in range(7)}
status_counts = {i: 0 for i in range(7)}

for message in messages:
    day = parse_time(message[4]).weekday()
    message_counts[day] += 1
for check in checks:
    day = parse_time(check[2]).weekday()
    checks_counts[day] += 1
for status in statuses:
    day = parse_time(status[3]).weekday()
    status_counts[day] += 1

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
plt.bar(range(len(days)), message_counts.values(),
        align='center', label='Messages')
plt.bar(range(len(days)), checks_counts.values(),
        align='center', label='Checks')
plt.bar(range(len(days)), status_counts.values(),
        align='center', label='Statuses')
plt.xticks(range(len(days)), days)
plt.xlabel('Day')
plt.ylabel('Student\'s activity')
plt.legend()
plt.show()
