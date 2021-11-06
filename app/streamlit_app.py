import streamlit as st
import pandas as pd
import os
import sys
if os.path.abspath(".") not in sys.path: sys.path.append(os.path.abspath("."))
from src.text import TextColumn
from src.numeric import NumericColumn
from src.datetime import DateColumn

import matplotlib.pyplot as plt


def Func_Numeric():
    st.title('2. Numeric Column Information')

    for i, column in enumerate(numeric_columns):
        values = []

        obj = NumericColumn(col_name=column, serie=data[column])

        values.append(obj.get_unique())
        values.append(obj.get_missing())
        values.append(obj.get_zeros())
        values.append(obj.get_negatives())
        values.append(obj.get_mean())
        values.append(obj.get_std())
        values.append(obj.get_min())
        values.append(obj.get_max())
        values.append(obj.get_median())

        st.write("")
        st.subheader(f'2.{i} Field Name:***{column}***')

        df = pd.DataFrame()
        df['value'] = values

        df.index = ['Number of unique values',
                    'Number of rows with missing values',
                    'Number of rows with 0',
                    'Number of rows with negative values',
                    'Average value',
                    'Standard deviation value',
                    'Minimum value',
                    'Maximum value',
                    'Median value']

        st.dataframe(df)

        print("")
        st.write('**Histogram**')

        fig, ax = plt.subplots(figsize=(20, 7))
        plt.grid(axis='y')
        obj.get_histogram()
        plt.xlabel(obj.col_name)
        plt.ylabel('Count of Records') 
        st.pyplot(fig)

        st.write("")

        st.subheader(f'Most Frequent Values')
        df2 = obj.get_frequent()
        st.write(df2)

def Func_Text():
    st.title('3. Text Column Information')

    for i, column in enumerate(text_columns):
        values = []

        obj = TextColumn(col_name=column, serie=data[column])

    # convert all the result to string to ensure the same data type (string)
    
        values.append(str(obj.get_unique()))
        values.append(str(obj.get_missing()))
        values.append(str(obj.get_empty()))
        values.append(str(obj.get_whitespace()))
        values.append(str(obj.get_lowercase()))
        values.append(str(obj.get_uppercase()))
        values.append(str(obj.get_alphabet()))
        values.append(str(obj.get_digit()))
        values.append(str(obj.get_mode()))
        

        st.write("")
        st.subheader(f'3.{i} Field Name:***{column}***')

        df = pd.DataFrame()
        df['value'] = values

        df.index = ['Number of Unique Values',
                    'Number of Rows with Missing Values',
                    'Number of Empty Rows',
                    'Number of Rows with Only Whitespace',
                    'Number of Rows with Only Lowercases',
                    'Number of Rows with Only Uppercases',
                    'Number of Rows with Only Alphabet',
                    'Number of Rows with Only Digits',
                    'Mode Value']

        st.dataframe(df)

        print("")
        st.write('**Bar Chart**')

        fig, ax = plt.subplots(figsize=(15, 7))
        plt.grid(axis='y')
        plt.xticks(rotation=90)
        obj.get_barchart()
        plt.xlabel(obj.col_name)
        plt.ylabel('Count of Records')
        st.pyplot(fig)
   

        st.write("")
        st.subheader(f'Most Frequent Values')
        
        df2 = obj.get_frequent()
        st.write(df2)


def Func_Datetime():
    st.title('4. Date Time Column Information')

    for i, column in enumerate(datetime_columns):
        values = []

        obj = DateColumn(col_name=column, serie=data[column])

    # convert all the result to string to ensure the same data type (string)
    
        values.append(str(obj.get_unique()))
        values.append(str(obj.get_missing()))
        values.append(str(obj.get_weekend()))
        values.append(str(obj.get_weekday()))
        values.append(str(obj.get_future()))
        values.append(str(obj.get_empty_1900()))
        values.append(str(obj.get_empty_1970()))
        values.append(str(obj.get_min()))
        values.append(str(obj.get_max()))
        

        st.write("")
        st.subheader(f'4.{i} Field Name:***{column}***')

        df = pd.DataFrame()
        df['value'] = values

        df.index = ['Number of unique values',
                    'Number of rows with missing values',
                    'Number of weekend dates',
                    'Number of weekday dates',
                    'Number of days in the future (after today)',
                    'Number of occurrence of 1900-01-01 value',
                    'Number of occurrence of 1970-01-01 value',
                    'Minimum Date',
                    'Maximum Date'
                    ]

        st.dataframe(df)

        print("")

        st.write('**Bar Chart**')

        fig, ax = plt.subplots(figsize=(15, 7))
        plt.grid(axis='y')
        plt.xticks(rotation=90)
        obj.get_barchart()
        plt.xlabel(obj.col_name)
        plt.ylabel('Count of Records')
        st.pyplot(fig)  

        st.write("")

        st.subheader(f'Most Frequent Values')
        df2 = obj.get_frequent()
        st.write(df2)

               

if __name__ == '__main__':
    
    st.title('Data Explorer Tool')
    
    file = st.file_uploader("Choose a CSV file", type=("csv"))
    st.write("")
    try:
        data = pd.read_csv(file)
        
        
        numeric_columns = list(data.dtypes[(data.dtypes == 'float64') | (data.dtypes == 'int64')].index)
        Func_Numeric()
        st.write("")        

        # set the selected columns

        datetimecol = st.multiselect(
					'Which columns do you want to convert to dates'
					,data.columns
                    )

        #datetimecol = 'Last_Update'
        # change type of the selected columns

        data[datetimecol] = data[datetimecol].apply(pd.to_datetime)        

        text_columns = list(data.dtypes[(data.dtypes == 'object') | (data.dtypes == 'category')].index)
        
        Func_Text()

        datetime_columns = list(data.dtypes[data.dtypes == 'datetime64[ns]'].index)
        
        Func_Datetime()        
        
    except:
        pass

