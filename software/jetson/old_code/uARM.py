#!/usr/bin/env python3

# File:        python/uARM.py
# By:          Samuel Duclos
# For:         Myself
# Description: uARM control in Python for TSO_team.
# For help:    python3 python/uARM_payload.py --help # <-- Use --help for help using this file like this. <--

from utils.payload import add_payload_args

import argparse, subprocess, sys, time

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Template for uARM control.', 
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser = add_payload_args(parser)
    args = parser.parse_known_args()[0]
    print(vars(args))
    return args

def run_process(args):
    python_payload = b'uARM_payload.py'
    result = subprocess.run([sys.executable], capture_output=True, text=True, timeout=None, input=python_payload)
    time.sleep(3)
    return result

def main():
    """Main function."""
    args = parse_args()

    try:
        while True:
            result = run_process(args)
            print('stdout:', result.stdout)
            print('stderr:', result.stderr)

    except Exception as e:
        print(e)

    finally:
        # Release resources.
        print('Done.')

if __name__ == '__main__':
    main()

