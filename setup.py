from setuptools import setup
from setuptools import find_packages
from os import path

install_requirements = [
    "acme>=2.9.0",
    "certbot>=2.9.0",
    "setuptools",
    "mchost24",
]

setup_dir = path.abspath(path.dirname(__file__))

with open(path.join(setup_dir, "README.md")) as file:
    long_description = file.read()

setup(
    name="certbot-dns-mchost24",
    version="1.0.0",
    description="Certbot DNS Authenticator plugin for MCHost24",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoeJoeTV/certbot-dns-mchost24",
    author="JoeJoeTV",
    author_email="joejoetv@joejoetv.de",
    license="GNU General Public License v3.0",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Plugins",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Security",
        "Topic :: Security :: Cryptography",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requirements,
    entry_points={
        "certbot.plugins": [
            "dns-mchost24 = certbot_dns_mchost24.main:Authenticator"
        ]
    },
)