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

np.average(df["Values"], weights=GetWeights(df["PictureDay"], df["SurveyDay"]))
