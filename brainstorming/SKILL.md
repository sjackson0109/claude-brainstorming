---
name: brainstorming
description: "Intelligent brainstorming orchestrator that automatically routes to specialised domain expertise. Activated by any brainstorming request - analyses the context and automatically invokes relevant sub-skills from 150 specialised domains including technical, business, design, strategy, and innovation areas."
---

# Brainstorming

## CRITICAL INSTRUCTION: SELECTIVE FILE ACCESS ONLY

**READ REFERENCE FILES STRATEGICALLY BASED ON THE USER'S REQUEST**

- **ALWAYS read** files from `./references/` when the user's request clearly matches that domain
- **MAY read** additional files when cross-domain insights would significantly improve the response
- **MAY read** related files for complex strategic questions that span multiple areas
- **AVOID reading** files that are clearly irrelevant to the request
- **TYPICAL RANGE**: 1-3 files for most requests, more for comprehensive strategic analysis

## Activation

This skill responds to any brainstorming, creative thinking, or problem-solving request and automatically identifies the most relevant specialised expertise from 150 reference skills stored in `./references/`:

**Primary triggers:**
- "Brainstorm ideas for [any topic]"
- "Help me think through [any problem]"
- "Use your Brainstorming skill to support me with [specific domain]"
- "Let's explore options for [any challenge]"
- "I need ideas for [any project]"
- "Can we brainstorm [any concept]?"

**CRITICAL: Reference File Access Protocol**
**EFFICIENCY RULE: Read reference files strategically to provide the best possible response**

When a user request would benefit from specialised knowledge:
1. **FIRST**: Identify the primary domain and read the most relevant file
2. **ASSESS**: Would cross-domain insights significantly enhance the response?
3. **IF YES**: Read additional related files that would add substantial value
4. **AVOID**: Reading files that are clearly irrelevant or add minimal value
5. **COMPLEX REQUESTS**: May justify reading multiple files for comprehensive analysis

**Scenarios that justify reading multiple files:**
- User explicitly requests multi-domain analysis
- Strategic questions requiring integrated perspectives
- Complex problems where cross-domain insights are valuable
- Implementation challenges that span multiple specialisations

**File reading decision guidelines:**
- Simple domain-specific request → **READ 1 PRIMARY FILE**
- Complex single-domain request → **READ 1-2 RELATED FILES**  
- Multi-domain request → **READ 2-4 RELEVANT FILES**
- Strategic/comprehensive analysis → **READ AS NEEDED FOR QUALITY RESPONSE**
- General brainstorming → **READ ONLY IF SPECIFIC EXPERTISE WOULD ADD VALUE**

## Reference File Mapping

The `./references/` directory contains 150 specialised brainstorming skills. **Read the appropriate file(s) when the user's request matches these domains:**

### Technical & Engineering
**Read when user mentions: APIs, software, architecture, cloud, systems, networking, DevOps, MLOps**
- `api-design.md` - API design, REST architecture, integration challenges
- `software-architecture.md` - System design, architectural patterns, scalability  
- `microservices-architecture.md` - Microservices, distributed systems
- `technical-architecture.md` - Technical system design, infrastructure planning
- `technical-networking.md` - Network architecture, connectivity solutions
- `technical.md` - General technical problem-solving, engineering approaches
- `cloud-migration.md` - Cloud strategy, platform migration planning
- `scalability-planning.md` - System scaling, performance optimisation  
- `devops-culture.md` - DevOps practices, CI/CD, automation
- `machine-learning-operations.md` - MLOps, AI system deployment, model management
- `data-architecture.md` - Data systems, governance, analytics platforms
- `context-diagram.md` - System context modelling, boundary definition
- `troubleshooting-and-problem-solving.md` - Technical debugging, issue resolution
- `technology-integration.md` - Technology platform integration, system connectivity
- `technology-roadmapping.md` - Technology strategy, evolution planning
- `3d-visualisation.md` - 3D modelling, visualisation, spatial design

