# To be filled by students
import streamlit as st
import seaborn as sns
from dataclasses import dataclass
import pandas as pd
import matplotlib.pyplot as plt



@dataclass
class NumericColumn:

  col_name: str
  serie: pd.Series
 
  def get_name(self):
    return self.col_name

  def get_unique(self):
    return self.serie.unique().shape[0]

  def get_missing(self):
    return self.serie.isnull().sum()

  def get_zeros(self):
    return self.serie[self.serie == 0].count()

  def get_negatives(self):
    return self.serie[self.serie < 0].count()

  def get_mean(self):
    return self.serie.mean()

  def get_std(self):
    return self.serie.std()
  
  def get_min(self):
    return self.serie.min()

  def get_max(self):
    return self.serie.max()

  def get_median(self):
    return self.serie.median()

  def get_histogram(self):
   return plt.hist(self.serie, bins = 50)

  def get_frequent(self):

    temp = self.serie.unique()
    temp = temp[::-1][:20]

    occurrence = []
    percentage = []

    for val in temp:

      cnt = self.serie[self.serie == val].count()
      occurrence.append(cnt)
      percentage.append(cnt / self.serie.shape[0] * 100)

    df = pd.DataFrame()
    df['value'] = temp
    df['occurrences'] = occurrence
    df['percentage'] = percentage

    return df.sort_values('occurrences', ascending=False)
