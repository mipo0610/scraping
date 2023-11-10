#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver


# In[2]:


chrome_driver_path = 'C:/chromedriver-win64/chromedriver.exe'  # chromedriver.exeのパスを指定
browser = webdriver.Chrome(executable_path=chrome_driver_path)


# In[3]:


# サウナイキタイの検索ページにアクセスする
browser.get('https://sauna-ikitai.com/search')


# In[4]:


from selenium.webdriver.common.by import By

# NAMEを使ってkeywordの要素を見つける
elem_keyword = browser.find_element(By.NAME, 'keyword')


# In[5]:


# XPATHを使ってkeyword入力要素を見つける
elem_submit = browser.find_element(By.XPATH, '/html/body/div/div[3]/div[1]/form/div/div[1]/div[4]/div/input')


# In[6]:


# keyword入力要素にキーワードを入力する
elem_submit.send_keys('東京')


# In[7]:


# XPATHを使って検索ボタン要素を見つける
elem_submit = browser.find_element(By.XPATH, '/html/body/div/div[3]/div[1]/form/div/div[1]/div[9]/button')


# In[8]:


# 検索ボタンをクリックする
elem_submit.click()


# In[9]:


# 表示オプションの選択要素を見つける
elem_submit = browser.find_element(By.XPATH, '/html/body/div/div[3]/header/div/div/select/option[5]') 


# In[10]:


from selenium.webdriver.support.ui import Select

select = Select(browser.find_element(By.NAME, 'ordering'))
select.select_by_value('male_ikitai_counts_desc')  #イキタイ男性多い順に並び替える


# In[11]:


#サウナ名を取得する
elem_saunaname = browser.find_element(By.CLASS_NAME, 'p-saunaItemName')


# In[12]:


#elements にする
elems_saunaname = browser.find_elements(By.CLASS_NAME, 'p-saunaItemName')


# In[13]:


# データ数を確認する
len(elems_saunaname)


# In[14]:


titles = []
for elem_saunaname in elems_saunaname:
    elem_title = elem_saunaname.find_element(By.CLASS_NAME, 'p-saunaItemName h3')
    title = elem_title.text
    titles.append(title)


# In[15]:


titles


# In[16]:


#サウナ所在地を取得する
elem_area = browser.find_element(By.CLASS_NAME, 'p-saunaItem')
elem_address = elem_area.find_element(By.CLASS_NAME, 'p-saunaItem_address')
address = elem_address.text
address


# In[17]:


#elements にする
elems_area = browser.find_elements(By.CLASS_NAME, 'p-saunaItem')


# In[18]:


# データ数を確認する
len(elems_area)


# In[19]:


addresses = []
for elem_area in elems_area:
    elem_address = elem_area.find_element(By.CLASS_NAME, 'p-saunaItem_address')
    address = elem_address.text
    addresses.append(address)


# In[20]:


addresses


# In[21]:


#サウナスコアを取得
elem_number = browser.find_element(By.CLASS_NAME, 'p-saunaItem')


# In[22]:


elem_numbers = browser.find_elements(By.CLASS_NAME, 'p-saunaItem')
scores = []


# In[23]:


#elements にする
elems_number = browser.find_elements(By.CLASS_NAME, 'p-saunaItem')


# In[24]:


#サウナスコアを取得
elem_number = browser.find_element(By.CLASS_NAME, 'p-saunaItem')
elem_score = elem_number.find_element(By.XPATH, '/html/body/div/div[3]/div[2]/section/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/ul[2]/li[1]/span')
score = elem_score.text
score


# In[25]:


len(elems_number)


# In[26]:


scores = []
for elem_number in elem_numbers:
    elem_score = elem_number.find_element(By.CLASS_NAME, 'p-saunaItem_number')
    score = float(elem_score.text)  # 文字列を数値に変換
    score = elem_score.text
    scores.append(score)


# In[27]:


# scores リストには各要素のスコアが追加されているはず
for score in scores:
    print(score)


# In[28]:


import pandas as pd


# In[29]:


df = pd.DataFrame()


# In[30]:


df['施設名'] = titles
df['所在地'] = addresses
df['イキタイ'] = scores


# In[31]:


df.index = pd.RangeIndex(start=1, stop=len(df)+1)


# In[32]:


df.head(10)


# In[ ]:




