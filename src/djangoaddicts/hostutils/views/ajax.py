import psutil

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

    template = loader.get_template("hostutils/bs5/ajax/host_cpu_stats.htm")

    def get(self, request, *args, **kwargs):
        cpu = int(request.GET["client_response"])
        self.data = dict(
            time=psutil.cpu_times(percpu=True)[cpu],
            time_percent=psutil.cpu_times_percent(percpu=True)[cpu],
            frequency=psutil.cpu_freq(percpu=True)[cpu],
        )
        return super().get(request, *args, **kwargs)


class GetHostNetworkStats(AjaxGetView):
    """
    Description:
        Get network statistics for a given network interface on the host machine.
    Args:
        request: AJAX request object.
    Returns:
        HttpResponse: JSON formatted response.
    """

    template = loader.get_template("hostutils/bs5/ajax/host_interface_stats.htm")

    def get(self, request, *args, **kwargs):
        interface = self.request.GET["client_response"]
        self.data = psutil.net_if_stats()[interface]
        return super().get(request, *args, **kwargs)


class GetHostParitionUsage(AjaxGetView):
    """
    Description:
        Get disk usage for a given partition on the host machine.
    Args:
        request: AJAX request object.
    Returns:
        HttpResponse: JSON formatted response.
    """

    template = loader.get_template("hostutils/bs5/ajax/host_partition_usage.htm")

    def get(self, request, *args, **kwargs):
        part = request.GET["client_response"]
        self.data = psutil.disk_usage(part)
        return super().get(request, *args, **kwargs)


class GetHostProcessDetails(AjaxGetView):
    """
    Description:
        Get process details for a given process on the host machine.
    Args:
        request: AJAX request object.
    Returns:
        HttpResponse: JSON formatted response.
    """

    template = loader.get_template("hostutils/bs5/ajax/host_process_details.htm")

    def get(self, request, *args, **kwargs):
        proc = request.GET["client_response"]
        try:
            self.data = psutil.Process(int(proc))
        except psutil.AccessDenied:
            self.data = {}
        return super().get(request, *args, **kwargs)
