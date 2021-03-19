# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['C:\\Users\\Engineering\\Desktop\\projects\\python\\desktopApp-Flir-env\\DesktopApp-FlirCamera\\src'],
             binaries=[],
             datas=[('icons\\cameraICO.ico', 'icons'),
                    ('icons\\camera.png', 'icons'),
                    ('icons\\cameraIcon.png', 'icons'),
                    ('icons\\capture.png', 'icons'),
                    ('icons\\logoflir.png', 'icons'),
                    ('icons\\logoIntecol.png', 'icons'),
                    ('icons\\play.png', 'icons'),
                    ('icons\\playCamera.png', 'icons'),
                    ('icons\\stop.png', 'icons'),
                    ('icons\\storage.png', 'icons')],
             hiddenimports=['PySide2.QtXml'],
             hookspath=[],  
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='DesktopAppFlir',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon='icons\\cameraICO.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='app')