### Cybersecurity & Risk Management  
**Read when user mentions: security, compliance, risk, governance, regulations, frameworks**
- `cybersecurity.md` - Security frameworks, threat analysis, protection strategies
- `cis-controls.md` - CIS security controls, security baseline implementation
- `cmmc-cybersecurity.md` - CMMC compliance, defence contractor security
- `common-criteria.md` - Common Criteria evaluation, security certification
- `risk-management-frameworks.md` - Risk assessment, mitigation strategies
- `dynamic-risk-assessment.md` - Real-time risk evaluation, adaptive security
- `gdpr-compliance-frameworks.md` - GDPR compliance, data protection regulations
- `iso-standards-compliance.md` - ISO standards, quality management systems
- `governance-frameworks.md` - Corporate governance, oversight structures
- `regulatory-technology.md` - RegTech solutions, compliance automation
- `data-governance-act.md` - Data governance regulations, data management compliance
- `digital-markets-act.md` - Digital markets regulation, platform compliance
- `digital-services-act.md` - Digital services regulation, content moderation
- `eu-ai-act-compliance.md` - EU AI Act compliance, AI governance
- `cobit-governance.md` - COBIT framework, IT governance practices
- `coso-framework.md` - COSO internal controls, enterprise risk management
- `dora-resilience.md` - DORA regulation, operational resilience

### Business Strategy & Commercial Development
**Read when user mentions: strategy, market analysis, competition, business development, partnerships**  
- `strategic-planning.md` - Strategic frameworks, competitive analysis, planning processes
- `strategic-foresight.md` - Future planning, scenario development, strategic anticipation
- `strategic-partnerships.md` - Alliance strategy, partnership development, collaboration
- `blue-ocean-strategy.md` - Market creation, competitive differentiation, value innovation
- `commercial-strategy.md` - Commercial planning, market approach, revenue strategy
- `commercial.md` - General commercial considerations, business model development
- `market-entry-strategies.md` - New market development, market penetration approaches
- `market-penetration-strategy.md` - Market share growth, penetration tactics
- `competitive-intelligence.md` - Market research, competitor analysis, intelligence gathering
- `merger-and-acquisition-analysis.md` - M&A strategy, due diligence, integration planning
- `business-case-development.md` - Business justification, ROI analysis, investment cases
- `business-operations.md` - Operational strategy, business process optimisation
- `value-chain-analysis.md` - Value chain optimisation, supply chain strategy
- `partnership-development.md` - Strategic partnerships, alliance management
- `network-effect-analysis.md` - Network effects, platform dynamics, ecosystem strategy

### Product Development & Innovation
**Read when user mentions: product strategy, innovation, development, lean startup, design thinking**
- `product-development.md` - Product strategy, development processes, lifecycle management
- `product.md` - General product considerations, product management
- `product-roadmap-planning.md` - Roadmap creation, feature prioritisation, product strategy
- `innovation-pipeline.md` - Innovation management, idea development, innovation processes
- `innovation-labs.md` - Innovation lab setup, experimental approaches, R&D management
- `disruptive-innovation.md` - Breakthrough innovation, market disruption, transformation
- `lean-startup-methodology.md` - Startup validation, MVP development, iterative development
- `design-thinking.md` - Creative problem-solving, human-centred innovation
- `value-proposition-design.md` - Value proposition development, customer value creation
- `platform-strategy.md` - Platform business models, ecosystem development

### Design & User Experience
**Read when user mentions: UI/UX, design, user research, interface, customer experience, usability, diagrams, visualisation**
- `mermaid-diagrams.md` - Visual diagramming, flowcharts, system architecture visualisation, process mapping
- `user-interface-design.md` - UI design, visual systems, typography, colour theory
- `user-experience-design.md` - UX strategy, user journeys, interaction design
- `user-research.md` - User research methodologies, behaviour analysis, user insights
- `user-testing.md` - Usability testing, validation methods, user feedback
- `human-centred-design.md` - Design thinking, empathy-driven design, human factors
- `customer-experience.md` - Customer journey design, experience optimisation

### Financial Strategy & Pricing
**Read when user mentions: pricing, revenue, financial modelling, portfolio management**
- `pricing-strategies.md` - Pricing models, revenue optimisation, pricing psychology
- `advanced-pricing-strategy.md` - Complex pricing approaches, dynamic pricing, value-based pricing
- `revenue-model-design.md` - Business model monetisation, revenue stream development
- `financial-modelling-stress-testing.md` - Financial analysis, scenario modelling, risk assessment
### Operations & Process Optimisation
**Read when user mentions: operations, processes, workflow, quality, supply chain, continuous improvement**
- `operational-excellence.md` - Operational strategy, process optimisation, performance improvement
- `workflow-optimisation.md` - Business process improvement, workflow design, efficiency
- `yield-optimisation.md` - Production optimisation, output maximisation, efficiency improvement
- `supply-chain-optimisation.md` - Supply chain strategy, logistics optimisation, procurement
- `quality-assurance.md` - Quality management, testing frameworks, quality control
- `continuous-improvement.md` - Continuous improvement methodologies, process enhancement
- `vendor-management.md` - Supplier relationship management, vendor strategy, procurement
- `root-cause-analysis.md` - Problem analysis, issue investigation, systematic diagnosis

