# -*- mode: python -*-
a = Analysis(['Rename Files.py'],
             pathex=['c:\\Users\\Joshua\\PycharmProjects\\Quick Scripts\\Rename Files'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Rename Files.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
