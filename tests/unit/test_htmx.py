import django
import os
import psutil
import subprocess

from django.shortcuts import reverse
from django.test import TestCase
from django.utils import timezone

from unittest.mock import patch


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.core.settings")
django.setup()


class GetHostProcessessTests(TestCase):
    """test GetHostProcesses ajax view"""
    def setUp(self):
        super(GetHostProcessessTests, self).setUp()
        self.url = reverse("hostutils:get_host_processes")
        self.headers = dict(HTTP_HX_REQUEST="true")

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

    def test_get_with_status_invalid_process(self):
        with self.assertRaises(psutil.NoSuchProcess):
            with patch('psutil.process_iter') as mocked_process_list:
                p = subprocess.Popen('ls', stdout=subprocess.PIPE)
                mocked_process_list.return_value = iter((psutil.Process(p.pid), psutil.Process(p.pid)))
                p.communicate()
                self.client.get(self.url, data={"status": "idle"}, **self.headers)

    def test_get_with_created_at_gte(self):
        response = self.client.get(self.url, data={"created_at__gte": timezone.now()}, **self.headers)
        self.assertEqual(response.status_code, 200)

    def test_get_with_created_at_lte(self):
        response = self.client.get(self.url, data={"created_at__lte": timezone.now()}, **self.headers)
        self.assertEqual(response.status_code, 200)
