FROM elgalu/selenium

USER root
ADD ./maincode /opt/maincode
RUN chmod -R 777 /opt/maincode
WORKDIR /opt/maincode
RUN pip install -r requirements.txt
EXPOSE 8080

USER seluser

ENTRYPOINT  ["python","main.py"]