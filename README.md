# HeavyMachine Catalog

A full-stack heavy engineering equipment catalog.

- **Backend** — Python Flask REST API (in-memory, no database)
- **Frontend** — React + Vite (served as a static build via Nginx)
- **Infra** — AWS CloudFormation VPC template

---

## Project Structure

```
HeavyMachine/
├── backend/
│   ├── main.py              # Flask API — binds to 0.0.0.0:8000
│   ├── machines_data.py     # 27 machines across 12 categories
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── components/
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
├── infra/
│   └── vpc.yaml             # CloudFormation VPC stack
└── README.md
```

---

## EC2 Deployment Guide

### 1. Launch EC2 Instance

| Setting | Value |
|---|---|
| AMI | Ubuntu Server 22.04 LTS |
| Instance type | `t3.micro` |
| VPC | `main-vpc` (from `infra/vpc.yaml`) |
| Subnet | Public subnet — `public-1a` or `public-1b` |
| Auto-assign Public IP | **Enable** |
| Key pair | Create or select existing |

**Security Group inbound rules:**

| Port | Protocol | Source |
|---|---|---|
| 22 | TCP | Your IP |
| 80 | TCP | 0.0.0.0/0 |

> Port 8000 does **not** need to be public — Nginx proxies `/api` internally.

---

### 2. Connect to the Instance

```bash
ssh -i your-key.pem ubuntu@<EC2_PUBLIC_IP>
```

---

### 3. Install Dependencies

```bash
sudo apt update && sudo apt upgrade -y

# Python
sudo apt install -y python3 python3-pip

# Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Nginx + Git
sudo apt install -y nginx git
```

---

### 4. Clone the Repository

```bash
cd /home/ubuntu
git clone https://github.com/Michaelnogh/HeavyMachine.git
cd HeavyMachine
```

---

### 5. Install Backend Dependencies

```bash
cd /home/ubuntu/HeavyMachine/backend
pip3 install -r requirements.txt
```

---

### 6. Register Flask as a systemd Service

This keeps the API running in the background and restarts it automatically on reboot or crash.

```bash
sudo tee /etc/systemd/system/heavymachine.service > /dev/null <<EOF
[Unit]
Description=HeavyMachine Flask API
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/HeavyMachine/backend
ExecStart=/usr/bin/python3 main.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable heavymachine
sudo systemctl start heavymachine
```

Verify it is running:

```bash
sudo systemctl status heavymachine
```

---

### 7. Build the Frontend

```bash
cd /home/ubuntu/HeavyMachine/frontend
npm install
npm run build
```

Built files are written to `frontend/dist/`.

---

### 8. Configure Nginx

Nginx serves the React build on port 80 and forwards all `/api` requests to Flask on port 8000.

```bash
sudo tee /etc/nginx/sites-available/heavymachine > /dev/null <<'EOF'
server {
    listen 80;
    server_name _;

    root /home/ubuntu/HeavyMachine/frontend/dist;
    index index.html;

    # React app — fallback to index.html for all non-file routes
    location / {
        try_files $uri $uri/ /index.html;
    }

    # Proxy /api to Flask
    location /api {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
EOF

# Enable the site
sudo ln -s /etc/nginx/sites-available/heavymachine /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default

# Test config then reload
sudo nginx -t
sudo systemctl restart nginx
```

---

### 9. Open the App

```
http://<EC2_PUBLIC_IP>
```

---

## Updating the App

Pull new code, rebuild the frontend, and restart the backend:

```bash
cd /home/ubuntu/HeavyMachine
git pull origin main

cd frontend
npm install
npm run build

sudo systemctl restart heavymachine
```

No need to restart Nginx — it reads from `dist/` on every request.

---

## Useful Commands

```bash
# Check Flask API logs
sudo journalctl -u heavymachine -f

# Check Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# Restart services
sudo systemctl restart heavymachine
sudo systemctl restart nginx

# Test the API directly on the instance
curl http://127.0.0.1:8000/api/categories
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/machines` | All machines |
| GET | `/api/machines?category=Bulldozer` | Filter by category |
| GET | `/api/machines?search=cat` | Search by name or manufacturer |
| GET | `/api/machines/<id>` | Single machine by ID |
| GET | `/api/categories` | All category names |

---

## AWS Infrastructure

The VPC is defined in `infra/vpc.yaml` (CloudFormation).

| Resource | CIDR / Detail |
|---|---|
| VPC | `10.0.0.0/16` |
| Public subnets | `10.0.1.0/24` (1a), `10.0.2.0/24` (1b) |
| Private app subnets | `10.0.11.0/24` (1a), `10.0.12.0/24` (1b) |
| Private data subnets | `10.0.21.0/24` (1a), `10.0.22.0/24` (1b) |
| NAT Gateway | Single AZ — us-east-1a |

Redeploy the stack:

```bash
aws cloudformation deploy \
  --stack-name main-vpc \
  --template-file infra/vpc.yaml \
  --region us-east-1
```
