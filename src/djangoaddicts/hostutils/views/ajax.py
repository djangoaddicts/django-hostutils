import psutil

from django.http import HttpResponse
from django.template import loader

from handyhelpers.views.ajax import AjaxGetView


class GetHostCpuStats(AjaxGetView):
    """
    Description:
        Get CPU status for a given cpu on the host machine.
    Args:
        request: AJAX request object.
    Returns:
        HttpResponse: JSON formatted response.
    """

    template = loader.get_template("hostutils/bs5/ajax/get_cpu_stats.htm")

    def get(self, request, *args, **kwargs):
        try:
            cpu = int(request.GET["client_response"])
            self.data = {
                "time": psutil.cpu_times(percpu=True)[cpu],
                "time_percent": psutil.cpu_times_percent(percpu=True)[cpu],
                "frequency": psutil.cpu_freq(percpu=True)[cpu],
            }
            return super().get(request, *args, **kwargs)
        except Exception as err:
            return HttpResponse('Invalid request inputs', status=400)


class GetHostNetworkStats(AjaxGetView):
    """
    Description:
        Get network statistics for a given network interface on the host machine.
    Args:
        request: AJAX request object.
    Returns:
        HttpResponse: JSON formatted response.
    """

    template = loader.get_template("hostutils/bs5/ajax/get_interface_stats.htm")

    def get(self, request, *args, **kwargs):
        try:
            interface = self.request.GET["client_response"]
            self.data = psutil.net_if_stats()[interface]
            return super().get(request, *args, **kwargs)
        except Exception as err:
            return HttpResponse('Invalid request inputs', status=400)


class GetHostParitionStats(AjaxGetView):
    """
    Description:
        Get disk usage for a given partition on the host machine.
    Args:
        request: AJAX request object.
    Returns:
        HttpResponse: JSON formatted response.
    """

    template = loader.get_template("hostutils/bs5/ajax/get_partition_stats.htm")

    def get(self, request, *args, **kwargs):
        try:
            part = request.GET["client_response"]
            self.data = psutil.disk_usage(part)
            return super().get(request, *args, **kwargs)
        except Exception as err:
            return HttpResponse('Invalid request inputs', status=400)


class GetHostProcessStats(AjaxGetView):
    """
    Description:
        Get process details for a given process on the host machine.
    Args:
        request: AJAX request object.
    Returns:
        HttpResponse: JSON formatted response.
    """

    template = loader.get_template("hostutils/bs5/ajax/get_process_stats.htm")

    def get(self, request, *args, **kwargs):
        try:
            proc = request.GET["client_response"]
            self.data = psutil.Process(int(proc))
        except Exception as err:
            return HttpResponse('Invalid request inputs', status=400)
        except psutil.AccessDenied:
            self.data = {}
        return super().get(request, *args, **kwargs)
