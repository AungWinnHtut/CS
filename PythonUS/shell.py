import os
import platform

if platform.system() == 'Windows':
    os.system('dir')
elif platform.system() == 'Linux':
    os.system('ls')