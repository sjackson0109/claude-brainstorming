---
name: brainstorming-technical-networking
description: "Expert-level brainstorming for network architecture and design. Leverages CCNA and CCIE expertise for routing, switching, security, WAN design, and enterprise networking solutions through structured dialogue."
---

# Technical Networking Brainstorming

## Activation Triggers

This skill responds to network architecture and design brainstorming requests:

- "Brainstorm network design for [enterprise/campus/data centre]"
- "Help me brainstorm routing strategy for [WAN/LAN/multi-site]"
- "Let's brainstorm network security architecture for [environment]"
- "Brainstorm SD-WAN implementation for [organisation]"
- "Help me brainstorm network segmentation for [security requirements]"
- "Let's brainstorm wireless design for [campus/office]"
- "Brainstorm network redundancy for [critical systems]"
- "Help me brainstorm network troubleshooting approach for [issue]"
- "Let's brainstorm cloud networking strategy for [hybrid environment]"

## Scope

**What this covers:**
- Enterprise network architecture and design (campus, WAN, data centre)
- Routing protocols and strategies (OSPF, EIGRP, BGP, static routing)
- Switching technologies and VLANs, STP, port security, QoS
- Network security architecture (firewalls, VPNs, network segmentation, zero trust)
- Wireless networking design (enterprise WiFi, coverage, capacity planning)
- SD-WAN and hybrid cloud connectivity
- Network performance optimisation and troubleshooting methodologies
- High availability and disaster recovery networking

**What this doesn't cover:**
- Application development (use Product Development Brainstorming)
- Business strategy and commercial planning (use Commercial Strategy Brainstorming)
- General IT operations (use Business Operations Brainstorming)
- Server and application architecture (use Technical Architecture Brainstorming)

## Conversation Rules

1. **One question at a time** - Focus on specific networking decisions
2. **Multiple choice preferred** - Present technical options with pros/cons
3. **Lead with recommendation** - Propose 2-3 approaches, recommend one with CCIE-level reasoning
4. **Standards-based design** - Follow industry best practices and RFC standards
5. **Validate incrementally** - Present network sections, check technical alignment

## Process

**Understanding the network requirements:**
- Current network state and pain points
- Performance, scalability, and availability requirements
- Security, compliance, and regulatory needs
- Budget constraints and implementation timeline

**Exploring network design options:**
- Propose 2-3 different approaches with technical trade-offs
- Consider scalability, maintainability, and operational complexity
- Evaluate technology choices and vendor considerations

**Presenting the design:**
- Break into logical network layers and components
- Generate appropriate mermaid diagrams based on context
- Focus on proven, standards-based solutions
- Validate technical feasibility and operational impact

## Expert Networking Frameworks

**Network Design Questions:**
- "What's your current network topology and what issues are you experiencing?"
- "What are your bandwidth, latency, and availability requirements?"
- "What security and compliance requirements must the network meet?"
- "What's your budget and timeline for implementation?"
- "Do you have existing vendor relationships or technology preferences?"

**Layer 3 Routing Design:**
- **IGP Selection**: OSPF vs EIGRP for internal routing (area design, summarization)
- **BGP Implementation**: eBGP for WAN, iBGP for large enterprises, route policies
- **Route Redundancy**: Multiple paths, load balancing, failover mechanisms
- **Summarization Strategy**: Hierarchical addressing, route aggregation

**Layer 2 Switching Design:**
- **VLAN Strategy**: Segmentation approach, VLAN numbering, trunk design
- **Spanning Tree**: RPVST+, MST for large networks, loop prevention
- **Access Control**: Port security, 802.1X, dynamic VLAN assignment
- **QoS Implementation**: Traffic classification, marking, queuing strategies

**Network Security Architecture:**
- **Segmentation Strategy**: DMZ design, internal segmentation, microsegmentation
- **Firewall Placement**: Perimeter, internal, host-based firewall strategies
- **VPN Design**: Site-to-site IPSec, remote access, SSL VPN considerations
- **Zero Trust Implementation**: Network access control, device trust verification

