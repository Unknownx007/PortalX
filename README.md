# ☠️ DEDSEC CAPTIVE PORTAL GATEWAY FRAMEWORK

```text
  __________________________________________________________________________
  < Wake up user... Your pathetic little network data belongs to DEDSEC now. >
  --------------------------------------------------------------------------
         \   ^__^
          \  ()()_______
             (__)\       )\/\
                U  ||----w |
                   ||     ||

    AUTOMATED BY SYSTEM DEVELOPER: Unknownx007
```

## 📝 Description & Overview

This automated wireless network exploration framework is engineered for native deployment on Kali Linux setups. Built around dynamic routing parameters and advanced local socket handling, the tool completely avoids rigid dependencies and hardcoded static paths. It allows operators to deploy an immediate local captive credential collection gateway on any internet domain or local subnet infrastructure—whether auditing a simulated enterprise profile, a public hotspot, or a router firmware update cell.

By integrating custom DNS wildcard spoofing layers alongside an automated, non-blocking HTTP socket engine, the tool intercepts in-flight connectivity checks executed by connected client devices. It force-triggers an automatic web pop-up screen natively across mobile and desktop platforms. Input credentials are captured instantly in raw plaintext, passed directly onto an integrated SQLite data vault, and streamed to the operator's active console monitor screen in real time.

---

## ⚙️ Operational Workflow & Core Engine Components

The framework operates cleanly across three isolated protocol phases:

*   **Step 1: Rogue Access Point and DHCP Lease Pool Setup**
    The framework programmatically interacts with native low-level wireless sub-daemons (`hostapd` and `dnsmasq`) to switch a local Wi-Fi interface card into an open network cell while simultaneously deploying a dynamic DHCP pool to handle client device IP address leases.
*   **Step 2: Wildcard DNS Spoofing & HTTP Intercept Hijack**
    An internal asynchronous UDP engine listens actively on Port 53, resolving all inbound vendor connectivity checks to the operator's local interface IP address. Concurrently, a multi-threaded TCP socket on Port 80 checks incoming paths, force-redirecting client probes using an active `302 Found` token.
*   **Step 3: Real-Time Token Parameter Parsing Matrix**
    The raw payload data strings submitted via the gateway form are isolated using a native Python URL parameter decoder engine. This completely suppresses background telemetry noise, identifies the exact client device hardware vendor profile, and streams verified plaintext tokens to the dashboard.

---

## 🛠️ Installation & Environment Configuration

Ensure your system's network driver configurations are fully up-to-date before launching the initialization blocks.

### 1. Configure System Dependencies
```bash
sudo apt-get update -y
sudo apt-get install -y hostapd dnsmasq iptables python3-pip
pip3 install beautifulsoup4 (make a venv if you struggel to install it)
```

### 2. Workspace Deployment
```bash
git clone https://github.com/Unknownx007/PortalX
cd Portalx
```

### 3. Execution Pipeline
```bash
sudo python3 portalx.py
```

---

## 📂 Custom Template Integration & Form Weaponization

The platform features a built-in **Custom HTML Ingestion Engine** that automates the weaponization of any offline template page globally.

### Ingestion Requirements:
1. Place your target website login or signup clone file (`.html`) inside the directory: **`templates/`** (e.g., create `templates/login.html`).
2. When launching the script, enter option **`2`** (Web Listeners Post), select template selection option **`2`** (Inject Custom Ingestion Template Vector), and provide the file path: `templates/login.html`.

### Automated DOM Modification:
*   The framework automatically parses the document object model using an internal parser, forcefully updating all HTML `<form>` targets to execute a `/login` `POST` request to your local listener.
*   The first available text/email and password fields are aligned automatically to match the backend parser registry structures (`user` and `pass`).
*   Upon input submission, the tool logs the plaintext tokens live on your screen and smoothly redirects the target device's browser directly to **`https://google.com`**.

---

## 📄 License & Regulatory Compliance

### MIT License
Copyright (c) 2026 Unknownx007

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

---

## ⚖️ Legal & Ethical Usage Notice
**Disclaimer:** This software development repository card is built solely for authorized security auditing, defensive gap analysis, wireless system vulnerability research, and environment compliance tracking. Executing active scanning or wireless credential hijacking sequences against unauthorized production targets without explicit, written mutual contractual permission is strictly prohibited. The framework author assumes zero legal accountability for environmental system downtime or programmatic misuse.
