---
name: shastra-wisdom
description: Deep research into Hindu scriptures (Vedas, Upanishads, Shruti, Smriti, Bhagavad Gita, Brahma Sutras, Puranas, Itihasas, Dharma Shastras, Agamas, and all other authentic Hindu texts) to find direct verses with English translations and metaphorical/practical interpretations for modern life. Use when the user asks a life question, seeks guidance on a situation, wants scriptural references on any topic, asks about Hindu philosophy, wants Vedic wisdom on a matter, or requests verses from specific scriptures. Triggers include questions like "What do the Vedas say about...", "scriptural guidance on...", "Hindu perspective on...", "Vedic wisdom for...", "What does Dharma say about...", or any question where the user wants authentic Hindu scriptural verses cited with translations and modern applicability. Only uses interpretations from authentic Hindu scholars and acharyas; excludes anti-Hindu distortions.
---

# Shastra Wisdom — Hindu Scripture Deep Research

Research all authentic Hindu scriptures to find direct verses, their translations, and their metaphorical/practical interpretation for the user's question, situation, or topic. Return cited verses with source, translator/commentator attribution, and modern-life applicability.

## Scripture Hierarchy

Search scriptures in this priority order. ALL categories must be searched; Vedas get highest weight in the final output.

### Tier 1 — Shruti (Revealed, Highest Authority)
1. **Rigveda** — Hymns of knowledge, cosmic order, dharma
2. **Yajurveda** (Shukla & Krishna) — Ritual formulas, ethics, duty
3. **Samaveda** — Melodies, devotion, aesthetics, inner harmony
4. **Atharvaveda** — Healing, daily life, protection, practical wisdom
5. **Principal Upanishads** (Isha, Kena, Katha, Prashna, Mundaka, Mandukya, Taittiriya, Aitareya, Chandogya, Brihadaranyaka) — Philosophical essence, Brahman, Atman, liberation
6. **Minor Upanishads** (Shvetashvatara, Kaushitaki, Maitri, etc.) — Specialized philosophical topics

