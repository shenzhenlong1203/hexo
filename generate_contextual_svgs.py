#!/usr/bin/env python3
"""
根据图片描述生成语境匹配的SVG配图
"""

import os
import re
import glob
from string import Template

IMG_DIR = '/Users/zhenlong/work/hexo/shenzhenlong/source/img'
POSTS_DIR = '/Users/zhenlong/work/hexo/shenzhenlong/source/_posts'

def parse_filename(filename):
    name = filename.replace('.svg', '')
    parts = name.split('-', 1)
    if len(parts) == 2 and parts[0].isdigit() and len(parts[0]) == 4:
        return parts[0], parts[1]
    return '2013', name

COLOR_SCHEMES = {
    'warm': ('#FF6B6B', '#FFE66D'),
    'cool': ('#667eea', '#764ba2'),
    'nature': ('#11998e', '#38ef7d'),
    'sunset': ('#fa709a', '#fee140'),
    'night': ('#1a1a2e', '#16213e'),
    'morning': ('#ffecd2', '#fcb69f'),
    'medical': ('#4facfe', '#00f2fe'),
    'tech': ('#6a11cb', '#2575fc'),
    'gray': ('#a8a8a8', '#d8d8d8'),
}

def choose_scheme(desc):
    if any(w in desc for w in ['医护', '医院', '病房', '防护服']):
        return 'medical'
    if any(w in desc for w in ['深夜', '夜晚', '月光']):
        return 'night'
    if any(w in desc for w in ['黄昏', '夕阳', '晚霞', '日落']):
        return 'sunset'
    if any(w in desc for w in ['日出', '曙光', '阳光', '早晨']):
        return 'morning'
    if any(w in desc for w in ['月亮', '中秋']):
        return 'night'
    if any(w in desc for w in ['爱情', '遇见', '挚爱', '拥抱', '温馨', '温暖']):
        return 'warm'
    if any(w in desc for w in ['迷茫', '困惑', '思考', '沉思']):
        return 'gray'
    if any(w in desc for w in ['代码', '编程', '技术', '架构', '数据库']):
        return 'tech'
    if any(w in desc for w in ['山', '水', '风景', '自然', '湖', '海']):
        return 'nature'
    return 'cool'

