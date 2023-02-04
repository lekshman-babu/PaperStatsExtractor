import requests
import bs4 
import csv

#open csv files
c=open("paper_stats.csv","w",encoding='utf-8')
csvw=csv.writer(c)
r=open("references.csv","w",encoding='utf-8')
csvr=csv.writer(r)

headerc=['title','no of words in abstract','no of words in body','no of images']
csvw.writerow(headerc)
headerr=['reference text','reference links']
csvr.writerow(headerr)

#to remove punctuations
def punct(para):
    punct='''±()=<>:.,/-'''
    for i in punct:
        para=para.replace(i,'')
    return para

#to count no of words
def count(para):
    count=0
    for i in para.split(' '):
        if i.isalpha():
            count+=1
    return count

#request website
link="https://www.nature.com/articles/s41598-023-28880-x"
res=requests.get(link)
soup=bs4.BeautifulSoup(res.text,"lxml")

#select the classes
title=soup.select('.c-article-title')
base=soup.select('.c-article-section__content')
image=soup.select('.c-article-section__figure-link')
reference=soup.select('.c-article-references__text')

#abstract
abs=base[0].text
abstract=punct(abs)
acount=count(abstract)

#body
Body=''
for i in range(1,7):
    Body+=base[i].text
body=punct(Body)
bcount=count(body)


csvlist=[title[0].text,acount,bcount,len(image)]
csvw.writerow(csvlist)

#reference
text=[]
links=[]
for i in range(len(reference)):
    ref=reference[i].text.split('https')
    text.append(ref[0])
    link=reference[i].select('a')
    if len(link)!=0:
        links.append(link[0].text)
    else:
        links.append(" ")
for i in range(len(text)):
    csvlistr=[text[i],links[i]]
    csvr.writerow(csvlistr)

