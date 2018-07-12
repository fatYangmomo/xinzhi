from django import forms
from django.views import View
from ..utils import (
    correct_response, err_response_with_desc
)

class Test(View):
	
	def get(self,request):
		username = request.GET.get('username')

		return correct_response({'test':'成功','username':username})
		