""" For using cx-freeze to turn python main.py into an executable """

from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(
    packages=["pygame", "win32api", "sys"],
    include_files=["controller", "model", "view", "global_variables.py", "Images"],
    excludes=[]
)

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('main.py', base=base, icon='red_car_horizontal.ico', targetName='Racing Game.exe')
]

setup(name='racing game',
      version='0.1',
      description='racing game',
      options=dict(build_exe=buildOptions),
      executables=executables)
