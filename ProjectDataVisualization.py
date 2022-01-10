import pandas as pd
import plotly.express as go

df = pd.read_csv("data.csv")
std_df = df.loc[df["student_id"] == "TRL_zet"]
a = df.groupby("level","student_id")["attempt"].mean()

fig = px.scatter(mean,x = "student_id", y = "level", color = "attempt", size = "20",title = "Data")
fig.show()