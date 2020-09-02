from lxml import html #
import requests #
import re #for filtering digits
import arabic_reshaper #pip install arabic_reshaper 
from bidi.algorithm import get_display  #pip install python-bidi
import csv


#page id
sample_id='omidtvclub'

#scrape page
page = requests.get('http://sapp.ir/'+sample_id)
tree = html.fromstring(page.text)
name = tree.xpath('/html/body/div/div/div[1]/h1')
follower = tree.xpath('//html/body/div/div/div[1]/h4')

#encode and decode to utf-8
name_ascii = name[0].text
name_encode = name_ascii.encode('utf-8')
name_decode = name_encode.decode("utf-8")

#reshape persian text for viewing in editor
reshaped_text = arabic_reshaper.reshape(name_decode)
persian_name = get_display(reshaped_text)
print(persian_name)

#encode and decode to utf-8
follower_ascii = follower[0].text
follwer_encode = follower_ascii.encode('utf-8')
follwer_decode = follwer_encode.decode("utf-8")

#filter digits
followers=int(re.sub('\D', '', follwer_decode))
print(followers)


scraped_data = [name_decode,followers]
print(scraped_data)
with open('%s-channel.csv'%(sample_id), 'w',encoding='utf-8-sig', errors='replace') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(scraped_data)
