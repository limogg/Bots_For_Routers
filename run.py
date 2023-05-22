import Router.constants as const


default_ip = const.starting_site

custom_ip = input('If you want too pass diferent ip adress you can pas it here else press enter and it will be default: ')

if custom_ip == "":
    custom_ip = default_ip
else:
    custom_ip = 'http://'+custom_ip+'/'

print(custom_ip)

PPpoE = input('Send PPoE name: ')
password = input('Send user password: ')
vlan = str(input('Send internet vlan: '))
client_id = str(input('Send client id: '))
number_of_tv = int(input('Send number of tv: '))
if number_of_tv > 0:
    tv_vlan =input('Send tv vlan: ')

else:
    tv_vlan = '0'

#false to dont set 5ghz name
ghz2 = False
#true to set wifi 5ghz name
ghz5 = True

#Xpath to search for wifi
xpath24 = const.wifi_24_xpath
xpath5 = const.wifi_5_xpath

#moved here because it open blank site before taking input
from Router.router import Router

router = Router()

#set internet
router.set_internet(custom_ip, PPpoE, password, vlan, client_id, ghz2, xpath24, ghz5, xpath5)

if number_of_tv != 0:
    router.add_tv(tv_vlan, number_of_tv)





