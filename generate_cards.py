import math
from PIL import Image, ImageDraw, ImageFont

W, H = 860, 1864

# Try loading Windows Segoe UI and Consolas fonts
try:
    font_bold_xl = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 68)
    font_bold_lg = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 46)
    font_bold_md = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 34)
    font_bold_sm = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
    font_reg_lg = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 38)
    font_reg_md = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 30)
    font_reg_sm = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 24)
    font_code = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 29)
    font_code_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 29)
except Exception:
    font_bold_xl = ImageFont.load_default()
    font_bold_lg = ImageFont.load_default()
    font_bold_md = ImageFont.load_default()
    font_bold_sm = ImageFont.load_default()
    font_reg_lg = ImageFont.load_default()
    font_reg_md = ImageFont.load_default()
    font_reg_sm = ImageFont.load_default()
    font_code = ImageFont.load_default()
    font_code_bold = ImageFont.load_default()

def draw_rounded_card_frame(draw, bg_color):
    # Full card background with rounded inner card frame
    draw.rectangle([0, 0, W, H], fill=bg_color)
    # Subtle inner border
    draw.rounded_rectangle([20, 20, W-20, H-20], radius=44, outline=(0, 0, 0, 15) if bg_color[0]>100 else (255, 255, 255, 20), width=3)

