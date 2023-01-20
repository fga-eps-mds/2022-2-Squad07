from setuptools import setup, find_packages
  
with open('requirements.txt') as f:
    requirements = f.readlines()

with open("README.md", "r") as fh:
    readme = fh.read()
  
long_description = readme
  
cmds = ["cmd/*.txt"]
setup(
        name ='ez_docs',
        version ='1.0.0',
        author ='Bruno Ribeiro, Bruno Martins, Diógenes Dantas, Igor Penha, Lucas Gobbi e Rafael Nobre',
        author_email ='rafaelmedeirosnobre2001@gmail.com',
        description ='Um pacote python de geração de documentos automáticos',
        long_description = long_description,
        long_description_content_type ="text/markdown",
        license ='MIT',
        packages = find_packages(),
        package_data = {'ez_docs' : cmds },
        entry_points ={
            'console_scripts': [
                'ez-docs= ez_docs.main:main'
            ]
        },
        classifiers =(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        keywords =['ez_docs', 'ez-docs'],
        install_requires = requirements,
        zip_safe = False
)