# Tech Assist AI (TAAI)

## Problem Statement

**Current Pain Points:**
- Long wait times at Tech Assist kiosks with no live queue visibility
- Unpredictable phone queue wait times
- Users placed on indefinite hold or offered callbacks
- Tech Assist overwhelmed with repetitive, simple queries
- No 24/7 self-service support option

**Impact:**
- Reduced employee productivity due to tech delays
- Inefficient use of Tech Assist resources
- Poor user experience and satisfaction

---

## Solution: Tech Assist AI (TAAI)

An intelligent chatbot powered by Azure OpenAI that provides instant, 24/7 tech support by surfacing knowledge from Confluence and SharePoint documentation.

### Key Features

1. **Instant Answers** - No wait times, available 24/7
2. **Context-Aware Responses** - RAG-powered search across internal knowledge bases
3. **Smart Escalation** - Seamlessly escalate to human agents when needed
4. **Live Queue Visibility** - Real-time kiosk availability tracking
5. **Multi-Channel Access** - Web, Teams, SharePoint integration

---

## Value Proposition

### For Employees
- ✅ Instant answers to common tech questions
- ✅ No waiting in queues for simple issues
- ✅ 24/7 availability
- ✅ Consistent, accurate information

### For Tech Assist
- ✅ Reduced repetitive queries (estimated 40-60% reduction)
- ✅ More time for complex technical issues
- ✅ Better resource allocation
- ✅ Improved service quality

### For Organisation
- ✅ Increased employee productivity
- ✅ Reduced operational costs
- ✅ Better knowledge management
- ✅ Data-driven insights on common issues

---

## System Architecture

### Technology Stack

**Backend:**
- Python 3.11+
- FastAPI (REST API)
- LangChain (RAG orchestration)
- Azure OpenAI (GPT-4)
- Azure Cognitive Search (vector search)
- PostgreSQL (conversation history)

**Frontend:**
- React 18 with TypeScript
- Tailwind CSS (Macquarie design system)
- WebSocket (real-time chat)
- React Query (state management)

**Infrastructure:**
- Azure App Service
- Azure Cognitive Search
- Azure OpenAI Service
- Azure Key Vault (secrets)

### Data Sources
1. **Confluence** - IT documentation and guides
2. **SharePoint** - Tech Assist knowledge base
3. **ServiceNow** - Ticket history (for training)
4. **Queue System** - Real-time kiosk availability

---

## How It Works

### User Flow
```
1. User opens TAAI chatbot
2. Types question (e.g., "How do I reset my VPN?")
3. TAAI searches Confluence + SharePoint via RAG
4. Returns contextual answer with source links
5. If unresolved → escalate to Tech Assist
```

### RAG Pipeline
```
Query → Embedding → Vector Search → Context Retrieval →
LLM Generation → Response + Citations
```

---

## Implementation Plan

### Phase 1: MVP (4-6 weeks)
- [ ] Set up Azure OpenAI integration
- [ ] Ingest Confluence/SharePoint data
- [ ] Build basic chat interface
- [ ] Implement RAG pipeline
- [ ] Deploy beta to pilot group

### Phase 2: Enhancement (4 weeks)
- [ ] Live queue tracking integration
- [ ] Microsoft Teams bot
- [ ] Conversation analytics dashboard
- [ ] User feedback mechanism

### Phase 3: Scale (4 weeks)
- [ ] Organisation-wide rollout
- [ ] Multi-language support
- [ ] Advanced analytics
- [ ] Continuous learning pipeline

---

## Marketing & Adoption Strategy

### Launch Campaign

**Week 1-2: Awareness**
- Macquarie-wide Outlook announcement
- Physical posters at Tech Assist kiosks
- Yammer/Teams posts with demo video

**Week 3-4: Pilot**
- Tech Assist SharePoint front page banner
- Pilot with 500 early adopters
- Gather feedback and iterate

**Week 5-6: Rollout**
- Full organisation launch
- Tech Assist kiosk integration
- Word-of-mouth via champions network

### Marketing Materials
1. **Email Template** - Outlook announcement
2. **Poster** - Physical kiosk signage
3. **Demo Video** - 60-second explainer
4. **SharePoint Banner** - Interactive widget
5. **Quick Start Guide** - 1-pager PDF

---

## Success Metrics

### KPIs
- **Resolution Rate**: % of queries resolved without escalation (Target: 60%)
- **Response Time**: Avg time to first response (Target: <3 seconds)
- **User Satisfaction**: CSAT score (Target: 4.5/5)
- **Deflection Rate**: % reduction in Tech Assist tickets (Target: 40%)
- **Adoption Rate**: Active users per month (Target: 10,000 in 6 months)

### Monitoring
- Real-time chat analytics dashboard
- Weekly usage reports
- Monthly NPS surveys
- Quarterly business impact review

---

## Security & Compliance

- **Authentication**: Azure AD SSO
- **Data Privacy**: Zero data retention for sensitive info
- **Encryption**: TLS 1.3 for all communications
- **Audit Logs**: Full conversation tracking
- **Access Control**: Role-based permissions

---

## Project Team

- **Product Owner**: TBD
- **Tech Lead**: TBD
- **Full-Stack Engineer**: TBD
- **AI Engineer**: TBD
- **UX Designer**: TBD
- **Change Manager**: TBD

---

## Next Steps

1. **Secure stakeholder approval** - Present business case to Tech Assist leadership
2. **Provision Azure resources** - Set up OpenAI, Cognitive Search
3. **Begin data ingestion** - Connect to Confluence/SharePoint
4. **Build MVP** - 4-week sprint to working prototype
5. **Pilot launch** - Beta with 100 Tech Assist users

---

## Contact

For questions or feedback, reach out to:
- **Product Team**: [tech-assist-ai@macquarie.com]
- **Tech Support**: [Submit a ticket]

---

**Built with ❤️ by the Digital Innovation Team**
