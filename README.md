# django-hostutils
[![Downloads](https://static.pepy.tech/badge/django-hostutils)](https://pepy.tech/project/django-hostutils)
[![OpenSSF Best Practices](https://bestpractices.coreinfrastructure.org/projects/7474/badge)](https://bestpractices.coreinfrastructure.org/projects/7474)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-hostutils)


Django hostutils is a collection of utilities to provide information and metrics for hosts running a Django project. Data is available via included Bootstrap 5 templates and custom views/templates also be used. Host metric data includes:
- Host OS, release, uptime
- CPU count and utilization
- Memory usage
- Disk partations and utilization
- Processes running, idle, sleeping
- Network interfaces and connections


<br/>

## Code Quality
| Workflow | Description             | Status                                                                       |
|----------|-------------------------|------------------------------------------------------------------------------|
|Bandit|security checks|![Bandit](https://github.com/djangoaddicts/django-hostutils/actions/workflows/bandit.yaml/badge.svg)|
|Black|code formatting|![Black](https://github.com/djangoaddicts/django-hostutils/actions/workflows/black.yaml/badge.svg)|
|Coveralls|code coverage status|[![Coverage Status](https://coveralls.io/repos/github/djangoaddicts/django-hostutils/badge.svg?branch=coveralls)](https://coveralls.io/github/djangoaddicts/django-hostutils?branch=coveralls)|
|Isort|python import ordering|![Isort](https://github.com/djangoaddicts/django-hostutils/actions/workflows/isort.yaml/badge.svg)|
|Mypy|static type checking|![Mypy](https://github.com/djangoaddicts/django-hostutils/actions/workflows/mypy.yaml/badge.svg)|
|Pytest|unit testing|![Pytest](https://github.com/djangoaddicts/django-hostutils/actions/workflows/pytest.yaml/badge.svg)|
|Radon|code complexity analysis|![Radon](https://github.com/djangoaddicts/django-hostutils/actions/workflows/radon.yaml/badge.svg)|
|Ruff|static code analysis|![Ruff](https://github.com/djangoaddicts/django-hostutils/actions/workflows/ruff.yaml/badge.svg)|
|Safety|security vulnerability checks|![Saftey](https://github.com/djangoaddicts/django-hostutils/actions/workflows/safety.yaml/badge.svg)|


<br/>

### Code Coverage Dashboard:
https://coveralls.io/github/djangoaddicts/django-hostutils


<br/>

## Documentation
| Workflow | Description             | Status                                                                       |
|----------|-------------------------|------------------------------------------------------------------------------|
|Docs|ReadTheDocs Build|[![Documentation Status](https://readthedocs.org/projects/django-hostutils/badge/?version=latest)](https://django-hostutils.readthedocs.io/en/latest/?badge=latest)|

Full documentation is available here:

https://django-hostutils.readthedocs.io/en/latest/index.html 


<br/>

## License
django-hostutils is licensed under the GNU-3 license (see the LICENSE file for details).

https://github.com/davidslusser/django-hostutils/blob/docs/LICENSE 


<br/>

## Installation 
- install via pip:
    ``` 
    pip install django-hostutils
    ```
- add the following to your INSTALLED_APPS in settings.py:

    ```python 
    djangoaddicts.hostutils
    ```
- add the following to your project-level urls.py:
   
   ```python
   path("hostutils/", include("djangoaddicts.hostutils.urls"), ),
   ```


<br/>

## Usage

### Included Views
Several pages are available. If you have a Bootstrap 5 nav-menu you can add the following snippet in your navbar where appropriate:

```python
{% include 'hostutils/bs5/snippets/hostutils_nav_menu.htm' %}
```

Individual pages can also be linked directly:

- Host overview page: 

    ```python
    {% url 'hostutils:host_details' %}
    ```

- CPU stats page: 

    ```python
    {% url 'hostutils:host_cpu' %}
    ```

- Disk stats page: 

    ```python
    {% url 'hostutils:host_disk' %}
    ```

- Memory stats page: 

    ```python
    {% url 'hostutils:host_memory' %}
    ```

- Network stats page: 

    ```python
    {% url 'hostutils:host_network' %}
    ```

- Process stats page: 

    ```python
    {% url 'hostutils:host_process' %}
    ```

### Custom Views
Custom views/templates can be used to override the Bootstrap 5 templates provided by default for GUI views. In your views, import the desired views(s) from hostutils and create a class that inherits the desired hostutils view.

- Here is an example of creating a custom view using ShowHost:
    
    ```python
    from djangoaddicts.hostutils.views import ShowHost

    class MyCustomShowHostView(ShowHost):
        template_name = "my_custom_template.html"
        title = "My Custom Title"
    ```
