import requests
import pandas as pd
from datetime import datetime

class DataCrawler:
    def __init__(self, stock_symbol):
        self.stock_symbol = stock_symbol
        self.data = None

    def get_data(self):
        url = f'https://m.cafef.vn/du-lieu/ajax/StockChartV3.ashx?symbol={self.stock_symbol}'

        response = requests.get(url)
        data = response.json().get("price", [])
        data.reverse()
        self.data = data
        return self.data

    def format_data(self):
        self.data = self.get_data()
        for data in self.data:
            data[0] = datetime.utcfromtimestamp(data[0]).strftime('%Y-%m-%d')

        df = pd.DataFrame(columns=["date", "close", "volume", "open", "high", "low"], data=self.data)
        return df

    def save_data(self):
        data = self.get_data(self.stock_symbol)
        df = self.format_data(data)
        df.to_csv(f"{self.stock_symbol}.csv", index=False)

crawler = DataCrawler("HPG")
crawler.save_data()