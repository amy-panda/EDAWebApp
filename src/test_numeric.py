# To be filled by students
import streamlit as st
import pandas as pd
import os
import sys
sys.path.insert(0,'..')
import numeric
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/dipalira/Melbourne-Housing-Data-Kaggle/master/Data/Melbourne_housing_FULL.csv'
data = pd.read_csv(url)

numeric_columns = list(data.dtypes[(data.dtypes == 'float64') | (data.dtypes == 'int64')].index)


def Test_Numeric():

    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 42px;">2. Numeric Column Information</p>'
    st.markdown(new_title, unsafe_allow_html=True)

    for i,column in enumerate(numeric_columns):

        values = []

        obj = numeric.NumericColumn(col_name = column, serie = data[column])

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

        fig, ax = plt.subplots(figsize = (20,7))
        plt.grid(axis = 'y')
        obj.get_histogram()
        plt.xlabel('Value')
        plt.ylabel('Count')
        st.pyplot(fig)

        st.write("")

        new_title = f'<p style="thick: bold; font-family:sans-serif; color:Black; font-size: 20px;"><strong>Most Frequent Values</strong></p>'
        st.markdown(new_title, unsafe_allow_html=True)
        df2 = obj.get_frequent()
        st.write(df2)




if __name__ == '__main__':
    Test_Numeric()
