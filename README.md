# SmartExtenderAI

## Project Status

**Current Status:** Data Collection & Analysis Complete

### Completed

- [x] ESP32 Beacon Node
- [x] ESP32 Receiver Node
- [x] RSSI Data Collection
- [x] Data Processing Pipeline
- [x] Statistical Analysis
- [x] Data Visualisation

### In Progress

- [ ] Machine Learning Classification
- [ ] Edge AI Deployment
- [ ] Predictive Maintenance Models
## Overview

SmartExtenderAI is an Edge AI and IoT project designed to identify optimal Wi-Fi extender placement locations using real-time RSSI (Received Signal Strength Indicator) measurements collected by ESP32-S3 microcontrollers.

The system consists of two ESP32-S3 devices:

* **Beacon Node** – broadcasts a dedicated Wi-Fi access point.
* **Receiver Node** – scans for the beacon signal and records RSSI measurements over time.

Collected signal data is analysed using Python, Pandas and Matplotlib to identify the optimal Wi-Fi extender placement location within a residential environment. Statistical features including mean RSSI, minimum RSSI, maximum RSSI and standard deviation are extracted from multiple experimental runs and visualised to support data-driven placement decisions. Enhancing all of this with the use of Edge AI, predictive maintenance concepts and machine learning.

The project demonstrates the integration of:

* IoT Sensor Networks
* Wireless Signal Analysis
* Edge AI
* Predictive Maintenance Concepts
* Data Analytics and Visualisation

---

## Project Objectives

### Primary Objective

Identify the optimal location for a Wi-Fi extender by analysing wireless signal strength measurements collected from multiple locations.

### Secondary Objectives

* Build a wireless sensing system using ESP32-S3 devices.
* Create a repeatable RSSI data collection methodology.
* Analyse network performance using Python.
* Develop machine learning models for location classification.
* Investigate predictive maintenance techniques for network health monitoring.
* Explore Edge AI deployment strategies for local decision-making.

---

## System Architecture

```text
ESP32 Beacon
      │
      │ Wi-Fi Broadcast
      ▼
ESP32 Receiver
      │
      │ RSSI Collection
      ▼
CSV Dataset
      │
      ▼
Python Data Pipeline
      │
      ├── Pandas
      ├── NumPy
      └── Matplotlib
      │
      ▼
Feature Engineering
      │
      ▼
Machine Learning Models
      │
      ▼
Location Classification &
Predictive Maintenance
```

---

## Data Collection Workflow

### Step 1 – Beacon Deployment

The Beacon ESP32-S3 broadcasts a dedicated Wi-Fi network.

Example:

SSID: Kitchen_Test

The beacon remains fixed during all experiments to ensure consistent measurements.

---

### Step 2 – RSSI Acquisition

The Receiver ESP32-S3 continuously scans for the beacon SSID and records:

* Timestamp
* RSSI (dBm)
* Channel Number
* Scan Number

Example:

```csv
timestamp,rssi
0,-64
1,-66
2,-65
3,-68
```

---

### Step 3 – Data Storage

Collected measurements are exported to CSV format for further analysis.

Datasets are collected from multiple candidate extender locations including:

* Kitchen
* Sitting Room
* Hallway
* Landing
* Bedroom

---

## Data Analysis

Python is used to clean, transform and analyse collected RSSI datasets.

### Libraries

* Pandas
* NumPy
* Matplotlib

### Calculated Features

For each location:

* Mean RSSI
* Minimum RSSI
* Maximum RSSI
* Standard Deviation
* Signal Stability Score

Example:

| Location | Mean RSSI | Std Dev |
| -------- | --------- | ------- |
| Kitchen  | -65       | 2       |
| Hallway  | -71       | 6       |
| Bedroom  | -80       | 10      |

Lower variability and stronger average signal indicate more suitable extender locations.

---

## Visualisation

Matplotlib is used to generate:

* RSSI Time-Series Graphs
* Signal Distribution Histograms
* Location Comparison Charts
* Signal Stability Analysis

Example outputs include:

* RSSI vs Time
* Average RSSI by Location
* Signal Variability Comparison

---

## Machine Learning

### Classification Problem

The objective is to classify candidate locations into:

* Optimal
* Acceptable
* Poor

### Input Features

* Mean RSSI
* RSSI Standard Deviation
* Minimum RSSI
* Maximum RSSI
* Packet Loss Percentage

### Output Labels

```text
Optimal
Acceptable
Poor
```

### Models

#### Decision Tree Classifier

Used for explainable decision-making and rule extraction.

#### Random Forest Classifier

Used to improve classification accuracy and reduce overfitting.

#### K-Nearest Neighbours (KNN)

Used as a baseline classification model.

---

## Predictive Maintenance

A secondary objective is to monitor long-term network health.

Historical RSSI measurements can be analysed to identify:

* Signal degradation
* Environmental interference
* Network instability
* Potential infrastructure issues

### Predictive Models

* Linear Regression
* Random Forest Regression

These models can forecast future signal quality and provide maintenance recommendations.

Example:

```text
Warning:
Signal quality predicted to fall below acceptable threshold within 14 days.
```

---

## Edge AI

Future development will investigate deploying lightweight inference models directly on ESP32 hardware.

Potential approaches:

* TensorFlow Lite
* TensorFlow Lite Micro
* Edge Impulse

This enables local decision-making without requiring cloud infrastructure.

Example:

```text
Location Score: 92%

Recommendation:
Place Wi-Fi extender at current location.
```

---

## Technology Stack

### Hardware

* ESP32-S3 Beacon Node
* ESP32-S3 Receiver Node
* PC for data analysis

### Embedded Software

* MicroPython
* Thonny IDE

### Data Science

* Python
* Pandas
* NumPy
* Matplotlib

### Machine Learning

* Scikit-Learn

### Future Edge AI

* TensorFlow Lite
* TensorFlow Lite Micro
* Edge Impulse

---

## Skills Demonstrated

* Python Programming
* Embedded Systems
* IoT Development
* Wireless Networking
* Data Analysis
* Machine Learning
* Edge AI Concepts
* Predictive Maintenance
* Data Visualisation
* Experimental Design

---

## Future Enhancements

* Real-time dashboard
* MQTT integration
* TinyML deployment
* Automated extender placement recommendations
* Multi-beacon signal triangulation
* Network anomaly detection
* Edge-based inference on ESP32 devices

---

## License

MIT License
