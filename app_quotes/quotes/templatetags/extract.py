from django import template
from django.shortcuts import get_object_or_404

from ..models import Author
#from ..utils import get_mongodb

register = template.Library()


def get_author(id_):
    # db = get_mongodb()
    # author = db.authors.find_one({'_id': ObjectId(id_)})
    author = get_object_or_404(Author, id=id_)
    return author.fullname


register.filter('author', get_author)
