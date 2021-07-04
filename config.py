# 数据库配置信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'mydb'
USERNAME = 'root'
PASSWORD = 'admin'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

# URI格式：dialect+driver://username:password@host:port/database
# dialect是数据库的实现，比如MySQL、PostgreSQL、SQLite，并且转换成小写
# driver是Python对应的驱动，如果不指定，会选择默认的驱动，比如MySQL的默认驱动是MySQLdb
# username是连接数据库的用户名
# password是连接数据库的密码
# host是连接数据库的域名
# port是数据库监听的端口号
# database是连接哪个数据库的名字