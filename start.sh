#!bin/bash
source venv/bin/activate
cd shop_backend && python3 manage.py runserver
cd shop_frontend && npm run serve