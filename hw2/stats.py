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
print(f"Total number of bot's turns: {len (index)}.")


data = data.drop(all_silence)

    
index = data.index

# total number of turns_user
print(f"Total number of user's turns: {len (index)}.")

data['tokenized_user'] = data.apply(lambda row: word_tokenize(row['user']), axis=1)
data['word_counts_user'] = data.apply(lambda row: len(row['tokenized_user']), axis=1)

#total number of words_user
print(f"Total number of user's words: {data['word_counts_user'].sum()}.")


data['tokenized_bot'] = data.apply(lambda row: word_tokenize(row['bot']), axis=1)
data['word_counts_bot'] = data.apply(lambda row: len(row['tokenized_bot']), axis=1)

#total number of words_bot
print(f"Total number of bot's words: {data['word_counts_bot'].sum()}.")


dialogues_total = 0
counter = 0
turns_per_dialog = []
words_per_dialog =[]
for n in data.itertuples(name=None):
    counter+=1
    if n[3] == "1":
        turns_per_dialog.append(counter)
        dialogues_total+=1
        counter = 0

turns_per_dialog.append(counter+1)
print(f"Turns per dialogue: {turns_per_dialog[1:]}.")

print(f"Mean dialogue length: {statistics.mean(turns_per_dialog)}.")
print(f"Std of dialogue lenghts: {statistics.stdev(turns_per_dialog)}.")

results = set()
data['tokenized_all']= data['tokenized_user']+data['tokenized_bot']
print(f"Vocabulary size: {len(data['tokenized_all'].apply(results.update))}.")

