import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["ConfigParser"], "excludes": [""]}

base = None
#if sys.platform == "win32":
#    base = "Win32GUI"

setup(name="ciremai HOST",
      version="0.1",
      description="ciremai HOST interface HL7 -> DB",
      options = {"build_exe":build_exe_options },
      executables= [Executable("host_hl7.py", base=base)]
      )
