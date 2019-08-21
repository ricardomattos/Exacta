#!/bin/bash

echo "using alembic to manage migrations"

alembic -c challenge.ini upgrade head

alembic -c challenge.ini revision --autogenerate -m "init"

echo "starting server"

pserve challenge.ini