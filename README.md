# HeavyMachine Catalog

A full-stack heavy engineering equipment catalog.

- **Backend** — Python Flask REST API (in-memory, no database)
- **Frontend** — React + Vite (dev server)
- **Infra** — AWS CloudFormation VPC template

---

## Project Structure

```
HeavyMachine/
├── backend/
│   ├── main.py              # Flask API
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

## Run on EC2

### 1. Launch EC2 Instance

| Setting | Value |
|---|---|
| AMI | Ubuntu Server 22.04 LTS |
| Instance type | `t3.micro` |
| Subnet | Any public subnet |
| Auto-assign Public IP | **Enable** |

**Security Group — open these ports:**

| Port | Purpose |
|---|---|
| 22 | SSH |
| 5173 | Vite dev server (frontend) |
| 8000 | Flask API (backend) |

---

### 2. Connect

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

### 5. Run the Backend

```bash
cd backend
pip3 install -r requirements.txt
python3 main.py
```

Flask runs on `http://0.0.0.0:8000`

---

### 6. Run the Frontend

Open a second terminal (or use `tmux`):

```bash
ssh -i your-key.pem ubuntu@<EC2_PUBLIC_IP>
cd HeavyMachine/frontend
npm install
npm run dev
```

Vite runs on `http://0.0.0.0:5173`

---

### 7. Open the App

```
http://<EC2_PUBLIC_IP>:5173
```

---

## Using tmux (run both in one session)

```bash
# Install tmux
sudo apt install -y tmux

# Start a session
tmux new -s app

# Run backend
cd ~/HeavyMachine/backend && python3 main.py

# Split pane  (Ctrl+B then %)
# Run frontend in the new pane
cd ~/HeavyMachine/frontend && npm run dev

# Detach from session: Ctrl+B then D
# Reattach later:
tmux attach -t app
```

---

## Updating the App

```bash
cd ~/HeavyMachine
git pull origin main

# Restart backend (Ctrl+C then)
python3 backend/main.py

# Restart frontend (Ctrl+C then)
npm run dev --prefix frontend
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

Redeploy:

```bash
aws cloudformation deploy \
  --stack-name main-vpc \
  --template-file infra/vpc.yaml \
  --region us-east-1
```
