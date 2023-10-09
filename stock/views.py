from django.shortcuts import render, HttpResponse
import math
import pandas as pd
from stock.models import Stock


def fetch_stock_from_exel_save_into_db():
    df = pd.read_excel('/opt/blog/stock/stock.xlsx')
    df.drop(df.columns[[0]], axis=1, inplace=True)
    df.columns = ['symbol', 'company_name', 'market_cap']
    df['active'] = df['market_cap'].apply(lambda x: False if isinstance(x, str) or math.isnan(x) else True)
    df['market_cap'] = df['market_cap'].apply(lambda x: 0 if isinstance(x, str) else x)
    df = df.dropna()
    print(df)
    data = [Stock(symbol=row['symbol'], company_name=row['company_name'], market_cap=row['market_cap']) for index, row
            in df.iterrows()]
    Stock.objects.bulk_create(data)
    # Stock.objects.all().delete()


# Create your views here.
def stock(request):
    stocks=Stock.objects.all()
    return render(request,'stock/all_stock.html',{'stocks':stocks})
