.. _features:

Features
========
Bootstrap 5 dashboard pages are provided for host summary, CPU status, disk partitions, memory usage, network interfaces, and processes. Below are examples of each dashboard.


| 
Build In Views
----------------


Host Dashboard
^^^^^^^^^^^^^^
``{% url 'hostutils:host_details' %}``

.. image:: images/host.jpg
  :width: 600
  :alt: Alternative text


|
CPU Dashboard
^^^^^^^^^^^^^
``{% url 'hostutils:host_cpu' %}``

.. image:: images/cpu.jpg
  :width: 600
  :alt: Alternative text


|
Disk Dashboard
^^^^^^^^^^^^^^
``{% url 'hostutils:host_disk' %}``

.. image:: images/disk.jpg
  :width: 600
  :alt: Alternative text


|
Memory Dashboard
^^^^^^^^^^^^^^^^
``{% url 'hostutils:host_memory' %}``

.. image:: images/memory.jpg
  :width: 600
  :alt: Alternative text


|
Network Dashboard
^^^^^^^^^^^^^^^^^
``{% url 'hostutils:host_network' %}``

.. image:: images/network.jpg
  :width: 600
  :alt: Alternative text


|
Process Dashboard
^^^^^^^^^^^^^^^^^
``{% url 'hostutils:host_process' %}``

.. image:: images/process.jpg
  :width: 600
  :alt: Alternative text


| 
Custom Views
----


Creating a custom view/template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Custom views/templates can be used to override the Bootstrap 5 templates provided by default for GUI views. In your views, import the desired views(s) from hostutils and create a class that inherits the desired hostutils view.

Here is an example of creating a custom view using ShowHost:

.. code-block:: python

  from djangoaddicts.hostutils.views import ShowHost

  class MyCustomShowHostView(ShowHost):
      template_name = "my_custom_template.html"
      title = "My Custom Title"

|
