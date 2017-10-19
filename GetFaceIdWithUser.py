import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_pickle("image_survey_metrics.pickle")

AllUsers = pd.DataFrame(df["user_id"].unique())
AllUsers.columns = ["user_id"]
AllUsers["Face"] = None
x = []
for user, userdf in df.groupby("user_id"):
    AllUsers["Face"].loc[AllUsers["user_id"] == user] = scipy.stats.mode(userdf["face_id"])[0]