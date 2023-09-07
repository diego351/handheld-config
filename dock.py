import subprocess

import config

FORCE_ADMIN_COMMAND = 'if not "%1"=="am_admin" (powershell start -verb runas "%0" am_admin & exit /b)'

enable_gpu_command = f'pnputil /enable-device {config.DGPU_ID}'
command = f'{FORCE_ADMIN_COMMAND} & {enable_gpu_command}'

subprocess.Popen([command], shell=True)
