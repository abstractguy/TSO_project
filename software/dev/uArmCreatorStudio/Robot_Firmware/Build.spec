# -*- mode: python -*-
import os
import platform

block_cipher = None

OS_TYPE = None

if platform.system() == 'Darwin':
    OS_TYPE = 'macosx'
elif platform.system() == 'Linux':
    OS_TYPE = 'linux'
elif platform.system() == 'Windows':
    OS_TYPE = 'windows'

if OS_TYPE is None:
    print ("System not supported {}".format(platform.system()))
    sys.exit(1)

avrdude_list = []
avrdude_path = 'avrdude'
if OS_TYPE.lower() == 'macosx':
    avrdude_list = [(os.path.join(avrdude_path, 'mac', 'avrdude')           ,       os.path.join('avrdude')),
                    (os.path.join(avrdude_path, 'mac', 'avrdude.conf')       ,      os.path.join('avrdude')),
                    (os.path.join(avrdude_path, 'mac', 'avrdude_bin')        ,      os.path.join('avrdude')),
                    (os.path.join(avrdude_path, 'mac', 'libusb.dylib')        ,     os.path.join('avrdude')),
                    (os.path.join(avrdude_path, 'mac', 'libusb-0.1.4.dylib')  ,     os.path.join('avrdude')),
                    (os.path.join(avrdude_path, 'mac', 'libusb-1.0.0.dylib')  ,     os.path.join('avrdude')),
                    (os.path.join(avrdude_path, 'mac', 'libusb-1.0.dylib')     ,    os.path.join('avrdude')),
                    ]
elif OS_TYPE.lower()  == 'windows':
    avrdude_list = [(os.path.join(avrdude_path, 'windows', 'avrdude.exe'),  os.path.join('avrdude')),
                    (os.path.join(avrdude_path, 'windows', 'libusb0.dll'),  os.path.join('avrdude')),
                    (os.path.join(avrdude_path, 'windows', 'avrdude.conf'), os.path.join('avrdude')),
    ]

data_files =  avrdude_list
print (data_files)

#if platform.system() == 'Windows':
#    data_files = [
#             ( 'avrdude/windows/*', 'avrdude' )
#             ]
#
#elif platform.system() == 'Darwin':
#    data_files = [
#             ( 'avrdude/mac/*.conf', 'avrdude' ),
#             ( 'avrdude/mac/bin/avrdude', 'avrdude/bin' ),
#             ( 'avrdude/mac/bin/avrdude_bin', 'avrdude/bin' ),
#             ( 'avrdude/mac/lib/*.dylib', 'avrdude/lib' )
#             ]
#elif platform.system() == 'Linux':
#    data_files = [
#             ( 'avrdude/linux/*', 'avrdude' ),
#             ]


a = Analysis(['flash_firmware.py'],
             pathex=['dist'],
             binaries=None,
             datas=data_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='flash_firmware',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='flash.ico')
