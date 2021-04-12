#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    create user symphony with encrypted password 'carambolasAzuis784';
    create database symphony owner symphony;
    GRANT ALL PRIVILEGES ON DATABASE symphony TO symphony;
EOSQL