FROM docker-selenium



RUN apt -qqy --no-install-recommends install \
        python\
        pip\
    && apt -qqy clean

RUN pip install -r requirements.txt



EXPOSE 8080

ENTRYPOINT  ["entry.sh"]