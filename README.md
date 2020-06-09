# Referral Network

Uses account management system, with referral/invite functionality.


## About:

Each user has a unique ID, an email and password.

Each user can generate an invitation with referral link and share it via standard
mediums.

A user can see how many new users have joined via his referral link.

Each user can authenticate to their account.

In addition, everybody can have a profile page that can include few photos
and text.

Every one can see the profile page of other users but only the owner can edit.


## Technology stack
* Django Framework 3.0.7
* Bootstrap 4.5.0.
* django-cleanup 4.0.0
* Pillow==7.1.2


## Installation
* Create a virtual environment:

On macOS and Linux:
```bash
python3 -m venv venv
```
On Windows:
```bash
py -m venv venv
```

* Switch your virtal environment in the terminal:

On macOS and Linux:
```bash
source venv/bin/activate
```
On Windows:
```bash
venv\Scripts\activate
```

* Then install all packages you need.

All requirements are stored in requirements.txt.
Use the package manager [pip](https://pip.pypa.io/en/stable/) 
to install by command:

```bash
pip install -r requirements.txt
```

* Now you can run your Django Server by command:
```bash
py manage.py runserver
```

or add Django Server in Run/Debug Configuration
and press run button.

* visit http://127.0.0.1:8000/

## Usage

Login:
![step1](static/img/readme/1.png?raw=true "Title")

My Profile page (you can edit your profile):
![step3](static/img/readme/2.png?raw=true "Title")

Avatar:
![step4](static/img/readme/3.png?raw=true "Title")

Referrals page:
![step4](static/img/readme/4.png?raw=true "Title")

Profile of Oleg`s referral (Masha):
![step4](static/img/readme/5.png?raw=true "Title")

All profiles page:
![step4](static/img/readme/6.png?raw=true "Title")


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU](https://choosealicense.com/licenses/gpl-3.0/)