# Tech Assist AI - Wireframes & UI Design

## Design System

### Macquarie Brand Colors
```
Primary: #00A9CE (Teal)
Secondary: #003C71 (Navy Blue)
Accent: #00D1A0 (Mint Green)
Background: #F5F7FA (Light Gray)
Text: #1A1A1A (Dark Gray)
Success: #28A745
Warning: #FFC107
Error: #DC3545
```

### Typography
- **Headings**: Macquarie Sans Bold
- **Body**: Macquarie Sans Regular
- **Code/Technical**: Courier New

---

## 1. Main Chat Interface

### Desktop View (1920x1080)

```
┌─────────────────────────────────────────────────────────────────────┐
│  ╔═══════════════════════════════════════════════════════════════╗  │
│  ║  [Macquarie Logo]  TECH ASSIST AI        [Queue: 🟢 No Wait]  ║  │
│  ╠═══════════════════════════════════════════════════════════════╣  │
│  ║                                                                ║  │
│  ║  ┌──────────────────────────────────────────────────────────┐ ║  │
│  ║  │  💬 Welcome! I'm TAAI, your 24/7 tech support assistant │ ║  │
│  ║  │     How can I help you today?                           │ ║  │
│  ║  │                                                          │ ║  │
│  ║  │  Quick actions:                                         │ ║  │
│  ║  │  [🔐 Password Reset]  [💻 VPN Issues]                  │ ║  │
│  ║  │  [📧 Email Problems]  [🖥️ Software Access]             │ ║  │
│  ║  └──────────────────────────────────────────────────────────┘ ║  │
│  ║                                                                ║  │
│  ║  ┌──────────────────────────────────────────────────────────┐ ║  │
│  ║  │  You:                                                    │ ║  │
│  ║  │  How do I reset my VPN password?              10:24 AM  │ ║  │
│  ║  └──────────────────────────────────────────────────────────┘ ║  │
│  ║                                                                ║  │
│  ║  ┌──────────────────────────────────────────────────────────┐ ║  │
│  ║  │  🤖 TAAI:                                                │ ║  │
│  ║  │                                                          │ ║  │
│  ║  │  To reset your VPN password, follow these steps:        │ ║  │
│  ║  │                                                          │ ║  │
│  ║  │  1. Go to https://vpn.macquarie.com                     │ ║  │
│  ║  │  2. Click "Forgot Password"                             │ ║  │
│  ║  │  3. Enter your employee ID                              │ ║  │
│  ║  │  4. Follow the email instructions                       │ ║  │
│  ║  │                                                          │ ║  │
│  ║  │  📚 Sources:                                            │ ║  │
│  ║  │  • VPN Setup Guide (Confluence)                         │ ║  │
│  ║  │  • Password Management Policy (SharePoint)              │ ║  │
│  ║  │                                                          │ ║  │
│  ║  │  Was this helpful? [👍] [👎]                            │ ║  │
│  ║  │                                        10:24 AM          │ ║  │
│  ║  └──────────────────────────────────────────────────────────┘ ║  │
│  ║                                                                ║  │
│  ╠════════════════════════════════════════════════════════════════╣  │
│  ║  Type your question...                        [📎] [Send →]  ║  │
│  ╚════════════════════════════════════════════════════════════════╝  │
│                                                                       │
│  [💬 New Chat]  [📊 My Tickets]  [❓ Help]  [⚙️ Settings]           │
└───────────────────────────────────────────────────────────────────────┘
```

### Components Breakdown

#### 1. Header Bar
```
┌─────────────────────────────────────────────────────────────┐
│ [🏢 Logo] Tech Assist AI           [🟢 Queue Status ▼]     │
│                                                             │
│ Dropdown shows:                                             │
│ ┌────────────────────────────┐                             │
│ │ 🟢 Sydney L5: No wait      │                             │
│ │ 🟡 Sydney L10: ~5 min      │                             │
│ │ 🔴 Melbourne: ~15 min      │                             │
│ │ [View All Locations →]     │                             │
│ └────────────────────────────┘                             │
└─────────────────────────────────────────────────────────────┘
```

