# PRD: Deal Safety Checker (working title)

## Problem & Goal
**Problem.** On US C2C marketplaces (Facebook Marketplace, Craigslist, OfferUp), scams are common — upfront payment requests, pressure to pay via Zelle/Venmo/Cash App, verification code requests, fake shipping, and attempts to move the conversation off-platform. Buyers who aren't familiar with US secondhand-trading culture and local payment apps struggle to notice these red flags in the middle of a live chat.

**Goal.** Let a user paste in their deal details and chat log, automatically surface scam risk signals, classify the likely scam type, and return a Deal Safety Report with a clear **Proceed / Caution / Do Not Proceed** verdict plus a safety checklist.

## Target User (Persona)
Someone buying a secondhand item in the US through one of the platforms above.

> **Jimin (24)** — an international student, 3 months into living in the US. She's chatting with a seller on Facebook Marketplace about a used laptop, and the seller says "send me $50 via Zelle first to hold the item." She has secondhand-trading experience from Korea, but doesn't know that Zelle payments are irreversible, or that this is a textbook advance-payment scam pattern. She needs a tool that tells her whether it's safe to go ahead.

## Value — Why Ours
- **Built for beginners.** Existing scam-prevention info is scattered across English-language blogs and forums, hard to reference in real time mid-chat. This tool is actionable — paste in "this exact chat" and get an immediate verdict.
- **Sentence-level evidence.** Instead of a vague "be careful," it highlights which specific sentences are risky and why, and classifies the scam type, so the user learns as they go.
- **Clear decision support.** A 3-tier verdict removes decision fatigue and translates straight into action.

## Must-Have Features (MVP)
1. **Deal details input form** — platform (choice of 3), item type, asking price, expected market price, payment method, transaction method (in-person/shipping), chat content (pasted text)
2. **Risky sentence highlighting** — flags sentences showing advance payment requests, verification code requests, off-platform payment pressure, avoidance of meeting in person, and voice-phishing-style handoffs, each with a reason
3. **Scam type classification** — matches the chat against predefined scam types (advance payment scam, verification code scam, off-platform payment scam, fake shipping scam, etc.) and shows the closest match
4. **Deal Safety Report** — overall verdict (Proceed / Caution / Do Not Proceed) + supporting reasons + safety checklist
5. **Single-page web app** — input → analysis → report in one continuous screen flow

## User Stories
- **US-1.** As a buyer, I want to paste in my deal details and chat log and get an automatic analysis of this deal's risk factors.
- **US-2.** As a buyer, I want risky sentences in the chat highlighted, along with why they're risky.
- **US-3.** As a buyer, I want to see which scam type this deal most closely resembles.
- **US-4.** As a buyer, I want a clear Proceed / Caution / Do Not Proceed verdict with supporting reasons.
- **US-5.** As a buyer, I want a pre-deal safety checklist (meet in public, pay on the spot, never share codes, etc.).

## Out of Scope
Chat screenshot upload / OCR · seller profile / account trust lookup · platform API integration / browser extension · user accounts, login, or transaction history · seller-facing features · real-time chat monitoring or push notifications · automated reporting or legal-action guidance
