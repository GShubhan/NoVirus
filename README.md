# 🛡 NoVirus - Multi-Engine Malware Scanner

A lightweight malware detection tool that monitors local downloads and checks file hashes against **VirusTotal’s multi-engine threat intelligence platform (70+ antivirus engines, 10+ sandboxes).**

---

## 🔍 Overview

NoVirus continuously monitors the `C:\Downloads` directory, extracts file hashes (MD5, SHA1, SHA256), and queries the VirusTotal API to retrieve:

- Detection results from 70+ antivirus engines  
- Dynamic sandbox analysis reports  
- Threat reputation context  
- Malicious detection count summary  

If a file is flagged, the system generates:
- A structured threat report  
- A visual pie chart of detection distribution  
- An alert highlighting scanner consensus  

---

## 🛠 Tech Stack

- **Python**
- VirusTotal Public API
- Hashing (MD5 / SHA1 / SHA256)
- Matplotlib (Detection visualization)

---

## ⚙️ How It Works

1. Monitor `Downloads` directory  
2. Generate file hash  
3. Query VirusTotal API  
4. Parse detection metadata  
5. Generate structured report + visualization  

---

## 🚀 Future Improvements

- Background daemon mode (scan every 5 minutes)
- Automatic quarantine or deletion option
- Optional file upload for unknown hashes (with user consent)
- Threat history logging
- Email/webhook alerts

---

## 📌 Motivation

Built to explore API-driven threat intelligence systems and understand how multi-engine malware detection platforms operate.