### Organisational Development & People Strategy
**Read when user mentions: organisation, workforce, culture, change management, talent, training**
- `organisational-design.md` - Organisational structure, role definition, hierarchy design
- `agentic-organisation-design.md` - Autonomous organisation structures, self-managing teams
- `workforce-planning.md` - Talent strategy, workforce analytics, human capital planning
- `talent-acquisition.md` - Recruitment strategy, talent sourcing, hiring processes
- `employee-engagement.md` - Engagement strategies, motivation, retention, satisfaction
- `change-management-psychology.md` - Change strategy, resistance management, transition psychology
- `change-communication-strategy.md` - Change communications, stakeholder messaging
- `change-readiness-assessment.md` - Change capability assessment, readiness evaluation
- `cultural-transformation.md` - Culture change, organisational culture development
- `cultural-intelligence.md` - Cross-cultural competency, global team management
- `cultural-adaptation.md` - Cultural change management, adaptation strategies
- `diversity-inclusion.md` - D&I frameworks, inclusive practices, equity strategies
- `training-and-development.md` - Learning strategy, skill development, capability building

### Analytics & Data-Driven Decision Making
**Read when user mentions: analytics, forecasting, data analysis, decision making, testing, measurement**
- `forecasting-and-prediction-models.md` - Predictive analytics, forecasting methodologies
- `social-media-analytics.md` - Social media measurement, digital analytics, engagement analysis
- `algorithmic-bias-detection.md` - AI bias assessment, fairness evaluation, algorithm auditing
- `bayesian-strategy-updating.md` - Probabilistic strategy, evidence-based adaptation
- `game-theory-applications.md` - Strategic interaction analysis, competitive dynamics
- `automated-swot-analysis.md` - Automated strategic analysis, systematic SWOT evaluation  
- `automated-stakeholder-analysis.md` - Stakeholder mapping, relationship analysis
- `scenario-modelling.md` - Scenario planning, future state modelling, alternative analysis
- `hypothesis-testing.md` - Scientific method application, experimental validation
- `evidence-based.md` - Evidence-based decision making, data-driven approaches
- `decision-tracking.md` - Decision management, outcome tracking, decision quality
- `impact-measurement.md` - Impact assessment, outcome measurement, effectiveness evaluation
- `ab-testing-integration.md` - A/B testing strategy, experimental design, validation

### Digital Strategy & E-commerce
**Read when user mentions: digital transformation, e-commerce, online strategy, digital platforms**
- `digital-strategy.md` - Digital transformation, technology strategy, digital business models
- `e-commerce-growth.md` - Online commerce strategy, digital marketplace, e-commerce optimisation

### Sustainability & Environmental Strategy
**Read when user mentions: sustainability, environment, green technology, clean tech, agriculture**
- `sustainability-frameworks.md` - Sustainability strategy, ESG frameworks, environmental planning
- `cleantech.md` - Clean technology development, environmental technology solutions
- `green-technology-assessment.md` - Environmental technology evaluation, green innovation
- `zero-waste-design.md` - Circular economy, waste elimination, sustainable design
- `agtech-agriculture.md` - Agricultural technology, farming innovation, food systems

### Crisis Management & Strategic Challenges
**Read when user mentions: crisis, risk, threats, adversarial situations, red team, brand protection**
- `crisis-management.md` - Crisis response, emergency planning, business continuity
- `brand-crisis-management.md` - Brand protection, reputation management, crisis communications
- `challenge-red-team.md` - Red team exercises, adversarial testing, security challenges
- `adversarial.md` - Adversarial analysis, competitive threats, hostile environment strategy

### Facilitation & Communication Excellence
**Read when user mentions: facilitation, workshops, communication, collaboration, writing**
- `workshop-facilitation.md` - Workshop design, facilitation techniques, group dynamics
- `writing-and-communication.md` - Professional communication, content strategy, messaging
- `virtual-collaboration.md` - Remote work strategy, virtual team management

### Knowledge Management & Learning Systems
**Read when user mentions: knowledge, learning, best practices, expertise, integration**
- `knowledge-management.md` - Knowledge systems, information management, organisational learning
- `best-practice-evolution.md` - Best practice development, methodological improvement
- `domain-expert-integration.md` - Expert knowledge integration, specialist collaboration
- `cross-domain-analysis.md` - Inter-disciplinary analysis, cross-functional integration
- `crowdsourced-validation.md` - Collective intelligence, crowd-based validation

