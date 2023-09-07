import argparse
import shutil

import GPUtil

import config

DGPU = 'dgpu'
IGPU = 'igpu'


def replace_files(config, key):
    for config_entry in config:
        to_copy_path = config_entry[key]
        dest_path = config_entry['destination']

        shutil.copytree(to_copy_path, dest_path, dirs_exist_ok=True)


def get_detected_gpu_to_use(gpu_names):
    for gpu_name in gpu_names:
        if 'NVIDIA' in gpu_name:
            return DGPU

    return IGPU


def run():
    parser = argparse.ArgumentParser(prog='bootup')
    parser.add_argument('force-gpu', type=str, choices=[DGPU, IGPU])
    args = parser.parse_args()

    gpu_names = [gpu.name for gpu in GPUtil.getGPUs()]

    if args.force_gpu is not None:
        # force_gpu argument passed

        if args.force_gpu == DGPU:
            print("Discrete GPU forced, replacing configs...")
            replace_files(config.GAME_PROFILES, 'd_config_path')

        elif args.force_gpu == IGPU:
            print('Integrated GPU forced replacing configs...')
            replace_files(config.GAME_PROFILES, 'i_config_path')

        else:
            raise NotImplementedError

    else:
        dgpu = get_detected_gpu_to_use(gpu_names)

        if dgpu == DGPU:
            print("Discrete gpu found, replacing configs...")
            replace_files(config.GAME_PROFILES, 'd_config_path')

        elif dgpu == IGPU:
            print('Discrete gpu NOT found, replacing configs...')
            replace_files(config.GAME_PROFILES, 'i_config_path')

        else:
            raise NotImplementedError


if __name__ == "__main__":
    run()
