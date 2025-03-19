@echo off
pip install -r requirements.txt
set FLASK_APP=app\Main.py
"C:\Program Files\Python\Scripts\flask.exe" run