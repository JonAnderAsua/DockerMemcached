# Imagen base
FROM ubuntu 

#Actualizar ubuntu
RUN apt -qq update 

#Crear enviroment
RUN apt install python3-pip -y

#Copiar ficheros
COPY main.py app/main.py
COPY cosasParaInstalar.txt app/cosasParaInstalar.txt 

#Elegir workdir
WORKDIR /app

#Actualizar pip
RUN pip install --upgrade pip

#Instalar las dependencias 
RUN python3 -m pip install --default-timeout=100 -r cosasParaInstalar.txt

#Runear la app
CMD ["/usr/bin/python3", "-m","main.py"]
