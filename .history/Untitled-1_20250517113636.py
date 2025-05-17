backend/app.py
from flask import Flask
from club_empreinte_digitale_site import app as club_app

if __name__ == "__main__":
    club_app.run(debug=True)