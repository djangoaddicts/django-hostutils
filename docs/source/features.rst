.. _features:

Features
========
Bootstrap 5 dashboard pages are provided for host summary, CPU status, disk partitions, memory usage, netowrk interfaces, and processes. Below are examples of each dashboard.

|
Host Dashboard
--------------
``{% url 'hostutils:host_details' %}``

.. image:: images/host.jpg
  :width: 600
  :alt: Alternative text


|
CPU Dashboard
--------------
``{% url 'hostutils:host_cpu' %}``

.. image:: images/cpu.jpg
  :width: 600
  :alt: Alternative text


|
Disk Dashboard
--------------
``{% url 'hostutils:host_disk' %}``

.. image:: images/disk.jpg
  :width: 600
  :alt: Alternative text


|
Memory Dashboard
----------------
``{% url 'hostutils:host_memory' %}``

.. image:: images/memory.jpg
  :width: 600
  :alt: Alternative text


|
Network Dashboard
-----------------
``{% url 'hostutils:host_network' %}``

.. image:: images/network.jpg
  :width: 600
  :alt: Alternative text


|
Process Dashboard
-----------------
``{% url 'hostutils:host_process' %}``

.. image:: images/process.jpg
  :width: 600
  :alt: Alternative text

|
