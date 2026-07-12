import base64
import re

# 1. Read and base64 encode the profile animation (profile.gif)
print("Encoding profile.gif...")
with open('profile.gif', 'rb') as f:
    img_data = base64.b64encode(f.read()).decode('utf-8')

# 2. SVG Template with CSS Animations and Orbit Cycles
svg_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 560" width="1000" height="560" fill="none">
  <defs>
    <!-- Fonts & Keyframe Animations -->
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap');
      
      .text-brand {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-weight: 800;
        font-size: 16px;
        letter-spacing: 1px;
        opacity: 0;
        animation: fadeIn 1s ease-out forwards;
      }
      
      .text-title {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-weight: 800;
        font-size: 64px;
        line-height: 1.1;
        fill: #FFFFFF;
        opacity: 0;
        animation: slideUp 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }
      
      .title-1 { animation-delay: 0.2s; }
      .title-2 { animation-delay: 0.4s; }
      
      .text-subtitle {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-weight: 700;
        font-size: 15px;
        letter-spacing: 2px;
        fill: #3b82f6;
        opacity: 0;
        animation: fadeIn 1s ease-out forwards;
        animation-delay: 0.6s;
      }
      
      .text-desc {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-weight: 400;
        font-size: 15px;
        line-height: 1.6;
        fill: #9ca3af;
        opacity: 0;
        animation: fadeIn 1s ease-out forwards;
        animation-delay: 0.8s;
      }
      
      .tech-pills {
        opacity: 0;
        animation: slideUp 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        animation-delay: 1s;
      }
      
      .text-tag {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-weight: 600;
        font-size: 9px;
        letter-spacing: 0.5px;
        fill: #9ca3af;
      }
      
      .cta-buttons {
        opacity: 0;
        animation: fadeIn 1.2s ease-out forwards;
        animation-delay: 1.2s;
      }
      
      .text-btn {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-weight: 700;
        font-size: 14px;
        letter-spacing: 0.5px;
        fill: #FFFFFF;
      }
      
      .metrics-grid {
        opacity: 0;
        animation: slideUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        animation-delay: 1.4s;
      }
      
      .text-stat-val {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-weight: 800;
        font-size: 32px;
        fill: #3b82f6;
      }
      
      .text-stat-lbl {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        font-weight: 600;
        font-size: 9px;
        letter-spacing: 0.5px;
        fill: #6b7280;
      }
      
      /* Glow & Animation Effects */
      .glow-avatar {
        filter: drop-shadow(0 0 15px rgba(59, 130, 246, 0.4));
      }
      
      .orbit-dashed {
        animation: spin 45s linear infinite;
        transform-origin: 730px 280px;
      }
      
      .orbit-inner {
        animation: spin-reverse 30s linear infinite;
        transform-origin: 730px 280px;
      }
      
      @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
      }
      
      @keyframes spin-reverse {
        from { transform: rotate(360deg); }
        to { transform: rotate(0deg); }
      }
      
      @keyframes fadeIn {
        to { opacity: 1; }
      }
      
      @keyframes slideUp {
        from {
          opacity: 0;
          transform: translateY(20px);
        }
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }
    </style>

    <!-- Gradients -->
    <linearGradient id="grad-sneh" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" />
      <stop offset="100%" stop-color="#00FF9C" />
    </linearGradient>
    
    <linearGradient id="grad-btn" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2563eb" />
      <stop offset="100%" stop-color="#00ff9c" />
    </linearGradient>
    
    <!-- Image Clip Path -->
    <clipPath id="clip-circle">
      <circle cx="730" cy="280" r="160" />
    </clipPath>
  </defs>

  <!-- Dark Canvas Background -->
  <rect width="1000" height="560" rx="16" fill="#030712" />
  
  <!-- Subtle Background Grid/Details -->
  <circle cx="900" cy="100" r="150" fill="#1e1b4b" opacity="0.2" filter="blur(80px)" />
  <circle cx="100" cy="450" r="200" fill="#0f172a" opacity="0.25" filter="blur(100px)" />

  <!-- BRAND TOP LEFT -->
  <text x="50" y="60" class="text-brand" fill="#FFFFFF">SNEH <tspan fill="#9ca3af">JAISWAL</tspan></text>
  <circle cx="178" cy="55" r="3" fill="#00FF9C" />

  <!-- LEFT COLUMN CONTENT -->
  
  <!-- "Hi, I'm Sneh Jaiswal" -->
  <g transform="translate(50, 110)">
    <text x="0" y="50" class="text-title title-1">Hi, I'm <tspan fill="url(#grad-sneh)">Sneh</tspan></text>
    <text x="0" y="115" class="text-title title-2">Jaiswal</text>
  </g>

  <!-- Subtitle -->
  <text x="50" y="270" class="text-subtitle">ALGO TRADER BUILDER</text>

  <!-- Description -->
  <g transform="translate(50, 295)">
    <text x="0" y="15" class="text-desc">I build <tspan fill="#ffffff" font-weight="600">Algorithmic Trading Platforms</tspan>, <tspan fill="#ffffff" font-weight="600">Fintech SaaS</tspan> &amp; high-performance</text>
    <text x="0" y="38" class="text-desc"><tspan fill="#ffffff" font-weight="600">Automation Systems</tspan> that traders and businesses rely on every day.</text>
  </g>

  <!-- Tech Badges Grid -->
  <g transform="translate(50, 365)" class="tech-pills">
    <!-- React -->
    <rect x="0" y="0" width="55" height="22" rx="11" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="27.5" y="14" class="text-tag" text-anchor="middle">REACT</text>
    
    <!-- Node.js -->
    <rect x="62" y="0" width="65" height="22" rx="11" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="94.5" y="14" class="text-tag" text-anchor="middle">NODE.JS</text>
    
    <!-- Python -->
    <rect x="134" y="0" width="60" height="22" rx="11" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="164" y="14" class="text-tag" text-anchor="middle">PYTHON</text>
    
    <!-- Next.js -->
    <rect x="201" y="0" width="60" height="22" rx="11" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="231" y="14" class="text-tag" text-anchor="middle">NEXT.JS</text>
    
    <!-- AWS -->
    <rect x="268" y="0" width="45" height="22" rx="11" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="290.5" y="14" class="text-tag" text-anchor="middle">AWS</text>
    
    <!-- MongoDB -->
    <rect x="320" y="0" width="75" height="22" rx="11" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="357.5" y="14" class="text-tag" text-anchor="middle">MONGODB</text>
    
    <!-- TypeScript -->
    <rect x="402" y="0" width="80" height="22" rx="11" fill="#0f172a" stroke="#1e293b" stroke-width="1" />
    <text x="442" y="14" class="text-tag" text-anchor="middle">TYPESCRIPT</text>
  </g>

  <!-- CTA Buttons -->
  <g transform="translate(50, 410)" class="cta-buttons">
    <!-- Contact Me Button -->
    <a href="mailto:snehjaiswal20@gmail.com" target="_blank">
      <rect x="0" y="0" width="160" height="42" rx="21" fill="url(#grad-btn)" cursor="pointer" />
      <text x="80" y="26" class="text-btn" text-anchor="middle" cursor="pointer">CONTACT ME</text>
    </a>
    
    <!-- View Projects Link -->
    <a href="https://snehj.lovable.app/projects" target="_blank">
      <text x="180" y="26" class="text-btn" fill="#9ca3af" cursor="pointer">VIEW PROJECTS →</text>
    </a>
  </g>

  <!-- Metrics Grid -->
  <g transform="translate(50, 475)" class="metrics-grid">
    <!-- Metric 1 -->
    <rect x="0" y="0" width="140" height="60" rx="8" fill="#090d16" stroke="#111827" stroke-width="1" />
    <text x="70" y="32" class="text-stat-val" text-anchor="middle">50+</text>
    <text x="70" y="48" class="text-stat-lbl" text-anchor="middle">PROJECTS SHIPPED</text>

    <!-- Metric 2 -->
    <rect x="150" y="0" width="140" height="60" rx="8" fill="#090d16" stroke="#111827" stroke-width="1" />
    <text x="220" y="32" class="text-stat-val" text-anchor="middle">5+</text>
    <text x="220" y="48" class="text-stat-lbl" text-anchor="middle">YEARS EXPERIENCE</text>

    <!-- Metric 3 -->
    <rect x="300" y="0" width="140" height="60" rx="8" fill="#090d16" stroke="#111827" stroke-width="1" />
    <text x="370" y="32" class="text-stat-val" text-anchor="middle">20+</text>
    <text x="370" y="48" class="text-stat-lbl" text-anchor="middle">CLIENTS SERVED</text>
  </g>

  <!-- RIGHT COLUMN: AVATAR & ORBITS WITH MULTIPLE LAYERS -->
  
  <!-- Outer Dotted Orbit (Clockwise) -->
  <circle cx="730" cy="280" r="185" stroke="#1e293b" stroke-width="1.5" stroke-dasharray="6 6" class="orbit-dashed" />
  
  <!-- Inner Orbit Ring (Counter-Clockwise) -->
  <circle cx="730" cy="280" r="172" stroke="#00ff9c" stroke-width="1" opacity="0.3" class="orbit-inner" stroke-dasharray="80 140" />
  <circle cx="730" cy="280" r="172" stroke="#2563eb" stroke-width="1" opacity="0.5" />
  
  <!-- Orbit Node (Little glowing dot on the ring) -->
  <g class="orbit-dashed">
    <circle cx="730" cy="95" r="5" fill="#00ff9c" class="glow-avatar" />
    <circle cx="730" cy="95" r="10" stroke="#00ff9c" stroke-width="1" opacity="0.5" />
  </g>
  
  <!-- Second Orbit Node -->
  <g class="orbit-inner">
    <circle cx="558" cy="280" r="4" fill="#3b82f6" class="glow-avatar" />
    <circle cx="558" cy="280" r="8" stroke="#3b82f6" stroke-width="1" opacity="0.5" />
  </g>

  <!-- Avatar Image with Circular Mask -->
  <g clip-path="url(#clip-circle)">
    <image href="data:image/gif;base64,{img_data}" x="550" y="100" width="360" height="360" />
  </g>

</svg>"""

# Replace profile placeholder
svg_content = svg_template.replace("{img_data}", img_data)

# Save header.svg file
print("Writing header.svg...")
with open('header.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

# 3. Base64 encode the entire SVG
print("Encoding header.svg to base64...")
svg_base64 = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
data_uri = f"data:image/svg+xml;base64,{svg_base64}"

# 4. Read README.md and replace the banner tag with the self-contained data URI
print("Updating README.md with inline data URI...")
with open('README.md', 'r', encoding='utf-8') as f:
    readme_content = f.read()

# Replace the img src
pattern = r'<img src="header\.svg" width="100%" alt="Sneh Jaiswal Animated Portfolio Banner" />'
replacement = f'<img src="{data_uri}" width="100%" alt="Sneh Jaiswal Animated Portfolio Banner" />'

new_readme_content = re.sub(pattern, replacement, readme_content)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_readme_content)

print("Successfully compiled and embedded animated SVG inside README.md!")
