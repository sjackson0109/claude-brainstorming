---
name: brainstorming-technical
description: "Focused brainstorming for technical architecture and engineering. Activated by 'brainstorm architecture...', 'brainstorm infrastructure...', 'brainstorm system design...'. Handles system architecture, cloud planning, DevOps, and technical implementations."
---

# Technical Architecture Brainstorming

## Activation

This skill responds to technical and engineering-focused brainstorming requests:

**Primary triggers:**
- "Brainstorm architecture for [system/application]"
- "Help me brainstorm infrastructure for [project]"
- "Let's brainstorm technical design for [feature]"
- "Brainstorm cloud strategy for [application]"
- "Help me brainstorm DevOps pipeline for [deployment]"

**Architecture & design:**
- "Brainstorm system architecture for [requirements]"
- "Help me brainstorm database design for [application]"
- "Let's brainstorm API design for [service]"
- "Brainstorm integration patterns for [systems]"

**Infrastructure & operations:**
- "Brainstorm infrastructure scaling for [growth]"
- "Help me brainstorm monitoring strategy for [system]"
- "Let's brainstorm security architecture for [platform]"
- "Brainstorm deployment strategy for [application]"

## Overview

Transform technical requirements into robust, scalable system designs through structured dialogue. Focus on:

- **System architecture** - Components, patterns, scalability, performance
- **Infrastructure design** - Cloud platforms, networking, security, cost optimisation
- **DevOps strategies** - CI/CD pipelines, automation, monitoring, deployment
- **Integration planning** - APIs, data flows, service boundaries
- **Database design** - Schema design, performance, reliability, scaling
- **Security architecture** - Authentication, authorisation, encryption, compliance

Start by understanding technical requirements and constraints, then explore architecture options with clear trade-offs.

## The Process

**Understanding the requirements:**
- Current system state and constraints
- Performance, scalability, and reliability requirements
- Security, compliance, and operational needs
- Budget, timeline, and team capabilities

**Exploring architecture options:**
- Propose 2-3 different approaches with trade-offs
- Consider complexity, maintainability, and team expertise
- Evaluate technology choices and integration requirements

**Presenting the design:**
- Break into logical components (200-300 words each)
- Use diagrams and visual representations where helpful
- Validate technical feasibility after each section
- Adapt to specific deliverable type:
  - **System architecture**: Components, data flow, interfaces
  - **Infrastructure**: Cloud resources, networking, security
  - **DevOps**: Pipeline stages, automation, monitoring
  - **Integration**: API contracts, data transformation, error handling

## Key Technical Frameworks

**Architecture Design Patterns:**
- Microservices vs monolithic architecture analysis
- Event-driven architecture and messaging patterns
- API gateway and service mesh considerations
- Database per service vs shared database trade-offs

**Cloud Platform Selection:**
- AWS, Azure, GCP feature comparison and cost analysis
- Serverless vs container vs virtual machine trade-offs
- Multi-cloud vs single-cloud strategy considerations
- Vendor lock-in mitigation and portability planning

**Infrastructure as Code:**
- Terraform, CloudFormation, ARM template selection
- Environment consistency and deployment automation
- Configuration management and secret handling
- Infrastructure versioning and rollback strategies

**DevOps Pipeline Design:**
- Source control branching and merge strategies
- Build automation and dependency management
- Testing pyramid and quality gates implementation
- Deployment strategies and rollback procedures

**Monitoring & Observability:**
- Metrics collection and alerting strategies
- Logging aggregation and analysis frameworks
- Distributed tracing and performance monitoring
- Service level objectives and error budgets

## Technical Templates

**Architecture Decision Record:**

| Decision | Options Considered | Choice Made | Rationale |
|----------|-------------------|-------------|-----------|
| Database | PostgreSQL, MongoDB, DynamoDB | PostgreSQL | ACID compliance, team expertise |
| Hosting | AWS, Azure, GCP | AWS | Existing expertise, cost analysis |
| API Style | REST, GraphQL, gRPC | REST | Simplicity, tooling maturity |

**System Component Matrix:**

| Component | Technology | Scalability | Complexity | Team Readiness |
|-----------|------------|-------------|------------|----------------|
| Web Frontend | React | High | Medium | High |
| API Gateway | Kong | High | Low | Medium |
| Backend Services | Node.js | High | Medium | High |
| Database | PostgreSQL | Medium | Low | High |
| Message Queue | RabbitMQ | High | Medium | Low |

**Infrastructure Cost Model:**

| Component | Monthly Cost | Scaling Factor | Notes |
|-----------|--------------|----------------|-------|
| Compute | £500 | 2x per 10k users | Auto-scaling configured |
| Storage | £200 | Linear with data | Includes backup costs |
| Network | £100 | 1.5x per region | CDN and transfer costs |
| Monitoring | £50 | Fixed | Tool licensing |

## Technical Documentation

**Architecture documentation:**
- `docs/architecture/YYYY-MM-DD-<system>-design.md`
- Include system diagrams, component relationships
- Document technology choices and rationale
- Specify performance and scalability targets

**Implementation planning:**
- Break design into development phases
- Identify technical dependencies and risks
- Plan proof-of-concept and validation steps
- Establish testing and quality assurance strategies

## Key Principles

- **Simplicity first** - Choose the simplest solution that meets requirements
- **Scalability by design** - Plan for growth but don't over-engineer initially
- **Security throughout** - Build security in from the start, not as an afterthought
- **Operational excellence** - Design for monitoring, debugging, and maintenance
- **Team capabilities** - Match technology choices to team skills and growth plans
- **Cost consciousness** - Optimise for cost-effectiveness and resource efficiency
- **Fail-safe design** - Plan for failures and build in resilience mechanisms