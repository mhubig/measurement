# -*- coding: utf-8 -*-
import os.path
from invoke import run, task

base_dir = os.path.dirname(os.path.abspath(__file__))
env_file = os.path.join(base_dir, "env/bin/activate_this.py")

if os.path.isfile(env_file):
    execfile(env_file, dict(__file__=env_file))
else:
    print("WARNING: No virtualenv found!")

@task(default=True)
def start():
    pass
