from django.urls import path
from djangoaddicts.hostutils.views import ajax
from djangoaddicts.hostutils.views import gui
from djangoaddicts.hostutils.views import htmx

app_name = "hostutils"

urlpatterns = [
    # host views
    path("host_details/", gui.ShowHost.as_view(), name="host_details"),
    path("host_network/", gui.ShowHostNetwork.as_view(), name="host_network"),
    path("host_process/", gui.ShowHostProcesses.as_view(), name="host_process"),
    path("host_disk/", gui.ShowHostDisk.as_view(), name="host_disk"),
    path("host_memory/", gui.ShowHostMemory.as_view(), name="host_memory"),
    path("host_cpu/", gui.ShowHostCpu.as_view(), name="host_cpu"),
    # ajax views
    path("host_interface_stats/", ajax.GetHostNetworkStats.as_view(), name="host_interface_stats"),
    path("host_process_details/", ajax.GetHostProcessDetails.as_view(), name="host_process_details"),
    path("host_partition_usage/", ajax.GetHostParitionUsage.as_view(), name="host_partition_usage"),
    path("get_host_cpu_stats/", ajax.GetHostCpuStats.as_view(), name="get_host_cpu_stats"),
    # htmx views
    path("get_host_processes/", htmx.GetHostProcesses.as_view(), name="get_host_processes"),
]