### Advanced Thinking & Analysis Methods
**Read when user mentions: systems thinking, analogies, dialectical analysis, biomimetics, ethics**
- `systems-thinking.md` - Systems analysis, holistic thinking, complex system design
- `analogical-reasoning.md` - Analogy-based problem solving, pattern recognition
- `dialectical-thinking.md` - Dialectical analysis, paradox resolution, opposing viewpoints
- `biomimetic-strategy.md` - Nature-inspired solutions, biological pattern application
- `ethical-decision-making.md` - Ethics frameworks, moral reasoning, value-based decisions
- `trend-analysis.md` - Trend identification, pattern analysis, future indicators

### Personal & Productivity Enhancement
**Read when user mentions: productivity, time management, personal effectiveness**
- `time-management-and-productivity.md` - Productivity systems, time optimisation, efficiency methods

## Intelligent Routing Process

### 1. Request Analysis Protocol
```
BEFORE reading any reference files:
1. Analyse the user's request for key domain indicators
2. Identify the primary subject area(s) 
3. Map keywords to relevant reference file names
4. Select the most appropriate 1-3 reference files
```

### 2. File Access Protocol  
```
ONLY read reference files that match the user's specific request:
- For UI design requests → Read `user-interface-design.md`
- For API challenges → Read `api-design.md`  
- For strategic planning → Read `strategic-planning.md`
- For multi-domain requests → Read max 3 most relevant files
```

### 3. Application Protocol
```
After reading the relevant reference file(s):
1. Apply the specific frameworks from that skill
2. Use domain-specific terminology and methodologies
3. Leverage the specialised knowledge and best practices
4. Provide targeted, expert-level guidance
```

## Example Routing with File Access

**Your request:** *"Use your Brainstorming skill to support me with this technical user interface design. Looking at aesthetics, pattern and colour irregularities within the UI, as well as font shape/size/weight inconsistencies."*

**Orchestrator protocol:**
1. **Domain Analysis**: UI design, visual design, typography, colour systems
2. **File Selection**: `user-interface-design.md` (primary reference)
3. **Action**: Read `./references/user-interface-design.md`  
4. **Application**: Apply visual design frameworks, typography systems, colour theory

**Result**: Expert UI design guidance using the specific methodologies, frameworks, and best practices from the `user-interface-design.md` reference skill.

## Multi-Domain Integration Protocol

**Example request:** *"Help me brainstorm a digital transformation strategy that includes cybersecurity considerations and change management."*

**File access sequence:**
1. **Primary domain**: Read `./references/digital-strategy.md`
2. **Security aspects**: Read `./references/cybersecurity.md`  
3. **Change management**: Read `./references/change-management-psychology.md`

**Integration approach:**
- Lead with digital strategy framework  
- Integrate security-by-design principles
- Apply change psychology methodologies
- Synthesise into comprehensive approach

## Reference File Structure

Each reference file in `./references/` follows this structure:
```
# [Skill Name]
## Purpose - What this skill accomplishes
## Core Capabilities - Key areas of expertise  
## Implementation Framework - Practical methodologies
## Industry Applications - Real-world use cases
```

**Usage instruction**: Read the entire relevant reference file to understand the full scope of capabilities and frameworks available for that domain.

## Efficiency Guidelines

### When to Read Reference Files
- **ALWAYS read** when user request matches a specific domain
- **Read immediately** before providing specialised guidance
- **Read maximum 3 files** for complex multi-domain requests
- **Do not read** for general brainstorming that doesn't require domain expertise

### File Selection Criteria
```
1. Keyword matching: Match user's terminology to file names
2. Context analysis: Understand the underlying challenge 
3. Priority ranking: Select most relevant primary domain first
4. Scope assessment: Determine if multi-domain integration needed
```

### Response Protocol After Reading
```
1. Apply the specific frameworks from the reference skill
2. Use domain-appropriate terminology and concepts
3. Leverage specialised best practices and methodologies
4. Provide implementation guidance using the reference content
5. Maintain practical, actionable focus
```

## Foundation Principles

All specialised brainstorming maintains these core principles:

- **Evidence-Based Expertise** - Use proven frameworks from reference skills
- **Domain-Specific Knowledge** - Apply specialised terminology and concepts  
- **Practical Implementation** - Focus on actionable, realistic solutions
- **Progressive Refinement** - Build understanding through focused dialogue
- **Quality Standards** - Apply industry best practices from reference materials
- **Strategic Alignment** - Ensure solutions support broader objectives

**Remember**: This orchestrator is only as effective as its ability to access and apply the specialised knowledge stored in the `./references/` directory. Always read the relevant reference file(s) before providing domain-specific guidance.