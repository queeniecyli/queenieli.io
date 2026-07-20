# Tech Assist AI - SharePoint Front Page Integration

## SharePoint Implementation Strategy

### Placement Options

#### Option 1: Hero Web Part (Recommended)
Full-width banner at the top of Tech Assist SharePoint homepage

#### Option 2: Quick Links Tile
Prominent tile in the existing quick links section

#### Option 3: Embedded Chat Widget
Interactive chatbot directly on the SharePoint page

---

## Option 1: Hero Web Part Design

### Layout
```
┌────────────────────────────────────────────────────────────────────┐
│  Tech Assist SharePoint                              [Search] [👤]  │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ╔══════════════════════════════════════════════════════════════╗ │
│  ║                                                              ║ │
│  ║  [BACKGROUND: Gradient #00A9CE to #003C71]                  ║ │
│  ║                                                              ║ │
│  ║   🤖 NEW!                                                    ║ │
│  ║                                                              ║ │
│  ║   Get Instant Tech Help with TAAI                           ║ │
│  ║   Your AI-powered assistant, available 24/7                 ║ │
│  ║                                                              ║ │
│  ║   ⚡ Instant answers • 🌐 Available 24/7 • 🧠 Smart & helpful ║ │
│  ║                                                              ║ │
│  ║   [Try TAAI Now →]  [Learn More]                           ║ │
│  ║                                                              ║ │
│  ║                                 [TAAI Mascot Illustration]  ║ │
│  ╚══════════════════════════════════════════════════════════════╝ │
│                                                                    │
│  ┌────────────┬────────────┬────────────┬────────────┐          │
│  │ 🔐 Password│ 💻 VPN    │ 📧 Email   │ 🖥️ Software │          │
│  │ Reset      │ Support   │ Help       │ Access     │          │
│  └────────────┴────────────┴────────────┴────────────┘          │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

### HTML/CSS Implementation

```html
<div class="taai-hero-banner" style="
  background: linear-gradient(135deg, #00A9CE 0%, #003C71 100%);
  color: white;
  padding: 40px;
  border-radius: 12px;
  margin-bottom: 30px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
">
  <!-- Badge -->
  <div style="
    display: inline-block;
    background: #00D1A0;
    color: #1A1A1A;
    padding: 6px 16px;
    border-radius: 20px;
    font-weight: bold;
    font-size: 14px;
    margin-bottom: 20px;
  ">
    🤖 NEW!
  </div>

  <!-- Headline -->
  <h1 style="
    font-size: 42px;
    font-weight: bold;
    margin: 0 0 15px 0;
    line-height: 1.2;
  ">
    Get Instant Tech Help with TAAI
  </h1>

  <!-- Subheadline -->
  <p style="
    font-size: 20px;
    margin: 0 0 25px 0;
    opacity: 0.95;
  ">
    Your AI-powered assistant, available 24/7
  </p>

  <!-- Feature Pills -->
  <div style="
    display: flex;
    gap: 20px;
    margin-bottom: 30px;
    flex-wrap: wrap;
  ">
    <div class="feature-pill">⚡ Instant answers</div>
    <div class="feature-pill">🌐 Available 24/7</div>
    <div class="feature-pill">🧠 Smart & helpful</div>
  </div>

  <!-- CTA Buttons -->
  <div style="display: flex; gap: 15px; flex-wrap: wrap;">
    <a href="https://taai.macquarie.com" class="cta-primary" style="
      background: white;
      color: #003C71;
      padding: 14px 32px;
      border-radius: 25px;
      text-decoration: none;
      font-weight: bold;
      font-size: 16px;
      display: inline-block;
      transition: transform 0.2s;
    ">
      Try TAAI Now →
    </a>

    <a href="/sites/TechAssist/SitePages/TAAI-Info.aspx" class="cta-secondary" style="
      background: rgba(255, 255, 255, 0.15);
      color: white;
      padding: 14px 32px;
      border-radius: 25px;
      text-decoration: none;
      font-weight: bold;
      font-size: 16px;
      display: inline-block;
      border: 2px solid white;
      transition: background 0.2s;
    ">
      Learn More
    </a>
  </div>

  <!-- Illustration (positioned absolutely on right) -->
  <div style="
    position: absolute;
    right: 40px;
    bottom: 0;
    width: 300px;
    height: 300px;
    opacity: 0.2;
    pointer-events: none;
  ">
    <!-- SVG robot illustration or image -->
    <img src="/sites/TechAssist/SiteAssets/taai-mascot.svg" alt="TAAI" style="width: 100%; height: auto;">
  </div>
</div>

<style>
.feature-pill {
  background: rgba(255, 255, 255, 0.2);
  padding: 8px 18px;
  border-radius: 20px;
  font-size: 14px;
  white-space: nowrap;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.cta-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}

.cta-secondary:hover {
  background: rgba(255, 255, 255, 0.25);
}

@media (max-width: 768px) {
  .taai-hero-banner h1 {
    font-size: 32px !important;
  }
  .taai-hero-banner p {
    font-size: 18px !important;
  }
}
</style>
```

---

## Option 2: Quick Links Tile

### Design
```
┌─────────────────────────────────┐
│  🤖 Tech Assist AI              │
│                                 │
│  Get instant help 24/7          │
│                                 │
│  ⚡ Average response: 3 sec     │
│  📊 98% satisfaction            │
│                                 │
│  [Chat Now →]                   │
└─────────────────────────────────┘
```

### JSON Configuration (for SharePoint Quick Links)

```json
{
  "title": "Tech Assist AI",
  "description": "Get instant tech help with AI",
  "url": "https://taai.macquarie.com",
  "icon": "Robot",
  "imageUrl": "/sites/TechAssist/SiteAssets/taai-icon.png",
  "target": "_blank",
  "style": "tile",
  "tileSize": "large",
  "backgroundColor": "#00A9CE"
}
```

---

## Option 3: Embedded Chat Widget

### Interactive Widget Design

```html
<div id="taai-widget" style="
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
">
  <!-- Closed State -->
  <button id="taai-bubble" style="
    width: 70px;
    height: 70px;
    border-radius: 50%;
    background: linear-gradient(135deg, #00A9CE 0%, #003C71 100%);
    border: none;
    box-shadow: 0 4px 20px rgba(0, 169, 206, 0.4);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    transition: transform 0.2s;
  " onclick="toggleTAAI()">
    🤖
  </button>

  <!-- Notification Badge -->
  <div id="taai-badge" style="
    position: absolute;
    top: 0;
    right: 0;
    background: #00D1A0;
    color: #1A1A1A;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    font-weight: bold;
    border: 3px solid white;
  ">
    NEW
  </div>

  <!-- Expanded Chat Window -->
  <div id="taai-window" style="
    position: absolute;
    bottom: 90px;
    right: 0;
    width: 380px;
    height: 600px;
    background: white;
    border-radius: 16px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
    display: none;
    flex-direction: column;
    overflow: hidden;
  ">
    <!-- Header -->
    <div style="
      background: linear-gradient(135deg, #00A9CE 0%, #003C71 100%);
      color: white;
      padding: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    ">
      <div>
        <h3 style="margin: 0; font-size: 18px;">Tech Assist AI</h3>
        <p style="margin: 5px 0 0 0; font-size: 12px; opacity: 0.9;">🟢 Online • Usually replies instantly</p>
      </div>
      <button onclick="toggleTAAI()" style="
        background: none;
        border: none;
        color: white;
        font-size: 24px;
        cursor: pointer;
        padding: 0;
        width: 30px;
        height: 30px;
      ">×</button>
    </div>

    <!-- Chat Area -->
    <div id="taai-chat" style="
      flex: 1;
      padding: 20px;
      overflow-y: auto;
      background: #F5F7FA;
    ">
      <!-- Welcome message -->
      <div style="
        background: white;
        padding: 16px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
      ">
        <p style="margin: 0 0 12px 0; font-weight: bold;">👋 Hi! I'm TAAI</p>
        <p style="margin: 0 0 15px 0; font-size: 14px; color: #6B7280;">
          I can help you with tech issues instantly. Try asking:
        </p>
        <div style="display: flex; flex-direction: column; gap: 8px;">
          <button class="quick-action">"How do I reset my password?"</button>
          <button class="quick-action">"VPN not connecting"</button>
          <button class="quick-action">"Request new laptop"</button>
        </div>
      </div>
    </div>

    <!-- Input Area -->
    <div style="
      padding: 15px;
      border-top: 1px solid #E5E7EB;
      background: white;
    ">
      <div style="display: flex; gap: 10px;">
        <input type="text" id="taai-input" placeholder="Type your question..." style="
          flex: 1;
          padding: 12px;
          border: 2px solid #E5E7EB;
          border-radius: 25px;
          outline: none;
          font-size: 14px;
        ">
        <button onclick="sendMessage()" style="
          background: #00A9CE;
          color: white;
          border: none;
          padding: 12px 24px;
          border-radius: 25px;
          cursor: pointer;
          font-weight: bold;
        ">Send</button>
      </div>
      <p style="
        margin: 8px 0 0 0;
        font-size: 11px;
        color: #9CA3AF;
        text-align: center;
      ">
        Powered by Azure OpenAI
      </p>
    </div>
  </div>
</div>

<style>
.quick-action {
  background: #F3F4F6;
  border: 1px solid #E5E7EB;
  padding: 10px 14px;
  border-radius: 8px;
  text-align: left;
  cursor: pointer;
  font-size: 13px;
  color: #1A1A1A;
  transition: all 0.2s;
}

.quick-action:hover {
  background: #00A9CE;
  color: white;
  border-color: #00A9CE;
}

#taai-bubble:hover {
  transform: scale(1.1);
}

@media (max-width: 768px) {
  #taai-window {
    width: calc(100vw - 40px) !important;
    height: calc(100vh - 120px) !important;
    right: 20px !important;
  }
}
</style>

<script>
function toggleTAAI() {
  const window = document.getElementById('taai-window');
  const badge = document.getElementById('taai-badge');
  if (window.style.display === 'none' || window.style.display === '') {
    window.style.display = 'flex';
    badge.style.display = 'none';
  } else {
    window.style.display = 'none';
  }
}

function sendMessage() {
  const input = document.getElementById('taai-input');
  const message = input.value.trim();
  if (message) {
    // Open full TAAI interface with pre-filled message
    window.open(`https://taai.macquarie.com?q=${encodeURIComponent(message)}`, '_blank');
    input.value = '';
  }
}

// Quick action buttons
document.querySelectorAll('.quick-action').forEach(btn => {
  btn.addEventListener('click', function() {
    const question = this.textContent.replace(/['"]/g, '');
    window.open(`https://taai.macquarie.com?q=${encodeURIComponent(question)}`, '_blank');
  });
});

// Enter key support
document.getElementById('taai-input')?.addEventListener('keypress', function(e) {
  if (e.key === 'Enter') {
    sendMessage();
  }
});
</script>
```

---

## SharePoint Web Part Configuration

### For SharePoint Admins

#### Step 1: Upload Assets
```
/sites/TechAssist/SiteAssets/TAAI/
├── taai-mascot.svg
├── taai-icon.png
├── taai-banner.html
└── taai-widget.html
```

#### Step 2: Add Web Part
1. Edit SharePoint page
2. Add "Embed" web part
3. Paste HTML code
4. Save and publish

#### Step 3: Set Permissions
- Ensure all users have read access
- Enable anonymous viewing (if required)

---

## A/B Testing Strategy

### Test Variants

**Variant A**: Hero Banner (Full-width)
- Measure: Click-through rate, TAAI activations

**Variant B**: Quick Links Tile
- Measure: Tile clicks, conversion rate

**Variant C**: Chat Widget
- Measure: Widget opens, messages sent

### Success Metrics
- **Primary**: TAAI activations from SharePoint
- **Secondary**: Time on page, bounce rate
- **Tertiary**: User feedback scores

Run each variant for 2 weeks, analyze results, implement winner

---

## Content Variations

### For Different Audiences

#### IT Admins
```
🔧 TAAI for IT Admins

Get instant documentation, troubleshooting guides,
and system information at your fingertips.

[Admin Portal →]
```

#### End Users
```
🤖 Need Tech Help?

TAAI is here 24/7 to help with:
• Password resets
• VPN issues
• Email problems
• Software access

[Get Help Now →]
```

#### Executives
```
📊 Tech Support Reimagined

TAAI delivers instant, AI-powered support,
reducing wait times and improving productivity.

[Learn More →] [See Dashboard →]
```

---

## Dynamic Content Ideas

### Real-Time Stats Display

```html
<div class="taai-stats" style="
  display: flex;
  gap: 30px;
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid rgba(255,255,255,0.2);
">
  <div>
    <div style="font-size: 32px; font-weight: bold;">12,450</div>
    <div style="font-size: 14px; opacity: 0.9;">Questions Answered</div>
  </div>
  <div>
    <div style="font-size: 32px; font-weight: bold;">2.3s</div>
    <div style="font-size: 14px; opacity: 0.9;">Avg Response Time</div>
  </div>
  <div>
    <div style="font-size: 32px; font-weight: bold;">4.6★</div>
    <div style="font-size: 14px; opacity: 0.9;">User Rating</div>
  </div>
</div>

<script>
// Fetch live stats from API
fetch('/api/v1/analytics/stats')
  .then(res => res.json())
  .then(data => {
    // Update numbers dynamically
  });
</script>
```

### Testimonial Carousel

```html
<div class="testimonial" style="
  background: rgba(255,255,255,0.1);
  padding: 20px;
  border-radius: 8px;
  margin-top: 20px;
">
  <p style="font-style: italic; margin: 0 0 10px 0;">
    "TAAI helped me reset my VPN in 30 seconds. Would have taken 15 minutes on the phone!"
  </p>
  <p style="margin: 0; font-size: 14px; opacity: 0.9;">
    — Sarah M., Sydney
  </p>
</div>
```

---

## Mobile Responsiveness

Ensure all SharePoint components are mobile-friendly:

```css
@media (max-width: 768px) {
  .taai-hero-banner {
    padding: 20px !important;
  }

  .taai-hero-banner h1 {
    font-size: 28px !important;
  }

  .feature-pill {
    font-size: 12px !important;
    padding: 6px 12px !important;
  }

  .cta-primary, .cta-secondary {
    width: 100% !important;
    text-align: center !important;
  }
}
```

---

## Maintenance Schedule

- **Weekly**: Update stats, rotate testimonials
- **Monthly**: Refresh banner messaging
- **Quarterly**: A/B test new designs
- **Annually**: Complete redesign

---

## Success Criteria

- 50%+ of Tech Assist SharePoint visitors interact with TAAI banner
- 30%+ conversion rate (banner click → TAAI session)
- Maintain <2s page load time
- 4.5+ user feedback score

---

This SharePoint integration will make TAAI highly visible to all Tech Assist users, driving adoption and reducing support ticket volume.
