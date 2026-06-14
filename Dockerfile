FROM python:3.11-slim-bookworm

# Install dependencies sistem
RUN apt-get update && apt-get install -y \
    python3-dev \
    libxml2-dev \
    libxslt1-dev \
    libldap2-dev \
    libsasl2-dev \
    libtiff5-dev \
    libjpeg62-turbo-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libxcb1-dev \
    libpq-dev \
    gcc \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Buat direktori kerja
WORKDIR /opt/odoo

# Copy requirements dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh source code Odoo dan custom_addons
COPY . .

# Buat user odoo agar aman
RUN useradd -m -d /opt/odoo -s /bin/bash odoo \
    && chown -R odoo:odoo /opt/odoo

# Buat folder untuk filestore (biar gambar gak ilang)
RUN mkdir -p /var/lib/odoo && chown -R odoo:odoo /var/lib/odoo
VOLUME ["/var/lib/odoo"]

USER odoo

# Port Odoo
EXPOSE 8069

# Command untuk menjalankan Odoo
CMD ["sh", "-c", "python3 odoo-bin --addons-path=addons,custom_addons -d ${DB_NAME:-odoo_polban_19} --db_host=${DB_HOST} --db_user=${DB_USER} --db_password=${DB_PASSWORD} --db_port=${DB_PORT:-5432}"]
