from mongoengine import Document,StringField,FileField

class Verb(Document):
    verb_name = StringField(required=True, unique=True,max_length=500)
    eng_meaning = StringField(required=True,max_length=500)
    hin_meaning=StringField(required=True,max_length=500)
    satz=StringField(required=True,max_length=1000)
    level=StringField()
    type=StringField()
    subtype=StringField()
    case=StringField()
    input_pic=FileField()
