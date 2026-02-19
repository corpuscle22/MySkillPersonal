---
name: sm-checker
description: Deep social media intelligence and analysis across all major platforms. Use when asked to (1) investigate a person's social media presence and public behavior, (2) analyze public posts, comments, likes, and interactions of specific individuals, (3) track how a topic or hashtag is trending across social media, (4) identify biases, racism, hate speech, or controversial stances in someone's public posts, (5) analyze debate dynamics and majority/minority voices on a topic, (6) create a social media behavior profile of a person, or (7) monitor public sentiment and discourse patterns. Triggers include "check social media", "sm check", "social media analysis", "what are they posting", "who do they support", "are they racist", "track this topic on social media", "trending analysis", "public posts review", "comment analysis", "social media habits", "digital footprint", or any request involving social media intelligence gathering on people or topics.
---

# SM-Checker: Social Media Intelligence & Analysis

## Overview

SM-Checker conducts deep, systematic analysis of public social media activity across all major platforms. It operates in two primary modes:

1. **Person Mode** - Profile a specific individual's public social media behavior, biases, alliances, controversies, and digital persona.
2. **Topic Mode** - Track how a topic/hashtag trends, who the major voices are, how debates are progressing, and what the majority/minority sentiments are.

Both modes produce a comprehensive report with evidence (direct post URLs, dates, engagement metrics) and detailed textual analysis.

## Workflow

### Phase 0: Mode Determination & Setup

Determine the mode based on the user's request:
- **Person Mode** - User names a specific individual or handle.
- **Topic Mode** - User names a topic, hashtag, event, or debate.
- **Combined** - User wants both (e.g., "What is [Person] saying about [Topic]?").

If key details are missing, ask clarifying questions:
- Person mode: Full name? Known handles/usernames? Location? Profession?
- Topic mode: Specific hashtag? Time window? Geographic focus? Specific angle?

### Phase 1: Platform Discovery Sweep

Search systematically across ALL platforms using `search_web` and `read_url_content`:

#### Person Mode - Platform-by-Platform Search

For each platform, use site-specific search operators:

| Platform | Search Strategy |
|---|---|
| **X/Twitter** | `site:x.com "{Name}"` OR `site:twitter.com "{Name}"` + known handles |
| **Facebook** | `site:facebook.com "{Name}"` + public posts/pages |
| **Instagram** | `site:instagram.com "{Name}"` + hashtag activity |
| **LinkedIn** | `site:linkedin.com "{Name}"` + professional posts/articles |
| **Reddit** | `site:reddit.com "{Name}"` OR `site:reddit.com "{username}"` |
| **YouTube** | `site:youtube.com "{Name}"` + comments, channels, appearances |
| **TikTok** | `site:tiktok.com "{Name}"` OR `site:tiktok.com "@{handle}"` |
| **Threads** | `site:threads.net "{Name}"` |
| **Mastodon** | `"{Name}" mastodon` + known instances |
| **Bluesky** | `site:bsky.app "{Name}"` |
| **Quora** | `site:quora.com "{Name}"` |
| **Truth Social** | `site:truthsocial.com "{Name}"` |
| **Gab** | `site:gab.com "{Name}"` |
| **Parler** | `site:parler.com "{Name}"` |
| **Gettr** | `site:gettr.com "{Name}"` |
| **Rumble** | `site:rumble.com "{Name}"` |
| **Telegram** | `"{Name}" telegram channel` OR `site:t.me "{Name}"` |
| **Discord** | `"{Name}" discord` (public server mentions) |
| **Pinterest** | `site:pinterest.com "{Name}"` |
| **Snapchat** | `site:snapchat.com "{Name}"` (public stories/profiles) |
| **Substack** | `site:substack.com "{Name}"` |
| **Medium** | `site:medium.com "{Name}"` |

**Username Pivot**: When a handle is discovered on one platform, immediately search that exact handle across all other platforms.

#### Topic Mode - Cross-Platform Trend Search

| Platform | Search Strategy |
|---|---|
| **X/Twitter** | `site:x.com "{topic}"` + `site:x.com "#{hashtag}"` |
| **Reddit** | `site:reddit.com "{topic}"` + subreddit-specific searches |
| **YouTube** | `site:youtube.com "{topic}"` (videos, comments, community posts) |
| **TikTok** | `site:tiktok.com "{topic}"` OR `site:tiktok.com "#{hashtag}"` |
| **Facebook** | `site:facebook.com "{topic}"` (groups, public pages) |
| **Instagram** | `site:instagram.com "#{hashtag}"` |
| **News/Blogs** | `"{topic}" social media reaction` + `"{topic}" viral` |
| **Threads** | `site:threads.net "{topic}"` |
| **Substack/Medium** | `site:substack.com "{topic}"` + `site:medium.com "{topic}"` |

