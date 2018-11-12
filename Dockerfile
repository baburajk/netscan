FROM centos:latest

LABEL Component="network + security tooling" \
      Name="baburajk/netscan"

RUN yum -y update \
    && yum -y install epel-release  \
    && yum install -y https://centos7.iuscommunity.org/ius-release.rpm \
    && yum install -y python36u python36u-libs python36u-devel python36u-pip 

# pipenv installation
RUN pip3.6 install pipenv
RUN ln -s /usr/bin/pip3.6 /bin/pip
RUN rm /usr/bin/python
# python must be pointing to python3.6
RUN ln -s /usr/bin/python3.6 /usr/bin/python

RUN pip install --upgrade pip

#COPY ARTIFACTS
WORKDIR  /base/tools
COPY ./requirements.txt /base/tools

#Copy ansible files
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#ENTRYPOINT [ "/bin/bash" ]
#CMD ["ls -l"]

