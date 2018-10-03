CREATE TABLE "config_gcs" (
    "type" varchar(20) NOT NULL,
    "enable" BOOLEAN NOT NULL,
    "project_id" TEXT NOT NULL,
    "private_key_id" TEXT NOT NULL,
    "private_key" TEXT NOT NULL,
    "client_email" TEXT NOT NULL,
    "client_id" TEXT NOT NULL,
    "auth_uri" TEXT NOT NULL,
    "token_uri" TEXT NOT NULL,
    "auth_provider_x509_cert_url" TEXT NOT NULL,
    "client_x509_cert_url" TEXT NOT NULL,
    CONSTRAINT config_gcs_pk PRIMARY KEY ("type")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "config_ftp" (
    "type" varchar(20) NOT NULL,
    "enable" BOOLEAN NOT NULL,
    "user" TEXT NOT NULL,
    "pass" TEXT NOT NULL,
    "host" TEXT NOT NULL,
    "port" integer NOT NULL,
    CONSTRAINT config_ftp_pk PRIMARY KEY ("type")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "config_local" (
    "type" varchar(20) NOT NULL,
    "enable" BOOLEAN NOT NULL,
    "dir" TEXT NOT NULL,
    CONSTRAINT config_local_pk PRIMARY KEY ("type")
) WITH (
  OIDS=FALSE
);






