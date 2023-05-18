from Router.router import Router
import Router.constants as const

PPpoE = 'user'
password = 'password1234'
vlan = '100'
client_id = '1234'
default_ip = const.starting_site
ghz2 = '_2,4GHz'
xpath24 = const.wifi_24_xpath
ghz5 = '_5GHZ'
xpath5 = const.wifi_5_xpath


router = Router()

router.open_starting_site(default_ip)
router.switch_to_navbar()
#pass everything to setup
router.go_and_set_interface(PPpoE, password, vlan)
router.switch_to_navbar()
router.set_wifi(client_id, password, ghz2, xpath24)
router.switch_to_navbar()
router.set_wifi(client_id, password, ghz5, xpath5)
router.switch_to_navbar()
router.set_ACL()




