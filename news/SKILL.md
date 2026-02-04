---
name: news
description: Get the latest news updates on a specific topic. Use this skill when the user wants a summary of the latest news, deep research on current events, or a fact-checked report on a specific topic. It searches authentic global sources, cross-corroborates information, and provides a concise bulleted or tabular summary with citations.
---

# News Research and Summary

## Workflow

1.  **Analyze the Topic**: Identify the core subject and specific keywords for the news search.
2.  **Initial Search**: Use `search_web` to find the latest news articles.
    *   **Primary Source Strategy**: Start with **Google News** queries (e.g., "Google News [topic]") to get an aggregated view of top stories.
    *   Query examples: "latest news [topic]", "[topic] current events", "[topic] updates [current_month] [current_year]".
    *   Focus on major international news outlets (e.g., Reuters, AP, BBC, Al Jazeera, NYT, trusted local sources).
    *   **Time Awareness**: Pay close attention to the publication **date and time**. Prioritize the absolute latest updates (last 1-24 hours).
3.  **Iterative Research & Expansion**:
    *   **Keep Adding Sources**: Do not stop at the first result. If the initial search reveals sub-topics or new developments, run specific follow-up searches for those details.
    *   **Official & Authentic Sources**: **Thoroughly check** official government websites (e.g., `.gov`, `.mil`, country-specific official domains) and organization websites (NGOs, corporate press releases) when relevant. Do not rely solely on secondary reporting if primary data is available.
    *   **Language Translation**: If the news is from a non-English speaking region, **translate** local sources to understand the ground reality. Ensure you are not limited to English-only outlets.
    *   **Deep Dive**: If a specific event is mentioned, search for that specific event + "fact check" or "details".
    *   **Global Coverage**: Explicitly look for international sources to get diverse perspectives.
4.  **Synthesize Findings**:
    *   Group related updates.
    *   **Verify**: Cross-corroborate major claims across at least two independent, reliable sources.
    *   Discard unverified rumors or clearly labeled opinion pieces unless requested.
5.  **Format Output**:
    *   **NO** long narrative paragraphs.
    *   **MANDATORY Timestamps**: Every single news item **MUST** include the **Date and Actual Time**, converted to **US CST (Central Standard Time)**.
        *   Format: `[Date] @ [Time] CST` (e.g., "Feb 4, 2026 @ 2:30 PM CST").
        *   If the source says "2 hours ago", calculate the specific time based on the current time. Do not just write "2 hours ago".
    *   Use **Bullet Points** for key updates.
    *   Use **Tables** for chronological timelines.
    *   **Citations & URL Hygiene (CRITICAL)**:
        *   **STRICTLY FORBIDDEN**: Do **NOT** use `vertexaisearch.cloud.google.com` links or any long, opaque redirect URLs. These are consistently broken (404).
        *   **MANDATORY Canonical Links**: You **MUST** ensure every link is a clean, direct URL to the publisher's site (e.g., `https://www.reuters.com/...`, `https://www.bbc.com/...`).
        *   **Search for Links**: If the initial search provides a dirty link, you **MUST** run a specific search for the article title (e.g., `site:bbc.com "Title of article"`) to retrieve the correct functioning URL.
        *   **Verify Domain**: If the source is "Reuters", the URL **must** contain `reuters.com`.
        *   **Zero Tolerance for Dead Links**: If you cannot find a working, clean URL, do **not** provide a link at all. Instead, provide the **Full Title, Author, and Publication Date** as text citation. A broken link is worse than no link.

## Output Format Example

**Topic: [Topic Name] - Latest Updates**

*   **[Headline/Key Event]** - *[Date] @ [Time] CST*
    *   [Detail about the event] ([Source Name](url))
    *   [Corroborating detail] ([Source Name](url))

*   **[Another Key Event]** - *[Date] @ [Time] CST*
    *   [Detail] ([Source Name](url))

### Timeline of Events
| Date & Time (CST) | Event | Source |
| :--- | :--- | :--- |
| [Date - Time] | [Event Description] | [Link](url) |

**Fact Check Notes:**
*   Confirmed: [Claim] verified by [Source A] and [Source B].
*   Disputed: [Claim] reported by [Source C] but denied by [Source D].

## Best Practices

*   **Google News**: Use it as a starting point to identify top coverage.
*   **Timestamp Precision**: Include the publication time in **US CST** to allow for easy comparison.
*   **Iterative Sourcing**: "Based on what is needed" - if the user asks for a specific angle, keep searching until that specific angle is covered.
*   **Authenticity**: Verify sources. Use authoritative domains.