Use additional time-bounded queries: `"{topic}" after:YYYY-MM-DD` or `"{topic}" [month] [year]`.

### Phase 2: Deep Content Analysis

For each discovered profile/thread, use `read_url_content` and `browser_subagent` to extract:

#### Person Mode - Behavioral Analysis Categories

1. **Political Alignment & Support**
   - Who they publicly endorse, retweet, share, or praise
   - Political figures, parties, movements they amplify
   - Causes, petitions, or campaigns they support

2. **Bias & Prejudice Indicators**
   - Language patterns suggesting bias (racial, religious, gender, ethnic)
   - Dog whistles, coded language, stereotyping
   - Who they target with negative commentary
   - Groups or communities they mock, belittle, or dehumanize

3. **Racism & Hate Speech**
   - Explicitly racist posts, comments, or shares
   - Sharing or amplifying known hate figures/groups
   - Use of slurs, derogatory terms, dehumanizing language
   - Pattern of targeting specific racial/ethnic/religious groups

4. **Social Media Habits & Persona**
   - Posting frequency and peak activity times
   - Content types (original posts vs. shares/retweets vs. comments)
   - Tone and communication style (aggressive, sarcastic, professional, trolling)
   - Echo chamber indicators (who they follow/interact with)
   - Level of engagement (likes, comments, shares they receive)

5. **Controversies & Conflicts**
   - Public arguments, feuds, or callouts
   - Deleted posts (via archive searches: `site:web.archive.org`, cached versions)
   - Posts that went viral for wrong reasons
   - Apologies, walkbacks, or doubling down

6. **Professional vs. Personal Disconnect**
   - Differences between LinkedIn persona and Twitter/Facebook persona
   - Contradictions between stated values and actual behavior

#### Topic Mode - Discourse Analysis Categories

1. **Trend Trajectory**
   - When the topic first gained traction
   - Peak engagement windows
   - Current momentum (rising, plateauing, declining)

2. **Majority vs. Minority Voices**
   - What is the dominant sentiment? (support, oppose, neutral)
   - Who are the loudest voices on each side?
   - Regional/demographic patterns in sentiment

3. **Debate Dynamics**
   - Key arguments from each side
   - Misinformation or propaganda patterns
   - Bot/fake account activity indicators (if detectable)
   - Astroturfing signals

4. **Influencer Map**
   - Top accounts driving the conversation
   - Engagement metrics of key posts
   - Cross-platform amplification patterns

### Phase 3: Archive & Cached Content Search

For comprehensive coverage, also search:
- **Google Cache**: `cache:{url}` for recently changed/deleted content
- **Wayback Machine**: `site:web.archive.org {profile_url}` for historical posts
- **Social media aggregators**: `"{Name}" site:socialblade.com`, `"{Name}" site:socialsearcher.com`
- **Deleted posts**: `"{Name}" deleted tweet`, `"{Name}" deleted post`

### Phase 4: Evidence Collection

For every significant finding:
1. **Capture the direct URL** to the post/comment (canonical, not redirect)
2. **Record the exact date and time** (convert to US CST)
3. **Quote the exact text** of the post/comment
4. **Note engagement metrics** (likes, retweets, shares, comments) if visible
5. **Capture context** (what they were replying to, thread context)

**URL Hygiene (CRITICAL)**:
- Never use `vertexaisearch.cloud.google.com` or opaque redirect URLs.
- Every link must be a clean, direct URL to the platform (e.g., `https://x.com/user/status/123456`).
- If a clean URL cannot be found, provide full text citation with platform, date, and username instead.


### Phase 6: Report Generation

Save the final report as a markdown file in the `outputs/` folder within the skill directory.

**Filename**: `sm_check_{subject_or_topic}_{YYYY-MM-DD}.md`

## Report Template

### Person Mode Report Structure

