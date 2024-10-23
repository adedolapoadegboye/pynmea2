from ... import nmea

class QTM(nmea.ProprietarySentence):
    sentence_types = {}

    def __new__(_cls, manufacturer, data):
        # Dynamically derive the message class name
        name = manufacturer + data[0]  # Use first data element as part of the name
        cls = _cls.sentence_types.get(name, _cls)
        return super(QTM, cls).__new__(cls)

class QTMVERNO(QTM):
    """
    PQTMVERNO Message

    Supports:
    - $PQTMVERNO,<VerStr>,<BuildDate>,<BuildTime>*<Checksum>
    """
    fields = (
        ('subtype', 'subtype'),  # VERNO
        ('version', 'version'),  # LC29HAANR01A04S for example
        ('build_date', 'build_date'),  # Format: YYYY/MM/DD
        ('build_time', 'build_time'),  # Format: HH:MM:SS
    )

    def __init__(self, manufacturer, data):
        super(QTMVERNO, self).__init__(manufacturer, data)
        print(data)  # Debugging print to confirm input structure

        # Set attributes based on successful data
        self.subtype = data[0]
        self.version = data[1]
        self.build_date = data[2]
        self.build_time = data[3]

class QTMSAVEPAR(QTM):
    """
    PQTM SAVEPAR Message

    Supports:
    - $PQTMSAVEPAR,OK*72
    """
    fields = (
        ('subtype', 'subtype'),
        ('status', 'status')
    )

    def __init__(self, manufacturer, data):
        super(QTMSAVEPAR, self).__init__(manufacturer, data)
        self.status = data[1]  # Handle status field

class QTMRESTOREPAR(QTM):
    """
    PQTM RESTOREPAR Message

    Supports:
    - $PQTMRESTOREPAR,OK*3B
    """
    fields = (
        ('subtype', 'subtype'),
        ('status', 'status')
    )

    def __init__(self, manufacturer, data):
        super(QTMRESTOREPAR, self).__init__(manufacturer, data)
        self.status = data[1]  # Handle status field

class QTMEPE(QTM):
    """
    PQTMEPE Message

    Outputs the estimated positioning error.

    Supports:
    - $PQTMEPE,<MsgVer>,<EPE_North>,<EPE_East>,<EPE_Down>,<EPE_2D>,<EPE_3D>*<Checksum>
    """

    fields = (
        ('subtype', 'subtype'),  # EPE
        ('msg_ver', 'msg_ver'),  # Message version (always 2)
        ('epe_north', 'epe_north'),  # Estimated north error (in meters)
        ('epe_east', 'epe_east'),  # Estimated east error (in meters)
        ('epe_down', 'epe_down'),  # Estimated down error (in meters)
        ('epe_2d', 'epe_2d'),  # Estimated 2D position error (in meters)
        ('epe_3d', 'epe_3d'),  # Estimated 3D position error (in meters)
    )

    def __init__(self, manufacturer, data):
        super(QTMEPE, self).__init__(manufacturer, data)
        print(data)  # Debugging print to confirm input structure

        # Set attributes based on input data
        self.subtype = data[0]
        self.msg_ver = int(data[1])
        self.epe_north = float(data[2])
        self.epe_east = float(data[3])
        self.epe_down = float(data[4])
        self.epe_2d = float(data[5])
        self.epe_3d = float(data[6])

