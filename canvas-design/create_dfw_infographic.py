"""
DFW Demographics Infographic - Cartographic Abstraction
A museum-quality visualization of Dallas-Fort Worth population data
SECOND PASS: Refined for pristine museum quality
"""

import math
from PIL import Image, ImageDraw, ImageFont
import os

# Canvas dimensions - portrait orientation for infographic
WIDTH = 1800
HEIGHT = 2400

# Color palette - refined for visual cohesion and depth
COLORS = {
    'background': '#0A1628',        # Deeper navy for contrast
    'primary_text': '#E8E9E4',      # Softer warm white
    'accent_gold': '#D4A574',       # Burnt sienna - prairie warmth  
    'metro_blue': '#4A6D8C',        # Richer steel blue
    'growth_green': '#5A9A8A',      # Brighter sage green
    'highlight': '#8A9DB8',         # Lighter slate blue
    'population_coral': '#C87A6D',  # Warmer terracotta
    'ethnic_teal': '#5E9B8E',       # Brighter muted teal
    'ethnic_amber': '#D4B86A',      # Richer golden amber
    'ethnic_rust': '#9B7068',       # Warmer dusty rust
    'ethnic_slate': '#7A8C9C',      # Lighter cool slate
    'subtle_line': '#1E3248',       # More visible grid lines
    'decorative': '#2A4058',        # Decorative element color
}

def create_canvas():
    """Create the base canvas with background"""
    img = Image.new('RGB', (WIDTH, HEIGHT), COLORS['background'])
    return img, ImageDraw.Draw(img)

def load_fonts():
    """Load fonts from canvas-fonts directory"""
    font_dir = os.path.join(os.path.dirname(__file__), 'canvas-fonts')
    
    fonts = {
        'title': ImageFont.truetype(os.path.join(font_dir, 'BigShoulders-Bold.ttf'), 120),
        'subtitle': ImageFont.truetype(os.path.join(font_dir, 'Jura-Light.ttf'), 32),
        'stat_large': ImageFont.truetype(os.path.join(font_dir, 'BigShoulders-Bold.ttf'), 96),
        'stat_medium': ImageFont.truetype(os.path.join(font_dir, 'BigShoulders-Regular.ttf'), 64),
        'stat_small': ImageFont.truetype(os.path.join(font_dir, 'Outfit-Bold.ttf'), 42),
        'label': ImageFont.truetype(os.path.join(font_dir, 'Jura-Light.ttf'), 22),
        'label_small': ImageFont.truetype(os.path.join(font_dir, 'Jura-Light.ttf'), 18),
        'section': ImageFont.truetype(os.path.join(font_dir, 'InstrumentSans-Regular.ttf'), 28),
        'county': ImageFont.truetype(os.path.join(font_dir, 'Outfit-Regular.ttf'), 28),
        'county_num': ImageFont.truetype(os.path.join(font_dir, 'BigShoulders-Bold.ttf'), 48),
    }
    return fonts

def draw_decorative_elements(draw):
    """Draw refined geometric decorative elements for museum-quality finish"""
    # Top left corner geometric accent - refined spacing
    for i in range(5):
        offset = i * 6
        draw.line([(50 + offset, 50), (50 + offset, 130)], fill=COLORS['accent_gold'], width=2)
    
    # Top right corner accent
    for i in range(5):
        offset = i * 6
        draw.line([(WIDTH - 50 - offset, 50), (WIDTH - 50 - offset, 130)], 
                  fill=COLORS['decorative'], width=2)
    
    # Bottom left corner accents
    for i in range(5):
        offset = i * 6
        draw.line([(50 + offset, HEIGHT - 130), (50 + offset, HEIGHT - 50)], 
                  fill=COLORS['decorative'], width=2)
    
    # Bottom right corner accents
    for i in range(5):
        offset = i * 6
        draw.line([(WIDTH - 50 - offset, HEIGHT - 130), (WIDTH - 50 - offset, HEIGHT - 50)], 
                  fill=COLORS['metro_blue'], width=2)
    
    # Subtle horizontal rule lines - refined positions
    draw.line([(120, 270), (WIDTH - 120, 270)], fill=COLORS['subtle_line'], width=1)
    draw.line([(120, HEIGHT - 140), (WIDTH - 120, HEIGHT - 140)], fill=COLORS['subtle_line'], width=1)

