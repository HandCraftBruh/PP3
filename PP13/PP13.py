import json
from collections import Counter

with open ('data.json') as f:                               
    data=json.load(f)

new_data=[]
for item in data['events_data']:
    clnt=item['client_id']
    ctg=item['category']
    if ctg=='report':
        new_data.append(clnt)

lst=Counter(new_data).keys()
print('Кол-во уникальных клиентов: ' + str(len(lst)))

#Сколько уникальных клиентов совершили действия
#с категорией (category) = report?

#'D:\Programs\Works\Python\PP3\PP13\data.json'