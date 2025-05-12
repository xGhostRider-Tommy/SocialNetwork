# Welcome to SocialNetwork!

Ciao! Questo e' un progetto per scuola. Abbiamo deciso di ricreare un Social Network semplificato con interfaccia web. Il back-end e' scritto in **Python** utilizzando **Flask** mentre il front-end e' scritto in **HTML** e **JavaScript**.


# Run

## Requirements
- Almeno **Python 3.9** o successivi
- Tutte le **librerie** in `requirements.txt`

**NOTE**: If you are using Windows, you need to have the Python installation installed to "All Users" as I didn't add the proper batch script to run the flask. You and still create yours and run it.
Just make shure that this command is runned before running Flask at ANY new cmd instance:
`set FLASK_APP=app\Main.py`

## Running
### MacOS
- **Run** `run.sh`
- **Go to** http://127.0.0.1:5000 or another link in base of your Flask settings

### Windows
- **Run** `run.bat`
- **Go to** http://127.0.0.1:5000 or another link in base of your Flask settings

## Reset data
### With Script
- **Run** `ClearData.py` using **Python**

### Manually
- **Delete** or **clear** the `static/images` folder
- **Delete** `Data` folder or **clear** the content of `Data/posts.csv` and `Data/users.csv`
