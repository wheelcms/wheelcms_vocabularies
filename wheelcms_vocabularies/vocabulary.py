import json

from django.db.utils import DatabaseError
# from django.db import connection

from .models import Vocabulary as VocabularyModel

## XXX cache this!

class Vocabulary(object):
    """
        Vocabulary cannot be used as a choice on a Model field since it
        will be evaluated at a moment when no database is available or
        tables haven't been created.
    """
    def __init__(self, key):
        self.key = key

    def __iter__(self):
        try:
            return iter(json.loads(
                        VocabularyModel.objects.get(key=self.key).raw)
                       )
        except (VocabularyModel.DoesNotExist, ValueError):
            return iter([])
        #except DatabaseError:
        #    ## table may not exist yet
        #    connection._rollback()
        #    return iter([])
