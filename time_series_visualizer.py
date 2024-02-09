import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col=0,parse_dates=['date'])

# Clean data
df = df.loc[(df['value']>=df['value'].quantile(0.025))
&(df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig,ax=plt.subplots(figsize=(16,6))
    ax=sns.lineplot(data=df,x='date',y='value')
    ax.set(
      xlabel='Date',
      ylabel='Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig



def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = (
        df.copy().groupby(pd.Grouper(freq='M')).mean().rename(columns={'value': 'avg'})
    )
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).strftime('%B')

    df_bar = pd.melt(
        df_bar,
        id_vars=['year', 'month'],
        value_vars=['avg']
    )

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(16, 6))
    sns.set_theme(style='ticks')

    sns.barplot(
        data=df_bar,
        x='year',
        y='value',
        hue='month',
        ax=ax
    )

    ax.set(xlabel='Years', ylabel='Average Page Views')
    plt.legend(
        title='Months',
        loc='upper left',
        labels=[
           "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
    )

    # Set x-axis major tick labels
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy().rename(columns={'value':'views'})
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig,(ax1,ax2)=plt.subplots(1,2,figsize=(16,6))
    sns.boxplot(data=df_box,
               ax=ax1,
               x='year',
               y='views')

    ax1.set(
      xlabel='Year',ylabel='Page Views',title='Year-wise Box Plot (Trend)'
    )

    sns.boxplot(data=df_box,ax=ax2,x='month',y='views',
               order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
