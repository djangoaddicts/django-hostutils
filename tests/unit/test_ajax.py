from django.test import TestCase
from django.shortcuts import reverse


class GetHostCpuStatsTests(TestCase):
    """test GetHostCpuStats ajax view"""
    def setUp(self):
        super(GetHostCpuStatsTests, self).setUp()
        self.url = reverse("hostutils:get_cpu_stats")
        self.headers = dict(HTTP_X_REQUESTED_WITH="XMLHttpRequest")

    def test_get(self):
        response = self.client.get(self.url, data={"client_response": "1"}, **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/ajax/get_cpu_stats.htm")

    def test_get_with_invalid_data(self):
        response = self.client.get(self.url, data={"blah": 0}, **self.headers)
        self.assertEqual(response.status_code, 400)

    def test_get_with_invalid_request(self):
        response = self.client.get(self.url, data={"client_response": "999"})
        self.assertEqual(response.status_code, 400)


class GetHostNetworkStatsTests(TestCase):
    """test GetHostNetworkStats ajax view"""
    def setUp(self):
        super(GetHostNetworkStatsTests, self).setUp()
        self.url = reverse("hostutils:get_interface_stats")
        self.headers = dict(HTTP_X_REQUESTED_WITH="XMLHttpRequest")

    def test_get(self):
        response = self.client.get(self.url, data={"client_response": "lo"}, **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/ajax/get_interface_stats.htm")

    def test_get_with_invalid_data(self):
        response = self.client.get(self.url, data={"blah": 0}, **self.headers)
        self.assertEqual(response.status_code, 400)

    def test_get_with_invalid_request(self):
        response = self.client.get(self.url, data={"client_response": "999"})
        self.assertEqual(response.status_code, 400)


class GetHostParitionStatsTests(TestCase):
    """test GetHostParitionStats ajax view"""
    def setUp(self):
        super(GetHostParitionStatsTests, self).setUp()
        self.url = reverse("hostutils:get_partition_stats")
        self.headers = dict(HTTP_X_REQUESTED_WITH="XMLHttpRequest")

    def test_get(self):
        response = self.client.get(self.url, data={"client_response": "/"}, **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/ajax/get_partition_stats.htm")

    def test_get_with_invalid_data(self):
        response = self.client.get(self.url, data={"blah": 0}, **self.headers)
        self.assertEqual(response.status_code, 400)

    def test_get_with_invalid_request(self):
        response = self.client.get(self.url, data={"client_response": "999"})
        self.assertEqual(response.status_code, 400)


class GetHostProcessStatsTests(TestCase):
    """test GetHostProcessStats ajax view"""
    def setUp(self):
        super(GetHostProcessStatsTests, self).setUp()
        self.url = reverse("hostutils:get_process_stats")
        self.headers = dict(HTTP_X_REQUESTED_WITH="XMLHttpRequest")

    def test_get(self):
        response = self.client.get(self.url, data={"client_response": "1"}, **self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "hostutils/bs5/ajax/get_process_stats.htm")

    def test_get_with_invalid_data(self):
        response = self.client.get(self.url, data={"blah": 0}, **self.headers)
        self.assertEqual(response.status_code, 400)

    def test_get_with_invalid_request(self):
        response = self.client.get(self.url, data={"client_response": "999"})
        self.assertEqual(response.status_code, 400)
