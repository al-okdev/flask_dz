from sqlalchemy import exc

import config
import errors
from app import db


class BaseModelMixin:

    @classmethod
    def by_id(cls, obj_id):
        obj = cls.query.get(obj_id)
        if obj:
            return obj
        else:
            raise errors.NotFound

    def add(self):
        db.session.add(self)
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.BadLuck

    def delete_ads(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        try:
            db.session.add(self)
            db.session.commit()
        except exc.IntegrityError:
            raise errors.BadLuck


class Ads(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(120), index=True, unique=True)
    data_create = db.Column(db.Date())
    user_id = db.Column(db.Integer)

    def __str__(self):
        return '<title {}>'.format(self.title)

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'data_create': self.data_create,
            'user_id': self.user_id,
        }