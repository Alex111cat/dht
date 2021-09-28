from time import sleep
import Adafruit_DHT

gpio=4
sensor=Adafruit_DHT.DHT11

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.")
    sleep(5);

mqttc.loop_forever()