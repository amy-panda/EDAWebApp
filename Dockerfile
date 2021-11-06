# To be filled by students
FROM python:3.8

RUN pip install pandas xlrd openpyxl matplotlib seaborn streamlit

ADD src/ ./src

ADD app/ ./app

CMD ["streamlit", "run","app/streamlit_app.py"]