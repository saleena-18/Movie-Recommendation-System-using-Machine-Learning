from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

    REPO_NAME = "Movie-Recommendation-System-using-Machine-Learning"
    AUTHOR_NAME = 'saleena-18'
    SRC_REPO = 'src'
    LIST_OF_REQUIREMENTS = ['streamlit']

    setup(
        name = SRC_REPO,
        version = "0.0.1",
        author = AUTHOR_NAME,
        author_email = 'dassaleena18@gmail.com',
        description = 'A small example package for movies recommendation',
        long_description = long_description,
        long_description_content_type =  'text/markdown',
        url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
        package = [SRC_REPO],
        license="MIT",
        python_requires = '>=3.7',
        install_requires = LIST_OF_REQUIREMENTS
    )