### Tier 2 — Core Smriti (Remembered, High Authority)
7. **Bhagavad Gita** — Dharma in action, synthesis of Yoga paths
8. **Brahma Sutras** — Systematic Vedantic philosophy
9. **Ramayana** (Valmiki) — Dharma in conduct, ideal character
10. **Mahabharata** (including Shanti Parva, Anushasana Parva, Vidura Niti, Bhishma's teachings) — Comprehensive dharmic guidance

### Tier 3 — Dharma Literature & Puranas
11. **Manusmriti** — Social order, duties (use with contextual interpretation)
12. **Yajnavalkya Smriti** — Legal and ethical frameworks
13. **Vishnu Purana, Bhagavata Purana, Shiva Purana, Markandeya Purana** — Devotional wisdom, cosmology, stories with moral teaching
14. **Other Puranas** (Garuda, Padma, Vayu, Matsya, etc.)
15. **Arthashastra** (Kautilya) — Governance, statecraft, practical wisdom

### Tier 4 — Specialized Texts
16. **Yoga Sutras** (Patanjali) — Mind, meditation, self-discipline
17. **Agamas & Tantras** — Temple worship, ritual, esoteric practices
18. **Thirukkural** (Tamil Veda) — Ethics, virtue, practical life
19. **Narada Bhakti Sutras, Shandilya Bhakti Sutras** — Devotion
20. **Panchadashi, Vivekachudamani** — Advaita Vedanta practice
21. **Works of Alvars and Nayanars** — Tamil devotional classics

## Trusted Commentators & Interpreters

ONLY use interpretations from these categories of scholars. If quoting an interpretation, attribute it.

See `references/trusted-scholars.md` for the complete list of trusted and excluded scholars with rationale.

### Quick Reference — Trusted Schools
- **Advaita**: Adi Shankaracharya, Swami Vivekananda, Swami Chinmayananda, Sri Aurobindo
- **Vishishtadvaita**: Ramanujacharya, Vedanta Desika
- **Dvaita**: Madhvacharya, Jayatirtha
- **Vedic Commentary**: Sayanacharya, R.L. Kashyap, Sri Aurobindo (symbolic Veda)
- **Modern Scholarly**: S. Radhakrishnan, Bibek Debroy, Eknath Easwaran, Swami Gambhirananda
- **Civilizational**: Rajiv Malhotra, David Frawley, Subhash Kak

### EXCLUDED — Anti-Hindu Distortions
- Colonial Indologists with missionary/racial agendas (Max Mueller, Monier-Williams)
- Marxist historians (D.N. Jha, Romila Thapar, Irfan Habib)
- Western polemicists (Wendy Doniger, Sheldon Pollock, Audrey Truschke)
- Anyone whose explicit purpose is to denigrate or mock Hindu scriptures

## Research Workflow

### Step 1: Understand the User's Query

Parse the user's input which can be:
- **Direct question**: "What do the Vedas say about death?"
- **Life situation**: "I'm going through a career crisis and feel lost"
- **Topic**: "Leadership" or "Forgiveness" or "Marriage"
- **Philosophical inquiry**: "What is the nature of consciousness?"

Extract **core themes** and map to **Sanskrit concepts** where possible.

Example: "I'm going through a career crisis" → Themes: [svadharma, karma yoga, nishkama karma, vairagya, shraddha, purushaartha]

### Step 2: Deep Scripture Research

For each extracted theme, search across ALL scripture tiers using web search tools.

**Search Strategy:**
```
1. Search: "[theme] + [scripture name] + verse + translation"
2. Search: "[Sanskrit concept] + shloka + meaning"
3. Search: "[theme] + [trusted commentator] + interpretation"
4. Search: site:sacred-texts.com [theme] + [scripture]
5. Search: site:wisdomlib.org [theme]
6. Search: site:gitasupersite.iitk.ac.in [related Gita chapter]
```

**Authentic Online Sources (prioritize):**
- `sacred-texts.com` — Comprehensive Vedic and Hindu text archive
- `wisdomlib.org` — Encyclopedic Hindu scripture reference
- `gitasupersite.iitk.ac.in` — IIT Kanpur Gita with multiple commentaries
- `vedicheritage.gov.in` — Government of India Vedic heritage portal
- `sanskritdocuments.org` — Sanskrit text archive
- `srimadbhagavatam.org` — Bhagavatam reference
- `valmikiramayan.net` — Complete Valmiki Ramayana
- `swamivivekanandaquotes.org` — Authenticated Vivekananda references
- `archive.org` — Digitized classical commentaries

See `references/online-sources.md` for the full annotated source list.

**Minimum Search Requirement:**
- At least **10 separate web searches** per query
- Must search across at least **3 different scripture tiers**
- Must attempt to find **Vedic/Upanishadic (Tier 1)** verses for every query
- Must check at least **2 authentic online sources** for verse verification

### Step 3: Verify & Attribute

For every verse found:
1. **Verify** the verse exists in the cited scripture — cross-reference at least 2 sources
2. **Get the Sanskrit/original text** if available
3. **Get the exact citation**: Scripture name, Kanda/Mandala/Chapter, Sukta/Section, Verse number
4. **Identify the translator** of the English translation being used
5. **Identify the commentator** whose interpretation is being cited

**CRITICAL: Never fabricate verses.** If a verse cannot be verified from 2+ sources, mark it as `[Unverified — attributed to X source]`. It is far better to cite 5 verified verses than 20 unverified ones.

### Step 4: Interpret for Modern Life

For each cited verse, provide:
1. **Literal meaning** — What the verse says on its face
2. **Deeper meaning** — The metaphorical, spiritual, or philosophical message (attributed to commentator)
3. **Modern application** — How this wisdom applies to the user's specific situation today

Where applicable, use the **three-level framework**:
- **Adhyatmika** (spiritual/inner) — What it means for the soul and inner growth
- **Adhibhautika** (worldly/practical) — What it means for daily life and relationships
- **Adhidaivika** (cosmic/universal) — What it means in the grand design

### Step 5: Synthesize Guidance

Weave the verse findings into a coherent, compassionate response:
- Directly address the user's question or situation
- Prioritize Vedic (Tier 1) verses at the top
- Include relevant verses from all tiers for completeness
- Provide a clear "dharmic path forward"
- Connect ancient wisdom to modern actionable steps
- Write with warmth — like a wise elder speaking to a beloved family member

## Output Format

ALWAYS use this structure:

```markdown
# Shastra Wisdom: [User's Topic/Question — rephrased as title]

## Summary
[2-3 sentences: what Hindu scriptures say about this topic, warm and clear]

## Vedic Guidance (Shruti)

### Verse 1
> **Sanskrit**: [Original Sanskrit if available]
>
> **Translation**: "[English translation]"
>
> — *[Scripture], [Chapter/Mandala/Sukta].[Verse number]*
> — Translation by [Translator name]

**Literal Meaning**: [What the verse literally says]

**Deeper Meaning**: [Metaphorical/philosophical interpretation — attributed to commentator if applicable]

**Modern Application**: [How this applies to the user's situation today]

---

[Repeat for additional Vedic/Upanishadic verses]

## Gita & Smriti Wisdom

[Same verse format for Bhagavad Gita, Ramayana, Mahabharata]

## Puranic & Dharma Shastra Insights

[Same verse format for Puranas, Smritis, other texts]

## Integrated Guidance

[3-5 paragraph synthesis weaving all scriptural wisdom into practical, modern-life guidance. Warm, encouraging tone.]

## Sources & Further Reading
| # | Scripture | Verse | Translator/Commentator | Source URL |
|---|-----------|-------|----------------------|------------|
| 1 | [Name]    | [Ref] | [Person]             | [URL]      |

## Commentator Traditions Referenced
[List acharyas/scholars used and their school of thought]
```

## Quality Standards

1. **Minimum 5 verified verses** per response (aim for 8-12 for comprehensive topics)
2. **At least 2 Vedic/Upanishadic verses** in every response
3. **Every verse must have**: Sanskrit (if available), English translation, exact citation, translator attribution
4. **Every interpretation must be attributed** — never present interpretation as if it were the verse itself
5. **Cross-tradition**: When relevant, show how different acharyas interpret the same concept
6. **No fabrication** — if a scripture doesn't address a topic, say so honestly
7. **Respectful tone** — treat all scriptures and Hindu traditions with reverence
8. **Practical relevance** — always connect to actionable modern guidance

## Handling Edge Cases

- **Contradictions between scriptures**: Present both, note Shruti overrides Smriti, explain the deeper synthesis
- **Sensitive topics** (caste, gender in Smritis): Provide contextual/reformist interpretation from Vivekananda, Dayananda; emphasize Vedantic Atman equality
- **No direct reference**: Use closest thematic match, note it is thematic, draw from broader Dharmic framework
- **Specific scripture request**: Honor it, briefly note relevant verses from other scriptures
