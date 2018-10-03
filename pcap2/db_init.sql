--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.4
-- Dumped by pg_dump version 9.5.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: query; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE IF NOT EXISTS query (
    id integer NOT NULL,
    query_key character varying(100),
    start timestamp without time zone,
    finish timestamp without time zone,
    queued_time timestamp without time zone,
    complete_time timestamp without time zone,
    callid character varying(100),
    status integer,
    msg character varying(100),
    switch_ip character varying(15),
    private_url character varying(255),
    public_url character varying(255),
    CONSTRAINT query_pkey PRIMARY KEY (id)
);


--
-- Name: query_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE IF NOT EXISTS query_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: query_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE query_id_seq OWNED BY query.id;


--
-- Name: query_cdr; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE IF NOT EXISTS query_cdr (
    id integer DEFAULT nextval('query_id_seq'::regclass) NOT NULL,
    query_key character varying(100),
    start timestamp without time zone,
    finish timestamp without time zone,
    queued_time timestamp without time zone,
    complete_time timestamp without time zone,
    search_filter character varying(1024),
    status integer,
    msg character varying(100),
    switch_ip character varying(15),
    url character varying(255),
    result_filter character varying(1024),
    email_to character varying(128),
    ftp_to character varying(256),
    cdrmail_subj character varying(64),
    cdrmail_body text,
    parent_querykey character varying(100),
    group_count integer,
    CONSTRAINT query_cdr_pkey PRIMARY KEY (id)
);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY query ALTER COLUMN id SET DEFAULT nextval('query_id_seq'::regclass);

--
-- Name: ix_query_status; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX IF NOT EXISTS ix_query_status ON query USING btree (status);


--
-- Name: query_cdr_status_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX IF NOT EXISTS query_cdr_status_idx ON query_cdr USING btree (status);


--
-- PostgreSQL database dump complete
--

