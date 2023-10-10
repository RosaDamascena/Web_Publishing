from django.shortcuts import render
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64

csv_path = 'weathers/data/austin_weather.csv'


def problem1(request):
    df = pd.read_csv(csv_path)
    context = {
        'df': df
    }
    return render(request, 'weathers/problem1.html', context)

plt.switch_backend('Agg')

def problem2(request):
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df_2014 = df[df['Date'] >= '2014-01-01']
    x_value = df_2014['Date']
    xtick_labels = df_2014['Date'].dt.strftime('%Y-%m')
    
    plt.clf()

    plt.figure(figsize=(10, 6))

    plt.plot(x_value, df_2014['TempHighF'], label='High Temperature')
    plt.plot(x_value, df_2014['TempAvgF'], label='Average Temperature')
    plt.plot(x_value, df_2014['TempLowF'], label='Low Temperature')

    plt.title("Temperature Variation")

    plt.ylabel('Temperature (Fahrenheit)')
    plt.xlabel('Date')

    plt.legend(loc='lower center')
    plt.grid()

    plt.xticks(x_value.iloc[::len(x_value)//7], xtick_labels.iloc[::len(xtick_labels)//7])

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()

    context = {
        'chart_image2': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'weathers/problem2.html', context)



def problem3(request):
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df_2014 = df[df['Date'] >= '2014-01-01']
    monthly_avg = df_2014.groupby(df_2014['Date'].dt.strftime('%Y-%m'))[['TempHighF', 'TempAvgF', 'TempLowF']].mean()

    plt.clf()
    plt.figure(figsize=(10, 6))

    x_value = monthly_avg.index
    plt.plot(x_value, monthly_avg['TempHighF'], label='Monthly High Temperature Avg')
    plt.plot(x_value, monthly_avg['TempAvgF'], label='Monthly Average Temperature Avg')
    plt.plot(x_value, monthly_avg['TempLowF'], label='Monthly Low Temperature Avg')

    plt.title("Temperature Variation")
    plt.ylabel('Temperature (Fahrenheit)')
    plt.xlabel('Date')

    plt.legend(loc='lower right')
    plt.grid()

    plt.xticks(x_value[::len(x_value)//7])

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()

    context = {
        'chart_image3': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'weathers/problem3.html', context)


def problem4(request):
    df = pd.read_csv(csv_path)

    df['Events'] = df['Events'].replace(' ', 'No Event')

    event_counts = df['Events'].str.split(' , ').explode().value_counts()

    event_mapping = {event: idx for idx, event in enumerate(event_counts.index)}

    event_values = list(event_mapping.values())
    event_labels = list(event_mapping.keys())

    plt.clf()

    plt.figure(figsize=(10, 6))

    plt.bar(event_values, event_counts.values)
    plt.xticks(event_values, event_labels)
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.title('Weather Event Counts')
    plt.grid()

    buffer = BytesIO()

    plt.savefig(buffer, format='png')

    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')

    buffer.close()

    context = {
        'chart_image4': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'weathers/problem4.html', context)