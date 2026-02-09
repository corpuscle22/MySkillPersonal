# System Architecture Overview: Diabetes Mellitus Identifier

## High-Level Architecture

The Diabetes Mellitus Identifier is a cloud-hosted clinical decision support service that integrates with EHR systems via CDS Hooks and SMART on FHIR protocols. The system evaluates patient laboratory data against ADA diagnostic criteria in real-time and returns actionable alerts to clinicians.

## Component Inventory

### Core Application Components

| Component | Technology | Purpose |
|-----------|------------|---------|
| CDS Hooks Service | Node.js/Express or Python/FastAPI | REST API handling hook requests/responses |
| Clinical Rules Engine | Drools, OpenCDS, or custom | Evaluates diagnostic criteria against patient data |
| FHIR Client | HAPI FHIR or custom | Queries EHR for additional patient data if needed |
| Alert Card Generator | Template engine | Formats CDS Hooks card responses |
| Audit Logger | Structured logging | Records all evaluations for compliance |
| Configuration Service | Key-value store | Manages feature flags, thresholds |

### Data Layer

| Component | Technology | Purpose |
|-----------|------------|---------|
| Audit Database | PostgreSQL | Stores evaluation history, overrides |
| Cache | Redis | Caches terminology lookups, patient context |
| Configuration Store | PostgreSQL/Consul | Stores rules configuration |

### Integration Layer

| Component | Protocol | Purpose |
|-----------|----------|---------|
| CDS Hooks Endpoint | HTTPS REST | Receives hook requests from EHR |
| FHIR Client | HTTPS REST | Queries FHIR server for data |
| OAuth 2.0 Client | HTTPS | Authenticates with EHR authorization server |
| HL7v2 Listener (optional) | MLLP/TCP | Receives lab results in real-time |

## Technology Stack

### Recommended Stack
```
┌─────────────────────────────────────────────────────────────┐
│                      Load Balancer                          │
│                     (AWS ALB / Azure LB)                    │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    API Gateway (Optional)                   │
│               (Kong / AWS API Gateway)                      │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    CDS Hooks Service                        │
│  ┌───────────────┐  ┌──────────────┐  ┌──────────────────┐ │
│  │  Express.js   │  │ Rules Engine │  │ Card Generator   │ │
│  │  (REST API)   │  │   (Custom)   │  │   (Handlebars)   │ │
│  └───────────────┘  └──────────────┘  └──────────────────┘ │
│                                                             │
│  ┌───────────────┐  ┌──────────────┐  ┌──────────────────┐ │
│  │ FHIR Client   │  │ OAuth Client │  │ Audit Logger     │ │
│  │  (Axios)      │  │   (OAuth2)   │  │   (Winston)      │ │
│  └───────────────┘  └──────────────┘  └──────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                       Data Layer                            │
│  ┌───────────────┐  ┌──────────────┐  ┌──────────────────┐ │
│  │  PostgreSQL   │  │    Redis     │  │  S3 (Backups)    │ │
│  │  (Audit DB)   │  │   (Cache)    │  │                  │ │
│  └───────────────┘  └──────────────┘  └──────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Scalability Considerations

### Horizontal Scaling
- CDS Hooks service is stateless; can scale horizontally
- Redis cluster for distributed caching
- PostgreSQL read replicas for audit queries

### Estimated Capacity
| Metric | Target |
|--------|--------|
| Concurrent requests | 1,000 |
| Response time (p95) | < 300ms |
| Daily evaluations | 500,000 |
| Audit data retention | 7 years |

## High Availability

### Multi-Zone Deployment
- Deploy across 2+ availability zones
- Database: Primary + synchronous standby
- Cache: Redis Cluster with 3 nodes minimum

### Failover Strategy
- Automatic health checks every 10 seconds
- Automatic failover to standby database
- Circuit breaker for EHR API calls

### Recovery Objectives
| Metric | Target |
|--------|--------|
| RPO (Recovery Point Objective) | 1 minute |
| RTO (Recovery Time Objective) | 5 minutes |
| Uptime SLA | 99.9% |

## Disaster Recovery

### Backup Strategy
- Database: Continuous WAL archiving + daily snapshots
- Configuration: Version-controlled in Git
- Audit logs: Replicated to separate region

### DR Site
- Warm standby in secondary region
- Automated failover via DNS (Route 53/Traffic Manager)
- Tested quarterly

## Performance Requirements

### Response Time SLAs
| Operation | Target | Maximum |
|-----------|--------|---------|
| CDS Hooks response | < 200ms | 500ms |
| FHIR query (with prefetch) | N/A | N/A |
| FHIR query (without prefetch) | < 100ms | 300ms |
| Audit log write | < 10ms | 50ms |

### Throughput
- 500 requests/second sustained
- 2,000 requests/second burst (30 seconds)

## Monitoring and Alerting

### Key Metrics
| Metric | Threshold | Action |
|--------|-----------|--------|
| Response time p95 | > 400ms | Alert on-call |
| Error rate | > 1% | Alert on-call |
| CPU utilization | > 80% | Auto-scale |
| Memory utilization | > 85% | Alert on-call |
| Database connections | > 80% pool | Alert on-call |

### Observability Stack
- **Metrics**: Prometheus + Grafana
- **Logs**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Traces**: Jaeger or AWS X-Ray
- **Alerts**: PagerDuty integration

## Security Architecture

See [security-architecture.md](security-architecture.md) for detailed security controls.

### Key Security Features
- OAuth 2.0 + SMART scopes for authentication
- TLS 1.3 for all connections
- PHI encryption at rest (AES-256)
- Audit logging of all access
- VPC isolation with private subnets
- WAF for application protection

## Deployment Architecture

### Kubernetes (Recommended)
```yaml
# Deployment topology
Namespace: diabetes-identifier
├── Deployment: cds-service (3 replicas)
├── Deployment: rules-engine (3 replicas)
├── Service: cds-service-lb (LoadBalancer)
├── ConfigMap: app-config
├── Secret: db-credentials
├── HPA: cds-service (min: 3, max: 10)
└── PDB: cds-service (minAvailable: 2)
```

### Serverless (Alternative)
- AWS Lambda for CDS Hooks handlers
- API Gateway for routing
- Aurora Serverless for database
- ElastiCache for Redis

## Integration Points

### Inbound
| Source | Protocol | Authentication |
|--------|----------|----------------|
| Epic | CDS Hooks / HTTPS | OAuth 2.0 Bearer |
| Cerner | CDS Hooks / HTTPS | OAuth 2.0 Bearer |
| HL7 Interface Engine | HL7v2 / MLLP | TLS + Client Cert |

### Outbound
| Destination | Protocol | Purpose |
|-------------|----------|---------|
| EHR FHIR Server | HTTPS | Query patient data |
| Terminology Server | HTTPS | Value set lookups |
| Notification Service | HTTPS | Escalation alerts |
| SIEM | Syslog/HTTPS | Security event forwarding |
