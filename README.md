# SimpleTaskManager
A simple task manager built with Python and Flask

## Setup
1. In File Manager, navigate to your TaskManager repo folder
2. Right-click, Open Terminal Here

3. To Create the Database:
python3 <enter>
>>> from app import db
>>> db.create_all()
>>> from models import Task
>>> from datetime import datetime
>>> t = Task(title="abc", date=datetime.utcnow()
>>> t

<should show abc, but probably transient.

>>> db.session.add(t)
>>> db.session.commit()
>>> Task.query.all()
<should show [abc], but probably transient.

>>> exit()

If model changes, just delete the data.db in the project folder and re-create as above

4. To Run the App:
python3 app

## add a .env file and add this line with your secret key:
``` SECRET_KEY = 'my_secret_key' ```
