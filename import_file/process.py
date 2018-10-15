from subprocess import check_output
import subprocess
import sys


# Simple command to list the directories and files in a folder
subprocess.call(['dir'], shell=False)

subprocess.Popen(['dir'], shell=False)