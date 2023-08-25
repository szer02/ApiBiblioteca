#ApiBiblioteca

ENV 
======

* Linux / MAC

```bash
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```

* Windows

```bash
python -m venv venv && venv\Scripts\activate.bat && pip install -r requirements.txt
```

Executar a api:
````bash
uvicorn main:app --reload --port 8000
````

Abra o seu navegador em http://127.0.0.1:5032

Documentação da APIs: http://127.0.0.1:5032/docs



sudo yum install python-devel postgresql-devel rpm-build
pip install psycopg2
