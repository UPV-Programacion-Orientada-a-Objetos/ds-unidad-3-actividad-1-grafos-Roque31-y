from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

# Configuración de la extensión de Cython
extensions = [
    Extension(
        name="neuronet_core",
        sources=[
            "neuronet_core.pyx",
            "cpp/GrafoDisperso.cpp"
        ],
        include_dirs=[
            ".",
            np.get_include()
        ],
        language="c++",
        extra_compile_args=["/std:c++17"] if __import__('sys').platform == 'win32' else ["-std=c++17"],
        extra_link_args=[]
    )
]

setup(
    name="NeuroNet",
    version="1.0.0",
    description="Sistema híbrido de análisis de grafos masivos con C++ y Python",
    author="NeuroNet Team",
    ext_modules=cythonize(
        extensions,
        compiler_directives={
            'language_level': "3",
            'embedsignature': True
        }
    ),
    zip_safe=False,
    install_requires=[
        'numpy',
        'networkx',
        'matplotlib'
    ]
)
