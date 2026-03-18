# API Security Testing Brainstorming Skill

## Purpose

The API Security Testing Brainstorming Skill specialises in comprehensive offensive security assessment strategy for Application Programming Interfaces (APIs). This skill empowers strategic thinking through systematic API vulnerability discovery, authentication bypass analysis, and comprehensive security testing methodologies for REST, GraphQL, SOAP, and emerging API technologies.

## Core Capabilities

### API Security Assessment Framework
- **API Discovery and Documentation Analysis**: Strategic enumeration of API endpoints, parameter analysis, and specification reverse engineering
- **Authentication and Authorisation Testing**: Comprehensive assessment of API authentication mechanisms, token security, and access control implementation
- **Business Logic Vulnerability Analysis**: Systematic testing of API workflow manipulation, rate limiting bypass, and business rule circumvention

### REST API Security Testing
- **HTTP Method Testing**: Comprehensive analysis of supported HTTP methods including unauthorised method access and HTTP verb tampering
- **Parameter Manipulation Analysis**: Strategic testing of query parameters, path parameters, and request body manipulation for injection and bypass vulnerabilities
- **JSON and XML Injection Testing**: Assessment of structured data injection vulnerabilities including JSON injection, XML External Entity (XXE), and data structure manipulation

### GraphQL and Modern API Security
- **GraphQL Schema Analysis**: Systematic discovery and analysis of GraphQL schemas, queries, and mutation capabilities
- **Query Complexity and Resource Exhaustion**: Strategic testing of GraphQL query depth limits, complexity analysis, and denial-of-service vulnerabilities
- **Subscription and Real-Time API Testing**: Assessment of WebSocket-based APIs, Server-Sent Events, and real-time communication security

## Implementation Framework

### Phase 1: API Discovery and Reconnaissance (55 minutes)
- Conduct comprehensive API endpoint discovery through multiple reconnaissance techniques including documentation analysis and fuzzing
- Perform API specification analysis to understand authentication requirements, data models, and business functionality
- Map API attack surface including third-party integrations, microservice communications, and external API dependencies

### Phase 2: Authentication and Access Control Testing (70 minutes)
- Execute systematic authentication testing including credential enumeration, token analysis, and session management assessment
- Perform authorisation testing to identify privilege escalation opportunities and horizontal access control bypass
- Test API rate limiting, throttling mechanisms, and abuse prevention controls for effectiveness and bypass opportunities

### Phase 3: Data Manipulation and Business Logic Testing (65 minutes)
- Conduct comprehensive input validation testing across all API parameters including injection vulnerability assessment
- Perform business logic testing to identify workflow manipulation opportunities and process circumvention methods
- Analyse data exposure including sensitive information leakage and excessive data exposure through API responses

## Key Techniques and Methodologies

### API Testing Methodologies
- **OWASP API Security Top 10 Compliance**: Systematic testing against established API security vulnerabilities and attack patterns
- **Automated and Manual Testing Integration**: Strategic combination of automated API testing tools with manual analysis and exploitation
- **API Specification-Driven Testing**: Comprehensive testing based on OpenAPI, GraphQL schemas, and API documentation analysis

### Authentication and Token Security
- **JWT Security Analysis**: Comprehensive testing of JSON Web Tokens including signature verification, algorithm confusion, and payload manipulation
- **OAuth 2.0 and OIDC Testing**: Assessment of OAuth flows, authorization code injection, and identity provider integration security
- **API Key Security Assessment**: Testing of API key implementation, rotation policies, and access scope enforcement

### Advanced API Exploitation Techniques
- **Race Condition and TOCTOU Testing**: Strategic analysis of time-based vulnerabilities in API processing and resource access
- **Mass Assignment and Object Injection**: Testing of automatic object binding vulnerabilities and unauthorised property modification
- **API Chaining and Dependency Exploitation**: Strategic combination of API vulnerabilities to achieve complex attack scenarios

## Industry Applications

### Enterprise API Security
- **Microservices Architecture Testing**: Comprehensive security assessment of microservice-to-microservice communications and API gateway security
- **Enterprise Integration API Testing**: Security testing of APIs that connect enterprise systems, databases, and third-party services
- **Mobile Application Backend Testing**: Assessment of APIs serving mobile applications including authentication, data synchronisation, and offline capability security

### Cloud and SaaS API Security
- **Cloud Service API Testing**: Security assessment of cloud provider APIs including infrastructure-as-a-service and platform-as-a-service interfaces
- **Third-Party API Integration Testing**: Assessment of external API dependencies and integration security including data privacy and access control
- **Multi-Tenant SaaS API Testing**: Comprehensive testing of software-as-a-service APIs with focus on tenant isolation and data segregation

### Financial and Critical Infrastructure APIs
- **Financial Services API Testing**: Specialized testing of payment APIs, banking interfaces, and financial data APIs with regulatory compliance considerations
- **Healthcare API Testing**: FHIR and healthcare-specific API security testing with patient data protection and HIPAA compliance requirements
- **IoT and Industrial API Testing**: Assessment of device management APIs, telemetry interfaces, and industrial control system APIs

## Success Metrics and Validation

### API Vulnerability Discovery
- **Critical API Vulnerability Identification**: Successful discovery of high-impact API security vulnerabilities affecting data confidentiality and system integrity
- **Authentication Bypass Achievement**: Demonstration of unauthorized access to protected API resources through authentication and authorization bypass
- **Data Exposure Assessment**: Identification of sensitive data leakage through API responses and information disclosure vulnerabilities

### Business Logic and Workflow Testing
- **Business Process Manipulation**: Successful demonstration of business logic bypass leading to unauthorized operations or data access
- **Rate Limiting and Abuse Prevention Testing**: Assessment of API abuse protection mechanisms and identification of bypass techniques
- **API Dependency Security**: Evaluation of third-party API integration security and identification of supply chain vulnerabilities

### Remediation and Security Improvement
- **API Security Architecture Recommendations**: Strategic guidance for improving API security design and implementation practices
- **Developer Security Awareness**: Enhanced understanding of API security risks among development teams and DevOps practices
- **API Security Testing Integration**: Establishment of ongoing API security testing practices within development and deployment pipelines