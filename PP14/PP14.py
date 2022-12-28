import csv

with open ('D:\Programs\Works\Python\PP3\PP14\StudentsPerformance 14.csv') as f:
    stnd = 0
    rds = 0
    for line in f:
        info = line.split(',')
        lunch = info[3]
        ws=info[7]

        if lunch=='"standard"' and ws>'"90"':
            stnd+= 1
        elif lunch == '"free/reduced"' or ws<='"90"':
            rds+=1
    sum=stnd+rds
    prct=stnd/sum*100

    print('Процент абитуриетов с оценкой экзамена по письму более 90,' + 
        '\nкоторые хорошо пообедали перед экзаменом: ' '%.1f' % prct +'%')