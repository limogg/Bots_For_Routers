from Router.router import Router
import Router.constants as const


default_ip = const.starting_site

#debug purpose only set to input when finished
PPpoE = 'user'
password = 'password1234'
vlan = '100'
client_id = '1234'
tv_vlan = '123'


#false to dont set 5ghz name
ghz2 = False
#true to set wifi 5ghz name
ghz5 = True

#Xpath to search for wifi
xpath24 = const.wifi_24_xpath
xpath5 = const.wifi_5_xpath


router = Router()

router.open_starting_site(default_ip)

# router.switch_to_navbar()
# router.set_port_binding()


#set internet
router.switch_to_navbar()
router.go_and_set_interface(PPpoE, password, vlan)

#pass all value than set wifi2.4
router.switch_to_navbar()
router.set_wifi(client_id, password, ghz2, xpath24)

#pass all value than set wifi5
router.switch_to_navbar()
router.set_wifi(client_id, password, ghz5, xpath5)

#set acl
router.switch_to_navbar()
router.set_ACL()

#set tv vlan
router.switch_to_navbar()
router.set_interface_for_tv(tv_vlan)

#set port binding



