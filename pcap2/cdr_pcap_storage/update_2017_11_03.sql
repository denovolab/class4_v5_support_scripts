ALTER TABLE storage_config ALTER COLUMN remote_server_port DROP NOT NULL;
ALTER TABLE storage_config ALTER COLUMN ftp_port DROP NOT NULL;
ALTER TABLE storage_config ALTER COLUMN remote_server_ip DROP NOT NULL;
ALTER TABLE storage_config ALTER COLUMN storage_path DROP NOT NULL;
ALTER TABLE storage_config ALTER COLUMN username DROP NOT NULL;
ALTER TABLE storage_config ALTER COLUMN password DROP NOT NULL;
ALTER TABLE storage_config ALTER COLUMN ftp_ip DROP NOT NULL;
ALTER TABLE storage_config ALTER COLUMN google_drive_key DROP NOT NULL;
ALTER TABLE storage_config ALTER COLUMN google_drive_name DROP NOT NULL;