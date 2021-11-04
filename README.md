<h1 align="left">Development of EDA Web App</h1>

# Description
This is an interactive web application develped using Streamlit that will read a provided CSV file by the user and perform some exploratory data analysis on it. The web application needs to be containerised with Docker and will be running using python 3.8.2.
# Authors
## Group 9
- Amy Yang
- Maedeh Mehdizadeh
- Rohan Pereira
- Tina Li

# Structure

    ├── app
    |   ├── __init__.py
    |   └── streamlit_app.py
    ├── src
    |    ├── test
    |    |   ├── __init__.py
    |    |   ├── test_data.py
    |    |   ├── test_datetime.py
    |    |   ├── test_numeric.py    
    |    |   └── test_text.py
    |    ├── __init__.py
    |    ├── data.py
    |    ├── datetime.py
    |    ├── numeric.py
    |    ├── text.py
    |    └── streamlit_app.py
    ├── Dockerfile
    ├── README.md          
    └── requirements.txt
# Instructions

## Available Commands for Docker
### In the project directory, you can run the commands below.

### To run the unittest, you can use:
#### `python -m unittest`

### To build the image, you can use:
#### `docker build -t [imagename] .`

### To run the image, you can use:
For Mac
#### ` docker run -dit --rm --name [containername] -p 8501:8501 -v "${PWD}":/app [imagename]`

For Windows
#### `docker run -dit --rm --name [containername] -p 8501:8501 -v "${Get-Location}":/app [imagename]`
### To check existing built images, you can use:
#### `docker images`

### To check the running container, you can use:
#### `docker ps`

### To refresh the streamlit updates in existing container, you can use:

For Windows
#### `docker stop [containername]; docker image rm [imagename]; docker build -t [imagename] .; docker run -dit --rm --name [containername] -p 8501:8501 -v "${Get-Location}":/app [imagename]`

