FROM alpine:3.7

RUN apk add --no-cache bash &&\
	apk update &&\
	apk upgrade

ENV PATH /usr/local/bin:$PATH

RUN apk add --no-cache make &&\
	apk add --no-cache python3-dev &&\
	apk add --no-cache python3 &&\
	apk add --no-cache firefox-esr &&\
	apk add --no-cache wget &&\
	apk add --no-cache git &&\
	apk add --no-cache icu-libs &&\
	apk add --no-cache xvfb &&\
	apk add --no-cache linux-headers &&\
	apk add --no-cache texinfo &&\
	apk add --no-cache gcc &&\
	apk add --no-cache g++ &&\
	apk add --no-cache gfortran &&\
	apk add --no-cache libxml2-dev &&\
	apk add --no-cache xmlsec-dev &&\
	apk add --no-cache py-requests &&\
	apk add --no-cache qt-dev &&\
	apk add --no-cache openjdk7-jre &&\
	apk add --no-cache dbus-x11 &&\
	apk add --no-cache ttf-freefont &&\
	rm -rf /var/cache/apk/*

#python
RUN python3 -m ensurepip &&\
	rm -r /usr/lib/python*/ensurepip &&\
	pip3 install --upgrade pip setuptools &&\
	if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi &&\
	if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi &&\
	rm -r /root/.cache

#firefox
RUN rm  -rf /tmp/* /var/cache/apk/* &&\
	wget "https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz" &&\
	tar -xvf geckodriver-v0.19.1-linux64.tar.gz &&\
	rm -rf geckodriver-v0.19.1-linux64.tar.gz &&\
	chmod a+x geckodriver &&\
	mv geckodriver /usr/local/bin/

#selenium
RUN pip install "selenium<3" &&\
	pip install virtualenv &&\
	pip install pyvirtualdisplay

#X server
RUN git clone "https://github.com/niklasb/webkit-server.git" &&\
	cd webkit-server &&\
	python setup.py install
ADD start_script.sh /tmp/start_script.sh
RUN chmod +x /tmp/start_script.sh

#mysql
RUN apk add --no-cache mariadb-dev
RUN pip install mysqlclient

# prepare le shell
RUN mkdir /var/shared
WORKDIR "/var/shared"
CMD ["/tmp/start_script.sh"]
