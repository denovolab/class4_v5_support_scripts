CREATE TABLE config_gcs (
    type varchar PRIMARY KEY NOT NULL,
    enable boolean,
    project_id text,
    private_key_id text,
    private_key text,
    client_email text,
    client_id text,
    auth_uri text,
    token_uri text,
    auth_provider_x509_cert_url text,
    client_x509_cert_url text
);

CREATE TABLE config_ftp (
    type varchar PRIMARY KEY NOT NULL,
    enable boolean,
    user text,
    pass text,
    host text,
    port integer
);

CREATE TABLE config_local (
    type varchar PRIMARY KEY NOT NULL,
    enable boolean,
    dir text
);

