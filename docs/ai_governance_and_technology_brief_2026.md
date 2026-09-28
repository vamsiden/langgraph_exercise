# Morgan Stanley Global Technology & Emerging Technologies Policy Brief
**Document Reference:** POL-ENG-AI-2026-V2  
**Publication Date:** June 10, 2026  
**Oversight Entity:** Global Technology Risk & Governance Committee; Data Protection Office  
**Classification:** Firmwide Operational & Regulatory Standard  

---

## 1. Overview & Scope
As outlined in Morgan Stanley's public disclosures and Section 6 of the U.S. Privacy Policy and Notice, the Firm leverages advanced automated computational systems, Machine Learning (ML), Natural Language Processing (NLP), and Generative Artificial Intelligence (GenAI) to drive operational leverage and optimize execution across its three core reporting segments: Institutional Securities, Wealth Management, and Investment Management.

This technical policy document sets binding standards for model ingestion, training boundaries, compute residency, and cross-border inference pipelines.

---

## 2. Infrastructure & Compute Architecture

### 2.1 Enclave Isolation and Cloud Regions
All production training, fine-tuning, and inference pipelines containing or processing institutional or retail customer telemetry run exclusively inside isolated Virtual Private Cloud (VPC) enclaves with mutual TLS (mTLS) enforcement.
* **Primary Region:** US East (Northern Virginia)
* **Secondary Disaster Recovery (DR) Region:** Europe Central (Frankfurt)

### 2.2 Cross-Border Data Ingestion and Telemetry
In accordance with Section 10 and Section 14 of the U.S. Privacy Policy and Notice, client communications and telemetry originating outside the United States may be transferred to and processed within the United States for computational execution, analytical modeling, and system monitoring.
* All international data transfers to U.S.-hosted AI inference engines require execution of Standard Contractual Clauses (SCCs) and approval from the Data Protection Office (`dataprotectionoffice@morganstanley.com`).
* Institutional clients and corporate plan administrators may audit cross-border transfer logs by submitting a formal request via the institutional ethics reporting desk (`www.morganstanleyethicspoint.com`).

---

## 3. Data Governance & Model Training Restrictions

| Data Category | Policy Status | Enforcement Mechanism |
| :--- | :--- | :--- |
| **Biometric Information** (voiceprints, facial geometry scans, palm scans) | **Strictly Prohibited** | Cryptographic tokenization & automated ingestion quarantine; prohibited from being used in pre-training or fine-tuning corpora. |
| **Authentication Credentials** (passwords, PINs, CVVs, security Q&As) | **Strictly Prohibited** | Edge-level masking and zero-log filters. |
| **Institutional Trading & Execution Telemetry** | **Permitted (Restricted)** | Anonymized order routing metadata permitted for execution latency optimization algorithms. |
| **Client Interaction Logs** (customer service text/chat interactions) | **Permitted (Conditional)** | Allowed solely for internal summarization and retrieval-augmented generation (RAG) agent tooling; sensitive PII scrubbed via redaction models. |

---

## 4. Segment-Specific Technology Allocations (2026 Directives)

Following the organizational realignment and workforce reductions enacted in Q1 2026, firmwide non-compensation technology spend has been reallocated toward the following initiatives:

* **Institutional Securities Group (ISG):** Deployment of ultra-low-latency deterministic execution pipelines in Equity Trading and credit-corporate pricing models.
* **Wealth Management (WM):** Scaling the automated portfolio rebalancing engine and integrating conversational assistant tools across the Workplace Solutions (Shareworks) and RIA channels.
* **Investment Management (IM):** Modernization of clearing interface architectures and automated risk-attribution pipelines across multi-asset private funds.