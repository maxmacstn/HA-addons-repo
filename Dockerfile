ARG BUILD_FROM
FROM $BUILD_FROM

RUN apk update && apk add --no-cache lighttpd ffmpeg python3
RUN sed -i -r 's#\#.*mod_alias.*,.*#    "mod_alias",#g' /etc/lighttpd/lighttpd.conf
RUN sed -i -r 's#.*include "mod_cgi.conf".*#   include "mod_cgi.conf"#g' /etc/lighttpd/lighttpd.conf
RUN mkdir -p /var/lib/lighttpd
RUN chown -R lighttpd:lighttpd /var/www/localhost/
RUN chown -R lighttpd:lighttpd /var/lib/lighttpd
RUN chown -R lighttpd:lighttpd /var/log/lighttpd

COPY mod_cgi.conf /etc/lighttpd/mod_cgi.conf
COPY /scripts/samplestream.cgi /var/www/localhost/cgi-bin/
COPY start.sh /
COPY scripts /scripts
RUN chmod a+x /start.sh

CMD [ "/start.sh" ]
