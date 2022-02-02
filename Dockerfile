ARG BUILD_FROM
FROM $BUILD_FROM

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y lighttpd ffmpeg
RUN cd /etc/lighttpd/conf-enabled && ln -s ../conf-available/cgi.conf
VOLUME /var/www/cgi-bin
COPY cgi.conf /etc/lighttpd/conf-available/cgi.conf
COPY start.sh /

CMD ["/start.sh"]
