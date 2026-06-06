#!/usr/bin/env python3
"""
生成精美的差异化SVG配图
每张图片根据其具体描述生成独特的视觉内容
"""

import os
import re
import glob
import hashlib

IMG_DIR = '/Users/zhenlong/work/hexo/shenzhenlong/source/img'
POSTS_DIR = '/Users/zhenlong/work/hexo/shenzhenlong/source/_posts'

def parse_filename(filename):
    name = filename.replace('.svg', '')
    parts = name.split('-', 1)
    if len(parts) == 2 and parts[0].isdigit() and len(parts[0]) == 4:
        return parts[0], parts[1]
    return '2013', name

def get_hash_seed(desc):
    """根据描述生成稳定的哈希种子，用于差异化元素位置"""
    return int(hashlib.md5(desc.encode()).hexdigest()[:8], 16)

# ==================== 配色方案 ====================

PALETTES = {
    'warm': ('#FF6B6B', '#FFE66D', '#FF8E53'),
    'cool': ('#667eea', '#764ba2', '#4facfe'),
    'nature': ('#11998e', '#38ef7d', '#0ba360'),
    'sunset': ('#fa709a', '#fee140', '#ff9a56'),
    'night': ('#0c1445', '#1a237e', '#283593'),
    'morning': ('#ffecd2', '#fcb69f', '#ff9a9e'),
    'medical': ('#4facfe', '#00f2fe', '#43e97b'),
    'tech': ('#6a11cb', '#2575fc', '#00d2ff'),
    'ocean': ('#006994', '#00b4d8', '#90e0ef'),
    'forest': ('#134e5e', '#71b280', '#2d5016'),
    'gray': ('#6c757d', '#adb5bd', '#dee2e6'),
    'spring': ('#f093fb', '#f5576c', '#ffecd2'),
}

def choose_palette(desc):
    if any(w in desc for w in ['医护', '医院', '病房', '防护服', 'B超', '产房']):
        return 'medical'
    if any(w in desc for w in ['深夜', '夜晚', '月光', '夜景']):
        return 'night'
    if any(w in desc for w in ['黄昏', '夕阳', '晚霞', '日落']):
        return 'sunset'
    if any(w in desc for w in ['日出', '曙光', '阳光', '早晨', '清晨']):
        return 'morning'
    if any(w in desc for w in ['月亮', '中秋']):
        return 'night'
    if any(w in desc for w in ['爱情', '挚爱', '拥抱', '温馨', '温暖', '向日葵', '和好', '牵手', '夕阳']):
        return 'warm'
    if any(w in desc for w in ['迷茫', '困惑', '思考', '沉思']):
        return 'gray'
    if any(w in desc for w in ['海', '青岛', '海边', '海水']):
        return 'ocean'
    if any(w in desc for w in ['山', '风景', '自然', '草原', '森林', '彩虹']):
        return 'nature'
    if any(w in desc for w in ['数据库', 'MySQL', 'Redis', 'MongoDB', 'Oracle']):
        return 'tech'
    if any(w in desc for w in ['代码', '编程', 'Filter', 'Servlet', 'Node.js', 'PHP']):
        return 'tech'
    if any(w in desc for w in ['架构', '流程', '原理', '拓扑', '关系']):
        return 'tech'
    if any(w in desc for w in ['雪', '冬', '冬日']):
        return 'cool'
    if any(w in desc for w in ['春', '花', '花开']):
        return 'spring'
    return 'cool'

# ==================== SVG生成器 ====================