**Wireless Design:**
- **Coverage Planning**: RF site surveys, capacity planning, interference analysis
- **Security Implementation**: WPA3-Enterprise, 802.1X, guest network isolation
- **Controller Strategy**: Centralised vs distributed, cloud-managed options
- **Performance Optimisation**: Channel planning, power management, roaming

**WAN and SD-WAN Strategy:**
- **Transport Selection**: MPLS, Internet, LTE, satellite connectivity options
- **SD-WAN Benefits**: Dynamic path selection, centralised policy, cost optimisation
- **Hybrid Connectivity**: Cloud on-ramps, direct connect options
- **Bandwidth Planning**: Application requirements, growth projections, burstability

**High Availability Design:**
- **Redundancy Strategy**: Active/active vs active/passive, geographic distribution
- **Failover Mechanisms**: HSRP/VRRP, link aggregation, routing protocol convergence
- **Disaster Recovery**: Network backup strategies, alternate site connectivity
- **Monitoring**: Network visibility, alerting, performance baselines

## Technical Decision Matrices

**Routing Protocol Selection:**

| Protocol | Scalability | Convergence | Complexity | Use Case |
|----------|-------------|-------------|------------|-----------|
| Static | Low | Fast | Low | Small networks, specific routes |
| OSPF | High | Medium | Medium | Enterprise LANs, hierarchical design |
| EIGRP | Medium | Fast | Low | Cisco-only environments |
| BGP | Very High | Slow | High | WAN, Internet connectivity, large enterprise |

**Switching Technology Comparison:**

| Feature | Access Layer | Distribution Layer | Core Layer |
|---------|-------------|-------------------|------------|
| Port Density | High (24-48 ports) | Medium (12-24 ports) | Low (4-12 high-speed) |
| PoE Requirement | Yes (cameras, phones, APs) | Optional | No |
| Stacking | Preferred | Optional | Not recommended |
| Layer 3 Features | Basic | Full routing | Full routing + advanced |

**Security Implementation Strategy:**

| Security Layer | Technology Options | Recommendation |
|----------------|-------------------|----------------|
| Perimeter | ASA, FortiGate, Palo Alto | Next-gen firewall with IPS |
| Internal | Micro-segmentation, VLANs | VLAN + firewall rules |
| Access Control | 802.1X, NAC, port security | 802.1X with dynamic VLANs |
| Monitoring | SIEM, flow analysis, IDS | NetFlow + security monitoring |

## Troubleshooting Methodology

**Structured Network Troubleshooting:**
1. **Problem Definition**: Symptoms, scope, timing, user impact
2. **Information Gathering**: Network topology, recent changes, logs
3. **Hypothesis Formation**: Most likely causes based on symptoms
4. **Testing Strategy**: Layer-by-layer approach (OSI model)
5. **Resolution Implementation**: Fix, test, document, prevent recurrence

**Common Network Issues:**
- **Performance Problems**: Bandwidth utilisation, latency, packet loss analysis
- **Connectivity Issues**: Layer 1/2/3 troubleshooting, routing table analysis
- **Security Incidents**: Traffic analysis, policy verification, breach response
- **Redundancy Failures**: Failover testing, convergence time analysis

## Visual Documentation with Mermaid

**Context-Aware Diagram Generation:**
The skill automatically generates appropriate mermaid diagrams based on the networking challenge, including topology diagrams, VPN configurations, redundancy designs, and troubleshooting workflows.

### Network Topology Diagrams

**Basic Enterprise Network Architecture:**
```mermaid
graph TD
    Internet[Internet] --> ISP[ISP Router]
    ISP --> FW[Firewall]
    FW --> Core[Core Switch]
    Core --> Dist1[Distribution Switch 1]
    Core --> Dist2[Distribution Switch 2]
    Dist1 --> Access1[Access Switch 1]
    Dist1 --> Access2[Access Switch 2]
    Dist2 --> Access3[Access Switch 3]
    Dist2 --> Access4[Access Switch 4]
```

