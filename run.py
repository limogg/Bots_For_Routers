from Router.router import Router
import Router.constants as const

PPpoE = 'user'
password = 'password1234'
vlan = '100'
client_id = '1234'
default_ip = const.starting_site

router = Router()

router.open_starting_site(default_ip)
router.switch_to_navbar()
#pass everything to setup
router.go_and_set_interface(PPpoE, password, vlan)
router.switch_to_navbar()
router.set_wifi(client_id, password)