#### 2. Welcome Message (First Visit)
```
┌─────────────────────────────────────────────────────────────┐
│  👋 Hi [Name]! Welcome to Tech Assist AI                   │
│                                                             │
│  I can help you with:                                       │
│  ✓ Password resets                                          │
│  ✓ VPN and network issues                                   │
│  ✓ Software installation                                    │
│  ✓ Email configuration                                      │
│  ✓ Hardware requests                                        │
│  ...and much more!                                          │
│                                                             │
│  💡 Tip: I'm available 24/7 and usually respond in seconds │
│                                                             │
│  [Get Started]                                              │
└─────────────────────────────────────────────────────────────┘
```

#### 3. Quick Action Buttons
```
┌──────────────┬──────────────┬──────────────┬──────────────┐
│ 🔐           │ 💻           │ 📧           │ 🖥️           │
│ Password     │ VPN Issues   │ Email        │ Software     │
│ Reset        │              │ Problems     │ Access       │
└──────────────┴──────────────┴──────────────┴──────────────┘
```

#### 4. Message Bubble (User)
```
┌────────────────────────────────────────────────────────┐
│  How do I reset my VPN password?          10:24 AM    │
└────────────────────────────────────────────────────────┘
```

#### 5. Message Bubble (TAAI)
```
┌──────────────────────────────────────────────────────────┐
│  🤖 TAAI                                                 │
│                                                          │
│  [Response text with formatting...]                      │
│                                                          │
│  📚 Sources:                                             │
│  • [Link 1] (Click to open)                             │
│  • [Link 2] (Click to open)                             │
│                                                          │
│  ──────────────────────────────────────────────         │
│  Still need help?                                        │
│  [📞 Call Tech Assist]  [🎫 Create Ticket]              │
│                                                          │
│  Was this helpful? [👍 Yes] [👎 No]      10:24 AM       │
└──────────────────────────────────────────────────────────┘
```

#### 6. Typing Indicator
```
┌────────────────────────────────────────┐
│  🤖 TAAI is typing                    │
│  ●●● (animated dots)                   │
└────────────────────────────────────────┘
```

#### 7. Input Box
```
┌──────────────────────────────────────────────────────────┐
│  Type your question...                    [📎] [Send →] │
└──────────────────────────────────────────────────────────┘
```

#### 8. File Attachment Preview
```
┌──────────────────────────────────────┐
│  📎 Attached:                        │
│  ┌─────────────────┐                │
│  │ 📄 screenshot.png│  [×]          │
│  │ 1.2 MB          │                │
│  └─────────────────┘                │
└──────────────────────────────────────┘
```

---

## 2. Queue Status Widget

### Compact View (Sidebar)
```
┌─────────────────────────────────┐
│  🏢 Tech Assist Queue Status   │
├─────────────────────────────────┤
│                                 │
│  📍 Sydney - Level 5           │
│  🟢 No wait                     │
│  👤 Available agents: 3         │
│                                 │
│  📍 Sydney - Level 10          │
│  🟡 ~5 min wait                │
│  👤 Available agents: 1         │
│                                 │
│  📍 Melbourne - Level 2        │
│  🔴 ~15 min wait               │
│  👤 Queue: 4 people            │
│                                 │
│  [View Details →]              │
│                                 │
│  ⏱ Updated 30 sec ago          │
└─────────────────────────────────┘
```

