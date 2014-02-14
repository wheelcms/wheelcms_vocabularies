import json

from .models import Vocabulary as VocabularyModel

## XXX cache this!

class Vocabulary(object):
    def __init__(self, key):
        self.key = key

    def __iter__(self):
        try:
            return iter(json.loads(VocabularyModel.objects.get(key=self.key).raw))
        except (VocabularyModel.DoesNotExist, ValueError):
            return iter([])
