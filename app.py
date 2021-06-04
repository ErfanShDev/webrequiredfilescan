import os
import platform
import time
import requests
from colorama import Fore, init
import sys
import datetime
init()


print(Fore.RED +" [*] Id Telgram Me :" + Fore.WHITE + "  @ERFAN_0909")
slppr = time.sleep(1)
print(Fore.RED +" [*] Id GitHub Me :" + Fore.WHITE + "   ErfanShDev")
slppr = time.sleep(1)
print(Fore.RED +" [*] Language Programer :" + Fore.WHITE + " Python")



slp6 = time.sleep(5)





print(Fore.GREEN +"""

               _                          _              _  __ _ _                                 
              | |                        (_)            | |/ _(_) |                                
 __      _____| |__  _ __ ___  __ _ _   _ _ _ __ ___  __| | |_ _| | ___  ___  ___ __ _ _ __  _ __  
 \ \ /\ / / _ \ '_ \| '__/ _ \/ _` | | | | | '__/ _ \/ _` |  _| | |/ _ \/ __|/ __/ _` | '_ \| '_ \ 
  \ V  V /  __/ |_) | | |  __/ (_| | |_| | | | |  __/ (_| | | | | |  __/\__ \ (_| (_| | | | | | | |
   \_/\_/ \___|_.__/|_|  \___|\__, |\__,_|_|_|  \___|\__,_|_| |_|_|\___||___/\___\__,_|_| |_|_| |_|
                                 | |                                                               
                                 |_|                                                               
   
                                                                                    
                                                                            """)
slpp0 = time.sleep(5)
# print(Fore.LIGHTRED_EX + "System Your: \n")
print(Fore.RED + """
███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗   
██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╗
███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║╚═╝
╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╗
███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║╚═╝
╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝   
                                                        
                                                             									   
""")
slp21 = time.sleep(2)
os = print(Fore.RED + "OS" + Fore.LIGHTCYAN_EX + ": " + platform.system() + "\n")
slp22 = time.sleep(2)
oswindows2 = print(Fore.RED + platform.uname()[0] + " Version And " + platform.uname()[0] + " Chand" + Fore.LIGHTCYAN_EX + ": " + platform.uname()[3] + " | " + platform.release() + "\n")
slp23 = time.sleep(2)
Cpu = print(Fore.RED + "Cpu" + Fore.LIGHTCYAN_EX + ": " + platform.uname()[5] + "\n")
slp24 = time.sleep(2)
iploc = print(Fore.RED + "Location" + Fore.LIGHTCYAN_EX + ": " + Fore.RED + "[*] " + Fore.LIGHTCYAN_EX + "Private " + Fore.RED + "[*] \n")
slp25 = time.sleep(2)




now = datetime.datetime.today()

mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)

print (Fore.RED +"Program runtime" + Fore.LIGHTCYAN_EX + ": " + mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss + "\n\n\n\n")
slp28 = time.sleep(5)





print(Fore.RED + "[*] Estefade Nadorost Be Ohdeye Khod User(Karbar) Mibashad va ma Hich Masoliyati Ra nmipazirim [*] \n")
slqp = time.sleep(5)
print("Please stand for a few seconds")
slop = time.sleep(2)

search = ['robots.txt',
'register/',
'wp-admin/',
'wp-content/wp-login.php',
'dashboard.php',
'dashbord.php',
'dashboard/',
'dashbord/',
'caphtcha/',
'caphtcha/v2/',
'admin/',
'caphtcha/v1/',
'caphtcha/v3/',
'recaphtcha/v2',
'recaphtcha/',
'login/',
'panel',
'logout',
'sitemap.xml',
'search/',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'users/',
'paneluser.php',
'Myaccount.php',
'Myaccount/',
'My-account.php',
'My-account/',
'profile.php',
'index.php',
'login.php',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'forgetpassword/',
'forget-password/',
'category/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']

print(Fore.WHITE)


urlgetuser = input("Plase Your Web Site Target + https:// Ya http://  : ")  



for cm in search:
    requestus = requests.get(urlgetuser+"/"+cm)
    if requestus.status_code == 200:
        print(Fore.GREEN+" [*]"+ Fore.WHITE+" Page Ok "+urlgetuser+"/"+cm + FORE.GREEN+ "[*]" )
    else:
        print(Fore.RED+" [*]"+Fore.WHITE+" Page Not Ok "+urlgetuser+"/"+cm + Fore.RED + "[*]")
