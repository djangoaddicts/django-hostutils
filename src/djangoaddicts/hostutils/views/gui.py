import datetime

import psutil
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from handyhelpers.permissions import InAnyGroup

# import forms
from djangoaddicts.hostutils.forms import HostProcessFilterForm


class ShowHost(InAnyGroup, View):
    """Display dashboard like page showing an overview of host data"""

    template_name = "hostutils/bs5/detail/detail_host.html"
    title = "Host Dashboard"
    permission_dict = {"GET": getattr(settings, "DJA_HOSTUTILS_PERMISSIONS", [])}

    def get(self, request, *args, **kwargs):
        """allow get method"""
        now = datetime.datetime.now()
        context = {}
        context["title"] = self.title
        context["subtitle"] = psutil.os.uname()[1]
        context["cpu_count"] = psutil.cpu_count(logical=False)
        context["memory"] = psutil.virtual_memory()
        context["disk_usage"] = psutil.disk_usage("/")
        context["disk_io_counters"] = psutil.disk_io_counters()
        context["network"] = psutil.net_connections()
        context["pids"] = psutil.pids()

        boot_time = psutil.boot_time()
        diff = relativedelta(now, datetime.datetime.fromtimestamp(boot_time))
        context["times"] = {}
        context["times"]["boot_time"] = datetime.datetime.fromtimestamp(boot_time)
        context["times"]["up_time"] = (
            f"{diff.days} days, {diff.hours} hours, {diff.minutes} minutes, " f"{diff.seconds} seconds"
        )

        context["platform"] = psutil.os.uname()

        return render(request, self.template_name, context=context)


class ShowHostCpu(InAnyGroup, View):
    """Display dashboard like page showing host cpu data"""

    template_name = "hostutils/bs5/detail/cpu.html"
    title = "CPU Dashboard"
    permission_dict = {"GET": getattr(settings, "DJA_HOSTUTILS_PERMISSIONS", [])}

    def get(self, request, *args, **kwargs):
        """CPU Dashboard"""
        context = {}
        context["title"] = self.title
        context["subtitle"] = psutil.os.uname()[1]
        context["stats"] = psutil.cpu_stats()
        context["physical_count"] = psutil.cpu_count(logical=False)
        context["logical_count"] = psutil.cpu_count(logical=True)
        context["percent"] = psutil.cpu_percent(interval=None)
        context["times_list"] = psutil.cpu_times(percpu=True)
        context["times_percent_list"] = psutil.cpu_times_percent(percpu=True)
        context["percent_list"] = psutil.cpu_percent(interval=None, percpu=True)
        context["frequency_list"] = psutil.cpu_freq(percpu=True)
        context["cpu_range"] = list(range(psutil.cpu_count(logical=True)))
        cpu_data = {}
        for i in range(context["logical_count"]):
            cpu_data[i] = {
                "times": context["times_list"][i],
                "time_percent": context["times_percent_list"][i],
                "percent": context["percent_list"][i],
                "frequency": context["frequency_list"][i],
            }
        context["cpu_data"] = cpu_data
        context["load_avg_1"], context["load_avg_5"], context["load_avg_15"] = [
            round(x / psutil.cpu_count() * 100, 2) for x in psutil.getloadavg()
        ]
        return render(request, self.template_name, context=context)


class ShowHostDisk(InAnyGroup, View):
    """Display dashboard like page showing host disk data"""

    template_name = "hostutils/bs5/detail/disk.html"
    title = "Disk Dashboard"
    permission_dict = {"GET": getattr(settings, "DJA_HOSTUTILS_PERMISSIONS", [])}

    def get(self, request, *args, **kwargs):
        """allow get method"""
        context = {}
        context["title"] = self.title
        context["subtitle"] = psutil.os.uname()[1]
        context["usage"] = psutil.disk_usage("/")
        context["io_counters"] = psutil.disk_io_counters()
        context["partition_lists"] = psutil.disk_partitions()
        return render(request, self.template_name, context=context)


class ShowHostMemory(InAnyGroup, View):
    """Display dashboard like page showing host memory data"""

    template_name = "hostutils/bs5/detail/memory.html"
    title = "Memory Dashboard"
    permission_dict = {"GET": getattr(settings, "DJA_HOSTUTILS_PERMISSIONS", [])}

    def get(self, request, *args, **kwargs):
        """allow get method"""
        context = {}
        context["title"] = self.title
        context["subtitle"] = psutil.os.uname()[1]
        context["virtual"] = psutil.virtual_memory()
        context["swap"] = psutil.swap_memory()
        return render(request, self.template_name, context=context)


class ShowHostNetwork(InAnyGroup, View):
    """Display dashboard like page showing host network data"""

    template_name = "hostutils/bs5/detail/network.html"
    title = "Network Dashboard"
    permission_dict = {"GET": getattr(settings, "DJA_HOSTUTILS_PERMISSIONS", [])}

    def get(self, request, *args, **kwargs):
        """allow get method"""
        context = {}
        context["title"] = self.title
        context["subtitle"] = psutil.os.uname()[1]
        context["connection_list"] = psutil.net_connections()
        context["interface_list"] = psutil.net_if_addrs()
        context["stats_list"] = psutil.net_if_stats()
        context["counters"] = psutil.net_io_counters()
        return render(request, self.template_name, context=context)


class ShowHostProcesses(InAnyGroup, View):
    """Display dashboard like page showing host process data"""

    template_name = "hostutils/bs5/detail/processes.html"
    title = "Process Dashboard"
    permission_dict = {"GET": getattr(settings, "DJA_HOSTUTILS_PERMISSIONS", [])}

    def get(self, request, *args, **kwargs):
        """allow get method"""
        context = {}
        context["title"] = self.title
        context["now"] = datetime.datetime.now()
        context["subtitle"] = psutil.os.uname()[1]
        counts = {"running": 0, "sleeping": 0, "idle": 0, "stopped": 0, "zombie": 0, "dead": 0, "disk-sleep": 0}
        process_list = []
        for process in psutil.process_iter():
            try:
                counts[process.status()] += 1
                process_list.append(
                    {
                        "pid": process.pid,
                        "name": process.name(),
                        "status": process.status(),
                        "create_time": process.create_time(),
                    }
                )
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        context["process_list"] = process_list
        context["counts"] = counts
        filter_form = {}
        filter_form["form"] = HostProcessFilterForm(request.GET or None)
        filter_form["modal_name"] = "filter_processes"
        filter_form["modal_size"] = "modal-lg"
        filter_form["modal_title"] = "Filter Host Processes"
        filter_form["hx_method"] = "hx-get"
        filter_form["hx_url"] = "/hostutils/get_host_processes"
        filter_form["hx_target"] = "id_process_list_container"
        filter_form["method"] = "GET"
        filter_form["action"] = "Filter"
        context["filter_form"] = filter_form
        return render(request, self.template_name, context=context)
