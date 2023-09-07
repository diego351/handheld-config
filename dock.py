import subprocess

import config
from helpers import DGPU, is_admin, set_global_profile_files

if not is_admin():
    print('Needs Administrator privileges')
    exit(1)

command = f'pnputil /enable-device {config.DGPU_ID}'

subprocess.Popen([command], shell=True)
set_global_profile_files(DGPU)
