
# Start with basic ubuntu image
FROM ubuntu:14.04

MAINTAINER Alex Goodell <alexgoodell@gmail.com>

# Install basics
RUN apt-get -y update
RUN apt-get install -y git make wget curl bison vim

# Graphviz dependencies
RUN apt-get -y install graphviz libgraphviz-dev

# Install python dependencies
RUN apt-get -y install build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

# sci py dependencies
RUN apt-get -y install libblas-dev liblapack-dev libatlas-base-dev gfortran

# Download python source
RUN mkdir ~/Downloads/ && cd ~/Downloads/ && wget http://python.org/ftp/python/2.7.10/Python-2.7.10.tgz

# Extract and install python
RUN cd ~/Downloads/ && tar -xvf Python-2.7.10.tgz && cd ~/Downloads/Python-2.7.10 && ./configure && cd ~/Downloads/Python-2.7.10 && make && cd ~/Downloads/Python-2.7.10 && make install

# Get pip (python package manager)
RUN cd ~/Downloads && wget https://bootstrap.pypa.io/get-pip.py && cd ~/Downloads && python get-pip.py
RUN pip install --upgrade pip

# Mapping dependencies
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:ubuntugis/ppa && apt-get update && apt-get install -y gdal-bin 

# Jupyter dependencies
RUN apt-get install -y emacs inkscape jed libsm6 libxext-dev libxrender1 lmodern netcat pandoc python-dev texlive-fonts-extra texlive-fonts-recommended texlive-generic-recommended texlive-latex-base texlive-latex-extra texlive-xetex unzip

# Clean packages up
RUN apt-get -y autoremove && apt-get -y clean && rm -rf /var/lib/apt/lists/*

# Install dependencies (these can be run all at once but was easier to break them up)
# General
RUN pip install future==0.16.0 termcolor==1.1.0
# Web
RUN pip install Jinja2==2.10
##  Mapping
# Basemap
RUN pip install Shapely==1.6.4.post1 Fiona==1.7.11.post1 descartes==1.1.0
RUN apt-get update && apt-get install -y libgeos-dev libgeos++-dev libgeos-3.4.2
RUN pip install https://github.com/matplotlib/basemap/archive/v1.0.7rel.tar.gz#egg=basemap
RUN pip install pyproj==1.9.5.1 lxml==4.2.0 pyshp==1.2.12 PySAL==1.14.3
# Ipython and Jupyer
RUN pip install jupyter==1.0.0 jupyter-client==5.2.3 jupyter-console==5.2.0 jupyter-contrib-core==0.3.3 jupyter-contrib-nbextensions==0.4.0 jupyter-core==4.4.0 jupyter-highlight-selected-word==0.1.0 jupyter-latex-envs==1.4.4 jupyter-nbextensions-configurator==0.4.0 ipykernel==4.8.2 ipython==5.5.0 ipython-genutils==0.2.0 ipywidgets==7.1.2 qtconsole==4.3.1 nbconvert==5.3.1 nbformat==4.4.0 notebook==5.4.0 appnope==0.1.0 backports-abc==0.5 backports.shutil-get-terminal-size==1.0.0 bleach==2.1.3 configparser==3.5.0 decorator==4.2.1 entrypoints==0.2.3 functools32==3.2.3.post2 futures==3.2.0 html5lib==1.0.1 jsonschema==2.6.0 MarkupSafe==1.0 mistune==0.8.3 pathlib2==2.3.0 pexpect==4.4.0 pickleshare==0.7.4 prompt-toolkit==1.0.15 ptyprocess==0.5.2 Pygments==2.2.0 python-dateutil==2.7.0 pyzmq==17.0.0 scandir==1.7 Send2Trash==1.5.0 simplegeneric==0.8.1 singledispatch==3.4.0.3 terminado==0.8.1 testpath==0.3.1 tornado==5.0.1 traitlets==4.3.2 wcwidth==0.1.7 webencodings==0.5.1 widgetsnbextension==3.1.4 funcparserlib==0.3.6 jupyter-pip==0.3.1
# Numeric analysis
RUN pip install numpy==1.14.2 pandas==0.22.0 pytz==2018.3 scipy==1.0.0 xlrd==1.1.0 xlwt==1.3.0
# Text analysis
RUN pip install beautifulsoup4==4.6.0 python-Levenshtein==0.12.0 fuzzywuzzy==0.16.0 bs4==0.0.1
# Document management
RUN pip install num2words==0.5.6 pandocfilters==1.4.2 PyYAML==3.12 bibtexparser==1.0.1 titlecase==0.12.0 tabulate==0.8.2
# Graphing and deps - terminalplot 0.2.6
RUN pip install seaborn==0.8.1 matplotlib==2.2.2 backports.functools-lru-cache==1.5 cycler==0.10.0 kiwisolver==1.0.1 pyparsing==2.2.0 subprocess32==3.2.7
# Fabric
RUN pip install asn1crypto==0.24.0 bcrypt==3.1.4 cffi==1.11.5 cryptography==2.2.1 enum34==1.1.6 Fabric3==1.14.post1 idna==2.6 ipaddress==1.0.19 paramiko==2.4.1 pyasn1==0.4.2 pycparser==2.18 PyNaCl==1.2.1 six==1.11.0 prompter==0.3.10
# REPL - ptpython
RUN pip install click==6.7 click-plugins==1.0.3 cligj==0.4.0 docopt==0.6.2 jedi==0.11.1 munch==2.2.0 parso==0.1.1 ptpython==0.41
# ArchiveNow
RUN pip install archivenow==2017.11.21.10.50.27 certifi==2018.1.18 chardet==3.0.4 Flask==0.12.2 itsdangerous==0.24 requests==2.18.4 urllib3==1.22 Werkzeug==0.14.1
# Block diag
RUN pip install blockdiag==1.5.3
# unknown
RUN pip install Pillow==5.0.0 ruamel.ordereddict==0.4.13 webcolors==1.8.1

ENV NB_USER ubuntubaby
ENV NB_UID 1000
ENV HOME /home/${NB_USER}

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

# RUN cd /home && git clone  --depth  1  https://github.com/alexgoodell/uganda-model.git .

# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

CMD ["jupyter", "notebook", "--ip", "0.0.0.0"]
