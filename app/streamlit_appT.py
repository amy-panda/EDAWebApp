#streamlit_app.py
import streamlit as st
import pandas as pd
import sys
#sys.path.append('../')
#import src
import os
if os.path.abspath(".") not in sys.path: sys.path.append(os.path.abspath("."))
from src.datetime import DateColumn
import matplotlib.pyplot as plt


def Func_Datetime():
    new_title = '<p style="font-family:sans-serif; color:Black; font-size: 42px;">4. Date Time Column Information</p>'
    st.markdown(new_title, unsafe_allow_html=True)

    for i, column in enumerate(datetime_columns):
        values = []

        #obj = src.datetime.DateColumn(col_name=column, serie=data[column])
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
        new_title = f'<p style="thick: bold; font-family:sans-serif; color:Black; font-size: 20px;">4.{i} Field Name: <strong>{column}</strong></p>'
        st.markdown(new_title, unsafe_allow_html=True)

        df = pd.DataFrame()
        df['value'] = values

        df.index = ['Number of unique values',
                    'Number of rows with missing values',
                    'Number of occurrence of days falling during weekend (Saturday and Sunday)',
                    'Number of weekday days (not Saturday or Sunday)',
                    'Number of cases with future dates (after today)',
                    'Number of occurrence of 1900-01-01 value',
                    'Number of occurrence of 1970-01-01 value',
                    'Minimum Date',
                    'Maximum Date']

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


        
        

if __name__ == '__main__':

    file = st.file_uploader("Upload file", type=("csv"))
    st.write("")
    try:
        data = pd.read_csv(file)

        st.write("")

        # set the selected columns
        st.write(f'text column finished, now is the datetime col')
        datetimecol = st.multiselect(
					'Which columns do you want to convert to dates'
					,data.columns
                    )

        #datetimecol = 'Last_Update'
        # change type of the selected columns
        st.write(f'Orignal df')
        st.dataframe(data) #ok -shot the original df
        st.write("")
        st.write(f'Selected DateTime Col')
        st.text(datetimecol) #ok- show the selected column
        st.write("")
        
        #datetimecol='Last_Update'
        #df1=data[datetimecol].apply(pd.to_datetime, errors='coerce')
        #data[datetimecol]= pd.to_datetime(data[datetimecol]) # only works with datetimecol='Last_Update'
        #data1 = data[[datetimecol]].apply(pd.to_datetime)
        #data.iloc[:, datetimecol]=data.iloc[:, datetimecol].astype('datetime64[ns]')
        #data.iloc[:, datetimecol] = data.iloc[:, datetimecol].apply(pd.to_datetime, errors='coerce')
        data[datetimecol] = data[datetimecol].apply(pd.to_datetime)
        
        st.dataframe(data)
        st.write(print(data.dtypes))# showing none in app but datetime64[ns] in terminal

        datetime_columns = list(data.dtypes[data.dtypes == 'datetime64[ns]'].index)
        st.write(datetime_columns)
        
        
        Func_Datetime()
    except:
        pass

