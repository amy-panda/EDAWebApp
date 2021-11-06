#streamlit_app.py
import streamlit as st
import pandas as pd
import sys
import os
if os.path.abspath(".") not in sys.path: sys.path.append(os.path.abspath("."))
from src.datetime import DateColumn
import matplotlib.pyplot as plt


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
        datetimecol = st.multiselect(
					'Which columns do you want to convert to dates'
					,data.columns
                    )

        # datetimecol = 'Last_Update'
        # change type of the selected columns
        data[datetimecol] = data[datetimecol].apply(pd.to_datetime)

        datetime_columns = list(data.dtypes[data.dtypes == 'datetime64[ns]'].index)
        
        Func_Datetime()
    except:
        pass

