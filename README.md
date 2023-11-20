# FAIR Python script template (QSMM level 2)

This repository provides a cookiecutter template to get started with a FAIR python script. This corrseponds to a QSSM level 2 project within QuTech.
Using this template will help the reliability of the code you use and develop. It will also help you to make your code more reusable and reproducible. For more information on the FAIR principles see [this page](https://www.go-fair.org/fair-principles/). For more information on best practices for software development at QuTech see [QuTech's data and software information site](https://qutech-delft.github.io/data-and-software-info/).

## Pre-requisites

We assume you have installed (installation instructions can be found in the links):

* [Python](https://wiki.python.org/moin/BeginnersGuide/Download), with packages:
  * [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)
  * [poetry](https://python-poetry.org/docs/#installation)
* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Using the template

To use the template run the following command:

```bash
cookiecutter gh:QuTech-Delft/fair-python-script-template
```

You will get asked a few questions about the project you want to create. After answering these questions the template will be created in the current directory.

## Developing with the template

You have just created an instance of the template for your project. What now?

First setup a repository for your project. Discuss with your supervisor what the best place for this is (some research groups have their own groups for this on either gitlab or github). Once you have created this repository you can push the code you just created to this repository. To do this run the following commands:

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <url of your repository>
git push -u origin master
```

You can get started developing your own code! Start by opening the README.md file of your new repository. You will notice that additionally some of the values you answered have been filled in in this readme. Next to that there are also instruction on how to install, use, extend and test the example script that is provided in this repository. You can use these instructions to start developing your own code. Make sure to keep updating the readme with relevant documentation for your own code and to keep pushing your changes to your remote git repositry.

## Open sourcing your code

This template is initially intended for internal QuTech projects. If you want to use this template for a project that is publicly accessible in some way then it is very important that you also consider intellectual property and licensing. The Software Development Support Team of QuTech can point you in the right direction for this.