**Hub-and-Spoke Topology:**
```mermaid
graph TD
    subgraph "Head Office - Hub"
        Hub[Hub Router]
        HubFW[Hub Firewall]
        HubLAN[Hub LAN]
    end
    
    subgraph "Branch 1 - Spoke"
        Spoke1[Branch Router 1]
        Spoke1LAN[Branch 1 LAN]
    end
    
    subgraph "Branch 2 - Spoke"
        Spoke2[Branch Router 2] 
        Spoke2LAN[Branch 2 LAN]
    end
    
    subgraph "Branch 3 - Spoke"
        Spoke3[Branch Router 3]
        Spoke3LAN[Branch 3 LAN]
    end
    
    Hub <--> Spoke1
    Hub <--> Spoke2
    Hub <--> Spoke3
    Hub --> HubFW --> HubLAN
    Spoke1 --> Spoke1LAN
    Spoke2 --> Spoke2LAN
    Spoke3 --> Spoke3LAN
    
    Internet[Internet] --> Hub
```

### VPN Configurations

**Site-to-Site VPN Architecture:**
```mermaid
graph LR
    subgraph "Site A"
        SiteA_LAN["LAN: 192.168.1.0/24"]
        SiteA_FW["Firewall A<br/>Public IP: 203.0.113.10"]
        SiteA_RTR["Router A"]
    end
    
    subgraph "Site B"  
        SiteB_LAN["LAN: 192.168.2.0/24"]
        SiteB_FW["Firewall B<br/>Public IP: 203.0.113.20"]
        SiteB_RTR["Router B"]
    end
    
    subgraph "Internet"
        ISP["Internet/ISP Cloud"]
        VPN_Tunnel["IPSec VPN Tunnel<br/>AES-256, SHA-256"]
    end
    
    SiteA_LAN --> SiteA_RTR --> SiteA_FW
    SiteB_LAN --> SiteB_RTR --> SiteB_FW
    SiteA_FW <--> ISP <--> SiteB_FW
    SiteA_FW -.-> VPN_Tunnel -.-> SiteB_FW
    
    style VPN_Tunnel fill:#e1f5fe,stroke:#01579b,stroke-dasharray: 5 5
```

**Hub-and-Spoke VPN with Multiple Sites:**
```mermaid
graph TD
    subgraph "Head Office - VPN Hub"
        HO_LAN["HQ LAN: 10.0.0.0/16"]
        HO_FW["Hub Firewall<br/>10.1.1.1"]
        HO_VPN["VPN Concentrator"]
    end
    
    subgraph "Branch 1"
        B1_LAN["Branch 1: 10.1.0.0/24"]
        B1_FW["Branch 1 FW<br/>10.1.1.10"]
    end
    
    subgraph "Branch 2"
        B2_LAN["Branch 2: 10.2.0.0/24"] 
        B2_FW["Branch 2 FW<br/>10.1.1.20"]
    end
    
    subgraph "Branch 3"
        B3_LAN["Branch 3: 10.3.0.0/24"]
        B3_FW["Branch 3 FW<br/>10.1.1.30"]
    end
    
    Internet[Internet Cloud]
    
    HO_LAN --> HO_FW --> HO_VPN
    B1_LAN --> B1_FW
    B2_LAN --> B2_FW  
    B3_LAN --> B3_FW
    
    HO_VPN <--> Internet <--> B1_FW
    HO_VPN <--> Internet <--> B2_FW
    HO_VPN <--> Internet <--> B3_FW
    
    HO_VPN -.-> B1_FW
    HO_VPN -.-> B2_FW
    HO_VPN -.-> B3_FW
```

### High Availability and Redundancy

**HSRP (Hot Standby Router Protocol) Configuration:**
```mermaid
graph TD
    subgraph "LAN Segment: 192.168.1.0/24"
        PC1["PC 1"]
        PC2["PC 2"] 
        PC3["PC 3"]
        VIP["Virtual IP: 192.168.1.1<br/>Virtual MAC: 0000.0c07.acXX"]
    end
    
    subgraph "Router Redundancy"
        R1["Router 1<br/>192.168.1.2<br/>Priority: 110<br/>State: ACTIVE"]
        R2["Router 2<br/>192.168.1.3<br/>Priority: 100<br/>State: STANDBY"]
    end
    
    subgraph "Upstream"
        ISP1[ISP Connection 1]
        ISP2[ISP Connection 2]
    end
    
    PC1 --> VIP
    PC2 --> VIP
    PC3 --> VIP
    VIP -.-> R1
    VIP -.-> R2
    R1 --> ISP1
    R2 --> ISP2
    R1 <--> R2
    
    style R1 fill:#c8e6c9,stroke:#2e7d32
    style R2 fill:#fff3e0,stroke:#ef6c00
    style VIP fill:#e3f2fd,stroke:#1976d2
```

