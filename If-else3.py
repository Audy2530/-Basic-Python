work_day = ('Mon','Tue','Wed','Thu','Fri')
Off_day = ('Sat','Sun')

week_day = (input('What day is it :  '))
if week_day in work_day :
        print('Go to Work')
elif week_day in Off_day :
        print('Day off')
else :
        print('Data EROR !!!')
