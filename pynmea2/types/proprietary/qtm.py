from ... import nmea

class QTM(nmea.ProprietarySentence):
    sentence_types = {}

    def __new__(_cls, manufacturer, data):
        # Dynamically derive the message class name
        name = manufacturer + data[0]  # Use first data element as part of the name
        cls = _cls.sentence_types.get(name, _cls)
        return super(QTM, cls).__new__(cls)

class QTMSAVEPAR(QTM):
    """
        PQTM SAVEPAR Message

        Supports:
        - $PQTMSAVEPAR,OK*72
    """
    fields = (
        ('Subtype', 'subtype'),
        ('Status', 'status')
    )
