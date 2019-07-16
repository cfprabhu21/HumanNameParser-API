# HumanNameParser-API
Python Django based Human Name Parser API.
This simple API for parsing the Human name. This is based on Python Django and DRF. <br>I am used the Python Human Name Parser <a href="https://github.com/derek73/python-nameparser">Refer</a>.<br>
Thanks <a href="https://github.com/derek73">Derek73</a>.<br>

API URL: http://cfprabhu.pythonanywhere.com/humannameparser/ <br>
Input data: {"name":"Dr. Juan Q. Xavier de la Vega III (Doc Vega)"}<br>
Response: <br>{
    "response": {<br>
        "suffix": "III",<br>
        "middle": "Q. Xavier",<br>
        "first": "Juan",<br>
        "nickname": "Doc Vega",<br>
        "title": "Dr.",<br>
        "last": "de la Vega"<br>
    },<br>
    "name": "Dr. Juan Q. Xavier de la Vega III (Doc Vega)"<br>
}<br>

<h2>How to run this project on local</h2><br>
<ul>
  <li>Clone this project from your Machine</li>
  <li> cd HumanNameParser-API</li>
  <li> pip install -r requirements.txt</li>
  <li> python manage.py runserver</>
</ul>  
  
  
