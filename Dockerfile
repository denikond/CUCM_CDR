FROM ubuntu:20.04
RUN apt-get update
RUN apt-get upgrade
RUN apt-get install -y curl
RUN apt-get install -y gnupg2
#RUN apt-get install -y wget
#RUN wget -O- https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN # optional: for bcp and sqlcmd
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrci
SHELL ["/bin/bash", "-c"]
RUN source ~/.bashrc
RUN # optional: for unixODBC development headers
RUN apt-get install -y unixodbc-dev
