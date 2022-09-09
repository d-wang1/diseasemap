import subprocess


def fetchIp():
    cmd = 'arp -a | findstr "80-8a-f7-04-46-4e" '
    returned_output = subprocess.check_output((cmd),shell=True,stderr=subprocess.STDOUT)
    parse=str(returned_output).split(' ',1)
    ip=parse[1].split(' ')
    return ip[1]