import os

settings_path = r'H:\files\quiz_app\quiz_project\settings.py'

with open(settings_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add imports if not exist
if 'import dj_database_url' not in content:
    content = content.replace('import os', "import os\nimport dj_database_url\nimport cloudinary\nimport cloudinary.uploader\nimport cloudinary.api")

# Update ALLOWED_HOSTS
content = content.replace("ALLOWED_HOSTS = ['liquidtripler.pythonanywhere.com', '127.0.0.1', 'localhost', '*']", "ALLOWED_HOSTS = ['*']")
if "ALLOWED_HOSTS = ['*']" not in content:
    content = content.replace("ALLOWED_HOSTS = []", "ALLOWED_HOSTS = ['*']")

# Update INSTALLED_APPS to include cloudinary
if "'cloudinary_storage'" not in content:
    content = content.replace("'django.contrib.staticfiles',", "'django.contrib.staticfiles',\n    'cloudinary_storage',\n    'cloudinary',")

# Update MIDDLEWARE for whitenoise
if "'whitenoise.middleware.WhiteNoiseMiddleware'" not in content:
    content = content.replace("'django.middleware.security.SecurityMiddleware',", "'django.middleware.security.SecurityMiddleware',\n    'whitenoise.middleware.WhiteNoiseMiddleware',")

# Update DATABASES
db_config = """
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://neondb_owner:npg_cAtom0jXEY8y@ep-curly-tree-ao9i5ghm.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require',
        conn_max_age=600
    )
}
"""
import re
content = re.sub(r'DATABASES\s*=\s*\{.*?\n\}', db_config.strip(), content, flags=re.DOTALL)

# Update STATIC and MEDIA
static_media_config = """
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Cloudinary setup
CLOUDINARY_URL = os.environ.get('CLOUDINARY_URL')
if CLOUDINARY_URL:
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
"""
content = re.sub(r'STATIC_URL\s*=\s*\'/static/\'.*?MEDIA_ROOT\s*=\s*os.path.join\(BASE_DIR, \'media\'\)', static_media_config.strip(), content, flags=re.DOTALL)

with open(settings_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Settings updated successfully.")
