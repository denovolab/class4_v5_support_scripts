BEGIN;
CREATE TABLE IF NOT EXISTS query_cdr (
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    query_key TEXT,
    start timestamp without time zone,
    finish timestamp without time zone,
    queued_time timestamp without time zone,
    complete_time timestamp without time zone,
    search_filter TEXT,
    status integer,
    msg TEXT,
    switch_ip TEXT,
    url TEXT,
    result_filter TEXT,
    email_to TEXT,
    ftp_to TEXT,
    cdrmail_subj TEXT,
    cdrmail_body text,
    parent_querykey TEXT,
    group_count integer
);

--
-- Name: query_cdr_status_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX IF NOT EXISTS query_cdr_status_idx ON query_cdr(status);

END;
