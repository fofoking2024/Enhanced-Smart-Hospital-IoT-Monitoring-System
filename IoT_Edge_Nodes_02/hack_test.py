import paho.mqtt.client as mqtt
import time

# Hacker credentials (possesses only Room 101 keys)
HACKER_ROOM = "Room101"
HACKER_PASS = "secure101"

# Malicious target (attempting to send a fake fire alert to another room)
TARGET_TOPIC = "hospital/Room102/sensors"
FAKE_PAYLOAD = '{"node_id": "Room102", "temperature": 99.9, "smoke_alert": true, "timestamp": "2026-03-07 00:00:00"}'

# Client setup
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="Hacker_Node")
client.username_pw_set(username=HACKER_ROOM, password=HACKER_PASS)

# Callback function to monitor the broker's response
def on_disconnect(client, userdata, disconnect_flags, reason_code, properties):
    print(f"\n[❌] The broker kicked us out (Disconnected)! Reason: {reason_code} - Unauthorized attempt!")

client.on_disconnect = on_disconnect

print("🕵️‍♂️ Starting simulated hack test (Lateral Movement Attack)...")
print("-" * 60)
print(f"[1] Logging in legitimately using {HACKER_ROOM} credentials...")
client.connect("127.0.0.1", 1883)
client.loop_start()
time.sleep(2)

print(f"[2] Attempting to send a fake fire alert to {TARGET_TOPIC}...")
# Attempt to publish (QoS=1 forces the broker to acknowledge)
client.publish(TARGET_TOPIC, FAKE_PAYLOAD, qos=1)

time.sleep(3)
print("-" * 60)
print("[3] Check the Node-RED Dashboard now!")
print("Did Room 102 get affected? (It should be completely safe and receive nothing).")

client.loop_stop()
client.disconnect()