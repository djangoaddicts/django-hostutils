import datetime
import psutil
from django.shortcuts import render
from django.views.generic import View

# import forms
from djangoaddicts.hostutils.forms import HostProcessFilterForm


class GetHostProcesses(View):
    
    @staticmethod
    def get_process_count(process_list: list , status: str) -> int:
        """get a count of processes for a given status

        Args:
            process_list (list): list of processes as returned from psutil.process_iter(
            status (str): name of process status to count

        Returns:
            int: number of processes of 'status'
        """
        count = 0
        for process in process_list:
            try:
                if process.status() == status:
                    count +=1 
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
