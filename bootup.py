import argparse

from helpers import DGPU, IGPU, get_detected_gpu_to_use, set_global_profile_files

parser = argparse.ArgumentParser(prog='bootup')
parser.add_argument('--force-gpu', type=str, choices=[DGPU, IGPU])
args = parser.parse_args()

if args.force_gpu is not None:
    set_global_profile_files(args.force_gpu)

else:
    print('Detecting the GPU...')
    gpu = get_detected_gpu_to_use()

    if gpu == IGPU:
        print('Integrated GPU detected.')

    elif gpu == DGPU:
        print('Discrete GPU detected.')

    set_global_profile_files(gpu)
