from django:latest
volume /media2/.image-sex
copy . /app 
entrypoint [ "python" ]
cmd ["/app/manage.py","runserver","0.0.0.0:8000"]
