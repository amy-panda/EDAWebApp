# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import matplotlib.pyplot as plt


## 
@dataclass
class DateColumn:
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

  def get_weekend(self):
    """
    Return number of occurrence of days falling during weekend (Saturday and Sunday)
    """
    return sum(self.serie.dt.dayofweek >4)


  def get_weekday(self):
    """
    Return number of weekday days (not Saturday or Sunday)
    """
    return sum(self.serie.dt.dayofweek <5)
  
  
  def get_future(self):
    """
    Return number of cases with future dates (after today), use Number of days (unique) in the future (after today) instead as per the sample
    """
    today = pd.to_datetime('today').normalize() 
    
    futureday_ct = sum(self.serie.unique() > today)

    return futureday_ct

  def get_empty_1900(self):
    """
    Return number of occurrence of 1900-01-01 value
    """
    On19000101_ct = sum(self.serie == pd.to_datetime('1990-01-01').normalize())
    return On19000101_ct 

  def get_empty_1970(self):
    """
    Return number of occurrence of 1970-01-01 value
    """
    On19700101_ct = sum(self.serie == pd.to_datetime('1990-01-01').normalize())
    return On19700101_ct 

  def get_min(self):
    """
    Return the minimum date
    """
    return self.serie.min()

  def get_max(self):
    """
    Return the maximum date 
    """
    return self.serie.max()

  def get_barchart(self):
    """
    Return the generated bar chart for selected column
    """
    return self.serie.value_counts().plot(kind='bar')

  
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
      percentage.append(cnt / self.serie.count() *100) # do not include <NA> records

    df = pd.DataFrame()
    df['value'] = temp
    df['occurrence'] = occurrence
    df['percentage'] = percentage

  # sort by occurrency in descending order and then by value in ascending order (alphabetically) and ignoring the index
    return df.sort_values(['occurrence','value'], ascending=(False,True),ignore_index=True)
