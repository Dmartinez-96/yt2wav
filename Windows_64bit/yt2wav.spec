# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\\\Users\\\\dakot\\\\Documents\\\\Programming_projects\\\\Python\\\\yt2wav.py'],
    pathex=[],
    binaries=[('C:\\\\Users\\\\dakot\\\\AppData\\\\Local\\\\Microsoft\\\\WinGet\\\\Links\\\\ffmpeg.exe', '.')],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='yt2wav',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
