from djangoaddicts.hostutils.views.ajax import (
    GetHostCpuStats,
    GetHostNetworkStats,
    GetHostParitionStats,
    GetHostProcessStats,
)
from djangoaddicts.hostutils.views.gui import (
    ShowHost,
    ShowHostCpu,
    ShowHostDisk,
    ShowHostMemory,
    ShowHostNetwork,
    ShowHostProcesses,
)
from djangoaddicts.hostutils.views.htmx import GetHostProcesses


__all__ = [
    "GetHostCpuStats",
    "GetHostNetworkStats",
    "GetHostParitionStats",
    "GetHostProcessStats",
    "GetHostProcesses",
    "ShowHost",
    "ShowHostCpu",
    "ShowHostDisk",
    "ShowHostDisk",
    "ShowHostMemory",
    "ShowHostNetwork",
    "ShowHostProcesses",
]
