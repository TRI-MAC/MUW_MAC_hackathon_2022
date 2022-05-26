# tobii-glasses3
Code and documentation relating to usage and development of experiments with Tobii Pro Glasses 3.

## Using Tobii Resources

Download the Glasses 3 interface: https://connect.tobiipro.com/s/g3-downloads/.

## Collecting live data from Tobii Glasses 3 using Python

Tobii provides an HTTP API that can be accessed by any language that supports HTTP GET functionality. The API documentation can be found here: https://www.tobiipro.com/siteassets/tobii-pro/products/hardware/glasses-3/tobii-pro-glasses-3-developer-guide/.

To use python to get real-time data from the Tobii using the "requests" package:

1. Turn on the Tobii Pro Glasses 3 Receiver.
2. If using wifi, connect to the receiver (should show up as TG08B-080200042301 in your wifi list).
3. To open the API UI, open a browser and enter http://tg03b-080200042301.local/ in the address bar.

## tobii_websocket_test.py
Demonstrates how to leverage Python websockets to request and consume events from the glasses.

## g3_api_test.py
Demonstrates how to send commands to connected glasses. 
