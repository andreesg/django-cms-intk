from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

# from .models import RichPage

# class IndexView(generic.ListView):
# 	template_name = 'rich_page/richpage_list.html'

# 	context_object_name = 'latest_richpage_list'

# 	def get_queryset(self):
# 		return RichPage.objects.all()

# class DetailView(generic.DetailView):
# 	model = RichPage
# 	template_name = 'rich_page/richpage_detail.html'
