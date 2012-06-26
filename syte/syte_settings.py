DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.1'

if DEPLOYMENT_MODE == 'dev':
	SITE_ROOT_URI = 'http://127.0.0.1:8000/'
	PREPEND_WWW = False
	DEBUG = True
else:
	SITE_ROOT_URI = 'http://www.javisoto.es/'
	PREPEND_WWW = True
	DEBUG = False

MEDIA_URL = SITE_ROOT_URI + 'static/'