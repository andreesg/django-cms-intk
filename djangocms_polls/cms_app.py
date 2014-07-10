from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from .menu import PollsMenu

class PollsApp(CMSApp):
	name = _("Poll App")
	urls = ['polls.urls']
	app_name = "polls"
	menus = [PollsMenu]

apphook_pool.register(PollsApp)


