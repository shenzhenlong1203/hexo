#!/usr/bin/env python3
"""
Generate beautiful placeholder images for blog posts.
Each image has a gradient background with the image description text overlaid.
"""

import os
import sys

# Color palettes by year - warm, aesthetic gradients
PALETTES = {
    '2013': [
        ('#667eea', '#764ba2'),  # purple
        ('#f093fb', '#f5576c'),  # pink
        ('#4facfe', '#00f2fe'),  # blue
        ('#43e97b', '#38f9d7'),  # green
        ('#fa709a', '#fee140'),  # sunset
        ('#a18cd1', '#fbc2eb'),  # lavender
        ('#fccb90', '#d57eeb'),  # peach
        ('#e0c3fc', '#8ec5fc'),  # pastel
    ],
    '2014': [
        ('#ff9a9e', '#fecfef'),  # rose
        ('#a1c4fd', '#c2e9fb'),  # sky
        ('#d4fc79', '#96e6a1'),  # mint
        ('#84fab0', '#8fd3f4'),  # ocean
        ('#cfd9df', '#e2ebf0'),  # silver
        ('#f6d365', '#fda085'),  # warm
        ('#fbc2eb', '#a6c1ee'),  # dream
        ('#fdcbf1', '#e6dee9'),  # soft
    ],
    '2015': [
        ('#667eea', '#764ba2'),
        ('#89f7fe', '#66a6ff'),
        ('#fddb92', '#d1fdff'),
        ('#9890e3', '#b1f4cf'),
        ('#ebc0fd', '#d9ded8'),
        ('#96fbc4', '#f9f586'),
        ('#2af598', '#009efd'),
        ('#cd9cf2', '#f6f3ff'),
    ],
    '2016': [
        ('#e8198b', '#c7eafd'),
        ('#7028e4', '#e5b2ca'),
        ('#dfe0ea', '#e9edf2'),
        ('#f5f7fa', '#c3cfe2'),
        ('#667eea', '#764ba2'),
        ('#89f7fe', '#66a6ff'),
        ('#fddb92', '#d1fdff'),
        ('#a8edea', '#fed6e3'),
    ],
    '2017': [
        ('#d299c2', '#fef9d7'),
        ('#667eea', '#764ba2'),
        ('#89f7fe', '#66a6ff'),
        ('#fddb92', '#d1fdff'),
        ('#a8edea', '#fed6e3'),
        ('#d9afd9', '#97d9e1'),
        ('#08aeea', '#b721ff'),
        ('#21d4fd', '#b721ff'),
    ],
    '2018': [
        ('#667eea', '#764ba2'),
        ('#89f7fe', '#66a6ff'),
        ('#fddb92', '#d1fdff'),
        ('#a8edea', '#fed6e3'),
        ('#d299c2', '#fef9d7'),
        ('#c471f5', '#fa71cd'),
        ('#48c6ef', '#6f86d6'),
        ('#feada6', '#f5efef'),
    ],
    '2019': [
        ('#667eea', '#764ba2'),
        ('#89f7fe', '#66a6ff'),
        ('#fddb92', '#d1fdff'),
        ('#a8edea', '#fed6e3'),
        ('#d299c2', '#fef9d7'),
        ('#c471f5', '#fa71cd'),
        ('#48c6ef', '#6f86d6'),
        ('#43e97b', '#38f9d7'),
    ],
    '2020': [
        ('#667eea', '#764ba2'),
        ('#89f7fe', '#66a6ff'),
        ('#fddb92', '#d1fdff'),
        ('#a8edea', '#fed6e3'),
        ('#d299c2', '#fef9d7'),
        ('#fa709a', '#fee140'),
        ('#30cfd0', '#330867'),
        ('#a8edea', '#fed6e3'),
    ],
}

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_svg_placeholder(description, year, index):
    """Create an SVG placeholder image with gradient background and text."""
    # Get palette for the year
    palette = PALETTES.get(year, PALETTES['2013'])
    color1, color2 = palette[index % len(palette)]
    
    # Clean description for display
    display_text = description.replace('.jpg', '').replace('-', ' ')
    # Remove year prefix if present
    if display_text.startswith(year + ' '):
        display_text = display_text[len(year) + 1:]
    elif display_text.startswith(year + '-'):
        display_text = display_text[len(year) + 1:]
    
    # Capitalize first letter of each word
    display_text = display_text.title()
    
    # Truncate if too long
    if len(display_text) > 40:
        display_text = display_text[:37] + '...'
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="400" viewBox="0 0 800 400">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{color1};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{color2};stop-opacity:1" />
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  <!-- Background -->
  <rect width="800" height="400" fill="url(#grad)" rx="0"/>
  
  <!-- Decorative circles -->
  <circle cx="650" cy="80" r="120" fill="white" opacity="0.1"/>
  <circle cx="100" cy="320" r="80" fill="white" opacity="0.08"/>
  <circle cx="700" cy="300" r="60" fill="white" opacity="0.06"/>
  
  <!-- Camera icon -->
  <g transform="translate(360, 120)" filter="url(#shadow)">
    <rect x="10" y="20" width="60" height="40" rx="5" fill="white" opacity="0.9"/>
    <circle cx="40" cy="40" r="12" fill="none" stroke="white" stroke-width="2" opacity="0.9"/>
    <circle cx="40" cy="40" r="6" fill="white" opacity="0.7"/>
    <rect x="25" y="15" width="15" height="8" rx="2" fill="white" opacity="0.9"/>
  </g>
  
  <!-- Year badge -->
  <rect x="340" y="185" width="120" height="30" rx="15" fill="white" opacity="0.25"/>
  <text x="400" y="205" font-family="Arial, sans-serif" font-size="14" fill="white" text-anchor="middle" font-weight="bold">{year}</text>
  
  <!-- Description text -->
  <text x="400" y="260" font-family="Arial, sans-serif" font-size="22" fill="white" text-anchor="middle" filter="url(#shadow)">{display_text}</text>
  
  <!-- Bottom text -->
  <text x="400" y="350" font-family="Arial, sans-serif" font-size="12" fill="white" text-anchor="middle" opacity="0.7">Dragon_SZ Blog</text>
