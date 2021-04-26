#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File:      software/jetson/utils/overclock_settings.py
# By:        Samuel Duclos
# For:       Myself
# Reference: https://github.com/NVIDIA-AI-IOT/jetson_benchmarks.git

import gc, os, subprocess, sys, time

FNULL = open(os.devnull, 'w')

# Class for Utilities (TRT check, Power mode switching)
# https://docs.nvidia.com/jetson/l4t/index.html#page/Tegra%2520Linux%2520Driver%2520Package%2520Development%2520Guide%2Fpower_management_jetson_xavier.html%23wwpID0E0KD0HA
class Overclock_utils:
    def __init__(self, jetson_devkit='xavier', gpu_freq=1377000000, dla_freq=1395200000, power_mode=0):
        self.jetson_devkit = jetson_devkit
        self.gpu_freq = gpu_freq
        self.dla_freq = dla_freq
        self.power_mode = power_mode

    def set_power_mode(self, power_mode, jetson_devkit):
        power_cmd = 'sudo nvpmodel -m' + str(power_mode)
        subprocess.call(power_cmd, shell=True, stdout=FNULL)
        print('Setting Jetson {} power mode'.format(jetson_devkit))

    def set_jetson_clocks(self):
        subprocess.call('jetson_clocks', shell=True, stdout=FNULL)
        print("Jetson clocks are Set")

    def set_jetson_fan(self, switch_opt):
        fan_cmd = 'sudo sh -c \'echo ' + str(switch_opt) + ' > /sys/devices/pwm-fan/target_pwm\''
        subprocess.call(fan_cmd, shell=True, stdout=FNULL)

    def run_set_clocks_withDVFS(self):
        if self.jetson_devkit == 'tx2':
            self.set_user_clock(device='gpu')
            self.set_clocks_withDVFS(frequency=self.gpu_freq, device='gpu')
        if self.jetson_devkit == 'nano':
            self.set_user_clock(device='gpu')
            self.set_clocks_withDVFS(frequency=self.gpu_freq, device='gpu')
        if self.jetson_devkit == 'xavier' or self.jetson_devkit == 'xavier-nx':
            self.set_user_clock(device='gpu')
            self.set_clocks_withDVFS(frequency=self.gpu_freq, device='gpu')
            self.set_user_clock(device='dla')
            self.set_clocks_withDVFS(frequency=self.dla_freq, device='dla')

    def set_user_clock(self, device):
        if self.jetson_devkit == 'tx2':
            self.enable_register = '/sys/devices/gpu.0/aelpg_enable'
            self.freq_register = '/sys/devices/gpu.0/devfreq/17000000.gp10b'
        if self.jetson_devkit == 'nano':
            self.enable_register = '/sys/devices/gpu.0/aelpg_enable'
            self.freq_register = '/sys/devices/gpu.0/devfreq/57000000.gpu'
        if self.jetson_devkit == 'xavier' or self.jetson_devkit == 'xavier-nx':
            if device == 'gpu':
                self.enable_register = '/sys/devices/gpu.0/aelpg_enable'
                self.freq_register = '/sys/devices/gpu.0/devfreq/17000000.gv11b'
            elif device == 'dla':
                base_register_dir = '/sys/kernel/debug/bpmp/debug/clk'
                self.enable_register = base_register_dir + '/nafll_dla/mrq_rate_locked'
                self.freq_register = base_register_dir + '/nafll_dla/rate'

    def set_clocks_withDVFS(self, frequency, device):
        from_freq = self.read_internal_register(register=self.freq_register, device=device)
        self.set_frequency(device=device, enable_register=self.enable_register, freq_register=self.freq_register, frequency=frequency, from_freq=from_freq)
        time.sleep(1)
        to_freq = self.read_internal_register(register=self.freq_register, device=device)
        print('{} frequency is set from {} Hz --> to {} Hz'.format(device, from_freq, to_freq))

    def set_frequency(self, device, enable_register, freq_register, frequency, from_freq):
        self.write_internal_register(enable_register, 1)
        if device == 'gpu':
            max_freq_reg = freq_register + '/max_freq'
            min_freq_reg = freq_register + '/min_freq'
            if int(frequency) > int(from_freq):
                self.write_internal_register(max_freq_reg, frequency)
                self.write_internal_register(min_freq_reg, frequency)
            else:
                self.write_internal_register(min_freq_reg, frequency)
                self.write_internal_register(max_freq_reg, frequency)
        elif device =='dla':
            self.write_internal_register(freq_register, frequency)

    def read_internal_register(self, register, device):
        if device == 'gpu':
            register += '/cur_freq'
        reg_read = open(register, 'r')
        reg_value = reg_read.read().rstrip("\n")
        reg_read.close()
        return reg_value

    def write_internal_register(self, register, value):
        reg_write = open(register, 'w')
        reg_write.write('%s' % value)
        reg_write.close()

    def clear_ram_space(self):
        cmd = 'sudo sh -c "echo 2 > /proc/sys/vm/drop_caches"'
        subprocess.call(cmd, shell=True)

    def close_all_apps(self):
        print('Please close all other applications...')
        time.sleep(5)

class Overclock:
    def __init__(self, jetson_devkit='xavier'):
        jetson_devkit = jetson_devkit.lower()
        if jetson_devkit == 'xavier':
            max_gpu_freq = 1377000000
            max_dla_freq = 1395200000
            precision = 'int8'
            self.max_power_mode = 0
        elif jetson_devkit == 'xavier-nx':
            max_gpu_freq = 1109250000
            max_dla_freq = 1100800000
            precision = 'int8'
            self.max_power_mode = 0
        elif jetson_devikit == 'tx2':
            max_gpu_freq = 1122000000
            max_dla_freq = None
            precision = 'fp16'
            self.max_power_mode = 3
        elif jetson_devkit == 'nano':
            max_gpu_freq = 921600000
            max_dla_freq = None
            precision = 'fp16'
            self.max_power_mode = 0

        self.overclocker = Overclock_utils(jetson_devkit=jetson_devkit,
                                           gpu_freq=max_gpu_freq,
                                           dla_freq=max_dla_freq,
                                           power_mode=self.max_power_mode)

    def overclock(self):
        self.overclocker.set_power_mode(self.max_power_mode, self.overclocker.jetson_devkit)
        self.overclocker.clear_ram_space()
        self.overclocker.set_jetson_clocks()
        self.overclocker.run_set_clocks_withDVFS()
        self.overclocker.set_jetson_fan(255)
        self.overclocker.close_all_apps()
        gc.collect()

    def underclock(self):
        self.overclocker.set_power_mode(2, self.overclocker.jetson_devkit)
        self.overclocker.clear_ram_space()
        self.overclocker.set_jetson_fan(0)
        del gc.garbage[:]

