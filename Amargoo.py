import requests,datetime,time,os

os.environ['TZ'] = 'Asia/Tehran'
time.tzset()
while(1):
    now = datetime.datetime.now()
    cms = requests.get('http://amargoo.ir/trade.php')
    time.sleep(1);
    print(cms.content)
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
