import os

from hyfi import HyFI, about, global_config

from ._version import __version__

# Read and parse pyproject.toml
current_dir = os.path.dirname(os.path.abspath(__file__))
about_path = os.path.join(current_dir, "conf", "about", "__init__.yaml")

about_data = HyFI.load(about_path)

# Extract package information
about._package_name_ = about_data.get("_package_name_", "package_name")
about.name = about_data.get("name", "package name")
about.authors = about_data.get("authors", ["Author name"])
about.description = about_data.get("description", "package description")
about.homepage = about_data.get("homepage", "https://package.homepage")
about.license = about_data.get("license", "MIT")
about.version = __version__
global_config.hyfi_package_config_path = "pkg://aibasics.conf"


def get_version() -> str:
    """This is the cli function of the package"""
    return __version__
