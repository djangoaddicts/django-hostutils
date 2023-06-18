from djangoaddicts.hostutils.views.gui import (
    ShowHost,
    ShowHostCpu,
    ShowHostDisk,
    ShowHostMemory,
    ShowHostNetwork,
    ShowHostProcesses,
)
from djangoaddicts.hostutils.views.htmx import (
    GetHostCpuStats,
    GetHostNetworkStats,
    GetHostParitionStats,
    GetHostProcesses,
    GetHostProcessStats,
)

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
