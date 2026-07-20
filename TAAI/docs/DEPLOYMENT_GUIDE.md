# Tech Assist AI - Deployment Guide

## Overview

This guide covers the complete deployment process for Tech Assist AI (TAAI), from infrastructure provisioning to go-live.

---

## Pre-Deployment Checklist

### 1. Azure Resource Requirements
- [ ] Azure subscription with sufficient quota
- [ ] Azure OpenAI access approved
- [ ] Azure Cognitive Search provisioned
- [ ] App Service Plan (Premium V3 or higher)
- [ ] PostgreSQL database (Flexible Server)
- [ ] Redis Cache instance
- [ ] Azure Key Vault for secrets
- [ ] Application Insights for monitoring

### 2. Access & Permissions
- [ ] Azure AD app registration completed
- [ ] Service principal with required RBAC roles
- [ ] Confluence API token generated
- [ ] SharePoint app credentials obtained
- [ ] ServiceNow API access configured

### 3. Code & Configuration
- [ ] Repository cloned
- [ ] Dependencies installed
- [ ] Environment variables configured
- [ ] Secrets stored in Azure Key Vault
- [ ] Database migrations prepared

---

## Phase 1: Infrastructure Setup (Week 1)

### 1.1 Provision Azure Resources

```bash
# Set variables
RESOURCE_GROUP="rg-taai-prod"
LOCATION="australiaeast"
PROJECT_NAME="taai"

# Create resource group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create Azure OpenAI
az cognitiveservices account create \
  --name "${PROJECT_NAME}-openai" \
  --resource-group $RESOURCE_GROUP \
  --kind OpenAI \
  --sku S0 \
  --location $LOCATION

# Deploy GPT-4 model
az cognitiveservices account deployment create \
  --name "${PROJECT_NAME}-openai" \
  --resource-group $RESOURCE_GROUP \
  --deployment-name gpt-4 \
  --model-name gpt-4 \
  --model-version "0613" \
  --model-format OpenAI \
  --scale-settings-scale-type "Standard"

# Deploy embedding model
az cognitiveservices account deployment create \
  --name "${PROJECT_NAME}-openai" \
  --resource-group $RESOURCE_GROUP \
  --deployment-name text-embedding-ada-002 \
  --model-name text-embedding-ada-002 \
  --model-version "2" \
  --model-format OpenAI \
  --scale-settings-scale-type "Standard"

# Create Cognitive Search
az search service create \
  --name "${PROJECT_NAME}-search" \
  --resource-group $RESOURCE_GROUP \
  --sku standard \
  --location $LOCATION

# Create PostgreSQL
az postgres flexible-server create \
  --name "${PROJECT_NAME}-db" \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --admin-user taai_admin \
  --admin-password '<SECURE_PASSWORD>' \
  --sku-name Standard_B2s \
  --tier Burstable \
  --storage-size 128 \
  --version 15

# Create database
az postgres flexible-server db create \
  --resource-group $RESOURCE_GROUP \
  --server-name "${PROJECT_NAME}-db" \
  --database-name taai_production

# Create Redis Cache
az redis create \
  --name "${PROJECT_NAME}-cache" \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --sku Standard \
  --vm-size C1

# Create App Service Plan
az appservice plan create \
  --name "${PROJECT_NAME}-plan" \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --is-linux \
  --sku P1V3

# Create App Service (API)
az webapp create \
  --name "${PROJECT_NAME}-api" \
  --resource-group $RESOURCE_GROUP \
  --plan "${PROJECT_NAME}-plan" \
  --runtime "PYTHON:3.11"

# Create Key Vault
az keyvault create \
  --name "${PROJECT_NAME}-kv" \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION

# Create Application Insights
az monitor app-insights component create \
  --app "${PROJECT_NAME}-insights" \
  --location $LOCATION \
  --resource-group $RESOURCE_GROUP \
  --application-type web
```

### 1.2 Configure Azure AD Authentication

```bash
# Register app in Azure AD
az ad app create \
  --display-name "Tech Assist AI" \
  --sign-in-audience AzureADMyOrg \
  --web-redirect-uris "https://taai.macquarie.com/auth/callback"

# Note the Application (client) ID and create client secret
# Store in Key Vault
```

### 1.3 Store Secrets in Key Vault

```bash
# OpenAI
az keyvault secret set \
  --vault-name "${PROJECT_NAME}-kv" \
  --name "AzureOpenAIKey" \
  --value "<your_openai_key>"

# Database
az keyvault secret set \
  --vault-name "${PROJECT_NAME}-kv" \
  --name "DatabaseURL" \
  --value "postgresql://user:pass@${PROJECT_NAME}-db.postgres.database.azure.com/taai_production"

# Confluence
az keyvault secret set \
  --vault-name "${PROJECT_NAME}-kv" \
  --name "ConfluenceToken" \
  --value "<your_confluence_token>"

# Continue for all secrets...
```

