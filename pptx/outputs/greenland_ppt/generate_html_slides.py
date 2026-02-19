import os

# Configuration
output_dir = "slides"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Absolute path based on script location
base_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(base_dir, "images").replace("\\", "/")
if os.name == 'nt': 
    image_dir = image_dir.replace("\\", "/")

slides_data = [
    {
        "type": "title",
        "title": "Greenland: The Arctic Jewel",
        "text": "10 Great Things to See",
        "image": f"{image_dir}/title_slide.png",
        "color": "#003366"  # Dark Blue
    },
    {
        "type": "left-img",
        "title": "Ilulissat Icefjord",
        "text": "A UNESCO World Heritage site where massive icebergs break off from the Sermeq Kujalleq glacier. It is the most productive glacier in the Northern Hemisphere and a stunning sight to behold.",
        "image": f"{image_dir}/ilulissat.png"
    },
    {
        "type": "right-img",
        "title": "Nuuk: The Capital",
        "text": "Greenland's vibrant capital city offers a unique blend of Inuit tradition and modern life. Visit the National Museum to see the famous Qilakitsoq mummies and explore the local art scene.",
        "image": f"{image_dir}/nuuk.png"
    },
    {
        "type": "full-img",
        "title": "The Northern Lights",
        "text": "Witness the mesmerizing Aurora Borealis dancing across the dark Arctic sky. Greenland's clear nights and minimal light pollution make it one of the best places on Earth to experience this phenomenon.",
        "image": f"{image_dir}/northern_lights.png"
    },
    {
        "type": "left-img",
        "title": "Uunartoq Hot Springs",
        "text": "Relax in natural geothermal pools on an uninhabited island, while watching icebergs float by in the fjord nearby. These are the only heated outdoor spas in the country.",
        "image": f"{image_dir}/hot_springs.png"
    },
    {
        "type": "right-img",
        "title": "Whale Watching",
        "text": "The nutrient-rich waters of Disko Bay attract up to 15 different whale species during the summer months. Visitors can spot humpback, fin, and minke whales breaching near the ice.",
        "image": f"{image_dir}/whale_watching.png"
    },
    {
        "type": "left-img",
        "title": "Arctic Circle Trail",
        "text": "For the adventurous, this 160km trek stretches from the ice sheet to the sea. Experience the vast, silent beauty of the Arctic tundra and spot wildlife like reindeer and musk oxen.",
        "image": f"{image_dir}/hiking.png"
    },
    {
        "type": "full-img",
        "title": "Kayaking the Fjords",
        "text": "Paddle through silent fjords among towering blue icebergs. Kayaking offers a unique, intimate perspective of nature's grandeur from the water level.",
        "image": f"{image_dir}/kayaking.png"
    },
    {
        "type": "right-img",
        "title": "Norse History",
        "text": "Explore the well-preserved ruins of Hvalsey Church, the site of the last written record of the Norse in Greenland from 1408. A hauntingly beautiful glimpse into the past.",
        "image": f"{image_dir}/viking_ruins.png"
    },
    {
        "type": "left-img",
        "title": "Tasiilaq",
        "text": "The largest town in East Greenland, known for its dramatic mountain scenery, colorful wooden houses, and distinct culture. It serves as a gateway to many local adventures.",
        "image": f"{image_dir}/tasiilaq.png"
    },
    {
        "type": "full-img",
        "title": "The Ice Sheet",
        "text": "Kangerlussuaq provides easy access to the vast Greenland Ice Sheet. You can walk right onto the ice cap and look out over the endless, shimmering white horizon.",
        "image": f"{image_dir}/kangerlussuaq.png"
    }
]

def create_html(slide_idx, data):
    layout_type = data["type"]
    title = data["title"]
    text = data["text"]
    image_path = data["image"]
    
    # Based CSS
    # Reduced padding and font sizes to prevent overflow
    css = """
    body {
        width: 720pt; height: 405pt; 
        margin: 0; padding: 0; 
        font-family: 'Helvetica', 'Arial', sans-serif;
        overflow: hidden;
        background-color: #f0f4f8;
        display: flex;
        position: relative;
    }
    h1 { font-size: 22pt; color: #004d40; margin-bottom: 10pt; margin-top: 0; }
    p { font-size: 14pt; color: #263238; line-height: 1.35; margin: 0; }
    .content-box { padding: 20pt; box-sizing: border-box; display: flex; flex-direction: column; justify-content: center; width: 100%; height: 100%; }
    .bg-img { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; object-fit: cover; }
    .content-layer { position: relative; z-index: 2; width: 100%; height: 100%; display: flex; }
    """

    content_html = ""

    if layout_type == "title":
        content_html = f"""
        <img src="{image_path}" class="bg-img">
        <div class="content-layer" style="align_items: center; justify-content: center;">
            <div style="background: rgba(255, 255, 255, 0.9); padding: 30pt; border-radius: 10pt; text-align: center; max-width: 80%;">
                <h1 style="font-size: 42pt; margin: 0; color: #003366;" data-animate-type="FADE_IN" data-animate-duration="1000">{title}</h1>
                <p style="font-size: 22pt; margin-top: 15pt; color: #546e7a;" data-animate-type="FADE_IN" data-animate-delay="500" data-animate-duration="1000">{text}</p>
            </div>
        </div>
        """
    elif layout_type == "left-img":
        content_html = f"""
        <div class="content-layer">
            <div style="flex: 1; height: 100%;">
                <img src="{image_path}" style="width: 100%; height: 100%; object-fit: cover;" data-animate-type="FLY_FROM_LEFT" data-animate-duration="1000">
            </div>
            <div style="flex: 1; height: 100%;">
                <div class="content-box">
                    <h1 data-animate-type="FADE_IN" data-animate-delay="500">{title}</h1>
                    <p data-animate-type="FADE_IN" data-animate-delay="800">{text}</p>
                </div>
            </div>
        </div>
        """
    elif layout_type == "right-img":
        content_html = f"""
        <div class="content-layer">
            <div style="flex: 1; height: 100%;">
                <div class="content-box">
                    <h1 data-animate-type="FADE_IN" data-animate-delay="500">{title}</h1>
                    <p data-animate-type="FADE_IN" data-animate-delay="800">{text}</p>
                </div>
            </div>
            <div style="flex: 1; height: 100%;">
                <img src="{image_path}" style="width: 100%; height: 100%; object-fit: cover;" data-animate-type="FLY_FROM_RIGHT" data-animate-duration="1000">
            </div>
        </div>
        """
    elif layout_type == "full-img":
        content_html = f"""
        <img src="{image_path}" class="bg-img" data-animate-type="FADE_IN" data-animate-duration="2000">
        <div class="content-layer" style="align_items: flex-end;">
            <div style="background: rgba(0, 0, 0, 0.7); width: 100%; padding: 25pt; color: white;" data-animate-type="FLY_FROM_BOTTOM" data-animate-duration="1000">
                <h1 style="color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">{title}</h1>
                <p style="color: #eceff1; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);">{text}</p>
            </div>
        </div>
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>{css}</style>
    </head>
    <body>
        {content_html}
    </body>
    </html>
    """
    
    with open(f"{output_dir}/slide{slide_idx}.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created slide{slide_idx}.html")

for i, data in enumerate(slides_data):
    create_html(i+1, data)
