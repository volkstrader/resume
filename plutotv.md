# Enterprise Platform team
## Intro

## Background

## Highlight

## Impact

---
# SWAT Team  

## Introduction  
The SWAT Team is a temporary engineering organization formed to support high-priority cross-team initiatives.  

## Background  
The team was tasked with migrating service infrastructure from AWS EC2/ECS to EKS to achieve:  
- **Cost Optimization:** Reducing operational expenses.  
- **Multi-Cloud Deployment:** Enabling a more flexible and scalable cloud architecture.  

## Highlights  

### **Collaboration with DevOps**  
- Developed Kubernetes standards for Go microservices:  
  - **ConfigMap Integration:** Enabled live updates for service configuration.  
  - **Secret Management:** Synchronized HashiCorp Vault secrets with Kubernetes Secret Store using ExternalSecrets.  
  - **CI/CD Standardization:** Created a standardized GitHub Action build workflow for Go microservices.  

### **Micro-Libraries Development**  
- Refactored the monolithic core library into focused micro-libraries with clear responsibilities.  

### **Code Generation (Codegen) Tooling**  
- Automated the generation of boilerplate code and project artifacts, including:  
  - Secret and dependency wiring.  
  - Non-Go files like Makefiles, GitHub Action YAMLs, Dockerfiles, Helm charts, and config files.  

### **Development Lifecycle Reform**  
- Replaced GitFlow with the **Release-First Branching Strategy:**  
  - Published detailed documentation on the new process.  
  - Promoted and assisted other teams in adopting the updated workflow.  

## Impact  
- **Faster Migrations:** Reduced service migration time from sprints to just a few days using standard templates and codegen.  
- **Simplified Maintenance:** Standardized boilerplate updates, reducing manual updates to two simple commands.  
- **Community Building:** Fostered a cross-team community for maintaining and improving micro-libraries.  
- **Leadership Endorsement:** Engineering VPs advocated for full adoption of the Release-First Branching Strategy across the organization.

---
# Digital Rights Management (DRM) Service  

## Introduction  
The DRM service supports three major license challenge protocols for video playback copyright protection. It also includes a Key Management System (KMS) for managing secret keys used in video encryption.  

## Background  
PlutoTV had a contractual obligation to deliver HD content with copyright protection. I was tasked with creating a DRM service that:  
- Supports **FairPlay** for HLS playback on Apple devices and the Safari browser  
- Supports **Widevine** for DASH playback on Android devices  
- Supports **PlayReady** for DASH playback on Xbox and PlayStation 5  
- Provides high scalability and low-latency encryption key management  

## Highlights  
- **Asynchronous Workflow Design:** Implemented using Confluent Kafka for job queuing and Kubernetes Cron Jobs for task execution.  
- **Architecture Documentation:** Designed and documented the system architecture, submitting it for review and approval by the architecture team.  
- **FairPlay Integration:** Used CGO to compile FairPlay C source code and integrated it with the Go service.  
- **Memory Leak Debugging:** Diagnosed and resolved FairPlay C source memory leaks using Valgrind.  

## Impact  
The project resulted in a stable, highly scalable platform that supports:  
- **Video Encryption Workflow:** Efficiently managing video encryption processes.  
- **DRM License Challenges:** Handling copyright-protected video playback on PlutoTV across multiple devices.

