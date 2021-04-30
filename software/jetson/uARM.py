#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:        software/jetson/uARM.py
# By:          Samuel Duclos
# For:         Myself
# Description: uARM control in Python for TSO_team.
# For help:    cd software/jetson && python3 uARM.py --help # <-- Use --help for help using this file like this. <--

from utils.uarm_payload import add_payload_args

import argparse, subprocess, sys, time

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Template for uARM control.', 
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser = add_payload_args(parser)
    args = parser.parse_known_args()[0]
    print(vars(args))
    return args

def run(*popenargs, **kwargs):
    """Emulate Python 3 subprocess.run()."""
    input = kwargs.pop("input", None)
    check = kwargs.pop("handle", False)

    if input is not None:
        if 'stdin' in kwargs:
            raise ValueError('stdin and input arguments may not both be used.')

        kwargs['stdin'] = subprocess.PIPE

    process = subprocess.Popen(*popenargs, **kwargs)

    try:
        stdout, stderr = process.communicate(input)

    except:
        process.kill()
        process.wait()
        raise

    retcode = process.poll()

    if check and retcode:
        raise subprocess.CalledProcessError(retcode, 
                                            process.args, 
                                            output=stdout, 
                                            stderr=stderr)

    return retcode, stdout, stderr

def run_process(args):
    """Run process payload in the background."""
    python_payload = 'uarm_payload.py'
    result, stdout, stderr = run(['/opt/conda/envs/school/bin/python3', python_payload])
    time.sleep(3)
    return result, stdout, stderr

def main():
    """Main function."""
    args = parse_args()

    try:
        result = run_process(args)

        while True:
            time.sleep(5)

    except Exception as e:
        print(e)

    except KeyboardInterrupt:
        print('Program was interrupted by user: exiting.')

    finally:
        # Release resources.
        print('Done.')

if __name__ == '__main__':
    main()

