# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.utils import abort


env.ve_activate = "source /home/korifena.ru/env/bin/activate"
env.pid = "/home/korifena.ru/pids/django.pid"
env.project_dir = "/home/korifena.ru/www"


@hosts('korifena.ru@korifena.ru')
def pull():
    with cd(env.project_dir):
        run('git pull')


@hosts('korifena.ru@korifena.ru')
def manage(command):
    if not command:
        abort("Specify command!")
    with cd(env.project_dir):
        run(env.ve_activate + ' && python manage.py ' + command, pty=True)


@hosts('korifena.ru@korifena.ru')
def test_hup():
    run('kill -s HUP `cat ' + env.pid + '`', pty=True)


@hosts('korifena.ru@korifena.ru')
def update():
    pull()
    hup()