**VRRP (Virtual Router Redundancy Protocol) Design:**
```mermaid
graph TD
    subgraph "VLAN 10: 10.1.10.0/24"
        Client1["Client 1"]
        Client2["Client 2"]
        DefaultGW["Default Gateway<br/>10.1.10.1<br/>VRID: 10"]
    end
    
    subgraph "Router Cluster"
        Master["VRRP Master<br/>10.1.10.2<br/>Priority: 200<br/>Advertisement: 1s"]
        Backup1["VRRP Backup 1<br/>10.1.10.3<br/>Priority: 150"]
        Backup2["VRRP Backup 2<br/>10.1.10.4<br/>Priority: 100"]
    end
    
    subgraph "Uplinks"
        Core1[Core Switch 1]
        Core2[Core Switch 2]
    end
    
    Client1 --> DefaultGW
    Client2 --> DefaultGW
    DefaultGW -.-> Master
    DefaultGW -.-> Backup1
    DefaultGW -.-> Backup2
    
    Master --> Core1
    Backup1 --> Core1
    Backup2 --> Core2
    
    Master <-.-> Backup1
    Master <-.-> Backup2
    Backup1 <-.-> Backup2
    
    style Master fill:#4caf50,stroke:#1b5e20
    style Backup1 fill:#ff9800,stroke:#e65100
    style Backup2 fill:#ff9800,stroke:#e65100
```

### Routing Protocol Visualisation

**OSPF Area Design:**
```mermaid
graph TD
    subgraph "Area 0 - Backbone"
        ABR1[ABR Router 1]
        ABR2[ABR Router 2] 
        Backbone[Backbone Links]
    end
    
    subgraph "Area 1 - Standard"
        A1R1[Area 1 Router 1]
        A1R2[Area 1 Router 2]
        A1NET["10.1.0.0/16"]
    end
    
    subgraph "Area 2 - NSSA"
        A2R1["Area 2 Router 1"]
        A2R2["Area 2 Router 2"]
        A2NET["10.2.0.0/16"]
        External["External Routes<br/>Type-7 LSA"]
    end
    
    ABR1 <--> Backbone <--> ABR2
    ABR1 <--> A1R1 <--> A1R2
    ABR2 <--> A2R1 <--> A2R2
    A1R1 --> A1NET
    A1R2 --> A1NET
    A2R1 --> A2NET
    A2R2 --> A2NET
    A2R2 --> External
    
    style Backbone fill:#e3f2fd,stroke:#1976d2
    style A1NET fill:#e8f5e8,stroke:#2e7d32
    style A2NET fill:#fff3e0,stroke:#ef6c00
```

**BGP Peering Relationships:**
```mermaid
graph LR
    subgraph "AS 65001 - Enterprise"
        R1["Router 1<br/>iBGP Peer"]
        R2["Router 2<br/>iBGP Peer"]
        RR["Route Reflector<br/>Router ID: 1.1.1.1"]
    end
    
    subgraph "AS 65002 - ISP A"
        ISPA["ISP-A Router<br/>eBGP Peer"]
    end
    
    subgraph "AS 65003 - ISP B" 
        ISPB["ISP-B Router<br/>eBGP Peer"]
    end
    
    subgraph "AS 65004 - Partner"
        Partner["Partner Network<br/>eBGP Peer"]
    end
    
    R1 <-.-> RR
    R2 <-.-> RR
    R1 <--> ISPA
    R2 <--> ISPB
    R1 <--> Partner
    
    style RR fill:#e1f5fe,stroke:#01579b
    style ISPA fill:#e8f5e8,stroke:#2e7d32
    style ISPB fill:#e8f5e8,stroke:#2e7d32
    style Partner fill:#fff3e0,stroke:#ef6c00
```

