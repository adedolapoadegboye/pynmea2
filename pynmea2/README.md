Here’s the **updated README** to align with the updated `setup.py` file:

---

# **pynmea2-quectel**  

`pynmea2-quectel` is a Python library that supports both the **standard NMEA 0183 protocol** and **Quectel proprietary GNSS messages**, making it suitable for a variety of GNSS modules and applications.  

This fork expands the original `pynmea2` library by adding support for **Quectel-specific PQTM messages**, enhancing compatibility with Quectel GNSS receivers.

The repository for `pynmea2-quectel` is available at <https://github.com/adedolapoadegboye/pynmea2>.  

---

## **Compatibility**

`pynmea2-quectel` supports the following Python versions:

- **Python 2.7**  
- **Python 3.4 – 3.13**  
- **PyPy**  

![Python version](https://img.shields.io/pypi/pyversions/pynmea2.svg?style=flat)  
[![Build status](https://github.com/adedolapoadegboye/pynmea2/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/adedolapoadegboye/pynmea2/actions/workflows/ci.yml)  
[![Coverage status](https://img.shields.io/coveralls/github/adedolapoadegboye/pynmea2/master.svg?style=flat)](https://coveralls.io/r/adedolapoadegboye/pynmea2?branch=master)  

---

## **Installation**

You can install the library using `pip`:

```bash
pip install pynmea2-quectel
```

[![PyPI version](https://img.shields.io/pypi/v/pynmea2.svg?style=flat)](https://pypi.org/project/pynmea2/)  
[![PyPI downloads](https://img.shields.io/pypi/dm/pynmea2.svg?style=flat)](https://pypi.org/project/pynmea2/)  

---

## **New Features in This Fork**

- **Support for Quectel proprietary PQTM messages**, extending functionality for Quectel GNSS receivers.
- Fully compatible with both **standard NMEA 0183 protocol** and Quectel-specific enhancements.

---

## **Usage Example: Parsing NMEA and Proprietary Messages**

The `pynmea2-quectel` library can parse both standard and proprietary NMEA sentences.  

Example:

```python
import pynmea2

# Parsing a Quectel PQTM message
msg = pynmea2.parse("$PQTM,123456.00,1,45.5,27.6*68")
print(msg)
```

**Output:**

```
<PQTM(timestamp=datetime.time(12, 34, 56), status='1', temp='45.5', humidity='27.6')>
```

---

## **Generating NMEA Sentences**

You can generate NMEA messages using the library:

```python
import pynmea2

msg = pynmea2.PQTM('PQ', 'TM', ('123456.00', '1', '45.5', '27.6'))
print(str(msg))
# Output: $PQTM,123456.00,1,45.5,27.6*68
```

---

## **Reading from Files Example**

See [examples/read_file.py](/examples/read_file.py):

```python
import pynmea2

with open('examples/data.log', 'r', encoding='utf-8') as file:
    for line in file:
        try:
            msg = pynmea2.parse(line)
            print(repr(msg))
        except pynmea2.ParseError as e:
            print(f'Parse error: {e}')
```

---

## **Reading from Serial Devices Example**

See [examples/read_serial.py](/examples/read_serial.py):

```python
import io
import pynmea2
import serial

ser = serial.Serial('/dev/ttyS1', 9600, timeout=5.0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

while True:
    try:
        line = sio.readline()
        msg = pynmea2.parse(line)
        print(repr(msg))
    except serial.SerialException as e:
        print(f'Device error: {e}')
        break
    except pynmea2.ParseError as e:
        print(f'Parse error: {e}')
```

---

## **Author and License**

- **Author**: Ade Adegboye  
- **Email**: [adedolapo.adegboye@quectel.com](mailto:adedolapo.adegboye@quectel.com)  
- **License**: MIT License  

---

## **Keywords and Topics**

- **Keywords**: python, nmea, gps, parse, parsing, nmea0183, 0183, quectel, gnss, proprietary  
- **Topics**: Scientific/Engineering (GIS), Software Development, GNSS Modules  

---

## **Summary**

`pynmea2-quectel` provides enhanced support for **Quectel proprietary messages**, in addition to full support for the **NMEA 0183 protocol**. It is ideal for developers working with **GNSS data**, especially those using **Quectel modules**. The package supports a broad range of Python versions, from 2.7 to 3.13, ensuring compatibility across various environments.

---

This README now reflects the changes in the **`setup.py`** file, emphasizing the new project name, author information, and Quectel support. Let me know if further adjustments are needed!