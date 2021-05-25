ARG BUILD_FROM
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_REF
ARG BUILD_VERSION

# Labels
LABEL \
    io.hass.name="ruuvitag-discovery" \
    io.hass.description="home assistant ruuvitag discovery add-on" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="Balda" \
    org.label-schema.description="Home Assistant RuuviTag discovery add-on" \
    org.label-schema.build-date=${BUILD_DATE} \
    org.label-schema.name="ruuvitag-discovery" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="https://github.com/balda/ruuvitag-discovery" \
    org.label-schema.usage="https://github.com/balda/ruuvitag-discovery/README.md" \
    org.label-schema.vcs-ref=${BUILD_REF} \
    org.label-schema.vcs-url="https://github.com/balda/ruuvitag-discovery" \
    org.label-schema.vendor="Community Hass.io Addons"

# Copy data for add-on
COPY run.sh /
COPY main.py /
COPY token.txt /
COPY requirements.txt /
COPY ipconfig.txt /
# Install requirements for add-on
#RUN apk add --no-cache python3



RUN apk add --no-cache \
    	jq \
        py-pip \
	python \
	python-dev \
	python3 \
	python3-dev\
 && pip install -U pip \
 && pip3 install -U pip \
 && pip install -U virtualenv


# Python 3 HTTP Server serves the current working dir
# So let's set it to our add-on persistent data directory.
WORKDIR /data

RUN chmod a+x /run.sh
RUN chmod a+x /main.py
RUN chmod a+x /token.txt
RUN chmod a+x /requirements.txt
RUN chmod a+x /ipconfig.txt

CMD [ "/run.sh" ]