### Security Architecture Diagrams

**DMZ and Internal Network Security:**
```mermaid
graph LR
    subgraph "Internet"
        WWW[Internet Users]
    end
    
    subgraph "DMZ"
        Web["Web Server<br/>10.10.10.10"]
        Mail["Mail Server<br/>10.10.10.11"]
        DNS["DNS Server<br/>10.10.10.12"]
    end
    
    subgraph "Internal Network"
        DB["Database Server<br/>192.168.1.10"]
        App["App Server<br/>192.168.1.11"]
        File["File Server<br/>192.168.1.12"]
    end
    
    subgraph "Management Network"
        Admin["Admin Workstation"]
        Monitor["Monitoring Server"]
    end
    
    WWW --> FW1["Perimeter Firewall<br/>Rules: 80, 443, 25, 53"]
    FW1 --> DMZ
    DMZ --> FW2["Internal Firewall<br/>Rules: DB Access Only"]
    FW2 --> Internal
    
    Admin -.-> FW1
    Admin -.-> FW2
    Monitor -.-> DMZ
    Monitor -.-> Internal
    
    style FW1 fill:#ffcdd2,stroke:#c62828
    style FW2 fill:#ffcdd2,stroke:#c62828
```

### SD-WAN and Modern Networks

**SD-WAN Multi-Transport Architecture:**
```mermaid
graph TD
    subgraph "Data Centre"
        DC_SDWAN[SD-WAN Controller]
        DC_Orchestrator[Orchestrator]
        DC_Analytics[Analytics Engine]
    end
    
    subgraph "Branch Office"
        Branch_SDWAN["SD-WAN Edge<br/>Policy Engine"]
        Branch_LAN["Branch LAN<br/>192.168.100.0/24"]
    end
    
    subgraph "Transport Options"
        MPLS["MPLS<br/>Primary: 100Mbps<br/>SLA: 99.9%"]
        Internet1["Internet 1<br/>Secondary: 200Mbps<br/>Best Effort"]
        Internet2["Internet 2<br/>Backup: 50Mbps<br/>Best Effort"]
        LTE["LTE/4G<br/>Emergency: 25Mbps"]
    end
    
    subgraph "Cloud Services"
        AWS[AWS VPC]
        Azure[Azure VNet]
        SaaS[SaaS Applications]
    end
    
    DC_SDWAN --> DC_Orchestrator
    DC_SDWAN --> DC_Analytics
    
    Branch_SDWAN <--> MPLS
    Branch_SDWAN <--> Internet1  
    Branch_SDWAN <--> Internet2
    Branch_SDWAN <--> LTE
    
    MPLS <--> DC_SDWAN
    Internet1 <--> AWS
    Internet1 <--> Azure
    Internet2 <--> SaaS
    
    Branch_SDWAN --> Branch_LAN
    
    style MPLS fill:#c8e6c9,stroke:#2e7d32
    style Internet1 fill:#fff3e0,stroke:#ef6c00
    style Internet2 fill:#fff3e0,stroke:#ef6c00
    style LTE fill:#ffcdd2,stroke:#c62828
```

**Diagram Generation Guidelines:**
- **Topology Diagrams**: Use graph TD/LR for physical network layouts, campus designs, WAN architectures
- **Protocol Flows**: Use flowchart TD for routing decisions, failover sequences, troubleshooting steps
- **Security Zones**: Use subgraphs to represent security boundaries, VLANs, network segments
- **Redundancy Designs**: Highlight active/standby states with colour coding and connection styles
- **VPN Tunnels**: Use dashed lines (-.-> or <-..->) to represent encrypted connections
- **Logical Relationships**: Use different arrow styles for control plane (<-.->), data plane (-->), and management (-.->)

## Output Focus

- **Standards-compliant network design** with proper addressing and routing
- **Scalable architecture** that grows with business requirements
- **Security-first approach** with defence in depth
- **Visual documentation** using context-appropriate mermaid diagrams
- **Operational simplicity** with clear documentation and procedures
- **Performance optimisation** for critical applications and services
- **Cost-effective solutions** balancing features with budget constraints
- **Vendor-neutral recommendations** with implementation alternatives