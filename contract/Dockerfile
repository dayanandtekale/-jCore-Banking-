FROM python:3.7
RUN apt-get update
RUN apt-get install -y \
    sudo libexpat1 apache2 apache2-utils    ssl-cert w3m w3m-img nano
RUN apt-get install -y apache2-dev python3-dev libapache2-mod-wsgi-py3 python3-pip

RUN python3 -m pip install flask 
RUN python3 -m pip install flask-api 
RUN python3 -m pip install flask-cors 
RUN python3 -m pip install opencv-python 
RUN python3 -m pip install pillow 
RUN python3 -m pip install pymongo
RUN python3 -m pip install pandas
RUN python3 -m pip install requests
RUN python3 -m pip install numpy==1.15.4

RUN apt-get install -y libgl1-mesa-dev
RUN python3 -m pip install jwt flask_jwt_extended


ENV dir /home/mydir/contract
WORKDIR $dir

COPY __init__.py $dir/

COPY contract/. $dir/contract/
COPY contract.conf /etc/apache2/conf-available/

RUN chown -R www-data:www-data /home/mydir/contract/contract/
RUN a2enconf contract

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

