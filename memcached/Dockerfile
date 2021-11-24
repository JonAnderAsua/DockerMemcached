FROM ubuntu

RUN apt update

RUN apt install -y memcached

EXPOSE 11211

#CMD ["/usr/bin/memcached -p 11211 -c 1024 -l 0.0.0.0 -u root -m 64 -I 1M"]

CMD ["memcached"]

# Establece el usuario para ejecutar el demonio Memcached
USER daemon

# Establece el punto de entrada para los binarios de Memcached
ENTRYPOINT memcached