### Expanded View (Full Screen)
```
┌────────────────────────────────────────────────────────────────┐
│  Tech Assist Live Queue Status                   [Refresh ↻]  │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  📍 SYDNEY - LEVEL 5                        🟢 Available │ │
│  │  ────────────────────────────────────────────────────────│ │
│  │  Wait Time: < 1 minute                                   │ │
│  │  Queue Length: 0 people                                  │ │
│  │  Available Agents: 3                                     │ │
│  │  Location: Building A, Level 5, Zone 3                   │ │
│  │  Hours: Mon-Fri 8:00 AM - 6:00 PM                       │ │
│  │                                                          │ │
│  │  [🗺️ Get Directions]  [📞 Call Instead]                │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  📍 SYDNEY - LEVEL 10                      🟡 Moderate  │ │
│  │  ────────────────────────────────────────────────────────│ │
│  │  Wait Time: ~5 minutes                                   │ │
│  │  Queue Length: 2 people                                  │ │
│  │  Available Agents: 1                                     │ │
│  │  Location: Building B, Level 10, Help Desk              │ │
│  │  Hours: Mon-Fri 8:00 AM - 6:00 PM                       │ │
│  │                                                          │ │
│  │  [🗺️ Get Directions]  [💬 Chat with TAAI Instead]      │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  📍 MELBOURNE - LEVEL 2                      🔴 Busy     │ │
│  │  ────────────────────────────────────────────────────────│ │
│  │  Wait Time: ~15 minutes                                  │ │
│  │  Queue Length: 4 people                                  │ │
│  │  Available Agents: 1                                     │ │
│  │  Location: 1 Collins St, Level 2, IT Desk               │ │
│  │  Hours: Mon-Fri 9:00 AM - 5:00 PM                       │ │
│  │                                                          │ │
│  │  [🗺️ Get Directions]  [💬 Chat with TAAI Instead]      │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
│  💡 Tip: TAAI can resolve most issues instantly with no wait  │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## 3. Escalation Flow

### Option 1: Create Ticket
```
┌────────────────────────────────────────────────────────────┐
│  Create Support Ticket                           [×]       │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Issue Summary (auto-filled from chat):                   │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ VPN password reset not working                       │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                            │
│  Category:                                                 │
│  [▼ Network & Connectivity]                               │
│                                                            │
│  Priority:                                                 │
│  ( ) Low  (●) Medium  ( ) High  ( ) Critical              │
│                                                            │
│  Description:                                              │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ Tried resetting my VPN password but not receiving    │ │
│  │ the email with reset instructions. Checked spam.     │ │
│  │                                                      │ │
│  │                                                      │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                            │
│  📎 Attach Screenshot (optional)                          │
│  [Choose File]                                             │
│                                                            │
│  📊 Your Position in Queue: 3                             │
│  ⏱ Estimated Response: 45 minutes                        │
│                                                            │
│  ✉️ You'll receive updates via email                      │
│                                                            │
│  [Cancel]                      [Create Ticket →]          │
└────────────────────────────────────────────────────────────┘
```

### Option 2: Call Tech Assist
```
┌────────────────────────────────────────────────────────────┐
│  Call Tech Assist                                [×]       │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  📞 +61 2 XXXX XXXX                                        │
│  [Call Now]                                                │
│                                                            │
│  Current Queue Status:                                     │
│  🟡 Moderate wait time (~5 minutes)                        │
│                                                            │
│  💡 Tip: Request a callback to avoid waiting               │
│  ┌──────────────────────────────────────────────────────┐ │
│  │  Preferred callback time:                            │ │
│  │  [▼ Next available] (in ~10 minutes)                 │ │
│  │                                                      │ │
│  │  Your number: [+61 4XX XXX XXX]                     │ │
│  │                                                      │ │
│  │  [Request Callback]                                  │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                            │
│  Hours:                                                    │
│  Mon-Fri: 8:00 AM - 6:00 PM AEST                          │
│  Sat-Sun: Closed                                           │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

---

## 4. Feedback Mechanism

### Inline Feedback
```
┌──────────────────────────────────────────────────────────┐
│  Was this helpful?                                       │
│  [👍 Yes, thanks!]  [👎 Not quite]                      │
└──────────────────────────────────────────────────────────┘

// If user clicks 👍
┌──────────────────────────────────────────────────────────┐
│  ✅ Thanks for your feedback!                            │
│  Anything else I can help with?                          │
└──────────────────────────────────────────────────────────┘

// If user clicks 👎
┌──────────────────────────────────────────────────────────┐
│  😔 Sorry I couldn't help. What went wrong?              │
│                                                          │
│  [☐] Information was incorrect                           │
│  [☐] Answer was unclear                                  │
│  [☐] Didn't solve my problem                            │
│  [☐] Other: ___________________________                  │
│                                                          │
│  Would you like to:                                      │
│  [Talk to an agent]  [Try rephrasing your question]     │
└──────────────────────────────────────────────────────────┘
```

