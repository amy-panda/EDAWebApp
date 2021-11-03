import streamlit as st
import pandas as pd
import os
import sys
if os.path.abspath(".") not in sys.path: sys.path.append(os.path.abspath("."))
from src.text import TextColumn

import matplotlib.pyplot as plt


def Test_Numeric():
    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 42px;">2. Numeric Column Information</p>'
    st.markdown(new_title, unsafe_allow_html=True)

    for i, column in enumerate(numeric_columns):
        values = []

        obj = numeric.NumericColumn(col_name=column, serie=data[column])

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
        new_title = f'<p style="thick: bold; font-family:sans-serif; color:Black; font-size: 20px;">2.{i} Field Name: <strong>{column}</strong></p>'
        st.markdown(new_title, unsafe_allow_html=True)

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
        new_title = f'<p style="thick: bold; font-family:sans-serif; color:Black; font-size: 20px;"><strong>Histogram</strong></p>'
        st.markdown(new_title, unsafe_allow_html=True)

        fig, ax = plt.subplots(figsize=(20, 7))
        plt.grid(axis='y')
        obj.get_histogram()
        plt.xlabel('Value') # xlabel will be the obj.col_name (binned)
        plt.ylabel('Count') #ylabel will be 'Count of Records'
        st.pyplot(fig)

        st.write("")

        new_title = f'<p style="thick: bold; font-family:sans-serif; color:Black; font-size: 20px;"><strong>Most Frequent Values</strong></p>'
        st.markdown(new_title, unsafe_allow_html=True)
        df2 = obj.get_frequent()
        st.write(df2)

def Func_Text():
    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 42px;">3. Text Column Information</p>'
    st.markdown(new_title, unsafe_allow_html=True)

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
        new_title = f'<p style="thick: bold; font-family:sans-serif; color:Black; font-size: 20px;">3.{i} Field Name: <strong>{column}</strong></p>'
        st.markdown(new_title, unsafe_allow_html=True)

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
        new_title = f'<p style="thick: bold; font-family:sans-serif; color:Black; font-size: 20px;"><strong>Bar Chart</strong></p>'
        st.markdown(new_title, unsafe_allow_html=True)

        fig, ax = plt.subplots(figsize=(15, 7))
        plt.grid(axis='y')
        plt.xticks(rotation=90)
        obj.get_barchart()
        plt.xlabel(obj.col_name)
        plt.ylabel('Count of Records')
        st.pyplot(fig)
   

        st.write("")

        new_title = f'<p style="thick: bold; font-family:sans-serif; color:Black; font-size: 20px;"><strong>Most Frequent Values</strong></p>'
        st.markdown(new_title, unsafe_allow_html=True)
        df2 = obj.get_frequent()
        st.write(df2)


# def Test_Datetime():
#     new_title = '<p style="font-family:sans-serif; color:Black; font-size: 42px;">4. Datetime Column Information</p>'
#     st.markdown(new_title, unsafe_allow_html=True)

# for i, column in enumerate(datetime_columns):
#         values = []

#         obj = datetime.DateColumn(col_name=column, serie=data[column])
        
#         values.append(str(obj.get_unique()))
        
        

if __name__ == '__main__':

    file = st.file_uploader("Upload file", type=("csv"))
    st.write("")
    try:
        data = pd.read_csv(file)
        numeric_columns = list(data.dtypes[(data.dtypes == 'float64') | (data.dtypes == 'int64')].index)
        Test_Numeric()
        text_columns = list(data.dtypes[(data.dtypes == 'object') | (data.dtypes == 'category')].index)
        Func_Text()
        # datetime_columns = list(data['Last_Update'])
        # Test_Datetime()
    except:
        pass

