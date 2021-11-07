# To be filled by students
import unittest
import pandas as pd
import sys
import os
from pandas._libs.missing import NA
from pandas.util.testing import assert_frame_equal
if os.path.abspath(".") not in sys.path: sys.path.append(os.path.abspath("."))
from src.datetime import DateColumn

class TestDateColumn(unittest.TestCase):
    def setUp(self):  
        self.data=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/01-01-2021.csv')
        self.data['Last_Update'] = self.data['Last_Update'].apply(pd.to_datetime)

    def tearDown(self):
        del self.data
    
    def test_get_name(self):
        df=pd.DataFrame(self.data)
        tcol=DateColumn(col_name='Last_Update',serie=df['Last_Update'])
        expected='Last_Update'
        result=tcol.get_name()
        
        self.assertEqual(result,expected)

    def test_get_unique(self):
        df=pd.DataFrame(self.data)
        tcol=DateColumn(col_name='Last_Update',serie=df['Last_Update'])
        expected=1
        result=tcol.get_unique()
        
        self.assertEqual(result,expected)  
        
        
    def test_get_missing(self):
        df=pd.DataFrame(self.data)
        tcol=DateColumn(col_name='Last_Update',serie=df['Last_Update'])
        expected=0
        result=tcol.get_missing()
        
        self.assertEqual(result,expected)         
        


if __name__ == '__main__':
     unittest.main()
