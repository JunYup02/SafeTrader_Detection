# Green Flag - Marketplace Chat Fraud Detection (Demo)

Rule-based demo implementing the PRD's P0 (chat risk scoring) and P1 (risk
warning UI), targeted at English-language chat on **eBay, OfferUp, and
Facebook Marketplace**.

## Why "no frontend" is wrong for an extension

A Chrome extension's UI is just split across a few surfaces instead of living
in one page:

- **content script** (`content.js` + `content.css` + `flag-widget.js`) — injected directly into the marketplace page. This draws the actual "Green Flag" widget and the inline badges on risky messages.
- **popup** (`popup.html`/`.js`/`.css`) — the small page that opens from the toolbar icon; shows the current risk summary and a manual transaction-risk calculator.
- **background** (`background.js`) — no UI, just stores default settings.
- **scorer.js** — the scoring logic shared by all of the above. This is the spot to swap in a real trained model/API call later.

## What changed for this round of requirements

1. **Seller-only scoring** — `content.js` only scores the counterparty's (seller's) chat messages and the listing/post text. The buyer's own ("me") messages are always skipped.
2. **Green Flag indicator** — replaced the old warning banner with a small draggable flag widget (`flag-widget.js`) whose color changes: green (safe) → orange (caution) → red (danger).
3. **Draggable position** — click-drag the flag anywhere on screen; the position is saved (`chrome.storage.local`, or `localStorage` in demo.html) and restored on reload.
4. **Risk shown as a percentage** — the flag always shows the current score as `N%` (0–100, higher = riskier), next to the flag icon.
5. **Real US marketplace targeting** — `manifest.json` matches `ebay.com`, `offerup.com`, and `facebook.com/marketplace` / `facebook.com/messages`, and `scorer.js` patterns were rewritten for English-language scam language (overpayment, cashier's-check, Zelle/Cash App prepay, shipping-label scams, verification-code phishing, off-platform redirects).

## How sender detection works (important limitation)

eBay/OfferUp/Facebook Marketplace all sit behind a login wall with hashed,
frequently-changing class names, so hardcoded per-site selectors would be
unverifiable and would silently break. Instead `content.js` uses two
site-agnostic heuristics:

- **Finding chat bubbles**: a broad selector matching common conventions — `class`/`data-testid`/`aria-label` containing "message", "msg", or "bubble", or `role="row"`.
- **Telling seller from buyer**: the near-universal chat UI convention that *your own* messages hug the right edge of the container, while the *other party's* hug the left. `isOutgoing()` in `content.js` implements this as a fallback. You can always force it explicitly with `data-sender="me"` / `data-sender="them"` (see `demo.html`), which the code checks first.

**This has not been verified against a live, logged-in eBay/OfferUp/Facebook
session** — I don't have accounts to test against in this environment. Before
relying on it in real use, load the unpacked extension, open real
conversations on each site, and check that: (a) the alignment heuristic
correctly separates seller vs. buyer messages, and (b) the chat-candidate
selector actually finds the message bubbles. If it misses on a given site,
tighten `CHAT_CANDIDATE_SELECTOR` in `content.js` for that site specifically.

## Run it

1. `chrome://extensions` → enable Developer Mode → "Load unpacked" → select this `extension/` folder.
2. Visit an eBay/OfferUp/Facebook Marketplace listing or chat — the flag should appear top-right.

## See it work without real accounts

Open `demo.html` directly in a browser (no extension install needed) — it
loads the exact same `scorer.js` / `flag-widget.js` / `content.js` as the real
extension. It simulates:
- A listing (title + description) with a "Load a risky listing" button.
- A chat window where you pick the sender (seller/buyer) per message, or play one of 3 preset scam scenarios.
- The draggable Green Flag, verifiable by dragging it around.

## Current rules (`scorer.js`)

- `urgency` — manufactured urgency ("I'll sell to someone else", "first come first served")
- `off_platform` — redirect off the app (phone/email/WhatsApp/Telegram, "text me instead")
- `verification_phishing` — asking for a verification/confirmation code
- `payment_pressure` — cashier's-check overpayment, Zelle/Cash App/wire transfer prepay requests
- `shipping_scam` — "my own shipper will pick it up", prepaid label, out-of-town excuses

Each matched category adds its weight (max 100). 30+ = caution (orange), 60+ = danger (red). Add/adjust patterns in the `RULES` array.

## Out of scope for this demo (see PRD §6)

- Real bank/deposit verification integration
- Image-based listing authenticity checks
- A model fine-tuned on real platform chat logs (rule-based scorer stands in for now)
- Full multi-turn conversational reasoning (sentence-level detection only)
- P2 items (auto-triggered reporting flow, first-party data pipeline)
