#!/bin/bash
set -e

# Tunggu sampai DB siap
echo "Waiting for PostgreSQL to be ready..."
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  sleep 2
done

# Cek apakah database sudah ada isinya
DB_EXISTS=$(PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -tAc "SELECT 1 FROM information_schema.tables WHERE table_name = 'res_company' LIMIT 1;")

if [ "$DB_EXISTS" != "1" ]; then
  echo "Database is empty. Importing migration backup..."
  PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" < /opt/odoo/data/cloud_migration_backup.sql
  echo "Import complete!"
else
  echo "Database already has data. Skipping import."
fi

# Jalankan Odoo normal
exec python3 odoo-bin --addons-path=addons,custom_addons -d "$DB_NAME" --db_host="$DB_HOST" --db_user="$DB_USER" --db_password="$DB_PASSWORD" --db_port="$DB_PORT"
