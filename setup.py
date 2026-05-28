from setuptools import setup

with open('README.md','r', encoding='utf-8') as f:
    long_desciption = f.read()

repo_name = 'book_recommender_system'
author_user_name = 'RaviNamdeoo'
src_repo = 'src'
list_of_requirements = ['numpy','pandas','streamlit']

setup(
    name = src_repo,
    version='0.0.1',
    author = author_user_name,
    description='Small package for Book recommender system',
    long_description=long_desciption,
    long_description_content_type='text/markdown',
    url = f'https://github.com/{author_user_name}/{repo_name}',
    author_email='cmnamdeo729@gmail.com',
    packages=[src_repo],
    licence='MIT',
    python_requires = '>=3.7',
    install_requires=list_of_requirements
)