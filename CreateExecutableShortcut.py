# Run with `python CreateExecutableShortcut.py <config_name> if you wish to use your own custom config`

import sys
import os
from win32com.client import Dispatch

if len(sys.argv) > 1:
    config_name = sys.argv[1]
else:
    config_name = 'config'

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortcut("Update Music.lnk")

shortcut.TargetPath = sys.executable
shortcut.Arguments = f"UpdateSongs.py --config-name {config_name}"
shortcut.WorkingDirectory = os.getcwd()
shortcut.IconLocation = os.path.abspath("icon.ico")

shortcut.save()
