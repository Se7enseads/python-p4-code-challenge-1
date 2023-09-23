# Flask code challenge

This application provides a RESTful API for the management of restaurants and their associated pizzas.
It includes the following features:

    - Listing all restaurants
    - Retrieving restaurant details by ID
    - Deleting restaurants
    - Listing all pizzas
    - Creating restaurant-pizza entries

The application is backed by a SQLite database and uses SQLAlchemy for data modeling and interaction.

## Table of Contents

- [Pre-requisites](#🚀-pre-requisites)
- [Usage](#usage)
- [License](#📝-license)

## 🚀 Pre-requisites

To run this program you need:

- [Code Editor/ IDE](#ide)
- [Python](#python)
- [GIT](#git)

### Python

First you need to check if you have python already installed (some OS come with python installed already) run either command:

```bash
python --version
python3 --version
```

If you don't have python installed follow this [tutorial](https://www.linuxcapable.com/how-to-install-python-3-11-on-ubuntu-linux/) for ubuntu or this for [tutorial](https://www.linuxcapable.com/how-to-install-python-3-11-on-linux-mint/) for linux mint.

### IDE

An [IDE](https://www.codecademy.com/article/what-is-an-ide) is short for Integrated Development Environment is a software helps programmers develop software code efficiently.

Popular Python IDEs include:

- [Visual Studio Code (VSCode)](https://code.visualstudio.com/) - [Installation](https://www.linuxcapable.com/install-visual-studio-code-on-ubuntu-linux/). (Recommended)
- [Pycharm Community](https://www.jetbrains.com/pycharm/) - [Installation](https://www.linuxcapable.com/how-to-install-pycharm-on-ubuntu-linux/).
- [Programiz](https://www.programiz.com/python-programming) - Online IDE.

### GIT

Before proceeding, make sure to [download](https://github.com/Se7enseads/python-p4-code-challenge-1/archive/refs/heads/main.zip) or to `clone` the project files onto your machine in order to run the project.

To `clone` this repo ensure you have [Git](https://git-scm.com/) installed onto your local machine.

To check if git is already installed, run this command in your terminal:

```bash
git --version
```

To install Git run this command in the `Terminal`

```bash
sudo apt install git
```

### Clone using https

```bash
git clone https://github.com/Se7enseads/python-p4-code-challenge-1
```

### Clone using SSH

To use [SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) you first need to [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo onto your github account.

To fork this repo click the drop down button or arrow next to the name `fork` and then click on `create a new fork` or click this [link](https://github.com/Se7enseads/python-p4-code-challenge-1/fork) to direct you to the forking page.

Click on `Create Fork` to fork.

![Fork image](resources/fork.png "Fork")

![Fork page](resources/forking_page.png "Fork Page")

After forking the repo, click on the drop down arrow next to the `green code button`, select the `SSH option` and copy the code provided.

![SSH image](resources/SSH.png "SSH")

```bash
git@github.com:[Your-username]/[repo]
```

For more information about git you can checkout the git [documentation.](https://git-scm.com/docs)

## Usage

Access the code from the cloned directory and launch it using `Visual Studio Code` or `VScode`. To run this code efficiently:

1. Run these commands to install the dependencies and set up the database:

   ```python
    $ pipenv install; pipenv shell
    $ cd server
    $ flask db upgrade
    $ python seed.py
   ```

2. Then, run the server while still in `server/`:

   ```python
   $ python app.py
   ```

3. Use [Postman](https://learning.postman.com/docs/getting-started/first-steps/get-postman/) to make requests to the routes specified in the `app.py`

## 📝 License

Copyright &copy; 2023 [Kyle Mututo.](https://github.com/Se7enseads)

This project is [MIT](LICENSE) licensed.

[👆 Back to Top](#flask-code-challenge)
