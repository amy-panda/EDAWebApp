# To be filled by students

import streamlit as st
import pandas as pd 
import src.data as data 
import src.datetime as datetime
import src.numeric as numeric
import src.text as text

def main():
    st.title("Data Explorer Tool")

    menu = ["Dataset","About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Dataset":
        data_file = st.file_uploader("Choose a CSV file",type = ["csv"])
        if st.button("Process"):
            if data_file is not None:
                df = pd.read_csv(data_file)
                dataTypeSeries = df.dtypes

                st.write("""**Types of Columns**""")
                st.write(dataTypeSeries.astype(str))

                st.write("""**Top Rows of Table**""")
                st.dataframe(df.head(5))
            
            # change the datetime column type
                datetime.transform(df)
                st.dataframe()

            # Display name of column as subtitle
                datecol = "column name of date values"
                st.subheader('4.0 Field Name: {}'.format(datecol))           

    else:
        st.subheader("About")
        st.text("DSP - AT3 Streamlit Web App")
        st.text("Group 9")
		


if __name__ == '__main__':
	    main()
