#!/usr/bin/env python
# coding: utf-8

# wordfreq-没有同义词

import os
import jieba
import jieba.posseg as psg
import re
import pandas as pd
def get_stop_dict(file):
    content = open(file,encoding="utf-8")
    word_list = []
    for c in content:
        c = re.sub('\n|\r','',c)
        word_list.append(c)
    return word_list

file_path = input("请输入当前文件夹路径:")
os.chdir(file_path)

stop_file = "stopwordlist.txt"
user_file = "add_word_list.txt"

stop_words = get_stop_dict(stop_file)
file_name = input("请输入文件名字:")
text = open(file_name,encoding="utf-8").read()
jieba.load_userdict(user_file)
text_lines  = text.split('\n')

flag_list = ['n','nz','vn']#a,形容词，v,形容词
counts={}

for line in text_lines:
    line_seg = psg.cut(line)
    for word_flag in line_seg:
        word = re.sub("[^\u4e00-\u9fa5]","",word_flag.word)
        if word_flag.flag in flag_list and len(word)>1 and word not in stop_words:
            counts[word]=counts.get(word,0)+1

word_freq = pd.DataFrame({'word':list(counts.keys()),'freq':list(counts.values())})
word_freq = word_freq.sort_values(by='freq',ascending=False)
word_freq.to_excel("word_freq.xlsx",index=False)

print("done!")



# wordfreq-合并同义词

import os
import jieba
import jieba.posseg as psg
import re
import pandas as pd
def get_stop_dict(file):
    content = open(file,encoding="utf-8")
    word_list = []
    for c in content:
        c = re.sub('\n|\r','',c)
        word_list.append(c)
    return word_list

file_path = input("请输入当前文件夹路径:")
os.chdir(file_path)

stop_file = "stopwordlist.txt"
user_file = "add_word_list.txt"
#add_word_list.txt内容格式是"单词"+"空格"+"n"，或者其他vn、a、nr等词性
synonym_file = "synonym_list.xlsx"
#第一列为'origin'，第二列为'new'，分别对应原始词语和替换后的词语

stop_words = get_stop_dict(stop_file)
synonym_words = pd.read_excel("synonym_list.xlsx")
synonym_origin = list(synonym_words['origin'])
synonym_new = list(synonym_words['new'])

file_name = input("请输入文件名字:")
text = open(file_name,encoding="utf-8").read()
jieba.load_userdict(user_file)
text_lines  = text.split('\n')


flag_list = ['n','nz','vn']#a,形容词，v,形容词
counts={}

for line in text_lines:
    line_seg = psg.cut(line)
    for word_flag in line_seg:
        word = re.sub("[^\u4e00-\u9fa5]","",word_flag.word)
        if word_flag.flag in flag_list and len(word)>1 and word not in stop_words:
            if word in synonym_origin:
                index = synonym_origin.index(word)
                word = synonym_new[index]
            counts[word]=counts.get(word,0)+1

word_freq = pd.DataFrame({'word':list(counts.keys()),'freq':list(counts.values())})
word_freq = word_freq.sort_values(by='freq',ascending=False)
word_freq.to_excel("word_freq1.xlsx",index=False)

print("done!")


# wordfreq-合并同义词2

import pandas as pd
import os

file_path = input("请输入当前文件夹路径:")
os.chdir(file_path)

file_name = input("请输入词频excel文件名：")#列名为word,freq
df = pd.read_excel(file_name)
syn_name = input("请输入同义词txt文件名：")
#每行为互为同义词的几个词语，空格隔开(公司 企业 集团)，行首的词语为最终替换词语(最终全部合并为“公司”)
txt = open(syn_name,encoding="utf-8").read()
txts = txt.split("\n")

for line in txts:
    words = line.split(" ")
    dic = {}
    for word in words:
        dic[word]=words[0]
    df['word']=df['word'].replace(dic)

df['new_freq']=df.groupby(['word'], as_index=False).cumsum()
df = df.drop_duplicates(subset=['word'], keep='last')
df=df[['word','new_freq']]

df.to_excel("word_freq2.xlsx",index=False)#保存新的词频文件
print("done!")


