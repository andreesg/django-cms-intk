import os
gettext = lambda s: s
"""
Django settings for aldryn_cms project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sdlydipei-dmk1i%ctu)3z$=dhwbm)m%t#c4a*-dgl^-0%53=h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition





ROOT_URLCONF = 'aldryn_cms.urls'

WSGI_APPLICATION = 'aldryn_cms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'aldryn_cms', 'static'),
)
SITE_ID = 1

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	#other
	'compressor.finders.CompressorFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings'
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'aldryn_cms', 'templates'),
)

INSTALLED_APPS = (
	#'aldryn_blog',
	#'aldryn_common',
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    	'djangocms_text_ckeditor',
	#'polls',
	#'djangocms_polls',
	'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion',
    'aldryn_cms',
	#new apps
	'media_tree',
    'aldryn_blog',
	'aldryn_common',
	'standard_form',
	'spurl',
	'haystack',
	'aldryn_search',
	'compressor',
	'absolute',
	'aldryn_forms',
	'captcha',
	'emailit',
	'aldryn_gallery',
	'filer',
	'taggit',
	'easy_thumbnails',
	'polls',
	'djangocms_polls',
	'rich_collection',
    'rich_page',
	#'aldryn_rich_page'
)

HAYSTACK_ROUTERS = ["aldryn_search.router.LanguageRouter",]

ALDRYN_SEARCH_REGISTER_APPHOOK = True

HAYSTACK_CONNECTIONS = {
        'default': {
                'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
                'URL': 'http://127.0.0.1:9200/',
                'INDEX_NAME': 'haystack',
        },
        'en': {
                'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
                'URL': 'http://127.0.0.1:9200/',
                'INDEX_NAME': 'haystack',
        },
        'nl': {
                'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
                'URL': 'http://127.0.0.1:9200/',
                'INDEX_NAME': 'haystack',
        },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

MEDIA_TREE_MEDIA_BACKENDS = (
    'media_tree.contrib.media_backends.easy_thumbnails.EasyThumbnailsBackend',
)

#ALDRYN_BLOG_SEARCH = True

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
    ('nl', gettext('nl')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'nl',
            'hide_untranslated': False,
            'name': gettext('nl'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('base.html', 'Page'),
    ('fullwidth.html', 'Fullwidth'),
	('sidebar_left.html', 'Sidebar left'),
	('sidebar_right.html', 'Sidebar right'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

#
# PostgreSQL db
#

DATABASES = {
        'default': {
                'ENGINE' : 'django.db.backends.postgresql_psycopg2',
                'NAME': 'db_dev',
                'USER': 'ernesto',
                'PASSWORD':'ernesto',
                'HOST': 'localhost',
                'PORT': '',
        }
}

