# All machine data lives here. main.py imports MACHINES from this file.
# Each machine follows the same schema so the frontend can rely on consistent fields.

MACHINES = [

    # ── BULLDOZERS ──────────────────────────────────────────────────────────────

    {
        "id": 1,
        "name": "Cat D6 XE",
        "category": "Bulldozer",
        "manufacturer": "Caterpillar",
        "model": "D6 XE",
        "year": 2023,
        "weight": 20638,
        "horsepower": 215,
        "description": (
            "Electric drive bulldozer with industry-leading fuel efficiency and "
            "precision grade control. The D6 XE's electric drive system delivers "
            "constant, uninterrupted power to the ground, reducing fuel consumption "
            "by up to 35% compared to traditional drive systems. Ideal for land "
            "clearing, road building, and earthmoving."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C9.3B ACERT",
            "Net Power":           "215 HP / 160 kW",
            "Operating Weight":    "20,638 kg",
            "Blade Capacity":      "4.5 m³",
            "Max Blade Width":     "3,900 mm",
            "Max Speed Forward":   "10.7 km/h",
            "Ground Pressure":     "52.4 kPa",
            "Fuel Tank Capacity":  "310 L",
            "Drive System":        "Electric Drive (XE)",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+D6+XE+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+D6+XE+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+D6+XE+Cab+Detail",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=D6+XE+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=D6+XE+Dimensions",
        ],
    },
    {
        "id": 2,
        "name": "Cat D8",
        "category": "Bulldozer",
        "manufacturer": "Caterpillar",
        "model": "D8",
        "year": 2022,
        "weight": 38556,
        "horsepower": 310,
        "description": (
            "Large-frame bulldozer built for heavy reclamation, production dozing, "
            "and large-scale earthmoving operations. Features a fully automatic "
            "powershift transmission with 3 forward and 3 reverse speeds. "
            "The elevated sprocket design reduces wear on major components."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C15 ACERT",
            "Net Power":           "310 HP / 231 kW",
            "Operating Weight":    "38,556 kg",
            "Blade Capacity":      "10.7 m³ (Semi-U)",
            "Max Blade Width":     "4,760 mm",
            "Max Speed Forward":   "11.3 km/h",
            "Ground Pressure":     "72.8 kPa",
            "Fuel Tank Capacity":  "640 L",
            "Transmission":        "Powershift 3F/3R",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+D8+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+D8+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+D8+Undercarriage",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=D8+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=D8+Dimensions",
        ],
    },
    {
        "id": 3,
        "name": "Cat D11",
        "category": "Bulldozer",
        "manufacturer": "Caterpillar",
        "model": "D11",
        "year": 2023,
        "weight": 104326,
        "horsepower": 850,
        "description": (
            "Caterpillar's flagship large dozer, designed for the highest productivity "
            "in mining and heavy construction applications. The D11 delivers unmatched "
            "capacity for large-scale operations and features the Cat GRADE with 3D "
            "system for fully automated blade control."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat 3508C EUI",
            "Net Power":           "850 HP / 634 kW",
            "Operating Weight":    "104,326 kg",
            "Blade Capacity":      "37.6 m³ (SU Blade)",
            "Max Blade Width":     "6,858 mm",
            "Max Speed Forward":   "11.4 km/h",
            "Ground Pressure":     "157 kPa",
            "Fuel Tank Capacity":  "1,628 L",
            "Track Gauge":         "2,895 mm",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+D11+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+D11+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+D11+Mining+Site",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=D11+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=D11+Dimensions",
        ],
    },

    # ── EXCAVATORS ──────────────────────────────────────────────────────────────

    {
        "id": 4,
        "name": "Cat 320",
        "category": "Excavator",
        "manufacturer": "Caterpillar",
        "model": "320",
        "year": 2023,
        "weight": 22800,
        "horsepower": 121,
        "description": (
            "20-tonne hydraulic excavator with Smart Mode auto-shifting that "
            "automatically matches engine and hydraulic power to job conditions. "
            "Available with factory-installed Cat Grade, 2D, 3D and assist "
            "technology for precision digging on any job site."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C4.4 ACERT",
            "Net Power":           "121 HP / 90.2 kW",
            "Operating Weight":    "22,800 kg",
            "Max Digging Depth":   "6,760 mm",
            "Max Reach":           "10,335 mm",
            "Bucket Capacity":     "0.52–1.19 m³",
            "Swing Speed":         "12.1 rpm",
            "Fuel Tank Capacity":  "410 L",
            "Hydraulic Flow":      "2 × 200 L/min",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+320+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+320+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+320+Boom+Detail",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=320+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=320+Reach+Diagram",
        ],
    },
    {
        "id": 5,
        "name": "Cat 340",
        "category": "Excavator",
        "manufacturer": "Caterpillar",
        "model": "340",
        "year": 2022,
        "weight": 40200,
        "horsepower": 270,
        "description": (
            "40-tonne next-generation excavator delivering up to 45% more production "
            "and 25% lower fuel consumption compared to previous models. "
            "Features an advanced hydraulic system and larger boom and stick for "
            "demanding mass excavation and large-scale construction projects."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C9.3B ACERT",
            "Net Power":           "270 HP / 201 kW",
            "Operating Weight":    "40,200 kg",
            "Max Digging Depth":   "7,545 mm",
            "Max Reach":           "11,650 mm",
            "Bucket Capacity":     "1.2–2.6 m³",
            "Swing Speed":         "10.2 rpm",
            "Fuel Tank Capacity":  "600 L",
            "Hydraulic Flow":      "2 × 330 L/min",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+340+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+340+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+340+Working",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=340+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=340+Reach+Diagram",
        ],
    },
    {
        "id": 6,
        "name": "Cat 395",
        "category": "Excavator",
        "manufacturer": "Caterpillar",
        "model": "395",
        "year": 2023,
        "weight": 90500,
        "horsepower": 433,
        "description": (
            "Large hydraulic excavator engineered for mass excavation, heavy lift, "
            "and demanding quarry applications. The Cat 395 delivers up to 10% more "
            "productivity than its predecessor with a reinforced undercarriage and "
            "heavy-lift configuration available for port and pipeline work."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C18 ACERT",
            "Net Power":           "433 HP / 323 kW",
            "Operating Weight":    "90,500 kg",
            "Max Digging Depth":   "8,380 mm",
            "Max Reach":           "13,250 mm",
            "Bucket Capacity":     "3.6–6.9 m³",
            "Swing Speed":         "7.0 rpm",
            "Fuel Tank Capacity":  "1,150 L",
            "Hydraulic Flow":      "2 × 520 L/min",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+395+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+395+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+395+Quarry",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=395+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=395+Reach+Diagram",
        ],
    },

    # ── BACKHOES ────────────────────────────────────────────────────────────────

    {
        "id": 7,
        "name": "Cat 420",
        "category": "Backhoe",
        "manufacturer": "Caterpillar",
        "model": "420",
        "year": 2022,
        "weight": 9070,
        "horsepower": 93,
        "description": (
            "Versatile backhoe loader with a powerful 93-hp engine, extendable "
            "stick and multi-purpose bucket for diverse job sites. The 420 features "
            "Cat's exclusive two-pedal electro-hydraulic powershift transmission "
            "for smooth, on-the-fly directional changes."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C3.6",
            "Net Power":           "93 HP / 69.3 kW",
            "Operating Weight":    "9,070 kg",
            "Max Dig Depth":       "5,882 mm",
            "Max Reach at Ground": "6,844 mm",
            "Loader Lift Capacity":"4,300 kg",
            "Bucket Rotation":     "184°",
            "Fuel Tank Capacity":  "163 L",
            "Transmission":        "Electro-Hydraulic Powershift",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+420+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+420+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+420+Bucket",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=420+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=420+Reach+Diagram",
        ],
    },
    {
        "id": 8,
        "name": "Cat 430",
        "category": "Backhoe",
        "manufacturer": "Caterpillar",
        "model": "430",
        "year": 2023,
        "weight": 9435,
        "horsepower": 100,
        "description": (
            "Heavy-duty backhoe loader offering superior breakout force and enhanced "
            "operator comfort for utility and construction work. The 430 includes "
            "a pressurized and sound-suppressed cab with a fully adjustable "
            "suspension seat and ergonomic joystick controls."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C3.6",
            "Net Power":           "100 HP / 74.5 kW",
            "Operating Weight":    "9,435 kg",
            "Max Dig Depth":       "6,057 mm",
            "Max Reach at Ground": "7,010 mm",
            "Loader Lift Capacity":"4,640 kg",
            "Bucket Rotation":     "184°",
            "Fuel Tank Capacity":  "163 L",
            "Transmission":        "Electro-Hydraulic Powershift",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+430+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+430+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+430+Loader",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=430+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=430+Reach+Diagram",
        ],
    },
    {
        "id": 9,
        "name": "Cat 450",
        "category": "Backhoe",
        "manufacturer": "Caterpillar",
        "model": "450",
        "year": 2023,
        "weight": 10360,
        "horsepower": 116,
        "description": (
            "Top-of-the-range backhoe loader with Cat Connect technology for "
            "integrated load-sensing hydraulics and improved fuel efficiency. "
            "The 450 offers the widest cab in its class with industry-leading "
            "visibility and optional Grade Control for precise grading."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C3.6",
            "Net Power":           "116 HP / 86.5 kW",
            "Operating Weight":    "10,360 kg",
            "Max Dig Depth":       "6,261 mm",
            "Max Reach at Ground": "7,217 mm",
            "Loader Lift Capacity":"5,130 kg",
            "Bucket Rotation":     "184°",
            "Fuel Tank Capacity":  "163 L",
            "Technology":          "Cat Connect Grade Control",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+450+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+450+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+450+Grade+Control",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=450+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=450+Reach+Diagram",
        ],
    },

    # ── BOBCAT ──────────────────────────────────────────────────────────────────

    {
        "id": 10,
        "name": "Bobcat E35",
        "category": "Bobcat",
        "manufacturer": "Bobcat",
        "model": "E35",
        "year": 2023,
        "weight": 3605,
        "horsepower": 24,
        "description": (
            "The Bobcat E35 is a compact excavator built for tight spaces and "
            "versatile applications. With its zero tail swing design, the E35 "
            "can work safely in confined areas without worrying about the rear "
            "of the machine swinging outside the tracks."
        ),
        "technicalSpecs": {
            "Engine Model":        "Kubota D1703",
            "Net Power":           "24 HP / 17.9 kW",
            "Operating Weight":    "3,605 kg",
            "Max Digging Depth":   "3,628 mm",
            "Max Reach":           "5,720 mm",
            "Tail Swing":          "Zero Tail Swing",
            "Bucket Capacity":     "0.06–0.12 m³",
            "Fuel Tank Capacity":  "40 L",
            "Auxiliary Hydraulics":"High-Flow Optional",
        },
        "images": [
            "https://placehold.co/800x500/D84315/FFFFFF?text=Bobcat+E35+Front",
            "https://placehold.co/800x500/1A1A1A/FF5722?text=Bobcat+E35+Side",
            "https://placehold.co/800x500/2d2d2d/FF5722?text=Bobcat+E35+Detail",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=E35+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=E35+Dimensions",
        ],
    },
    {
        "id": 11,
        "name": "Bobcat T86",
        "category": "Bobcat",
        "manufacturer": "Bobcat",
        "model": "T86",
        "year": 2024,
        "weight": 5398,
        "horsepower": 92,
        "description": (
            "The Bobcat T86 is a large-frame compact track loader delivering "
            "maximum power and performance with a rated operating capacity of "
            "1,474 kg. The T86 features Bobcat's vertical lift path for "
            "outstanding reach and dump height, ideal for truck loading."
        ),
        "technicalSpecs": {
            "Engine Model":        "Deutz TCD 2.9 L4",
            "Net Power":           "92 HP / 68.7 kW",
            "Operating Weight":    "5,398 kg",
            "Rated Operating Cap": "1,474 kg",
            "Tip Load":            "2,948 kg",
            "Max Lift Height":     "3,950 mm",
            "Travel Speed":        "12.5 km/h",
            "Fuel Tank Capacity":  "90 L",
            "Lift Path":           "Vertical",
        },
        "images": [
            "https://placehold.co/800x500/D84315/FFFFFF?text=Bobcat+T86+Front",
            "https://placehold.co/800x500/1A1A1A/FF5722?text=Bobcat+T86+Side",
            "https://placehold.co/800x500/2d2d2d/FF5722?text=Bobcat+T86+Detail",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=T86+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=T86+Dimensions",
        ],
    },

    # ── MINI BAGGER ─────────────────────────────────────────────────────────────

    {
        "id": 12,
        "name": "Kubota KX040-4",
        "category": "Mini Bagger",
        "manufacturer": "Kubota",
        "model": "KX040-4",
        "year": 2023,
        "weight": 4160,
        "horsepower": 40,
        "description": (
            "The Kubota KX040-4 is a 4-tonne mini excavator offering an optimal "
            "balance of compact dimensions and powerful digging performance. "
            "Its retractable undercarriage retracts from 1,550 mm to 1,990 mm "
            "for easy transport and improved stability on the job site."
        ),
        "technicalSpecs": {
            "Engine Model":        "Kubota V2607-CR-TE4",
            "Net Power":           "40 HP / 29.8 kW",
            "Operating Weight":    "4,160 kg",
            "Max Digging Depth":   "3,838 mm",
            "Max Reach":           "6,235 mm",
            "Bucket Capacity":     "0.11 m³",
            "Tail Swing Radius":   "1,130 mm",
            "Fuel Tank Capacity":  "55.5 L",
            "Undercarriage":       "Retractable (1,550–1,990 mm)",
        },
        "images": [
            "https://placehold.co/800x500/1B5E20/FFFFFF?text=Kubota+KX040+Front",
            "https://placehold.co/800x500/1A1A1A/66BB6A?text=Kubota+KX040+Side",
            "https://placehold.co/800x500/2d2d2d/66BB6A?text=Kubota+KX040+Detail",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=KX040+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=KX040+Dimensions",
        ],
    },
    {
        "id": 13,
        "name": "Cat 301.7",
        "category": "Mini Bagger",
        "manufacturer": "Caterpillar",
        "model": "301.7",
        "year": 2023,
        "weight": 1795,
        "horsepower": 13,
        "description": (
            "The Cat 301.7 is a 1.8-tonne mini excavator offering the smallest "
            "footprint in the Cat mini lineup, ideal for interior demolition, "
            "landscaping, and utility work in very confined spaces. "
            "Its canopy and cab variants provide flexible protection for operators."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C0.7",
            "Net Power":           "13 HP / 9.7 kW",
            "Operating Weight":    "1,795 kg",
            "Max Digging Depth":   "2,380 mm",
            "Max Reach":           "4,020 mm",
            "Bucket Capacity":     "0.033 m³",
            "Tail Swing Radius":   "Zero Tail Swing",
            "Fuel Tank Capacity":  "16 L",
            "Track Width":         "230 mm (rubber)",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+301.7+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+301.7+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+301.7+Detail",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=301.7+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=301.7+Dimensions",
        ],
    },

    # ── LOADER ──────────────────────────────────────────────────────────────────

    {
        "id": 14,
        "name": "Cat 950 GC",
        "category": "Loader",
        "manufacturer": "Caterpillar",
        "model": "950 GC",
        "year": 2022,
        "weight": 17337,
        "horsepower": 186,
        "description": (
            "The Cat 950 GC is a medium wheel loader designed for cost-effective "
            "performance in general construction and aggregate applications. "
            "It features a Z-bar loader linkage that provides excellent breakout "
            "force and load retention for efficient material handling."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C7.1 ACERT",
            "Net Power":           "186 HP / 138.7 kW",
            "Operating Weight":    "17,337 kg",
            "Bucket Capacity":     "3.1 m³",
            "Breakout Force":      "153.6 kN",
            "Max Travel Speed":    "39.8 km/h",
            "Tip Load (Full Turn)":"9,848 kg",
            "Fuel Tank Capacity":  "265 L",
            "Transmission":        "Cat Automatic 4F/3R",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+950+GC+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+950+GC+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+950+GC+Bucket",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=950+GC+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=950+GC+Dimensions",
        ],
    },
    {
        "id": 15,
        "name": "Volvo L120H",
        "category": "Loader",
        "manufacturer": "Volvo",
        "model": "L120H",
        "year": 2023,
        "weight": 20800,
        "horsepower": 249,
        "description": (
            "The Volvo L120H is a versatile wheel loader offering a perfect "
            "balance of productivity and fuel efficiency. OptiShift technology "
            "with torque converter lock-up and Reverse-By-Braking reduces "
            "fuel consumption and wear in loading and truck filling operations."
        ),
        "technicalSpecs": {
            "Engine Model":        "Volvo D8J EU Stage V",
            "Net Power":           "249 HP / 186 kW",
            "Operating Weight":    "20,800 kg",
            "Bucket Capacity":     "3.5–5.5 m³",
            "Breakout Force":      "168 kN",
            "Max Travel Speed":    "40 km/h",
            "Tip Load (Full Turn)":"11,400 kg",
            "Fuel Tank Capacity":  "400 L",
            "Technology":          "OptiShift + Load-Sensing Hydraulics",
        },
        "images": [
            "https://placehold.co/800x500/1565C0/FFFFFF?text=Volvo+L120H+Front",
            "https://placehold.co/800x500/1A1A1A/42A5F5?text=Volvo+L120H+Side",
            "https://placehold.co/800x500/2d2d2d/42A5F5?text=Volvo+L120H+Bucket",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=L120H+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=L120H+Dimensions",
        ],
    },

    # ── CRANE ───────────────────────────────────────────────────────────────────

    {
        "id": 16,
        "name": "Liebherr LTM 1200-5.1",
        "category": "Crane",
        "manufacturer": "Liebherr",
        "model": "LTM 1200-5.1",
        "year": 2022,
        "weight": 72000,
        "horsepower": 680,
        "description": (
            "The Liebherr LTM 1200-5.1 is a 200-tonne all-terrain mobile crane "
            "on a 5-axle carrier with outstanding manoeuvrability. The 80-metre "
            "telescopic main boom and variable Y-guying system allow this crane "
            "to tackle a wide range of lifting and rigging challenges on construction sites."
        ),
        "technicalSpecs": {
            "Max Lifting Capacity":"200 t",
            "Main Boom Length":    "80 m (telescopic)",
            "Max Tip Height":      "120 m (with fly jib)",
            "Engine (Carrier)":    "Liebherr D9508 A8 / 680 HP",
            "Engine (Superstr.)":  "Liebherr D934 S A6 / 272 HP",
            "Carrier Weight":      "72,000 kg (counterweight excl.)",
            "Road Speed":          "75 km/h",
            "Axles":               "5",
            "Outrigger Spread":    "8.2 × 8.0 m",
        },
        "images": [
            "https://placehold.co/800x500/B71C1C/FFFFFF?text=Liebherr+LTM+1200+Front",
            "https://placehold.co/800x500/1A1A1A/EF5350?text=Liebherr+LTM+1200+Boom",
            "https://placehold.co/800x500/2d2d2d/EF5350?text=Liebherr+LTM+1200+Cab",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=LTM+1200+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=LTM+1200+Load+Chart",
        ],
    },
    {
        "id": 17,
        "name": "Manitowoc 16000",
        "category": "Crane",
        "manufacturer": "Manitowoc",
        "model": "16000",
        "year": 2023,
        "weight": 204000,
        "horsepower": 800,
        "description": (
            "The Manitowoc 16000 is a lattice-boom crawler crane with a maximum "
            "lifting capacity of 600 tonnes. Designed for large petrochemical, "
            "power, and industrial construction projects, it features Manitowoc's "
            "Crane Control System (CCS) for precise, real-time load management."
        ),
        "technicalSpecs": {
            "Max Lifting Capacity":"600 t",
            "Max Boom Length":     "137 m",
            "Max Luffing Jib":     "91 m",
            "Engine":              "Cummins QSK19 / 800 HP",
            "Operating Weight":    "204,000 kg (base machine)",
            "Max Counterweight":   "200 t",
            "Carbody Width":       "9.9 m",
            "Track Width":         "1.2 m",
            "Control System":      "Manitowoc CCS",
        },
        "images": [
            "https://placehold.co/800x500/37474F/FFFFFF?text=Manitowoc+16000+Front",
            "https://placehold.co/800x500/1A1A1A/90A4AE?text=Manitowoc+16000+Boom",
            "https://placehold.co/800x500/2d2d2d/90A4AE?text=Manitowoc+16000+Detail",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=16000+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=16000+Load+Chart",
        ],
    },

    # ── FORKLIFT ────────────────────────────────────────────────────────────────

    {
        "id": 18,
        "name": "Toyota 8FBN25",
        "category": "Forklift",
        "manufacturer": "Toyota",
        "model": "8FBN25",
        "year": 2023,
        "weight": 3855,
        "horsepower": 20,
        "description": (
            "The Toyota 8FBN25 is a 2.5-tonne three-phase AC electric counterbalance "
            "forklift designed for intensive indoor warehouse operations. "
            "System of Active Stability (SAS) electronically monitors and controls "
            "stability to prevent tip-over in a wide range of operating conditions."
        ),
        "technicalSpecs": {
            "Drive Type":          "AC Electric (3-phase)",
            "Rated Capacity":      "2,500 kg",
            "Load Centre":         "500 mm",
            "Lift Height (max)":   "6,000 mm",
            "Machine Weight":      "3,855 kg",
            "Battery Voltage":     "48 V",
            "Travel Speed":        "16 km/h (laden)",
            "Turning Radius":      "2,340 mm",
            "Safety System":       "Toyota SAS (Active Stability)",
        },
        "images": [
            "https://placehold.co/800x500/E65100/FFFFFF?text=Toyota+8FBN25+Front",
            "https://placehold.co/800x500/1A1A1A/FF6D00?text=Toyota+8FBN25+Side",
            "https://placehold.co/800x500/2d2d2d/FF6D00?text=Toyota+8FBN25+Mast",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=8FBN25+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=8FBN25+Dimensions",
        ],
    },
    {
        "id": 19,
        "name": "Cat GP25N",
        "category": "Forklift",
        "manufacturer": "Caterpillar",
        "model": "GP25N",
        "year": 2022,
        "weight": 3864,
        "horsepower": 50,
        "description": (
            "The Cat GP25N is a 2.5-tonne LPG counterbalance forklift delivering "
            "excellent performance in demanding outdoor and indoor environments. "
            "With Cat's exclusive side-mount LPG tank, cylinder changes are "
            "quick and safe, minimizing downtime on busy distribution sites."
        ),
        "technicalSpecs": {
            "Drive Type":          "LPG (Liquefied Petroleum Gas)",
            "Engine":              "Cat/Mitsubishi 4G63",
            "Net Power":           "50 HP / 37.3 kW",
            "Rated Capacity":      "2,500 kg",
            "Lift Height (max)":   "7,000 mm",
            "Machine Weight":      "3,864 kg",
            "Travel Speed":        "19 km/h (laden)",
            "Turning Radius":      "2,350 mm",
            "Mast Type":           "Full Free Triple",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+GP25N+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+GP25N+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+GP25N+Mast",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=GP25N+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=GP25N+Dimensions",
        ],
    },

    # ── GRADER ──────────────────────────────────────────────────────────────────

    {
        "id": 20,
        "name": "Cat 140 GC",
        "category": "Grader",
        "manufacturer": "Caterpillar",
        "model": "140 GC",
        "year": 2023,
        "weight": 14566,
        "horsepower": 155,
        "description": (
            "The Cat 140 GC motor grader is designed for road maintenance and "
            "construction grading operations. It provides exceptional blade "
            "control and a smooth, quiet cab environment, making it an ideal "
            "choice for road authorities and civil contractors."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C7.1 ACERT",
            "Net Power":           "155 HP / 115.5 kW",
            "Operating Weight":    "14,566 kg",
            "Blade Length":        "3,700 mm",
            "Blade Width":         "610 mm",
            "Max Blade Sideshift": "676 mm (each side)",
            "Max Gradeability":    "25%",
            "Fuel Tank Capacity":  "227 L",
            "Wheel Arrangement":   "AWD Optional",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+140+GC+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+140+GC+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+140+GC+Blade",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=140+GC+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=140+GC+Dimensions",
        ],
    },
    {
        "id": 21,
        "name": "Komatsu GD655-7",
        "category": "Grader",
        "manufacturer": "Komatsu",
        "model": "GD655-7",
        "year": 2022,
        "weight": 16965,
        "horsepower": 175,
        "description": (
            "The Komatsu GD655-7 motor grader delivers outstanding blade control "
            "and powerful grading performance for road construction and maintenance. "
            "The GD655-7 is equipped with Komatsu's Tier 4 Final engine featuring "
            "Eco Mode and auto deceleration for reduced fuel consumption."
        ),
        "technicalSpecs": {
            "Engine Model":        "Komatsu SAA6D107E-3",
            "Net Power":           "175 HP / 130 kW",
            "Operating Weight":    "16,965 kg",
            "Blade Length":        "3,965 mm",
            "Blade Height":        "635 mm",
            "Max Circle Drive Torque": "6.5 kN·m",
            "Max Gradeability":    "25%",
            "Fuel Tank Capacity":  "270 L",
            "Hydraulic System":    "Load-Sensing Variable Displacement",
        },
        "images": [
            "https://placehold.co/800x500/F57F17/1A1A1A?text=Komatsu+GD655+Front",
            "https://placehold.co/800x500/1A1A1A/FFB300?text=Komatsu+GD655+Side",
            "https://placehold.co/800x500/2d2d2d/FFB300?text=Komatsu+GD655+Blade",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=GD655+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=GD655+Dimensions",
        ],
    },

    # ── ROLLER ──────────────────────────────────────────────────────────────────

    {
        "id": 22,
        "name": "Cat CS11 GC",
        "category": "Roller",
        "manufacturer": "Caterpillar",
        "model": "CS11 GC",
        "year": 2022,
        "weight": 10705,
        "horsepower": 101,
        "description": (
            "The Cat CS11 GC vibratory soil compactor is designed for efficient "
            "compaction of granular soils, base materials, and asphalt on highway "
            "and road construction projects. Its smooth drum with dual-amplitude "
            "vibration provides excellent compaction in fewer passes."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C3.6",
            "Net Power":           "101 HP / 75.4 kW",
            "Operating Weight":    "10,705 kg",
            "Drum Width":          "2,130 mm",
            "Drum Diameter":       "1,524 mm",
            "Vibration Frequency": "32 Hz / 28 Hz",
            "Amplitude (High/Low)":"1.87 mm / 0.90 mm",
            "Max Travel Speed":    "12.2 km/h",
            "Fuel Tank Capacity":  "180 L",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+CS11+GC+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+CS11+GC+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+CS11+GC+Drum",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=CS11+GC+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=CS11+GC+Dimensions",
        ],
    },
    {
        "id": 23,
        "name": "Bomag BW 213 D-5",
        "category": "Roller",
        "manufacturer": "Bomag",
        "model": "BW 213 D-5",
        "year": 2023,
        "weight": 12900,
        "horsepower": 130,
        "description": (
            "The Bomag BW 213 D-5 single drum roller with padfoot shell is "
            "purpose-built for compaction of cohesive soils on dam and embankment "
            "construction. Bomag's DRVMS (Density and Ratio Value Measurement System) "
            "provides continuous in-situ compaction documentation."
        ),
        "technicalSpecs": {
            "Engine Model":        "Deutz TCD 3.6 L4",
            "Net Power":           "130 HP / 97 kW",
            "Operating Weight":    "12,900 kg",
            "Drum Width":          "2,130 mm",
            "Centrifugal Force":   "250 / 127 kN",
            "Vibration Frequency": "32 / 28 Hz",
            "Max Travel Speed":    "10 km/h",
            "Fuel Tank Capacity":  "255 L",
            "Smart Technology":    "Bomag DRVMS",
        },
        "images": [
            "https://placehold.co/800x500/C62828/FFFFFF?text=Bomag+BW213+Front",
            "https://placehold.co/800x500/1A1A1A/EF5350?text=Bomag+BW213+Side",
            "https://placehold.co/800x500/2d2d2d/EF5350?text=Bomag+BW213+Drum",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=BW213+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=BW213+Dimensions",
        ],
    },

    # ── DUMP TRUCK ──────────────────────────────────────────────────────────────

    {
        "id": 24,
        "name": "Cat 777G",
        "category": "Dump Truck",
        "manufacturer": "Caterpillar",
        "model": "777G",
        "year": 2022,
        "weight": 70761,
        "horsepower": 1050,
        "description": (
            "The Cat 777G is a 100-tonne off-highway rigid dump truck built for "
            "high-productivity mining and quarry haul operations. The 777G features "
            "an automatic retarder control and Cat Detect Object Detection system "
            "for enhanced safety on busy haul roads."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C27 ACERT",
            "Net Power":           "1,050 HP / 783 kW",
            "Payload Capacity":    "100 t",
            "Gross Machine Weight":"170,800 kg",
            "Empty Weight":        "70,761 kg",
            "Body Capacity":       "59.5 m³",
            "Max Travel Speed":    "64.4 km/h",
            "Fuel Tank Capacity":  "3,028 L",
            "Transmission":        "Automatic Planetary 7F/1R",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+777G+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+777G+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+777G+Dumping",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=777G+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=777G+Dimensions",
        ],
    },
    {
        "id": 25,
        "name": "Komatsu HD785-7",
        "category": "Dump Truck",
        "manufacturer": "Komatsu",
        "model": "HD785-7",
        "year": 2023,
        "weight": 76940,
        "horsepower": 1192,
        "description": (
            "The Komatsu HD785-7 is a 91-tonne payload mining dump truck renowned "
            "for its fuel efficiency and long service intervals. The VHMS (Vehicle "
            "Health Monitoring System) and Komtrax satellite monitoring provide "
            "real-time operational data to maximise availability and reduce downtime."
        ),
        "technicalSpecs": {
            "Engine Model":        "Komatsu SSDA16V160",
            "Net Power":           "1,192 HP / 889 kW",
            "Payload Capacity":    "91 t",
            "Gross Vehicle Weight":"168,000 kg",
            "Empty Weight":        "76,940 kg",
            "Body Capacity":       "57 m³",
            "Max Travel Speed":    "64 km/h",
            "Fuel Tank Capacity":  "3,240 L",
            "Monitoring System":   "Komatsu VHMS + Komtrax",
        },
        "images": [
            "https://placehold.co/800x500/F57F17/1A1A1A?text=Komatsu+HD785+Front",
            "https://placehold.co/800x500/1A1A1A/FFB300?text=Komatsu+HD785+Side",
            "https://placehold.co/800x500/2d2d2d/FFB300?text=Komatsu+HD785+Bed",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=HD785+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=HD785+Dimensions",
        ],
    },

    # ── SKID STEER ──────────────────────────────────────────────────────────────

    {
        "id": 26,
        "name": "Cat 262D3",
        "category": "Skid Steer",
        "manufacturer": "Caterpillar",
        "model": "262D3",
        "year": 2023,
        "weight": 3271,
        "horsepower": 74,
        "description": (
            "The Cat 262D3 skid steer loader delivers strong performance for "
            "construction, landscaping, and agricultural applications. "
            "Its vertical lift path provides excellent reach and dump height "
            "for efficient truck loading, while the wide cab opening eases "
            "operator entry and exit throughout the working day."
        ),
        "technicalSpecs": {
            "Engine Model":        "Cat C2.8T",
            "Net Power":           "74 HP / 55.2 kW",
            "Operating Weight":    "3,271 kg",
            "Rated Operating Cap": "975 kg",
            "Tip Load":            "1,950 kg",
            "Max Lift Height":     "3,146 mm",
            "Travel Speed":        "11.7 km/h",
            "Fuel Tank Capacity":  "68 L",
            "Lift Path":           "Vertical",
        },
        "images": [
            "https://placehold.co/800x500/F4A820/1A1A1A?text=Cat+262D3+Front",
            "https://placehold.co/800x500/1A1A1A/F4A820?text=Cat+262D3+Side",
            "https://placehold.co/800x500/2d2d2d/F4A820?text=Cat+262D3+Bucket",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=262D3+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=262D3+Dimensions",
        ],
    },
    {
        "id": 27,
        "name": "Bobcat S770",
        "category": "Skid Steer",
        "manufacturer": "Bobcat",
        "model": "S770",
        "year": 2023,
        "weight": 4382,
        "horsepower": 92,
        "description": (
            "The Bobcat S770 is a large-frame skid steer loader engineered for "
            "demanding applications requiring high lift capacity and powerful "
            "auxiliary hydraulics. The S770 features Bobcat's selectable joystick "
            "controls and a pressurised cab with filtered air for all-day comfort."
        ),
        "technicalSpecs": {
            "Engine Model":        "Deutz TCD 2.9 L4",
            "Net Power":           "92 HP / 68.7 kW",
            "Operating Weight":    "4,382 kg",
            "Rated Operating Cap": "1,588 kg",
            "Tip Load":            "3,175 kg",
            "Max Lift Height":     "3,023 mm",
            "Travel Speed":        "12.5 km/h",
            "Fuel Tank Capacity":  "95 L",
            "Auxiliary Hydraulics":"High-Flow (117 L/min)",
        },
        "images": [
            "https://placehold.co/800x500/D84315/FFFFFF?text=Bobcat+S770+Front",
            "https://placehold.co/800x500/1A1A1A/FF5722?text=Bobcat+S770+Side",
            "https://placehold.co/800x500/2d2d2d/FF5722?text=Bobcat+S770+Bucket",
        ],
        "schematics": [
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=S770+Side+Profile",
            "https://placehold.co/900x600/0d1b2a/7ab8f5?text=S770+Dimensions",
        ],
    },
]
