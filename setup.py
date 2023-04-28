from setuptools import setup


# https://stackoverflow.com/questions/75091265/python-setuptools-scm-get-version-from-git-tags
# https://github.com/pypa/setuptools_scm#importing-in-setuppy

def myversion():
    from setuptools_scm.version import SEMVER_PATCH, guess_next_simple_semver, release_branch_semver_version
    def my_release_branch_semver_version(version):
        v = release_branch_semver_version(version)
        if v == version.format_next_version(guess_next_simple_semver, retain=SEMVER_PATCH):
            return version.format_next_version(guess_next_simple_semver, fmt="{guessed}", retain=SEMVER_PATCH)
        return v

    return {
        'version_scheme': my_release_branch_semver_version,
        'local_scheme': 'no-local-version',
    }


setup(use_scm_version=myversion)
