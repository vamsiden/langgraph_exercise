Here are targeted questions designed to test a LangGraph-based workflow across the 4 documents (`2q2026_earnings_report.md`, `privacy_policy_notice.md`, `ai_governance_and_technology_brief_2026.md`, and `global_workforce_restructuring_memo_mar2026.md`).

They range from straightforward 2-hop checks to complex 3-hop synthesis problems, complete with evaluation criteria and expected answers.

---

### Question 1: Workplace IPO Inflows & CPRA Rights

* **Complexity:** 2-Hop
* **Required Documents:** `2q2026_earnings_report.md` + `privacy_policy_notice.md`


* **Prompt:**
> *"According to the Q2 2026 earnings results, how much in net new assets was driven by the Workplace channel, and if a customer who joined through that channel wants to exercise their California rights to delete their data, what contact method must they use and what major categories of personal financial information are exempt from deletion?"*


* **Evaluation Criteria:**
* Agent retrieves Wealth Management net new assets ($148.1 billion total) and notes that just over half (~$74+ billion) originated from IPOs in the Workplace channel.


* Agent identifies **Shareworks by Morgan Stanley** as the specific service brand and provides its contact path: **Telephone +1 (866) 722-7310** or the **Wealth Management Privacy Center** web form.
* Agent extracts the exemption under Section 5.2: information collected when applying for or obtaining a financial product or service for personal, family, or household purposes (GLBA-covered data) is excluded from CPRA deletion rights.



---

### Question 2: Operational Efficiency, Severance Charges, and Headcount Flow

* **Complexity:** 2-Hop / Reconciliation
* **Required Documents:** `2q2026_earnings_report.md` + `global_workforce_restructuring_memo_mar2026.md`


* **Prompt:**
> *"Analyze the workforce management action of 2026: Detail the pre-tax severance charge allocated to each of the three business segments, identify what percentage of the workforce was impacted, and trace the worldwide headcount changes from December 31, 2025 to June 30, 2026."*


* **Evaluation Criteria:**
* Total pre-tax severance: **$178 million**.


* Segment breakdown:
* Institutional Securities: **$94 million**

* Wealth Management: **$61 million**

* Investment Management: **$23 million**



* Percentage impacted: **~2.0%** of global workforce (~1,600 employees).


* Headcount progression:
* Dec 31, 2025: **84,210** employees
* Mar 31, 2026: **83,922** employees


* Jun 30, 2026: **82,944** employees







---

### Question 3: Strategic Reinvestment into AI and Technology

* **Complexity:** 3-Hop
* **Required Documents:** `2q2026_earnings_report.md` + `global_workforce_restructuring_memo_mar2026.md` + `ai_governance_and_technology_brief_2026.md`


* **Prompt:**
> *"How did the savings achieved from the Q1 2026 workforce restructuring influence Morgan Stanley's Q2 2026 operating efficiency ratio, and specifically what technology capabilities were funded across the Institutional Securities and Wealth Management divisions as a result?"*


* **Evaluation Criteria:**
* Connects the severance action to maintaining the **65% expense efficiency ratio** for both Q2 and 1H 2026 (improved from 71% in 2Q 2025).


* Notes that non-compensation expenses increased in Q2 2026 across both segments partly due to strategic technology spend.


* Identifies the exact platform initiatives from the AI Governance brief:
* **Institutional Securities Group (ISG):** Ultra-low-latency deterministic execution pipelines for Equity Trading and credit-corporate pricing models.
* **Wealth Management (WM):** Scaling the automated portfolio rebalancing engine and integrating conversational assistant tools across Workplace Solutions (Shareworks) and RIA channels.





---

### Question 4: Biometric Data Boundary & Model Governance

* **Complexity:** 2-Hop
* **Required Documents:** `privacy_policy_notice.md` + `ai_governance_and_technology_brief_2026.md`
* **Prompt:**
> *"Under Morgan Stanley's U.S. Privacy Policy, what types of biometric information does the firm collect, and under what circumstances may this biometric data be used to train or fine-tune internal Generative AI or machine learning models?"*


* **Evaluation Criteria:**
* Identifies the biometric categories listed in Section 1 of the Privacy Policy: **voiceprints, fingerprints, facial images, and palm scans**.
* Recognizes the restriction in Section 3 of the AI Governance Brief: Biometric information is **strictly prohibited** from model training or fine-tuning, protected by cryptographic tokenization and automated ingestion quarantines.



---

### Question 5: Cross-Border Inferences and Institutional Audits

* **Complexity:** 2-Hop
* **Required Documents:** `privacy_policy_notice.md` + `ai_governance_and_technology_brief_2026.md`
* **Prompt:**
> *"If an institutional client located in Europe has telemetry data processed by Morgan Stanley's AI pipelines in the U.S., what cloud regions host this workload, what governance approval is mandatory, and where can the client submit an audit request regarding these cross-border transfers?"*


* **Evaluation Criteria:**
* Cloud infrastructure: Primary enclave in **US East (Northern Virginia)** with DR in **Europe Central (Frankfurt)**.
* Transfer requirements: Standard Contractual Clauses (SCCs) and formal sign-off from the **Data Protection Office** (`dataprotectionoffice@morganstanley.com`).
* Institutional audit portal: The institutional ethics reporting portal at **`[www.morganstanleyethicspoint.com](https://www.morganstanleyethicspoint.com)`** (as cross-referenced in Section 2.2 of the Brief and Section 5.3 of the Privacy Notice).



---

### Question 6: Employee Data Retention vs. Consumer Rights

* **Complexity:** 2-Hop
* **Required Documents:** `privacy_policy_notice.md` + `global_workforce_restructuring_memo_mar2026.md`
* **Prompt:**
> *"Can an employee laid off during the March 2026 workforce restructuring use the California Consumer Privacy Act (CPRA) consumer portal to delete their historical payroll and performance records? Explain the governing policy and retention timeline."*


* **Evaluation Criteria:**
* **No.** Consumer privacy disclosures under the U.S. Privacy Policy explicitly state that employee/contractor data is covered by a **separate notice** and does not fall under retail consumer request procedures.
* The Workforce Restructuring Memo specifies that personnel, payroll, and review files are bound by the **Employee & Contractor Privacy Notice** and held under mandatory statutory recordkeeping rules (typically **7 years**).
* System access is revoked upon separation, and any inquiries regarding employee files must go directly to `dataprotectionoffice@morganstanley.com`.



---

### Suggested Scoring Rubric for LangGraph Workflows

| Metric | Passing Threshold | Description |
| --- | --- | --- |
| **Document Routing Accuracy** | $\ge 90\%$ | Agent correctly identifies and queries only the relevant documents without cross-polluting search context. |
| **Multi-Hop Synthesis** | $100\%$ | Agent does not prematurely stop after retrieving the first document chunk; successfully links entities across hops. |
| **Numerical Consistency** | Exact Match | Severance numbers ($178M, $94M, $61M, $23M), asset flows ($148B), and phone numbers match verbatim.

 |