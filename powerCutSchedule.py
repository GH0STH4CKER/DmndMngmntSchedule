# Author Gh0stH4cker
# Python version - 3.8.10
import requests,json,datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

n = 0
today = datetime.date.today().strftime("%Y-%m-%d")
tomrw = (datetime.date.today()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")

print(f'Power Cuts On {today} :\n')

Mygroup = input('Group Letter : ')
print('')

url = "https://cebcare.ceb.lk/Incognito/GetLoadSheddingEvents"

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "39",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": ".AspNetCore.Antiforgery.ThOcTlhnrMo=CfDJ8Ed8YgQVYi9HklDnDGoiq-8JnGUC-wgpbX5hiIHd3795VAFsj0TbvfINS5x_N5XKmCWJGrDAvu4m7T6aIPw2_AKCX4pB9H7PTW6NL87svvbt7mgR9iZyZa-_UcpOLJUPvt9Kp8laliE_MaKYJQkFEFk",
    "Host": "cebcare.ceb.lk",
    "Origin": "https://cebcare.ceb.lk",
    "Referer": "https://cebcare.ceb.lk/Incognito/DemandMgmtSchedule",
    "RequestVerificationToken": "CfDJ8Ed8YgQVYi9HklDnDGoiq--OZy2B-Vc8LUo91hBIR6O99hv9VX5Uh1XelRz00-Y4qCwczafD05X2lVTX44TiKbZwxtYPO9Wly2WA34ddx1N4V9Fnaz1asvAQ3vYefdzfYl4zn2n1IcSW3cbw_3ZY5OM",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.54",
    "X-Requested-With": "XMLHttpRequest"
}

data = {"StartTime": today,"EndTime": tomrw}

r = requests.post(url,headers=headers,data=data,verify=False)

if r.status_code == 200 and "loadShedGroupId" in r.text :

    detail = json.loads(r.text)
    for i in detail :
        if i['loadShedGroupId'] == Mygroup.upper() :
            n+=1
            print('Time :',str(i['startTime']).replace(today,'')[+1:],'-',str(i['endTime']).replace(today,'')[+1:])
    if n == 0 :
        print('No results !')    
else:
    print(404)
