FROM centos:latest

LABEL Component="Netscan tooling image" \
      Name="baburajk/devops" 

#Import keys
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7
RUN rpm --import https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7
RUN rpm --import https://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7Server

RUN yum -y update \
    && yum -y install epel-release  \
    && yum install -y https://centos7.iuscommunity.org/ius-release.rpm \
    && yum install -y python35u python35u-libs python35u-devel python35u-pip python35u-setuptools python35-pip \
    && yum install -y git g++ gcc traceroute libssl-devel libffi-devel gcc-c++

#Install ansible and nginx
RUN yum -y install nginx \
    && yum -y install ansible 

RUN yum -y install wget curl netcat nmap ipv6-toolkit dstat hping3 bind-utils mtr dstat tcpdump
RUN yum -y install whois

# Python must be pointing to python3.x
#RUN rm /usr/bin/python
#RUN ln -s /usr/bin/python3.5 /usr/bin/python

#Install pip
RUN wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \
    python3.5 get-pip.py ; pip --version

#ENV PYTHON_PIP_VERSION 18.1
#RUN set -ex; wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \
	#python get-pip.py  --disable-pip-version-check --no-cache-dir "pip==$PYTHON_PIP_VERSION" ; \
	#pip --version; 

COPY ./config/requirements.txt /base/tools/
#ADD https://www.caida.org/tools/measurement/scamper/code/scamper-cvs-20180504.tar.gz /base/tools
#RUN cd /base/tools; tar -xvzf scamper-cvs-20180504.tar.gz; cd scamper-cvs-20180504  ; ./configure ; make ; make install

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r /base/tools/requirements.txt

RUN git clone https://github.com/gnomikos/traIXroute.git && \
    cd traIXroute

WORKDIR /traIXroute
RUN pip install -r setup/requirements.txt &&\
    python setup.py sdist 
      #python lib/traixroute/downloader/install_scamper.py install_scamper.py &&\
        #python setup.py sdist bdist_wheel

RUN wget -O scamper.tar.gz https://www.caida.org/tools/measurement/scamper/code/scamper-cvs-20180504.tar.gz
RUN tar -xvzf scamper.tar.gz 
RUN cd scamper-cvs-20180504/ ; ./configure ; make ; make install


#WORKDIR bin/
#ENTRYPOINT ["./traixroute"]
#CMD ["-h"]


