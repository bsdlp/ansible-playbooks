MCSERVERS = [
        { 'name': 'vanilla',  'hostname': 'mc.voltaire.sh',     'port': '25565' },]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://user:pass@db_host/voltaire'
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT='465'
MAIL_USE_SSL=True
MAIL_USERNAME='no-reply@voltaire.sh'
MAIL_PASSWORD='passwordlol'

ADMINS=['bsd@voltaire.sh']

RECAPTCHA_USE_SSL=True
RECAPTCHA_PRIVATE_KEY='recap_privkey'
RECAPTCHA_PUBLIC_KEY='recap_pubkey'

CSRF_ENABLED = True
SECRET_KEY = 'keep_this_sekrit'

