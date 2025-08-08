# FlaskBackdoor - Malicious
![vlcsnap-7622090](https://github.com/user-attachments/assets/496ec9cd-1302-45e2-93d7-8483f59f6f94)

This project demonstrates a **malicious script injection** into a Flask-based web application via an insecure CI/CD pipeline using Jenkins.

> **Author:** Appar Thebe  
> **Educational Use Only**

## Purpose

To show how attackers can exploit unsecured DevOps pipelines (like Jenkins) to introduce unauthorized routes into Flask applications **without modifying the Git repository**. This can allow backdoors or other hidden features to be deployed into production.

---

##  Attack Summary

- A new `/hack` route is injected into the Flask app dynamically during the Jenkins pipeline build.
- This route returns a malicious message without the code being present in version control.
- The exploit simulates an **insider or automation-based attack**.

## 🛠️ Files

- `main.py` - Core Flask app modified to include a backdoor.
- `Dockerfile` - Docker instructions for building the image.
- `requirements.txt` - Python dependencies.

## How to Run (Locally)

```bash
# Build the Docker image
sudo docker build -t flask-app .

# Run the container
sudo docker run -d -p 5000:5000 flask-app
```

Access the malicious route:
```
http://localhost:5000/hack
```

---

##  Educational Takeaway

This project highlights:

- The risks of **improper access control** in CI/CD pipelines.
- How **build-time tampering** can bypass traditional source code reviews.
- The need for **artifact integrity validation** and **secure Jenkins configurations**.

---
Hacker Screenshot 
![Screenshot 2025-05-01 172759](https://github.com/user-attachments/assets/66a3d22f-c01f-470b-a9da-f936aae2419a)

## Disclaimer

This is for academic and ethical research purposes only. Do not attempt unauthorized attacks on real-world systems. Goes for testing.
