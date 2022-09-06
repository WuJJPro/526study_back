# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


from app.extensions import db



class Collect(db.Model):
    __tablename__ = 'collect'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    userid = db.Column(db.String(255))
    collect_type = db.Column(db.Integer)
    file_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.FetchedValue())



class Download(db.Model):
    __tablename__ = 'download'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    userid = db.Column(db.String(255))
    download_type = db.Column(db.Integer)
    file_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.FetchedValue())



class FileCollection(db.Model):
    __tablename__ = 'file_collection'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    file_tag = db.Column(db.JSON)
    contain = db.Column(db.JSON)
    collection_name = db.Column(db.String(255))
    price = db.Column(db.Integer)



class UploadFile(db.Model):
    __tablename__ = 'upload_file'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    file_name = db.Column(db.String(255))
    field = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.FetchedValue())
    upload_user = db.Column(db.String(255))
    download_number = db.Column(db.Integer)
    file_type = db.Column(db.String(255))
    state = db.Column(db.Integer, info='1 未审核\\n2 已通过\\n0 未通过')
    file_path = db.Column(db.Integer)
    file_tap = db.Column(db.JSON)
    price = db.Column(db.Integer)



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    nickname = db.Column(db.String(255))
    avatar = db.Column(db.String(255))
    gold = db.Column(db.Integer)
    is_admin = db.Column(db.Integer, server_default=db.FetchedValue())
