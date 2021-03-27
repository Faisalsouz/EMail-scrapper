from bs4 import BeautifulSoup
import requests
#url='https://www.tripadvisor.com/Restaurants-g187382-oa30-Muenster_North_Rhine_Westphalia.html#EATERY_LIST_CONTENTS'
#url='https://www.tripadvisor.com/Restaurant_Review-g187382-d947380-Reviews-Altes_Gasthaus_Leve-Muenster_North_Rhine_Westphalia.html'
#soup=BeautifulSoup()
#selctor='#EATERY_LIST_CONTENTS > div.deckTools.btm > div > a'
# html_txt=requests.get(url).text
# bs_parser=BeautifulSoup(html_txt,'html.parser')
#print(bs_parser.find('wQjYiB7z'))
#email=bs_parser.find_all('div', class_='_36TL14Jn _3jdfbxG0')#ui_icon email _3ZW3afUk' class of websiteclass='_2wKz--mA _27M8V6YV'
#print(email)
# for i in email:
#     em=i.find_all('a',href=True)
#     em=[a['href'] for a in em]

#print([em.get('href') for em in email])
#print([l.get('href') for l in all_link])

# for l in all_link:
#     # print(l)
#     urls=l.find_all('a',href=True)
#     print(urls)
    # for u in urls:
        #
        # print(u.text)
        # print(u['href'])
st=['mailto:info@hof-zur-linde.de?subject=?'][0]
st2=st.replace('mailto:','').replace('?subject=?','')
st='https://www.tripadvisor.com/Restaurant_Review-g187368-d14002976-Reviews-Nohut-Bielefeld_North_Rhine_Westphalia.html'
st.strip('')