import subprocess

subprocess.run("virtualenv -p python3 env", shell=True, check=True)
subprocess.run("./env/bin/python setup.py install", shell=True, check=True)