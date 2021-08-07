# free mailing service url: app.sendgrid.com

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # console.debug case

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'email@mail.com'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'key'