# ----------------- CARD 1: Building Better Solutions -----------------
def create_card_1():
    img = Image.new("RGB", (W, H), (246, 248, 250))
    d = ImageDraw.Draw(img)
    draw_rounded_card_frame(d, (246, 248, 250))
    
    # Header
    d.text((70, 70), "Ritesh Parmar", fill=(17, 24, 39), font=font_bold_lg)
    # Hamburger icon
    d.line([W - 130, 85, W - 80, 85], fill=(17, 24, 39), width=5)
    d.line([W - 130, 100, W - 95, 100], fill=(17, 24, 39), width=5)
    
    # Hero Title
    d.text((70, 240), "Building", fill=(15, 23, 42), font=font_bold_xl)
    d.text((70, 325), "Better", fill=(15, 23, 42), font=font_bold_xl)
    d.text((70, 410), "Solutions", fill=(15, 23, 42), font=font_bold_xl)
    
    # Subtitle & Tagline
    d.text((70, 525), "DOT NET Backend Developer · Techgrains", fill=(30, 41, 59), font=font_bold_md)
    d.text((70, 580), "Clean Code · Reliable APIs · Scalable Systems", fill=(100, 116, 139), font=font_reg_sm)
    
    # Mountain illustration card mockup in middle
    d.rounded_rectangle([70, 660, W - 70, 1140], radius=32, fill=(235, 239, 244))
    # Draw stylized mountain silhouette
    d.polygon([(70, 1140), (280, 820), (450, 1010), (620, 780), (W - 70, 1140)], fill=(203, 213, 225))
    d.polygon([(70, 1140), (280, 820), (360, 930), (220, 1140)], fill=(148, 163, 184))
    d.polygon([(450, 1010), (620, 780), (710, 910), (580, 1140)], fill=(148, 163, 184))
    # Sun circle
    d.ellipse([W - 200, 720, W - 140, 780], fill=(226, 232, 240))
    
    # CTA Button
    d.rounded_rectangle([70, 1220, 430, 1315], radius=48, fill=(15, 23, 42))
    d.text((115, 1245), "View My Projects  →", fill=(255, 255, 255), font=font_bold_sm)
    
    # Divider
    d.line([70, 1390, W - 70, 1390], fill=(226, 232, 240), width=2)
    
    # Stats Row
    stat_x = [70, 340, 610]
    stats = [
        ("3+", "Years Experience"),
        ("5+", "Projects"),
        ("6+", "Modules")
    ]
    for i, (num, label) in enumerate(stats):
        x = stat_x[i]
        d.text((x, 1440), num, fill=(15, 23, 42), font=font_bold_xl)
        d.text((x, 1530), label, fill=(100, 116, 139), font=font_reg_sm)
        
    # Bottom scroll arrow
    d.ellipse([(W//2 - 32), 1690, (W//2 + 32), 1754], fill=(241, 245, 249))
    d.text(((W//2 - 12), 1700), "↓", fill=(100, 116, 139), font=font_bold_md)
    return img

# ----------------- CARD 2: Program.cs -----------------
def create_card_2():
    img = Image.new("RGB", (W, H), (24, 28, 36))
    d = ImageDraw.Draw(img)
    draw_rounded_card_frame(d, (24, 28, 36))
    
    # Window Header
    d.ellipse([70, 80, 94, 104], fill=(239, 68, 68))
    d.ellipse([110, 80, 134, 104], fill=(245, 158, 11))
    d.ellipse([150, 80, 174, 104], fill=(16, 185, 129))
    
    # Tab title
    d.text((210, 75), "Program.cs", fill=(148, 163, 184), font=font_code)
    d.line([50, 130, W - 50, 130], fill=(45, 55, 72), width=2)
    
    # Code snippet lines
    code_lines = [
        ("var ", (86, 156, 214), "builder = ", (212, 212, 212), "WebApplication.", (78, 201, 176), "CreateBuilder();", (220, 220, 170)),
        ("", (0,0,0)),
        ("builder.Services.", (212, 212, 212), "AddControllers", (220, 220, 170), "();", (212, 212, 212)),
        ("builder.Services.", (212, 212, 212), "AddEndpointsApiExplorer", (220, 220, 170), "();", (212, 212, 212)),
        ("builder.Services.", (212, 212, 212), "AddSwaggerGen", (220, 220, 170), "();", (212, 212, 212)),
        ("", (0,0,0)),
        ("var ", (86, 156, 214), "app = builder.", (212, 212, 212), "Build", (220, 220, 170), "();", (212, 212, 212)),
        ("", (0,0,0)),
        ("if ", (197, 134, 192), "(app.Environment.", (212, 212, 212), "IsDevelopment", (220, 220, 170), "())", (212, 212, 212)),
        ("{", (212, 212, 212)),
        ("    app.", (212, 212, 212), "UseSwagger", (220, 220, 170), "();", (212, 212, 212)),
        ("    app.", (212, 212, 212), "UseSwaggerUI", (220, 220, 170), "();", (212, 212, 212)),
        ("}", (212, 212, 212)),
        ("", (0,0,0)),
        ("app.", (212, 212, 212), "UseHttpsRedirection", (220, 220, 170), "();", (212, 212, 212)),
        ("app.", (212, 212, 212), "UseAuthorization", (220, 220, 170), "();", (212, 212, 212)),
        ("app.", (212, 212, 212), "MapControllers", (220, 220, 170), "();", (212, 212, 212)),
        ("", (0,0,0)),
        ("app.", (212, 212, 212), "Run", (220, 220, 170), "();", (212, 212, 212)),
    ]
    
    y = 200
    for line in code_lines:
        x = 70
        for i in range(0, len(line), 2):
            text = line[i]
            color = line[i+1]
            d.text((x, y), text, fill=color, font=font_code)
            bbox = font_code.getbbox(text)
            x += (bbox[2] - bbox[0])
        y += 54
        
    # Bottom tech badge
    d.rounded_rectangle([70, H - 180, W - 70, H - 90], radius=24, fill=(35, 42, 54))
    d.text((110, H - 150), "C#", fill=(148, 163, 184), font=font_bold_sm)
    d.text((160, H - 150), "|", fill=(71, 85, 105), font=font_reg_sm)
    d.text((185, H - 150), "ASPDOT NET Core Web API", fill=(56, 189, 248), font=font_bold_sm)
    d.text((W - 190, H - 150), "DOT NET 8 / 9", fill=(148, 163, 184), font=font_reg_sm)
    return img

# ----------------- CARD 3: API Endpoints & Tech Stack -----------------
def create_card_3():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_rounded_card_frame(d, (255, 255, 255))
    
    # Title
    d.text((70, 80), "API Endpoints", fill=(15, 23, 42), font=font_bold_lg)
    
    endpoints = [
        ("GET", (14, 165, 233), (224, 242, 254), "/api/projects"),
        ("POST", (16, 185, 129), (209, 250, 229), "/api/projects"),
        ("PUT", (245, 158, 11), (254, 243, 199), "/api/projects/{id}"),
        ("DELETE", (239, 68, 68), (254, 226, 226), "/api/projects/{id}")
    ]
    
    y = 190
    for method, col_text, col_bg, route in endpoints:
        # Card item
        d.rounded_rectangle([70, y, W - 70, y + 100], radius=24, fill=(248, 250, 252), outline=(226, 232, 240), width=2)
        # Badge
        d.rounded_rectangle([95, y + 20, 230, y + 80], radius=16, fill=col_bg)
        d.text((115, y + 32), method, fill=col_text, font=font_bold_sm)
        # Route
        d.text((255, y + 32), route, fill=(30, 41, 59), font=font_code_bold)
        y += 130
        
    # Divider
    d.line([70, 760, W - 70, 760], fill=(226, 232, 240), width=2)
    
    # Tech Stack Section
    d.text((70, 810), "Tech Stack", fill=(15, 23, 42), font=font_bold_lg)
    
    techs = [
        ("DOT NET Core", (81, 43, 212), (243, 237, 254)),
        ("C#", (35, 145, 47), (237, 248, 238)),
        ("MySQL", (0, 117, 143), (233, 247, 250)),
        ("React", (97, 218, 251), (236, 250, 254)),
        ("TypeScript", (49, 120, 198), (235, 243, 252)),
        ("Swagger", (133, 234, 41), (242, 252, 235))
    ]
    
    grid_positions = [
        (70, 910), (330, 910), (590, 910),
        (70, 1100), (330, 1100), (590, 1100)
    ]
    
    for i, (name, icon_col, bg_col) in enumerate(techs):
        gx, gy = grid_positions[i]
        d.rounded_rectangle([gx, gy, gx + 200, gy + 150], radius=24, fill=bg_col, outline=(226, 232, 240), width=2)
        # Colored circle icon
        d.ellipse([gx + 75, gy + 30, gx + 125, gy + 80], fill=icon_col)
        # Text
        d.text((gx + 25, gy + 95), name, fill=(30, 41, 59), font=font_bold_sm)
        
    # Additional Architecture box
    d.rounded_rectangle([70, 1340, W - 70, 1720], radius=28, fill=(248, 250, 252), outline=(226, 232, 240), width=2)
    d.text((105, 1375), "System Capabilities", fill=(15, 23, 42), font=font_bold_md)
    caps = [
        "✓  Clean Architecture & Repository Pattern",
        "✓  JWT Authentication & Role Security",
        "✓  Entity Framework Core & Dapper ORM",
        "✓  High-Throughput RESTful APIs",
        "✓  Automated CI/CD & Docker Ready"
    ]
    cy = 1445
    for c in caps:
        d.text((105, cy), c, fill=(51, 65, 85), font=font_reg_sm)
        cy += 50
        
    return img

# ----------------- CARD 4: Project Analytics -----------------
def create_card_4():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_rounded_card_frame(d, (255, 255, 255))
    
    # Title & Dropdown
    d.text((70, 80), "Project Analytics", fill=(15, 23, 42), font=font_bold_lg)
    d.rounded_rectangle([W - 250, 80, W - 70, 135], radius=20, fill=(241, 245, 249))
    d.text((W - 225, 93), "This Week  ▾", fill=(71, 85, 105), font=font_reg_sm)
    
    # Top stats
    d.text((70, 200), "Total Requests", fill=(100, 116, 139), font=font_reg_sm)
    d.text((70, 245), "12,540", fill=(15, 23, 42), font=font_bold_xl)
    d.text((275, 260), "↑ 32%", fill=(16, 185, 129), font=font_bold_sm)
    
    d.text((480, 200), "Success Rate", fill=(100, 116, 139), font=font_reg_sm)
    d.text((480, 245), "99.8%", fill=(15, 23, 42), font=font_bold_xl)
    d.text((670, 260), "↑ 0.4%", fill=(16, 185, 129), font=font_bold_sm)
    
    # Chart area
    chart_y_top = 400
    chart_y_bottom = 680
    chart_pts = [
        (100, 620), (200, 560), (300, 590), (400, 480),
        (500, 530), (600, 440), (740, 470)
    ]
    # Draw green gradient polygon below line
    chart_poly = [(100, chart_y_bottom)] + chart_pts + [(740, chart_y_bottom)]
    d.polygon(chart_poly, fill=(236, 253, 245))
    # Line
    for i in range(len(chart_pts) - 1):
        d.line([chart_pts[i], chart_pts[i+1]], fill=(16, 185, 129), width=5)
    for pt in chart_pts:
        d.ellipse([pt[0]-7, pt[1]-7, pt[0]+7, pt[1]+7], fill=(255, 255, 255), outline=(16, 185, 129), width=4)
        
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i, pt in enumerate(chart_pts):
        d.text((pt[0] - 22, 705), days[i], fill=(148, 163, 184), font=font_reg_sm)
        
    # Divider
    d.line([70, 780, W - 70, 780], fill=(226, 232, 240), width=2)
    
    # Recent Activity
    d.text((70, 830), "Recent Activity", fill=(15, 23, 42), font=font_bold_lg)
    
    activities = [
        ("API response time improved", "12s → 2s (83% faster)", "2h ago", (16, 185, 129)),
        ("New module deployed", "v1.2.0 production build", "4h ago", (14, 165, 233)),
        ("Database backup completed", "Daily MySQL cluster sync", "8h ago", (168, 85, 247)),
        ("Automated tests passing", "142 unit / integration tests", "12h ago", (16, 185, 129)),
        ("Swagger documentation updated", "OpenAPI 3.0 specification", "1d ago", (245, 158, 11))
    ]
    
    ay = 920
    for title, subtitle, time_str, dot_col in activities:
        # Card item
        d.rounded_rectangle([70, ay, W - 70, ay + 120], radius=24, fill=(248, 250, 252), outline=(226, 232, 240), width=2)
        # Status circle
        d.ellipse([100, ay + 42, 136, ay + 78], fill=dot_col)
        # Title
        d.text((160, ay + 26), title, fill=(15, 23, 42), font=font_bold_sm)
        d.text((160, ay + 66), subtitle, fill=(100, 116, 139), font=font_reg_sm)
        # Time
        d.text((W - 190, ay + 42), time_str, fill=(148, 163, 184), font=font_reg_sm)
        ay += 145
        
    return img

# ----------------- CARD 5: My Projects -----------------
def create_card_5():
    img = Image.new("RGB", (W, H), (26, 32, 44))
    d = ImageDraw.Draw(img)
    draw_rounded_card_frame(d, (26, 32, 44))
    
    # Title & Search
    d.text((70, 80), "My Projects", fill=(255, 255, 255), font=font_bold_lg)
    # Search icon / magnifying glass
    d.ellipse([W - 120, 85, W - 90, 115], outline=(148, 163, 184), width=3)
    d.line([W - 98, 107, W - 80, 125], fill=(148, 163, 184), width=3)
    
    # Tabs
    d.rounded_rectangle([70, 175, 160, 230], radius=20, fill=(255, 255, 255))
    d.text((95, 188), "All", fill=(15, 23, 42), font=font_bold_sm)
    
    d.rounded_rectangle([185, 175, 335, 230], radius=20, fill=(45, 55, 72))
    d.text((210, 188), "Backend", fill=(203, 213, 225), font=font_reg_sm)
    
    d.rounded_rectangle([360, 175, 510, 230], radius=20, fill=(45, 55, 72))
    d.text((385, 188), "Frontend", fill=(203, 213, 225), font=font_reg_sm)
    
    projects = [
        ("</>", "API Rescue Lab", "Full Stack · React + DOT NET Core", (56, 189, 248)),
        ("▣", "SFMS System", "DOT NET Core · MySQL · Microservices", (168, 85, 247)),
        ("⚛", "RMA Flow", "React · ASPDOT NET Core · Clean Architecture", (34, 197, 94)),
        ("📊", "Reporting Automation", "Telerik · SQL · Background Services", (245, 158, 11)),
        ("🛡️", "API Watchdog", "Testing · Monitoring · Health Checks", (239, 68, 68))
    ]
    
    py = 280
    for icon, title, tech, badge_col in projects:
        # Project item card
        d.rounded_rectangle([70, py, W - 70, py + 230], radius=28, fill=(35, 43, 58), outline=(51, 65, 85), width=2)
        # Icon box
        d.rounded_rectangle([105, py + 35, 185, py + 115], radius=20, fill=(45, 55, 72))
        d.text((125, py + 50), icon, fill=badge_col, font=font_bold_md)
        # Title
        d.text((215, py + 45), title, fill=(255, 255, 255), font=font_bold_md)
        # Tech
        d.text((215, py + 105), tech, fill=(148, 163, 184), font=font_reg_sm)
        # Arrow CTA
        d.rounded_rectangle([105, py + 145, 260, py + 195], radius=16, fill=(51, 65, 85))
        d.text((125, py + 155), "Live Demo  →", fill=(241, 245, 249), font=font_reg_sm)
        d.text((W - 130, py + 70), "→", fill=(148, 163, 184), font=font_bold_lg)
        py += 265
        
    return img

# ----------------- CARD 6: Let's Build Together -----------------
def create_card_6():
    img = Image.new("RGB", (W, H), (248, 250, 252))
    d = ImageDraw.Draw(img)
    draw_rounded_card_frame(d, (248, 250, 252))
    
    # Tag
    d.text((70, 80), "Let's Build Together", fill=(100, 116, 139), font=font_bold_sm)
    d.text((W - 120, 75), "↗", fill=(15, 23, 42), font=font_bold_lg)
    
    # Big Title
    d.text((70, 220), "Have a", fill=(15, 23, 42), font=font_bold_xl)
    d.text((70, 310), "Project", fill=(15, 23, 42), font=font_bold_xl)
    d.text((70, 400), "in Mind?", fill=(15, 23, 42), font=font_bold_xl)
    
    # Description
    d.text((70, 520), "I'm always open to discussing new opportunities,", fill=(71, 85, 105), font=font_reg_md)
    d.text((70, 575), "system architectures, and high-performance ideas.", fill=(71, 85, 105), font=font_reg_md)
    
    # Button
    d.rounded_rectangle([70, 680, 420, 780], radius=48, fill=(15, 23, 42))
    d.text((120, 710), "Get in Touch  →", fill=(255, 255, 255), font=font_bold_md)
    
    # Contact Details Card
    d.rounded_rectangle([70, 850, W - 70, 1180], radius=32, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
    d.text((110, 890), "Contact Direct", fill=(15, 23, 42), font=font_bold_md)
    d.text((110, 960), "✉  ritesh.parmar1599@gmail.com", fill=(51, 65, 85), font=font_reg_md)
    d.text((110, 1030), "✈  github.com/riteshparmar-admin", fill=(51, 65, 85), font=font_reg_md)
    d.text((110, 1100), "in  linkedin.com/in/ritesh-parmar-13ab7a23a/", fill=(51, 65, 85), font=font_reg_md)
    
    # Mountain Landscape Illustration at bottom
    d.rounded_rectangle([70, 1260, W - 70, 1750], radius=32, fill=(235, 239, 244))
    d.polygon([(70, 1750), (290, 1420), (450, 1600), (630, 1380), (W - 70, 1750)], fill=(203, 213, 225))
    d.polygon([(70, 1750), (290, 1420), (380, 1530), (230, 1750)], fill=(148, 163, 184))
    d.polygon([(450, 1600), (630, 1380), (720, 1510), (590, 1750)], fill=(148, 163, 184))
    d.ellipse([W - 200, 1320, W - 140, 1380], fill=(226, 232, 240))
    
    return img

def main():
    generators = [
        create_card_1,
        create_card_2,
        create_card_3,
        create_card_4,
        create_card_5,
        create_card_6
    ]
    
    cards = [gen() for gen in generators]
    
    # Save 1 through 13
    for i in range(1, 14):
        card_img = cards[(i - 1) % len(cards)]
        p = f"work/{i}.webp"
        card_img.save(p, format="WEBP", quality=95)
        print(f"Saved {p}")

if __name__ == '__main__':
    main()
