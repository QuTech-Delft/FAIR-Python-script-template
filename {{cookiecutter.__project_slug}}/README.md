# {{ cookiecutter.project_name }}

**Owner:** {{ cookiecutter.author_name }} ({{ cookiecutter.author_email }})

## Scope

In this section we describe why this sofware was built and give a quick overview of the system.

### Purpose
<!--
Describe the purpose of your software project. Describe why and in which context you are writing this software. Describe what your software will and will not do.
-->
{{ cookiecutter.project_purpose }}

### System Overview
<!--
Describe the total system this piece of software is a part of and where in this system this fits in. For a lot of simple scripts this does not have to be very complicated.
-->
{{ cookiecutter.system_overview }}

## User Documentation
<!--
This user documentation contains information on how to get started with the script that is contained in the basic templates.
Extend this section with specific instructions for users of your software (e.g. what format should the input data be in? What kind of settings can be changed? ...)
-->

### Pre-requisites

To use this script you first need to install [python](https://www.python.org/) (version 3.10 or higher) and [poetry](https://python-poetry.org/). The installation guide also assumes you have [git](https://git-scm.com/) installed.

### Installation

To install this software first make a local copy of this repostitory (e.g by cloning it with `git clone`). In the root directory of your local folder run the following commands:

``` bash
poetry install
```

### Using the script

#### The input

The script expects a csv file as input. The first column of this file should be the names of the columns.

#### Settings

The script has a few settings which can be changed. These settings can be found at the top of the file `{{ cookiecutter.module_name }}/main.py`.

| Setting | Explanation | Default |
| --- |  --- | --- |
| INPUT_FILE_PATH | The script looks for the input file in this location. | './example_input.csv' |
| OUTPUT_PATH | The script creates the output file in this location. | './output.csv' |
| COLUMN_NAME | The name of the column on the filtering should happen. | 'column_1' |
| THRESHOLD | Rows with a value higher than this threshold in the column with the name `COLUMN_NAME` will be removed. | 5 |

#### Running the script

By running the `poetry install` command poetry created a [virtual environment](https://docs.python.org/3/library/venv.html). To run the script you need to use this virtual environment. It can be activated by running:

```bash
poetry shell
```

Now all the commands you run will be running in an environment with the correct versions of packages installed. At the same time your normal python installation will remain unaffected. If you want to exit this enviroment you can use the `deactivate` command.

To now run the script run the following command:

```bash
python -m {{ cookiecutter.module_name }}.main
```

### The output

The output is a new csv file with the rows filtered out. g.The file can be found in the location defined by the `OUTPUT_PATH` setting.

## Developer Documentation
<!--
Provides some information for people who want to continue developing this software (or for yourself in the future if you ever return to it). It should provide the commnands a developer needs to for example test the software. Extend this section with specific instructions for developers of your software.
-->

### Running the tests

To run the tests run the following command after running `poetry shell`

```bash
pytest
```

### Checking the codestyle

To check if new code adheres to our code style you can run flake8 with the following command:

```bash
flake8 .
```

### Managing dependencies

To add a new package that is reqequired use:

```bash
poetry add <package_name>
```

To update the dependencies run:

```bash
poetry update
```

If you want other people to be able to run the script with the same updated packages (for exampel to reproduce your results) then make sure to commit the changes to your `poetry.lock` file.

## Software Development Plan

This sections describes how we will develop the software. It covers aspects like documentation, maintenance and dependency management.

### Dependencies
<!--
Describe the depedencies your project needs. Before using dependencies consider whether they are of a good enough quality for your research and whether their license allows them to be used by your.
-->
External (not owned by QuTech):

* Pandas: for easier data processing. Pandas is widely used, actively maintained and has a 3-clause BSD license allowing us to use and modify it.

#### Dependency Management
<!--
Describe how you want to manage depedencies. There are various tools available. What is important is that for the packages you import you define:
1. The names of the packages
2. The versions of the packages you have used
That way someone new (or you yourself in the future) can easily install those same packages with the correct versions. In Python tools like poetry or pip can help with this.
-->
We use Poetry to manage the depdencies for us. The poetry.lock file is committed so that it is clear which specific versions were used in a certain version of this script.

### Testing
<!--
What and how do you test it? E.g. do you have automatic unit tests, code coverage checks, tests for code style etc.
-->
We provide some simple tests to check that the processing works as expected. Additionally we use flake8 to make sure we adhere to pep8 code style standards this ensures the code remains readable. Because this code is only worked on by a single developer these checks are simply ran manually. The commands to run it can be found in the developer documentation.

### Version Control and Versioning
<!--
Describe how you will use version control and versioning. For simple scripts it can remain simple. If you want to do more complex things (e.g. proper semantic versioning for a package that you want to publish externally you can ask the SDST for advice.)

-->
We will use git as a version control system. Because the project is being worked on by a single developer we keep the flow simple. Once changes are ready they are committed to the main branch. If we want to refer to a specific version of the software (e.g. a specific version used in a certain analysis) then we refer to the specific commit that was used.

### Describe project resources
<!--
If you need resources to execute the project describe them here, together with who you need to align this or from who you need approval for this (this can be relevant for example when you are running an experiment on hardware)
-->
For this simple data processing script only a personal laptop is needed.

### Safety, Securiy, Privacy Assurance
<!--
If it could be an issue describe safety, security and privacy considerations.
-->
This software does not process any personal data and does not send any data to 3rd parties we therefore do not foresee safety, security or privacy issues.

### Software licensing
<!--
What licensing will your software use? For private projects this is not very relevant. Without a license they will be considered property of QuTech. For public repositories this is very important to consider. If you make your software public the license will determine who and how the software can be used. This also has implications for intellectual property (copyright).
-->
It is an internal QuTech repository. The software will therefore remain proprietary.

### Third party tools
<!--
If applicable, describe third party tools you need during the development. The place where you store your code is a logical one for example. But you might also make use of tools to document your code, track issues, ...
-->
**Add any third party tools you used here** (see comments for more info)
