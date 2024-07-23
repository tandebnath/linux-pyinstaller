# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['app.py'],  # Main script
    pathex=['.'],  # Path to the script
    binaries=[],  # Additional binaries if any
    datas=[],  # Additional data files if any
    hiddenimports=[],  # List of hidden imports
    hookspath=[],  # Custom hooks
    runtime_hooks=[],  # Runtime hooks
    excludes=[],  # Excluded modules
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='directory_selector',  # Name of the output directory and executable
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True  # True for console application, False for GUI
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='directory_selector'
)
