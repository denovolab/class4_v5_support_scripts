-- pg_dump  -C -F p -b -v  -t storage_config -f storage_config_dump.sql class4_pr -U postgres
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.7
-- Dumped by pg_dump version 9.6.3

-- Started on 2017-09-06 17:45:52 GMT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;


DROP TABLE IF EXISTS storage_config CASCADE;
DROP TYPE IF EXISTS parser_type;
DROP TYPE IF EXISTS storage_type;

CREATE TYPE parser_type AS ENUM ('cdr', 'pcap');
CREATE TYPE storage_type AS ENUM ('local', 'ftp', 'sftp', 'gcs');


CREATE TABLE storage_config (
    storage storage_type NOT NULL,
    conf_type parser_type NOT NULL,
    remote_server_port integer,
    ftp_port integer,
    storage_days integer DEFAULT 60,
    storage_days_local integer DEFAULT 60,
    remote_server_ip text,
    storage_path text,
    username text,
    password text,
    ftp_ip text,
    google_drive_key text,
    google_drive_name text
);


ALTER TABLE storage_config OWNER TO postgres;
