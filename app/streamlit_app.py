import streamlit as st
import pandas as pd
import os
import sys
if os.path.abspath(".") not in sys.path: sys.path.append(os.path.abspath("."))
from src.text import TextColumn
from src.numeric import NumericColumn
from src.datetime import DateColumn
from src.data import Dataset
import matplotlib.pyplot as plt


def Func_Data():
    st.title('1. Overall Information')
    
    da = Dataset(name=file.name, df=data)
  
    '**Name of Table:**', da.get_name()
    '**Number of Rows:**', str(da.get_n_rows())
    '**Number of Columns:**', str(da.get_n_cols())
    '**Number of Duplicated Rows:**', str(da.get_n_duplicates())
    '**Number of Rows with Missing Values:**', str(da.get_n_missing())
    '**List of Columns:**'
    st.text(', '.join(da.get_cols_list()))

    '**Type of Columns:**'
    st.dataframe(pd.DataFrame.from_dict(da.get_cols_dtype(), orient='index', columns=['type']))
    
    rows = st.slider('Select the number of rows to be displayed', min_value=5, max_value=da.df.shape[0], value=5)
    '**Top Rows of Table**'
    st.dataframe(da.get_head(n=rows))

    '**Bottom Rows of Table**'
    st.dataframe(da.get_tail(n=rows))

    '**Random Sample Rows of Table**'
    st.dataframe(da.get_sample(n=rows))



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

        st.subheader(f'2.{i} Field Name: {column}')
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

        st.write('')

        '**Histogram**'
        fig, ax = plt.subplots(figsize=(25, 10))

        try:
            obj.get_histogram()
        except:
            pass
        plt.grid(axis='y')
        plt.xlabel(f'{column} (binned)')
        plt.ylabel('Count of Records')
        st.pyplot(fig)

        st.write("")

        # new_title = f'<p style="thick: bold; font-family:sans-serif; color:Black; font-size: 20px;"><strong>Most Frequent Values</strong></p>'
        # st.markdown(new_title, unsafe_allow_html=True)
        '**Most Frequent Values**'
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
        '**Bar Chart**'

        fig, ax = plt.subplots(figsize=(15, 7))
        plt.grid(axis='y')
        plt.xticks(rotation=90)
        obj.get_barchart()
        plt.xlabel(obj.col_name)
        plt.ylabel('Count of Records')
        st.pyplot(fig)
   

        st.write("")
        '**Most Frequent Values**'
        
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

        '**Bar Chart**'

        fig, ax = plt.subplots(figsize=(15, 7))
        plt.grid(axis='y')
        plt.xticks(rotation=90)
        obj.get_barchart()
        plt.xlabel(obj.col_name)
        plt.ylabel('Count of Records')
        st.pyplot(fig)  

        st.write("")

        '**Most Frequent Values**'
        df2 = obj.get_frequent()
        st.write(df2)

               

if __name__ == '__main__':
    
    st.title('Data Explorer Tool')
    
    file = st.file_uploader("Choose a CSV file", type=("csv"))

    
    if file: 
        extension = file.name.split('.')[1]
        if extension.upper() != 'CSV':
            st.warning('Please note only CSV files are accepted, you can upload another file')
        else:
            data = pd.read_csv(file)
            data.columns.name = file.name  
            da = Dataset(name=file.name, df=data)

            
            Func_Data()
            
            cols = st.multiselect('Which columns do you want to convert to dates', 
                                da.df.columns.tolist()
                                )
            for col in cols:
                try:
                    da.df[col] = pd.to_datetime(da.df[col])
                    st.success('Column converted to datetime')
                except:
                    st.error('This data type is not available, try something else')   

            
            numeric_columns = list(da.df.select_dtypes(include=['float64','int64']).columns)
            Func_Numeric()
            st.write("")
                    
            
            text_columns = list(da.df.select_dtypes(include=['object','category']).columns)
            Func_Text()
            st.write("") 
                
            datetime_columns = list(da.df.select_dtypes(include='datetime64[ns]').columns)
            Func_Datetime()        
            st.write("")           
            

