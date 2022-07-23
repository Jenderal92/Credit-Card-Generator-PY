import requests ,re ,time ,os,sys
from colorama import Fore

print '{}CC GENERATOR | Python Code'.format(Fore.BLUE)

try:
	CC = requests.get('https://creditcardgenerator.money/', timeout=7).content
	REG = re.findall('</label> </td><td><input type="text" value=(.*?) name=',CC)
	print (Fore.YELLOW + '>Type:' + Fore.GREEN + REG[0]).replace('"','')
	print (Fore.YELLOW + '>CC Number:' + Fore.GREEN + REG[1]).replace('"','')
	print (Fore.YELLOW + '>Validate:' + Fore.GREEN + REG[2]).replace('"','')
	print (Fore.YELLOW + '>Name On:' + Fore.GREEN + REG[3]).replace('"','')
	print (Fore.YELLOW + '>CCV Code:' + Fore.GREEN + REG[4]).replace('"','')
	print (Fore.YELLOW + '>Balance ($):' + Fore.GREEN + REG[5]).replace('"','')
	
except: pass

print('////////////////////////////////////////////')

ulangin = raw_input("Apakah anda Ingin mengulangi program? Y/N : ")
if ulangin=="y":
	os.system("python2 l.py")
elif ulangin =="n":
	print(Fore.RED + "CODED BY SHIN_CODE" + Fore.WHITE)
	sys.exit()