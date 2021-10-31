FROM python:3.8.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
CMD ["streamlit", "run", "app.py"]