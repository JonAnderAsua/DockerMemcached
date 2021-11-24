# Imagen base
FROM ubuntu 

RUN apt -qq update 

#Crear enviroment
RUN apt install python3-pip -y
#RUN python -m venv /venv
#ENV PATH=/venv/bin:$PATH

RUN apt install -y \
	libmemcached11 \
	libmemcached12 \
	libmemcached-dev \
	libz-dev

#Copiar ficheros
#COPY main.py app/main.py
COPY cosasParaInstalar.txt app/cosasParaInstalar.txt 

#Elegir workdir
WORKDIR /app

#Instalar dependencias
RUN pip install --upgrade pip 
RUN python3 -m pip install --default-timeout=100 -r cosasParaInstalar.txt



CMD ["/usr/bin/python3", "-m","main.py"]
#CMD ["/bin/bash"]
