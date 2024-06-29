FROM python:3.8-slim

WORKDIR /CRUD_WEBAPP

COPY static/ /CRUD_WEBAPP/static/
COPY templates/ /CRUD_WEBAPP/templates
COPY backend.py database.py pydeps.txt /CRUD_WEBAPP/

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r pydeps.txt

EXPOSE 5000

CMD ["python", "backend.py"]
