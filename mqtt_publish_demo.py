# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("CoreElectronics/test", "Hello", hostname="m15.cloudmqtt.com")
publish.single("CoreElectronics/topic", "World!", hostname="m15.cloudmqtt.com")
print("Done")
 