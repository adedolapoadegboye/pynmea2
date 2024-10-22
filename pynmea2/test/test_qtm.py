import pynmea2

def test_pqtmsavepar_ok():
    """Test PQTMSAVEPAR with OK status."""
    data = "$PQTMSAVEPAR,OK*72"
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.qtm.QTMSAVEPAR
    assert msg.status == "OK"

def test_pqtmsavepar_invalid_params():
    """Test PQTMSAVEPAR with 'Invalid parameters' error."""
    data = "$PQTMSAVEPAR,1*47"
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.qtm.QTMSAVEPAR
    assert msg.status == "Invalid parameters"

def test_pqtmsavepar_execution_failed():
    """Test PQTMSAVEPAR with 'Execution failed' error."""
    data = "$PQTMSAVEPAR,2*44"
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.qtm.QTMSAVEPAR
    assert msg.status == "Execution failed"

def test_pqtmsavepar_command_not_supported():
    """Test PQTMSAVEPAR with 'Command not supported' error."""
    data = "$PQTMSAVEPAR,3*45"
    msg = pynmea2.parse(data)
    assert type(msg) == pynmea2.qtm.QTMSAVEPAR
    assert msg.status == "Command not supported"
