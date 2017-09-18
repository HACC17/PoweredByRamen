## Team Name:
PoweredByRamen

## Team Members:
* Shiho You - 志保
* Siyuan Chen - 斯源

## About:

Django project to recreate Hawaii Department of Health's EAL Surfer form (originally in Excel format) as a web application for the HACC event.
Resource materials provided by DoH: https://github.com/HACC17/challenges/tree/master/DOH_HEER

## Prerequisites:
* Basic command line knowledge
* Python (v 2.7.x, might need some tweaking in the code if you're planning to use v 3.6.x)
* Pip (v 9.0.1) or easy_install (v 36.4.0)
* Sqlite3 (v 3.16.0 or equivalent)
* Pdfkit (v 0.6.1)
* Wkhtmltopdf (v 0.12.4)
* Django (v 1.11.5)
* (Optional) virtualenv (v 15.1.0)

## How to run:
Optional -- create a virtualenv project (assuming you had installed it via pip) with command
```bash
virtualenv <projectName>
cd <projectName>
source  <projectName>/bin/activate
```
1. Clone/Download project to desired folder
2. Go into the cloned/downloaded project folder and Install required packages with command
```bash
pip -r requirements.txt
```
3. Navigate into "EAL_Surfer" directory via cmd prompt/*NIX shell
4. Run command 
```bash
python manage.py runserver
```
Note: for some reason the "wkhtmltopdf" package doesn't install correctly, so you will
need to install it from their official website, and add the executable to your ENV or copy the executable somehwere your system will find 
5. Open web browser and enter url: "http://127.0.0.1:8000/" (left it as default)
6. Enjoy

## Optional:
1. There's an admin page for administrator to add/update/delete data from the back-end Sqlite DB
2. Before that create a superuser for the app via. command
```bash
python manage.py createsuperuser
```
3. Access the administrative page by going to "http://127.0.0.1:8000/admin"
4. This page will prompt for username and password created in step 2
5. Now you have admin access to the back-end DB
