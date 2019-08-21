FROM python:3.7-stretch

ARG DIR_PATH=/home/app

COPY entrypoint.sh /usr/local/sbin/entrypoint.sh
COPY . ${DIR_PATH}

WORKDIR ${DIR_PATH}

RUN pip install -e quotes/ \
 && pip install -e .

ENTRYPOINT ["entrypoint.sh"]