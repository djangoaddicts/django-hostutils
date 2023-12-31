from django.test import TestCase
from django.shortcuts import reverse
from unittest.mock import patch
import psutil
import subprocess
import itertools


class ShowHostCpuTests(TestCase):
    """test ShowHostCpu view"""

    def test_get(self):
        """verify page can be rendered"""
        url = reverse("hostutils:host_cpu")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/detail/cpu.html")


class ShowHostDiskTests(TestCase):
    """test ShowHostDisk view"""

    def test_get(self):
        """verify page can be rendered"""
        url = reverse("hostutils:host_disk")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/detail/disk.html")


class ShowHostTests(TestCase):
    """test ShowHost view"""

    def test_get(self):
        """verify page can be rendered"""
        url = reverse("hostutils:host_details")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/detail/detail_host.html")


class ShowHostMemoryTests(TestCase):
    """test ShowHostMemory view"""

    def test_get(self):
        """verify page can be rendered"""
        url = reverse("hostutils:host_memory")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/detail/memory.html")


class ShowHostNetworkTests(TestCase):
    """test ShowHostNetwork view"""

    def test_get(self):
        """verify page can be rendered"""
        url = reverse("hostutils:host_network")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/detail/network.html")


class ShowHostProcessesTests(TestCase):
    """test ShowHostProcesses view"""

    def test_get(self):
        """verify page can be rendered"""
        url = reverse("hostutils:host_process")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/detail/processes.html")

    def test_get_with_invalid(self):
        """verify page is redered if psutil.NoSuchProcess is raised"""
        url = reverse("hostutils:host_process")
        process_list = psutil.process_iter()
        with patch("psutil.process_iter") as mocked_process_list:
            p = subprocess.Popen("ls", stdout=subprocess.PIPE)
            mp = iter((psutil.Process(p.pid), psutil.Process(p.pid)))
            p.communicate()
            mocked_process_list.return_value = itertools.chain(mp, process_list)
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "hostutils/bs5/detail/processes.html")
