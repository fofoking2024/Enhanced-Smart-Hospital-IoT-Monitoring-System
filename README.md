# 🏥 Enhanced Smart Hospital IoT Monitoring System

An advanced, secure, and real-time IoT solution for monitoring hospital environments, built with a **Zero Trust Architecture** to ensure patient data privacy and system integrity.

## 📋 Project Overview
This project simulates a smart hospital environment where 5 independent rooms are monitored for **Temperature** and **Smoke Detection**. It bridges the gap between network simulation (GNS3) and industrial IoT protocols (MQTT).

## 🏗️ System Architecture (The 5 Layers)
The system is built on a robust five-layer engineering framework:
1. **Sensor Simulation Layer:** Python-based edge nodes simulating real-time room data.
2. **Communication Layer:** Centralized MQTT Broker (Mosquitto) for efficient data flow.
3. **Security & Identity Layer:** Strict Authentication and **ACL (Access Control Lists)**.
4. **Processing Layer:** Node-RED flows for data parsing and logic execution.
5. **Visualization Layer:** Interactive real-time Dashboards for medical staff.

## 🛡️ Key Engineering Features
- **Zero Trust Security:** No implicit trust. Every node must authenticate.
- **Data Isolation:** Room 101 cannot access or spoof data for Room 102, enforced via ACL policies.
- **Cybersecurity Resilience:** Successfully tested against "Identity Spoofing" attacks, verified by **Wireshark** packet analysis.
- **Forensic Logging:** Automated data archiving in CSV format for medical and technical audits.

## 🛠️ Tech Stack
- **Programming:** Python (Eclipse Paho MQTT API)
- **Middleware:** Mosquitto MQTT Broker
- **Logic & UI:** Node-RED & Node-RED Dashboard
- **Network Simulation:** GNS3 & VMware Workstation
- **Analysis:** Wireshark (Packet Sniffing & Protocol Analysis)

## 📁 Repository Structure
- `IoT_Edge_Nodes_02/`: Python scripts for room simulation and security testing.
- `Logic_and_Dashboard_03/`: Node-RED flows and MQTT configuration files.
- `Database_Logs_04/`: Sample archived data and network capture files (.pcapng).
- `Documentaion_05/`: Technical reports, system topology, and diagrams.

## 👨‍🔬 Author
**Engineer Fares Al-Selwi** *Electrical Engineering - Sana'a University*
