# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import matplotlib.pyplot as plt

@dataclass
class TextColumn:
  col_name: str
  serie: pd.Series
  
  def get_name(self):
    """
    Return name of selected column
    """
    return self.col_name
  
  def get_unique(self):
    """
    Return number of unique values for selected column
    """
  
    return self.serie.nunique()
  
  def get_missing(self):
    """
    Return number of missing values for selected column
    """

    return self.serie.isnull().sum()
    

  def get_empty(self):
    """
    Return number of rows with empty string for selected column
    """

    return self.serie[self.serie==''].count()

  def get_whitespace(self):
    """
    Return number of rows with only whitespaces for selected column
    """
    return self.serie.str.isspace().sum()

  def get_lowercase(self):
    """
    Return number of rows with only lower case characters for selected column
    """
    return self.serie.str.islower().sum()

  def get_uppercase(self):
    """
    Return number of rows with only upper case characters for selected column
    """
    return self.serie.str.isupper().sum()
  
  def get_alphabet(self):
    """
    Return number of rows with only alphabet characters for selected column
    """
    return self.serie.str.isalpha().sum()

  def get_digit(self):
    """
    Return number of rows with only numbers as characters for selected column
    """
    return self.serie.str.isdigit().sum()

  def get_mode(self):
    """
    Return the mode value for selected column
    """
    return self.serie.mode()[0]


  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """

    list_x=list(self.serie.unique())
    list_y=list(self.serie.value_counts())
    return plt.bar(list_x,list_y)


  def get_frequent(self):
    """
    Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
    """
    
    temp = self.serie.unique()
    temp = temp[::-1][:20]

    occurrence = []
    percentage = []

    for val in temp:

      cnt = self.serie[self.serie == val].count()
      occurrence.append(cnt)
      percentage.append(cnt / self.serie.shape[0])

    df = pd.DataFrame()
    df['value'] = temp
    df['occurrence'] = occurrence
    df['percentage'] = percentage

  # sort by occurrency in descending order and then by value in ascending order (alphabetically) and ignoring the index
    return df.sort_values(['occurrence','value'], ascending=(False,True),ignore_index=True)

