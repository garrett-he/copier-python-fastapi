from jinja2.ext import Extension, Environment
from packaging.specifiers import SpecifierSet


def version_list(value: str, versions: list[str]) -> list[str]:
    return list(SpecifierSet(value).filter(versions))


class VersionExtension(Extension):
    def __init__(self, environment: Environment):
        super().__init__(environment)

        environment.filters['version_list'] = version_list
