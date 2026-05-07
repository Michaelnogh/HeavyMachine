# HeavyMachine Catalog

A full-stack heavy engineering equipment catalog.

- **Backend** — Python Flask REST API (in-memory data, no database)
- **Frontend** — React + Vite
- **Infra** — AWS CloudFormation VPC template

---

## Project Structure

```
HeavyMachine/
├── backend/
│   ├── main.py              # Flask API
│   ├── machines_data.py     # 27 machines, 12 categories
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── components/      # CategoryFilter, SearchBar, MachineCard,
│   │                        # MachineDetails, ImageGallery, SpecsTable
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
├── infra/
│   └── vpc.yaml             # CloudFormation VPC stack
├── start.ps1                # Windows local dev launcher
└── README.md
```

---

## Run Locally (Windows)

### Prerequisites
- Python 3.10+
- Node.js 18+

### Backend
```powershell
cd backend
pip install -r requirements.txt
python main.py
# API available at http://localhost:8000
```

### Frontend
```powershell
cd frontend
npm install
npm run dev
# App available at http://localhost:5173
```

Or run both at once:
```powershell
.\start.ps1
```

---

## Deploy on AWS EC2

### 1. Launch an EC2 Instance

| Setting | Value |
|---|---|
| AMI | Ubuntu Server 22.04 LTS |
| Instance type | `t3.micro` (free tier eligible) |
| VPC | Use the `main-vpc` created by `infra/vpc.yaml` |
| Subnet | Any **public** subnet (`public-1a` or `public-1b`) |
| Auto-assign Public IP | **Enable** |
| Key pair | Create or select an existing key pair |

**Security Group — open these ports:**

| Port | Protocol | Source | Purpose |
|---|---|---|---|
| 22 | TCP | Your IP | SSH |
| 80 | TCP | 0.0.0.0/0 | HTTP (Nginx → React) |
| 8000 | TCP | 0.0.0.0/0 | Flask API (optional, can be proxied) |

---

### 2. SSH into the Instance

```bash
ssh -i your-key.pem ubuntu@<EC2_PUBLIC_IP>
```

---

### 3. Install System Dependencies

```bash
sudo apt update && sudo apt upgrade -y

# Python
sudo apt install -y python3 python3-pip

# Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Nginx
sudo apt install -y nginx

# Git
sudo apt install -y git
```

---

### 4. Clone the Repository

```bash
git clone https://github.com/Michaelnogh/HeavyMachine.git
cd HeavyMachine
```

---

### 5. Set Up the Backend

```bash
cd backend
pip3 install -r requirements.txt
```

Create a systemd service so Flask starts automatically:

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
```

Enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable heavymachine
sudo systemctl start heavymachine

# Verify it is running
sudo systemctl status heavymachine
```

---

### 6. Build the Frontend

```bash
cd /home/ubuntu/HeavyMachine/frontend
npm install
npm run build
# Built files are output to frontend/dist/
```

---

### 7. Configure Nginx

Nginx will serve the built React app on port 80 and forward `/api` requests to Flask on port 8000.

```bash
sudo tee /etc/nginx/sites-available/heavymachine > /dev/null <<EOF
server {
    listen 80;
    server_name _;

    # Serve the React build
    root /home/ubuntu/HeavyMachine/frontend/dist;
    index index.html;

    # All non-API routes go to React (handles client-side routing)
    location / {
        try_files \$uri \$uri/ /index.html;
    }

    # Proxy /api requests to Flask
    location /api {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOF
```

Enable the site and restart Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/heavymachine /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
```

---

### 8. Open the App

Navigate to your EC2 public IP in a browser:

```
http://<EC2_PUBLIC_IP>
```

The React catalog will load and fetch machine data from Flask at `/api`.

---

### 9. Updating the App

To deploy new changes from GitHub:

```bash
cd /home/ubuntu/HeavyMachine
git pull origin main

# Rebuild frontend
cd frontend && npm install && npm run build

# Restart backend
sudo systemctl restart heavymachine
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

The VPC is defined in `infra/vpc.yaml` and deployed as a CloudFormation stack.

| Resource | Detail |
|---|---|
| VPC CIDR | `10.0.0.0/16` |
| Public subnets | `10.0.1.0/24` (1a), `10.0.2.0/24` (1b) |
| Private app subnets | `10.0.11.0/24` (1a), `10.0.12.0/24` (1b) |
| Private data subnets | `10.0.21.0/24` (1a), `10.0.22.0/24` (1b) |
| NAT Gateway | Single AZ (us-east-1a) |

To redeploy the stack:

```bash
aws cloudformation deploy \
  --stack-name main-vpc \
  --template-file infra/vpc.yaml \
  --region us-east-1
```
