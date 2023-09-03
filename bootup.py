import GPUtil
import json
import shutil

gpu_names = [gpu.name for gpu in GPUtil.getGPUs()]

with open('config.json') as config_file:
    config = json.load(config_file)
    

def replace_files(config, key):
    for config_entry in config:
        to_copy_path = config_entry[key]
        dest_path = config_entry['destination']
        
        shutil.copytree(to_copy_path, dest_path, dirs_exist_ok=True)
        



dgpu_found = False
for gpu_name in gpu_names:
    if 'NVIDIA' in gpu_name:
        dgpu_found = True
        break

if dgpu_found:
    print("Discrete gpu found, replacing configs...")
    replace_files(config, 'd_config_path')

else:
    print('Discrete gpu NOT found, replacing configs...')
    replace_files(config, 'i_config_path')
