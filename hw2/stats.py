# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 16:32:33 2021

@author: dim_k
"""

import pandas as pd
import statistics
from nltk.tokenize import word_tokenize


data = pd.read_csv("dialog-babi-task5-full-dialogs-trn.txt", sep='\t', names = ['user', 'bot'])
data = data.dropna()
data = data.reset_index(drop=True)
data [["turn", "user"]] = data["user"].str.split (" ", 1, expand=True)


index = data.index
silence_utt= data['user'] == "<SILENCE>"
all_silence = index[silence_utt]

for sil in reversed(all_silence):
    data.loc[sil-1][1]= data.loc[sil-1][1] + ", " + data.loc[sil][1]

# total number of turns_bot
bot_turns_total = len (index)

data = data.drop(all_silence)

    
index = data.index

# total number of turns_user
user_turns_total = len(index)

data['tokenized_user'] = data.apply(lambda row: word_tokenize(row['user']), axis=1)
data['word_counts_user'] = data.apply(lambda row: len(row['tokenized_user']), axis=1)

#total number of words_user
words_total_user = data['word_counts_user'].sum()

data['tokenized_bot'] = data.apply(lambda row: word_tokenize(row['bot']), axis=1)
data['word_counts_bot'] = data.apply(lambda row: len(row['tokenized_bot']), axis=1)

#total number of words_bot
words_total_bot = data['word_counts_bot'].sum()        


dialogues_total = 0
counter = 0
turns_per_dialog = []
words_per_dialog =[]
for n in data.itertuples(name=None):
    counter+=1
    if n[3] == "1":
        turns_per_dialog.append(counter)
        #words = n[5]
        #words_per_dialog.append(words)
        dialogues_total+=1
        counter = 0

turns_per_dialog.append(counter+1)
turns_per_dialog = turns_per_dialog[1:]


for i in turns_per_dialog:
    


#for x in data.itertuples(name=None):
    #print(x)



#mean_num_turns = statistics.mean(turns_per_dialog)

#std_turns = statistics.stdev(turns_per_dialog)


#print("Mean of the sample is % s " %(statistics.mean(data))) 