### End-of-Conversation Survey
```
┌────────────────────────────────────────────────────────────┐
│  How was your experience with TAAI?              [×]       │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Overall Satisfaction:                                     │
│  ⭐ ⭐ ⭐ ⭐ ⭐                                              │
│  (Click to rate)                                           │
│                                                            │
│  Did TAAI resolve your issue?                             │
│  (●) Yes, completely                                       │
│  ( ) Partially                                             │
│  ( ) No, I still need help                                │
│                                                            │
│  How would you improve TAAI?                              │
│  ┌──────────────────────────────────────────────────────┐ │
│  │                                                      │ │
│  │                                                      │ │
│  └──────────────────────────────────────────────────────┘ │
│                                                            │
│  [Skip]                              [Submit Feedback]    │
└────────────────────────────────────────────────────────────┘
```

---

## 5. Mobile View (375x667)

```
┌───────────────────────────┐
│ [≡]  TAAI      [Queue ⚫]│
├───────────────────────────┤
│                           │
│  ┌─────────────────────┐  │
│  │ 💬 Welcome!         │  │
│  │ How can I help?     │  │
│  │                     │  │
│  │ [🔐 Password]       │  │
│  │ [💻 VPN]            │  │
│  │ [📧 Email]          │  │
│  └─────────────────────┘  │
│                           │
│  ┌─────────────────────┐  │
│  │ You:                │  │
│  │ How do I reset my   │  │
│  │ VPN password?       │  │
│  │           10:24 AM  │  │
│  └─────────────────────┘  │
│                           │
│  ┌─────────────────────┐  │
│  │ 🤖 TAAI:            │  │
│  │                     │  │
│  │ To reset your VPN   │  │
│  │ password...         │  │
│  │                     │  │
│  │ 📚 Sources:         │  │
│  │ • VPN Guide         │  │
│  │                     │  │
│  │ Helpful?            │  │
│  │ [👍] [👎]           │  │
│  │           10:24 AM  │  │
│  └─────────────────────┘  │
│                           │
│                           │
├───────────────────────────┤
│ Type message...  [📎][→] │
└───────────────────────────┘
```

---

## 6. SharePoint Web Part Embed

### Minimal Widget (300x400)
```
┌────────────────────────────────┐
│  💬 Tech Assist AI            │
├────────────────────────────────┤
│                                │
│  Ask me anything about:        │
│  • Passwords & access          │
│  • VPN & network               │
│  • Software & hardware         │
│                                │
│  ┌──────────────────────────┐  │
│  │ Type your question...    │  │
│  └──────────────────────────┘  │
│  [Ask TAAI →]                  │
│                                │
│  ──────────────────────────    │
│  🟢 Sydney L5: No wait         │
│  🟡 Sydney L10: ~5 min         │
│                                │
│  [View Full Queue]             │
│                                │
└────────────────────────────────┘
```

---

## 7. Microsoft Teams Integration

### Teams App Interface
```
┌─────────────────────────────────────────────────────────┐
│  Tech Assist AI                                    [@]  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  🤖 TAAI Bot                                   Online   │
│  Your 24/7 tech support assistant                       │
│  ─────────────────────────────────────────────────      │
│                                                         │
│  👋 Hi! I can help with tech issues right here in      │
│  Teams. Try asking:                                     │
│                                                         │
│  • "How do I reset my password?"                       │
│  • "VPN not connecting"                                │
│  • "Request new laptop"                                │
│                                                         │
│  ┌───────────────────────────────────────────────────┐ │
│  │ [Type a message...]                               │ │
│  └───────────────────────────────────────────────────┘ │
│                                                         │
│  📍 Quick Links:                                        │
│  • IT Help Portal                                       │
│  • Submit a Ticket                                      │
│  • Check Queue Status                                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Adaptive Card Response
```
┌─────────────────────────────────────────────────────────┐
│  🤖 TAAI                                      10:24 AM  │
├─────────────────────────────────────────────────────────┤
│  To reset your VPN password:                           │
│                                                         │
│  1️⃣ Go to https://vpn.macquarie.com                   │
│  2️⃣ Click "Forgot Password"                           │
│  3️⃣ Enter your employee ID                            │
│  4️⃣ Follow email instructions                         │
│                                                         │
│  📚 Source: VPN Setup Guide                            │
│  [Open in Browser]                                      │
│                                                         │
│  ─────────────────────────────────────────────────      │
│  Still need help?                                       │
│  [📞 Call Tech Assist] [🎫 Create Ticket]              │
│                                                         │
│  Was this helpful? [👍 Yes] [👎 No]                    │
└─────────────────────────────────────────────────────────┘
```

---

## 8. Analytics Dashboard (Admin View)

### Overview
```
┌──────────────────────────────────────────────────────────────────┐
│  TAAI Analytics Dashboard                          [Last 30 days]│
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  📊 Key Metrics                                                  │
│  ┌─────────────┬─────────────┬─────────────┬──────────────┐    │
│  │ Total Chats │ Resolution  │ Avg Response│ User Sat     │    │
│  │             │ Rate        │ Time        │ (CSAT)       │    │
│  │    12,450   │    62%      │   2.3 sec   │   4.6/5.0    │    │
│  │  ↑ 23%      │  ↑ 5%       │  ↓ 0.4s     │  ↑ 0.3       │    │
│  └─────────────┴─────────────┴─────────────┴──────────────┘    │
│                                                                  │
│  📈 Usage Trend                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │     ▁▂▄▅▆█▆▅▄▃▂▁                     [Graph: Line chart]  │ │
│  │  1K ────────────────────────────────────────────────       │ │
│  │   0 ────────────────────────────────────────────────       │ │
│  │      Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct     │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  🔥 Top Categories                                               │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  1. VPN & Network Issues          ████████████░ 45%        │ │
│  │  2. Password Resets               ██████████░░ 38%        │ │
│  │  3. Software Installation         ████████░░░░ 28%        │ │
│  │  4. Email Configuration           █████░░░░░░░ 18%        │ │
│  │  5. Hardware Requests             ███░░░░░░░░░ 12%        │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ⚠️ Escalation Rate: 38% (target: <40%)                        │
│  💡 Top Reason: Issue too complex for self-service              │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Design Tokens (CSS Variables)

