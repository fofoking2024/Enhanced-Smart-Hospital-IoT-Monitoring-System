# 🏥 Enhanced Smart Hospital IoT Monitoring System

An advanced, secure, and real-time Industrial IoT (IIoT) solution designed for monitoring modern hospital environments. Built on a **Zero Trust Architecture**, this system ensures strict patient data privacy, absolute network isolation, and resilient defense against identity spoofing attacks.

## ✨ Features

*   **Real-time Monitoring:** Comprehensive framework simulating 5 independent hospital rooms with real-time Temperature and Smoke/Fire Detection.
*   **Zero Trust Architecture:** Strict patient data privacy, network isolation, and resilient defense against identity spoofing attacks.
*   **5-Layer Modular Architecture:** Decoupled design for scalability and fault tolerance.
*   **MQTT Communication:** Utilizes a centralized Mosquitto MQTT Broker for message distribution.
*   **Node-RED Logic:** Custom runtime logic, data extraction, and rule-based parsing for immediate decision-making.
*   **Interactive Dashboard:** Low-latency web dashboard for real-time analytics and dynamic threshold alerts.
*   **Cybersecurity:** Implements Access Control Lists (ACL) for topic-level isolation and includes penetration testing for resilience against spoofing attacks.
*   **Network Analysis:** Wireshark integration for deep packet inspection and protocol verification.

## 🏗️ System Architecture

The system’s design is strictly modular, organized into a decoupled 5-layer architecture to maximize scalability and fault tolerance:

1.  **Sensor Simulation Layer (Edge Nodes):** Multithreaded Python scripts simulating independent microcontrollers. Each node encapsulates local sensor trends and internal health telemetry.
2.  **Communication Layer (Transport):** A centralized, high-throughput **Mosquitto MQTT Broker** acting as the message distribution hub.
3.  **Security & Identity Layer (Enforcement):** Strict client authentication combined with topic-level **ACL policies** to prevent cross-room data leakage.
4.  **Processing Layer (Middleware/Logic):** **Node-RED** workspace running custom runtime logic, data extraction, and rule-based parsing.
5.  **Visualization Layer (UI/UX):** An interactive, low-latency web dashboard providing medical and technical staff with real-time analytics and dynamic threshold alerts.

### 🌐 Network & System Topology

The entire setup is simulated over a virtualized production network. Below is the comprehensive topology mapping the logical placement of edge endpoints, the central broker, the management console, and packet sniffing interfaces:

![System Architecture and Network Topology](Documentaion_05/01_system_topology.png)
*Figure 1: Comprehensive Network Architecture and Node Topology inside GNS3.*

## 💻 Technical Implementation Details

### 1. Python Edge Nodes & Data Stream

Each room operates an independent Python node powered by the `paho-mqtt` client library. The script samples environmental data, converts it into structured JSON payloads, and streams it asynchronously every 4 seconds.

*   **Payload Format:** `{"Room": 101, "Temperature": 24.5, "Smoke_Alarm": 0}`

![Python Sensors Flow](Documentaion_05/02_python_nodes.png)
*Figure 2: Execution of multithreaded Python sensor nodes and continuous JSON telemetry streaming.*

### 2. Node-RED Core Logic Workspace

Node-RED ingests raw payloads from subscribed MQTT topics. It extracts specific parameters, triggers immediate logic decisions (e.g., sound fire alarm if `Smoke_Alarm == 1`), and maps numbers seamlessly into visualization nodes.

![Node-RED Workspace Flow](Documentaion_05/03_nodered_workspace.png)
*Figure 3: Node-RED processing pipeline showing structured flows, interconnecting wires, and active debug messages.*

### 3. Real-time Monitoring Dashboard

The medical console provides dynamic real-time tracking. Color-coded gauges change behavior under critical thresholds, and history charts display continuous environmental conditions across all 5 wards.

![Real-time Monitoring Dashboard](Documentaion_05/04_hospital_dashboard.png)
*Figure 4: Production-grade real-time interactive medical monitoring dashboard.*

## 🛡️ Cybersecurity & Zero Trust Framework

### 1. Access Control Lists (ACL) Setup

To enforce strict data privacy, the network follows a **Zero Trust** model. Implicit trust is eliminated. A compromised node in Room 101 must never be able to view or corrupt data in Room 102. This is implemented via a strict, server-side `acl.txt` configuration on the Mosquitto broker, locking down read/write privileges per user.

![ACL Security Configuration](Documentaion_05/05_mosquitto_acl.png)
*Figure 5: Access Control Lists (ACL) profile enforcing explicit topic isolation on the MQTT Broker.*