def draw_header(draw, fonts):
    """Draw the header section with title and population stat"""
    # Main title
    title_text = "DALLAS–FORT WORTH"
    bbox = draw.textbbox((0, 0), title_text, font=fonts['title'])
    title_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - title_width) // 2, 80), title_text, font=fonts['title'], fill=COLORS['primary_text'])
    
    # Subtitle
    subtitle_text = "METROPLEX POPULATION DEMOGRAPHICS  ·  2024"
    bbox = draw.textbbox((0, 0), subtitle_text, font=fonts['subtitle'])
    subtitle_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - subtitle_width) // 2, 200), subtitle_text, font=fonts['subtitle'], fill=COLORS['highlight'])

def draw_main_population(draw, fonts):
    """Draw the central population statistic with visual prominence"""
    center_y = 380
    
    # Main population number
    pop_text = "8,344,032"
    bbox = draw.textbbox((0, 0), pop_text, font=fonts['stat_large'])
    pop_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - pop_width) // 2, center_y), pop_text, font=fonts['stat_large'], fill=COLORS['accent_gold'])
    
    # Population label
    pop_label = "TOTAL METRO POPULATION"
    bbox = draw.textbbox((0, 0), pop_label, font=fonts['label'])
    label_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - label_width) // 2, center_y + 100), pop_label, font=fonts['label'], fill=COLORS['highlight'])
    
    # Growth indicator
    growth_text = "+2.2%"
    bbox = draw.textbbox((0, 0), growth_text, font=fonts['stat_small'])
    growth_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - growth_width) // 2, center_y + 135), growth_text, font=fonts['stat_small'], fill=COLORS['growth_green'])
    
    growth_label = "ANNUAL GROWTH"
    bbox = draw.textbbox((0, 0), growth_label, font=fonts['label_small'])
    label_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - label_width) // 2, center_y + 180), growth_label, font=fonts['label_small'], fill=COLORS['subtle_line'])

def draw_ethnic_composition(draw, fonts):
    """Draw the ethnic composition visualization as proportional bars"""
    section_y = 650
    bar_height = 65
    bar_width = 1200
    bar_x = (WIDTH - bar_width) // 2
    
    # Section label
    section_label = "ETHNIC COMPOSITION"
    bbox = draw.textbbox((0, 0), section_label, font=fonts['section'])
    label_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - label_width) // 2, section_y), section_label, font=fonts['section'], fill=COLORS['highlight'])
    
    # Demographic data (percentages)
    demographics = [
        ('Non-Hispanic White', 42, COLORS['highlight']),
        ('Hispanic/Latino', 29, COLORS['accent_gold']),
        ('Black/African American', 16, COLORS['ethnic_rust']),
        ('Asian', 8, COLORS['ethnic_teal']),
        ('Other/Multiracial', 5, COLORS['metro_blue']),
    ]
    
    # Draw proportional bar
    bar_y = section_y + 50
    current_x = bar_x
    
    for name, percent, color in demographics:
        segment_width = int((percent / 100) * bar_width)
        draw.rectangle([current_x, bar_y, current_x + segment_width, bar_y + bar_height], fill=color)
        current_x += segment_width
    
    # Draw labels below bar
    label_y = bar_y + bar_height + 20
    current_x = bar_x
    
    for name, percent, color in demographics:
        segment_width = int((percent / 100) * bar_width)
        
        # Percentage label
        pct_text = f"{percent}%"
        draw.text((current_x + 10, label_y), pct_text, font=fonts['stat_small'], fill=color)
        
        # Name label (abbreviated for space)
        if len(name) > 15:
            short_name = name.split('/')[0] if '/' in name else name[:12]
        else:
            short_name = name
        draw.text((current_x + 10, label_y + 45), short_name, font=fonts['label_small'], fill=COLORS['primary_text'])
        
        current_x += segment_width

