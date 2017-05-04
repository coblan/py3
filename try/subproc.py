#!python3

import os
import subprocess

os.chdir(r'D:\coblan\webcode')

subprocess.Popen(r'start webpack --config field.conf.js',shell=True)
subprocess.Popen(r'start webpack --config field.mb.conf.js',shell=True)