---

## Phase 2: Data Ingestion (Week 2)

### 2.1 Pull Confluence Data

```bash
# Run ingestion script
cd backend
python scripts/ingest_confluence.py \
  --spaces IT,TECHSUPPORT,INFOSEC \
  --output data/confluence_docs.jsonl
```

### 2.2 Pull SharePoint Data

```bash
python scripts/ingest_sharepoint.py \
  --site "https://macquarie.sharepoint.com/sites/TechAssist" \
  --list "Knowledge Base" \
  --output data/sharepoint_docs.jsonl
```

### 2.3 Process and Chunk Documents

```bash
python scripts/process_documents.py \
  --input data/confluence_docs.jsonl \
  --input data/sharepoint_docs.jsonl \
  --output data/processed_chunks.jsonl \
  --chunk-size 512 \
  --chunk-overlap 50
```

### 2.4 Generate Embeddings

```bash
python scripts/generate_embeddings.py \
  --input data/processed_chunks.jsonl \
  --output data/embeddings.jsonl \
  --batch-size 100
```

### 2.5 Index in Azure Cognitive Search

```bash
python scripts/index_documents.py \
  --input data/embeddings.jsonl \
  --index-name tech-assist-kb \
  --create-index
```

**Expected Results:**
- ~10,000-50,000 document chunks indexed
- Average indexing time: 2-4 hours
- Verify search functionality with test queries

---

## Phase 3: Application Deployment (Week 3)

### 3.1 Database Setup

```bash
# Run migrations
cd backend
alembic upgrade head

# Seed initial data (if needed)
python scripts/seed_database.py
```

### 3.2 Build and Deploy Backend

```bash
# Build Docker image
docker build -t taai-api:latest -f backend/Dockerfile backend/

# Tag for Azure Container Registry
docker tag taai-api:latest taai.azurecr.io/taai-api:latest

# Push to ACR
docker push taai.azurecr.io/taai-api:latest

# Deploy to App Service
az webapp config container set \
  --name "${PROJECT_NAME}-api" \
  --resource-group $RESOURCE_GROUP \
  --docker-custom-image-name taai.azurecr.io/taai-api:latest \
  --docker-registry-server-url https://taai.azurecr.io
```

### 3.3 Configure App Service Settings

```bash
# Set environment variables from Key Vault references
az webapp config appsettings set \
  --name "${PROJECT_NAME}-api" \
  --resource-group $RESOURCE_GROUP \
  --settings \
    AZURE_OPENAI_API_KEY="@Microsoft.KeyVault(SecretUri=https://${PROJECT_NAME}-kv.vault.azure.net/secrets/AzureOpenAIKey/)" \
    DATABASE_URL="@Microsoft.KeyVault(SecretUri=https://${PROJECT_NAME}-kv.vault.azure.net/secrets/DatabaseURL/)" \
    # ... other settings
```

### 3.4 Enable Managed Identity

```bash
# Enable system-assigned managed identity
az webapp identity assign \
  --name "${PROJECT_NAME}-api" \
  --resource-group $RESOURCE_GROUP

# Grant Key Vault access
IDENTITY_ID=$(az webapp identity show --name "${PROJECT_NAME}-api" --resource-group $RESOURCE_GROUP --query principalId -o tsv)

az keyvault set-policy \
  --name "${PROJECT_NAME}-kv" \
  --object-id $IDENTITY_ID \
  --secret-permissions get list
```

### 3.5 Deploy Frontend

```bash
# Build React app
cd frontend
npm install
npm run build

# Deploy to Azure Static Web Apps (or App Service)
az staticwebapp create \
  --name "${PROJECT_NAME}-web" \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --source ./build \
  --branch main
```

---

## Phase 4: Testing (Week 4)

### 4.1 Smoke Tests

```bash
# Test API health
curl https://taai-api.azurewebsites.net/health

# Test chat endpoint
curl -X POST https://taai-api.azurewebsites.net/api/v1/chat/message \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{
    "user_id": "test_user",
    "session_id": "test_session",
    "message": "How do I reset my password?"
  }'
```

### 4.2 Load Testing

```bash
# Using Apache Bench
ab -n 1000 -c 10 -T application/json -p payload.json \
  https://taai-api.azurewebsites.net/api/v1/chat/message

# Using Azure Load Testing
az load test create \
  --name "taai-load-test" \
  --resource-group $RESOURCE_GROUP \
  --load-test-config-file load-test-config.yaml
```

