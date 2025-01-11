from python:latest
volume /media2/.image-sex
copy . /app 
workdir /app
run pip install -r requirment.txt
entrypoint [ "python" ]
cmd ["manage.py","runserver","0.0.0.0:8000"]