def generate_baby_scene(desc, year, seed):
    """婴儿/亲子场景 - 温馨小手拉大手"""
    c1, c2, c3 = PALETTES['warm']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{c1};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{c2};stop-opacity:1"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:white;stop-opacity:0.3"/>
      <stop offset="100%" style="stop-color:white;stop-opacity:0"/>
    </radialGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <circle cx="400" cy="180" r="120" fill="url(#glow)"/>
  <!-- 大手 -->
  <g transform="translate(250, 140)">
    <ellipse cx="80" cy="60" rx="70" ry="50" fill="white" opacity="0.7"/>
    <ellipse cx="40" cy="30" rx="12" ry="25" fill="white" opacity="0.6" transform="rotate(-20,40,30)"/>
    <ellipse cx="65" cy="20" rx="11" ry="22" fill="white" opacity="0.6"/>
    <ellipse cx="90" cy="22" rx="11" ry="20" fill="white" opacity="0.6"/>
    <ellipse cx="115" cy="30" rx="10" ry="18" fill="white" opacity="0.6" transform="rotate(15,115,30)"/>
  </g>
  <!-- 小手 -->
  <g transform="translate(380, 160) scale(0.4)">
    <ellipse cx="50" cy="40" rx="40" ry="30" fill="white" opacity="0.85"/>
    <ellipse cx="25" cy="18" rx="7" ry="16" fill="white" opacity="0.8" transform="rotate(-15,25,18)"/>
    <ellipse cx="42" cy="12" rx="6" ry="14" fill="white" opacity="0.8"/>
    <ellipse cx="58" cy="14" rx="6" ry="13" fill="white" opacity="0.8"/>
    <ellipse cx="73" cy="20" rx="6" ry="12" fill="white" opacity="0.8" transform="rotate(10,73,20)"/>
  </g>
  <!-- 爱心点缀 -->
  <g opacity="0.4">
    <path d="M 180 100 A 8 8 0 0 0 164 100 C 164 108 180 116 180 116 C 180 116 196 108 196 100 A 8 8 0 0 0 180 100 Z" fill="white"/>
    <path d="M 600 120 A 6 6 0 0 0 588 120 C 588 126 600 132 600 132 C 600 132 612 126 612 120 A 6 6 0 0 0 600 120 Z" fill="white"/>
    <path d="M 650 250 A 5 5 0 0 0 640 250 C 640 255 650 260 650 260 C 650 260 660 255 660 250 A 5 5 0 0 0 650 250 Z" fill="white"/>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_hospital_corridor(desc, year, seed):
    """医院走廊场景"""
    c1, c2, c3 = PALETTES['medical']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{c1};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{c2};stop-opacity:1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 走廊透视 -->
  <polygon points="100,50 700,50 800,350 0,350" fill="white" opacity="0.1"/>
  <polygon points="200,80 600,80 680,350 120,350" fill="white" opacity="0.08"/>
  <!-- 走廊灯 -->
  <circle cx="300" cy="70" r="8" fill="white" opacity="0.6"/>
  <circle cx="400" cy="70" r="8" fill="white" opacity="0.6"/>
  <circle cx="500" cy="70" r="8" fill="white" opacity="0.6"/>
  <!-- 门 -->
  <rect x="180" y="100" width="60" height="120" rx="3" fill="white" opacity="0.15"/>
  <rect x="300" y="100" width="60" height="120" rx="3" fill="white" opacity="0.15"/>
  <rect x="440" y="100" width="60" height="120" rx="3" fill="white" opacity="0.15"/>
  <rect x="560" y="100" width="60" height="120" rx="3" fill="white" opacity="0.15"/>
  <!-- 等待的人影 -->
  <g transform="translate(350, 200)" opacity="0.5">
    <circle cx="20" cy="0" r="12" fill="white"/>
    <path d="M 20 12 L 20 50" stroke="white" stroke-width="8" stroke-linecap="round"/>
    <path d="M 20 25 L 5 40" stroke="white" stroke-width="6" stroke-linecap="round"/>
    <path d="M 20 25 L 35 40" stroke="white" stroke-width="6" stroke-linecap="round"/>
  </g>
  <!-- 十字标志 -->
  <g transform="translate(650, 80)" opacity="0.3">
    <rect x="10" y="0" width="10" height="30" fill="white"/>
    <rect x="0" y="10" width="30" height="10" fill="white"/>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_ultrasound(desc, year, seed):
    """B超影像场景"""
    c1, c2, c3 = PALETTES['medical']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <radialGradient id="scan" cx="50%" cy="40%" r="60%">
      <stop offset="0%" style="stop-color:#1a3a5c;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#0a1628;stop-opacity:1"/>
    </radialGradient>
  </defs>
  <rect width="800" height="400" fill="url(#scan)"/>
  <!-- 扇形扫描区域 -->
  <path d="M 400 50 Q 200 150 150 350 L 650 350 Q 600 150 400 50 Z" fill="#0d2137" opacity="0.8"/>
  <!-- 扫描线 -->
  <g opacity="0.15" stroke="#4facfe" stroke-width="0.5">
    <line x1="400" y1="50" x2="200" y2="350"/>
    <line x1="400" y1="50" x2="300" y2="350"/>
    <line x1="400" y1="50" x2="400" y2="350"/>
    <line x1="400" y1="50" x2="500" y2="350"/>
    <line x1="400" y1="50" x2="600" y2="350"/>
  </g>
  <!-- 胎儿轮廓示意 -->
  <ellipse cx="400" cy="200" rx="60" ry="80" fill="none" stroke="#4facfe" stroke-width="2" opacity="0.5"/>
  <circle cx="380" cy="160" r="25" fill="none" stroke="#4facfe" stroke-width="1.5" opacity="0.4"/>
  <!-- 数据标注 -->
  <g font-family="monospace" font-size="10" fill="#4facfe" opacity="0.6">
    <text x="50" y="30">HR: 140bpm</text>
    <text x="50" y="45">GA: 24w3d</text>
    <text x="600" y="30">BPD: 6.2cm</text>
    <text x="600" y="45">FL: 4.5cm</text>
  </g>
  <!-- 边框 -->
  <rect x="10" y="10" width="780" height="380" fill="none" stroke="#4facfe" stroke-width="1" opacity="0.3" rx="5"/>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_night_feeding(desc, year, seed):
    """深夜喂奶场景"""
    c1, c2, c3 = PALETTES['night']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{c1};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{c2};stop-opacity:1"/>
    </linearGradient>
    <radialGradient id="lamp" cx="50%" cy="0%" r="80%">
      <stop offset="0%" style="stop-color:#fff3cd;stop-opacity:0.4"/>
      <stop offset="100%" style="stop-color:#fff3cd;stop-opacity:0"/>
    </radialGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 星星 -->
  <g fill="white" opacity="0.5">
    <circle cx="100" cy="40" r="1.5"/><circle cx="200" cy="70" r="1"/><circle cx="350" cy="30" r="1.5"/>
    <circle cx="550" cy="50" r="1"/><circle cx="680" cy="35" r="1.5"/><circle cx="750" cy="80" r="1"/>
  </g>
  <!-- 月亮 -->
  <circle cx="680" cy="60" r="25" fill="#f5f5f5" opacity="0.7"/>
  <circle cx="690" cy="52" r="22" fill="{c1}" opacity="0.8"/>
  <!-- 台灯光晕 -->
  <circle cx="350" cy="120" r="150" fill="url(#lamp)"/>
  <!-- 摇椅剪影 -->
  <g transform="translate(300, 150)" opacity="0.4">
    <ellipse cx="50" cy="100" rx="60" ry="8" fill="white"/>
    <path d="M 20 100 L 30 40 L 70 40 L 80 100" stroke="white" stroke-width="4" fill="none"/>
    <path d="M 35 40 L 35 20" stroke="white" stroke-width="3" fill="none"/>
    <circle cx="35" cy="15" r="12" fill="white"/>
  </g>
  <!-- 奶瓶 -->
  <g transform="translate(450, 200)" opacity="0.3">
    <rect x="0" y="0" width="20" height="50" rx="5" fill="white"/>
    <rect x="3" y="-15" width="14" height="20" rx="3" fill="white"/>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="#4facfe">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_protective_suit(desc, year, seed):
    """防护服背影场景"""
    c1, c2, c3 = PALETTES['medical']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{c1};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{c2};stop-opacity:1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 病房门框 -->
  <rect x="250" y="60" width="300" height="280" rx="5" fill="white" opacity="0.1"/>
  <rect x="260" y="70" width="280" height="270" fill="none" stroke="white" stroke-width="2" opacity="0.2"/>
  <!-- 防护服背影 -->
  <g transform="translate(340, 100)" opacity="0.7">
    <!-- 头罩 -->
    <circle cx="60" cy="30" r="28" fill="white"/>
    <!-- 护目镜 -->
    <rect x="42" y="22" width="36" height="14" rx="4" fill="#4facfe" opacity="0.5"/>
    <!-- 身体 -->
    <path d="M 60 58 L 60 180" stroke="white" stroke-width="35" stroke-linecap="round"/>
    <!-- 手臂 -->
    <path d="M 60 90 L 20 140" stroke="white" stroke-width="16" stroke-linecap="round"/>
    <path d="M 60 90 L 100 140" stroke="white" stroke-width="16" stroke-linecap="round"/>
    <!-- 手套 -->
    <circle cx="20" cy="145" r="10" fill="white"/>
    <circle cx="100" cy="145" r="10" fill="white"/>
    <!-- 背上的字 -->
    <text x="60" y="140" text-anchor="middle" font-size="14" font-weight="bold" fill="#4facfe" opacity="0.8">加油</text>
  </g>
  <!-- 光晕 -->
  <circle cx="400" cy="200" r="100" fill="url(#glow2)" opacity="0.3"/>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>
  <defs><radialGradient id="glow2" cx="50%" cy="50%" r="50%"><stop offset="0%" style="stop-color:white;stop-opacity:0.3"/><stop offset="100%" style="stop-color:white;stop-opacity:0"/></radialGradient></defs>'''

def generate_tv_watching(desc, year, seed):
    """看电视场景"""
    c1, c2, c3 = PALETTES['warm']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:{c1};stop-opacity:1"/><stop offset="100%" style="stop-color:{c2};stop-opacity:1"/></linearGradient></defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 电视屏幕 -->
  <rect x="250" y="60" width="300" height="180" rx="10" fill="#1a1a2e" opacity="0.8"/>
  <rect x="260" y="70" width="280" height="160" rx="5" fill="#2a2a4e"/>
  <!-- 屏幕光 -->
  <rect x="270" y="80" width="260" height="140" fill="white" opacity="0.05"/>
  <!-- 播放按钮 -->
  <polygon points="390,130 390,170 430,150" fill="white" opacity="0.4"/>
  <!-- 沙发 -->
  <rect x="200" y="280" width="400" height="60" rx="15" fill="white" opacity="0.3"/>
  <rect x="220" y="260" width="360" height="30" rx="10" fill="white" opacity="0.25"/>
  <!-- 电视柜 -->
  <rect x="280" y="240" width="240" height="15" rx="3" fill="white" opacity="0.2"/>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_promotion(desc, year, seed):
    """晋升答辩/办公室场景"""
    c1, c2, c3 = PALETTES['tech']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:{c1};stop-opacity:1"/><stop offset="100%" style="stop-color:{c2};stop-opacity:1"/></linearGradient></defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 投影屏幕 -->
  <rect x="150" y="40" width="500" height="160" rx="5" fill="white" opacity="0.15"/>
  <rect x="160" y="50" width="480" height="140" fill="white" opacity="0.1"/>
  <!-- PPT内容示意 -->
  <rect x="180" y="65" width="200" height="12" rx="3" fill="white" opacity="0.4"/>
  <rect x="180" y="85" width="160" height="8" rx="2" fill="white" opacity="0.25"/>
  <rect x="180" y="100" width="140" height="8" rx="2" fill="white" opacity="0.25"/>
  <rect x="180" y="115" width="170" height="8" rx="2" fill="white" opacity="0.25"/>
  <!-- 图表示意 -->
  <rect x="420" y="70" width="80" height="100" rx="3" fill="white" opacity="0.2"/>
  <rect x="430" y="140" width="20" height="25" fill="white" opacity="0.4"/>
  <rect x="455" y="120" width="20" height="45" fill="white" opacity="0.5"/>
  <rect x="480" y="100" width="20" height="65" fill="white" opacity="0.6"/>
  <!-- 演讲台 -->
  <rect x="350" y="230" width="100" height="80" rx="5" fill="white" opacity="0.2"/>
  <!-- 掌声/点赞 -->
  <g transform="translate(600, 250)" opacity="0.4">
    <text font-size="40">👏</text>
  </g>
  <!-- 奖杯 -->
  <g transform="translate(120, 250)" opacity="0.5">
    <path d="M 30 0 L 30 50 L 10 60 L 50 60 L 30 50" fill="#FFE66D"/>
    <ellipse cx="30" cy="0" rx="20" ry="25" fill="none" stroke="#FFE66D" stroke-width="4"/>
    <rect x="20" y="60" width="20" height="10" fill="#FFE66D"/>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_family_photo(desc, year, seed):
    """一家三口合影"""
    c1, c2, c3 = PALETTES['morning']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{c1};stop-opacity:1"/>
      <stop offset="50%" style="stop-color:{c2};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{c3};stop-opacity:1"/>
    </linearGradient>
    <radialGradient id="sun" cx="80%" cy="20%" r="30%">
      <stop offset="0%" style="stop-color:#fff7cd;stop-opacity:0.5"/>
      <stop offset="100%" style="stop-color:#fff7cd;stop-opacity:0"/>
    </radialGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <circle cx="650" cy="80" r="100" fill="url(#sun)"/>
  <!-- 太阳光线 -->
  <g stroke="#FFE66D" stroke-width="2" opacity="0.3">
    <line x1="650" y1="50" x2="650" y2="20"/><line x1="670" y1="55" x2="690" y2="30"/>
    <line x1="680" y1="80" x2="710" y2="80"/><line x1="670" y1="105" x2="690" y2="130"/>
  </g>
  <!-- 草地 -->
  <ellipse cx="400" cy="350" rx="450" ry="80" fill="#4a7c59" opacity="0.4"/>
  <!-- 一家三口剪影 -->
  <g transform="translate(280, 160)" opacity="0.7">
    <!-- 爸爸 -->
    <circle cx="60" cy="30" r="22" fill="white"/>
    <path d="M 60 52 L 60 120" stroke="white" stroke-width="16" stroke-linecap="round"/>
    <path d="M 60 75 L 30 100" stroke="white" stroke-width="12" stroke-linecap="round"/>
    <!-- 妈妈 -->
    <circle cx="160" cy="35" r="20" fill="white"/>
    <path d="M 160 55 L 160 115" stroke="white" stroke-width="14" stroke-linecap="round"/>
    <path d="M 160 75 L 130 100" stroke="white" stroke-width="11" stroke-linecap="round"/>
    <!-- 宝宝（中间被抱着） -->
    <circle cx="110" cy="90" r="14" fill="white"/>
    <path d="M 110 104 L 110 130" stroke="white" stroke-width="10" stroke-linecap="round"/>
  </g>
  <!-- 花朵 -->
  <g opacity="0.5">
    <circle cx="150" cy="300" r="8" fill="white"/><circle cx="150" cy="300" r="4" fill="#FF6B6B"/>
    <circle cx="650" cy="310" r="6" fill="white"/><circle cx="650" cy="310" r="3" fill="#FFE66D"/>
    <circle cx="500" cy="290" r="7" fill="white"/><circle cx="500" cy="290" r="3.5" fill="#FF6B6B"/>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c2}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_confused(desc, year, seed):
    """迷茫/困惑场景"""
    c1, c2, c3 = PALETTES['gray']
    s = get_hash_seed(desc)
    fog_positions = [(s % 200) + 50, ((s >> 8) % 150) + 80, ((s >> 16) % 180) + 60]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:{c1};stop-opacity:1"/><stop offset="100%" style="stop-color:{c2};stop-opacity:1"/></linearGradient></defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 迷雾 -->
  <ellipse cx="{fog_positions[0]}" cy="150" rx="200" ry="80" fill="white" opacity="0.08"/>
  <ellipse cx="{fog_positions[1]}" cy="200" rx="180" ry="60" fill="white" opacity="0.06"/>
  <ellipse cx="{fog_positions[2]}" cy="100" rx="150" ry="70" fill="white" opacity="0.07"/>
  <!-- 岔路口 -->
  <path d="M 400 350 L 400 250" stroke="white" stroke-width="4" opacity="0.3"/>
  <path d="M 400 250 Q 200 220 100 280" stroke="white" stroke-width="3" opacity="0.2" fill="none"/>
  <path d="M 400 250 Q 600 220 700 280" stroke="white" stroke-width="3" opacity="0.2" fill="none"/>
  <!-- 思考的人 -->
  <g transform="translate(370, 200)" opacity="0.5">
    <circle cx="30" cy="0" r="18" fill="white"/>
    <path d="M 30 18 L 30 70" stroke="white" stroke-width="12" stroke-linecap="round"/>
    <path d="M 30 35 L 10 55" stroke="white" stroke-width="8" stroke-linecap="round"/>
    <path d="M 30 35 L 50 25" stroke="white" stroke-width="8" stroke-linecap="round"/>
  </g>
  <!-- 问号 -->
  <text x="460" y="180" font-size="60" font-weight="bold" fill="white" opacity="0.2">?</text>
  <text x="320" y="150" font-size="40" font-weight="bold" fill="white" opacity="0.15">?</text>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_love(desc, year, seed):
    """爱情/遇见挚爱"""
    c1, c2, c3 = PALETTES['warm']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{c1};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{c2};stop-opacity:1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 飘落的爱心 -->
  <g opacity="0.3">
    <path d="M 100 50 A 12 12 0 0 0 76 50 C 76 62 100 74 100 74 C 100 74 124 62 124 50 A 12 12 0 0 0 100 50 Z" fill="white"/>
    <path d="M 300 80 A 8 8 0 0 0 284 80 C 284 88 300 96 300 96 C 300 96 316 88 316 80 A 8 8 0 0 0 300 80 Z" fill="white"/>
    <path d="M 550 40 A 10 10 0 0 0 530 40 C 530 50 550 60 550 60 C 550 60 570 50 570 40 A 10 10 0 0 0 550 40 Z" fill="white"/>
    <path d="M 700 120 A 7 7 0 0 0 686 120 C 686 127 700 134 700 134 C 700 134 714 127 714 120 A 7 7 0 0 0 700 120 Z" fill="white"/>
    <path d="M 200 200 A 9 9 0 0 0 182 200 C 182 209 200 218 200 218 C 200 218 218 209 218 200 A 9 9 0 0 0 200 200 Z" fill="white"/>
    <path d="M 600 220 A 11 11 0 0 0 578 220 C 578 231 600 242 600 242 C 600 242 622 231 622 220 A 11 11 0 0 0 600 220 Z" fill="white"/>
  </g>
  <!-- 咖啡馆/相遇场景 -->
  <g transform="translate(250, 140)" opacity="0.4">
    <!-- 桌子 -->
    <ellipse cx="150" cy="120" rx="100" ry="20" fill="white"/>
    <rect x="145" y="120" width="10" height="60" fill="white"/>
    <!-- 两杯咖啡 -->
    <ellipse cx="100" cy="100" rx="15" ry="10" fill="white" opacity="0.7"/>
    <ellipse cx="200" cy="100" rx="15" ry="10" fill="white" opacity="0.7"/>
    <!-- 蒸汽 -->
    <path d="M 95 90 Q 100 80 95 70" stroke="white" stroke-width="2" fill="none" opacity="0.5"/>
    <path d="M 195 90 Q 200 80 195 70" stroke="white" stroke-width="2" fill="none" opacity="0.5"/>
  </g>
  <!-- 两个人影 -->
  <g opacity="0.5">
    <circle cx="330" cy="180" r="16" fill="white"/>
    <path d="M 330 196 L 330 260" stroke="white" stroke-width="12" stroke-linecap="round"/>
    <circle cx="430" cy="185" r="15" fill="white"/>
    <path d="M 430 200 L 430 260" stroke="white" stroke-width="11" stroke-linecap="round"/>
    <!-- 牵手 -->
    <path d="M 330 220 Q 380 230 430 220" stroke="white" stroke-width="3" fill="none" opacity="0.6"/>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_sunflower(desc, year, seed):
    """向日葵与和好"""
    c1, c2, c3 = PALETTES['warm']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:{c1};stop-opacity:1"/><stop offset="100%" style="stop-color:{c2};stop-opacity:1"/></linearGradient></defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 向日葵1 -->
  <g transform="translate(200, 200)" opacity="0.7">
    <line x1="0" y1="0" x2="0" y2="120" stroke="#4a7c59" stroke-width="6"/>
    <ellipse cx="0" cy="100" rx="20" ry="10" fill="#4a7c59" opacity="0.6"/>
    <g>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(30)"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(60)"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(90)"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(120)"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(150)"/>
    </g>
    <circle cx="0" cy="0" r="15" fill="#8B4513"/>
  </g>
  <!-- 向日葵2 -->
  <g transform="translate(400, 180) scale(0.8)" opacity="0.6">
    <line x1="0" y1="0" x2="0" y2="120" stroke="#4a7c59" stroke-width="6"/>
    <g>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(30)"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(60)"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(90)"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(120)"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(150)"/>
    </g>
    <circle cx="0" cy="0" r="15" fill="#8B4513"/>
  </g>
  <!-- 向日葵3 -->
  <g transform="translate(600, 210) scale(0.7)" opacity="0.5">
    <line x1="0" y1="0" x2="0" y2="120" stroke="#4a7c59" stroke-width="6"/>
    <g>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(30)"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(60)"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(90)"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(120)"/>
      <ellipse cx="0" cy="-25" rx="12" ry="25" fill="#FFE66D" transform="rotate(150)"/>
    </g>
    <circle cx="0" cy="0" r="15" fill="#8B4513"/>
  </g>
  <!-- 地面 -->
  <ellipse cx="400" cy="350" rx="400" ry="60" fill="#4a7c59" opacity="0.3"/>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_expectation(desc, year, seed):
    """期待/希望/未来"""
    c1, c2, c3 = PALETTES['morning']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{c1};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{c2};stop-opacity:1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 道路通向远方 -->
  <polygon points="350,350 450,350 500,200 300,200" fill="white" opacity="0.15"/>
  <!-- 远方的光 -->
  <circle cx="400" cy="180" r="60" fill="#FFE66D" opacity="0.4"/>
  <circle cx="400" cy="180" r="40" fill="#FFE66D" opacity="0.5"/>
  <circle cx="400" cy="180" r="20" fill="white" opacity="0.7"/>
  <!-- 飞鸟 -->
  <g opacity="0.4">
    <path d="M 150 80 Q 160 70 170 80 Q 180 70 190 80" stroke="white" stroke-width="2" fill="none"/>
    <path d="M 200 60 Q 208 52 216 60 Q 224 52 232 60" stroke="white" stroke-width="1.5" fill="none"/>
    <path d="M 175 90 Q 182 83 189 90 Q 196 83 203 90" stroke="white" stroke-width="1.5" fill="none"/>
  </g>
  <!-- 近处的草 -->
  <g stroke="#4a7c59" stroke-width="2" opacity="0.5">
    <line x1="100" y1="350" x2="95" y2="320"/><line x1="100" y1="350" x2="105" y2="325"/>
    <line x1="700" y1="350" x2="695" y2="315"/><line x1="700" y1="350" x2="705" y2="320"/>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c2}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_window(desc, year, seed):
    """窗台/窗景"""
    c1, c2, c3 = PALETTES['gray']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:{c1};stop-opacity:1"/><stop offset="100%" style="stop-color:{c2};stop-opacity:1"/></linearGradient></defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 窗户框架 -->
  <rect x="200" y="40" width="400" height="250" rx="5" fill="white" opacity="0.15"/>
  <rect x="210" y="50" width="180" height="230" fill="white" opacity="0.08"/>
  <rect x="410" y="50" width="180" height="230" fill="white" opacity="0.08"/>
  <line x1="400" y1="40" x2="400" y2="290" stroke="white" stroke-width="4" opacity="0.2"/>
  <line x1="200" y1="165" x2="600" y2="165" stroke="white" stroke-width="4" opacity="0.2"/>
  <!-- 窗台上的植物 -->
  <g transform="translate(250, 290)" opacity="0.5">
    <rect x="-15" y="0" width="30" height="25" rx="3" fill="white"/>
    <path d="M 0 0 Q -10 -20 -5 -35" stroke="#4a7c59" stroke-width="3" fill="none"/>
    <path d="M 0 0 Q 10 -15 15 -30" stroke="#4a7c59" stroke-width="3" fill="none"/>
    <ellipse cx="-5" cy="-35" rx="8" ry="12" fill="#4a7c59" opacity="0.6"/>
    <ellipse cx="15" cy="-30" rx="7" ry="10" fill="#4a7c59" opacity="0.6"/>
  </g>
  <!-- 窗外的云 -->
  <ellipse cx="300" cy="100" rx="50" ry="18" fill="white" opacity="0.15"/>
  <ellipse cx="500" cy="120" rx="40" ry="15" fill="white" opacity="0.12"/>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_study_room(desc, year, seed):
    """自习室/图书馆场景"""
    c1, c2, c3 = PALETTES['night']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:{c1};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{c2};stop-opacity:1"/>
    </linearGradient>
    <radialGradient id="desklamp" cx="50%" cy="0%" r="60%">
      <stop offset="0%" style="stop-color:#fff3cd;stop-opacity:0.5"/>
      <stop offset="100%" style="stop-color:#fff3cd;stop-opacity:0"/>
    </radialGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 书架背景 -->
  <g opacity="0.2">
    <rect x="0" y="0" width="800" height="80" fill="white" opacity="0.1"/>
    <rect x="20" y="10" width="30" height="60" fill="white" opacity="0.15"/>
    <rect x="60" y="15" width="25" height="55" fill="white" opacity="0.12"/>
    <rect x="95" y="8" width="28" height="62" fill="white" opacity="0.14"/>
    <rect x="135" y="12" width="22" height="58" fill="white" opacity="0.13"/>
    <rect x="600" y="10" width="30" height="60" fill="white" opacity="0.15"/>
    <rect x="640" y="15" width="25" height="55" fill="white" opacity="0.12"/>
    <rect x="675" y="8" width="28" height="62" fill="white" opacity="0.14"/>
    <rect x="715" y="12" width="22" height="58" fill="white" opacity="0.13"/>
  </g>
  <!-- 桌子 -->
  <rect x="200" y="200" width="400" height="15" rx="3" fill="white" opacity="0.3"/>
  <!-- 台灯 -->
  <circle cx="350" cy="150" r="80" fill="url(#desklamp)"/>
  <g transform="translate(340, 100)" opacity="0.6">
    <rect x="-3" y="0" width="6" height="50" fill="white"/>
    <ellipse cx="0" cy="55" rx="25" ry="8" fill="white"/>
  </g>
  <!-- 书本 -->
  <g transform="translate(280, 185)" opacity="0.5">
    <rect x="0" y="0" width="50" height="15" rx="2" fill="#FF6B6B"/>
    <rect x="55" y="-3" width="45" height="18" rx="2" fill="#4facfe"/>
    <rect x="105" y="2" width="40" height="13" rx="2" fill="#FFE66D"/>
  </g>
  <!-- 笔记本电脑 -->
  <rect x="420" y="175" width="100" height="25" rx="3" fill="white" opacity="0.4"/>
  <rect x="430" y="165" width="80" height="15" rx="2" fill="white" opacity="0.35"/>
  <!-- 坐着的人 -->
  <g transform="translate(370, 130)" opacity="0.4">
    <circle cx="30" cy="0" r="18" fill="white"/>
    <path d="M 30 18 L 30 70" stroke="white" stroke-width="14" stroke-linecap="round"/>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="#4facfe">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_database_tech(desc, year, seed):
    """数据库技术图"""
    s = get_hash_seed(desc)
    db_type = 'mysql'
    if 'redis' in desc.lower():
        db_type = 'redis'
    elif 'mongodb' in desc.lower() or 'mongo' in desc.lower():
        db_type = 'mongodb'
    elif 'oracle' in desc.lower():
        db_type = 'oracle'
    
    colors = {'mysql': ('#00758f', '#00bcd4'), 'redis': ('#dc382d', '#ff6b6b'), 
              'mongodb': ('#47a248', '#7dcea0'), 'oracle': ('f80100', '#ff6b6b')}
    c1, c2 = colors.get(db_type, ('#00758f', '#00bcd4'))
    
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{c1};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{c2};stop-opacity:1"/>
    </linearGradient>
    <pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse">
      <path d="M 50 0 L 0 0 0 50" fill="none" stroke="white" stroke-width="0.5" opacity="0.1"/>
    </pattern>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <rect width="800" height="400" fill="url(#grid)"/>
  <!-- 数据库圆柱 -->
  <g transform="translate(300, 80)">
    <ellipse cx="100" cy="30" rx="80" ry="25" fill="white" opacity="0.9"/>
    <rect x="20" y="30" width="160" height="120" fill="white" opacity="0.8"/>
    <ellipse cx="100" cy="150" rx="80" ry="25" fill="white" opacity="0.7"/>
    <line x1="20" y1="60" x2="180" y2="60" stroke="{c1}" stroke-width="1" opacity="0.3"/>
    <line x1="20" y1="90" x2="180" y2="90" stroke="{c1}" stroke-width="1" opacity="0.3"/>
    <line x1="20" y1="120" x2="180" y2="120" stroke="{c1}" stroke-width="1" opacity="0.3"/>
  </g>
  <!-- 连接线和节点 -->
  <g stroke="white" stroke-width="2" fill="none" opacity="0.4">
    <path d="M 150 150 L 150 200 L 250 200"/>
    <path d="M 650 150 L 650 200 L 550 200"/>
  </g>
  <g transform="translate(50, 200)" opacity="0.6">
    <rect width="80" height="60" rx="8" fill="white"/><circle cx="40" cy="30" r="15" fill="{c1}"/>
  </g>
  <g transform="translate(670, 200)" opacity="0.6">
    <rect width="80" height="60" rx="8" fill="white"/><circle cx="40" cy="30" r="15" fill="{c1}"/>
  </g>
  <!-- SQL装饰 -->
  <g font-family="monospace" font-size="12" fill="white" opacity="0.15">
    <text x="30" y="320">SELECT * FROM</text>
    <text x="30" y="340">WHERE id = 1</text>
    <text x="550" y="320">INSERT INTO</text>
    <text x="550" y="340">VALUES (...)</text>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_code_tech(desc, year, seed):
    """代码/编程技术图"""
    c1, c2, c3 = PALETTES['tech']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{c1};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{c2};stop-opacity:1"/>
    </linearGradient>
    <pattern id="codeGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="white" stroke-width="0.5" opacity="0.1"/>
    </pattern>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <rect width="800" height="400" fill="url(#codeGrid)"/>
  <!-- 代码编辑器窗口 -->
  <g transform="translate(120, 60)">
    <rect width="560" height="240" rx="10" fill="white" opacity="0.9"/>
    <rect width="560" height="35" rx="10" fill="#f0f0f0"/>
    <circle cx="25" cy="17" r="7" fill="#ff5f56"/>
    <circle cx="48" cy="17" r="7" fill="#ffbd2e"/>
    <circle cx="71" cy="17" r="7" fill="#27c93f"/>
    <!-- 代码行 -->
    <g font-family="monospace" font-size="11" opacity="0.6">
      <rect x="20" y="50" width="120" height="8" rx="2" fill="#c678dd"/>
      <rect x="150" y="50" width="80" height="8" rx="2" fill="#61afef"/>
      <rect x="20" y="68" width="40" height="8" rx="2" fill="#e5c07b"/>
      <rect x="70" y="68" width="150" height="8" rx="2" fill="#98c379"/>
      <rect x="20" y="86" width="100" height="8" rx="2" fill="#c678dd"/>
      <rect x="130" y="86" width="90" height="8" rx="2" fill="#98c379"/>
      <rect x="20" y="104" width="60" height="8" rx="2" fill="#e06c75"/>
      <rect x="20" y="122" width="30" height="8" rx="2" fill="#56b6c2"/>
      <rect x="20" y="150" width="140" height="8" rx="2" fill="#61afef"/>
      <rect x="20" y="168" width="90" height="8" rx="2" fill="#e5c07b"/>
      <rect x="120" y="168" width="110" height="8" rx="2" fill="#98c379"/>
      <rect x="20" y="186" width="50" height="8" rx="2" fill="#c678dd"/>
    </g>
  </g>
  <!-- 代码符号 -->
  <g opacity="0.12" font-family="monospace" font-size="30" fill="white">
    <text x="50" y="350">&lt;/&gt;</text>
    <text x="650" y="80">{'{}'}</text>
    <text x="580" y="350">[]</text>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_architecture(desc, year, seed):
    """架构图"""
    c1, c2, c3 = PALETTES['nature']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:{c1};stop-opacity:1"/><stop offset="100%" style="stop-color:{c2};stop-opacity:1"/></linearGradient></defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <rect width="800" height="400" fill="url(#grid)" opacity="0.5"/>
  <!-- 架构层 -->
  <g transform="translate(100, 40)">
    <rect width="600" height="60" rx="10" fill="white" opacity="0.85"/>
    <text x="300" y="35" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">Application Layer</text>
    <polygon points="300,110 290,100 310,100" fill="white" opacity="0.5"/>
    <rect y="110" width="600" height="60" rx="10" fill="white" opacity="0.75"/>
    <text x="300" y="145" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">Service Layer</text>
    <polygon points="300,180 290,170 310,170" fill="white" opacity="0.5"/>
    <rect y="180" width="600" height="60" rx="10" fill="white" opacity="0.65"/>
    <text x="300" y="215" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">Data Layer</text>
    <polygon points="300,250 290,240 310,240" fill="white" opacity="0.5"/>
    <rect y="250" width="600" height="60" rx="10" fill="white" opacity="0.55"/>
    <text x="300" y="285" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">Infrastructure</text>
  </g>
  <defs><pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse"><path d="M 50 0 L 0 0 0 50" fill="none" stroke="white" stroke-width="0.5" opacity="0.08"/></pattern></defs>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_flowchart(desc, year, seed):
    """流程图"""
    c1, c2, c3 = PALETTES['sunset']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:{c1};stop-opacity:1"/><stop offset="100%" style="stop-color:{c2};stop-opacity:1"/></linearGradient></defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <g transform="translate(300, 30)">
    <rect width="200" height="45" rx="22" fill="white" opacity="0.9"/>
    <text x="100" y="28" text-anchor="middle" font-size="13" font-weight="bold" fill="{c1}">Start</text>
    <polygon points="100,55 92,47 108,47" fill="white" opacity="0.6"/>
    <rect y="65" width="200" height="45" rx="8" fill="white" opacity="0.8"/>
    <text x="100" y="92" text-anchor="middle" font-size="12" fill="#333">Process A</text>
    <polygon points="100,120 92,112 108,112" fill="white" opacity="0.6"/>
    <polygon points="100,130 180,160 100,190 20,160" fill="white" opacity="0.75"/>
    <text x="100" y="165" text-anchor="middle" font-size="11" fill="#333">Condition</text>
    <polygon points="100,200 92,192 108,192" fill="white" opacity="0.6"/>
    <rect y="210" width="200" height="45" rx="8" fill="white" opacity="0.8"/>
    <text x="100" y="237" text-anchor="middle" font-size="12" fill="#333">Process B</text>
    <polygon points="100,265 92,257 108,257" fill="white" opacity="0.6"/>
    <rect y="275" width="200" height="45" rx="22" fill="white" opacity="0.9"/>
    <text x="100" y="303" text-anchor="middle" font-size="13" font-weight="bold" fill="{c1}">End</text>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_nature_landscape(desc, year, seed):
    """通用自然风景"""
    c1, c2, c3 = PALETTES['nature']
    s = get_hash_seed(desc)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#87ceeb;stop-opacity:1"/>
      <stop offset="60%" style="stop-color:{c1};stop-opacity:1"/>
      <stop offset="100%" style="stop-color:{c2};stop-opacity:1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 云 -->
  <ellipse cx="150" cy="70" rx="70" ry="25" fill="white" opacity="0.6"/>
  <ellipse cx="180" cy="60" rx="50" ry="22" fill="white" opacity="0.5"/>
  <ellipse cx="550" cy="90" rx="60" ry="20" fill="white" opacity="0.5"/>
  <!-- 远山 -->
  <polygon points="0,280 80,180 180,230 280,160 400,220 520,170 650,210 800,190 800,280" fill="#2d5016" opacity="0.5"/>
  <!-- 近山 -->
  <polygon points="0,310 100,250 220,280 350,240 480,270 600,235 720,260 800,245 800,310" fill="#4a7c59" opacity="0.6"/>
  <!-- 草地 -->
  <rect x="0" y="300" width="800" height="100" fill="#2d5016" opacity="0.4"/>
  <!-- 花 -->
  <g opacity="0.6">
    <circle cx="100" cy="320" r="6" fill="white"/><circle cx="100" cy="320" r="3" fill="#FF6B6B"/>
    <circle cx="300" cy="330" r="5" fill="white"/><circle cx="300" cy="330" r="2.5" fill="#FFE66D"/>
    <circle cx="500" cy="315" r="6" fill="white"/><circle cx="500" cy="315" r="3" fill="#f093fb"/>
    <circle cx="700" cy="325" r="5" fill="white"/><circle cx="700" cy="325" r="2.5" fill="#4facfe"/>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_moon_night(desc, year, seed):
    """月夜风景"""
    c1, c2, c3 = PALETTES['night']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#0a0e27;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#1a237e;stop-opacity:1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 星星 -->
  <g fill="white">
    <circle cx="50" cy="30" r="1.5" opacity="0.8"/><circle cx="120" cy="80" r="1" opacity="0.6"/>
    <circle cx="200" cy="45" r="1.5" opacity="0.7"/><circle cx="280" cy="90" r="1" opacity="0.9"/>
    <circle cx="350" cy="50" r="1.5" opacity="0.6"/><circle cx="480" cy="70" r="1" opacity="0.8"/>
    <circle cx="550" cy="40" r="1.5" opacity="0.7"/><circle cx="720" cy="50" r="1.5" opacity="0.6"/>
    <circle cx="750" cy="80" r="1" opacity="0.8"/><circle cx="100" cy="150" r="1" opacity="0.7"/>
    <circle cx="300" cy="140" r="1.5" opacity="0.8"/><circle cx="600" cy="130" r="1" opacity="0.6"/>
  </g>
  <!-- 月亮 -->
  <circle cx="620" cy="80" r="45" fill="#f5f5f5" opacity="0.85"/>
  <circle cx="605" cy="68" r="38" fill="#0a0e27" opacity="0.8"/>
  <circle cx="620" cy="80" r="65" fill="#f5f5f5" opacity="0.1"/>
  <!-- 地面 -->
  <polygon points="0,300 100,260 200,280 300,250 400,270 500,240 600,260 700,230 800,250 800,300" fill="#1a1a2e" opacity="0.7"/>
  <rect x="0" y="300" width="800" height="100" fill="#0d1117" opacity="0.6"/>
  <!-- 水面倒影 -->
  <ellipse cx="620" cy="330" rx="30" ry="6" fill="#f5f5f5" opacity="0.15"/>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="#4facfe">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_sunset_scene(desc, year, seed):
    """黄昏/夕阳场景"""
    c1, c2, c3 = PALETTES['sunset']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#ff7e5f;stop-opacity:1"/>
      <stop offset="50%" style="stop-color:#feb47b;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#ff9a56;stop-opacity:1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 夕阳 -->
  <circle cx="400" cy="220" r="70" fill="#ff4500" opacity="0.7"/>
  <circle cx="400" cy="220" r="100" fill="#ff4500" opacity="0.2"/>
  <!-- 云 -->
  <g opacity="0.4">
    <ellipse cx="200" cy="150" rx="80" ry="15" fill="#ff6347"/>
    <ellipse cx="600" cy="170" rx="60" ry="12" fill="#ff6347"/>
  </g>
  <!-- 地面剪影 -->
  <polygon points="0,280 100,260 200,270 300,250 400,265 500,245 600,260 700,235 800,250 800,280" fill="#2d1810" opacity="0.6"/>
  <rect x="0" y="280" width="800" height="120" fill="#1a0f0a" opacity="0.7"/>
  <!-- 树剪影 -->
  <g fill="#2d1810" opacity="0.7">
    <g transform="translate(120, 240)">
      <rect x="-4" y="0" width="8" height="40"/>
      <circle cx="0" cy="-8" r="25"/><circle cx="-18" cy="8" r="20"/><circle cx="18" cy="8" r="20"/>
    </g>
    <g transform="translate(680, 250)">
      <rect x="-3" y="0" width="6" height="35"/>
      <circle cx="0" cy="-6" r="20"/><circle cx="-14" cy="6" r="16"/><circle cx="14" cy="6" r="16"/>
    </g>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_sea_scene(desc, year, seed):
    """海景"""
    c1, c2, c3 = PALETTES['ocean']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs>
    <linearGradient id="sky" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#87ceeb;stop-opacity:1"/>
      <stop offset="100%" style="stop-color:#006994;stop-opacity:1"/>
    </linearGradient>
  </defs>
  <rect width="800" height="200" fill="url(#sky)"/>
  <!-- 太阳 -->
  <circle cx="400" cy="120" r="50" fill="#FFE66D" opacity="0.8"/>
  <circle cx="400" cy="120" r="70" fill="#FFE66D" opacity="0.2"/>
  <!-- 海鸥 -->
  <g opacity="0.5">
    <path d="M 150 60 Q 160 50 170 60 Q 180 50 190 60" stroke="white" stroke-width="2" fill="none"/>
    <path d="M 600 80 Q 610 70 620 80 Q 630 70 640 80" stroke="white" stroke-width="2" fill="none"/>
  </g>
  <!-- 海 -->
  <rect x="0" y="200" width="800" height="200" fill="#006994"/>
  <!-- 波浪 -->
  <path d="M 0 220 Q 100 210 200 220 T 400 220 T 600 220 T 800 220" stroke="white" stroke-width="2" fill="none" opacity="0.3"/>
  <path d="M 0 250 Q 100 240 200 250 T 400 250 T 600 250 T 800 250" stroke="white" stroke-width="2" fill="none" opacity="0.25"/>
  <path d="M 0 280 Q 100 270 200 280 T 400 280 T 600 280 T 800 280" stroke="white" stroke-width="2" fill="none" opacity="0.2"/>
  <path d="M 0 310 Q 100 300 200 310 T 400 310 T 600 310 T 800 310" stroke="white" stroke-width="2" fill="none" opacity="0.15"/>
  <path d="M 0 340 Q 100 330 200 340 T 400 340 T 600 340 T 800 340" stroke="white" stroke-width="2" fill="none" opacity="0.1"/>
  <!-- 帆船 -->
  <g transform="translate(350, 220)" opacity="0.6">
    <polygon points="0,0 20,-40 40,0" fill="white"/>
    <path d="M -10 0 L 50 0 L 45 10 L -5 10 Z" fill="#8B4513"/>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_default_landscape(desc, year, seed):
    """默认风景"""
    c1, c2, c3 = PALETTES['cool']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:{c1};stop-opacity:1"/><stop offset="100%" style="stop-color:{c2};stop-opacity:1"/></linearGradient></defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <ellipse cx="200" cy="350" rx="300" ry="100" fill="white" opacity="0.08"/>
  <ellipse cx="600" cy="360" rx="250" ry="80" fill="white" opacity="0.06"/>
  <g opacity="0.3">
    <g transform="translate(150, 260)">
      <rect x="-4" y="0" width="8" height="50" fill="white"/>
      <circle cx="0" cy="-8" r="28" fill="white"/><circle cx="-18" cy="8" r="22" fill="white"/><circle cx="18" cy="8" r="22" fill="white"/>
    </g>
    <g transform="translate(400, 270)">
      <rect x="-3" y="0" width="6" height="40" fill="white"/>
      <circle cx="0" cy="-6" r="22" fill="white"/><circle cx="-14" cy="6" r="18" fill="white"/><circle cx="14" cy="6" r="18" fill="white"/>
    </g>
    <g transform="translate(650, 255)">
      <rect x="-5" y="0" width="10" height="55" fill="white"/>
      <circle cx="0" cy="-10" r="30" fill="white"/><circle cx="-20" cy="8" r="24" fill="white"/><circle cx="20" cy="8" r="24" fill="white"/>
    </g>
  </g>
  <circle cx="150" cy="80" r="25" fill="white" opacity="0.06"/>
  <circle cx="650" cy="120" r="35" fill="white" opacity="0.05"/>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_snow_scene(desc, year, seed):
    """雪景"""
    c1, c2, c3 = PALETTES['cool']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs><linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" style="stop-color:#a8c0d6;stop-opacity:1"/><stop offset="100%" style="stop-color:#d4e4f1;stop-opacity:1"/></linearGradient></defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 雪花 -->
  <g fill="white" opacity="0.7">
    <circle cx="50" cy="30" r="3"/><circle cx="150" cy="60" r="2"/><circle cx="250" cy="40" r="3"/>
    <circle cx="350" cy="70" r="2.5"/><circle cx="450" cy="25" r="3"/><circle cx="550" cy="55" r="2"/>
    <circle cx="650" cy="35" r="3"/><circle cx="750" cy="65" r="2"/><circle cx="100" cy="120" r="2.5"/>
    <circle cx="300" cy="130" r="2"/><circle cx="500" cy="110" r="3"/><circle cx="700" cy="125" r="2"/>
    <circle cx="80" cy="200" r="2.5"/><circle cx="400" cy="190" r="2"/><circle cx="600" cy="200" r="3"/>
  </g>
  <!-- 雪山 -->
  <polygon points="0,300 100,180 200,240 300,150 400,220 500,160 600,210 700,170 800,200 800,300" fill="white" opacity="0.5"/>
  <polygon points="0,330 100,270 200,300 300,250 400,290 500,260 600,280 700,250 800,270 800,330" fill="#e8e8e8" opacity="0.6"/>
  <!-- 雪地 -->
  <rect x="0" y="320" width="800" height="80" fill="white" opacity="0.7"/>
  <!-- 雪人 -->
  <g transform="translate(400, 280)" opacity="0.6">
    <circle cx="0" cy="30" r="25" fill="white"/>
    <circle cx="0" cy="0" r="18" fill="white"/>
    <circle cx="-6" cy="-5" r="2" fill="#333"/>
    <circle cx="6" cy="-5" r="2" fill="#333"/>
    <polygon points="0,0 15,5 0,10" fill="#ff6b35"/>
  </g>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c1}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

def generate_spring_scene(desc, year, seed):
    """春天/花开"""
    c1, c2, c3 = PALETTES['spring']
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" width="100%" height="100%">
  <defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:{c1};stop-opacity:1"/><stop offset="50%" style="stop-color:{c2};stop-opacity:1"/><stop offset="100%" style="stop-color:{c3};stop-opacity:1"/></linearGradient></defs>
  <rect width="800" height="400" fill="url(#bg)"/>
  <!-- 樱花树 -->
  <g transform="translate(200, 150)">
    <rect x="-10" y="100" width="20" height="100" fill="#8B7355"/>
    <circle cx="0" cy="60" r="70" fill="#FFB7C5" opacity="0.6"/>
    <circle cx="-40" cy="90" r="50" fill="#FFB7C5" opacity="0.5"/>
    <circle cx="40" cy="80" r="55" fill="#FFB7C5" opacity="0.5"/>
    <circle cx="-20" cy="110" r="45" fill="#FFB7C5" opacity="0.4"/>
    <circle cx="30" cy="105" r="48" fill="#FFB7C5" opacity="0.4"/>
  </g>
  <!-- 飘落的花瓣 -->
  <g fill="#FFB7C5" opacity="0.6">
    <ellipse cx="300" cy="200" rx="5" ry="3" transform="rotate(30,300,200)"/>
    <ellipse cx="400" cy="180" rx="4" ry="2.5" transform="rotate(-20,400,180)"/>
    <ellipse cx="500" cy="220" rx="5" ry="3" transform="rotate(45,500,220)"/>
    <ellipse cx="350" cy="260" rx="4" ry="2.5" transform="rotate(-35,350,260)"/>
    <ellipse cx="600" cy="240" rx="5" ry="3" transform="rotate(15,600,240)"/>
    <ellipse cx="450" cy="300" rx="4" ry="2.5" transform="rotate(-45,450,300)"/>
  </g>
  <!-- 草地 -->
  <ellipse cx="400" cy="360" rx="450" ry="60" fill="#4a7c59" opacity="0.4"/>
  <g transform="translate(660, 40)"><rect width="90" height="32" rx="16" fill="white" opacity="0.85"/><text x="45" y="21" text-anchor="middle" font-size="14" font-weight="bold" fill="{c2}">{year}</text></g>
  <text x="400" y="365" text-anchor="middle" font-size="16" font-weight="bold" fill="white" opacity="0.95">{desc}</text>
  <text x="400" y="385" text-anchor="middle" font-size="11" fill="white" opacity="0.6">Dragon_SZ Blog</text>
</svg>'''

