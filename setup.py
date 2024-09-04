from setuptools import setup, find_packages

setup(
    name="enigma",
    version="0.1.0",
    description="A simple encryption library using matrix-based algorithms",
    packages=find_packages(),  # Inclui todos os pacotes Python na pasta
    install_requires=[
        'numpy>=1.18.0',
        'flask>=2.0.0'
    ],
    entry_points={
        'console_scripts': [
            'enigma-server=enigma.main:app.run',  # Comando para rodar o servidor Flask
        ],
    },
    author="João Gabriel Rutkowski Delomo & João Whitaker Citino",
    author_email="joaocitino10@gmail.com",
    url="https://github.com/joaowcitino/alglin_criptografia",  # Atualize com seu repositório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)