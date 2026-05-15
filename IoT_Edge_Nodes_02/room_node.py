import paho.mqtt.client as mqtt
import time
import random
import json

BROKER_ADDRESS = "127.0.0.1"
PORT = 1883

ROOMS = ["Room101", "Room102", "Room103", "Room104", "Room105"]

# التغيير الأول: إضافة قاموس (Dictionary) يحتوي على بيانات الاعتماد لكل غرفة
# تحديث بيانات الاعتماد لتطابق ملف passwords.txt
CREDENTIALS = {
    "Room101": "secure101",
    "Room102": "secure102",
    "Room103": "secure103",
    "Room104": "secure104",
    "Room105": "secure105"
}

clients = {}

# إنشاء عملاء MQTT لكل غرفة
for room in ROOMS:
    # التعديل هنا: تحديد إصدار الـ API (VERSION2) لإخفاء التحذير (DeprecationWarning)
    clients[room] = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=f"{room}_Node")
    
    # التغيير الثاني: حقن اسم المستخدم وكلمة المرور قبل بدء الاتصال
    clients[room].username_pw_set(username=room, password=CREDENTIALS[room])

def connect_clients():
    for room, client in clients.items():
        try:
            client.connect(BROKER_ADDRESS, PORT)
            client.loop_start()
            # التغيير الثالث: تعديل رسالة الطباعة لتأكيد أن الاتصال أصبح آمناً
            print(f"[+] Connected {room} to MQTT Broker securely 🔒")
        except Exception as e:
            print(f"[-] Connection failed for {room}. Error: {e}")

def generate_sensor_data(room_id):
    temperature = round(random.uniform(20.0, 25.0), 2)
    smoke_detected = random.choice([False, False, False, False, False, True])
    data = {
        "node_id": room_id,
        "temperature": temperature,
        "smoke_alert": smoke_detected,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    return json.dumps(data)

if __name__ == "__main__":
    connect_clients()
    print("Starting secure hospital room sensors... Press Ctrl+C to stop.")
    print("-" * 60)
    try:
        while True:
            for room in ROOMS:
                payload = generate_sensor_data(room)
                topic = f"hospital/{room}/sensors"
                clients[room].publish(topic, payload)
                print(f"Published to {topic}: {payload}")
            time.sleep(4)
    except KeyboardInterrupt:
        print("\nSimulation stopped. Disconnecting...")
        for client in clients.values():
            client.loop_stop()
            client.disconnect()
