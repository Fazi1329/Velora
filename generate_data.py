import json

# Define the exact 55 products extracted from the supplier image
products = []

raw_data = [
    # 1-6 Electronics & Accessories
    (1, "Electronics & Accessories", "JBL Speakers", 150, "VEL-EA-01", "JBL Charge 5 Waterproof Portable Speaker", "Electronics",
     "https://images.unsplash.com/photo-1545454675-3531b543be5d?auto=format&fit=crop&w=800&q=80",
     "High-output portable acoustics with dual passive radiators, IP67 waterproof certification, built-in powerbank, and 20 hours of playtime.",
     {"Driver": "Racetrack driver & separate tweeter", "Playtime": "Up to 20 Hours", "Water Rating": "IP67 Waterproof & Dustproof", "Origin": "Supplier Authorized Hub"},
     "Tier 1 Sound Series - Preserved exact $150 USD price.", False, ""),

    (2, "Electronics & Accessories", "AirPods Pro", 150, "VEL-EA-02", "AirPods Pro (2nd Generation Active Noise Cancellation)", "Electronics",
     "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?auto=format&fit=crop&w=800&q=80",
     "Pro-grade wireless earbuds featuring intelligent active noise cancellation, adaptive transparency, personalized spatial audio, and MagSafe case.",
     {"Chip": "H2 Headphone Chip", "Audio": "Personalized Spatial Audio with Head Tracking", "Case": "MagSafe USB-C Fast Charge", "Origin": "Supplier Authorized Hub"},
     "Flagship wireless in-ear audio. Preserved exact $150 USD price.", False, ""),

    (3, "Electronics & Accessories", "AirPods Max", 200, "VEL-EA-03", "AirPods Max Wireless Over-Ear Active Noise Cancellation", "Electronics",
     "https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=800&q=80",
     "High-fidelity computational acoustics enclosed in anodized aluminum earcups with breathable knit canopy and custom neodymium magnetic drivers.",
     {"Drivers": "40mm Dynamic Neodymium", "Noise Control": "Active Noise Cancellation + Transparency", "Finish": "Space Gray / Anodized Aluminum", "Origin": "Supplier Authorized Hub"},
     "Over-ear studio luxury audio. Preserved exact $200 USD price.", False, ""),

    (4, "Electronics & Accessories", "Smart Watches", 100, "VEL-EA-04", "Smart Watch Ultra Precision Navigation & Biometrics", "Electronics",
     "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80",
     "Aerospace titanium alloy chassis housing Always-On OLED display, multi-sport biometrics, optical ECG heart tracker, and cellular capability.",
     {"Chassis": "49mm Lightweight Titanium Alloy", "Water Rating": "WR100 / 100m Dive Rated", "Sensors": "Optical Blood Oxygen & Heart Rate", "Origin": "Supplier Verified Hub"},
     "Tier 1 Smart Watch - Preserved exact $100 USD price.", False, ""),

    (5, "Electronics & Accessories", "Sneakers", 150, "VEL-EA-05", "Designer Streetwear Silhouette Luxury Sneakers", "Footwear",
     "https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=800&q=80",
     "Architectural sculpted midsole paired with fine calfskin leather overlays, breathable ballistic mesh underlays, and ergonomic cushioning.",
     {"Upper": "Technical Mesh & Calfskin Suede", "Sole": "Multi-Tier Sculpted Rubber", "Colorway": "Monochrome Studio Edition", "Origin": "Supplier Curated Stock"},
     "Tier 1 Sneakers ($150 USD). Distinguish from Row 48 ($100 USD).", True, "Categorized under Electronics & Accessories in original sheet; flagged for multi-category placement."),

    (6, "Electronics & Accessories", "Colognes", 200, "VEL-EA-06", "Luxury Fragrance Sourcing Discovery Extrait", "Colognes",
     "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?auto=format&fit=crop&w=800&q=80",
     "Artisanal European niche fragrance discovery selection featuring concentrated parfum oils, rare woody accords, and exceptional longevity.",
     {"Concentration": "Pure Extrait de Parfum", "Volume": "100ml / 3.4 fl oz", "Notes": "Smoky Amber, Tuscan Iris, Cashmere", "Origin": "Parisian Sourcing Network"},
     "Tier 1 Colognes ($200 USD). Distinguish from specific fragrance bottles.", True, "Categorized under Electronics & Accessories in original sheet; linked with Cologne suite."),

    # 7-13 Sportwears
    (7, "Sportwears", "Nike", 150, "VEL-SP-07", "Nike Sportswear Tech Fleece Heritage Track Set", "Sportswear",
     "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=800&q=80",
     "Double-sided spacer fleece delivering lightweight warmth without bulk, articulated sleeves, and bonded zip utility storage.",
     {"Material": "66% Cotton / 34% Polyester Tech Fleece", "Cut": "Slim Tailored Athletic", "Care": "Machine Wash Cold", "Origin": "Official Regional Supplier"},
     "Tier 1 Sportwears Nike ($150 USD). Distinguish from Athleisure Nike Row 19 ($120 USD).", False, ""),

    (8, "Sportwears", "Uniqlo", 150, "VEL-SP-08", "Uniqlo U Premium Heavyweight Blocktech Set", "Sportswear",
     "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?auto=format&fit=crop&w=800&q=80",
     "Christophe Lemaire Parisian atelier design in water-repellent Blocktech bonded cotton with concealed storm placket.",
     {"Material": "Blocktech Bonded Cotton Twill", "Design": "Uniqlo U Atelier Paris", "Origin": "Supplier Network"},
     "Tier 1 Uniqlo ($150 USD). Distinguish from Uniquo Row 20 ($120 USD) & Casual Row 41 ($200 USD).", False, ""),

    (9, "Sportwears", "Adidas", 150, "VEL-SP-09", "Adidas Originals Trefoil Adicolor Heritage Tracksuit", "Sportswear",
     "https://images.unsplash.com/photo-1518002171953-a080ee817e1f?auto=format&fit=crop&w=800&q=80",
     "Glossy Tricot archival sportswear featuring signature 3-stripes down the sleeves and pants with ribbed funnel collar.",
     {"Fabric": "Primeblue Recycled Tricot", "Design": "Archive Beckenbauer Cut", "Origin": "Supplier Authorized Hub"},
     "Tier 1 Adidas Sportwears ($150 USD). Distinguish from Row 21 ($120 USD).", False, ""),

    (10, "Sportwears", "Bape", 200, "VEL-SP-10", "A Bathing Ape 1st Camo Shark Athletic Zip Jacket", "Sportswear",
     "https://images.unsplash.com/photo-1509631179647-0177331693ae?auto=format&fit=crop&w=800&q=80",
     "Legendary Harajuku streetwear staple in heavyweight Japanese cotton terry with full-zip hood shark face motif and Tokyo camo print.",
     {"Fabric": "100% Japanese Cotton Terry", "Graphics": "WGM Chenille Patch & Shark Face", "Origin": "Tokyo / Asian Sourcing Network"},
     "Tier 1 Bape Sportwears ($200 USD). Distinguish from Row 22 ($150 USD).", False, ""),

    (11, "Sportwears", "Balenciaga", 200, "VEL-SP-11", "Balenciaga Athletic Tracksuit Oversized Shell", "Sportswear",
     "https://images.unsplash.com/photo-1544441893-675973e31985?auto=format&fit=crop&w=800&q=80",
     "Exaggerated drop-shoulder silhouette in technical crinkled polyamide, featuring contrast piping and minimalist chest embroidery.",
     {"Material": "Technical Crinkled Polyamide", "Cut": "Balenciaga Signature Oversized", "Origin": "European Atelier Sourcing Hub"},
     "Tier 1 Balenciaga Sportwears ($200 USD). Preserved exact price.", False, ""),

    (12, "Sportwears", "Puma", 150, "VEL-SP-12", "Puma T7 Vintage Heritage Track Collection", "Sportswear",
     "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?auto=format&fit=crop&w=800&q=80",
     "Archival 7cm signature stripe inserts down arms and legs, rib-knit stand collar, and classic cat logo embroidery.",
     {"Fabric": "Double-Knit Polyester Blend", "Styling": "Retro 1968 Heritage Cut", "Origin": "Supplier Authorized Hub"},
     "Tier 1 Puma ($150 USD). Preserved exact price.", False, ""),

    (13, "Sportwears", "Prada", 250, "VEL-SP-13", "Prada Linea Rossa Technical Nylon Sport Jacket", "Sportswear",
     "https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=800&q=80",
     "High-performance Re-Nylon textile with heat-sealed seams, signature red latex Linea Rossa emblem on chest, and windproof hood.",
     {"Material": "Regenerated Nylon (Re-Nylon)", "Badge": "Linea Rossa Latex Emblem", "Origin": "Milan Sourcing Desk"},
     "Flagship high-tier Sportwears Prada ($250 USD). Highest price in sport tier.", False, ""),

    # 14-18 Hoodies
    (14, "Hoodies", "RL/Gucci", 200, "VEL-HD-14", "Ralph Lauren x Gucci Monogram Heritage Hoodie", "Hoodies",
     "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?auto=format&fit=crop&w=800&q=80",
     "Hybrid luxury curation combining classic Ivy League polo heritage with Florentine interlocking monogram detailing.",
     {"Material": "Heavyweight 450 GSM French Terry", "Details": "Gold-Tone Aglets & Embroidery", "Origin": "European Designer Sourcing"},
     "Listed as RL/Gucci in supplier sheet ($200 USD). Dual-brand reference.", False, ""),

    (15, "Hoodies", "Spider Hoodie", 150, "VEL-HD-15", "Sp5der Worldwide 555555 Angel Web Hoodie", "Hoodies",
     "https://images.unsplash.com/photo-1578587018452-892bacefd3f2?auto=format&fit=crop&w=800&q=80",
     "Viral Atlanta streetwear design featuring crystal rhinestone spider web motif, puff print lettering, and custom heavyweight fleece.",
     {"Fleece": "100% Cotton 400 GSM", "Print": "Multi-color Rhinestone & Puff Print", "Origin": "US Streetwear Hub"},
     "Tier 1 Spider Hoodie ($150 USD). Preserved exact price.", False, ""),

    (16, "Hoodies", "Denim Tears", 150, "VEL-HD-16", "Denim Tears The Cotton Wreath Emblem Hoodie", "Hoodies",
     "https://images.unsplash.com/photo-1509967419530-da38b4704bc6?auto=format&fit=crop&w=800&q=80",
     "Tremaine Emory signature graphic arrangement with all-over puff printed cotton wreaths across chest, hood, and sleeves.",
     {"Fleece": "Vintage Washed French Terry", "Applique": "3D Screenprinted Wreaths", "Origin": "Streetwear Sourcing Desk"},
     "Denim Tears ($150 USD). Preserved exact price.", False, ""),

    (17, "Hoodies", "Lacoste/ Prada", 200, "VEL-HD-17", "Lacoste x Prada Re-Edition Technical Zip Hoodie", "Hoodies",
     "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?auto=format&fit=crop&w=800&q=80",
     "Refined sportswear crossover combining French piqué cotton warmth with Italian technical nylon paneling.",
     {"Material": "Organic Piqué Cotton & Technical Nylon", "Emblem": "Dual Archival Badges", "Origin": "European Sourcing Network"},
     "Listed as Lacoste/ Prada in sheet ($200 USD). Dual-brand reference.", False, ""),

    (18, "Hoodies", "Essential Hoodie", 100, "VEL-HD-18", "Fear of God Essentials Core Pullover Hoodie", "Hoodies",
     "https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=800&q=80",
     "Relaxed dropped-shoulder boxy fit with rubberized ESSENTIALS logo on chest and signature rubber label on hood.",
     {"Fleece": "80% Cotton / 20% Polyester", "Fit": "Signature Oversized Boxy", "Origin": "Supplier Curated Stock"},
     "Essential Hoodie ($100 USD). Entry luxury tier in hoodie collection.", False, ""),

    # 19-25 Sportswear / Athleisure
    (19, "Sportswear / Athleisure", "Nike", 120, "VEL-SA-19", "Nike Dri-FIT Performance Track Athleisure Set", "Sportswear",
     "https://images.unsplash.com/photo-1539185441755-769473a23570?auto=format&fit=crop&w=800&q=80",
     "Moisture-wicking technical weave engineered for daily lifestyle comfort, athletic training, and airport travel.",
     {"Technology": "Nike Dri-FIT Advanced", "Cut": "Tapered Modern Athletic", "Origin": "Supplier Authorized Hub"},
     "Athleisure Nike Tier ($120 USD). Preserved exact sheet price.", False, ""),

    (20, "Sportswear / Athleisure", "Uniquo", 120, "VEL-SA-20", "Uniquo Airism Seamless Athleisure Set", "Sportswear",
     "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=800&q=80",
     "Ultra-lightweight cooling fabric with four-way stretch, quick-drying performance, and minimalist clean silhouette.",
     {"Fabric": "Breathable Microfiber Weave", "Weight": "Ultra-light", "Origin": "Supplier Network"},
     "Spelled 'Uniquo' in original supplier sheet ($120 USD). Flagged for spelling confirmation (Uniqlo variant).", True, "Spelled 'Uniquo' with a 'q' in original sheet. Preserved verbatim with flag for confirmation."),

    (21, "Sportswear / Athleisure", "Adidas", 120, "VEL-SA-21", "Adidas Tiro 24 Technical Athleisure Tracksuit", "Sportswear",
     "https://images.unsplash.com/photo-1518002171953-a080ee817e1f?auto=format&fit=crop&w=800&q=80",
     "AEROREADY moisture management with ankle zips for versatile wear and modern football-inspired silhouette.",
     {"Technology": "AEROREADY Moisture Absorption", "Inseam": "Tapered with Ankle Zips", "Origin": "Regional Supplier Network"},
     "Athleisure Adidas Tier ($120 USD). Preserved exact sheet price.", False, ""),

    (22, "Sportswear / Athleisure", "BAPE", 150, "VEL-SA-22", "A Bathing Ape College Graphic Athleisure Crew", "Sportswear",
     "https://images.unsplash.com/photo-1509631179647-0177331693ae?auto=format&fit=crop&w=800&q=80",
     "Ape Head collegiate chest graphic screenprinted on heavyweight loopback Japanese fleece with woven wrist tag.",
     {"Material": "100% Cotton Loopback", "Fit": "Standard Harajuku", "Origin": "Asian Sourcing Network"},
     "BAPE Athleisure Tier ($150 USD). Preserved exact sheet price.", False, ""),

    (23, "Sportswear / Athleisure", "Puma Lifestyle + Under Armour", 150, "VEL-SA-23", "Puma Lifestyle & Under Armour Technical Set", "Sportswear",
     "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?auto=format&fit=crop&w=800&q=80",
     "Dual-performance composite athleisure combining Puma lifestyle design with Under Armour ColdGear thermal fabric.",
     {"Fabric": "ColdGear Thermal Dual-Layer", "Properties": "4-Way Stretch Compression & Comfort", "Origin": "Supplier Curated Stock"},
     "Combined entry in supplier list: Puma Lifestyle + Under Armour ($150 USD).", False, ""),

    (24, "Sportswear / Athleisure", "Balenciaga", 200, "VEL-SA-24", "Balenciaga Distressed Athleisure Lounge Set", "Sportswear",
     "https://images.unsplash.com/photo-1544441893-675973e31985?auto=format&fit=crop&w=800&q=80",
     "Heavy vintage wash cotton with subtle raw edge fraying, relaxed drapey fit, and discreet monochromatic embroidery.",
     {"Material": "Pre-washed Vintage Cotton", "Finish": "Hand-Finished Distressing", "Origin": "European Atelier Sourcing"},
     "Balenciaga Athleisure Tier ($200 USD). Preserved exact price.", False, ""),

    (25, "Sportswear / Athleisure", "Prada", 200, "VEL-SA-25", "Prada Technical Gabardine Lounge Set", "Sportswear",
     "https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=800&q=80",
     "Tailored Italian nylon gabardine with stretch waistband, engraved silver-tone hardware, and enameled triangle plaque.",
     {"Material": "High-Density Nylon Gabardine", "Hardware": "Polished Nickel Pulls", "Origin": "Milan Sourcing Desk"},
     "Prada Athleisure Tier ($200 USD). Distinguish from Sportwears Row 13 ($250 USD).", False, ""),

    # 26-31 Luxury & Designer
    (26, "Luxury & Designer", "Ralph Lauren", 200, "VEL-LX-26", "Ralph Lauren Purple Label Cable Knit Sweater", "Luxury",
     "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?auto=format&fit=crop&w=800&q=80",
     "Pure Italian cashmere cable-knit featuring hand-linked seams, ribbed crew neckline, and subtle tonal pony embroidery.",
     {"Knit": "7-Gauge Italian Cashmere", "Care": "Dry Clean Only", "Origin": "Supplier Luxury Archive"},
     "Ralph Lauren Designer Collection ($200 USD). Preserved exact price.", False, ""),

    (27, "Luxury & Designer", "Gucci", 200, "VEL-LX-27", "Gucci GG Supreme Classic Jacquard Knit", "Luxury",
     "https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=800&q=80",
     "Fine wool jacquard knit decorated with the historic GG monogram in contrasting camel and ebony, finished with web trim.",
     {"Composition": "100% Fine Wool", "Pattern": "Allover Interlocking GG Jacquard", "Origin": "European Atelier Sourcing"},
     "Gucci Luxury Designer Collection ($200 USD). Preserved exact price.", False, ""),

    (28, "Luxury & Designer", "Tommy Hilfiger", 200, "VEL-LX-28", "Tommy Hilfiger Archive Colorblock Sailing Jacket", "Luxury",
     "https://images.unsplash.com/photo-1544441893-675973e31985?auto=format&fit=crop&w=800&q=80",
     "Retro 90s heritage colorblock design in water-resistant ripstop nylon with bold back crest and stowaway hood.",
     {"Shell": "Weatherproof Ripstop Nylon", "Lining": "Breathable Micro-Mesh", "Origin": "Supplier Curated Stock"},
     "Tommy Hilfiger Designer ($200 USD). Preserved exact price.", False, ""),

    (29, "Luxury & Designer", "Balenciaga", 200, "VEL-LX-29", "Balenciaga Paris Crest Signature Pullover", "Luxury",
     "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?auto=format&fit=crop&w=800&q=80",
     "Heavy fleece crewneck with embroidered vintage Paris crest on chest, drop shoulders, and washed vintage effect.",
     {"Fabric": "Heavyweight Organic Cotton Fleece", "Cut": "Cocoon Oversized", "Origin": "European Atelier Sourcing"},
     "Balenciaga Luxury & Designer ($200 USD). Preserved exact price.", False, ""),

    (30, "Luxury & Designer", "Lacoste", 200, "VEL-LX-30", "Lacoste Heritage Piqué Knit Classic Collection", "Luxury",
     "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?auto=format&fit=crop&w=800&q=80",
     "Signature Petit Piqué knit with mother-of-pearl buttons and embroidered green crocodile badge at the chest.",
     {"Knit": "100% Cotton Petit Piqué", "Buttons": "Genuine Mother-of-Pearl", "Origin": "French Sourcing Network"},
     "Lacoste Luxury Designer ($200 USD). Preserved exact price.", False, ""),

    (31, "Luxury & Designer", "Prada", 200, "VEL-LX-31", "Prada Milano Triangle Logo Tailored Knit", "Luxury",
     "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?auto=format&fit=crop&w=800&q=80",
     "Virgin wool crewneck knit with tonal enameled metal triangle logo applied at the nape of the neck.",
     {"Yarn": "100% Virgin Wool", "Plaque": "Enameled Metal Triangle", "Origin": "Milan Sourcing Desk"},
     "Prada Luxury & Designer ($200 USD). Preserved exact price.", False, ""),

    # 32-36 Streetwear / Urban Fashion
    (32, "Streetwear / Urban Fashion", "Supreme", 200, "VEL-ST-32", "Supreme Heavyweight Cross Box Logo Pullover", "Streetwear",
     "https://images.unsplash.com/photo-1552374196-1ab2a1c593e8?auto=format&fit=crop&w=800&q=80",
     "Dense cross-grain fleece constructed in Canada with iconic embroidered box logo graphic and kangaroo pouch pocket.",
     {"Weight": "500 GSM Cross-Grain Fleece", "Details": "Ribbed Gusset Side Panels", "Origin": "NYC / Supplier Vault"},
     "Supreme Streetwear ($200 USD). Preserved exact price.", False, ""),

    (33, "Streetwear / Urban Fashion", "Fear of God", 200, "VEL-ST-33", "Fear of God Mainline Seventh Collection Henley", "Streetwear",
     "https://images.unsplash.com/photo-1509967419530-da38b4704bc6?auto=format&fit=crop&w=800&q=80",
     "Jerry Lorenzo masterwork tailoring blending American workwear elegance with luxury Italian textiles and horn buttons.",
     {"Fabric": "Washed Vintage Cotton Twill", "Closure": "Engraved Horn Buttons", "Origin": "LA / Milan Sourcing Desk"},
     "Fear of God Mainline ($200 USD). Preserved exact price.", False, ""),

    (34, "Streetwear / Urban Fashion", "Off-White", 200, "VEL-ST-34", "Off-White Industrial Diag Stencil Pullover", "Streetwear",
     "https://images.unsplash.com/photo-1509631179647-0177331693ae?auto=format&fit=crop&w=800&q=80",
     "Virgil Abloh design language featuring signature spray stencil diagonal stripes down the sleeves and back arrows.",
     {"Fleece": "100% French Terry Cotton", "Graphics": "Screenprinted Industrial Diag & Arrows", "Origin": "European Atelier Sourcing"},
     "Off-White Streetwear ($200 USD). Preserved exact price.", False, ""),

    (35, "Streetwear / Urban Fashion", "Essentials", 200, "VEL-ST-35", "Essentials Fear of God Heavyweight Knit Capsule", "Streetwear",
     "https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=800&q=80",
     "Chunky knit silhouette with intarsia ESSENTIALS logo across the front, raglan sleeves, and relaxed ribbed hem.",
     {"Knit": "Heavy Cotton-Blend Yarn", "Fit": "Relaxed Modern Drop", "Origin": "Supplier Curated Stock"},
     "Essentials Streetwear Tier ($200 USD). Preserved exact price.", False, ""),

    (36, "Streetwear / Urban Fashion", "Stüssy", 200, "VEL-ST-36", "Stüssy 8-Ball Mohair Cardigan / Streetwear", "Streetwear",
     "https://images.unsplash.com/photo-1578587018452-892bacefd3f2?auto=format&fit=crop&w=800&q=80",
     "Cozy brushed mohair-blend knit with huge jacquard 8-Ball emblem on the back, pearlized buttons, and relaxed silhouette.",
     {"Yarn": "Brushed Mohair & Wool Blend", "Buttons": "Horn Pattern Acetate", "Origin": "California / Tokyo Sourcing Desk"},
     "Stüssy Streetwear ($200 USD). Preserved exact price.", False, ""),

    # 37-41 Casual / Lifestyle Brands
    (37, "Casual / Lifestyle Brands", "Zara", 200, "VEL-CS-37", "Zara Premium Studio Capsule Overcoat", "Casual",
     "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=800&q=80",
     "Limited-edition Studio Collection crafted in textured Manteco wool with structured shoulders and double-breasted closure.",
     {"Wool": "Italian Manteco Wool Blend", "Lining": "Viscose Satin", "Origin": "European Sourcing Hub"},
     "Zara Premium Collection ($200 USD). Preserved exact price.", False, ""),

    (38, "Casual / Lifestyle Brands", "ASOS", 200, "VEL-CS-38", "ASOS Design White Label Structured Tailoring", "Casual",
     "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=800&q=80",
     "Architectural tailored blazer and trouser coordinate in heavy twill, featuring clean peak lapels and horn buttons.",
     {"Fabric": "Dense Suiting Twill", "Styling": "Modern Wide-Leg & Boxy Blazer", "Origin": "UK Supplier Network"},
     "ASOS Casual / Lifestyle ($200 USD). Preserved exact price.", False, ""),

    (39, "Casual / Lifestyle Brands", "H&M", 200, "VEL-CS-39", "H&M Studio Edition Monochromatic Trench", "Casual",
     "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?auto=format&fit=crop&w=800&q=80",
     "High-end runway showcase edition trench coat in crisp water-repellent gabardine with oversized storm flaps and buckle belt.",
     {"Fabric": "Heavy Water-Repellent Cotton Gabardine", "Details": "Tortoiseshell Buckles", "Origin": "Stockholm / European Sourcing"},
     "H&M Studio Collection ($200 USD). Preserved exact price.", False, ""),

    (40, "Casual / Lifestyle Brands", "Fashion Nova", 200, "VEL-CS-40", "Fashion Nova Luxe Statement Evening Silhouette", "Casual",
     "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=800&q=80",
     "Dramatic floor-length structured gown with high-compression boning, draped satin finish, and asymmetric neckline.",
     {"Fabric": "Stretch Satin & Boned Bodice", "Occasion": "Black Tie & Gala", "Origin": "Supplier Curated Stock"},
     "Fashion Nova Luxe ($200 USD). Preserved exact price.", False, ""),

    (41, "Casual / Lifestyle Brands", "Uniqlo", 200, "VEL-CS-41", "Uniqlo +J Jil Sander Tailored Wool Overcoat", "Casual",
     "https://images.unsplash.com/photo-1544441893-675973e31985?auto=format&fit=crop&w=800&q=80",
     "Iconic +J collaboration design showcasing razor-sharp minimalist German tailoring in pure Nikke wool melton.",
     {"Fabric": "100% Japanese Wool Melton", "Design": "+J Jil Sander Collaboration", "Origin": "Supplier Authorized Hub"},
     "Uniqlo Casual Tier ($200 USD). Distinguish from Row 8 ($150 USD) & Row 20 ($120 USD).", False, ""),

    # 42-49 Electronics & Accessories (Second Tier)
    (42, "Electronics & Accessories", "JBL Speakers", 120, "VEL-EA-42", "JBL Flip 6 Compact Waterproof Bluetooth Speaker", "Electronics",
     "https://images.unsplash.com/photo-1545454675-3531b543be5d?auto=format&fit=crop&w=800&q=80",
     "Compact 2-way speaker system delivering crystal highs and deep bass with PartyBoost multi-speaker linking and IP67 rating.",
     {"System": "2-way speaker system with separate tweeter", "Battery": "12 Hours Playtime", "Origin": "Supplier Authorized Hub"},
     "Tier 2 JBL Speakers ($120 USD). Distinguish from Row 1 ($150 USD).", False, ""),

    (43, "Electronics & Accessories", "AirPods", 150, "VEL-EA-43", "AirPods True Wireless Earbuds with Lightning Case", "Electronics",
     "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?auto=format&fit=crop&w=800&q=80",
     "Seamless optical sensors and motion accelerometers with automatic play/pause, Siri voice commands, and quick charge case.",
     {"Chip": "H1 Headphone Chip", "Total Battery": "Over 24 Hours with Case", "Origin": "Supplier Authorized Hub"},
     "Standard AirPods ($150 USD). Distinguish from AirPods Pro (Row 2).", False, ""),

    (44, "Electronics & Accessories", "Dyson Pure Hot+Cool", 100, "VEL-EA-44", "Dyson Pure Hot+Cool Air Purifier & Heater Fan", "Electronics",
     "https://images.unsplash.com/photo-1585338107529-13afc5f02586?auto=format&fit=crop&w=800&q=80",
     "Triple-function HEPA air purifier, personal heating, and cooling fan equipped with Air Multiplier technology.",
     {"Filtration": "Fully Sealed HEPA H13 Filter", "Coverage": "Whole Room Air Circulation", "Origin": "Supplier Authorized Hub"},
     "Dyson Pure Hot+Cool ($100 USD). Preserved exact supplier price.", False, ""),

    (45, "Electronics & Accessories", "Dyson V11", 100, "VEL-EA-45", "Dyson V11 Cordless Vacuum Cleaner System", "Electronics",
     "https://images.unsplash.com/photo-1558317374-067fb5f30001?auto=format&fit=crop&w=800&q=80",
     "High-torque motorhead with Dynamic Load Sensor (DLS) intelligence that auto-adapts suction between carpets and hard floors.",
     {"Motor": "Dyson Hyperdymium Motor (125,000 RPM)", "Run Time": "Up to 60 Minutes", "Origin": "Supplier Authorized Hub"},
     "Dyson V11 ($100 USD). Preserved exact supplier price.", False, ""),

    (46, "Electronics & Accessories", "Smart Watches", 100, "VEL-EA-46", "Precision Smart Watch Activity & Health Tracker", "Electronics",
     "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?auto=format&fit=crop&w=800&q=80",
     "Sleek curved AMOLED touchscreen display with sleep staging analysis, ECG biometric heart-rate sensor, and NFC payments.",
     {"Screen": "1.78 inch HD AMOLED", "Battery": "Up to 7 Days Typical Use", "Origin": "Supplier Verified Hub"},
     "Tier 2 Smart Watches ($100 USD). Preserved exact price.", False, ""),

    (47, "Electronics & Accessories", "Headphones", 100, "VEL-EA-47", "Studio Wireless ANC Over-Ear Headphones", "Electronics",
     "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=800&q=80",
     "Custom 40mm titanium diaphragm drivers with active noise cancellation, plush memory foam protein ear cushions, and 40h battery.",
     {"Diaphragm": "40mm Custom Titanium Drivers", "Battery": "40 Hours Playback", "Origin": "Supplier Authorized Hub"},
     "Studio Headphones ($100 USD). Preserved exact price.", False, ""),

    (48, "Electronics & Accessories", "Sneakers", 100, "VEL-EA-48", "Minimalist Urban Runner Sneakers", "Footwear",
     "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?auto=format&fit=crop&w=800&q=80",
     "Monochromatic daily runner with responsive EVA cushioning, breathable knit sock upper, and durable traction outsole.",
     {"Upper": "Engineered Breathable Knit", "Cushioning": "Responsive EVA Foam", "Origin": "Supplier Curated Stock"},
     "Tier 2 Sneakers listed under Electronics & Accessories ($100 USD). Distinguish from Row 5 ($150 USD).", True, "Categorized under Electronics in sheet; verify apparel mapping."),

    (49, "Electronics & Accessories", "Spider Hoodies", 150, "VEL-EA-49", "Sp5der Web Punk Edition Heavyweight Fleece", "Hoodies",
     "https://images.unsplash.com/photo-1578587018452-892bacefd3f2?auto=format&fit=crop&w=800&q=80",
     "Cobweb graphic hoodie with contrast rhinestone highlights and signature Young Thug streetwear aesthetic.",
     {"Fleece": "Heavyweight 400 GSM Cotton", "Print": "Screenprinted Web & Crystal Rhinestones", "Origin": "US Streetwear Hub"},
     "Spider Hoodies listed under Electronics & Accessories in sheet ($150 USD). Distinguish from Row 15.", True, "Categorized under Electronics in original sheet; cross-referenced with Hoodies section."),

    # 50-55 Colognes
    (50, "Colognes", "Toscano Leather", 150, "VEL-CL-50", "Maison Alhambra Toscano Leather Eau de Parfum", "Colognes",
     "https://images.unsplash.com/photo-1523293182086-7651a899d37f?auto=format&fit=crop&w=800&q=80",
     "Opulent unisex leather fragrance opening with raspberry and saffron, developing into rich thyme, olibanum, and suede.",
     {"Top Notes": "Saffron, Raspberry, Thyme", "Heart Notes": "Olibanum, Night Blooming Jasmine", "Base": "Black Leather, Suede, Amberwood", "Volume": "80ml / 2.7 fl oz"},
     "Toscano Leather ($150 USD). Preserved exact supplier price.", False, ""),

    (51, "Colognes", "Stronger With You", 200, "VEL-CL-51", "Emporio Armani Stronger With You Intensely Pour Homme", "Colognes",
     "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?auto=format&fit=crop&w=800&q=80",
     "Addictive oriental fougère fragrance opening with spicy pink pepper and violet, layered over sweet toffee and bourbon vanilla.",
     {"Top Notes": "Pink Pepper, Juniper Essence", "Heart Notes": "Lavender, Sage, Toffee Accord", "Base": "Bourbon Vanilla, Amber, Suede", "Volume": "100ml / 3.4 fl oz"},
     "Stronger With You ($200 USD). Preserved exact supplier price.", False, ""),

    (52, "Colognes", "Bleu de Chanel", 200, "VEL-CL-52", "Chanel Bleu de Chanel Eau de Parfum", "Colognes",
     "https://images.unsplash.com/photo-1588405748880-12d1d2a59f75?auto=format&fit=crop&w=800&q=80",
     "Tribute to masculine freedom in an aromatic-woody fragrance with a captivating trail of New Caledonian sandalwood.",
     {"Top Notes": "Grapefruit, Lemon, Mint, Pink Pepper", "Heart Notes": "Ginger, Nutmeg, Jasmine, Iso E Super", "Base": "Incense, Vetiver, Cedar, Sandalwood", "Volume": "100ml / 3.4 fl oz"},
     "Bleu de Chanel ($200 USD). Preserved exact supplier price.", False, ""),

    (53, "Colognes", "Valentino", 200, "VEL-CL-53", "Valentino Born In Roma Uomo Intense", "Colognes",
     "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=800&q=80",
     "Rockstud-studded bottle encapsulating vibrant bourbon vanilla infused with amber accords and smoked vetiver.",
     {"Top Notes": "Bourbon Vanilla Infusion", "Heart Notes": "Lavandin Accord", "Base": "Smoked Vetiver Extract", "Volume": "100ml / 3.4 fl oz"},
     "Valentino Born In Roma ($200 USD). Preserved exact supplier price.", False, ""),

    (54, "Colognes", "Sauvage", 200, "VEL-CL-54", "Dior Sauvage Eau de Parfum", "Colognes",
     "https://images.unsplash.com/photo-1547887537-6158d64c35b3?auto=format&fit=crop&w=800&q=80",
     "Francois Demachy creation inspired by the desert at twilight, fusing juicy Calabrian bergamot with Papua New Guinean vanilla absolute.",
     {"Top Notes": "Calabrian Bergamot, Pepper", "Heart Notes": "Sichuan Pepper, Lavender, Star Anise, Nutmeg", "Base": "Ambroxan, Papua New Guinean Vanilla", "Volume": "100ml / 3.4 fl oz"},
     "Dior Sauvage ($200 USD). Preserved exact supplier price.", False, ""),

    (55, "Colognes", "Myslf", 200, "VEL-CL-55", "Yves Saint Laurent MYSLF Eau de Parfum", "Colognes",
     "https://images.unsplash.com/photo-1523293182086-7651a899d37f?auto=format&fit=crop&w=800&q=80",
     "Woody-floral statement scent contrasting sparkling Calabrian bergamot with raw orange blossom heart and sensual Indonesian patchouli.",
     {"Top Notes": "Calabrian Bergamot & Vert de Bergamot", "Heart Notes": "Tunisian Orange Blossom Absolute", "Base": "Ambrofix & Indonesian Patchouli Heart", "Volume": "100ml / 3.4 fl oz"},
     "YSL Myslf ($200 USD). Preserved exact supplier price.", False, "")
]

for row in raw_data:
    r_num, s_cat, s_item, price, sku, name, group, img, desc, specs, notes, flagged, flag_reason = row
    products.append({
        "id": sku,
        "row": r_num,
        "supplierCategory": s_cat,
        "supplierItem": s_item,
        "numericPrice": price,
        "currency": "USD",
        "priceFormatted": f"${price} USD",
        "name": name,
        "group": group,
        "image": img,
        "gallery": [img],
        "description": desc,
        "specifications": specs,
        "notes": notes,
        "flagged": flagged,
        "flagReason": flag_reason,
        "status": "Available on Enquiry",
        "approved": True
    })

js_content = "window.VELORA_PRODUCTS = " + json.dumps(products, indent=2) + ";\n"

with open(r"c:\Users\fazsa\OneDrive\Desktop\Velora\products-data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated products-data.js successfully with {len(products)} products!")
