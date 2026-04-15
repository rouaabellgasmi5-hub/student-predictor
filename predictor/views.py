from django.shortcuts import render
import pandas as pd

def home(request):
    data = None

    if request.method == "POST":
        file = request.FILES.get('file')
        if file:
            df = pd.read_csv(file)

            # نحسبو moyenne
            df['Average'] = df[['Math', 'English', 'Science']].mean(axis=1)

            # prediction
            df['Result'] = df['Average'].apply(lambda x: 'Pass' if x >= 12 else 'Fail')

            data = df.to_html()

    return render(request, 'home.html', {'data': data})