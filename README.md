# Welcome to SocialNetwork!

Hi! This is a school project. We have decided to re-create a simplified version of a **SocialNetwork** with a **Web interface**.
**Back-End** written in **Python** using **Flask**.
**Front-End** written in **HTML** and **JavaScript**.


# Run

## Requirements
- **Python 3.9<=**
- All **libraries** in `requirements.txt`

**NOTE**: If you are using Windows, you need to have the Python installation installed to "All Users" as I didn't add the proper batch script to run Flask. You can still create yours and run it.
Just make sure that this command is run before running Flask at ANY new cmd instance:
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
