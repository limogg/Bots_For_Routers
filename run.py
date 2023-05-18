from Router.router import Router
import Router.constants as const

PPoE = 'user'
password = 'password'
vlan = '100'
default_ip = const.starting_site

router = Router()

router.open_starting_site(default_ip)
router.switch_to_navbar()
#pass everything to setup
router.go_and_set_interface(PPoE, password, vlan)




