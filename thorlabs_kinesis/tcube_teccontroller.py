# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 15:37:05 2021

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

lib = cdll.LoadLibrary("Thorlabs.MotionControl.TCube.TEC.dll")

# enum TC_DisplayModes
TC_ActualTemperature = 0x00
TC_TargetTemperature = 0x01
TC_TempDifference = 0x02
TC_Current = 0x03

# enum TC_SensorTypes
TC_Transducer = 0x00
TC_TH20kOhm = 0x01
TC_TH200kOhm = 0x02

# enum MOT_MotorTypes
MOT_NotMotor = c_int(0)
MOT_DCMotor = c_int(1)
MOT_StepperMotor = c_int(2)
MOT_BrushlessMotor = c_int(3)
MOT_CustomMotor = c_int(100)
MOT_MotorTypes = c_int


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


class TC_LoopParameters(Structure):
    _fields_ = [("differentialGain", c_short),
                ("integralGain", c_short),
                ("proportionalGain", c_short)]
    
    
    
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

TC_CheckConnection = bind(lib, "TC_CheckConnection", [POINTER(c_char)], c_bool)
TC_ClearMessageQueue = bind(lib, "TC_ClearMessageQueue", [POINTER(c_char)], None)
TC_Close = bind(lib, "TC_Close", [POINTER(c_char)], None)
TC_Disable = bind(lib, "TC_Disable", [POINTER(c_char)], c_short)
TC_Disconnect = bind(lib, "TC_Disconnect", [POINTER(c_char)], c_short)
TC_Enable = bind(lib, "TC_Enable", [POINTER(c_char)], c_short)
TC_EnableLastMsgTimer = bind(lib, "TC_EnableLastMsgTimer", [POINTER(c_char), c_bool, c_int32], None)

TC_GetCurrentLimit = bind(lib, "TC_GetCurrentLimit", [POINTER(c_char)], c_word)
TC_GetCurrentReadung = bind(lib, "TC_GetCurrentReadung", [POINTER(c_char)], c_word)
TC_GetFirmwareVersion = bind(lib, "TC_GetFirmwareVersion", [POINTER(c_char)], c_dword)
TC_GetHardwareInfo = bind(lib, "TC_GetHardwareInfo", [POINTER(c_char), POINTER(c_char), c_dword, POINTER(c_word), POINTER(c_word), POINTER(c_char), c_dword, POINTER(c_dword), POINTER(c_word), POINTER(c_word)], c_short)
TC_GetHardwareInfoBlock = bind(lib, "TC_GetHardwareInfoBlock", [POINTER(c_char)], TLI_HardwareInformation)
TC_GetHWDisplayMode = bind(lib, "TC_GetHWDisplayMode", [POINTER(c_char)], c_short) # Enumerated as TC_DisplayModes
TC_GetLEDBrightness = bind(lib, "TC_GetLEDBrightness", [POINTER(c_char)], c_short)
TC_GetNextMessage = bind(lib, "TC_GetNextMessage", [POINTER(c_char), POINTER(c_word), POINTER(c_word), POINTER(c_dword)], c_bool)
TC_GetSensorType = bind(lib, "TC_GetSensorType", [POINTER(c_char)], c_short) # Enumerated as TC_SensorTypes
TC_GetSoftwareVersion = bind(lib, "TC_GetSoftwareVersion", [POINTER(c_char)], c_dword)
TC_GetStatusBits = bind(lib, "TC_GetStatusBits", [POINTER(c_char)], c_dword)
TC_GetTemperatureReading = bind(lib, "TC_GetTemperatureReading", [POINTER(c_char)], c_short)
TC_GetTemperatureSet = bind(lib, "TC_GetTemperatureSet", [POINTER(c_char)], c_short)
TC_GetTempLoopParams = bind(lib, "TC_GetTempLoopParams", [POINTER(c_char), POINTER(TC_LoopParameters)], c_short)

TC_HasLastMsgTimerOverrun = bind(lib, "TC_HasLastMsgTimerOverrun", [POINTER(c_char)], c_bool)
TC_Identify = bind(lib, "TC_Identify",  [POINTER(c_char)], None)
TC_LoadNamedSettings = bind(lib, "TC_LoadNamedSettings", [POINTER(c_char), POINTER(c_char)], c_bool)
TC_LoadSettings = bind(lib, "TC_LoadSettings", [POINTER(c_char)], c_bool)
TC_MessageQueueSize = bind(lib, "TC_MessageQueueSize", [POINTER(c_char)], c_int)
TC_Open = bind(lib, "TC_Open", [POINTER(c_char)], c_short)
TC_PersistSettings = bind(lib, "TC_PersistSettings", [POINTER(c_char)], c_bool)
TC_PollingDuration = bind(lib, "TC_PollingDuration", [POINTER(c_char)], c_long)
TC_RegisterMessageCallback = bind(lib, "TC_RegisterMessageCallback", [POINTER(c_char), CFUNCTYPE(None)], None)

TC_RequestCurrentLimit = bind(lib, "TC_RequestCurrentLimit", [POINTER(c_char)], c_short)
TC_RequestHWDisplayMode = bind(lib, "TC_RequestHWDisplayMode", [POINTER(c_char)], c_short)
TC_RequestLEDBrightness = bind(lib, "TC_RequestLEDBrightness", [POINTER(c_char)], c_short)
TC_RequestReadings = bind(lib, "TC_RequestReadings", [POINTER(c_char)], c_short)
TC_RequestSensorType = bind(lib, "TC_RequestSensorType", [POINTER(c_char)], c_short)
TC_RequestSettings = bind(lib, "TC_RequestSettings", [POINTER(c_char)], c_short)
TC_RequestStatus = bind(lib, "TC_RequestStatus", [POINTER(c_char)], c_short)
TC_RequestStatusBits = bind(lib, "TC_RequestStatusBits", [POINTER(c_char)], c_short)
TC_RequestTemperatureSet = bind(lib, "TC_RequestTemperatureSet", [POINTER(c_char)], c_short)
TC_RequestTempLoopParams = bind(lib, "TC_RequestTempLoopParams", [POINTER(c_char)], c_short)

TC_Reset = bind(lib, "TC_Reset", [POINTER(c_char)], c_short)
TC_SetCurrentLimit = bind(lib, "TC_SetCurrentLimit", [POINTER(c_char), c_word])
TC_SetHWDisplayMode = bind(lib, "TC_SetHWDisplayMode", [POINTER(c_char), c_short], c_short) # enumerated
TC_SetLEDBrightness = bind(lib, "TC_SetLEDBrightness", [POINTER(c_char), c_short], c_short)
TC_SetSensorType = bind(lib, "TC_SetSensorType", [POINTER(c_char), c_short], c_short)
TC_SetTemperature = bind(lib, "TC_SetTemperature", [POINTER(c_char), c_short], c_short)
TC_SetTempLoopParams = bind(lib, "TC_SetTempLoopParams", [POINTER(c_char), POINTER(TC_LoopParameters)], c_short)

TC_StartPolling = bind(lib, "TC_StartPolling", [POINTER(c_char), c_int], c_bool)
TC_StopPolling = bind(lib, "TC_StopPolling", [POINTER(c_char)], None)
# TODO TC_TimeSinceLastMsgReceived
TC_WaitForMessage = bind(lib, "TC_WaitForMessage", [POINTER(c_char), POINTER(c_word), POINTER(c_word), POINTER(c_dword)], c_bool)
