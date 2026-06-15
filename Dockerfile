FROM python:3.11-slim-bookworm

# Install dependencies sistem (ditambah libpng dan zlib untuk gambar)
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
    libpng-dev \
    zlib1g-dev \
    postgresql-client \
    gcc \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Buat direktori kerja
WORKDIR /opt/odoo

# Copy requirements dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh source code dan file data
COPY . .

# Buat user odoo agar aman
RUN useradd -m -d /opt/odoo -s /bin/bash odoo \
    && chown -R odoo:odoo /opt/odoo

# Buat folder untuk filestore (Mounted ke Render Disk)
RUN mkdir -p /var/lib/odoo && chown -R odoo:odoo /var/lib/odoo
VOLUME ["/var/lib/odoo"]

USER odoo

# Port Odoo
EXPOSE 8069

# Gunakan script entrypoint
ENTRYPOINT ["/opt/odoo/entrypoint.sh"]
