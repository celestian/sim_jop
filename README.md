# sim_jop

The Game of Railway Traffic Control


## About

The goal of sim_jop project is create open source game of railway traffic control.
If you want to be in touch with the community, please connect to [discord](https://discord.gg/drcmjBf).


## Development & Contributions

### Setup development environment on Linux

    # packages needed on Fedora 29
    sudo dnf install -y python3-pip

    # clone the repository
    git clone git@github.com:celestian/sim_jop.git

    # setup commit template
    git config commit.template .git-commit-template

    # git configuration
    git config user.name "your_name"
    git config user.email "your_email"

    # (optionally)
    git config user.signingkey your_gpg_key

    # create virtual environment
    python3 -m venv env

    # install requirements
    ./install.sh

### Activate development environment

    source env/bin/activate

### Build package & release

    pip3 install --upgrade setuptools wheel twine
    python3 setup.py sdist bdist_wheel
    python3 -m twine upload dist/*


## Resources

### JOP, DOZ
- [ztp-jop](http://spz.logout.cz/zabezpec/ztp-jop.html)
- [mapa CDP]( https://provoz.szdc.cz/PORTAL/Show.aspx?path=/Data/Mapy/DOZ.pdf)
- [plánky](http://www.gvd.cz/cz/data/planky/planky.html)
- [GVD](http://gvd.cz/czx/)
- [Brodek u Přerova](http://www.gvd.cz/cz/data/planky/3xx/309/331421.xls)

### Software engineering
- [regular expression](https://regexr.com/)
- [yaml](https://pyyaml.org/wiki/PyYAMLDocumentation)
- [pyglet](https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/)
