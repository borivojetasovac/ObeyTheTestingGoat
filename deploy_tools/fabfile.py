from fabric.contrib.files import append, exists, sed
from fabric.api import cd, env, local, run
import random

REPO_URL = 'https://github.com/borivojetasovac/ObeyTheTestingGoat'

def deploy():
    site_folder = f'/home/{env.user}/sites/{env.host}'      # env.user - the username you're using to log in to the server
    run(f'mkdir -p {site_folder}')                          # run - runs given shell command on the server
    with cd(site_folder):                                   # cd - runs all the following statements inside given working directory
        _get_latest_source()
        _update_settings(env.host)                          # env.host - the address of the server specified at the command line
        _update_virtualenv()
        _update_static_files()
        _update_database()

def _get_latest_source():
    if exists('.git'):
        run('git fetch')
    else:
        run(f'git clone {REPO_URL} .')
    current_commit = local("git log -n 1 --format=%H", capture=True)    # local - runs a command on your local machine: this gets the ID of the current commit on your local PC
    run(f'git reset --hard {current_commit}')                           # the server ends up with whatever code is currently checked out on your machine (as long as it's pushed)

def _update_settings(site_name):
    settings_path = 'superlists/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
            'ALLOWED_HOSTS =.+$',
            f'ALLOWED_HOSTS = ["{site_name}"]'
    )
    secret_key_file = 'superlists/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choices(chars, k=50))
        append(secret_key_file, f'SECRET_KEY = "{key}"')
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')       # append - adds a line to the end of a file (won't do that if the line is already there)

def _update_virtualenv():
    if not exists('virtualenv/bin/pip'):
        run(f'python3.6 -m venv virtualenv')
    run('./virtualenv/bin/pip install -r requirements.txt')

def _update_static_files():
    run('./virtualenv/bin/python manage.py collectstatic --noinput')    # use virtualenv version of Pyhton whenever you run a Django manage.py command !

def _update_database():
    run('./virtualenv/bin/python manage.py migrate --noinput')          # --noinput - removes any interactive yes/no confirmations
