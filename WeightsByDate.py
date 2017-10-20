import datetime
import numpy as np


def GetWeights(PictureDay, SurveyDay):
    ##### Creating scale
    #SurveyDay = datetime.date.today() # placeholder
    # Adding and subtracting months 
    if SurveyDay.month >=10:
        StartPeriod = datetime.date(SurveyDay.year, SurveyDay.month-3, SurveyDay.day)
        EndPeriod = datetime.date(SurveyDay.year+1, (SurveyDay.month+3)%12, SurveyDay.day)    
    elif SurveyDay <=3:
        StartPeriod = datetime.date(SurveyDay.year-1, (SurveyDay.month+9)%12 + 1, SurveyDay.day)
        EndPeriod = datetime.date(SurveyDay.year, SurveyDay.month+3, SurveyDay.day)
    else:
        StartPeriod = datetime.date(SurveyDay.year, SurveyDay.month-3, SurveyDay.day)
        EndPeriod = datetime.date(SurveyDay.year, SurveyDay.month+3, SurveyDay.day)
    # Convert to days to get the integer
    FirstPeriod = (SurveyDay - StartPeriod).days
    SecondPeriod = (EndPeriod - SurveyDay).days
    ## Need picture day
    #PictureDay = datetime.date(2017,8,15)
    if PictureDay <= SurveyDay:
        PictureDays = (PictureDay - StartPeriod).days
        PictureWeight = float(PictureDays) / FirstPeriod
    else:
        PictureDays = (PictureDay - SurveyDay).days
        PictureWeight = float(PictureDays) / SecondPeriod
    return PictureWeight

#np.average(df["Values"], weights=GetWeights(df["PictureDay"], df["SurveyDay"]))

def Get_Linear_Weight(peak_date,given_date, days_drop_interval = 90):
    '''
    Constructs a triangle which has a peak value of 1 in the peak_date 
    and then linearly descends until it reaches 0 in days_interval days
    
    type(peak_date) = datetime.datetime
    type(given_date) = datetime.datetime
    days_drop_interval = int
    
    Usage:
    
    peak_date=datetime.datetime(2017,10,20)
    given_date=datetime.datetime(2018,1,21)
    Get_Linear_Weight(peak_date,given_date,days_drop_interval=200)
    > 0.9535
    
    Get_Linear_Weight(peak_date,given_date,days_drop_interval=30)
    > 0
    '''
    #peak_date=datetime.datetime(peak_date)
    #given_date=datetime.datetime(given_date)
    diff = peak_date-given_date
    if abs(diff)>datetime.timedelta(days_drop_interval):
        return 0
    return 1-(abs(diff.days)/float(days_drop_interval))

def Get_Uniform_Weight(peak_date,given_date, days_drop_interval = 90):
    '''
    Returns 1 if peak date within specified (days) interval from the given date 
    
    type(peak_date) = datetime.datetime
    type(given_date) = datetime.datetime
    days_drop_interval = int
    
    Usage:
    
    peak_date=datetime.datetime(2017,10,20)
    given_date=datetime.datetime(2018,1,21)
    Get_Linear_Weight(peak_date,given_date,days_drop_interval=200)
    > 1
    
    Get_Linear_Weight(peak_date,given_date,days_drop_interval=30)
    > 0
    '''
    if abs(peak_date-given_date)>datetime.timedelta(days_drop_interval):
        return 0
    return 1