import pandas as pd  
wnba_attendance = pd.read_csv("C:/Users/Jake/Desktop/wnba_attendance_alltime.csv")

yearly_attendance = wnba_attendance.groupby(["Year"]).agg({"Attendance": "mean"})

top_games = wnba_attendance.sort_values("Attendance", ascending=False).head(10)

top_teams = wnba_attendance.groupby(["Home Team"]).agg({"Attendance": "mean"}).sort_values("Attendance", ascending=False)

print(yearly_attendance.head())

yearly_attendance.reset_index().to_csv("C:/Users/Jake/Desktop/yearly_attendance.csv", index=False)

print(top_games.head())

top_games.reset_index().to_csv("C:/Users/Jake/Desktop/top_games.csv", index=False)

print(top_teams.head())

top_teams.reset_index().to_csv("C:/Users/Jake/Desktop/top_teams.csv", index=False)