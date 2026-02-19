# Platform-Specific Search & Analysis Guide

## Table of Contents
1. [X/Twitter](#xtwitter)
2. [Facebook](#facebook)
3. [Instagram](#instagram)
4. [LinkedIn](#linkedin)
5. [Reddit](#reddit)
6. [YouTube](#youtube)
7. [TikTok](#tiktok)
8. [Threads](#threads)
9. [Mastodon](#mastodon)
10. [Bluesky](#bluesky)
11. [Quora](#quora)
12. [Alternative Platforms](#alternative-platforms)
13. [Long-Form Platforms](#long-form-platforms)
14. [Messaging-Adjacent Platforms](#messaging-adjacent-platforms)
15. [Archive & Historical Tools](#archive--historical-tools)

---

## X/Twitter

### Search Techniques
- `site:x.com "{name}"` or `site:twitter.com "{name}"` (both domains work)
- `site:x.com "{name}" {keyword}` for filtered results
- `"{name}" from:@handle` via Twitter advanced search
- For replies: `site:x.com "{name}" "replying to"`
- For retweets: track who they amplify via `site:x.com "@handle" RT`

### Accessible Content
- Public tweets, replies, retweets, quotes
- Bio, location, join date, follower/following counts
- Pinned tweet
- Media tab (images/videos posted)
- Likes (if public, some users hide these)

### Known Limitations
- Twitter/X may require login for some searches
- Rate-limited results via Google indexing
- Older tweets may not be indexed by Google; use `browser_subagent` to scroll feed
- Suspended accounts show no content but suspension notice is evidence

### Engagement Metrics
- Likes, Retweets, Quote Tweets, Replies, Bookmarks, Views
- "Community Notes" on flagged misinformation posts

---

## Facebook

### Search Techniques
- `site:facebook.com "{name}"` for profiles
- `site:facebook.com "{name}" {keyword}` for specific topics
- `site:facebook.com/groups "{topic}"` for group discussions
- `site:facebook.com/pages "{name}"` for public pages

### Accessible Content
- Public posts, comments, shares on public pages/groups
- Profile photos, cover photos, bio/intro section
- Public check-ins, life events (if public)
- Page reviews and ratings

### Known Limitations
- Most personal profiles are heavily privacy-locked
- Group content often requires membership
- Facebook's Google indexing is limited compared to other platforms
- Use `browser_subagent` for better access to public post content

---

## Instagram

### Search Techniques
- `site:instagram.com "{name}"` for profiles
- `site:instagram.com/p/ "{name}"` for specific posts
- `site:instagram.com "{hashtag}"` for hashtag exploration
- `"{name}" instagram` for third-party mentions

### Accessible Content
- Public posts (photos, reels, stories highlights)
- Bio, profile picture, follower/following counts
- Comment sections on public posts
- Tagged locations

### Known Limitations
- Stories disappear after 24 hours (only highlights persist)
- Instagram heavily restricts non-logged-in browsing
- Use `browser_subagent` cautiously; may hit login walls
- Comment threads can be deep; focus on visible top comments

---

## LinkedIn

### Search Techniques
- `site:linkedin.com/in/ "{name}"` for profiles
- `site:linkedin.com/pulse/ "{name}"` for articles
- `site:linkedin.com/posts/ "{name}"` for posts
- `"{name}" linkedin {company}` for contextual matching

### Accessible Content
- Professional headline, summary, experience, education
- Published articles and posts
- Recommendations (given/received)
- Skills, endorsements, certifications
- Activity feed (likes, comments, shares on others' posts)

### Known Limitations
- Full profile view may require login
- Activity outside posts/articles is harder to access
- LinkedIn restricts heavy scraping aggressively

### Special Notes
- LinkedIn persona often differs significantly from other platforms
- Professional tone may mask personal views; compare with Twitter/Facebook for contrast

---

## Reddit

### Search Techniques
- `site:reddit.com/user/{username}` for user post history
- `site:reddit.com "{name}"` for mentions
- `site:reddit.com/r/{subreddit} "{topic}"` for subreddit-specific
- `"{name}" reddit AMA` for Ask Me Anything sessions
- `site:reddit.com "{topic}" after:YYYY-MM-DD`

### Accessible Content
- Full post and comment history (publicly visible)
- Karma scores (post karma, comment karma)
- Subreddit activity patterns (which subs they frequent)
- Awards given/received
- Account age

### Known Limitations
- Reddit usernames are pseudonymous; need to link to real identity
- Deleted posts/comments may be recoverable via `removeddit.com` or `reveddit.com`
- Some subreddits are private/quarantined

### Special Value
- Reddit users are often more candid/unfiltered than other platforms
- Comment history reveals genuine opinions, biases, and interests
- Subreddit participation patterns reveal ideological alignment

---

## YouTube

### Search Techniques
- `site:youtube.com "{name}"` for channels and videos
- `site:youtube.com "{name}" {topic}` for specific content
- `"{name}" youtube comment` for comment activity
- `site:youtube.com/watch "{topic}"` for video discussions

### Accessible Content
- Channel content (videos, playlists, community posts)
- Comment sections (public)
- About section, links, subscriber count
- Video descriptions and tags
- Liked videos playlist (if public)

### Known Limitations
- Comment sections can be massive; focus on top/relevant comments
- YouTube comment search is limited; use Google's site-specific search
- Live stream chats are ephemeral

---

## TikTok

### Search Techniques
- `site:tiktok.com "@{handle}"` for profiles
- `site:tiktok.com "{topic}"` or `site:tiktok.com "#{hashtag}"`
- `"{name}" tiktok` for third-party mentions/embeds

### Accessible Content
- Public videos and captions
- Comment sections
- Bio, follower/following counts
- Duets and stitches (response videos)
- Liked videos (if public)

### Known Limitations
- TikTok is heavily video-based; text extraction limited
- Google indexing of TikTok is inconsistent
- Use `browser_subagent` for browsing specific profiles
- Audio-based content requires describing rather than quoting

---

## Threads

### Search Techniques
- `site:threads.net "{name}"` for profiles
- `site:threads.net "@{handle}"` for specific users
- `"{name}" threads.net` for broader discovery

### Accessible Content
- Public posts and replies
- Bio, follower count
- Reposts and quotes

### Known Limitations
- Relatively new platform; Google indexing still growing
- Instagram-linked accounts; can cross-reference

---

## Mastodon

### Search Techniques
- `"{name}" mastodon` for general discovery
- `site:{instance}.social "{name}"` for instance-specific (e.g., mastodon.social)
- `"{name}" fediverse` for broader ActivityPub network

### Accessible Content
- Public toots (posts), boosts (retweets), replies
- Bio, follower counts
- Instance affiliation (which server they chose reveals community alignment)

### Known Limitations
- Decentralized; content spread across many instances
- No single search index; must search instance by instance or use aggregators

---

## Bluesky

### Search Techniques
- `site:bsky.app "{name}"`
- `"{name}" bluesky` for external mentions

### Accessible Content
- Public posts, reposts, replies
- Bio, follower counts
- Custom feeds they follow/create

---

## Quora

### Search Techniques
- `site:quora.com "{name}"` for profile and answers
- `site:quora.com/profile/{name}` for direct profile
- `site:quora.com "{topic}"` for topic discussions

### Accessible Content
- Questions asked, answers written
- Topics followed
- Credentials listed
- Upvote counts

### Special Value
- Long-form answers reveal deep opinions and expertise claims
- Quora users often share personal anecdotes and beliefs

---

## Alternative Platforms

### Truth Social
- `site:truthsocial.com "{name}"` or `"{name}" truth social`
- Often used by politically right-leaning individuals
- Presence here itself is a data point

### Gab
- `site:gab.com "{name}"` or `"{name}" gab.com`
- Known for hosting far-right and extremist content
- Presence and activity level are significant indicators

### Parler / Gettr
- `site:parler.com "{name}"` / `site:gettr.com "{name}"`
- Alternative social media with specific political alignment

### Rumble
- `site:rumble.com "{name}"`
- YouTube alternative; content often demonetized/banned elsewhere

---

## Long-Form Platforms

### Substack
- `site:substack.com "{name}"` for newsletters/blogs
- Long-form content reveals detailed opinions and ideology
- Comment sections also valuable

### Medium
- `site:medium.com "@{name}"` or `site:medium.com "{name}"`
- Articles, claps (likes), responses
- Detailed thought pieces

---

## Messaging-Adjacent Platforms

### Telegram
- `site:t.me "{name}"` for public channels/groups
- `"{name}" telegram channel`
- Public channels are fully accessible; private groups are not

### Discord
- `"{name}" discord server` for public server mentions
- `site:discord.com "{name}"` limited but worth trying
- Discord is mostly private; focus on public server listings

---

## Archive & Historical Tools

### Wayback Machine (web.archive.org)
- Search: `https://web.archive.org/web/*/platform.com/username`
- Captures historical snapshots of profiles and posts
- Critical for finding deleted content

### Google Cache
- Search: `cache:URL` for recently cached versions
- Useful for very recently deleted content

### Removeddit / Reveddit
- `https://reveddit.com/user/{reddit_username}`
- Shows deleted/removed Reddit comments and posts

### Social Blade (socialblade.com)
- `site:socialblade.com "{name}"`
- Tracks follower growth, posting frequency over time
- Available for YouTube, Twitter, Instagram, TikTok, Twitch

### Thread Readers
- `site:threadreaderapp.com "{name}"` for unrolled Twitter threads
- Preserves threads that may have been deleted

### Politwoops
- Tracks deleted tweets by politicians
- `"{name}" politwoops`
