FROM elgalu/selenium



RUN apt -qqy --no-install-recommends install \
        python\
        pip\
    && apt -qqy clean

ADD ./maincode /opt/maincode
WORKDIR /opt/maincode
RUN pip install -r requirements.txt
EXPOSE 8080

ENTRYPOINT  ["./entry.sh"]