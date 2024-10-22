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
        - $PQTMSAVEPAR,1*6A (Invalid parameters)
        - $PQTMSAVEPAR,2*6B (Execution failed)
        - $PQTMSAVEPAR,3*6C (Command not supported)
    """
    fields = (
        ('Subtype', 'subtype'),
        ('Status', 'status')
    )

    def __init__(self, manufacturer, data):
        super(QTMSAVEPAR, self).__init__(manufacturer, data)
        self.status = self.parse_status(data[1])  # Handling the status field

    @staticmethod
    def parse_status(value):
        """
        Parse the status field to return either the OK status or the corresponding error description.
        """
        status_map = {
            "1": "Invalid parameters",
            "2": "Execution failed",
            "3": "Command not supported"
        }
        return status_map.get(value, value)  # Default to the original value if not in map
