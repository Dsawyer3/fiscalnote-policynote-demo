# PolicyNote API Demo — AI Chatbot & Minor Safety Legislation Tracker

## What This Does

A small Python tool that demonstrates the PolicyNote API by answering a real
government-affairs question: **who are the most active sponsors on a fast-moving
policy topic?**

This demo focuses on AI companion chatbot regulation and minor safety, a genuinely
active multi-state trend in 2026 (Virginia, California, Tennessee, Illinois, and a
federal CHAT Act / SAFE BOTs Act track are all represented in the results).

## How It Works

1. **Authenticate** (`auth.py`) — exchanges the API key for a short-lived Bearer
   token via `POST /v1/auth/token`.
2. **Search legislation** (`legislation.py`) — searches bills using
   `GET /v1/legislation/search` with a keyword query.
3. **Surface the insight** (`sponsor_insight.py`) — pulls the `primary_sponsors`
   field off every matching bill and tallies how often each person appears,
   surfacing the most active legislators on the topic.

## Endpoints Used

- `POST /v1/auth/token` — authentication
- `GET /v1/legislation/search` — bill search with keyword filtering

## Sample Output

Query: 'artificial intelligence chatbot minor'
Total bills matched: 116
Bills analyzed: 116

Top 10 most active sponsors on this topic:
  5 bill(s) - Steve Padilla
  3 bill(s) - Erin K. Maye Quade
  3 bill(s) - Warren Dunlap Hamilton
  3 bill(s) - June Robinson
  ...

## Positioning in a Customer Conversation

A government-affairs professional doesn't just want a list of bills, they want to know which bills to worry about and who's driving them. This demo shows how raw legislative data becomes an actionable answer in a few lines of code: instead of manually scanning 116 bills across a dozen states, a customer gets an instant read on which legislators to watch and build relationships with on this issue.

The same pattern extends naturally to the Stakeholders endpoints (/v2/people/search, /v2/people/fetch) to enrich these names with party, chamber, and biography, a natural next step and a good example of how a single API surfaces value across multiple endpoint families (Legislation + Stakeholders), not just one.

## Notes / What I'd Do With More Time

- The sponsor data occasionally includes committees (e.g., "Senate Appropriations Committee") rather than individual legislators. A production version would separate or filter these.
- This demo pulls results in a single page (limit=150), since the total for this query (116) fit under one page. A production integration would use the continuation_token to paginate through larger result sets.

## Setup

1. python3 -m venv venv && source venv/bin/activate
2. pip install requests python-dotenv
3. Create a .env file with POLICYNOTE_API_KEY=your_key_here
4. python3 sponsor_insight.py