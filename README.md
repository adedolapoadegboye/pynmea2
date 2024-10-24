# nmea2-quectel

`nmea2-quectel` is an extension of the popular Python library [`pynmea2`](https://github.com/Knio/pynmea2), designed to handle Quectel GNSS module-specific NMEA messages with enhanced capabilities. This library offers full compatibility with standard NMEA parsing while adding support for proprietary Quectel-specific messages, configuration commands, and detailed status outputs.

## Features

- **Extended NMEA Support**: Full compatibility with standard NMEA messages.
- **Quectel Proprietary Commands**:
  - Configuration and status commands specific to Quectel GNSS modules.
  - Support for advanced operations such as geofencing, odometer, and debugging commands.
- **Message Parsing and Construction**: Ability to parse, construct, and interpret messages such as:
  - `PQTMCFGGEOFENCE`, `PQTMGEOFENCESTATUS`
  - `PQTMCFGSVIN`, `PQTMSVINSTATUS`
  - `PQTMVEL`, `PQTMPL`, `PQTMDOP`
  - `PQTMCFGRCVRMODE`, `PQTMCFGNMEADP`
- **Support for Set and Get Operations**: Handle both configuration (`SET`) and retrieval (`GET`) commands.
- **High-Level API**: Simplifies interaction with Quectel modules via clean message classes.

## Installation

You can install the library directly from GitHub:

```bash
pip install git+https://github.com/your-username/nmea2-quectel.git
```

Or, clone the repository and install it manually:

```bash
git clone https://github.com/your-username/nmea2-quectel.git
cd nmea2-quectel
pip install .
```

## Usage

Here's a quick example of how to use `nmea2-quectel` to parse and interact with Quectel-specific messages.

### Parsing Quectel-Specific NMEA Messages

```python
import pynmea2

# Example message for setting GNSS mode
msg = pynmea2.parse("$PQTMCFGRCVRMODE,OK,2*7A")
print(msg)
print(f"Status: {msg.status}, Mode: {msg.get_mode_description()}")
```

### Supported Messages

#### `PQTMCFGRCVRMODE`
```python
msg = pynmea2.parse("$PQTMCFGRCVRMODE,OK,2*7A")
print(msg.mode)  # Output: 2
print(msg.get_mode_description())  # Output: "Base Station"
```

#### `PQTMCFGGEOFENCE`
```python
msg = pynmea2.parse("$PQTMCFGGEOFENCE,OK,1,1,0,2,30.123,-90.123,5.0,-91.456*41")
print(msg.index)  # Output: 1
print(msg.lat0, msg.lon0)  # Output: 30.123, -90.123
```

#### `PQTMVEL`
```python
msg = pynmea2.parse("$PQTMVEL,1,154512.100,1.0,2.0,3.0,5.0,6.0,180.512,0.124*67")
print(msg.vel_n, msg.vel_e, msg.vel_d)  # Output: 1.0, 2.0, 3.0
```

### Creating Your Own Messages

You can also construct messages programmatically for specific operations:

```python
from pynmea2.quectel import PQTMCFGRCVRMODE

msg = PQTMCFGRCVRMODE("Quectel", ["CFGRCVRMODE", "OK", "2"])
print(str(msg))  # Output: "$PQTMCFGRCVRMODE,OK,2*7A"
```

## Documentation

For detailed documentation on each Quectel-specific message, refer to the official [Quectel GNSS Module Protocol Specification](https://www.quectel.com/product/gnss).

The following message classes are currently supported:
- **Configuration Commands**: `PQTMCFGRCVRMODE`, `PQTMCFGSVIN`, `PQTMCFGNMEADP`, `PQTMCFGGEOFENCE`
- **Status Messages**: `PQTMSVINSTATUS`, `PQTMGEOFENCESTATUS`, `PQTMDOP`, `PQTMPL`
- **Command Responses**: `PQTMDebugOn`, `PQTMCFGFIXRATE`, `PQTMGNSSSTART`, `PQTMGNSSSTOP`
- **Output Messages**: `PQTMVEL`, `PQTMDOP`, `PQTMODO`

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request with your improvements or bug fixes.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgments

- Based on [`pynmea2`](https://github.com/Knio/pynmea2).
- Special thanks to the Quectel team for their detailed GNSS protocol documentation.

---

Feel free to reach out if you encounter issues or have suggestions for improvement.