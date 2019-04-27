FROM elgalu/selenium

USER root

RUN apt -qqy --no-install-recommends install \
        python\
        pip\
    && apt -qqy clean

ADD ./maincode /opt/maincode
WORKDIR /opt/maincode
RUN pip install -r requirements.txt
EXPOSE 8080

USER seluser

ENTRYPOINT  ["./entry.sh"]