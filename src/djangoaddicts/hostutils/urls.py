from django.urls import path

from djangoaddicts.hostutils.views import gui, htmx

app_name = "hostutils"

urlpatterns = [
    # host views
    path("host_cpu/", gui.ShowHostCpu.as_view(), name="host_cpu"),
    path("host_details/", gui.ShowHost.as_view(), name="host_details"),
    path("host_disk/", gui.ShowHostDisk.as_view(), name="host_disk"),
    path("host_memory/", gui.ShowHostMemory.as_view(), name="host_memory"),
    path("host_network/", gui.ShowHostNetwork.as_view(), name="host_network"),
    path("host_process/", gui.ShowHostProcesses.as_view(), name="host_process"),
    # htmx views
    path("get_host_processes/", htmx.GetHostProcesses.as_view(), name="get_host_processes"),
    path("get_cpu_stats/<int:cpu>/", htmx.GetHostCpuStats.as_view(), name="get_cpu_stats"),
    path("get_interface_stats/<str:interface>/", htmx.GetHostNetworkStats.as_view(), name="get_interface_stats"),
    path("get_partition_stats/", htmx.GetHostParitionStats.as_view(), name="get_partition_stats"),
    path("get_process_stats/<int:pid>/", htmx.GetHostProcessStats.as_view(), name="get_process_stats"),
]
