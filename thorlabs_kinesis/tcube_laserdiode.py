# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 15:47:02 2021

@author: Felix
"""
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

lib = cdll.LoadLibrary("Thorlabs.MotionControl.TCube.LaserDiode.dll")

# enum FT_Status
FT_OK = c_short(0x00)
FT_InvalidHandle = c_short(0x01)
FT_DeviceNotFound = c_short(0x02)
FT_DeviceNotOpened = c_short(0x03)
FT_IOError = c_short(0x04)
FT_InsufficientResources = c_short(0x05)
FT_InvalidParameter = c_short(0x06)
FT_DeviceNotPresent = c_short(0x07)
FT_IncorrectDevice = c_short(0x08)
FT_Status = c_short

# enum MOT_MotorTypes
MOT_NotMotor = c_int(0)
MOT_DCMotor = c_int(1)
MOT_StepperMotor = c_int(2)
MOT_BrushlessMotor = c_int(3)
MOT_CustomMotor = c_int(100)
MOT_MotorTypes = c_int

# enum LD_DisplayUnits
LD_ILim = c_short(0x01)
LD_ILD = c_short(0x02)
LD_IPD = c_short(0x03)
LD_PLD = c_short(0x04)
LD_ILim = c_short(0x01)
LD_ILD = c_short(0x02)
LD_IPD = c_short(0x03)
LD_PLD = c_short(0x04)

# enum LD_InputSourceFlags
LD_SoftwareOnly = c_short(0x01)
LD_ExternalSignal = c_short(0x02)
LD_Potentiometer = c_short(0x04)
LD_SoftwareOnly = c_short(0)
LD_Potentiometer = c_short(0x01)
LD_WheelAndSoftware = c_short(0x04)

# enum LD_Polarity
# TODO: Needs test. Documentation is unclear on datatype
LD_CathodeGrounded = c_short(1)
LD_AnodeGrounded = c_short(2)
LD_CathodeGrounded = c_short(1)
LD_AnodeGrounded = c_short(2)



class TLI_DeviceInfo(Structure):
    _fields_ = [("typeID", c_dword),
                ("description", (65 * c_char)),
                ("serialNo", (9 * c_char)),
                ("PID", c_dword),
                ("isKnownType", c_bool),
                ("motorType", MOT_MotorTypes),
                ("isPiezoDevice", c_bool),
                ("isLaser", c_bool),
                ("isCustomType", c_bool),
                ("isRack", c_bool),
                ("maxChannels", c_short)]


class TLI_HardwareInformation(Structure):
    _fields_ = [("serialNumber", c_dword),
                ("modelNumber", (8 * c_char)),
                ("type", c_word),
                ("firmwareVersion", c_dword),
                ("notes", (48 * c_char)),
                ("deviceDependantData", (12 * c_byte)),
                ("hardwareVersion", c_word),
                ("modificationState", c_word),
                ("numChannels", c_short)]
    
    
class LD_InputSourceFlags(Structure):
    _fields_ = [("LD_SoftwareOnly", c_short),
                ("LD_ExternalSignal", c_short),
                ("LD_Potentiometer", c_short),
                ("LD_SoftwareOnly", c_short),
                ("LD_Potentiometer", c_short),
                ("LD_WheelAndSoftware", c_short)]
    
    
class LD_DisplayUnits(Structure):
    _fields_  = [("LD_ILim", c_short),
                 ("LD_ILD", c_short),
                 ("LD_IPD", c_short),
                 ("LD_PLD", c_short),
                 ("LD_ILim", c_short),
                 ("LD_ILD", c_short),
                 ("LD_IPD", c_short),
                 ("LD_PLD", c_short)]
    
    
class LD_Polarity(Structure):
    _fields_ = [("LD_CathodeGrounded", c_short),
                ("LD_AnodeGrounded", c_short),
                ("LD_CathodeGrounded", c_short),
                ("LD_AnodeGrounded", c_short)]
    


TLI_BuildDeviceList = bind(lib, "TLI_BuildDeviceList", None, c_short)
TLI_GetDeviceListSize = bind(lib, "TLI_GetDeviceListSize", None, c_short)
# TLI_GetDeviceList  <- TODO: Implement SAFEARRAY first. ISC_API short __cdecl TLI_GetDeviceList(SAFEARRAY** stringsReceiver);
# TLI_GetDeviceListByType  <- TODO: Implement SAFEARRAY first. ISC_API short __cdecl TLI_GetDeviceListByType(SAFEARRAY** stringsReceiver, int typeID);
# TLI_GetDeviceListByTypes  <- TODO: Implement SAFEARRAY first. ISC_API short __cdecl TLI_GetDeviceListByTypes(SAFEARRAY** stringsReceiver, int * typeIDs, int length);
TLI_GetDeviceListExt = bind(lib, "TLI_GetDeviceListExt", [POINTER(c_char), c_dword], c_short)
TLI_GetDeviceListByTypeExt = bind(lib, "TLI_GetDeviceListByTypeExt", [POINTER(c_char), c_dword, c_int], c_short)
TLI_GetDeviceListByTypesExt = bind(lib, "TLI_GetDeviceListByTypesExt", [POINTER(c_char), c_dword, POINTER(c_int), c_int], c_short)
TLI_GetDeviceInfo = bind(lib, "TLI_GetDeviceInfo", [POINTER(c_char), POINTER(TLI_DeviceInfo)], c_short)
TLI_InitializeSimulations = bind(lib, "TLI_InitializeSimulations", None, None)
TLI_UninitializeSimulations = bind(lib, "TLI_UninitializeSimulations", None, None)

LD_CheckConnection = bind(lib, "LD_CheckConnection", [POINTER(c_char)], c_bool)
LD_ClearMessageQueue = bind(lib, "LD_ClearMessageQueue", [POINTER(c_char)], None)
LD_Close = bind(lib, "LD_Close", [POINTER(c_char)], None)
LD_Disable = bind(lib, "LD_Disable", [POINTER(c_char)], c_short)
LD_DisableOutput = bind(lib, "LD_DisableOutput", [POINTER(c_char)], c_short)
LD_Enable = bind(lib, "LD_Enable", [POINTER(c_char)], c_short)
LD_EnableLastMsgTimer = bind(lib, "LD_EnableLastMsgTimer", [POINTER(c_char), c_bool, c_int32], None)
LD_EnableMaxCurrentAdjust = bind(lib, "LD_EnableMaxCurrentAdjust", [POINTER(c_char), c_bool, c_bool], c_short)
LD_EnableOutput = bind(lib, "LD_EnableOutput", [POINTER(c_char)], c_short)
LD_EnableTIAGainAdjust = bind(lib, "LD_EnableTIAGainAdjust", [POINTER(c_char), c_bool], c_short)
LD_FindTIAGain = bind(lib, "LD_FindTIAGain", [POINTER(c_char)], c_short)

#LD_GetControlSource = bind(lib, "LD_GetControlSource", [POINTER(c_char), POINTER(LD_InputSourceFlags)], c_short) # TODO: Test. Documentation is kinda weird on the LD_InputSourceFlags
LD_GetControlSource = bind(lib, "LD_GetControlSource", [POINTER(c_char)], c_short) # Apperently, this returns the control source as a single short not a structure.

LD_GetDisplayUnits = bind(lib, "LD_GetDisplayUnits", [POINTER(c_char)], LD_DisplayUnits)
LD_GetFirmwareVersion = bind(lib, "LD_GetFirmwareVersion", [POINTER(c_char)], c_dword)
# TODO Test HardwareInfo
LD_GetHardwareInfo = bind(lib, "LD_GetHardwareInfo", [POINTER(c_char), POINTER(c_char), c_dword, POINTER(c_word), POINTER(c_word), POINTER(c_char), c_dword, POINTER(c_dword), POINTER(c_word), POINTER(c_word)], c_short)
LD_GetHardwareInfoBlock = bind(lib, "LD_GetHardwareInfoBlock", [POINTER(c_char), POINTER(TLI_HardwareInformation)], c_short)
LD_GetInterlockState = bind(lib, "LD_GetInterlockState", [POINTER(c_char)], c_ubyte)
LD_GetLaserDiodeCurrentReading = bind(lib, "LD_GetLaserDiodeCurrentReading", [POINTER(c_char)], c_word)
LD_GetLaserDiodeMaxCurrentLimit = bind(lib, "LD_GetLaserDiodeMaxCurrentLimit", [POINTER(c_char)], c_word)
LD_GetLaserPolarity = bind(lib, "LD_GetLaserPolarity", [POINTER(c_char)], LD_Polarity)
LD_GetLaserSetPoint = bind(lib, "LD_GetLaserSetPoint", [POINTER(c_char)], c_word)
LD_GetLEDBrightness = bind(lib, "LD_GetLEDBrightness", [POINTER(c_char)], c_word)
LD_GetMaxCurrentDigPot = bind(lib, "LD_GetMaxCurrentDigPot", [POINTER(c_char)], c_word)
LD_GetNextMessage = bind(lib, "LD_GetNextMessage", [POINTER(c_char), POINTER(c_word), POINTER(c_word), POINTER(c_dword)], c_bool)
LD_GetPhotoCurrentReading = bind(lib, "LD_GetPhotoCurrentReading", [POINTER(c_char)], c_word)
LD_GetSoftwareVersion = bind(lib, "LD_GetSoftwareVersion", [POINTER(c_char)], c_dword)
LD_GetStatusBits = bind(lib, "LD_GetStatusBits", [POINTER(c_char)], DWORD) # Need to interpret the returned int bit-wise (see API documentation for status bit positions)
# For instance ReturnedInt >> 0 & 1 for the first bit (Laser enabled?)
LD_GetVoltageReading = bind(lib, "LD_GetVoltageReading", [POINTER(c_char)], c_word)
LD_GetWACalibFactor = bind(lib, "LD_GetWACalibFactor", [POINTER(c_char)], c_float)

LD_HasLastMsgTimerOverrun = bind(lib, "LD_HasLastMsgTimerOverrun", [POINTER(c_char)], c_bool)
LD_Identify = bind(lib, "LD_Identify", [POINTER(c_char)], None)
LD_LoadNamedSettings = bind(lib, "LD_LoadNamedSettings", [POINTER(c_char), POINTER(c_char)], c_bool)
LD_LoadSettings = bind(lib, "LD_LoadSettings", [POINTER(c_char)], c_bool)
LD_MessageQueueSize = bind(lib, "LD_MessageQueueSize", [POINTER(c_char)], c_int)
LD_Open = bind(lib, "LD_Open", [POINTER(c_char)], c_bool)
LD_PersistSettings = bind(lib, "LD_PersistSettings", [POINTER(c_char)], c_bool)
LD_PollingDuration = bind(lib, "LD_PollingDuration", [POINTER(c_char)], c_long)
LD_RegisterMessageCallback = bind(lib, "LD_RegisterMessageCallback", [POINTER(c_char), CFUNCTYPE(None)], None)

LD_RequestControlSource = bind(lib, "LD_RequestControlSource", [POINTER(c_char)], c_short)
LD_RequestDisplay = bind(lib, "LD_RequestDisplay", [POINTER(c_char)], c_short)
LD_RequestLaserDiodeMaxCurrentLimit = bind(lib, "LD_RequestLaserDiodeMaxCurrentLimit", [POINTER(c_char)], c_short)
LD_RequestLaserPolarity = bind(lib, "LD_RequestLaserPolarity", [POINTER(c_char)], c_short)
LD_RequestLaserSetPoint = bind(lib, "LD_RequestLaserSetPoint", [POINTER(c_char)], c_short)
LD_RequestMaxCurrentDigPot = bind(lib, "LD_RequestMaxCurrentDigPot", [POINTER(c_char)], c_short)
LD_RequestReadings = bind(lib, "LD_RequestReadings", [POINTER(c_char)], c_short)
LD_RequestSettings = bind(lib, "LD_RequestSettings", [POINTER(c_char)], c_short)
LD_RequestStatus = bind(lib, "LD_RequestStatus", [POINTER(c_char)], c_short)
LD_RequestStatusBits = bind(lib, "LD_RequestStatusBits", [POINTER(c_char)], c_short)
LD_RequestWACalibFactor = bind(lib, "LD_RequestWACalibFactor", [POINTER(c_char)], c_short)

LD_SetClosedLoopMode = bind(lib, "LD_SetClosedLoopMode", [POINTER(c_char)], c_short)
# LD_SetControlSource = bind(lib, "LD_SetControlSource", [POINTER(c_char), LD_InputSourceFlags], c_short)
LD_SetControlSource = bind(lib, "LD_SetControlSource", [POINTER(c_char), c_short], c_short) # Apparently, this sets the control source as a single short.
LD_SetDisplayUnits = bind(lib, "LD_SetDisplayUnits", [POINTER(c_char), LD_DisplayUnits], c_short)
LD_SetLaserPolarity = bind(lib, "LD_SetLaserPolarity", [POINTER(c_char), LD_Polarity], c_short)
LD_SetLaserSetPoint = bind(lib, "LD_SetLaserSetPoint", [POINTER(c_char), c_word], c_short)
LD_SetLEDBrightness = bind(lib, "LD_SetLEDBrightness", [POINTER(c_char), c_short], c_short)
LD_SetMaxCurrentDigPot = bind(lib, "LD_SetMaxCurrentDigPot", [POINTER(c_char), c_word], c_short)
LD_SetOpenLoopMode = bind(lib, "LD_SetOpenLoopMode", [POINTER(c_char)], c_short)
LD_SetWACalibFactor = bind(lib, "LD_SetWACalibFactor", [POINTER(c_char), c_float], c_short)

LD_StartPolling = bind(lib, "LD_StartPolling", [POINTER(c_char), c_int], c_bool)
LD_StopPolling = bind(lib, "LD_StopPolling", [POINTER(c_char)], None)
# TODO LD_TimeSinceLastMsgReceived = bind(lib, "LD_TimeSinceLastMsgReceived", [POINTER(c_char), ])
LD_WaitForMessage = bind(lib, "LD_WaitForMessage", [POINTER(c_char), c_word, c_word, c_dword], c_bool)


