# Psychology Handbook

## Purpose
Living document for tracking learned skills, behaviors, assessment frameworks, and cross-references to historical psychologists. Updated from questions, GitHub MD files, and evidence-based sources. Used to improve psychological assessment abilities over time.

## Core Principles
- Always cross-reference with repo files: behavioral-psychology.md, cognitive-psychology.md, key-concepts.md, key-researchers.md, knowledge_base.json.
- Log new questions and insights in question_log.md.
- Prioritize evidence-based approaches (e.g., VA/DoD, APA guidelines).
- Note limitations: not a licensed clinician; for educational/guidance purposes only.
- For test/sandbox data only unless explicitly stated otherwise.

## PTSD Assessment & Treatment Outline (Initial)
### 1. Assessment
- Screen for trauma history and symptoms using validated tools (e.g., PCL-5).
- Rule out acute safety risks (suicide, self-harm, ongoing danger).
- Assess comorbidities (depression, substance use, sleep disorders).
- Consider cultural, developmental, and contextual factors.
- Differential for hallucinations: trauma-related vs. primary psychotic disorder (content tied to trauma, retained insight favors PTSD).

### 2. Psychoeducation
- Explain common trauma reactions (hyperarousal, avoidance, re-experiencing, negative cognitions).
- Normalize symptoms without pathologizing.
- Introduce the treatment model (e.g., fear conditioning, cognitive processing).

### 3. Stabilization & Skills
- Grounding techniques, breathing, affect regulation.
- Safety planning if needed.
- Build therapeutic alliance and trust.
- Address physiological arousal (hypertension) via medical referral + relaxation.

### 4. Trauma-Focused Therapy (First-Line per VA/DoD 2023 & APA)
- **Prolonged Exposure (PE)**: In-vivo and imaginal exposure to trauma cues; 8-15 sessions.
- **Cognitive Processing Therapy (CPT)**: Identify and challenge stuck points (e.g., self-blame, safety beliefs).
- **EMDR**: Bilateral stimulation to process trauma memories.
- Typically 8-16 sessions, manualized, delivered by trained providers.
- Adapt for hallucinations: target trauma-linked perceptual experiences; consider trauma-focused CBT for psychosis if needed.

### 5. Pharmacotherapy (if psychotherapy not feasible or as adjunct)
- SSRIs: sertraline, paroxetine (FDA-approved for PTSD).
- SNRI: venlafaxine.
- For sleep/nightmares: prazosin (suggested, not strong).
- Avoid benzodiazepines (strong against).
- For severe hallucinations with impaired reality testing: consider atypical antipsychotics per psychosis guidelines (e.g., risperidone, quetiapine) — but only after ruling out primary psychosis.
- Monitor blood pressure; SSRIs/SNRIs can have cardiovascular effects.

### 6. Relapse Prevention & Maintenance
- Review progress, consolidate gains.
- Plan for triggers and setbacks.
- Step-down or booster sessions.

### 7. Cross-References
- Behavioral: Classical/operant conditioning (Pavlov, Skinner) — trauma as conditioned fear response; hyperarousal as conditioned autonomic response.
- Cognitive: Schema theory, cognitive distortions (Beck, Ellis) — maladaptive beliefs post-trauma; hallucinations as top-down perceptual errors.
- Key researchers: Ebbinghaus (memory), Piaget (development), others as relevant.
- Gulf War context: Higher rates of PTSD, hypertension, and somatic symptoms reported in veterans.

## Test Sample Case Analysis (Sandbox Only)
**Date:** 2026-09-12
**Sample:** Military personnel, Gulf War veteran. Symptoms: "shell shock," recurring anxiety, inability to control symptoms, high blood pressure, auditory hallucinations, visual hallucinations. Framed as PTSD.

**ML Classification (from ml_framework.py):**
- Top document: behavioral-psychology.md (strong match on conditioning, anxiety, stimulus-response).
- Secondary: cognitive-psychology.md (perception, memory, hallucinations as perceptual/cognitive phenomena).
- Relevant researchers: Ivan Pavlov, B.F. Skinner, Aaron Beck, Albert Ellis, Jean Piaget.
- Matched topics: classical conditioning, operant conditioning, reinforcement, schema, perception, memory.

**Key Insights from Cross-Reference:**
- Shell shock = historical term for combat-related PTSD/acute stress (WWI era); modern equivalent is PTSD with hyperarousal.
- Hallucinations in PTSD: Common (auditory up to ~40%, visual ~30% in some samples); often trauma-themed, with retained insight. Distinguish from schizophrenia by content linkage and reality testing.
- Hypertension: Strongly associated with chronic PTSD via sympathetic nervous system activation (catecholamines). Gulf War veterans show elevated rates.
- Treatment priority: Stabilize physiology (BP), rule out primary psychosis, then trauma-focused therapy. PE/CPT/EMDR remain first-line; adapt for perceptual symptoms.
- Behavioral lens: Fear conditioning (Pavlov) explains re-experiencing and hyperarousal; avoidance reinforced (Skinner).
- Cognitive lens: Negative appraisals and schemas (Beck) maintain symptoms; hallucinations may reflect intrusive trauma memories processed as perception.

**Recommendations Summary:**
1. Full assessment: PCL-5, trauma narrative, medical eval for BP, psychosis screen (e.g., SCID or PANSS if indicated).
2. Stabilize: Medical management of hypertension, grounding, safety plan.
3. Psychoeducation on trauma reactions and conditioning model.
4. Trauma-focused therapy: PE, CPT, or EMDR (8-16 sessions). For hallucinations, use trauma-focused approaches or adapted CBT for psychosis.
5. Meds: Sertraline/paroxetine/venlafaxine; prazosin for nightmares. Avoid benzos. Antipsychotics only if primary psychosis confirmed.
6. Monitor cardiovascular and perceptual symptoms throughout.
7. Relapse prevention focused on trigger identification and autonomic regulation.

**Learned Skills/Behaviors Added:**
- Differential diagnosis for trauma-related vs. primary hallucinations.
- Integration of physiological (BP) and psychological symptoms in PTSD.
- Adaptation of first-line therapies for perceptual disturbances.
- Gulf War-specific comorbidity awareness.

## Update Log
- 2026-09-12: Initial creation. Added PTSD outline based on VA/DoD CPG 2023, APA guidelines, and repo knowledge base. Ready for prompts.
- 2026-09-12: Test sample processed. Added case analysis, ML classification, cross-references to Pavlov/Skinner/Beck, hallucination differentials, hypertension link, and updated recommendations. Handbook now tracks perceptual symptoms and cardiovascular comorbidities.

## Future Additions
- Additional disorders (anxiety, depression, etc.).
- ML classifier improvements (add PTSD/hallucination topics to knowledge_base.json).
- User-specific patterns and preferences.
- More historical figures (e.g., Janet on dissociation, Ehlers & Clark on cognitive model of PTSD).