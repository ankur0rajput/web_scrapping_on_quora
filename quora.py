# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 07:32:25 2018

@author: Ankur
"""

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

#for hello2.txt..that we get after using lynx -dump and grep command in terminal
    #lynx -dump https://www.quora.com/topic/CAT-Preparation > hello.txt
    #grep https://www.quora.com/topic/ hello.txt > hello2.txt
a = []
with open("hello2.txt", "r") as ins:
    for line in ins:
        a.append(line)
    #used to remove the numbering and extracting only links
mylist=[]
newlist=[]
for i in range(22):
    mylist.append(a[i].split('.'))
    mylist[i].pop(0)
    newlist.append('.'.join(mylist[i]))
    
    
#for hello4.txt..that we get after using lynx -dump and grep command in terminal
    #lynx -dump https://www.quora.com/topic/CAT-Coaching > hello3.txt
    #grep https://www.quora.com/topic/ hello3.txt > hello4.txt
a_1=[]    
with open("hello4.txt", "r") as f:
        for line in f:
            a_1.append(line)
            #print(line)
    #used to remove the numbering and extracting only links
mylist_1=[]
newlist_1=[]
for i in range(34):
    mylist_1.append(a_1[i].split('.'))
    mylist_1[i].pop(0)
    newlist_1.append('.'.join(mylist_1[i]))
            
    
#for removing multiple occurance of same link   
c=[]
for i in newlist:
       if i not in c:
          c.append(i)

for i in newlist_1:
       if i not in c:
          c.append(i)

#for collecting all questions by traversing each links
d=[]    
for i in c:
    html=urlopen(i)
    bsobj=BeautifulSoup(html,"lxml")
    
    namelist =bsobj.findAll("span",{"class":"ui_qtext_rendered_qtext"})
    for name in namelist:
        d.append(name.get_text())

#for traversing to each question and collecting information of number of answers present for that question
        
 
      #...........preparing links for question traversal........
      
e=[]
f=[]        
for i in d:
    if i.endswith('?'):
        i = i[:-1]
        e.append(re.split(r'[.;,\s]\s*', i))
for i in e:
    f.append('-'.join(i))
    

g=[]    
for i in f:
       if i not in g :
          g.append(i)
    
#  h is the dictionary that contains key as questions and value as number of answers available for that question using BeatifulSoup and urllib libraries

h={}   
for i in g:
    try:
        html=urlopen("https://www.quora.com"+"/"+i)
        bsobj=BeautifulSoup(html,"lxml")
        
        namelist =bsobj.findAll("div",{"class":"answer_count"})
        #h.setdefault(i, [])
        for name in namelist:
            h[i]=name.get_text()
            #h[i].append(name.get_text())
    except:
        continue

    

    
#  k is a list containing questions having greater than 4 answers
k=[]
for key, value in h.items():
    if not ((value[0]=='0' and value[1]==' ') or (value[0]=='1' and value[1]==' ') or (value[0]=='2' and value[1]==' ') or (value[0]=='3' and value[1]==' ') or (value[0]=='4' and value[1]==' ')):
        #print(key)
        k.append(key)
 

#..................tags collection........... starts.............  
#  l is the dictionary that contains key as questions and value as list of tags available for that question using BeatifulSoup and urllib libraries         
l={}
for i in k:
    source=urlopen("https://www.quora.com"+"/"+i)  
    soup=BeautifulSoup(source,"lxml")
    x=soup.findAll("span",{"class":"name_text"})
    z=BeautifulSoup(str(x)[1:-1],"lxml")
    q=z.findAll("span","TopicNameSpan TopicName")
    
    l.setdefault(i, [])
    for j in q:
        l[i].append(j.get_text())
        #print(j.text)
        #l[i]=j.get_text()
        
#....................answer collction starts........
# m is the dictionary that contains key as questions and value as list of 4 answers for that question using BeatifulSoup and urllib libraries        
m={}
for p in k:
    source=urlopen("https://www.quora.com"+"/"+p)  
    soup=BeautifulSoup(source,"lxml")
    x=soup.findAll("div",{"class":"ui_qtext_expanded"})
    
    z=BeautifulSoup(str(x)[1:-1],"lxml")
    q=z.findAll("span","ui_qtext_rendered_qtext")
    m.setdefault(p, [])
    for j,i in enumerate(q):
        if j<4:
            m[p].append(i.get_text())
            #print(j,i.get_text())
        
 

#  k is the list of required questions.....................
#  dictionary h is the solution for subtask1(key:questions,value:number of answers)
#  dictionary m is the solution for subtask2(key:questions,value:list of 4 answers for that key question)
#  dictionary l is the solution for subtask3(key:questions,value:list of tags)
            
            
#before running the code please ensure that you internet speed should be good.
#if you are getting error at any point int the code then please run the code again this happens because of slow net speed            
            
#........................................................................end..............
#.....................
    
    
