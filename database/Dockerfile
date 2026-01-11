FROM pgvector/pgvector:pg16

ARG PG_MAJOR=16

COPY ./polish-tsearch/polish.affix /usr/share/postgresql/${PG_MAJOR}/tsearch_data/polish.affix
COPY ./polish-tsearch/polish.dict /usr/share/postgresql/${PG_MAJOR}/tsearch_data/polish.dict
COPY ./polish-tsearch/polish.stop /usr/share/postgresql/${PG_MAJOR}/tsearch_data/polish.stop