### 4.3 User Acceptance Testing (UAT)

**Test Scenarios:**
1. Password reset guidance
2. VPN troubleshooting
3. Email configuration
4. Software access request
5. Hardware request
6. Complex multi-step issue
7. Escalation to human agent
8. Feedback submission

**UAT Participants:**
- 20 Tech Assist team members
- 30 end users from various departments
- 5 IT admins

**Success Criteria:**
- 90%+ can complete basic tasks
- Average response time <5 seconds
- 4.0+ satisfaction score
- <5% error rate

---

## Phase 5: Pilot Launch (Week 5-6)

### 5.1 Pilot Group Selection

**Target Audience:**
- 500 users across Sydney, Melbourne, Brisbane
- Mix of technical and non-technical roles
- Early adopters and tech-savvy users
- Tech Assist team members

### 5.2 Pilot Kickoff

**Day 1:**
- Email announcement to pilot group
- Slack/Teams onboarding message
- Short demo video (2 minutes)
- Link to quick start guide

**Week 1:**
- Daily check-ins with Tech Assist team
- Monitor usage metrics closely
- Rapid bug fixes and adjustments
- Collect feedback via surveys

**Week 2:**
- Analyze pilot data
- Implement high-priority improvements
- Prepare for full rollout

### 5.3 Pilot Metrics

Track:
- Daily active users
- Messages per user
- Resolution rate
- Escalation rate
- User satisfaction (CSAT)
- Top issues/questions
- Error rates
- Performance metrics

**Success Criteria:**
- 50%+ pilot users try TAAI
- 60%+ resolution rate
- <40% escalation rate
- 4.0+ CSAT score
- <5% error rate
- <5s P95 response time

---

## Phase 6: Production Rollout (Week 7-8)

### 6.1 Marketing Campaign Launch

**Week 7:**
- Organization-wide email announcement (Monday 9 AM)
- Physical posters installed at all locations
- SharePoint front page banner goes live
- Yammer/Teams announcements
- Intranet news article
- Demo videos published

**Week 8:**
- Reminder emails
- Manager toolkits distributed
- Word-of-mouth campaign
- Lunch & learn sessions

### 6.2 Phased Rollout Strategy

```
Week 7:
- Day 1-2: Sydney offices (5,000 users)
- Day 3-4: Melbourne offices (3,000 users)
- Day 5: Brisbane & other locations (2,000 users)

Week 8:
- Monitor and stabilize
- Rapid response to issues
- Scale infrastructure as needed
```

### 6.3 Support Plan

**Tier 1 (TAAI itself):**
- Handles routine queries
- Available 24/7
- Auto-escalates when needed

**Tier 2 (Tech Assist):**
- Handles escalations
- Complex technical issues
- TAAI training and feedback

**Tier 3 (Development Team):**
- Bug fixes
- Performance optimization
- Feature enhancements
- On-call rotation (24/7)

---

## Phase 7: Monitoring & Optimization (Ongoing)

### 7.1 Monitoring Setup

**Azure Application Insights:**
```bash
# Configure alerts
az monitor metrics alert create \
  --name "High Error Rate" \
  --resource-group $RESOURCE_GROUP \
  --scopes "/subscriptions/{subscriptionId}/resourceGroups/${RESOURCE_GROUP}/providers/Microsoft.Web/sites/${PROJECT_NAME}-api" \
  --condition "avg Percentage Error > 5" \
  --window-size 5m \
  --evaluation-frequency 1m \
  --action email <email>
```

**Key Metrics:**
- Request rate (req/sec)
- Response time (P50, P95, P99)
- Error rate (%)
- Token usage (OpenAI)
- Database connection pool
- Redis cache hit rate
- Queue depth (ServiceNow)

**Dashboards:**
1. **Operations Dashboard**
   - System health
   - Performance metrics
   - Error logs
   - Active users

2. **Business Dashboard**
   - Daily active users
   - Total conversations
   - Resolution rate
   - User satisfaction
   - Cost per query

3. **Quality Dashboard**
   - Confidence scores
   - Top queries
   - Failed searches
   - Feedback sentiment

### 7.2 Continuous Improvement

**Weekly:**
- Review top escalated queries
- Identify knowledge gaps
- Update documentation
- Fine-tune prompt engineering

**Monthly:**
- User feedback analysis
- A/B testing results
- Performance optimization
- Cost optimization

**Quarterly:**
- Major feature releases
- Model updates (GPT-4 → GPT-4.5)
- Knowledge base refresh
- Strategic roadmap review

---

## Rollback Plan

If critical issues arise during rollout:

