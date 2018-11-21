import pandas as pd 
import numpy as np 

data = pd.read_csv("events_Barcelona.csv") 
data = data.drop(data.columns[4:8],axis=1)

#Removing NaN values
data = data.dropna()

data = data[data.coordinates0 != 'None']
data = data[data.coordinates0 != '0']

def strtoint(x):
	for index,row in data.iterrows():
		try:
			return float(x)
		except ValueError:
	return 0

data['coordinates0'] = data['coordinates0'].apply(strtoint)
data['coordinates2'] = data['coordinates2'].apply(strtoint)

from datetime import datetime
    
def unix_converter(x):
	#for index,row in data.iterrows():
	y = datetime.utcfromtimestamp(x/1000).strftime('%Y-%m-%d %H:%M:%S')
	return y

data['time'] = data['Time'].apply(unix_converter)

strin = data.Event[149]

import re

def remove_emoji(string):
	emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
	return emoji_pattern.sub(r'', string)

#data['event'] = data['Event'].apply(remove_emoji)

#from py_translator import Translator

#def translatetoenglish(text):
#    s = Translator().translate(text=a, dest='en').text
#    print(s)
    
#data['event'] = data['Event'].apply(translatetext)
