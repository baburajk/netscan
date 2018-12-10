FROM centos:latest

LABEL Component="RECON"

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
RUN yum -y install nginx  
RUN yum -y install ansible 
RUN yum -y install wget curl ipv6-toolkit dstat hping3 bind-utils mtr dstat tcpdump
RUN yum -y install whois

RUN yum -y install wget
RUN rpm -vhU https://nmap.org/dist/nmap-7.70-1.x86_64.rpm
RUN rpm -vhU https://nmap.org/dist/ncat-7.70-1.x86_64.rpm
RUN nmap --script-updatedb

# Python must be pointing to python3.x
#RUN rm /usr/bin/python
#RUN ln -s /usr/bin/python3.5 /usr/bin/python

#Install pip
RUN wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \
    python3.5 get-pip.py ; pip --version

COPY ./config/requirements.txt /base/tools/

RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r /base/tools/requirements.txt

RUN wget -O scamper.tar.gz https://www.caida.org/tools/measurement/scamper/code/scamper-cvs-20180504.tar.gz
RUN tar -xvzf scamper.tar.gz 
RUN cd scamper-cvs-20180504/ ; ./configure ; make ; make install


#Disable traIXroute temporarily
#RUN git clone https://github.com/gnomikos/traIXroute.git && \
   # cd traIXroute

#WORKDIR /traIXroute
#RUN pip install -r setup/requirements.txt &&\
    #python setup.py sdist 

      #python lib/traixroute/downloader/install_scamper.py install_scamper.py &&\
        #python setup.py sdist bdist_wheel


#WORKDIR bin/
#ENTRYPOINT ["nmap"]
#CMD ["-h"]