# ==================== 主函数 ====================

def generate_smart_svg(desc, year):
    """智能生成SVG，每个描述对应独特的场景"""
    # 精确匹配具体场景（优先匹配更具体的）
    if '喂奶' in desc:
        return generate_night_feeding(desc, year, 0)
    if any(w in desc for w in ['婴儿', '小手', '大手', '亲子', '新生儿']):
        return generate_baby_scene(desc, year, 0)
    if '医院走廊' in desc or ('走廊' in desc and '医院' in desc):
        return generate_hospital_corridor(desc, year, 0)
    if 'B超' in desc or '产房' in desc:
        return generate_ultrasound(desc, year, 0)
    if '防护服' in desc or '医护人员' in desc:
        return generate_protective_suit(desc, year, 0)
    if '电视' in desc or '在一起' in desc:
        return generate_tv_watching(desc, year, 0)
    if '答辩' in desc or '晋升' in desc or '办公室' in desc:
        return generate_promotion(desc, year, 0)
    if '一家三口' in desc or '合影' in desc and '家庭' in desc:
        return generate_family_photo(desc, year, 0)
    if '向日葵' in desc or '和好' in desc:
        return generate_sunflower(desc, year, 0)
    if '挚爱' in desc or '遇见' in desc and '爱情' in desc:
        return generate_love(desc, year, 0)
    if '爱情的力量' in desc:
        return generate_love(desc, year, 0)
    if '窗台' in desc or '窗' in desc:
        return generate_window(desc, year, 0)
    if '自习室' in desc or '备考' in desc:
        return generate_study_room(desc, year, 0)
    if '迷茫' in desc or '困惑' in desc or '沉思' in desc:
        return generate_confused(desc, year, 0)
    if '期待' in desc or '希望' in desc or '未来' in desc or '曙光' in desc:
        return generate_expectation(desc, year, 0)
    if '雪' in desc or '冬' in desc and '雪' in desc:
        return generate_snow_scene(desc, year, 0)
    if '春' in desc or '花' in desc or '花开' in desc:
        return generate_spring_scene(desc, year, 0)
    if '月' in desc and ('夜' in desc or '中秋' in desc):
        return generate_moon_night(desc, year, 0)
    if '黄昏' in desc or '夕阳' in desc or '晚霞' in desc or '日落' in desc:
        return generate_sunset_scene(desc, year, 0)
    if '海' in desc or '青岛' in desc or '海边' in desc:
        return generate_sea_scene(desc, year, 0)
    
    # 技术类
    if any(w in desc.lower() for w in ['mysql', 'redis', 'mongodb', 'mongo', 'oracle', '数据库', 'sql']):
        return generate_database_tech(desc, year, 0)
    if any(w in desc for w in ['架构', '拓扑', '分层', '设计']):
        return generate_architecture(desc, year, 0)
    if any(w in desc for w in ['流程', '步骤', '过程']):
        return generate_flowchart(desc, year, 0)
    if any(w in desc for w in ['代码', '编程', 'Filter', 'Servlet', 'Node.js', 'PHP', 'J2ME', 'Shell', '脚本']):
        return generate_code_tech(desc, year, 0)
    
    # 默认风景
    return generate_default_landscape(desc, year, 0)

def main():
    print("开始生成精美的差异化SVG图片...")
    
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
        
        svg_content = generate_smart_svg(description, year)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        generated += 1
        if generated % 50 == 0:
            print("已生成 {}/{} 张图片...".format(generated, len(needed_images)))
    
    print("完成！共生成了 {} 张SVG图片".format(generated))

if __name__ == '__main__':
    main()
