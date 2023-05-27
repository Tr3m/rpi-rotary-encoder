# RPi-rotary-encoder: Rotary Encoder for Raspberry Pi

A simple rotary encoder python class that abstracts all the code needed for using a 3-pin rotary encoder with Raspberry Pi's GPIO pins.

## Usage

```python
from Encoder import Encoder
import time

my_encoder = Encoder(<PIN_1>, <PIN_2>, <MIN_VALUE>, <MAX_VALUE>, <INCREMENT>)

while True:
    time.sleep(0.2)
    my_encoder.getValue()

```

Value changes are stored inside the Encoder object and can be returned by calling the `getValue()` method.

Code examples usable on the Raspberry Pi can be found under the ```examples``` directory.

## OSCEncoder Class

```OSCEncoder``` is an Encoder subclass with the addition of being able broadcast the value changes as OSC messages over the network for IoT applications.

## Usage

```python
from OSCEncoder import OSCEncoder
from pythonosc.udp_client import SimpleUDPClient

client = SimpleUDPClient(ip, port)

my_osc_encoder = OSCEncoder(<PIN_1>, <PIN_2>, <MIN_VALUE>, <MAX_VALUE>, <INCREMENT>, client, "some/osc/address")

while True:
    time.sleep(0.2)
    my_osc_encoder.getValue() # While this method can still be used, it's not required for the encoder to broadcast the value changes.

```

The ```OSCEncoder``` class depends on the [python-osc](https://pypi.org/project/python-osc/) package, which can be installed by running:

```shell
pip install python-osc
```