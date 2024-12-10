# Digital Right Management (DRM) Service
## Intro
DRM service support 3 major license challenge protocols for video playback copyright protection.  In addition, a KMS to manage secret keys for video clips encryption.

## Background
PlutoTV had a contractual obligation to deliver HD contents with copyright protection.  I was tasked to create a DRM Service
* to provide Fairplay support for HLS playback on Apple devices and Safari browser
* to provide Widevine support for DASH playback on Android devices
* to provide PlayRead support for XBox and PlayStation5 DASH playback
* to provide high scalability, low read latency encryption key management

## Highlight
* Design and implement asychronous workflow using Confluence Kafka for job queue and Kubernetes cron job execution
* Document archtecutre design and submit for archtecture team review and approval
* Use CGO to complie Fairplay C source code, and interop with Go service
* Debug Fairplay C source memory leak with valgrind
  
## Imapact
* A stable and highly scalable platform to support
  * Vidoe encryption workflow
  * DRM challenge for every copyright protected video played on PlutoTV

# SWAT Team
## Intro
SWAT Team is a temporary enginerring organizattion to support high priority cross team initiative

## Background
Migrate service infrastructure from AWS EC2/ECS to EKS for
* cost of operation optimization
* multi-cloud deployment

## Highlight
* Work with DevOps team to develop standards for golang micro-services in Kubernetes runtime environment
  * use ConfigMap for configuration with live update
  * sync HashiCorp Vault secret with Kubernetes secret store with ExternalSecrets
  * standardize GitHub Action golang micro-service build workflow
* Develop micro-libraries
  * breakup monolithic core library into multiple limited purpose micro-libraries
* Develope codegen to standardize boilerplate code artifacts
  * codegen boilerplate code: secret wireup, certain standard dependency wireup
  * codegen projectt non-go artifacts: Makefile, GitHub Action yamls, Dockerfile, Helm chart, config files ...
* Reform development life cycle from GitFlow to Release First Branching Model
  * Publish Release First Branching Model documentation
  * Promote and assist other teams to adopt the new process

## Impact
* 

# Enterprise Platform team
