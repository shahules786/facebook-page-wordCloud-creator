
# coding: utf-8

# In[ ]:

import collections
from wordcloud import WordCloud,STOPWORDS
import os
import matplotlib.pyplot as plt
import facebook
import requests
import json
from nltk.corpus import stopwords
from PIL import Image
import re

os.chdir("python27")

#extracting data....
with open("token.txt" ,"r") as f:
    token=f.read()
num=100
page=raw_input("enter the page name:")
num=int(input("enter number"))
try: 
     graph=facebook.GraphAPI(token)
     all_fields=["shares","message",]
     all_fields=",".join(all_fields)
     posts=graph.get_connections(page,"posts",fields=all_fields)
        
except Exception as e: 
        print("token expired or page not found error")
        exit(0)
down=0
while (True):
    if(down>num):
            break
    else:
            try:
                fname="wordcloud_{}.txt".format(page)
                with open(fname,"a") as f:
                  for post in posts["data"]:
                        #print(post)
                        f.write(json.dumps(post["message"] + "\n"))
                    
                        down+=1
                        
                  posts=requests.get(posts["paging"]["next"]).json()
            except KeyError:
                    print("no more posts availabe")
                    break

                #creating wordcloud

word_post=[]
c = collections.Counter()
with open("wordcloud_{}.txt".format(page), 'rt') as f:
    for line in f:        
        c.update(line.split(" "))
        message=re.sub(r'(\s)?\ud.*','',line)
        word_post.append(message)
text=" ".join(word_post)        
        
        
stopwordslist=[]
print 'Most common:'
for letter, count in c.most_common(num):
    if(len(letter)<5):
       stopwordslist.append(letter)

text=" ".join(word_post)
print(text)


stopwordslist.append("\ud83d")
stopwordslist.append("\ude0e")
stopwordslist.extend(word.encode("utf-8") for word in stopwords.words("english"))
wordcloud=WordCloud(stopwords=stopwordslist,background_color="black",width=1000,height=1200).generate(text)
plt.imshow(wordcloud)
plt.show()
plt.axis("off")
fname="wordcloud_{}.png".format(page)
image=Image.open(fname)
image.savefig("home//{}.jpeg".format(fname),dpi=(1200,1200))
image.show()



# In[ ]:




# In[9]:




# In[ ]:



