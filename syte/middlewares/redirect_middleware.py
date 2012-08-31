from django.http import HttpResponseRedirect

from syte.syte_settings import *


class ValidateHostMiddleware(object):
	def process_request(self, request):
		if DEPLOYMENT_MODE == 'prod' and not request.META['HTTP_HOST'].startswith(SITE_ROOT_URI):
			return HttpResponseRedirect("http://" + SITE_ROOT_URI + request.META['PATH_INFO'])