### 2. Penetration Testing & Spoofing Mitigation

To test system resilience, a rogue script (`hack_test.py`) was introduced to mimic an insider threat attempting to inject a fake fire alarm into another room. Thanks to the ACL firewall, the broker immediately blocks the malicious message, drops the unauthorized connection, and shields the dashboard from fake alerts.

![Penetration Test Interception](Documentaion_05/06_attack_mitigation.png)
*Figure 6: Automated blocking and total evasion of an unauthorized injection attack.*

### 3. Wireshark Network Packet Analysis

Deep packet inspection was carried out to capture network data frames. Wireshark analysis logs confirm that raw connection requests are monitored and unauthorized subscription queries are cleanly dropped without disclosing critical backend topic hierarchies to the adversary.

![Wireshark Packet Analysis](Documentaion_05/07_wireshark_analysis.png)
*Figure 7: Protocol verification and cryptographic telemetry mapping using Wireshark.*

## ⚙️ Installation and Setup

This section outlines the steps to set up the Enhanced Smart Hospital IoT Monitoring System. Ensure you have administrative privileges for installation.

### 1. Essential Software Installation

Install the following software components. It is recommended to restart your system after installing Node.js and Python to ensure environment variables are updated.

*   **VMware Workstation Pro:** For running virtual machines.
*   **GNS3-3.0.6-all-in-one.exe:** The primary software for network simulation.
*   **GNS3 VM:** Extract the compressed file and import the OVF file into VMware.
*   **Node.js (node-v24.13.1-x64.msi):** The runtime environment for Node-RED.
*   **Mosquitto (mosquitto-2.1.2-install-windows-x64.exe):** The MQTT message broker. Install to the default path `C:\Program Files\mosquitto`.
*   **VS Code:** The main code editor.
*   **Python 3.x:** Ensure `Add Python to PATH` is enabled during installation.

### 2. Terminal Commands for Libraries and Environments

Open `CMD` as an administrator and execute the following commands:

#### a. Python Libraries

Install the `paho-mqtt` library for Python to enable MQTT communication:

```bash
pip install paho-mqtt
```

#### b. Node-RED Installation

Install Node-RED and its dashboard components:

```bash
npm install -g --unsafe-perm node-red
cd %USERPROFILE%\.node-red
npm install node-red-dashboard
```

### 3. Post-Installation Check

Verify the successful installation of each tool by running the following commands in `CMD`:

| Tool      | Check Command        | Expected Result               |
| :-------- | :------------------- | :---------------------------- |
| Python    | `python --version`   | Version number (e.g., `x.3`)  |
| Node.js   | `node -v`            | Version `v24.13.1`            |
| Mosquitto | `mosquitto -h`       | Server help instructions      |
| Node-RED  | `node-red --help`    | Program execution options     |

## ▶️ Usage

Follow these steps to run the system:

1.  **Start Mosquitto Server:**
    ```bash
net start mosquito
    ```
    Alternatively, manually start the server by opening CMD and running:
    ```bash
"C:\Program Files\mosquitto\mosquitto.exe" -v -c "C:\Program Files\mosquitto\mosquitto.conf"
    ```

2.  **Start Node-RED:**
    ```bash
node-red
    ```

3.  **Run Python Edge Nodes:**
    ```bash
python IoT_Edge_Nodes_02/room_node.py
    ```
    *(Note: The original instructions mentioned a path `D:\Enhanced_Smart_Hospital\IoT_Edge_Nodes_02\room_node.py`. Adjust the path if your repository is cloned elsewhere.)*

4.  **Access Dashboard:**
    Open your web browser and navigate to:
    *   Local Dashboard: `http://127.0.0.1:1880/ui`
    *   Node-RED Flow: `http://127.0.0.1:1880/#flow/flow1`

## 📁 Repository Structure

```text
├── IoT_Edge_Nodes_02/          # Multi-client Python scripts for sensor simulation & exploit scripts
├── Logic_and_Dashboard_03/     # Node-RED flow configuration files and Mosquitto broker rules
├── Database_Logs_04/           # Archived CSV data captures and raw Wireshark network logs (.pcapng)
├── Documentaion_05/            # Technical engineering blueprints, project slides, and high-res system figures
└── instructions.txt           # Environment deployment and quickstart execution guidelines
```

## 👨‍🔬 Author

**Engineer Fares Al-Selwi** *Electrical Engineering - Faculty of Engineering, Sana'a University*

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
