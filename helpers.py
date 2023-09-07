import ctypes
import os
import shutil

import GPUtil

import config

DGPU = 'dgpu'
IGPU = 'igpu'


def is_admin():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    return is_admin


def replace_files(config, key):
    for config_entry in config:
        to_copy_path = config_entry[key]
        to_copy_path = os.path.abspath(os.path.join(to_copy_path, os.pardir))
        dest_path = config_entry['destination']

        shutil.copytree(to_copy_path, dest_path, dirs_exist_ok=True)


def get_detected_gpu_to_use():
    gpu_names = [gpu.name for gpu in GPUtil.getGPUs()]
    for gpu_name in gpu_names:
        if config.D_GPU_NAME in gpu_name:
            return DGPU

    return IGPU


def set_global_profile_files(gpu):
    if gpu == DGPU:
        print("Setting discrete GPU profiles, replacing configs...")
        replace_files(config.GAME_PROFILES, 'd_config_path')
        print('Done')

    elif gpu == IGPU:
        print('Setting integrated GPU profiles, replacing configs...')
        replace_files(config.GAME_PROFILES, 'i_config_path')
        print('Done')

    else:
        raise NotImplementedError
