source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
API_URL=https://honguiniproductions.com:8000 reflex export --frontend-only
rm -rf public
unzip frontend.zip -d public
rm -rf frontend.zip 
deactivate