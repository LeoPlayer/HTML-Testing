# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/leo/Desktop/Software/Main/src/main/python/main.py'],
             pathex=['/Users/leo/Desktop/Software/Main/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/leo/Desktop/Software/Main/venv/lib/python3.6/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/var/folders/cl/k_g0f11s05ggxzwcdp2c_0rw0000gp/T/tmp9rj87egf/fbs_pyinstaller_hook.py'],
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
          name='run',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/leo/Desktop/Software/Main/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='run')
app = BUNDLE(coll,
             name='run.app',
             icon='/Users/leo/Desktop/Software/Main/target/Icon.icns',
             bundle_identifier='app')
