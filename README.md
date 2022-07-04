# Project description:  
[数据+代码] 上市公司年报文本分词、关键词词频统计+数字化转型关键词表...可以根据“创新、数字化等关键词+Word2vec相似词扩充”计算词典的词频作为代理变量；

# How to use:  
1)根据1-3文件夹里面的数据将所需文件放在运行目录下面；  
2)在Jupyter Notebook运行 Wordfreq_Davion.py 主程序；  

# Dataset description:
1)test.txt 文件存放上市公司文本数据，可以根据爬取的PDF文件转换为该纯文本格式；    
2)stopwordlist.txt 文件为停用词词典；   
3)add_word_list.txt 文件格式是"单词"+"空格"+"n"，或者其他vn、a、nr等词性；针对词典可能存在的“专有名词、网络名词和歧义分割”等缺陷，定义用户词典，同时可以对词性进行过滤；该项目中存放了与上市公司数字化转型相关的关键词表；    
4)synonym_list.xlsx 文件为同义词词典，需要用户自定义；第一列为'origin'，第二列为'new'，分别对应原始词语和替换后的词语；  
5)synonym_list.txt 文件为同义词词典，需要用户自定义；每行为互为同义词的几个词语，空格隔开(公司 企业 集团)，行首的词语为最终替换词语(最终全部合并为“公司”)；  
6)word_freq.xlsx 文件为不考虑同义词的词频结果；word_freq1.xlsx 文件为考虑同义词的词频结果；word_freq2.xlsx 文件为直接依据word_freq.xlsx 文件结果，进而考虑同义词的词频结果；  

# Contact me:  
👋 Hi, I’m @DavionWu2018  
👀 I’m interested in sustainable tourism, tourism firm management, text mining, and event study.  
🌱 I’m currently learning tourism management.  
💞️ I’m looking to collaborate on text mining of tourism big data.  
📫 How to reach me: dwu@mail.nankai.edu.cn.  
