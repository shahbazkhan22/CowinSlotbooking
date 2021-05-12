import requests
import json
import time
from datetime import datetime
from playsound import playsound
date = '14-05-2021'

def check(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(url,headers=headers)
    #print(r.status_code)
    data = r.json()
    for c in data['centers']:
        for s in c['sessions']:
            if(s['min_age_limit']==18 and s['available_capacity']>0):
                print(c['address'],c['district_name'],c['pincode'],s['vaccine'],s['available_capacity'],s['min_age_limit'])
                playsound('beep.mp3')

if __name__=="__main__":
    while(True):
        for i in range(140,151):
            url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id='+str(i)+'&date='+date
            check(url)
        print('Sleeping for 30 secs',str(datetime.now().time()))
        time.sleep(30)
