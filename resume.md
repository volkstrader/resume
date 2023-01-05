# Chuck Chau Professional Career at PlutoTV
* [LinkedIn](https://www.linkedin.com/in/cchau2/)
* [GitHub](https://github.com/volkstrader)
* Tenure: 9/2019 to Present
* Titles: Senior Backend Engineer -> Lead Engineer -> Senior Lead Engineer

# Roles

## Go-whip
* Conduct code reviewes for the team projects and shared libraries
* Enforce go-opinated best coding practice and convention
* Mentor peer engineers on code logic, language features, and convention

## Shaper
* Recommend 3rd party library/tool
* Reform SDLC process to enforce executive visions - shift left, small and frequent release
* Enforce standards and updates through codegen library
* Introduce domain specific micro-library pattern
* Member of Community of Practice -API Standards & Best Practices

## Developer
* Pioneer green field POC - drm, cgo, kafka, codege
* Refacotr monolithic library into micro libraries
* DRM backend subject matter expert 
* Technical liason between our team and external vendors

## Team Leader
* Design and conduct technical interview
* 1:1 performance review with developers
* Prepare supporting documentation and make recommendation to terminate unfit developers 
* Provide technical opinion for SAFe agile PI planning
* Interact with architecture team on system design
* Interact with DevOps team on infrastructure customization
* Interact with Platform Reliability team on observability, metrics and alerts
* Explain system design to developers
* Group stories into releases and create roadmap for delivery
* Assign tasks to developers based on skill level and priority

# Feature Projects

## SWAT
* Migrating all services from ECS to EKS is the highest priority goal for 2023
* Special task force team is created to focus on migration tasks
* Based on my previous successful kubernetes migration experiences, I will lead the effort to achieve the objective

## KVETCH (kubertenes)
* Lead infrastructure change project to adopt Kubernetes hosting
* Establish standard for k8s application
** ConfigMaps for configuration
** HashiCorp Valut for secret storage
** ExternalSecrets for secret data synchronization between Vault and k8s secret storage
** Developed standard go micro-library to bootstrap k8s application startup
** Developed codegen library to provision GitHub Action CI yaml rendering, helm charts yaml rendering, Makefile rendering, boilerplate go code rendering 
* Lead effort to migrate `service-bootstrap`, the highest traffic service which provide the first pixle data to bootstrap PlutoTV players
** Refactor concurrency using `chain of responsibility` and `pubsub` design pattern 

## DRM - Concierge/PlayReady
* Support license challenge for XBox and PlayStation5 DASH playback
* Proxy license challenge payload directly to Irdeto
* Use Confluent Kafka to facilitate key synchronization between KMS and Irdeto, to observe API rate limit 

## DRM - Concierge/Widevine
* Support license challenge for Android DASH playback
* Inject encryption key data based on PSSH input
* Proxy license challenge payload to Google Widevine

## DRM - Concierge/Fairplay
* Support license challenge for Apple devices or Safari browser HLS playback
* Proxy license challenge payload to self hosted Fairplay license service
* LRU cache most frequently used encryption keys

## DRM - Fairplay license service
* Eanble PlutoTV to deliver HD and above quality contents 
* Use CGO to compile Fairplay C source with Go service
* Detect and debug Fairplay C source memory leak with valgrind

## DRM - Key Management System (KMS)
* Store AES Key Data and IV for video clips encryption
* Low read latency
* MongoDB Atlas storage

## Watchlist
* Provide backend support for viewing experience features
** Favorite Channel
** Favorite VOD
** Resume Point
* Architech a high available and scalable API service which supports at least 1K RPS. 

## Foundation Library
* 1st generation common go library for PlutoTV core servie Restful API micro-services
* Select 3rd party HTTP Web Framework - echo 
* Select 3rd party Log Framework - logrus
* Select 3rd party IoC Container Framework - Uber dig
 