### Rollback Procedure

```bash
# 1. Stop traffic to TAAI
az webapp stop --name "${PROJECT_NAME}-api" --resource-group $RESOURCE_GROUP

# 2. Redirect users to Tech Assist
# Update DNS or load balancer

# 3. Restore previous version
az webapp deployment slot swap \
  --name "${PROJECT_NAME}-api" \
  --resource-group $RESOURCE_GROUP \
  --slot staging \
  --action swap

# 4. Communicate to users
# Send email explaining temporary unavailability

# 5. Debug and fix issues in staging

# 6. Re-deploy when ready
```

**Rollback Criteria:**
- Error rate >10%
- Response time >30 seconds
- Security incident
- Data loss/corruption
- Critical bug affecting >50% of users

---

## Post-Deployment Checklist

- [ ] All services running and healthy
- [ ] Monitoring and alerts configured
- [ ] Documentation updated
- [ ] Team trained on support procedures
- [ ] Runbooks created for common issues
- [ ] Backup and disaster recovery tested
- [ ] Performance baselines established
- [ ] User feedback mechanisms in place
- [ ] Marketing materials deployed
- [ ] Success metrics tracking automated

---

## Troubleshooting Common Issues

### Issue: Slow Response Times

**Diagnosis:**
```bash
# Check App Service metrics
az monitor metrics list \
  --resource "/subscriptions/{subscriptionId}/resourceGroups/${RESOURCE_GROUP}/providers/Microsoft.Web/sites/${PROJECT_NAME}-api" \
  --metric "AverageResponseTime" \
  --interval PT1M

# Check Redis cache
az redis show \
  --name "${PROJECT_NAME}-cache" \
  --resource-group $RESOURCE_GROUP \
  --query "redisVersion,sslPort"
```

**Solutions:**
- Scale up App Service
- Optimize database queries
- Increase Redis cache size
- Add CDN for static assets

### Issue: High Error Rate

**Diagnosis:**
```bash
# Check application logs
az webapp log tail --name "${PROJECT_NAME}-api" --resource-group $RESOURCE_GROUP

# Check Application Insights
az monitor app-insights metrics show \
  --app "${PROJECT_NAME}-insights" \
  --resource-group $RESOURCE_GROUP \
  --metric "requests/failed"
```

**Solutions:**
- Review error logs for patterns
- Check Azure OpenAI quota
- Verify database connections
- Check external API availability

### Issue: Low Accuracy

**Diagnosis:**
- Review low-confidence responses
- Analyze user feedback
- Check search relevance scores

**Solutions:**
- Improve document chunking
- Enhance prompt engineering
- Add more training data
- Fine-tune embedding model

---

## Disaster Recovery

### Backup Strategy

**Daily:**
- PostgreSQL automated backups (7-day retention)
- Azure Cognitive Search index snapshot

**Weekly:**
- Full system configuration backup
- Export conversation history

**Monthly:**
- Disaster recovery drill

### Recovery Procedures

**RTO: 15 minutes**
**RPO: 1 hour**

```bash
# Restore database
az postgres flexible-server restore \
  --resource-group $RESOURCE_GROUP \
  --name "${PROJECT_NAME}-db-restored" \
  --source-server "${PROJECT_NAME}-db" \
  --restore-point-in-time "2024-01-15T10:00:00Z"

# Restore search index
python scripts/restore_index.py \
  --backup-file backups/index-2024-01-15.json \
  --index-name tech-assist-kb
```

---

## Contacts

**Project Team:**
- Product Owner: [Name] <email>
- Tech Lead: [Name] <email>
- DevOps Engineer: [Name] <email>
- On-Call: [Phone]

**Escalation Path:**
1. Development Team → 15 min response
2. Tech Lead → 30 min response
3. Engineering Manager → 1 hour response
4. CTO → 4 hour response

**Support Channels:**
- Slack: #taai-support
- Email: tech-assist-ai@macquarie.com
- Phone: (on-call rotation)

---

## Success Criteria

### Technical
- ✅ 99.9% uptime
- ✅ <5s P95 response time
- ✅ <1% error rate
- ✅ API rate limits enforced

### Business
- ✅ 10,000+ active users in first month
- ✅ 60%+ resolution rate
- ✅ <40% escalation rate
- ✅ 4.5+ CSAT score
- ✅ 40%+ reduction in Tech Assist ticket volume

### Operational
- ✅ Automated deployments
- ✅ Comprehensive monitoring
- ✅ Incident response playbooks
- ✅ Team trained and confident

---

**Deployment complete! 🚀**

Monitor closely for the first 48 hours and be prepared to iterate quickly based on user feedback.
