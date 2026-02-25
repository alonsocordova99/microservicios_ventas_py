# api-fastapi-python

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
uvicorn main:app --reload
```

## Alembic

```bash
    pip install alembic
    alembic init alembic
    alembic revision --autogenerate -m "Descripción de la revision"
    alembic upgrade head
    alembic downgrade -1
    alembic history
```

Para crear una nueva base de datos, ejecutar el siguiente comando:

```bash
alembic revision --autogenerate -m "Descripción de la revision"
```

Para actualizar la base de datos, ejecutar el siguiente comando:

```bash
alembic upgrade head
```

Para revertir la última revision, ejecutar el siguiente comando:

```bash
alembic downgrade -1
```

Para ver las revisiones, ejecutar el siguiente comando:

```bash
alembic history
```