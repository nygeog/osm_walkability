# OSM Walkability
Training on Open Street Map derived features for constructing a walkability index

## Resources:

https://github.com/mvexel/overpass-api-python-wrapper

http://wiki.openstreetmap.org/wiki/Points_of_interest

http://blogs.cuit.columbia.edu/socialepicluster/2017/03/06/webinar-online-urban-informatics-studying-how-urban-design-influences-health-in-new-york-city/

https://taginfo.openstreetmap.org/keys

https://github.com/mvexel/overpass-api-python-wrapper

http://wiki.openstreetmap.org/wiki/Osmconvert

## Project Requirements
Project Requirements - for easily getting started with this project using Python. 

    virtualenv env
    source env/bin/activate
    wget https://raw.githubusercontent.com/nygeog/cartoprojectsrequirements/master/requirements.txt
    wget https://raw.githubusercontent.com/nygeog/cartoprojectsrequirements/master/.gitignore
    pip install -r requirements.txt
    jupyter nbextension enable --py --sys-prefix widgetsnbextension
    open .gitignore
    touch _settings.py
    open _settings.py
    mkdir data
    mkdir data/input
    mkdir data/processing
    mkdir data/output
    python -m pip install -U pip setuptools
    pip install wheel
    pip install -U numpy scipy scikit-learn
    pip install overpass
