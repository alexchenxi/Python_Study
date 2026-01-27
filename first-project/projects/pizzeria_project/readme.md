创建虚拟环境
python -m venv ll_env
激活虚拟环境
ll_env\Scripts\activate
更新pip
python.exe -m pip install --upgrade pip
安装django
pip install django
Django创建新项目
django-admin startproject ll_project .
启动服务器
python manage.py runserver