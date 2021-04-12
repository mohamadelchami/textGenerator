import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRED = ['beautifulsoup4', 'Jinja2', 'FacebookChatPhisher']
setuptools.setup(
    name="phishingTextGenerator", 
    version="0.0.1",
    author="Ashraf Taifour, Abdullah Arif, Abdullah Chattha, Abdullah Chattha, Steve Pham",
    description="A program to generate phishing text based on the output of the Facebook Scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohamadelchami/textGenerator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    package_data={'phishingTextGenerator': ['templates/*']},
    include_package_data=True,
    install_requires=REQUIRED,
    python_requires='>=3.7',
)