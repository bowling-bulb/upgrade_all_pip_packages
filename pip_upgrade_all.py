import json
from subprocess import call, check_output

package_list = json.loads(check_output("pip3 list --format=json", shell=True))
packages = [i['name'] for i in package_list]

for p in packages:
    try:
        call("sudo -H pip3 install --upgrade " + p, shell=True)
    except:
        pass