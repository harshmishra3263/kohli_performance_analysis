import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Read CSV file
df=pd.read_csv("dataset.csv")
print(df.head(10))
#find total nimber of runs kohli has scored
total_runs=df["Runs"].sum()
matches=len(df["Runs"])

print(f"Total number of runs kohli has scord{total_runs}")
    #Average of number of runs he had played at differrent position
avg_runs=df["Runs"].mean()
print(f"average runs scored by kohli in {matches} is,{avg_runs}")
#number of matches he has played at differrent position 
positions=df["Pos"].unique()
print(positions)


df["Pos"]=df["Pos"].map({
    3.0:"Batting at 3",
    4.0:"Batting at 4",
    2.0:"Batting at 2",
    1.0:"Batting at 1",
    7.0:"Batting at 7",
    5.0:"Batting at 5",
    6.0:"Batting at 6",
})
print(df[["Runs","Pos","Opposition"]].head())

# pos_counts=df["Pos"].value_counts()
# print(pos_counts)
# print(type(pos_counts))
# pos_values=pos_counts.values
# pos_labels=pos_counts.index
# print(pos_values)
# fig=plt.figure(figsize=(10,7))
# plt.pie(pos_values,labels=pos_labels)
# plt.show()
def show_pie_plot(df,key):
    counts=df[key].value_counts()
    count_index=counts.index
    count_values=counts.values
    fig=plt.figure(figsize=(10,7))
    plt.pie(count_values,labels=count_index)
    plt.show()
# pie chart on opponents

show_pie_plot(df,"Opposition")


    
# no_of_opponents=df["Opposition"].value_counts()
# opponents_values=no_of_opponents.values
# opponents_labels=no_of_opponents.index
# fig=plt.figure(figsize=(10,7))
# plt.pie(opponents_values,labels=opponents_labels)
# plt.show()

show_pie_plot(df,"Pos")



# pie chart on ground
show_pie_plot(df,"Ground")
# pie chart on dismissals

#Total number of scored in different position
runs_at_pos=df.groupby("Pos")["Runs"].sum()

runs_at_pos_values=runs_at_pos.values
runs_at_pos_labels=runs_at_pos.index
fig=plt.figure(figsize=(10,7))
plt.pie(runs_at_pos_values,labels=runs_at_pos_labels)
plt.show()
print(runs_at_pos)

#total sixes with differrent opposiion
total_sixes=df.groupby("Opposition")["6s"].sum()
sixes_with_ops_values=total_sixes.values
sixes_with_ops_labels=total_sixes.index
fig=plt.figure(figsize=(10,7))
plt.pie(sixes_with_ops_values,labels=sixes_with_ops_labels)
plt.show()
print(total_sixes)
#number of centuries scored by kohli in first and second innnings
centuries=df.query("Runs>=100")
print(centuries)
innings=centuries["Inns"]
tons=centuries["Runs"]

fig=plt.figure(figsize=(10,7))
plt.bar(innings,tons,color='blue',width=0.2)
plt.show()
#calculate the dimissial of virat kohli
dismissals=df["Dismissal"].value_counts()
print(dismissals)
dismissals_values=dismissals.values
dismissals_labels=dismissals.index
fig=plt.figure(figsize=(10,7))
plt.pie(dismissals_values,labels=dismissals_labels)
plt.show()

#Against which teams he has scored the most runs
runs=df.groupby("Opposition")["Runs"].sum()
runs_values=runs.values
runs_labels=runs.index
fig=plt.figure(figsize=(10,7))
plt.pie(runs_values,labels=runs_labels)
plt.show()
print(runs)

#Against which team he has score most centuries

#kohli strike rate in first vs second innings
#runs scored by him and 6s played


