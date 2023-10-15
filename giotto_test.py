import math
import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt
import time

def send():
    broker = '' #change this as needed
    ssid = 'Tufts_Wireless'
    password = ''
    topic_pub = '' #publishing to this topic

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
    print('Connected to WiFi')

    def whenCalled(topic, msg):
        print((topic.decode(), msg.decode()))

    fred = mqtt.MQTTClient('Nick Send', broker, keepalive=600)
    fred.connect()

# Define constants
d = 1.0  # Diameter of the circle
arm = d  # Length of each arm

num_points = 70 # Number of points on the circle
all_angles = [] # Collects all angle tuples into a list

for i in range(num_points):
    # Calculate the angle for the current point on the circle
    angle = 2 * math.pi * i / num_points

    # Rounds the values and converts from radians to degrees
    theta1 = round(math.degrees(theta1),2)
    theta2 = round(math.degrees(theta2),2)

    # Add the angles into a tuple; appends to list
    angles = (theta1, theta2)
    all_angles.append(angles)

    # Print the results
    print("Target Position (x, y):", x, y)
    print("Joint Angle 1 (theta1):", theta1, "degrees")
    print("Joint Angle 2 (theta2):", theta2, "degrees")




