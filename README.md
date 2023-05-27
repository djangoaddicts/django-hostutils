# django-hostutils
Host utilities package for django projects. Bootstrap 5 templates are provided.  Host metric data includes:
- Host OS, release, uptime
- CPU count and utilization
- Memory usage
- Disk partations and utilization
- Processes running, idle, sleeping
- Network interfaces and connections


<br/>

| | |
|--------------|------|
| Author       | David Slusser |
| Description  | Host utilities package for django projects. |
| Requirements | `Python 3.x` +<br>`Django 3.2.x` + |

<br/>

## Code Quality
| Workflow | Description             | Status                                                                       |
|----------|-------------------------|------------------------------------------------------------------------------|
|Bandit|security checks|![Bandit](https://github.com/davidslusser/workflow_tests/actions/workflows/bandit.yaml/badge.svg)|
|Black|code formatting|![Black](https://github.com/davidslusser/workflow_tests/actions/workflows/black.yaml/badge.svg)|
|Coveralls|code coverage status|[![Coverage Status](https://coveralls.io/repos/github/djangoaddicts/django-hostutils/badge.svg?branch=coveralls)](https://coveralls.io/github/djangoaddicts/django-hostutils?branch=coveralls)|
|Mypy|static type checking|![Mypy](https://github.com/davidslusser/workflow_tests/actions/workflows/mypy.yaml/badge.svg)|
|Pylint|static code analysis|![Pylint](https://github.com/davidslusser/workflow_tests/actions/workflows/pylint.yaml/badge.svg)|
|Pytest|unit testing|![Pytest](https://github.com/davidslusser/workflow_tests/actions/workflows/pytest.yaml/badge.svg)|

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
- pip install django-hostutils
- add the following to your INSTALLED_APPS

    ```python 
    djangoaddicts.hostutils
    ```
- add the following to your project-level urls.py:
   
   ```python
   path("hostutils/", include("djangoaddicts.hostutils.urls"), ),
   ```

<br/>

## Usage
Several pages are available. If you have a Bootstrap 5 nav-menu you can add the following snippet in your navbar where appropriate:

```
{% include 'hostutils/bs5/snippets/hostutils_nav_menu.htm' %}
```

Individual pages can also be linked directly:

- Host overview page: 

    ```
    {% url 'hostutils:host_details' %}
    ```

- CPU stats page: 

    ```
    {% url 'hostutils:host_cpu' %}
    ```

- Disk stats page: 

    ```
    {% url 'hostutils:host_disk' %}
    ```

- Memory stats page: 

    ```
    {% url 'hostutils:host_memory' %}
    ```

- Network stats page: 

    ```
    {% url 'hostutils:host_network' %}
    ```

- Process stats page: 

    ```
    {% url 'hostutils:host_process' %}
    ```
