# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import alsaaudio as audio
import time
import math
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

scanCards = audio.cards()
mixer = audio.Mixer('Digital', cardindex=2)

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)
# you can specify an I2C adress instead of the default 0x48
# ads = ADS.ADS1115(i2c, address=0x49)

# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
# chan = AnalogIn(ads, ADS.P0, ADS.P1)

ads.gain = 1

def avgToLevel(a):
    read = (a + 950) / 22000
    calculated = min (100, max(0.000001,100 * read))
    modified = math.floor(100 + 20 * math.log(calculated/100, 10))
    return min (100, max(0, modified))

lastResult = -1

while True:
    result = avgToLevel(chan.value)
    time.sleep(0.2)
    if lastResult != result:
        lastResult = result
        mixer.setvolume(result)
        print("{:>5}".format(result))
    time.sleep(0.1)
