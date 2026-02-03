创建虚拟环境
python -m venv ll_env
激活虚拟环境
ll_env\Scripts\activate
更新pip（可选）
python.exe -m pip install --upgrade pip
安装django
pip install django
Django创建新项目
django-admin startproject blog_project .
迁移数据库
python manage.py migrate
启动服务器
python manage.py runserver

创建应用程序
python manage.py startapp blogs
定义模型
blogs/models.py
激活模型
blog_project/settings.py
修改数据库，使其能够存储
python manage.py makemigrations blogs
#修改 models.py，对blogs 调用 makemigrations，以及让 Django 迁移项目。

创建超级用户
python manage.py createsuperuser
