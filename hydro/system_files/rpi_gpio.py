"""
Support for controlling GPIO pins of a Raspberry Pi.

For more details about this component, please refer to the documentation at
https://home-assistant.io/components/rpi_gpio/
"""
# pylint: disable=import-error
import logging

from homeassistant.const import (
    EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP)

REQUIREMENTS = ['RPi.GPIO==0.6.1']

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'rpi_gpio'


# pylint: disable=no-member
def setup(hass, config):
    """Setup the Raspberry PI GPIO component."""
    ## MV3 change
    #import RPi.GPIO as GPIO
    import Adafruit_BBIO.GPIO as GPIO

    def cleanup_gpio(event):
        """Stuff to do before stopping."""
        GPIO.cleanup()

    def prepare_gpio(event):
        """Stuff to do when home assistant starts."""
        hass.bus.listen_once(EVENT_HOMEASSISTANT_STOP, cleanup_gpio)

    hass.bus.listen_once(EVENT_HOMEASSISTANT_START, prepare_gpio)
    ## MV3 change
    #GPIO.setmode(GPIO.BCM)
    return True


def setup_output(port):
    """Setup a GPIO as output."""
    ## MV3 change
    #import RPi.GPIO as GPIO
    import Adafruit_BBIO.GPIO as GPIO
    if port == 7:
        GPIO.setup("P9_42", GPIO.OUT)
    elif port == 60:
        GPIO.setup("P9_12", GPIO.OUT)
    elif port == 26:
        GPIO.setup("P8_14", GPIO.OUT)
    elif port == 46:
        GPIO.setup("P8_16", GPIO.OUT)
    else:
        print("MV3 NOT SUPPORTED OUTPUT")


def setup_input(port, pull_mode):
    """Setup a GPIO as input."""
    ## MV3 change
    #import RPi.GPIO as GPIO
    import Adafruit_BBIO.GPIO as GPIO
    GPIO.setup(port, GPIO.IN,
               GPIO.PUD_DOWN if pull_mode == 'DOWN' else GPIO.PUD_UP)


def write_output(port, value):
    """Write a value to a GPIO."""
    ## MV3 change
    #import RPi.GPIO as GPIO
    import Adafruit_BBIO.GPIO as GPIO
    if port == 7:
        if value == 0:
            GPIO.output("P9_42", GPIO.LOW)
        else:
            GPIO.output("P9_42", GPIO.HIGH)
    elif port == 60:
        if value == 0:
            GPIO.output("P9_12", GPIO.LOW)
        else:
            GPIO.output("P9_12", GPIO.HIGH)
    elif port == 26:
        if value == 0:
            GPIO.output("P8_14", GPIO.LOW)
        else:
            GPIO.output("P8_14", GPIO.HIGH)
    elif port == 46:
        if value == 0:
            GPIO.output("P8_16", GPIO.LOW)
        else:
            GPIO.output("P8_16", GPIO.HIGH)
    else:
        print("MV3 NOT SUPPORTED OUTPUT")


def read_input(port):
    """Read a value from a GPIO."""
    ## MV3 change
    #import RPi.GPIO as GPIO
    import Adafruit_BBIO.GPIO as GPIO
    return GPIO.input(port)


def edge_detect(port, event_callback, bounce):
    """Add detection for RISING and FALLING events."""
    import RPi.GPIO as GPIO
    GPIO.add_event_detect(
        port,
        GPIO.BOTH,
        callback=event_callback,
        bouncetime=bounce)
