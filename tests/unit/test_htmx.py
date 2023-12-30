import itertools
import psutil
import subprocess

from django.shortcuts import reverse
from django.test import TestCase
from django.utils import timezone

from unittest.mock import patch


class GetHostProcessessTests(TestCase):
    """test GetHostProcesses ajax view"""

    def setUp(self):
        super(GetHostProcessessTests, self).setUp()
        self.url = reverse("hostutils:get_host_processes")
        self.headers = dict(HTTP_HX_REQUEST="true")
        self.now = timezone.now()

    def test_get(self):
        response = self.client.get(self.url, **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/snippets/host_process_card.htm")
        self.assertTemplateUsed(response, "hostutils/bs5/snippets/host_process_card_swap.htm")

    def test_get_with_clear(self):
        response = self.client.get(self.url, data={"clear": True}, **self.headers)
        self.assertEqual(response.status_code, 200)

    def test_get_with_status(self):
        response = self.client.get(self.url, data={"status": "idle"}, **self.headers)
        self.assertEqual(response.status_code, 200)

    def test_get_with_created_at_gte(self):
        response = self.client.get(self.url, data={"created_at__gte": timezone.now()}, **self.headers)
        self.assertEqual(response.status_code, 200)

    def test_get_with_created_at_lte(self):
        response = self.client.get(self.url, data={"created_at__lte": timezone.now()}, **self.headers)
        self.assertEqual(response.status_code, 200)

    def test_get_with_status_running(self):
        with patch("psutil.Process.status") as status:
            status.return_value = "running"
            self.client.get(self.url, data={"status": "running"}, **self.headers)

    def test_get_with_invalid(self):
        process_list = psutil.process_iter()
        with patch("psutil.process_iter") as mocked_process_list:
            p = subprocess.Popen("ls", stdout=subprocess.PIPE)
            mp = iter((psutil.Process(p.pid), psutil.Process(p.pid)))
            p.communicate()
            mocked_process_list.return_value = itertools.chain(mp, process_list)
            self.client.get(self.url, **self.headers)

    def test_get_with_status_invalid(self):
        with patch("psutil.Process.status") as status:
            status.return_value = "running"
            process_list = psutil.process_iter()
            with patch("psutil.process_iter") as mocked_process_list:
                p = subprocess.Popen("ls", stdout=subprocess.PIPE)
                mp = iter((psutil.Process(p.pid), psutil.Process(p.pid)))
                p.communicate()
                mocked_process_list.return_value = itertools.chain(mp, process_list)
                self.client.get(self.url, data={"status": "running"}, **self.headers)

    def test_get_with_gte_invalid(self):
        with patch("psutil.Process.status") as status:
            status.return_value = "running"
            process_list = psutil.process_iter()
            with patch("psutil.process_iter") as mocked_process_list:
                p = subprocess.Popen("ls", stdout=subprocess.PIPE)
                mp = iter((psutil.Process(p.pid), psutil.Process(p.pid)))
                p.communicate()
                mocked_process_list.return_value = itertools.chain(mp, process_list)
                self.client.get(
                    self.url,
                    data={"status": "running", "created_at__gte": self.now - timezone.timedelta(days=1)},
                    **self.headers,
                )

    def test_get_with_lte_invalid(self):
        with patch("psutil.Process.status") as status:
            status.return_value = "running"
            process_list = psutil.process_iter()
            with patch("psutil.process_iter") as mocked_process_list:
                p = subprocess.Popen("ls", stdout=subprocess.PIPE)
                mp = iter((psutil.Process(p.pid), psutil.Process(p.pid)))
                p.communicate()
                mocked_process_list.return_value = itertools.chain(mp, process_list)
                self.client.get(
                    self.url,
                    data={"status": "running", "created_at__lte": self.now - timezone.timedelta(days=1)},
                    **self.headers,
                )


class GetHostCpuStatsTests(TestCase):
    """test GetHostCpuStats htmx view"""

    def setUp(self):
        super(GetHostCpuStatsTests, self).setUp()
        self.url = reverse("hostutils:get_cpu_stats", kwargs={"cpu": 1})
        self.headers = dict(HTTP_HX_REQUEST="true")

    def test_get(self):
        response = self.client.get(self.url, **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/htmx/get_cpu_stats.htm")

    def test_get_with_invalid_data(self):
        url = reverse("hostutils:get_cpu_stats", kwargs={"cpu": 99})
        response = self.client.get(url, **self.headers)
        self.assertEqual(response.status_code, 400)

    def test_get_with_invalid_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 400)


class GetHostNetworkStatsTests(TestCase):
    """test GetHostNetworkStats htmx view"""

    def setUp(self):
        super(GetHostNetworkStatsTests, self).setUp()
        self.url = reverse("hostutils:get_interface_stats", kwargs={"interface": "lo"})
        self.headers = dict(HTTP_HX_REQUEST="true")

    def test_get(self):
        response = self.client.get(self.url, **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/htmx/get_interface_stats.htm")

    def test_get_with_invalid_data(self):
        url = reverse("hostutils:get_interface_stats", kwargs={"interface": "blah"})
        response = self.client.get(url, **self.headers)
        self.assertEqual(response.status_code, 400)

    def test_get_with_invalid_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 400)


class GetHostParitionStatsTests(TestCase):
    """test GetHostParitionStats htmx view"""

    def setUp(self):
        super(GetHostParitionStatsTests, self).setUp()
        self.url = reverse("hostutils:get_partition_stats") + "?part=/"
        self.headers = dict(HTTP_HX_REQUEST="true")

    def test_get(self):
        response = self.client.get(self.url, **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/htmx/get_partition_stats.htm")

    def test_get_with_invalid_data(self):
        url = reverse("hostutils:get_partition_stats") + "?part=blah"
        response = self.client.get(url, **self.headers)
        self.assertEqual(response.status_code, 400)

    def test_get_with_invalid_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 400)


class GetHostProcessStatsTests(TestCase):
    """test GetHostProcessStats htmx view"""

    def setUp(self):
        super(GetHostProcessStatsTests, self).setUp()
        self.url = reverse("hostutils:get_process_stats", kwargs={"pid": 1})
        self.headers = dict(HTTP_HX_REQUEST="true")

    def test_get(self):
        response = self.client.get(self.url, **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/htmx/get_process_stats.htm")

    def test_access_denied(self):
        with patch("psutil.Process") as mocked_process:
            mocked_process.side_effect = psutil.AccessDenied
            response = self.client.get(self.url, **self.headers)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "hostutils/bs5/htmx/get_process_stats.htm")

    def test_exe(self):
        with patch("psutil.Process") as mocked_process:
            mocked_process.exe = object
            response = self.client.get(self.url, **self.headers)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "hostutils/bs5/htmx/get_process_stats.htm")

    def test_get_with_invalid_data(self):
        url = reverse("hostutils:get_process_stats", kwargs={"pid": 0})
        response = self.client.get(url, **self.headers)
        self.assertEqual(response.status_code, 200)

    def test_get_with_invalid_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 400)
