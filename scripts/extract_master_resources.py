# -*- coding: utf-8 -*-
"""
Extract flashcards, top 52 data management tools, GTK tools, and modules from master sources.
"""
import json
import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
master_html = os.path.join(os.path.dirname(base_dir), 'ArcGIS_Pro_Associate_2025_Master', 'ArcGIS_Pro_Associate_2025_Simulator (2).html')
modules_src = os.path.join(os.path.dirname(base_dir), 'modules_data.json')

with open(master_html, 'r', encoding='utf-8') as f:
    html_text = f.read()

# 1. Extract Flashcards
print("Extracting 100 Flashcards...")
m_fc = re.search(r'const\s+FLASHCARDS\s*=\s*(\[.*?\]);', html_text, re.DOTALL)
if m_fc:
    flashcards = json.loads(m_fc.group(1))
    print(f"Loaded {len(flashcards)} flashcards.")
    fc_path = os.path.join(base_dir, 'public', 'data', 'references', 'flashcards.json')
    os.makedirs(os.path.dirname(fc_path), exist_ok=True)
    with open(fc_path, 'w', encoding='utf-8') as f:
        json.dump(flashcards, f, ensure_ascii=False, indent=2)
    print("Saved public/data/references/flashcards.json")

# 2. Extract 52 Data Management Tools
print("Extracting Data Management Tools...")
dm_section_start = html_text.find('id="dm-tools-grid"')
dm_section_end = html_text.find('<!-- 4C. APPLIED GEOPROCESSING', dm_section_start)
if dm_section_end == -1:
    dm_section_end = html_text.find('id="gtk-tools-section"', dm_section_start)

dm_cards_html = html_text[dm_section_start:dm_section_end]
tool_card_blocks = dm_cards_html.split('<div class="tool-card')
dm_tools = []

for block in tool_card_blocks[1:]:
    # Extract details
    category_m = re.search(r'<span class="text-\[10px\][^>]*>([^<]+)</span>', block)
    title_m = re.search(r'<h4 class="text-base[^>]*>([^<]+)</h4>', block)
    title_ar_m = re.search(r'<span class="text-xs[^>]*font-arabic"[^>]*>([^<]+)</span>', block)
    url_m = re.search(r'<a href="([^"]+)"[^>]*title="Open Official Esri Documentation"', block)
    arcpy_m = re.search(r'<code>(arcpy\.[^<]+)</code>', block)
    ui_m = re.search(r'<strong class="text-slate-300">UI Path:</strong>\s*<code[^>]*>([^<]+)</code>', block)
    en_desc_m = re.search(r'<p class="[^"]*lang-text-en">([^<]+)</p>', block)
    ar_desc_m = re.search(r'<p class="[^"]*lang-text-ar[^"]*"[^>]*>([^<]+)</p>', block)
    trap_en_m = re.search(r'<span class="text-amber-400 font-bold">Exam Trap:</span>\s*([^<]+)</div>', block)
    trap_ar_m = re.search(r'<span class="text-amber-400 font-bold font-arabic">فخ الاختبار:</span>\s*([^<]+)</div>', block)

    tool_item = {
        "id": f"DM-T-{len(dm_tools)+1:03d}",
        "category": category_m.group(1).strip() if category_m else "Data Management",
        "name": title_m.group(1).strip() if title_m else "Tool",
        "name_ar": title_ar_m.group(1).strip() if title_ar_m else "",
        "doc_url": url_m.group(1).strip() if url_m else "https://pro.arcgis.com",
        "arcpy_syntax": arcpy_m.group(1).strip() if arcpy_m else "",
        "ui_path": ui_m.group(1).strip() if ui_m else "",
        "description": {
            "en": en_desc_m.group(1).strip() if en_desc_m else "",
            "ar": ar_desc_m.group(1).strip() if ar_desc_m else ""
        },
        "exam_trap": {
            "en": trap_en_m.group(1).strip() if trap_en_m else "",
            "ar": trap_ar_m.group(1).strip() if trap_ar_m else ""
        }
    }
    dm_tools.append(tool_item)

print(f"Extracted {len(dm_tools)} Data Management Tools.")
dm_tools_path = os.path.join(base_dir, 'public', 'data', 'references', 'data-management-tools.json')
with open(dm_tools_path, 'w', encoding='utf-8') as f:
    json.dump(dm_tools, f, ensure_ascii=False, indent=2)
print("Saved public/data/references/data-management-tools.json")

