import unittest
import pandas as pd
import sys
import os
from pandas._libs.missing import NA
from pandas.util.testing import assert_frame_equal
if os.path.abspath(".") not in sys.path: sys.path.append(os.path.abspath("."))
from src.text import TextColumn

class TestTextColumn(unittest.TestCase):
    def setUp(self):  
        self.data=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/01-01-2021.csv')

    def tearDown(self):
        del self.data
    
    def test_get_name(self):
        df=pd.DataFrame(self.data)
        tcol=TextColumn(col_name='ISO3',serie=df['ISO3'])        
        expected='ISO3'
        result=tcol.get_name()
        
        self.assertEqual(result,expected)

    def test_get_unique(self):
        df=pd.DataFrame(self.data)
        tcol=TextColumn(col_name='ISO3',serie=df['ISO3'])
        expected=6
        result=tcol.get_unique()
        
        self.assertEqual(result,expected)  
        
        
    def test_get_missing(self):
        df=pd.DataFrame(self.data)
        tcol=TextColumn(col_name='ISO3',serie=df['ISO3'])
        expected=0
        result=tcol.get_missing()
        
        self.assertEqual(result,expected)         
        
    def test_get_empty(self):
        df=pd.DataFrame(self.data)
        tcol=TextColumn(col_name='ISO3',serie=df['ISO3'])
        expected=0
        result=tcol.get_empty()
        
        self.assertEqual(result,expected)        

    
    def test_get_whitespace(self):
        df=pd.DataFrame(self.data)
        tcol=TextColumn(col_name='ISO3',serie=df['ISO3'])
        expected=0
        result=tcol.get_whitespace()
        
        self.assertEqual(result,expected)      
    
    
    def test_get_lowercase(self):
        df=pd.DataFrame(self.data)
        tcol=TextColumn(col_name='ISO3',serie=df['ISO3'])
        expected=0
        result=tcol.get_lowercase()
        
        self.assertEqual(result,expected)        


    def test_get_uppercase(self):
        df=pd.DataFrame(self.data)
        tcol=TextColumn(col_name='ISO3',serie=df['ISO3'])
        expected=58
        result=tcol.get_uppercase()
        
        self.assertEqual(result,expected)        


    def test_get_alphabet(self):
        df=pd.DataFrame(self.data)
        tcol=TextColumn(col_name='ISO3',serie=df['ISO3'])
        expected=58
        result=tcol.get_alphabet()
        
        self.assertEqual(result,expected)
        
     
    def test_get_digit(self):
        df=pd.DataFrame(self.data)
        tcol=TextColumn(col_name='ISO3',serie=df['ISO3'])
        expected=0
        result=tcol.get_digit()
        
        self.assertEqual(result,expected)

    def test_get_mode(self):
        df=pd.DataFrame(self.data)
        tcol=TextColumn(col_name='ISO3',serie=df['ISO3'])
        expected='USA'
        result=tcol.get_mode()
        
        self.assertEqual(result,expected)


    def test_get_frequent(self):
        df=pd.DataFrame(self.data)
        tcol=TextColumn(col_name='ISO3',serie=df['ISO3'])
        expected=pd.DataFrame({'value':['USA','ASM','GUM','MNP','PRI','VIR'],
                               'occurrence':[53,1,1,1,1,1],
                               'percentage':[53/58,1/58,1/58,1/58,1/58,1/58]})

        result=tcol.get_frequent()
        
        # test the data frame with the index number being ignored
        assert_frame_equal(result.reset_index(drop=True),expected.reset_index(drop=True))



if __name__ == '__main__':
     unittest.main()
