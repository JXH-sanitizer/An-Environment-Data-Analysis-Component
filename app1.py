from flask import Flask
from apps import create_fileapp
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from exts import db
from apps.file.model import File
from apps.pollution.model import Pollution

app = create_fileapp()
manager = Manager(app=app)
migrate = Migrate(app=app,db=db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    #print(app.url_map) 打印app的url表，便于找寻各视图函数的路由
    manager.run()
