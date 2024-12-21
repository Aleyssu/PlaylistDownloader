import sys
import os
from win32com.client import Dispatch

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortcut("Update Music.lnk")

shortcut.TargetPath = sys.executable
shortcut.Arguments = "UpdateSongs.py"
shortcut.WorkingDirectory = os.getcwd()
shortcut.IconLocation = os.path.abspath("icon.ico")

shortcut.save()