</svg>'''
    
    return svg

def main():
    output_dir = '/Users/zhenlong/work/hexo/shenzhenlong/source/img'
    os.makedirs(output_dir, exist_ok=True)
    
    posts_dir = '/Users/zhenlong/work/hexo/shenzhenlong/source/_posts'
    
    # Collect all unique image references
    images = set()
    for filename in sorted(os.listdir(posts_dir)):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract image references
        import re
        matches = re.findall(r'!\[.*?\]\(/img/([^)]+)\)', content)
        for img_name in matches:
            images.add(img_name)
    
    print(f"Found {len(images)} unique images to generate")
    
    # Generate images
    count = 0
    for img_name in sorted(images):
        # Determine year from filename
        year = img_name.split('-')[0] if '-' in img_name else '2013'
        if not year.isdigit() or len(year) != 4:
            year = '2013'
        
        # Generate SVG
        svg_content = create_svg_placeholder(img_name, year, count)
        
        # Write SVG file
        output_path = os.path.join(output_dir, img_name.replace('.jpg', '.svg'))
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        # Also write as .jpg (we'll use SVG but keep .jpg reference working)
        # Actually, let's write both - SVG for quality, and rename
        jpg_path = os.path.join(output_dir, img_name)
        if not os.path.exists(jpg_path):
            # Copy SVG to jpg path - browsers can display SVG even with .jpg extension
            # But better: create a simple redirect or just use the SVG
            # Let's just create the SVG and update references
            pass
        
        count += 1
        if count % 50 == 0:
            print(f"Generated {count}/{len(images)} images...")
    
    print(f"\nDone! Generated {count} SVG placeholder images in {output_dir}")
    
    # Now update all markdown files to use .svg instead of .jpg
    update_count = 0
    for filename in sorted(os.listdir(posts_dir)):
        if not filename.endswith('.md'):
            continue
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace .jpg with .svg in image paths
        import re
        new_content = re.sub(r'\!\[(.*?)\]\(/img/(.*?)\.jpg\)', r'![\1](/img/\2.svg)', content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            update_count += 1
    
    print(f"Updated {update_count} markdown files to use .svg images")

if __name__ == '__main__':
    main()