# 3. Extract Applied GTK Pro 3.2 Tools
print("Extracting GTK Tools...")
gtk_start = html_text.find('id="gtk-tools-grid"')
gtk_end = html_text.find('<!-- 4D. DECISION MATRICES', gtk_start)
if gtk_end == -1:
    gtk_end = html_text.find('id="decision-matrices-section"', gtk_start)
if gtk_end == -1:
    gtk_end = len(html_text)

gtk_cards_html = html_text[gtk_start:gtk_end]
gtk_blocks = gtk_cards_html.split('<div class="tool-card')
gtk_tools = []

for block in gtk_blocks[1:]:
    category_m = re.search(r'<span class="text-\[10px\][^>]*>([^<]+)</span>', block)
    title_m = re.search(r'<h4 class="text-base[^>]*>([^<]+)</h4>', block)
    title_ar_m = re.search(r'<span class="text-xs[^>]*font-arabic"[^>]*>([^<]+)</span>', block)
    url_m = re.search(r'<a href="([^"]+)"', block)
    arcpy_m = re.search(r'<code>(arcpy\.[^<]+)</code>', block)
    ui_m = re.search(r'<strong class="text-slate-300">UI Path:</strong>\s*<code[^>]*>([^<]+)</code>', block)
    en_desc_m = re.search(r'<p class="[^"]*lang-text-en">([^<]+)</p>', block)
    ar_desc_m = re.search(r'<p class="[^"]*lang-text-ar[^"]*"[^>]*>([^<]+)</p>', block)
    trap_en_m = re.search(r'<span class="text-amber-400 font-bold">Exam Trap:</span>\s*([^<]+)</div>', block)
    trap_ar_m = re.search(r'<span class="text-amber-400 font-bold font-arabic">فخ الاختبار:</span>\s*([^<]+)</div>', block)

    tool_item = {
        "id": f"GTK-T-{len(gtk_tools)+1:03d}",
        "category": category_m.group(1).strip() if category_m else "Analysis",
        "name": title_m.group(1).strip() if title_m else "Tool",
        "name_ar": title_ar_m.group(1).strip() if title_ar_m else "",
        "doc_url": url_m.group(1).strip() if url_m else "https://pro.arcgis.com",
        "arcpy_syntax": arcpy_m.group(1).strip() if arcpy_m else "",
        "ui_path": ui_m.group(1).strip() if ui_m else "",
        "description": {
            "en": en_desc_m.group(1).strip() if en_desc_m else "",
            "ar": ar_desc_m.group(1).strip() if ar_desc_m else ""
        },
        "exam_trap": {
            "en": trap_en_m.group(1).strip() if trap_en_m else "",
            "ar": trap_ar_m.group(1).strip() if trap_ar_m else ""
        }
    }
    gtk_tools.append(tool_item)

print(f"Extracted {len(gtk_tools)} GTK Applied Tools.")
gtk_tools_path = os.path.join(base_dir, 'public', 'data', 'references', 'gtk-tools.json')
with open(gtk_tools_path, 'w', encoding='utf-8') as f:
    json.dump(gtk_tools, f, ensure_ascii=False, indent=2)
print("Saved public/data/references/gtk-tools.json")

# 4. Save Modules into public/data/modules/modules.json
print("Processing Learning Modules...")
with open(modules_src, 'r', encoding='utf-8') as f:
    modules_data = json.load(f)

# Also ensure each module references official doc links
official_hubs = [
    {"title": "Get Started with ArcGIS Pro", "url": "https://pro.arcgis.com/en/pro-app/latest/get-started/introducing-arcgis-pro.htm", "kind": "official"},
    {"title": "ArcGIS Pro App Help", "url": "https://pro.arcgis.com/en/pro-app/latest/help/main/welcome-to-the-arcgis-pro-app-help.htm", "kind": "official"},
    {"title": "ArcGIS Pro Tool Reference", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/main/arcgis-pro-tool-reference.htm", "kind": "official"},
    {"title": "ArcPy Reference", "url": "https://pro.arcgis.com/en/pro-app/latest/arcpy/main/arcgis-pro-arcpy-reference.htm", "kind": "official"}
]

for m in modules_data:
    m["doc_hubs"] = official_hubs

modules_out = os.path.join(base_dir, 'public', 'data', 'modules', 'modules.json')
os.makedirs(os.path.dirname(modules_out), exist_ok=True)
with open(modules_out, 'w', encoding='utf-8') as f:
    json.dump(modules_data, f, ensure_ascii=False, indent=2)
print(f"Saved {len(modules_data)} modules to public/data/modules/modules.json")

print("All master resources extracted successfully!")