```css
:root {
  /* Colors */
  --color-primary: #00A9CE;
  --color-secondary: #003C71;
  --color-accent: #00D1A0;
  --color-background: #F5F7FA;
  --color-surface: #FFFFFF;
  --color-text-primary: #1A1A1A;
  --color-text-secondary: #6B7280;
  --color-success: #28A745;
  --color-warning: #FFC107;
  --color-error: #DC3545;
  --color-info: #17A2B8;

  /* Typography */
  --font-family-base: 'Macquarie Sans', -apple-system, sans-serif;
  --font-family-mono: 'Courier New', monospace;
  --font-size-xs: 0.75rem;
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 1.875rem;

  /* Spacing */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
  --spacing-2xl: 3rem;

  /* Border Radius */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 1rem;
  --radius-full: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.15);

  /* Animation */
  --transition-fast: 150ms ease-in-out;
  --transition-base: 250ms ease-in-out;
  --transition-slow: 350ms ease-in-out;
}
```

---

## Accessibility Considerations

1. **Keyboard Navigation**
   - Tab through all interactive elements
   - Enter to submit messages
   - Escape to close modals
   - Arrow keys for message history

2. **Screen Reader Support**
   - ARIA labels for all buttons
   - Live regions for new messages
   - Semantic HTML structure
   - Alt text for images

3. **Color Contrast**
   - WCAG AAA compliance
   - Minimum 7:1 contrast ratio for text
   - Color-blind friendly palette

4. **Text Scaling**
   - Supports up to 200% zoom
   - Responsive font sizes
   - No horizontal scrolling

5. **Focus Indicators**
   - Clear focus outlines
   - Skip to main content link
   - Focus trap in modals

---

## Responsive Breakpoints

```css
/* Mobile */
@media (max-width: 640px) { }

/* Tablet */
@media (min-width: 641px) and (max-width: 1024px) { }

/* Desktop */
@media (min-width: 1025px) { }

/* Large Desktop */
@media (min-width: 1440px) { }
```

---

## Interaction States

### Button States
```
Normal:    [Button] (solid color)
Hover:     [Button] (darker shade, cursor pointer)
Active:    [Button] (slightly inset, darker)
Disabled:  [Button] (grayed out, cursor not-allowed)
Loading:   [Button] (spinner, disabled)
```

### Message States
```
Sending:   [Message] (opacity 0.6, spinner)
Sent:      [Message] (full opacity, checkmark)
Error:     [Message] (red border, retry button)
```

---

This wireframe document provides a comprehensive visual guide for implementing the Tech Assist AI interface. Next steps would be to create high-fidelity mockups in Figma and proceed with development.