def generate_svg(desc, year):
    scheme_name = choose_scheme(desc)
    c1, c2 = COLOR_SCHEMES[scheme_name]
    
    # 判断场景类型
    has_person = any(w in desc for w in ['人', '爸爸', '妈妈', '婴儿', '孩子', '家庭', '医护', '护士', '医生'])
    has_mountain = any(w in desc for w in ['山', '远山'])
    has_water = any(w in desc for w in ['水', '湖', '海', '河'])
    has_moon = '月' in desc
    has_sun = any(w in desc for w in ['日', '阳光', '曙光', '太阳'])
    has_window = '窗' in desc
    has_desk = any(w in desc for w in ['桌', '书桌'])
    has_love = any(w in desc for w in ['爱情', '挚爱', '拥抱'])
    has_code = any(w in desc for w in ['代码', '编程', '技术', '架构'])
    has_question = any(w in desc for w in ['迷茫', '困惑', '思考'])
    
    # 背景装饰元素
    bg_elements = ''
    
    # 人物剪影
    if has_person and not has_code:
        bg_elements += '''
    <g transform="translate(350, 100)" opacity="0.7">
      <circle cx="50" cy="30" r="25" fill="white"/>
      <path d="M 50 55 L 50 130" stroke="white" stroke-width="18" stroke-linecap="round"/>
      <path d="M 50 80 L 20 110" stroke="white" stroke-width="14" stroke-linecap="round"/>
      <path d="M 50 80 L 80 110" stroke="white" stroke-width="14" stroke-linecap="round"/>
      <path d="M 50 130 L 25 180" stroke="white" stroke-width="16" stroke-linecap="round"/>
      <path d="M 50 130 L 75 180" stroke="white" stroke-width="16" stroke-linecap="round"/>
    </g>'''
    
    # 爱心
    if has_love:
        bg_elements += '''
    <g transform="translate(400, 130) scale(1.2)" opacity="0.6">
      <path d="M 0 -15 A 15 15 0 0 0 -30 0 C -30 15 0 30 0 30 C 0 30 30 15 30 0 A 15 15 0 0 0 0 -15 Z" fill="white"/>
    </g>'''
    
    # 问号
    if has_question:
        bg_elements += '''
    <text x="400" y="180" text-anchor="middle" font-size="100" font-weight="bold" fill="white" opacity="0.4">?</text>'''
    
    # 太阳/月亮
    if has_moon:
        bg_elements += '''
    <circle cx="620" cy="70" r="35" fill="white" opacity="0.7"/>
    <circle cx="608" cy="62" r="30" fill="url(#bg)" opacity="0.4"/>'''
    elif has_sun:
        bg_elements += '''
    <circle cx="400" cy="120" r="50" fill="white" opacity="0.5"/>
    <circle cx="400" cy="120" r="70" fill="white" opacity="0.2"/>'''
    
    # 山
    if has_mountain:
        bg_elements += '''
    <polygon points="0,280 80,170 160,230 280,140 400,210 520,150 650,200 800,180 800,280" fill="white" opacity="0.15"/>
    <polygon points="0,300 120,210 240,260 360,190 480,240 600,220 800,250 800,300" fill="white" opacity="0.1"/>'''
    
    # 水面
    if has_water:
        bg_elements += '''
    <rect x="0" y="260" width="800" height="100" fill="white" opacity="0.08"/>
    <path d="M 0 275 Q 100 270 200 275 T 400 275 T 600 275 T 800 275" stroke="white" stroke-width="2" fill="none" opacity="0.2"/>
    <path d="M 0 295 Q 150 290 300 295 T 600 295 T 800 295" stroke="white" stroke-width="2" fill="none" opacity="0.15"/>'''
    
    # 窗户
    if has_window:
        bg_elements += '''
    <rect x="280" y="70" width="240" height="150" fill="white" opacity="0.15" rx="4"/>
    <rect x="290" y="80" width="105" height="130" fill="white" opacity="0.1"/>
    <rect x="405" y="80" width="105" height="130" fill="white" opacity="0.1"/>
    <line x1="400" y1="70" x2="400" y2="220" stroke="white" stroke-width="2" opacity="0.2"/>
    <line x1="280" y1="145" x2="520" y2="145" stroke="white" stroke-width="2" opacity="0.2"/>'''
    
    # 书桌
    if has_desk:
        bg_elements += '''
    <rect x="250" y="240" width="300" height="12" fill="white" opacity="0.25" rx="2"/>
    <rect x="270" y="252" width="12" height="60" fill="white" opacity="0.2"/>
    <rect x="518" y="252" width="12" height="60" fill="white" opacity="0.2"/>
    <rect x="290" y="222" width="50" height="18" fill="white" opacity="0.3" rx="2"/>
    <rect x="350" y="218" width="45" height="22" fill="white" opacity="0.25" rx="2"/>
    <rect x="410" y="215" width="80" height="25" fill="white" opacity="0.35" rx="2"/>'''
    
    # 代码符号
    if has_code:
        bg_elements += '''
    <g opacity="0.12" font-family="monospace" font-size="28" fill="white">
      <text x="60" y="70">&lt;/&gt;</text>
      <text x="620" y="90">{ }</text>
      <text x="120" y="340">[ ]</text>
      <text x="550" y="310">; ;</text>
    </g>'''
    
    # 树木
    if not has_person and not has_window and not has_code:
        bg_elements += '''
    <g transform="translate(120, 240)" opacity="0.2">
      <rect x="-4" y="0" width="8" height="55" fill="white"/>
      <circle cx="0" cy="-8" r="25" fill="white"/>
      <circle cx="-16" cy="8" r="20" fill="white"/>
      <circle cx="16" cy="8" r="20" fill="white"/>
    </g>
    <g transform="translate(680, 250)" opacity="0.15">
      <rect x="-4" y="0" width="8" height="50" fill="white"/>
      <circle cx="0" cy="-8" r="22" fill="white"/>
      <circle cx="-14" cy="6" r="18" fill="white"/>
      <circle cx="14" cy="6" r="18" fill="white"/>
    </g>'''
    
    # 装饰圆点
    bg_elements += '''
    <circle cx="100" cy="60" r="25" fill="white" opacity="0.08"/>
    <circle cx="720" cy="300" r="45" fill="white" opacity="0.06"/>'''
    
    svg_template = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{c1};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{c2};stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <rect width="800" height="400" fill="url(#bg)"/>
  {bg_elements}
  
  <rect x="0" y="310" width="800" height="90" fill="white" opacity="0.08"/>
  
  <g transform="translate(650, 45)">
    <rect width="100" height="36" rx="18" fill="white" opacity="0.85"/>
    <text x="50" y="24" text-anchor="middle" font-size="16" font-weight="bold" fill="{c1}">{year}</text>
  </g>
  
  <text x="400" y="360" text-anchor="middle" font-size="18" font-weight="bold" fill="white" opacity="0.9">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.5">Dragon_SZ Blog</text>
</svg>'''
    
    return svg_template.format(c1=c1, c2=c2, bg_elements=bg_elements, year=year, desc=desc)

def main():
    print("开始生成语境匹配的SVG图片...")
    
    needed_images = set()
    for md_file in glob.glob(os.path.join(POSTS_DIR, '*.md')):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = re.findall(r'!\[(.*?)\]\(/img/(.*?\.svg)\)', content)
            for alt_text, filename in matches:
                needed_images.add((filename, alt_text))
    
    print("共需要生成 {} 张SVG图片".format(len(needed_images)))
    
    generated = 0
    for filename, alt_text in needed_images:
        filepath = os.path.join(IMG_DIR, filename)
        year, desc_from_file = parse_filename(filename)
        description = alt_text if alt_text else desc_from_file
        
        svg_content = generate_svg(description, year)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        generated += 1
        if generated % 50 == 0:
            print("已生成 {}/{} 张图片...".format(generated, len(needed_images)))
    
    print("完成！共生成了 {} 张SVG图片".format(generated))

if __name__ == '__main__':
    main()
