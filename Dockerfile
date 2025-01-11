FROM python:latest
VOLUME /media2/.image-sex
COPY . /app 
WORKDIR /app
RUN pip install -r requirment.txt
EXPOSE 80 
EXPOSE 8000
ENTRYPOINT [ "python" ]
CMD ["manage.py","runserver","0.0.0.0:80"]
