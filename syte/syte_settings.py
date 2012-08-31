# -*- coding: utf-8 -*-

DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.1'

if DEPLOYMENT_MODE == 'dev':
	SITE_ROOT_URI = '127.0.0.1:8000'
	PREPEND_WWW = False
	DEBUG = True
else:
	SITE_ROOT_URI = 'www.javiersoto.me'
	PREPEND_WWW = True
	DEBUG = False

MEDIA_URL = "http://" + SITE_ROOT_URI + '/static/'