```
# Social Media Intelligence Report: {Full Name}

**Generated**: {Date} | **Time Window Analyzed**: {Range} | **Platforms Covered**: {Count}

## Executive Summary
[2-3 paragraph overview of key findings, overall digital persona characterization, and any red flags]

## Platform Presence Map
| Platform | Handle/Profile | Status | Activity Level | Notes |
|---|---|---|---|---|
| X/Twitter | @handle | Active | High | Primary platform |
| Facebook | /profile | Active | Medium | Personal use |
| ... | ... | ... | ... | ... |

## Political Alignment & Affiliations
### Public Support
- [Person/Party/Movement supported] - [Evidence with post URL and date]
### Public Opposition
- [Person/Party/Movement opposed] - [Evidence with post URL and date]

## Bias & Prejudice Analysis
### Identified Patterns
- [Pattern description with specific examples, quoted text, URLs, dates]
### Severity Assessment
- [Rating: None / Occasional / Frequent / Pervasive]
- [Types: Racial / Religious / Gender / Ethnic / Political / Other]

## Racism & Hate Speech Findings
- [Specific instances with exact quotes, URLs, dates, and context]
- [Pattern analysis if applicable]

## Social Media Habits Profile
### Posting Behavior
- Frequency: [X posts/day or /week]
- Peak Hours: [Time patterns]
- Content Mix: [% original / % shares / % comments]
### Communication Style
- [Characterization with examples]
### Echo Chamber Analysis
- Key accounts they interact with
- Content bubble indicators

## Controversies & Red Flags
### [Controversy Title] - {Date}
- **What happened**: [Description]
- **Evidence**: [URL, quoted text]
- **Outcome**: [Resolution or ongoing]

## Key Posts Archive
| # | Date (CST) | Platform | Post Content (Excerpt) | URL | Engagement | Significance |
|---|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... | ... |


## Assessment Summary
[Final characterization of the person's public digital behavior]
```

### Topic Mode Report Structure

```
# Social Media Trend Analysis: {Topic/Hashtag}

**Generated**: {Date} | **Time Window**: {Range} | **Platforms Analyzed**: {Count}

## Executive Summary
[Overview of how the topic is trending, dominant narratives, and key dynamics]

## Trend Trajectory
### Timeline of Key Moments
| Date (CST) | Event/Post | Platform | Impact |
|---|---|---|---|
| ... | ... | ... | ... |

### Momentum Assessment
- Current Status: [Rising / Peaking / Declining / Stable]
- Velocity: [engagement rate changes]

## Platform-by-Platform Breakdown
### X/Twitter
- Volume: [estimated posts in time window]
- Dominant sentiment: [For/Against/Mixed]
- Top posts: [URLs with engagement stats]
### Reddit
- Active subreddits: [list]
- Dominant sentiment: [For/Against/Mixed]
- Top threads: [URLs]
### [Other platforms...]

## Sentiment Analysis
### Majority Voice
- Position: [Summary]
- Key arguments: [Bullet points]
- Notable advocates: [Handles/names with URLs]
### Minority Voice
- Position: [Summary]
- Key arguments: [Bullet points]
- Notable advocates: [Handles/names with URLs]
### Sentiment Distribution
- Support: [~%] | Oppose: [~%] | Neutral: [~%]

## Key Influencers & Voices
| # | Name/Handle | Platform | Stance | Reach | Key Post |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... |

## Debate Dynamics
### Key Flashpoints
- [Specific debates with URLs and summaries]
### Misinformation Patterns
- [Identified false claims circulating, with counter-evidence]
### Propaganda / Astroturfing Signals
- [Any coordinated inauthentic behavior patterns]


## Conclusions & Outlook
[Where the discourse is heading, predictions based on trajectory]
```

## Tools & Methods

### Primary Tools
- `search_web` - Cross-platform discovery and search
- `read_url_content` - Extract post content, comments, profiles
- `browser_subagent` - Navigate dynamic SM pages, scroll feeds, capture content


### Search Optimization Techniques
- **Exact match**: Always use `"{Name}"` in quotes for precision
- **Date filtering**: Append `after:YYYY-MM-DD` or `before:YYYY-MM-DD`
- **Site operators**: `site:platform.com` for platform-specific results
- **Boolean combinations**: `"{Name}" AND ("racist" OR "hate" OR "slur")`
- **Negative filtering**: `"{Name}" -site:irrelevant.com`

### Platform-Specific Reference
See `references/platform-guide.md` for detailed per-platform search techniques, content accessibility notes, and known limitations.

## Important Notes

- **Public content only**: Only analyze publicly visible posts. Do not attempt to access private/locked accounts.
- **Evidence-based**: Every claim must link to a specific post URL with date.
- **Context matters**: Always include thread context - a reply looks different from an original post.
- **Archived content**: Deleted posts found via archives should be clearly marked as "[Deleted/Archived]".
- **Timestamp precision**: All timestamps converted to US CST. Format: `Mon DD, YYYY @ HH:MM AM/PM CST`.
- **No speculation**: Distinguish between confirmed patterns and isolated incidents. Use language like "pattern of..." vs. "single instance of...".
