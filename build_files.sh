# build_files.sh
echo "Building the project..."
python3.9 -m pip install -r requirements.txt --break-system-packages
python3.9 manage.py collectstatic --noinput --clear
echo "Build complete."
