# Evaluation Set

## Case 1 - Normal Case
**Input:**  
Team discussed launching a student ambassador campaign next month. Sarah will draft the outreach email by Friday. Mike will prepare the budget estimate by Monday. The team will review progress next Wednesday.

**Good output should:**  
Clearly summarize the meeting and list all action items with the correct owners and deadlines.

---

## Case 2 - Normal Case
**Input:**  
Customer success team met to discuss onboarding delays. The main issue is that new clients are not submitting documents on time. Jenny will redesign the onboarding checklist. Alex will send reminder emails to clients.

**Good output should:**  
Accurately capture the main issue and provide clear action items for Jenny and Alex without adding extra assumptions.

---

## Case 3 - Edge Case
**Input:**  
marketing?? sales down maybe?? support issues again  
need fix asap  
who owns this?? not sure  
maybe next week talk again  

**Good output should:**  
Handle fragmented and unclear notes without inventing details, provide only a high-level summary, and indicate that responsibilities and action items are not clearly defined.

---

## Case 4 - Likely Hallucination Case
**Input:**  
The team briefly mentioned vendor pricing, legal review, and a possible rollout plan, but no final decisions were made. Someone may follow up next week.

**Good output should:**  
Avoid inventing owners, deadlines, or decisions that were not stated. It should stay cautious and only reflect the limited information provided.

---

## Case 5 - Needs Human Review / Failure-Prone Case
**Input:**  
John may contact the vendor, or maybe Lisa already did. Budget might be around $8,000, but I am not sure if that was for Q2 or Q3. Someone should check legal before rollout, but the timing was not confirmed.

**Good output should:**  
Handle uncertain and conflicting details carefully, avoid presenting them as facts, and indicate that human review is needed before relying on the output.