def draw_county_data(draw, fonts):
    """Draw county-level population data as geometric blocks"""
    section_y = 920
    
    # Section label
    section_label = "MAJOR COUNTIES"
    bbox = draw.textbbox((0, 0), section_label, font=fonts['section'])
    label_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - label_width) // 2, section_y), section_label, font=fonts['section'], fill=COLORS['highlight'])
    
    # County data
    counties = [
        ('DALLAS', '2.66M', '+3.1%'),
        ('TARRANT', '2.23M', '+1.5%'),
        ('COLLIN', '1.25M', '+3.9%'),
        ('DENTON', '1.02M', '+3.4%'),
    ]
    
    block_width = 380
    block_height = 170
    spacing = 40
    total_width = (block_width * 4) + (spacing * 3)
    start_x = (WIDTH - total_width) // 2
    block_y = section_y + 50
    
    for i, (name, population, growth) in enumerate(counties):
        x = start_x + i * (block_width + spacing)
        
        # Block background
        draw.rectangle([x, block_y, x + block_width, block_y + block_height], 
                       fill=COLORS['subtle_line'], outline=COLORS['metro_blue'], width=2)
        
        # County name
        bbox = draw.textbbox((0, 0), name, font=fonts['county'])
        name_width = bbox[2] - bbox[0]
        draw.text((x + (block_width - name_width) // 2, block_y + 15), 
                  name, font=fonts['county'], fill=COLORS['highlight'])
        
        # Population
        bbox = draw.textbbox((0, 0), population, font=fonts['county_num'])
        pop_width = bbox[2] - bbox[0]
        draw.text((x + (block_width - pop_width) // 2, block_y + 55), 
                  population, font=fonts['county_num'], fill=COLORS['accent_gold'])
        
        # Growth rate
        bbox = draw.textbbox((0, 0), growth, font=fonts['label'])
        growth_width = bbox[2] - bbox[0]
        draw.text((x + (block_width - growth_width) // 2, block_y + 115), 
                  growth, font=fonts['label'], fill=COLORS['growth_green'])

def draw_growth_visualization(draw, fonts):
    """Draw migration and growth data visualization"""
    section_y = 1250
    
    # Section label
    section_label = "POPULATION GROWTH DRIVERS"
    bbox = draw.textbbox((0, 0), section_label, font=fonts['section'])
    label_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - label_width) // 2, section_y), section_label, font=fonts['section'], fill=COLORS['highlight'])
    
    # Growth data as concentric elements
    center_x = WIDTH // 2
    center_y = section_y + 200
    
    # Outer ring - Total growth
    draw.ellipse([center_x - 160, center_y - 160, center_x + 160, center_y + 160], 
                 outline=COLORS['accent_gold'], width=4)
    
    # Middle ring - International migration
    draw.ellipse([center_x - 120, center_y - 120, center_x + 120, center_y + 120], 
                 outline=COLORS['ethnic_teal'], width=4)
    
    # Inner ring - Domestic migration  
    draw.ellipse([center_x - 80, center_y - 80, center_x + 80, center_y + 80], 
                 outline=COLORS['metro_blue'], width=4)
    
    # Center stat
    center_stat = "178K"
    bbox = draw.textbbox((0, 0), center_stat, font=fonts['stat_medium'])
    stat_width = bbox[2] - bbox[0]
    draw.text((center_x - stat_width // 2, center_y - 35), 
              center_stat, font=fonts['stat_medium'], fill=COLORS['primary_text'])
    
    center_label = "NEW RESIDENTS"
    bbox = draw.textbbox((0, 0), center_label, font=fonts['label_small'])
    label_width = bbox[2] - bbox[0]
    draw.text((center_x - label_width // 2, center_y + 35), 
              center_label, font=fonts['label_small'], fill=COLORS['highlight'])
    
    # Side labels for migration types
    # International
    draw.text((center_x + 180, center_y - 100), "58%", font=fonts['stat_small'], fill=COLORS['ethnic_teal'])
    draw.text((center_x + 180, center_y - 60), "INTERNATIONAL", font=fonts['label_small'], fill=COLORS['primary_text'])
    draw.text((center_x + 180, center_y - 40), "MIGRATION", font=fonts['label_small'], fill=COLORS['primary_text'])
    
    # Domestic
    draw.text((center_x - 350, center_y - 100), "14%", font=fonts['stat_small'], fill=COLORS['metro_blue'])
    draw.text((center_x - 350, center_y - 60), "DOMESTIC", font=fonts['label_small'], fill=COLORS['primary_text'])
    draw.text((center_x - 350, center_y - 40), "MIGRATION", font=fonts['label_small'], fill=COLORS['primary_text'])

def draw_ranking_section(draw, fonts):
    """Draw national rankings and projections"""
    section_y = 1680
    
    # Divider line
    draw.line([(200, section_y - 30), (WIDTH - 200, section_y - 30)], fill=COLORS['subtle_line'], width=1)
    
    # Rankings in horizontal layout
    rankings = [
        ('4TH', 'LARGEST METRO', 'IN THE NATION'),
        ('3RD', 'FASTEST GROWING', 'MAJOR METRO'),
        ('2ND', 'PROJECTED BY', '2060'),
    ]
    
    spacing = 450
    start_x = (WIDTH - (spacing * 2)) // 2
    
    for i, (number, line1, line2) in enumerate(rankings):
        x = start_x + i * spacing
        
        # Large number
        bbox = draw.textbbox((0, 0), number, font=fonts['stat_medium'])
        num_width = bbox[2] - bbox[0]
        draw.text((x - num_width // 2, section_y), number, font=fonts['stat_medium'], fill=COLORS['accent_gold'])
        
        # Description
        bbox = draw.textbbox((0, 0), line1, font=fonts['label'])
        line1_width = bbox[2] - bbox[0]
        draw.text((x - line1_width // 2, section_y + 75), line1, font=fonts['label'], fill=COLORS['primary_text'])
        
        bbox = draw.textbbox((0, 0), line2, font=fonts['label_small'])
        line2_width = bbox[2] - bbox[0]
        draw.text((x - line2_width // 2, section_y + 100), line2, font=fonts['label_small'], fill=COLORS['highlight'])

def draw_city_highlight(draw, fonts):
    """Draw Fort Worth milestone highlight"""
    section_y = 1900
    
    # Decorative bracket
    draw.rectangle([300, section_y, WIDTH - 300, section_y + 180], outline=COLORS['metro_blue'], width=2)
    
    # Fort Worth milestone
    ft_worth = "FORT WORTH"
    bbox = draw.textbbox((0, 0), ft_worth, font=fonts['section'])
    text_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - text_width) // 2, section_y + 20), ft_worth, font=fonts['section'], fill=COLORS['highlight'])
    
    milestone = "1,008,106"
    bbox = draw.textbbox((0, 0), milestone, font=fonts['stat_medium'])
    text_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - text_width) // 2, section_y + 60), milestone, font=fonts['stat_medium'], fill=COLORS['population_coral'])
    
    label = "SURPASSES 1 MILLION  ·  11TH LARGEST U.S. CITY  ·  FASTEST GROWING TOP 30"
    bbox = draw.textbbox((0, 0), label, font=fonts['label_small'])
    text_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - text_width) // 2, section_y + 135), label, font=fonts['label_small'], fill=COLORS['primary_text'])

def draw_projection(draw, fonts):
    """Draw future projection"""
    section_y = 2150
    
    # Projection stat
    proj_label = "2060 PROJECTION"
    bbox = draw.textbbox((0, 0), proj_label, font=fonts['label'])
    label_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - label_width) // 2, section_y), proj_label, font=fonts['label'], fill=COLORS['highlight'])
    
    proj_stat = "12.4 MILLION"
    bbox = draw.textbbox((0, 0), proj_stat, font=fonts['stat_medium'])
    stat_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - stat_width) // 2, section_y + 35), proj_stat, font=fonts['stat_medium'], fill=COLORS['growth_green'])

def draw_footer(draw, fonts):
    """Draw minimal footer with data source"""
    footer_text = "DATA: U.S. CENSUS BUREAU  ·  DALLAS FEDERAL RESERVE  ·  2024"
    bbox = draw.textbbox((0, 0), footer_text, font=fonts['label_small'])
    text_width = bbox[2] - bbox[0]
    draw.text(((WIDTH - text_width) // 2, HEIGHT - 80), footer_text, font=fonts['label_small'], fill=COLORS['subtle_line'])

def main():
    """Generate the complete infographic"""
    print("Creating DFW Demographics Infographic...")
    
    # Create canvas
    img, draw = create_canvas()
    
    # Load fonts
    fonts = load_fonts()
    
    # Draw all sections
    draw_decorative_elements(draw)
    draw_header(draw, fonts)
    draw_main_population(draw, fonts)
    draw_ethnic_composition(draw, fonts)
    draw_county_data(draw, fonts)
    draw_growth_visualization(draw, fonts)
    draw_ranking_section(draw, fonts)
    draw_city_highlight(draw, fonts)
    draw_projection(draw, fonts)
    draw_footer(draw, fonts)
    
    # Save the infographic
    output_path = os.path.join(os.path.dirname(__file__), 'dfw-demographics-infographic.png')
    img.save(output_path, 'PNG', quality=95)
    print(f"Infographic saved to: {output_path}")
    
    return output_path

if __name__ == '__main__':
    main()
