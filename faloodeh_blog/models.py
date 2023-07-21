from Faloodeh.Faloodeh_SqlAlchemy import models
from Faloodeh.Faloodeh_SqlAlchemy.models import Text, DateTime
from sqlalchemy.sql import func


class Post(models.Model):
    __tablename__ = 'post'
    _id = models.Column('id', models.Integer, unique=True, primary_key=True)
    title = models.Column('title', models.String(100))
    slug = models.Column('slug', models.String(100))
    body = models.Column(Text())
    date = models.Column(DateTime(timezone=True), server_default=func.now())
    image = models.Column('image', models.String(150))

# class Student(models.Model):
#     __tablename__ = 'student'
    
#     _id = models.Column('id', models.Integer, unique=True, primary_key=True)
#     name = models.Column('name', models.String(50))

engine = models.engine()
session = models.session(bind=engine)
models.migrate_db(engine)