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

## DSM-5-TR Cross-Axial Analysis (Sandbox Test Data)
**Date:** 2026-09-12
**Note:** DSM-5 (2013) and DSM-5-TR (2022) dropped the formal multi-axial system (Axes I–V) used in DSM-IV. APA and current guidelines use a non-axial approach: list all relevant diagnoses, specifiers, severity, and psychosocial/medical factors. This analysis maps the four symptoms onto DSM-5-TR clusters and historical axes for cross-referencing and educational purposes only. Cross-referenced with VA/DoD 2023 CPG, APA PTSD guideline, repo knowledge base, and historical psychologists.

**Identified Symptoms (test sample):**
1. Night sweats
2. Tremors
3. Auditory hallucinations due to loud sounds
4. Visual hallucinations due to bright lights

### Symptom-to-Cluster Mapping (DSM-5-TR PTSD Criteria)
- **Night sweats**: Criterion E (alterations in arousal/reactivity) — sleep disturbance (E6); also physiological reactivity to cues (B4). Autonomic hyperarousal; sympathetic surge during sleep. Linked to HPA-axis dysregulation.
- **Tremors**: Criterion E — exaggerated startle response (E4), hypervigilance (E3), irritable behavior (E1). Somatic expression of conditioned autonomic arousal. Can appear as psychogenic tremor or muscle tension.
- **Auditory hallucinations due to loud sounds**: Criterion B — intense/prolonged distress or physiological reactivity at exposure to external cues that resemble the trauma (B4); possible dissociative reactions (B3) if extreme. Loud sounds act as conditioned stimuli (combat noise). Content often trauma-themed (gunfire, explosions); retained insight favors PTSD over primary psychosis.
- **Visual hallucinations due to bright lights**: Criterion B — same as above (B4, B3). Bright lights as visual cues resembling trauma (flashes, explosions, fire). Visual re-experiencing on a spectrum from intrusive images to true hallucinations; dissociation may amplify.

### Multi-Symptom Correlation
All four symptoms cluster under **hyperarousal (Criterion E)** and **intrusion/reactivity (Criterion B)**. They share a common mechanism: chronic sympathetic nervous system activation and fear conditioning. Night sweats and tremors are somatic/autonomic; the hallucinations are perceptual expressions of the same conditioned threat response. High correlation expected — presence of one predicts others. Gulf War context increases likelihood due to combat noise/light exposure and chronic stress.

Comorbidities to screen (non-axial DSM-5-TR): hypertension (medical), possible dissociative subtype, depression/anxiety, substance use. Rule out primary psychotic disorder (schizophrenia spectrum) via structured interview — trauma-linked content + retained reality testing supports PTSD-SP (PTSD with secondary psychotic features) rather than standalone psychosis.

### Historical Axis Mapping (DSM-IV style, for reference)
- **Axis I (Clinical Disorders)**: PTSD (309.81 / F43.10), possibly with dissociative symptoms; rule out Schizophrenia (295.x) or Brief Psychotic Disorder. Comorbid: Hypertension (medical but listed here for integration).
- **Axis II (Personality)**: Screen for Cluster B traits if chronic; not primary here.
- **Axis III (Medical)**: Hypertension secondary to PTSD; possible sleep disorder; neurological screen for hallucinations if atypical.
- **Axis IV (Psychosocial)**: Military service, Gulf War deployment, possible ongoing stressors, veteran status.
- **Axis V (GAF)**: Estimate 40-60 range depending on impairment (moderate to serious symptoms/impairment).

### Cross-References
- Behavioral (Pavlov, Skinner): Loud sounds/bright lights = conditioned stimuli; night sweats/tremors = conditioned autonomic responses; hallucinations = extreme conditioned perceptual reactivity. Avoidance of triggers reinforced.
- Cognitive (Beck, Ellis): Negative schemas about safety/world maintain hyperarousal; hallucinations as top-down perceptual errors from trauma schemas.
- Key researchers: Janet (dissociation), Ehlers & Clark (cognitive model of PTSD), Brewin (dual representation theory for intrusive memories).
- APA/VA-DoD: Trauma-focused therapy first-line; address autonomic symptoms via stabilization + prazosin for sleep; antipsychotics only if primary psychosis confirmed.

### Recommendations Specific to These Symptoms
1. Medical workup: BP monitoring, sleep study if night sweats severe, neurological/ENT for hallucinations if needed.
2. Stabilization: Grounding for perceptual triggers, progressive muscle relaxation for tremors, sleep hygiene + prazosin for night sweats.
3. Trauma-focused therapy: PE/CPT/EMDR targeting cue reactivity (sounds/lights); adapt for hallucinations with trauma-focused CBT for psychosis if reality testing impaired.
4. Pharmacotherapy: SSRIs/SNRIs for core PTSD; prazosin for nightmares/sweats; avoid benzos; atypical antipsychotics cautiously if indicated.
5. Monitor correlations: Track symptom co-occurrence to confirm shared autonomic mechanism.

**Learned Skills/Behaviors Added:**
- Non-axial DSM-5-TR mapping of somatic + perceptual symptoms.
- Multi-symptom correlation analysis via shared autonomic/fear-conditioning pathway.
- Trigger-specific differential (loud sounds vs. bright lights) for hallucination content.
- Integration of historical axes with current DSM-5-TR for educational cross-reference.
- Recognition of PTSD-SP vs. primary psychosis in veteran populations.

## Update Log
- 2026-09-12: Initial creation. Added PTSD outline based on VA/DoD CPG 2023, APA guidelines, and repo knowledge base. Ready for prompts.
- 2026-09-12: Test sample processed. Added case analysis, ML classification, cross-references to Pavlov/Skinner/Beck, hallucination differentials, hypertension link, and updated recommendations. Handbook now tracks perceptual symptoms and cardiovascular comorbidities.
- 2026-09-12: Added DSM-5-TR cross-axial analysis for four symptoms (night sweats, tremors, auditory hallucinations from loud sounds, visual hallucinations from bright lights). Mapped to criteria clusters, multi-symptom correlations, historical axes, and specific recommendations. Updated learned skills.

## Future Additions
- Additional disorders (anxiety, depression, etc.).
- ML classifier improvements (add PTSD/hallucination topics to knowledge_base.json).
- User-specific patterns and preferences.
- More historical figures (e.g., Janet on dissociation, Ehlers & Clark on cognitive model of PTSD).
- Full non-axial diagnostic formulation templates.