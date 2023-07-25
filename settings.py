class File_Config:
    ENV = 'development'
    DEBUG = True
    UPLOAD_FOLDER = 'uploads/'  #设定文件保存路径的文件夹
    ALLOWED_EXTENSIONS = {'xls','xlsx'}  #设定文件扩展名
    MAX_CONTENT_LENGTH = 16*1024*1024  #设定文件最大大小
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@host:port/database name'  #设定保存数据的数据库的路径