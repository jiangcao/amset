from setuptools import find_packages, setup

from amset import __version__

with open("README.md", "r") as file:
    long_description = file.read()

if __name__ == "__main__":
    setup(
        name="amset",
        version=__version__,
        description="AMSET is a tool to calculate carrier transport properties "
        "from ab initio calculation data",
        long_description=long_description,
        long_description_content_type='text/markdown',
        url="https://github.com/hackingmaterials/amset",
        author="Alex Ganose",
        author_email="aganose@lbl.gov",
        license="modified BSD",
        keywords="mobility conductivity seebeck scattering lifetime rates dft vasp",
        packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
        package_data={
            "amset": [
                "defaults.yaml", "plot/amset_base.mplstyle", "plot/revtex.mplstyle"
            ]
        },
        data_files=["LICENSE", "requirements.txt"],
        zip_safe=False,
        install_requires=[
            'quadpy==0.16.2',
            'numpy==1.19.2',
            'pymatgen==2020.8.13',
            'scipy==1.5.2',
            'monty==4.0.0',
            'matplotlib==3.3.1',
            'BoltzTraP2==20.7.1',
            'tqdm==4.48.2',
            'tabulate==0.8.7',
            'memory_profiler==0.57.0',
            'spglib==1.16.0',
            'click==7.1.2',
            'sumo==2.0.0',
            'h5py==2.10.0',
            'pyFFTW==0.12.0',
            'interpolation==2.1.6',
        ],
        extras_require={
            'docs': [
                'mkdocs==1.1.2',
                'mkdocs-material==5.5.12',
                'mkdocs-minify-plugin==0.3.0',
                'mkdocs-macros-plugin==0.4.9',
                'markdown-include==0.6.0',
                'markdown-katex==202008.1025',
            ],
            'all-electron': ['pawpyseed==0.6.3'],
            'dev': [
                'coverage==5.2.1',
                'codacy-coverage==1.3.11',
                'pycodestyle==2.6.0',
                'mypy==0.782',
                'pydocstyle==5.1.1',
                'flake8==3.8.3',
                'pylint==2.6.0',
            ]
        },
        classifiers=[
            "Programming Language :: Python :: 3.6",
            "Development Status :: 4 - Beta",
            "Intended Audience :: Science/Research",
            "Intended Audience :: System Administrators",
            "Intended Audience :: Information Technology",
            "Operating System :: OS Independent",
            "Topic :: Other/Nonlisted Topic",
            "Topic :: Scientific/Engineering",
        ],
        test_suite="nose.collector",
        tests_require=["nose"],
        entry_points={"console_scripts": ["amset = amset.tools.cli:cli"]},
    )
