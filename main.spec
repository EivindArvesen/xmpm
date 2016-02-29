#-*- mode: python -*-
import os, sys, shutil

root = os.path.dirname(os.path.realpath('__file__'))
version = "0.2.0"
appname = "Raskolnikov"

#options = [ ('v', None, 'OPTION'), ('W ignore', None, 'OPTION') ]

a = Analysis(
    [
        #os.path.join(HOMEPATH,'support/_mountzlib.py'),
        #os.path.join(CONFIGDIR,'support/useUnicode.py'),
        'raskolnikov/main.py'
    ],
    datas=[],
    binaries=[],
    pathex=[],
    hiddenimports=['PyQt4.QtCore', 'PyQt4.QtGui', 'PyQt4.QtGui.QApplication', 'PyQt4.QtGui.QKeySequence'],
    hookspath=None,
    runtime_hooks=None,
    excludes=None # ['PySide']
)

# extrafiles = [(os.path.join("assets", 'style.qss'), os.path.join("raskolnikov", "assets", 'style.qss'), 'DATA')]

more_binaries = [] # Added
qtLib_dir = '/Users/Eivind/anaconda/pkgs/qt-4.8.7-1/lib' # Added
for qtLib_type in os.listdir(qtLib_dir): # Added
    if qtLib_type.endswith('.dylib'): # Added
        more_binaries.append((qtLib_type, os.path.join(qtLib_dir, qtLib_type), 'BINARY')) # Added


pyz = PYZ (a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries + more_binaries,
          a.zipfiles,
          a.datas,
          #options,
          name=os.path.join(root, 'dist', appname),
          #background=True, # This is currently assigned to PyInstaller's 3.1 milestone
          debug=False,  # True # False
          strip=True, # None # True
          upx=True,
          console=False # True # False
          )

if sys.platform.startswith("darwin"):
    app = BUNDLE (exe,
                  name=os.path.join(root, 'dist', appname+'.app'),
                  icon=os.path.join(root, 'res', 'icon.icns'),
                  bundle_identifier=None,
                  info_plist={
                  'LSUIElement': '1' # True
                  },
                  version=version)

    images = ['axe_dark.png', 'axe_light.png', 'small_icon.png']
    for image in images:
        shutil.copy(
            os.path.join("res", image),
            os.path.join(root, 'dist', appname+'.app', 'Contents/Resources/', image))

    # shutil.copy(
    #     os.path.join(os.path.expanduser('~'), 'anaconda', 'pkgs', 'qt-4.8.7-1', 'lib', 'libQtGui.4.8.7.dylib'),
    #     os.path.join(root, 'dist', appname+'.app', "Contents", "Frameworks", "libQtGui.4.dylib"))

    shutil.copytree(
        '/usr/local/Cellar/qt/4.8.7_1/lib/QtGui.framework/Versions/4/Resources/qt_menu.nib',
        os.path.join(root, 'dist', appname+'.app', 'Contents/Resources/qt_menu.nib'))

    shutil.copy(
        "/Users/Eivind/anaconda/envs/raskolnikov/lib/python2.7/site-packages/PyQt4/QtGui.so",
        os.path.join(root, 'dist', appname+'.app', os.path.join("Contents", "Frameworks", "PyQt4.QtGui.so")))

    shutil.copytree(
        "/usr/local/Cellar/qt/4.8.7_1/lib/QtCore.framework",
        os.path.join(root, 'dist', appname+'.app', "Contents", "Frameworks", "QtCore.framework"))

    # shutil.copytree(
    #  '/Library/Frameworks/QtGui.framework/Versions/Current/Resources/qt_menu.nib',
    #  os.path.join(root, 'dist', appname+'.app', 'Contents/Resources/qt_menu.nib'))

    shutil.copy(
     os.path.join("res", "icon.icns"),
     os.path.join('dist', appname+'.app', 'Contents/Resources/icon-windowed.icns'))
