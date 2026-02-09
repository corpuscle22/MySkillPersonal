from PIL import Image, ImageDraw, ImageFont

def create_concept_image(filename):
    # Create a white canvas
    img = Image.new('RGB', (800, 600), color='white')
    d = ImageDraw.Draw(img)
    
    # Draw Bed Sheet context (light gray area)
    d.rectangle([50, 500, 750, 600], fill='#F0F0F0')
    
    # Draw the Pad (Teal Pill Shape)
    pad_color = '#008080'  # Teal
    # Main body
    d.rounded_rectangle([200, 200, 600, 400], radius=50, fill=pad_color, outline='black', width=2)
    # Nodes (lighter teal circles in center)
    d.ellipse([350, 280, 400, 330], fill='#40E0D0', outline='black')
    d.ellipse([420, 280, 470, 330], fill='#40E0D0', outline='black')
    
    # Draw the Remote (White Pebble)
    d.rounded_rectangle([650, 300, 720, 450], radius=20, fill='#FFFFFF', outline='black', width=2)
    # Buttons
    d.ellipse([670, 320, 700, 350], fill='#DDDDDD', outline='black') # Up
    d.ellipse([670, 360, 700, 390], fill='#DDDDDD', outline='black') # Down
    d.ellipse([670, 400, 700, 430], fill='#FFCCCC', outline='black') # Power/Massage
    
    # Text Labels
    try:
        # standard font
        font = ImageFont.load_default()
    except:
        font = None
        
    d.text((380, 180), "Lumbar Pad (Top View)", fill='black', font=font)
    d.text((660, 280), "Remote", fill='black', font=font)
    
    img.save(filename)
    print(f"Saved {filename}")

def create_mechanism_diagram(filename):
    img = Image.new('RGB', (800, 600), color='white')
    d = ImageDraw.Draw(img)
    
    # Base Plate (Grey)
    d.rectangle([200, 100, 600, 500], fill='#DDDDDD', outline='black', width=3)
    
    # Linear Track (Lead Screw - Vertical Line)
    d.line([400, 120, 400, 480], fill='black', width=5)
    # Track Threads representations
    for y in range(120, 480, 20):
        d.line([390, y, 410, y], fill='black', width=1)
        
    # Carriage (Blue Box on Track)
    d.rectangle([300, 250, 500, 350], fill='#AAAAFF', outline='black', width=2)
    
    # Massage Motor (Circle on Carriage)
    d.ellipse([380, 280, 420, 320], fill='#555555', outline='black')
    
    # Massage Nodes (attached to motor, eccentric)
    d.ellipse([350, 260, 390, 300], fill='#008080', outline='black') # Left Node
    d.ellipse([410, 260, 450, 300], fill='#008080', outline='black') # Right Node
    
    # Track Motor (at bottom)
    d.rectangle([380, 480, 420, 520], fill='#333333', outline='black')
    
    # Labels
    d.text((430, 130), "Lead Screw (Track)", fill='black')
    d.text((510, 300), "Carriage", fill='black')
    d.text((220, 270), "Massage Nodes", fill='black')
    d.text((430, 500), "Track Motor", fill='black')
    
    img.save(filename)
    print(f"Saved {filename}")

def create_system_diagram(filename):
    img = Image.new('RGB', (800, 400), color='white')
    d = ImageDraw.Draw(img)
    
    # Define boxes
    boxes = {
        'Remote': (50, 150, 150, 250),
        'Receiver': (200, 150, 300, 250),
        'MCU': (350, 150, 450, 250),
        'Driver1': (500, 50, 600, 150),
        'Driver2': (500, 250, 600, 350),
        'Motor1': (650, 50, 750, 150),
        'Motor2': (650, 250, 750, 350)
    }
    
    for name, coords in boxes.items():
        d.rectangle(coords, fill='#E0E0E0', outline='black', width=2)
        d.text((coords[0]+10, coords[1]+40), name, fill='black')
        
    # Connections (Arrows)
    # Remote -> Receiver
    d.line([150, 200, 200, 200], fill='black', width=2)
    # Receiver -> MCU
    d.line([300, 200, 350, 200], fill='black', width=2)
    # MCU -> Driver 1
    d.line([450, 200, 500, 100], fill='black', width=2)
    # MCU -> Driver 2
    d.line([450, 200, 500, 300], fill='black', width=2)
    # Driver 1 -> Motor 1
    d.line([600, 100, 650, 100], fill='black', width=2)
    # Driver 2 -> Motor 2
    d.line([600, 300, 650, 300], fill='black', width=2)
    
    img.save(filename)
    print(f"Saved {filename}")

if __name__ == "__main__":
    create_concept_image("vertebra_concept.png")
    create_mechanism_diagram("vertebra_mechanism.png")
    create_system_diagram("vertebra_system.png")
