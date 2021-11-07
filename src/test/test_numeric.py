import unittest
import pandas as pd
import sys
if os.path.abspath(".") not in sys.path: sys.path.append(os.path.abspath("."))
from src.numeric import NumericColumn
from pandas.util.testing import assert_frame_equal

class Test_Numeric(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_csv( 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/01-01-2021.csv')

    def tearDown(self):
        del self.data

    def test_get_name(self):
        ncol = NumericColumn(col_name='Lat',serie=self.data['Lat'])
        expected='Lat'
        result=ncol.get_name()

        self.assertEqual(result, expected)

    def test_get_unique(self):
        ncol = NumericColumn(col_name='Lat', serie=self.data['Lat'])
        expected = 57
        result = ncol.get_unique()

        self.assertEqual(result, expected)

    def test_get_missing(self):
        ncol = NumericColumn(col_name='Lat', serie=self.data['Lat'])
        expected = 2
        result = ncol.get_missing()

        self.assertEqual(result, expected)

    def test_get_zeros(self):
        ncol = NumericColumn(col_name='Lat', serie=self.data['Lat'])
        expected = 0
        result = ncol.get_zeros()

        self.assertEqual(result, expected)

    def test_get_negatives(self):
        ncol = NumericColumn(col_name='Lat', serie=self.data['Lat'])
        expected = 1
        result = ncol.get_negatives()

        self.assertEqual(result, expected)

    def test_get_mean(self):
        ncol = NumericColumn(col_name='Lat', serie=self.data['Lat'])
        expected = 36.840089285714285
        result = ncol.get_mean()

        self.assertEqual(result, expected)

    def test_get_std(self):
        ncol = NumericColumn(col_name='Lat', serie=self.data['Lat'])
        expected = 10.887035414985837
        result = ncol.get_std()

        self.assertEqual(result, expected)

    def test_get_min(self):
        ncol = NumericColumn(col_name='Lat', serie=self.data['Lat'])
        expected = -14.271
        result = ncol.get_min()

        self.assertEqual(result, expected)

    def test_get_max(self):
        ncol = NumericColumn(col_name='Lat', serie=self.data['Lat'])
        expected = 61.3707
        result = ncol.get_max()

        self.assertEqual(result, expected)

    def test_get_median(self):
        ncol = NumericColumn(col_name='Lat', serie=self.data['Lat'])
        expected = 39.06185
        result = ncol.get_median()

        self.assertEqual(result, expected)

    def test_get_frequent(self):
        ncol = NumericColumn(col_name='Lat', serie=self.data['Lat'])
        expected = pd.DataFrame({'value': [42.7560, 44.2685, 15.0979, 40.3888, 35.5653, 44.5720, 40.5908,
                                           18.2208, 41.6809, 33.8569, 44.2998, 35.7478, 31.0545, 40.1500,
                                           44.0459, 18.3358, 37.7693, 47.4009, 38.4912, 47.5289],
                                 'occurrences': [1]*20,
                                 'percentage': [1.724138]*20})

        result = ncol.get_frequent()

        assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))

if __name__ == '__main__':


     unittest.main()