class QTMCFGGEOFENCE(QTM):
    """
    PQTMCFGGEOFENCE Message

    Supports:
    - $PQTMCFGGEOFENCE,OK,<Index>,<Status>,<Reserved>,<Shape>,<Lat0>,<Lon0>,<Lat1/Radius>,
      [<Lon1>,<Lat2>,<Lon2>,<Lat3>,<Lon3>]*<Checksum>
    """

    fields = (
        ('Subtype', 'subtype'),  # Always "CFGGEOGENCE"
        ('Status', 'status'),  # "OK"
        ('Index', 'index'),  # Geofence index (0-3)
        ('Enabled', 'enabled'),  # 0 = Disabled, 1 = Enabled
        ('Reserved', 'reserved'),  # Always 0
        ('Shape', 'shape'),  # Geofence shape (0-3)
        ('Lat0', 'lat0'),  # Latitude of the first point
        ('Lon0', 'lon0'),  # Longitude of the first point
        ('Lat1_or_Radius', 'lat1_or_radius'),  # Latitude/Radius based on shape
        ('Lon1', 'lon1'),  # Longitude of the second point (optional)
        ('Lat2', 'lat2'),  # Latitude of the third point (optional)
        ('Lon2', 'lon2'),  # Longitude of the third point (optional)
        ('Lat3', 'lat3'),  # Latitude of the fourth point (optional)
        ('Lon3', 'lon3')  # Longitude of the fourth point (optional)
    )

    def __init__(self, manufacturer, data):
        super(QTMCFGGEOFENCE, self).__init__(manufacturer, data)
        print(data)  # Debugging print to confirm input structure

        # Extract and assign the mandatory fields
        self.subtype = data[0]  # Should always be "CFGGEOGENCE"
        self.status = data[1]  # Should be "OK"
        self.index = data[2]
        self.enabled = data[3]  # 0 = Disabled, 1 = Enabled
        self.reserved = data[4]
        self.shape = data[5]
        self.lat0 = data[6]
        self.lon0 = data[7]
        self.lat1_or_radius = data[8]

        # Optional fields (only for specific shapes)
        if len(data) > 9:
            self.lon1 = data[9]
        if len(data) > 10:
            self.lat2 = data[10]
        if len(data) > 11:
            self.lon2 = data[11]
        if len(data) > 12:
            self.lat3 = data[12]
        if len(data) > 13:
            self.lon3 = data[13]

class QTMGEOFENCESTATUS(QTM):
    """
    PQTMGEOFENCESTATUS Message

    Supports:
    - $PQTMGEOFENCESTATUS,<MsgVer>,<Time>,<State0>,<State1>,<State2>,<State3>*<Checksum>

    Geofence State Meaning:
    - 0 = Unknown (Not defined)
    - 1 = Inside geofence
    - 2 = Outside geofence
    """

    fields = (
        ('Subtype', 'subtype'),  # Always "GEOFENCESTATUS"
        ('MsgVer', 'msg_ver'),  # Message version (Always 1)
        ('Time', 'time'),  # UTC time (hhmmss.sss)
        ('State0', 'state0'),  # Geofence state 0
        ('State1', 'state1'),  # Geofence state 1
        ('State2', 'state2'),  # Geofence state 2
        ('State3', 'state3')  # Geofence state 3
    )

    def __init__(self, manufacturer, data):
        super(QTMGEOFENCESTATUS, self).__init__(manufacturer, data)
        print(data)  # Debugging print to confirm input structure

        # Assign the parsed fields
        self.subtype = data[0]  # Should always be "GEOFENCESTATUS"
        self.msg_ver = data[1]  # Always 1
        self.time = data[2]  # UTC time in hhmmss.sss format

        # Convert states from raw data to meaningful descriptions
        self.state0 = self.parse_state(data[3])  # Geofence 0 state
        self.state1 = self.parse_state(data[4])  # Geofence 1 state
        self.state2 = self.parse_state(data[5])  # Geofence 2 state
        self.state3 = self.parse_state(data[6])  # Geofence 3 state

    @staticmethod
    def parse_state(state_value):
        """
        Parse the state field and return the corresponding description.
        """
        state_map = {
            "0": "Unknown",
            "1": "Inside geofence",
            "2": "Outside geofence"
        }
        return state_map.get(state_value, "Invalid state")  # Handle unexpected values

class QTMCFGSVIN(QTM):
    """
    PQTMCFGSVIN Message

    Note: This command is supported on LC29H (DA, EA) only

    Supports:
    - $PQTMCFGSVIN,OK,<Mode>,<MinDur>,<3D_AccLimit>,<ECEF_X>,<ECEF_Y>,<ECEF_Z>*<Checksum>

    Parameters:
    - Mode: Configure the receiver mode (0 = Disable, 1 = Survey-in, 2 = Fixed mode).
    - MinDur: Minimum survey-in duration (0-86400 seconds).
    - 3D_AccLimit: Limit 3D position accuracy in meters (0 = No limit).
    - ECEF_X/Y/Z: WGS84 ECEF X, Y, and Z coordinates in meters.
    """

    fields = (
        ('subtype', 'subtype'),  # CFGSVIN
        ('status', 'status'),  # OK
        ('mode', 'mode'),  # Receiver mode (0, 1, 2)
        ('min_dur', 'min_dur'),  # Survey-in duration (in seconds)
        ('acc_limit', 'acc_limit'),  # 3D accuracy limit in meters
        ('ecef_x', 'ecef_x'),  # ECEF X coordinate
        ('ecef_y', 'ecef_y'),  # ECEF Y coordinate
        ('ecef_z', 'ecef_z'),  # ECEF Z coordinate
    )

    def __init__(self, manufacturer, data):
        super(QTMCFGSVIN, self).__init__(manufacturer, data)
        print(data)  # Debugging print to confirm input structure

        # Set attributes based on input data
        self.subtype = data[0]  # Always "CFGSVIN"
        self.status = data[1]  # Should be "OK"
        self.mode = data[2]  # Mode (0, 1, or 2)
        self.min_dur = data[3]  # Survey-in minimum duration
        self.acc_limit = data[4]  # 3D accuracy limit
        self.ecef_x = data[5]  # ECEF X coordinate
        self.ecef_y = data[6]  # ECEF Y coordinate
        self.ecef_z = data[7]  # ECEF Z coordinate

