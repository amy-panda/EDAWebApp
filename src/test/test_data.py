# To be filled by students
import unittest
import pandas as pd
import sys
import os
from pandas._libs.missing import NA
from pandas.util.testing import assert_frame_equal
if os.path.abspath(".") not in sys.path: sys.path.append(os.path.abspath("."))
from src.data import Dataset

class TestDataset(unittest.TestCase):
    def setUp(self):  
        self.data=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/01-01-2021.csv')

    def tearDown(self):
        del self.data
    
    def test_get_name(self):
        df1=pd.DataFrame(self.data)
        data=Dataset(name='01-01-2021.csv',df=df1)
        expected='01-01-2021.csv'
        result=data.get_name()
        
        self.assertEqual(result,expected)


    def test_get_n_rows(self):
        df1=pd.DataFrame(self.data)
        data=Dataset(name='01-01-2021.csv',df=df1)
        expected=58
        result=data.get_n_rows()
        
        self.assertEqual(result,expected)


    def test_get_n_cols(self):
            df1=pd.DataFrame(self.data)
            data=Dataset(name='01-01-2021.csv',df=df1)
            expected=18
            result=data.get_n_cols()
            
            self.assertEqual(result,expected)

if __name__ == '__main__':
     unittest.main()
