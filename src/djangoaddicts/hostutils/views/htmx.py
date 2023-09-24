import datetime

import psutil
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import View
from handyhelpers.views.htmx import BuildBootstrapModalView

# import forms
from djangoaddicts.hostutils.forms import HostProcessFilterForm


class GetHostCpuStats(BuildBootstrapModalView):
    """Get statistics for a given CPU"""

    modal_button_close = None
    modal_button_submit = "Close"
    modal_size = "modal-lg"
    modal_title = "CPU Details"

    def get(self, request, *args, **kwargs):
        context = {}
        self.modal_subtitle = kwargs["cpu"]
        try:
            cpu = kwargs["cpu"]
            context = {
                "time": psutil.cpu_times(percpu=True)[cpu],
                "time_percent": psutil.cpu_times_percent(percpu=True)[cpu],
                "frequency": psutil.cpu_freq(percpu=True)[cpu],
            }
        except IndexError:
            return HttpResponse("Invalid request", status=400)
        self.modal_body = loader.render_to_string("hostutils/bs5/htmx/get_cpu_stats.htm", context=context)
        return super().get(request, *args, **kwargs)


class GetHostNetworkStats(BuildBootstrapModalView):
    """Get statistics for a given network interface"""

    modal_button_close = None
    modal_button_submit = "Close"
    modal_size = "modal-lg"
    modal_title = "Network Interface Details"

    def get(self, request, *args, **kwargs):
        context = {}
        self.modal_subtitle = kwargs["interface"]
        try:
            context["data"] = psutil.net_if_stats()[kwargs["interface"]]
        except KeyError:
            return HttpResponse("Invalid request", status=400)
        self.modal_body = loader.render_to_string("hostutils/bs5/htmx/get_interface_stats.htm", context=context)
        return super().get(request, *args, **kwargs)


class GetHostParitionStats(BuildBootstrapModalView):
    """Get statistics for a given disk partition"""

    modal_button_close = None
    modal_button_submit = "Close"
    modal_title = "Partition Details"

    def get(self, request, *args, **kwargs):
        context = {}
        part = request.GET.get("part", None)
        self.modal_subtitle = part
        try:
            context["data"] = psutil.disk_usage(part)
        except FileNotFoundError:
            return HttpResponse("Invalid request", status=400)
        self.modal_body = loader.render_to_string("hostutils/bs5/htmx/get_partition_stats.htm", context=context)
        return super().get(request, *args, **kwargs)


class GetHostProcesses(View):
    """Get host processes"""

    @staticmethod
    def get_process_count(process_list: list, status: str) -> int:
        """get a count of processes for a given status

        Args:
            process_list (list): list of processes as returned from psutil.process_iter()
            status (str): name of process status to count

        Returns:
            int: number of processes of 'status'
        """
        count = 0
        for process in process_list:
            try:
                if process.status() == status:
                    count += 1
            except psutil.NoSuchProcess:
                continue
        return count

    def get(self, request):
        """Get host prcesses"""
        context = {}
        process_list = list(psutil.process_iter())
        filter_form = HostProcessFilterForm(request.GET or None)
        context["counts"] = {
            "running": self.get_process_count(process_list, "running"),
            "sleeping": self.get_process_count(process_list, "sleeping"),
            "idle": self.get_process_count(process_list, "idle"),
            "stopped": self.get_process_count(process_list, "stopped"),
            "zombie": self.get_process_count(process_list, "zombie"),
            "dead": self.get_process_count(process_list, "dead"),
        }

        if request.GET.dict().get("clear", None):
            context["clear_filter"] = False

        else:
            if filter_form.is_valid():
                context["clear_filter"] = True

                if filter_form.cleaned_data.get("status", None):
                    filtered_process_list = []
                    for i in process_list:
                        if i.status() in filter_form.cleaned_data["status"]:
                            filtered_process_list.append(i)
                    process_list = filtered_process_list

                if filter_form.cleaned_data.get("created_at__gte", None):
                    filtered_process_list = []
                    for i in process_list:
                        if i.create_time() > filter_form.cleaned_data["created_at__gte"].timestamp():
                            filtered_process_list.append(i)
                    process_list = filtered_process_list
                if filter_form.cleaned_data.get("created_at__lte", None):
                    filtered_process_list = []
                    for i in process_list:
                        if i.create_time() < filter_form.cleaned_data["created_at__lte"].timestamp():
                            filtered_process_list.append(i)
                    process_list = filtered_process_list

        context["process_list"] = process_list
        context["title"] = "Host Processes"
        context["now"] = datetime.datetime.now()
        context["subtitle"] = psutil.os.uname()[1]
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
        return render(request, template_name="hostutils/bs5/snippets/host_process_card_swap.htm", context=context)


class GetHostProcessStats(BuildBootstrapModalView):
    """Get statistics for a given process"""

    modal_button_submit = None
    modal_size = "modal-lg"
    modal_title = "Process Details"

    def get(self, request, *args, **kwargs):
        context = {}
        self.modal_subtitle = kwargs["pid"]
        try:
            data = psutil.Process(kwargs["pid"])
            context = {
                "pid": data.pid,
                "ppid": data.ppid(),
                "name": data.name(),
                "status": data.status(),
                "create_time": data.create_time(),
                "username": data.username(),
                "cmdline": data.cmdline(),
                "cpu_num": data.cpu_num(),
                "cpu_percent": data.cpu_percent(),
                "memory_percent": data.memory_percent(),
                "num_threads": data.num_threads(),
                "threads": data.threads(),
            }
            context["cwd"] = data.cwd()
            context["exe"] = data.exe()
        except psutil.AccessDenied:
            pass
        except psutil.NoSuchProcess:
            pass
        self.modal_body = loader.render_to_string("hostutils/bs5/htmx/get_process_stats.htm", context=context)
        return super().get(request, *args, **kwargs)
