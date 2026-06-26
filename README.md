<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=170&color=0:0ea5e9,100:6366f1&text=Dai%20Thang&fontAlign=50&fontAlignY=35&fontSize=45&fontColor=ffffff&desc=DevOps%20%7C%20DevSecOps%20%7C%20Cloud-native%20Engineering&descAlign=50&descAlignY=58&descSize=16" />

[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-0ea5e9?style=for-the-badge\&logo=vercel\&logoColor=white)](https://daithang-portfolio-672q.onrender.com/)
[![Email](https://img.shields.io/badge/Email-Contact-ea4335?style=for-the-badge\&logo=gmail\&logoColor=white)](mailto:daithanghuynhle@gmail.com)
[![Facebook](https://img.shields.io/badge/Facebook-hldaithangg-1877f2?style=for-the-badge\&logo=facebook\&logoColor=white)](https://facebook.com/hldaithangg)

</div>

---

## About

* UIT student from Vietnam
* Currently focusing on **DevOps / DevSecOps / Cloud-native Engineering**
* Backend & full-stack foundation with experience in **microservices**, **security**, and **database design**
* Interested in **CI/CD**, **Kubernetes**, **GitOps**, **cloud infrastructure**, **observability**, and **security automation**

---

## Tech Stack & Tools I Work With

<div align="center">

### DevOps / Cloud / Infrastructure

![Linux](https://img.shields.io/badge/Linux-fcc624?style=for-the-badge\&logo=linux\&logoColor=111111)
![Docker](https://img.shields.io/badge/Docker-2496ed?style=for-the-badge\&logo=docker\&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326ce5?style=for-the-badge\&logo=kubernetes\&logoColor=white)
![Helm](https://img.shields.io/badge/Helm-0f1689?style=for-the-badge\&logo=helm\&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-844fba?style=for-the-badge\&logo=terraform\&logoColor=white)
![OpenTofu](https://img.shields.io/badge/OpenTofu-ffda18?style=for-the-badge\&logo=opentofu\&logoColor=111111)
![AWS](https://img.shields.io/badge/AWS-ff9900?style=for-the-badge\&logo=amazonaws\&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285f4?style=for-the-badge\&logo=googlecloud\&logoColor=white)

### CI/CD / DevSecOps / Observability

![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088ff?style=for-the-badge\&logo=githubactions\&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-d24939?style=for-the-badge\&logo=jenkins\&logoColor=white)
![Argo CD](https://img.shields.io/badge/Argo%20CD-ef7b4d?style=for-the-badge\&logo=argo\&logoColor=white)
![SonarQube](https://img.shields.io/badge/SonarQube-4e9bcd?style=for-the-badge\&logo=sonarqube\&logoColor=white)
![Trivy](https://img.shields.io/badge/Trivy-1904da?style=for-the-badge\&logo=aqua\&logoColor=white)
![Gitleaks](https://img.shields.io/badge/Gitleaks-111111?style=for-the-badge\&logo=git\&logoColor=white)
![Cilium](https://img.shields.io/badge/Cilium-f8c517?style=for-the-badge\&logo=cilium\&logoColor=111111)
![Prometheus](https://img.shields.io/badge/Prometheus-e6522c?style=for-the-badge\&logo=prometheus\&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-f46800?style=for-the-badge\&logo=grafana\&logoColor=white)

### Backend / Database

![TypeScript](https://img.shields.io/badge/TypeScript-3178c6?style=for-the-badge\&logo=typescript\&logoColor=white)
![NestJS](https://img.shields.io/badge/NestJS-e0234e?style=for-the-badge\&logo=nestjs\&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6db33f?style=for-the-badge\&logo=springboot\&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169e1?style=for-the-badge\&logo=postgresql\&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-dc382d?style=for-the-badge\&logo=redis\&logoColor=white)
![MinIO](https://img.shields.io/badge/MinIO-c72e49?style=for-the-badge\&logo=minio\&logoColor=white)

</div>

---

## Featured Projects

### SageLMS — AI-powered LMS with DevSecOps Pipeline

Microservices-based LMS with AI Tutor, API Gateway, service-based architecture, Docker/Kubernetes direction, and DevSecOps validation pipeline.

`Spring Boot` • `FastAPI` • `React` • `PostgreSQL + pgvector` • `Redis` • `Docker` • `Kubernetes` • `GitHub Actions` • `OpenTofu` • `Trivy` • `Checkov` • `SonarCloud`

* Built microservices for auth, courses, content, progress, assessment, AI tutor, and worker processing
* Designed CI quality gates with secret scanning, testing, Docker build/scan, IaC validation, and code quality checks
* Worked with cloud/infrastructure automation using OpenTofu and GitHub Actions

[Repository](https://github.com/daithang59/sagelms)

---

### DocVault — Secure Document Management Platform

Enterprise-style document management system with microservices, RBAC, approval workflow, object storage, and tamper-proof audit logging.

`Next.js` • `NestJS` • `PostgreSQL` • `Prisma` • `Keycloak` • `MinIO` • `Docker` • `GitHub Actions` • `Gitleaks`

* Built secure document lifecycle: create → upload → review → publish → archive
* Implemented role-based access, classification rules, ACL, audit trail, and workflow approval
* Added E2E checks for authorization, malware upload blocking, DLP behavior, audit access, and compliance flow

[Repository](https://github.com/daithang59/docvault)

---

### EKS Cilium Benchmark — Kubernetes Networking Benchmark

Benchmark project comparing Kubernetes service datapath performance between kube-proxy baseline and Cilium eBPF kube-proxy replacement on AWS EKS.

`AWS EKS` • `Terraform` • `Helm` • `Kubernetes` • `Cilium` • `eBPF` • `Fortio` • `Prometheus` • `Grafana` • `Hubble`

* Provisioned EKS infrastructure with Terraform
* Compared kube-proxy iptables baseline vs Cilium eBPF kube-proxy replacement
* Designed benchmark scenarios for service baseline, high-load connection churn, and NetworkPolicy overhead
* Collected evidence through benchmark logs, metadata, Kubernetes state, metrics, and observability tools

[Repository](https://github.com/daithang59/NT531_EKS-Cilium-Kubeproxy-Benchmark)

---

### Other Projects

* **VLeague Management System** — football league management platform with RBAC, match scheduling, reports, Docker Compose and CI/CD baseline
  [Repository](https://github.com/daithang-organization/SE104_VLEAGUE)

* **MentorMe Web/Mobile** — mentor/mentee platform with scheduling, realtime chat, video call, and mobile app
  [Web](https://github.com/kaing615/MentorMe) • [Mobile](https://github.com/kaing615/MentorMe-Mobile-App)

---

## Project Cards

<div align="center">

<a href="https://github.com/daithang59/sagelms">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=daithang59&repo=sagelms&theme=tokyonight&hide_border=true" />
</a>

<a href="https://github.com/daithang59/docvault">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=daithang59&repo=docvault&theme=tokyonight&hide_border=true" />
</a>

<a href="https://github.com/daithang59/NT531_EKS-Cilium-Kubeproxy-Benchmark">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=daithang59&repo=NT531_EKS-Cilium-Kubeproxy-Benchmark&theme=tokyonight&hide_border=true" />
</a>

<a href="https://github.com/daithang-organization/SE104_VLEAGUE">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=daithang-organization&repo=SE104_VLEAGUE&theme=tokyonight&hide_border=true" />
</a>

</div>

---

## Engineering Footprint

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=daithang59&show_icons=true&theme=tokyonight&hide_border=true" height="165" />
<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=daithang59&layout=compact&theme=tokyonight&hide_border=true" height="165" />

<br />

<img src="https://streak-stats.demolab.com?user=daithang59&theme=tokyonight&hide_border=true" />

<br />

<img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=daithang59&theme=tokyonight" />

</div>

---

## Contribution Snake

<div align="center">

<img src="https://raw.githubusercontent.com/daithang59/daithang59/output/github-contribution-grid-snake.svg" alt="github contribution snake" />

</div>

---

## Contact

* Portfolio: [daithang-portfolio-672q.onrender.com](https://daithang-portfolio-672q.onrender.com/)
* Email: [daithanghuynhle@gmail.com](mailto:daithanghuynhle@gmail.com)
* Facebook: [hldaithangg](https://facebook.com/hldaithangg)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:6366f1,100:0ea5e9" />

</div>
