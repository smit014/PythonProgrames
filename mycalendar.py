
def display_dates(v ,startpoint):
    calander=""
    calander =display_blank(startpoint)
    for z in range(1,int(v+1)):
        calander = str(calander) + str(z)+ "\t" 
        if (startpoint  + z) % 7 == False:
            calander +="\n"
    return calander 

def display_days():
    calander=""
    drange =['sun', 'mon', 'tue', 'wen', 'thr', 'fri', 'sat']
    for s in drange:
        calander +="{}".format(s)+"\t"
    return calander + "\n"

def get_date(mm,year):
    v=30
    
    if mm == 2:
        if check_if_leap_year(year):
            v = 29
        else :
            v = 28
    elif mm in [1, 3, 5, 7, 8, 10, 12]:
        v = 31
    return v;
def display_blank(startpoint):
    calendar = ''
    for i in range(1 ,startpoint+1):
        calendar +="-"+"\t"
    return calendar

def display_startpoint(year,mm):
    start_year =1970
    point =4
    tdays =0
    
    for a in range(start_year,year):
        if check_if_leap_year(a):
            tdays += int(366)
        else:
            tdays += int(365)
    if (mm > 1):
        for x in range(1 ,mm):
            tdays += get_date(x,year)
    if (tdays + point) <= 7:
        startpoint = tdays + point
    else: 
        startpoint =(tdays + point)%7
    return startpoint 

def check_if_leap_year(year):
    if year % 400 ==False:
        return True
    elif year % 100==False:
        return False
    elif year % 4 ==False:
        return True

def display_calender(year,mm):
    calander=""
    calander+="year:{}\n".format(year)
    calander += "Month:{}\n".format(mm)
    calander+= display_days()
    v = get_date(mm,year)
    startpoint = display_startpoint(year,mm)
    calander += display_dates(v ,startpoint)
    calander +="\n"
    print(calander)

#type Input
#year=2012
#mm=6
#display_calender(year,mm)