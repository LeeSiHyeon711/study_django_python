import pymysql

# PyMySQL을 MySQLdb로 위장
pymysql.install_as_MySQLdb()

# Django 6.0의 버전 체크를 우회하기 위해 MySQLdb 버전 정보 수정
try:
    import MySQLdb
    # MySQLdb의 버전 정보를 2.2.1로 설정하여 Django의 버전 체크 통과
    MySQLdb.version_info = (2, 2, 1, 'final', 0)
    MySQLdb.__version__ = '2.2.1'
except ImportError:
    pass

# Django의 mysql 백엔드 버전 체크를 우회
import django.db.backends.mysql.base
# Database 객체의 __version__ 속성을 수정
if hasattr(django.db.backends.mysql.base, 'Database'):
    django.db.backends.mysql.base.Database.__version__ = '2.2.1'
