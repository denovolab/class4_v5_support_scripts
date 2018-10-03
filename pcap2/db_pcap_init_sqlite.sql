BEGIN;

CREATE TABLE IF NOT EXISTS query (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    query_key TEXT,
    start timestamp without time zone,
    finish timestamp without time zone,
    queued_time timestamp without time zone,
    complete_time timestamp without time zone,
    callid TEXT,
    status integer,
    msg TEXT,
    switch_ip TEXT,
    private_url TEXT,
    public_url TEXT
);

--
-- Name: ix_query_status; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX IF NOT EXISTS ix_query_status ON query(status);
END;
