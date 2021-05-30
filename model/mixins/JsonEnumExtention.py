import json
from model.enums.Lang import Lang
from model.enums.PartOfSpeech import PartOfSpeech
from model.enums.TokenizerType import TokenizerType
from model.enums.ViewType import ViewType
from model.enums.Defins import Defins


PUBLIC_ENUMS = {
    'Lang': Lang,
    'PartOfSpeech': PartOfSpeech,
    'TokenizerType': TokenizerType,
    'ViewType': ViewType,
    'Defins': Defins
}


class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj) in PUBLIC_ENUMS.values():
            return {"__enum__": str(obj)}
        return json.JSONEncoder.default(self, obj)


def as_enum(d):
    if "__enum__" in d:
        name, member = d["__enum__"].split(".")
        return getattr(PUBLIC_ENUMS[name], member)
    else:
        return d
