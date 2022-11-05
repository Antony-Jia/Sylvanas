#/bin/bash

alembic upgrade head

python -m app.initial_data