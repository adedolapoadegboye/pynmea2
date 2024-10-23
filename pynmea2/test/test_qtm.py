import pynmea2

def test_pqtmverno():
    """Test PQTMVERNO with successful version response."""
    data = "$PQTMVERNO,LC29HAANR01A04S,2022/11/04,16:39:48*34"
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.qtm.QTMVERNO
    assert msg.subtype == "VERNO"
    assert msg.version == "LC29HAANR01A04S"
    assert msg.build_date == "2022/11/04"
    assert msg.build_time == "16:39:48"

def test_pqtmsavepar():
    """Test PQTMSAVEPAR with OK status."""
    data = "$PQTMSAVEPAR,OK*72"
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.qtm.QTMSAVEPAR
    assert msg.status == "OK"

def test_pqtmrestorepar():
    """Test PQTMRESTOREPAR with OK status."""
    data = "$PQTMRESTOREPAR,OK*3B"
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.qtm.QTMRESTOREPAR
    assert msg.status == "OK"

def test_qtmepe():
    """Test QTMEPE with example data."""
    data = "$PQTMEPE,2,3.393,3.476,12.713,4.857,13.609*5D"
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.qtm.QTMEPE
    assert msg.subtype == "EPE"
    assert msg.msg_ver == "2"
    assert msg.epe_north == "3.393"
    assert msg.epe_east == "3.476"
    assert msg.epe_down == "12.713"
    assert msg.epe_2d == "4.857"
    assert msg.epe_3d == "13.609"
