import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters 
import numpy as np

register_matplotlib_converters()


# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")

# Clean data
df = df.set_index("date")
df = df[(df["value"] <= df["value"].quantile(.975)) & (df["value"]  >= df["value"].quantile(.025))]

df.index = pd.to_datetime(df.index)

# df2 = df.loc["date",:].apply(lambda x: x.strftime('%b, %Y')) 

def draw_line_plot():
    # Draw line plot
    

    fig, ax = plt.subplots()
   
    plt.plot(df.index,df["value"])
    plt.ylabel("Page Views")
    plt.xlabel("Date")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
# It should show average daily page views for each month grouped
#  by year. The legend should show month labels and have a title of
#  "Months". On the chart, the label on the x axis should be 
# "Years" and the label on the y axis should be "Average Page Views".
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    # print(df_bar)
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # print(df_bar["month"])
    # print(df_bar["year"])
    caterog = df_bar.groupby([df.index.year, df.index.month],)["value"].agg(np.mean).rename_axis(["year","month"])
    # because we have 11 months not 12.
  
    caterog = caterog.reset_index()
    # monthDict={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
    # caterog['month'] = caterog['month'].apply(lambda data: month_dic[data - 1])
   
    # months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",]
    # caterog['month'] = caterog["month"].apply(lambda data: months[data -1 ])
    
    # print(caterog)
    # print(caterog)
    # # Draw bar plot
    df_pivot = pd.pivot_table(
    caterog,
    values="value",
    index="year",
    columns= "month")
    # Plot a bar chart using the DF
    ax = df_pivot.plot(kind="bar")
    # Get a Matplotlib figure from the axes object for formatting purposes
    fig = ax.get_figure()
    # Change the plot dimensions (width, height)
    fig.set_size_inches(3,4)
    # Change the axes labels
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    plt.legend( ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",])

    plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    print(df_box)
    # Draw box plots (using Seaborn)

    fig,axis = plt.subplots(1,2)
    fig.set_size_inches(7,8)
    sns.boxplot (x = df_box["year"], y = df_box["value"], ax = axis[0]).set(xlabel="Year", ylabel="Page Views")
    sns.boxplot(x=df_box["month"], y=df_box["value"],
              order=['Jan', 'Feb', "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
              ax = axis[1]).set(xlabel="Month", ylabel= "Page Views")
    axis[0].set_title('Year-wise Box Plot (Trend)')
    axis[1].set_title('Month-wise Box Plot (Seasonality)')
    plt.show()
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

# draw_line_plot()
# draw_bar_plot()
draw_box_plot()
