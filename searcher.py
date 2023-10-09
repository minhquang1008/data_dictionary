import pandas as pd


class Data:

    def __init__(self):
        self.__table = None

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        self.__table = value

    def getData(self, column_name):
        sheet_id = '1Rgst7ZPw2b9dj4YXwa24vHzLaLEq4vuv'
        df = pd.read_excel(
            f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx',
            sheet_name=self.table,
            header=2
        )
        df.dropna(axis=0, how='all', inplace=True)
        # df.dropna(axis=1, how='all', inplace=True)
        return df[df['DataMart Column'] == column_name]

        

