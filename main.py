import requests as req
from bs4 import BeautifulSoup as bs
head = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
url = "https://malangterkini.pikiran-rakyat.com/gaya-hidup/pr-1254435179/spoiler-kunci-jawaban-game-online-tebak-kata-shopee-level-70-1200?page=3"
ge = req.get(url,headers=head).text
sop = bs(ge,"lxml")
while True:
    anuan = int(input('Lvl 70 - 1221: '))
    if anuan < 70 or anuan > 1221:
        print('Hanya level 70 - 1221\n')
    else:
        s = sop.find('ol',{'start':'70'})
        al = [x.text.replace(' ','') for x in s.find_all('li')]
        an = anuan - 70
        try:
            for y in range(0,6):
                print(f"Level : {anuan+y}\nJawaban : {al[an+y]}\n")
        except:pass
        lan = input('Lanjut ?y/n : ')
        if lan =='y':
            continue
        elif lan =='n':
            break
