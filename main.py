import requests,os,pycountry
from datetime import datetime
from time import sleep
def get_info(username):
     patre={
    "Host": "www.tiktok.com",
    "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"99\", \"Google Chrome\";v\u003d\"99\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.0.0; Plume L2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
#    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q\u003d0.9,ar-DZ;q\u003d0.8,ar;q\u003d0.7,fr;q\u003d0.6,hu;q\u003d0.5,zh-CN;q\u003d0.4,zh;q\u003d0.3",}
     patrek=requests.get(f'https://www.tiktok.com/@{username}',headers=patre).text
#     with open ('wtxxxx.txt','a+') as w:
#         w.write(str(patrek))
     try:
        getting = str(patrek.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
        try:id = str(getting.split('id":"')[1]).split('",')[0]
        except:id=""
        try:name = str(getting.split('nickname":"')[1]).split('",')[0]
        except:name=""
        try:bio = str(getting.split('signature":"')[1]).split('",')[0]
        except:bio=""
        try:country = str(getting.split('region":"')[1]).split('",')[0]
        except:country="" 
        try:private = str(getting.split('privateAccount":')[1]).split(',"')[0]
        except:private=""
        try:followers = str(getting.split('followerCount":')[1]).split(',"')[0]
        except:followers=""
        try:following = str(getting.split('followingCount":')[1]).split(',"')[0]
        except:following=""
        try:like = str(getting.split('heart":')[1]).split(',"')[0]
        except:like=""
        try:video = str(getting.split('videoCount":')[1]).split(',"')[0]
        except:video=""
        try:secid = str(getting.split('secUid":"')[1]).split('"')[0]
        except:video=""
        countryn=str(pycountry.countries.get(alpha_2=country)).split("name='")[1].split("'")[0]
        countryf=str(pycountry.countries.get(alpha_2=country)).split("flag='")[1].split("'")[0]
        binary = "{0:b}".format(int(id))
        i = 0
        bits = ""
        while i < 31:
           bits += binary[i]
           i += 1
        timestamp = int(bits, 2)
        cdt = datetime.fromtimestamp(timestamp)
        kls=f"""───────────────\n⎌ ᴜѕᴇʀɴᴀᴍᴇ ➢ {username} \n⎌ ѕᴇᴄᴜɪᴅ ➢ {secid} \n⎌ ɴᴀᴍᴇ ➢ {name}\n⎌ ғᴏʟʟᴏᴡᴇʀѕ ➢ {followers} \n⎌ ғᴏʟʟᴏᴡɪɴɢ ➢ {following}\n⎌ ʟɪᴋᴇ ➢ {like}\n⎌ ᴠɪᴅᴇᴏ ➢ {video}\n⎌ ᴘʀɪᴠᴀᴛᴇ ➢ {private}\n⎌ ᴄᴏᴜɴᴛʀʏ ➢ {countryn} {countryf}\n⎌ ᴄʀᴇᴀᴛᴇᴅ ᴅᴀᴛᴇ ➢ {cdt}\n⎌ ɪᴅ ➢ {id}\n⎌ ʙɪᴏ ➢ {bio}\n───────────────""";print(kls)
     except:
      print(f'[×] Wrong UserName : {username}')
     sleep(600)
os.system('cls')
get_info(username=input('[+] TikTok UserName : '))
