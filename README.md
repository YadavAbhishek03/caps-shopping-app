# 🛒 Shopping App Deployment on AWS EKS manually

This project demonstrates how to containerize and deploy a simple shopping app on **Amazon EKS** (Elastic Kubernetes Service) with a **custom VPC**, subnets, route tables, and public access — all.

---

## 🧰 Tech Stack

- AWS (EKS, ECR,
- Docker
- Kubernetes (`kubectl`)
- Python HTTP Server (serving static files)

---

## 📁 Project Structure

eks_shopping_app/
├── app/
│ ├── app.py
│ └── static/
└── README.md



---

## 🚀 Step-by-Step Deployment

### 1️⃣ Clone the Project

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO


## Build & Push Docker Image to Amazon ECR

# Authenticate Docker to your ECR
aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com

# Build your image
docker build -t caps-shopping-app .

# Tag it for ECR
docker tag caps-shopping-app:latest <ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com/caps-shopping-app:latest

# Push to ECR
docker push <ACCOUNT_ID>.dkr.ecr.ap-south-1.amazonaws.com/caps-shopping-app:latest


## Create EKS Infrastructure 

eksctl create cluster \
  --name shopping-cluster \
  --region ap-south-1 \
  --nodegroup-name shopping-nodes \
  --node-type t3.medium \
  --nodes 2 \
  --managed



### 4️ Connect to EKS

aws eks update-kubeconfig --region ap-south-1 --name shopping-eks-cluster

## Deploy App to EKS

kubectl apply -f deployment.yml
kubectl apply -f service.yml

# Verify pods and service
kubectl get pods
kubectl get svc

## Find the EXTERNAL-IP of your shopping-service, and open in browser:

http://<external-lb-dns>


📌 Notes
Ensure your image's container listens on port 8000.

The service maps port 80 → 8000 internally.

All traffic is routed through a LoadBalancer provisioned by Kubernetes.

💬 Author
Abhishek Yadav
GitHub: @YadavAbhishek03
Project: caps-shopping-app

🔗 Tags
#AWS #EKS #Kubernetes #DevOps #Docker #CloudNative


---

✅ Let me know if you'd like me to:
- Add diagrams or visuals
- Publish this on your GitHub for you
- Create a `.gitignore` now too
