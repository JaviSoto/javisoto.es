from django.http import HttpResponseRedirect

from syte.syte_settings import *


class ValidateHostMiddleware(object):
	def process_request(self, request):
		if DEPLOYMENT_MODE == 'prod' and not request.META['HTTP_HOST'].endswith(SITE_ROOT_URI):
			return HttpResponseRedirect(SITE_ROOT_URI)