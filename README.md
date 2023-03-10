<h1> API for YaTube project</h1>
<h4> Description: API for social network YaTube </h4>

<h1>Technology stack:</h1>

    Python 3.9
    Django 3.2.16
    Django Rest Framework
    SQLite

<h1>Manual</h1>

<h4><i>1.Clone this repository:</i></h4>

    git clone git@github.com:hukumabob/api_final_yatube.git

    cd api_final_yatube

<h4><i>2.Install virtual environment</i></h4>

    python -m venv venv

<h4><i>3.Activate virtual environment</i></h4>

    source venv\Scripts\activate

<h4><i>4.Install python packages:</i></h4>

    python -m pip install --upgrade pip

    pip install -r requirements.txt

<h4><i>5.Run database migrations:</i></h4>

    python manage.py migrate

<h4><i>6.Run project:</i></h4>

    python manage.py runserver
      
<h1>Samples</h1>

<em><strong> GET: http://127.0.0.1:8000/api/v1/posts/ </em></strong> 

<em><strong> Response: </em></strong>

    {
      "count": 123,
      "next": "http://api.example.org/accounts/?offset=400&limit=100",
      "previous": "http://api.example.org/accounts/?offset=200&limit=100",
      "results": [
        {
          "id": 0,
          "author": "string",
          "text": "string",
          "pub_date": "2021-10-14T20:41:29.648Z",
          "image": "string",
          "group": 0
        }
      ]
    }

<em><strong> POST: http://127.0.0.1:8000/api/v1/posts/ : </em></strong>

 <em><strong> Responce: </em></strong>

      {
       "text": "string",
       "image": "string",
       "group": 0
      }

 <em><strong> Request: </em></strong>

      {
       "id": 0,
       "author": "string",
       "text": "string",
       "pub_date": "2021-08-24T14:15:22Z",
       "image": "string","group": 0
      }
<h1>Static API documentation</h1>
    
http://127.0.0.1:8000/redoc/