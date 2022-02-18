# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 15:31:46 2022

@author: Felix
"""

import os

from ctypes import (
    Structure,
    cdll,
    c_bool,
    c_short,
    c_int,
    c_uint,
    c_int16,
    c_int32,
    c_char,
    c_byte,
    c_long,
    c_float,
    c_double,
    POINTER,
    CFUNCTYPE,
    c_ubyte
)

from thorlabs_kinesis._utils import (
    c_word,
    c_dword,
    bind
)

from ctypes.wintypes import (
    DWORD,
    WORD
    )

# add Kinesis C dlls to the search path
dllpath = 'C:\\Program Files\\Thorlabs\\Kinesis'
os.add_dll_directory(dllpath)

lib = cdll.LoadLibrary("Thorlabs.MotionControl.KCube.LaserDiode.dll")

TLI_InitializeSimulations = bind(lib, "TLI_InitializeSimulations", None, None)
TLI_UninitializeSimulations = bind(lib, "TLI_UninitializeSimulations", None, None)

TLI_BuildDeviceList = bind(lib, "TLI_BuildDeviceList", None, c_short)

LD_Open = bind(lib, "LD_Open", [POINTER(c_char)], c_short)
LD_Close = bind(lib, "LD_Close", [POINTER(c_char)], None)
LD_Disable = bind(lib, "LD_Disable", [POINTER(c_char)], c_short)
LD_DisableOutput = bind(lib, "LD_DisableOutput", [POINTER(c_char)], c_short)
LD_Enable = bind(lib, "LD_Enable", [POINTER(c_char)], c_short)
LD_EnableOutput = bind(lib, "LD_EnableOutput", [POINTER(c_char)], c_short)

LD_SetLaserSetPoint = bind(lib, "LD_SetLaserSetPoint", [POINTER(c_char), c_word], c_short)

LD_StartPolling = bind(lib, "LD_StartPolling", [POINTER(c_char), c_int], c_bool)
LD_StopPolling = bind(lib, "LD_StopPolling", [POINTER(c_char)], None)

