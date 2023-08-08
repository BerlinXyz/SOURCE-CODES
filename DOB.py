#CODED BY SIAM AHMED
import requests,re 
def getDOB(cookie):
  try:
    url="https://mbasic.facebook.com/profile.php"
    userAgent="Mozilla/5.0 (Linux; Android 11; SM-M126F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.2764.410 Mobile Safari/537.36"
    header={
      'Host': 'mbasic.facebook.com',
      'viewport-width': '980',
      'sec-ch-prefers-color-scheme': 'light',
      'upgrade-insecure-requests': '1',
      'user-agent': userAgent,
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'dnt': '1',
      'x-requested-with': 'mark.via.gr',
      'sec-fetch-site': 'none',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-user': '?1',
      'sec-fetch-dest': 'document',
      'referer': 'https://mbasic.facebook.com/',
      'accept-encoding': 'gzip, deflate',
      'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
      'cookie':cookie
    }
    response=requests.get(url, headers=header).text
    dateOfbirth=re.search("\d{1,2} \w* \d{4}",response).group()
    print("Date of Birth = ",dateOfbirth)
  except:pass