class QTMSVINSTATUS(QTM):
    """
    PQTMSVINSTATUS Message

    Outputs the survey-in status.

    Supports:
    - $PQTMSVINSTATUS,<MsgVer>,<TOW>,<Valid>,<Res0>,<Res1>,<Obs>,<CfgDur>,<MeanX>,<MeanY>,
      <MeanZ>,<MeanAcc>*<Checksum>

    Parameters:
    - MsgVer: Message version (Always 1).
    - TOW: GPS Time of Week (milliseconds).
    - Valid: Survey-in position validity flag (0 = Invalid, 1 = In-progress, 2 = Valid).
    - Res0: Reserved field (Always 0).
    - Res1: Reserved field (Always 0).
    - Obs: Number of position observations.
    - CfgDur: Configured duration from the PQTMCFGSVIN command.
    - MeanX/Y/Z: Mean position along the X, Y, and Z axes in meters.
    - MeanAcc: Mean position accuracy in meters.
    """

    fields = (
        ('subtype', 'subtype'),  # Always "SVINSTATUS"
        ('msg_ver', 'msg_ver'),  # Message version (Always 1)
        ('tow', 'tow'),  # GPS Time of Week (milliseconds)
        ('valid', 'valid'),  # Survey-in validity flag (0, 1, 2)
        ('res0', 'res0'),  # Reserved (Always 0)
        ('res1', 'res1'),  # Reserved (Always 0)
        ('obs', 'obs'),  # Number of observations
        ('cfg_dur', 'cfg_dur'),  # Configured duration
        ('mean_x', 'mean_x'),  # Mean X position in meters
        ('mean_y', 'mean_y'),  # Mean Y position in meters
        ('mean_z', 'mean_z'),  # Mean Z position in meters
        ('mean_acc', 'mean_acc'),  # Mean position accuracy in meters
    )

    def __init__(self, manufacturer, data):
        super(QTMSVINSTATUS, self).__init__(manufacturer, data)
        print(data)  # Debugging print to confirm input structure

        # Assign the parsed fields to class attributes
        self.subtype = data[0]
        self.msg_ver = data[1]
        self.tow = data[2]
        self.valid = self.parse_validity(data[3])
        self.res0 = data[4]
        self.res1 = data[5]
        self.obs = data[6]
        self.cfg_dur = data[7]
        self.mean_x = data[8]
        self.mean_y = data[9]
        self.mean_z = data[10]
        self.mean_acc = data[11]

    @staticmethod
    def parse_validity(value):
        """
        Parse the validity flag to a meaningful description.
        """
        validity_map = {
            "0": "Invalid",
            "1": "In-progress",
            "2": "Valid"
        }
        return validity_map.get(value, "Unknown validity")

class QTMGNSSSTART(QTM):
    """
    PQTMGNSSSTART Message

    Starts the GNSS engine.

    Supports:
    - $PQTMGNSSSTART,OK*<Checksum>

    If successful, the response is:
    - OK
    """

    fields = (
        ('subtype', 'subtype'),  # Always "GNSSSTART"
        ('status', 'status'),  # Always "OK"
    )

    def __init__(self, manufacturer, data):
        super(QTMGNSSSTART, self).__init__(manufacturer, data)
        print(data)  # Debugging print to confirm input structure

        # Extract subtype and status
        self.subtype = data[0]
        self.status = data[1]

