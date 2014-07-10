from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import PollPluginModel

class PollPlugin(CMSPluginBase):
	model = PollPluginModel
	module = _("PollsPlugin")
	name = _("Poll Plugin")
	render_template = "djangocms_polls/poll_plugin.html"

	def render(self, context, instance, placeholder):
		context.update({'instance':instance})
		return context

plugin_pool.register_plugin(PollPlugin)

