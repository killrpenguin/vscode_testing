import subprocess


ls = subprocess.run(['ls', '-a'], stdout=subprocess.PIPE).stdout.decode("utf-8")

print(f"{ls}")