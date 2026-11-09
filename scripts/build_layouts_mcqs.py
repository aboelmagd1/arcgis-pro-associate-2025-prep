# -*- coding: utf-8 -*-
"""
Build all 45 Layouts & Sharing MCQs (LS-001 through LS-045) for EAPA_2025.
"""
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_file = os.path.join(base_dir, 'public', 'data', 'questions', 'layouts-sharing.json')

ref_map = {
    "layouts": {"title": "Layouts in ArcGIS Pro, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/layouts/layouts-in-arcgis-pro.htm", "kind": "official"},
    "mapseries": {"title": "Map series, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/layouts/map-series.htm", "kind": "official"},
    "packages": {"title": "Sharing packages, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/sharing/overview/sharing-packages.htm", "kind": "official"},
    "weblayers": {"title": "Share a web layer, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/sharing/overview/share-a-web-layer.htm", "kind": "official"},
    "exporting": {"title": "Export a map or layout, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/layouts/export-a-map-or-layout.htm", "kind": "official"}
}

def make_q(qid, objective, diff, qtype, tools, q_en, q_ar, opts, ans, exp_en, exp_ar, why_wrong, ref_key):
    return {
        "id": qid,
        "kind": "mcq",
        "domain": "Layouts and Sharing",
        "objective": objective,
        "difficulty": diff,
        "type": qtype,
        "tools": tools,
        "question": {"en": q_en, "ar": q_ar},
        "options": [
            {"id": "A", "text": {"en": opts[0][0], "ar": opts[0][1]}},
            {"id": "B", "text": {"en": opts[1][0], "ar": opts[1][1]}},
            {"id": "C", "text": {"en": opts[2][0], "ar": opts[2][1]}},
            {"id": "D", "text": {"en": opts[3][0], "ar": opts[3][1]}}
        ],
        "correctAnswer": ans,
        "explanation": {"en": exp_en, "ar": exp_ar},
        "incorrectOptionsExplanation": {
            "en": {k: v[0] for k, v in why_wrong.items()},
            "ar": {k: v[1] for k, v in why_wrong.items()}
        },
        "references": [ref_map[ref_key]]
    }

questions = []

# LS-001 to LS-045: 45 high-caliber bilingual questions
ls_data = [
    # 1: Map Series definition
    (
        "Determine how to create and manage map layouts and map series", "Beginner", "Conceptual", ["Spatial Map Series"],
        "What is the primary purpose of creating a Spatial Map Series in an ArcGIS Pro page layout?",
        "ما هو الغرض الأساسي من إنشاء سلسلة خرائط مكانية (Spatial Map Series) في لوحة إخراج بـ ArcGIS Pro؟",
        [["To automate the generation of a multi-page map book from a single layout using features from an index layer", "أتمتة إنتاج أطلس خرائط متعدد الصفحات من لوحة إخراج واحدة بالاعتماد على معالم طبقة الفهرس"], ["To convert 2D maps into 3D animations", "تحويل الخرائط ثنائية الأبعاد إلى رسوم متحركة ثلاثية الأبعاد"], ["To compress raster images into JPEG format", "ضغط صور الراستر إلى صيغة JPEG"], ["To create database backups on a schedule", "إنشاء نسخ احتياطية لقاعدة البيانات وفق جدول زمني"]],
        "A",
        "A Spatial Map Series uses a single layout and iterates across individual features in an index layer (e.g. parcels, grid cells, counties) to produce a standardized, multi-page map book.",
        "تستخدم سلسلة الخرائط المكانية لوحة إخراج واحدة وتتنقل عبر معالم طبقة الفهرس (مثل قطع الأراضي أو شبكات التوزيع أو المحافظات) لإنتاج أطلس خرائط معياري موحد متعدد الصفحات.",
        {"B": ["Map series generate static multi-page layouts, not 3D video animations.", "تنتج سلاسل الخرائط لوحات طباعة وليس رسوم فيديو متحركة."], "C": ["Image compression is managed in export formats, not map series.", "ضغط الصور يُدار في صيغ التصدير."], "D": ["Database backups are administrative DBMS operations.", "النسخ الاحتياطي عملية إدارية لخوادم قواعد البيانات."]},
        "mapseries"
    ),
    # 2: Map Series Requirements
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Technical", ["Spatial Map Series"],
        "Which two elements are strictly required to configure a Spatial Map Series in ArcGIS Pro?",
        "ما هما العنصران الإلزاميان تماماً لتهيئة سلسلة خرائط مكانية (Spatial Map Series) في ArcGIS Pro؟",
        [["A Map Frame and an Index Layer", "إطار خريطة (Map Frame) وطبقة فهرس (Index Layer)"], ["A Scale Bar and a North Arrow", "شريط مقياس وسهم شمال"], ["A 3D Local Scene and an elevation surface", "مشهد محلي ثلاثي الأبعاد وسطح ارتفاع"], ["A Python script and an Excel table", "سكربت بايثون وجدول إكسل"]],
        "A",
        "A Spatial Map Series requires a Layout Map Frame (which displays the map) and an Index Layer (a polygon or polyline layer whose features define the extent and center of each page).",
        "تتطلب سلسلة الخرائط المكانية وجود إطار خريطة (Map Frame) لعرض الخريطة وطبقة فهرس (Index Layer) تحدد معالمها نطاق ومركز كل صفحة في الأطلس.",
        {"B": ["Scale bars and north arrows are optional decorative layout elements.", "أشرطة المقاييس وأسهم الشمال عناصر تصميم اختيارية وليست إلزامية لتشغيل السلسلة."], "C": ["Map series operate on 2D map frames in layouts.", "تعمل سلاسل الخرائط على إطارات الخرائط ثنائية الأبعاد."], "D": ["No programming or external spreadsheets are required.", "لا تتطلب السلسلة برمجة أو جداول خارجية."]},
        "mapseries"
    ),
    # 3: Dynamic Text Tags
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Technical", ["Dynamic Text"],
        "Which dynamic text tag in a Map Series layout dynamically displays the current page number and total page count (e.g., 'Page 3 of 50')?",
        "أي وسم نص ديناميكي (Dynamic Text) في لوحة سلسلة الخرائط يعرض ديناميكياً رقم الصفحة الحالية وإجمالي عدد الصفحات (مثل: 'Page 3 of 50')؟",
        [["Page <dyn type=\"page\" property=\"number\"/> of <dyn type=\"page\" property=\"count\"/>", "Page <dyn type=\"page\" property=\"number\"/> of <dyn type=\"page\" property=\"count\"/>"], ["Page $PAGE of $TOTAL", "Page $PAGE of $TOTAL"], ["Page %PageNumber% of %TotalPages%", "Page %PageNumber% of %TotalPages%"], ["Page {PAGE_NUM} OF {PAGES}", "Page {PAGE_NUM} OF {PAGES}"]],
        "A",
        "ArcGIS Pro dynamic text uses XML-formatted tags, where `<dyn type=\"page\" property=\"number\"/>` evaluates to the current page number and property=\"count\" evaluates to total pages.",
        "تستخدم النصوص الديناميكية في ArcGIS Pro وسوماً بصيغة XML؛ حيث يعيد الوسم `<dyn type=\"page\" property=\"number\"/>` رقم الصفحة الحالية و property=\"count\" إجمالي الصفحات.",
        {"B": ["Dollar signs are used in Arcade, not layout dynamic text tags.", "علامات الدولار للغة Arcade وليست لوسوم النصوص الديناميكية."], "C": ["Percent signs are ModelBuilder inline variables.", "علامات النسبة المئوية لمتغيرات ModelBuilder."], "D": ["Curly brackets are Python string formatting syntax.", "الأقواس المعقوفة لتنسيق سلاسل بايثون."]},
        "mapseries"
    ),
    # 4: Dynamic text attribute extraction
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Technical", ["Dynamic Text"],
        "How can an analyst dynamically display the value of the 'DISTRICT_LEADER' field from the active index layer feature on each page of a Map Series?",
        "كيف يمكن للمحلل عرض قيمة حقل 'DISTRICT_LEADER' ديناميكياً من معلم طبقة الفهرس النشط في كل صفحة من صفحات سلسلة الخرائط؟",
        [["Insert dynamic text: <dyn type=\"page\" property=\"attribute\" field=\"DISTRICT_LEADER\"/>", "إدراج نص ديناميكي: <dyn type=\"page\" property=\"attribute\" field=\"DISTRICT_LEADER\"/>"], ["Type the name manually 50 times on separate text boxes", "كتابة الاسم يدوياً 50 مرة في مربعات نصية منفصلة"], ["Export the layer to a shapefile", "تصدير الطبقة إلى shapefile"], ["Run the Calculate Field geoprocessing tool", "تشغيل أداة Calculate Field"]],
        "A",
        "The dynamic text attribute tag extracts and displays attribute values directly from the current page's index feature using the syntax `<dyn type=\"page\" property=\"attribute\" field=\"FieldName\"/>`.",
        "يستخرج وسم سمة النص الديناميكي ويعرض القيم السماتية مباشرة من معلم الفهرس للصفحة الحالية باستخدام الصياغة المعيارية `<dyn type=\"page\" property=\"attribute\" field=\"اسم الحقل\"/>`.",
        {"B": ["Manual typing defeats the automation purpose of map series.", "الكتابة اليدوية تلغي الفائدة من أتمتة السلسلة."], "C": ["Exporting to shapefile does not display text on layouts.", "تصدير الملف لا يظهر النصوص على اللوحة."], "D": ["Calculate field edits table records, not layout dynamic text.", "حساب الحقل يعدل الجداول ولا يغير نصوص اللوحة."]},
        "mapseries"
    ),
    # 5: Project Package (.ppkx)
    (
        "Choose how to share content from ArcGIS Pro", "Beginner", "Conceptual", ["Sharing Packages"],
        "Which sharing package encapsulates an entire ArcGIS Pro project—including all maps, scenes, layouts, custom toolboxes, styles, and a consolidated geodatabase of all underlying data?",
        "أي حزمة مشاركة تجمع مشروع ArcGIS Pro بأكمله—بما في ذلك كافة الخرائط والمشاهد واللوحات وصناديق الأدوات المخصصة والأنماط مع قاعدة بيانات مجمعة لكافة البيانات الأصلية؟",
        [["Project Package (.ppkx)", "حزمة المشروع Project Package (.ppkx)"], ["Layer Package (.lpkx)", "حزمة الطبقة Layer Package (.lpkx)"], ["Map Package (.mpkx)", "حزمة الخريطة Map Package (.mpkx)"], ["Tile Package (.tpkx)", "حزمة البلاطات Tile Package (.tpkx)"]],
        "A",
        "A Project Package (.ppkx) packages everything within an ArcGIS Pro project into a single compressed file, consolidating referenced data so external recipients can open the project without broken data paths.",
        "تجمع حزمة المشروع (.ppkx) كافة عناصر المشروع داخل ملف مضغوط واحد، وتدمج البيانات المرجعية في قاعدة بيانات جغرافية مجمعة لتمكين المستلمين من فتح المشروع دون انقطاع مسارات البيانات.",
        {"B": ["Layer Package (.lpkx) bundles only a single layer or group layer.", "حزمة الطبقة (.lpkx) تجمع طبقة واحدة أو مجموعة طبقات فقط."], "C": ["Map Package (.mpkx) bundles a single 2D map.", "حزمة الخريطة (.mpkx) تجمع خريطة ثنائية الأبعاد واحدة."], "D": ["Tile Package (.tpkx) stores pre-rendered raster basemap tiles.", "حزمة البلاطات (.tpkx) تخزن بلاطات صور مخزنة مؤقتاً."]},
        "packages"
    ),
    # 6: Map Package (.mpkx) vs Project Package (.ppkx)
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Conceptual", ["Sharing Packages"],
        "What is the difference between a Map Package (.mpkx) and a Project Package (.ppkx)?",
        "ما هو الفرق بين حزمة الخريطة (.mpkx) وحزمة المشروع (.ppkx)؟",
        [["A Map Package contains a single 2D map and its data; a Project Package contains multiple maps, 3D scenes, page layouts, tasks, and tools", "تحتوي حزمة الخريطة على خريطة ثنائية الأبعاد واحدة وبياناتها؛ بينما تحتوي حزمة المشروع على عدة خرائط ومشاهد ثلاثية الأبعاد ولوحات طباعة ومهام وأدوات"], ["A Map Package only works in ArcMap; a Project Package only works in Pro", "تعمل حزمة الخريطة في ArcMap وحزمة المشروع في Pro"], ["A Project Package cannot include geodatabase data", "لا يمكن لحزمة المشروع تضمين بيانات الجيوداتابيس"], ["A Map Package creates web feature services automatically", "تنشئ حزمة الخريطة خدمات ويب تلقائياً"]],
        "A",
        "An .mpkx packages a single Map item (.mapx + data). A .ppkx packages the complete project workspace (.aprx) including all associated maps, scenes, layouts, toolboxes, and geodatabases.",
        "تجمع حزمة .mpkx خريطة واحدة وبياناتها؛ بينما تجمع حزمة .ppkx مساحة عمل المشروع الكاملة (.aprx) بما فيها من خرائط ومشاهد متعددة ولوحات إخراج وصناديق أدوات.",
        {"B": ["Both .mpkx and .ppkx are native ArcGIS Pro package formats.", "كلا التنسيقين أصيلان في ArcGIS Pro."], "C": ["Project packages consolidate referenced geodatabase datasets by default.", "تدمج حزم المشاريع بيانات الجيوداتابيس افتراضياً."], "D": ["Packages are local archives, not live hosted web services.", "الحزم ملفات أرشيفية محلية وليست خدمات ويب حية."]},
        "packages"
    ),
    # 7: Mobile Map Package (.mmpk)
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Tool-based", ["Mobile Map Package"],
        "Which package format is specifically engineered for offline fieldwork in mobile applications like ArcGIS Field Maps, bundling vector basemaps, operational layers, address locators, and transportation networks into a single file?",
        "أي صيغة حزم مصممة خصيصاً للعمل الميداني بدون إنترنت في تطبيقات الجوال مثل ArcGIS Field Maps، وتدمج خرائط الأساس المتجهة والطبقات التشغيلية ومحددات العناوين وشبكات النقل في ملف واحد؟",
        [["Mobile Map Package (.mmpk)", "Mobile Map Package (.mmpk)"], ["Project Package (.ppkx)", "Project Package (.ppkx)"], ["Tile Package (.tpkx)", "Tile Package (.tpkx)"], ["Shapefile (.shp)", "Shapefile (.shp)"]],
        "A",
        "Mobile Map Packages (.mmpk) consolidate vector basemaps, operational feature layers, geocoding locators, and network datasets into a compressed format optimized for offline mobile navigation and data collection.",
        "تدمج حزم الخرائط المحمولة (.mmpk) خرائط الأساس المتجهة والطبقات التشغيلية ومحددات العناوين وشبكات التحليل المكاني في ملف مضغوط عالي الأداء مخصص للعمل الميداني دون اتصال بالإنترنت.",
        {"B": ["Project packages are designed for desktop ArcGIS Pro workstations.", "حزم المشاريع مخصصة لأجهزة الحاسب المكتبي."], "C": ["Tile packages only hold raster cache tiles, without locators or networks.", "حزم البلاطات تحتوي على صور وبلاطات فقط دون محددات عناوين."], "D": ["Shapefiles cannot store locators, network topologies, or multiple layers.", "ملفات shapefile لا تدعم الشبكات أو محددات العناوين."]},
        "packages"
    ),
    # 8: Vector Tile Package (.vtpk) vs Tile Package (.tpkx)
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Conceptual", ["Sharing Packages"],
        "What is the key advantage of a Vector Tile Package (.vtpk) over a traditional Raster Tile Package (.tpkx)?",
        "ما هي الميزة الأساسية لحزمة البلاطات المتجهة (.vtpk) مقارنة بحزمة بلاطات الراستر التقليدية (.tpkx)؟",
        [["Vector tiles are significantly smaller in file size, scale crisply to high-DPI displays without pixelation, and support on-the-fly client-side restyling", "البلاطات المتجهة أصغر حجماً بكثير، وتحافظ على حدة الرسم ونقائه في الشاشات عالية الدقة دون تشويش بكسلي، وتدعم إعادة التلوين لدى المستخدم"], ["Vector tiles can store raw Landsat satellite multispectral bands", "تستطيع البلاطات المتجهة تخزين النطاقات الطيفية لصور لاندسات"], ["Vector tiles can be edited using the Traverse tool", "يمكن تحرير البلاطات المتجهة بأداة Traverse"], ["Vector tiles do not require coordinate systems", "لا تتطلب البلاطات المتجهة نظام إحداثيات"]],
        "A",
        "Vector tiles store vector representations of features as protocol buffers. They are compact, adapt resolution smoothly to any screen DPI, rotate without distorted labels, and allow restyling styles without rebuilding caches.",
        "تخزن البلاطات المتجهة المعالم بتنسيق متجه مضغوط؛ فتكون أحجامها أصغر بعشر مرات، وتظهر بنقاء فائق على الشاشات الحديثة دون تشويش، وتسمح بتدوير الخريطة وتغيير الألوان دون إعادة بناء الكاش.",
        {"B": ["Raster tile packages (.tpkx) handle continuous imagery bands, not vector tiles.", "حزم الراستر هي المخصصة للصور الفضائية."], "C": ["Vector tiles are read-only cached basemaps and cannot be edited with editing tools.", "البلاطات المتجهة للقراءة فقط كخرائط أساس."], "D": ["Vector tiles require projected coordinate systems (typically Web Mercator).", "تتطلب البلاطات المتجهة نظام إحداثيات محدد."]},
        "packages"
    ),
    # 9: Sharing Web Layer: Errors vs Warnings
    (
        "Choose how to share content from ArcGIS Pro", "Beginner", "Technical", ["Share Web Layer"],
        "During the 'Analyze' stage of sharing a web layer to ArcGIS Online, what is the critical difference between an Error (red circle with 'X') and a Warning (yellow triangle)?",
        "أثناء مرحلة التحليل (Analyze) لنشر طبقة ويب إلى ArcGIS Online، ما هو الفرق الجوهري بين الخطأ (دائرة حمراء بها علامة X) والتحذير (مثلث أصفر)؟",
        [["Errors prevent publishing and MUST be resolved before sharing; Warnings are advisory and do not block publishing", "الأخطاء تمنع النشر تماماً ويجب حلها إلزامياً قبل المشاركة؛ بينما التحذيرات إرشادية ولا تمنع استكمال عملية النشر"], ["Warnings delete the dataset; Errors do not", "التحذيرات تحذف البيانات والأخطاء لا تحذفها"], ["Errors can be ignored if the user has an Administrator role", "يمكن تجاهل الأخطاء إذا كان للمستخدم صلاحية مسؤول"], ["Both errors and warnings permanently cancel the publishing process", "يلغي كلاهما عملية النشر بشكل دائم"]],
        "A",
        "The ArcGIS Pro sharing analyzer marks blocking issues as Errors (e.g. unsupported layer types, missing unique IDs), which completely prevent publishing until fixed. Warnings indicate potential performance or cosmetic issues but allow publishing to proceed.",
        "يميز محلل المشاركة المشكلات الحرجة كأخطاء (Errors) تمنع النشر إجبارياً حتى إصلاحها (مثل غياب المعرفات الفريدة)؛ بينما تمثل التحذيرات (Warnings) ملاحظات لتحسين الأداء ولا تعطل إتمام النشر.",
        {"B": ["Neither message deletes datasets.", "لا تؤدي أي من الرسائل لحذف البيانات."], "C": ["Administrator roles cannot override fatal publishing errors.", "صلاحيات المسؤول لا تتجاوز الأخطاء البرمجية المانعة."], "D": ["Warnings permit publishing immediately.", "تسمح التحذيرات بنشر الطبقة مباشرة."]},
        "weblayers"
    ),
    # 10: Reference registered data vs Copy all data
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Conceptual", ["Share Web Layer"],
        "When publishing a web feature layer to ArcGIS Enterprise, what is the impact of choosing 'Reference registered data' instead of 'Copy all data'?",
        "عند نشر طبقة معالم ويب إلى ArcGIS Enterprise، ما هو أثر اختيار 'Reference registered data' بدلاً من 'Copy all data'؟",
        [["The web service connects live to the enterprise geodatabase so edits made by web or desktop clients update the same central database in real time", "تتصل خدمة الويب مباشرة بقاعدة البيانات المؤسسية المركزية بحيث تنعكس التعديلات من الويب أو الأجهزة المكتبية لحظياً على نفس البيانات"], ["A duplicate snapshot copy of the data is uploaded to the hosting server's relational datastore", "تُرفع نسخة طبق الأصل مكررة من البيانات إلى مخزن البيانات المستضاف بالخادم"], ["All vector features are converted into raster JPEG images", "تتحول كافة المعالم الاتجاهية إلى صور راستر"], ["The enterprise geodatabase is permanently uninstalled", "يتم إلغاء تثبيت قاعدة البيانات المؤسسية نهائياً"]],
        "A",
        "'Reference registered data' creates a dynamic service pointing directly to the enterprise database source. 'Copy all data' duplicates the dataset and pushes it into the ArcGIS Data Store.",
        "ينشئ خيار 'Reference registered data' خدمة متصلة حية بمصدر قاعدة البيانات المؤسسية المسجلة، مما يتيح مزامنة التعديلات الميدانية والمكتبية آنياً على نفس السجلات دون تكرار للبيانات.",
        {"B": ["Uploading duplicate snapshots is the behavior of 'Copy all data'.", "رفع نسخ مكررة هو سلوك خيار Copy all data."], "C": ["Feature services publish vector geometries, not raster JPEGs.", "خدمات المعالم تنشر بيانات اتجاهية وليست صوراً."], "D": ["It does not damage the database engine.", "لا يؤثر على خادم قاعدة البيانات إطلاقاً."]},
        "weblayers"
    ),
    # 11: Export Georeferenced PDF
    (
        "Identify how to export data, maps, and scenes to different formats", "Intermediate", "Tool-based", ["Export Layout"],
        "An analyst needs to export a PDF map for field engineers so they can measure coordinates, calculate distances, and toggle layer visibility using free Adobe Acrobat Reader. Which option must be enabled during PDF export?",
        "يحتاج محلل لتصدير خريطة بصيغة PDF لمهندسين ميدانيين لتمكينهم من قياس الإحداثيات والمسافات وتشغيل وإطفاء الطبقات ببرنامج Adobe Acrobat Reader المجاني. أي خيار يجب تفعيله أثناء تصدير PDF؟",
        [["Export georeference information and Include layers and attributes", "Export georeference information وتفعيل Include layers and attributes"], ["Convert all text to raster bitmaps", "تحويل كافة النصوص إلى صور نقطية"], ["Set resolution to 72 DPI", "ضبط الدقة على 72 DPI"], ["Export as CMYK monochrome", "التصدير بنمط ألوان CMYK أحادي"]],
        "A",
        "Enabling 'Export georeference information' embeds geospatial coordinates into the PDF (making it a GeoPDF). Enabling 'Include layers and attributes' embeds PDF layer management and attribute inspection for Acrobat Reader.",
        "يؤدي تفعيل 'Export georeference information' إلى دمج الإحداثيات الجغرافية داخل ملف PDF (ليصبح GeoPDF)؛ ويتيح خيار 'Include layers' إمكانية إظهار وإخفاء الطبقات واستعراض سماتها في قارئ أدوبي.",
        {"B": ["Rasterizing text removes searchability and increases file size.", "تحويل النصوص لصور يفقدها ميزة البحث."], "C": ["72 DPI is low screen resolution, poor for measurement.", "دقة 72 ضعيفة جداً للقياس."], "D": ["Monochrome strips map colors.", "النمط الأحادي يلغي ألوان الخريطة."]},
        "exporting"
    ),
    # 12: Resolution DPI for Print
    (
        "Identify how to export data, maps, and scenes to different formats", "Beginner", "Technical", ["Export Layout"],
        "What is the industry-standard resolution (DPI) recommended when exporting a formal cartographic page layout to PDF for high-quality commercial paper printing?",
        "ما هي الدقة المعيارية الموصى بها بالنقاط في البوصة (DPI) عند تصدير لوحة إخراج كارتوغرافية إلى PDF للطباعة الورقية التجارية عالية الجودة؟",
        [["300 DPI", "300 DPI"], ["72 DPI", "72 DPI"], ["96 DPI", "96 DPI"], ["2400 DPI", "2400 DPI"]],
        "A",
        "300 DPI (dots per inch) is the worldwide standard for crisp commercial printing. 72 or 96 DPI is intended for web or monitor display; 2400 DPI generates unnecessarily massive files without noticeable paper benefit.",
        "تُعد دقة 300 DPI المعيار العالمي الموصى به للطباعة الورقية التجارية الواضحة؛ بينما تُستخدم دقة 72 أو 96 لشاشات العرض والويب، وتنتج دقة 2400 ملفات ضخمة جداً دون فائدة بصرية ملموسة.",
        {"B": ["72 DPI produces pixelated, blurry paper prints.", "دقة 72 تنتج طباعة ورقية مشوشة."], "C": ["96 DPI is standard Windows screen resolution.", "دقة 96 مخصصة لشاشات الحواسيب."], "D": ["2400 DPI exceeds print plate resolving capabilities and slows processing.", "دقة 2400 تتجاوز قدرة الطابعات وتضخم حجم الملف دون داعٍ."]},
        "exporting"
    ),
    # 13: Color model: RGB vs CMYK
    (
        "Identify how to export data, maps, and scenes to different formats", "Intermediate", "Conceptual", ["Export Layout"],
        "When preparing a map layout exclusively destined for offset commercial printing presses, which color model should be configured in the Export settings?",
        "عند إعداد لوحة خريطة مخصصة حصرياً للمطابع التجارية (أوفست)، أي نموذج ألوان يجب اختياره في إعدادات التصدير؟",
        [["CMYK (Cyan, Magenta, Yellow, Key/Black)", "CMYK (السماوي، القرمزي، الأصفر، والأسود)"], ["RGB (Red, Green, Blue)", "RGB (الأحمر، الأخضر، والأزرق)"], ["HSV (Hue, Saturation, Value)", "HSV (درجة اللون، التشبع، والقيمة)"], ["Greyscale 1-bit", "Greyscale 1-bit"]],
        "A",
        "Commercial printing presses use four-color process ink (CMYK). Designing and exporting in CMYK prevents unpredictable color shifts (such as muddy greens or neon blues turning dull) that occur during RGB-to-CMYK conversion.",
        "تعتمد المطابع التجارية على أحبار الطباعة الأربعة (CMYK)؛ ويضمن التصدير بنمط CMYK تجنب التغيرات اللونية المفاجئة التي تحدث عند تحويل ألوان الشاشات (RGB) إلى ألوان الطباعة الورقية.",
        {"B": ["RGB is an additive light model for computer monitors and web applications.", "نموذج RGB مخصص لشاشات الحواسيب والعرض الضوئي."], "C": ["HSV is a color picker model, not a print output profile.", "نموذج HSV لاختيار الألوان في الواجهة."], "D": ["Greyscale 1-bit removes all color.", "النمط الأحادي يلغي كافة الألوان."]},
        "exporting"
    ),
    # 14: Dynamic Legend: Only show visible
    (
        "Determine how to create and manage map layouts and map series", "Beginner", "Tool-based", ["Legend"],
        "In a layout legend, how do you automatically prevent layers or symbol classes that are not currently visible in the map frame extent from appearing in the legend?",
        "في مفتاح الخريطة (Legend) باللوحة، كيف تمنع تلقائياً ظهور الطبقات أو الرموز غير المعروضة حالياً ضمن نطاق إطار الخريطة من الظهور في المفتاح؟",
        [["Check 'Only show features visible in the map extent' in Legend element properties", "تفعيل خيار 'Only show features visible in the map extent' في خصائص عنصر مفتاح الخريطة"], ["Manually delete the missing symbols from the legend every time the map pans", "حذف الرموز الغائبة يدوياً في كل مرة يتم فيها تحريك الخريطة"], ["Turn off the entire map frame", "إطفاء إطار الخريطة بالكامل"], ["Export the layout to a BMP file", "تصدير اللوحة إلى ملف BMP"]],
        "A",
        "Enabling 'Only show features visible in the map extent' dynamically updates the legend to show only the symbology classes and layers that currently have features drawn inside the active map frame.",
        "يؤدي تفعيل خيار 'Only show features visible in the map extent' إلى تحديث مفتاح الخريطة ديناميكياً ليقتصر فقط على الرموز والطبقات التي تظهر معالمها فعلياً داخل إطار الخريطة الحالي.",
        {"B": ["Manual deletion is tedious and breaks on next map extent update.", "الحذف اليدوي مرهق ويتلف المفتاح عند تغيير النطاق."], "C": ["Turning off the frame hides the map entirely.", "إطفاء الإطار يخفي الخريطة."], "D": ["BMP export does not configure legend filtering.", "تصدير BMP لا يضبط عناصر المفتاح."]},
        "layouts"
    ),
    # 15: North Arrow Orientation
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Conceptual", ["North Arrow"],
        "When placing a North Arrow on a layout depicting an area with significant map projection convergence, which north arrow direction setting aligns the arrow with the true geographic North Pole?",
        "عند وضع سهم الشمال على لوحة خريطة لمنطقة ذات زاوية تقارب إسقاطي كبيرة، أي إعداد لاتجاه سهم الشمال يجعله يشير بدقة إلى القطب الشمالي الجغرافي الحقيقي؟",
        [["True North", "True North (الشمال الحقيقي)"], ["Map North", "Map North (شمال الخريطة)"], ["Magnetic North", "Magnetic North (الشمال المغناطيسي)"], ["Grid South", "Grid South (جنوب الشبكة)"]],
        "A",
        "True North points toward the geographic North Pole based on the map's coordinate system projection convergence angle at the center of the frame. Map North merely points straight up toward the top of the physical page.",
        "يشير خيار True North نحو القطب الشمالي الجغرافي الفعلي محسوباً وفق زاوية تقارب خطوط الطول للإسقاط عند مركز الخريطة؛ بينما يشير Map North إلى أعلى حافة الصفحة الورقية فقط.",
        {"B": ["Map North points straight up relative to the page boundary regardless of projection curvature.", "يشير Map North لأعلى الورقة متجاهلاً انحناء خطوط الطول."], "C": ["Magnetic North points toward the Earth's shifting magnetic pole.", "يشير Magnetic North للقطب المغناطيسي المتحرك."], "D": ["Grid South points toward the south.", "يشير Grid South للاتجاه المعاكس."]},
        "layouts"
    ),
    # 16: Scale Bar Linking
    (
        "Determine how to create and manage map layouts and map series", "Beginner", "Tool-based", ["Scale Bar"],
        "When multiple Map Frames are inserted into a single layout (e.g., Main Map and Inset Map), how do you ensure the Scale Bar reflects the scale of the Main Map?",
        "عند إدراج عدة إطارات خرائط في لوحة واحدة (مثل خريطة رئيسية وخريطة تفصيلية مصغرة)، كيف تضمن أن شريط المقياس يعبر عن مقياس رسم الخريطة الرئيسية؟",
        [["Set the 'Map Frame' property of the Scale Bar element to target the Main Map frame explicitly", "ضبط خاصية 'Map Frame' لعنصر شريط المقياس ليرتبط صراحة بإطار الخريطة الرئيسية"], ["Place the scale bar physically inside the main map frame", "وضع شريط المقياس فيزيائياً داخل إطار الخريطة الرئيسية"], ["Change the scale bar color to match the basemap", "تغيير لون شريط المقياس ليطابق خريطة الأساس"], ["Lock the operating system screen orientation", "قفل تدوير شاشة نظام التشغيل"]],
        "A",
        "Layout elements like scale bars, legends, and north arrows are linked to a specific Map Frame via their Element Properties pane. Selecting the Main Map Frame ensures the scale bar calculates length from that specific frame's scale.",
        "ترتبط عناصر اللوحة (كأشرطة المقاييس وأسهم الشمال) بإطار خريطة محدد عبر نافذة الخصائص؛ ويضمن ربطه بإطار الخريطة الرئيسية تحديث مقياس الرسم وفق نطاق ذلك الإطار حصراً.",
        {"B": ["Physical placement on the page does not establish software element linking.", "الموضع المكاني على الصفحة لا يربط العنصر برمجياً."], "C": ["Color changes do not affect scale calculations.", "تغيير الألوان لا يؤثر على الحسابات."], "D": ["Screen orientation is an OS feature.", "تدوير الشاشة خاصية نظام تشغيل."]},
        "layouts"
    ),
    # 17: Extent Indicators
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Tool-based", ["Extent Indicator"],
        "An analyst has a main detailed city map and a small overview locator map frame of the entire state on the same layout. Which layout element draws a dynamic rectangle on the state overview map showing the current boundary of the detailed city map?",
        "لدى محلل خريطة تفصيلية لمدينة وخريطة عامة مصغرة للولاية بأكملها في نفس اللوحة. أي عنصر تصميم يرسم مستطيلاً ديناميكياً على خريطة الولاية يوضح الحدود الحالية لخريطة المدينة التفصيلية؟",
        [["Extent Indicator", "Extent Indicator (مؤشر النطاق)"], ["Scale Bar", "Scale Bar (شريط المقياس)"], ["North Arrow", "North Arrow (سهم الشمال)"], ["Table Frame", "Table Frame (إطار الجدول)"]],
        "A",
        "An Extent Indicator displays the geographical extent of one map frame (e.g. detailed city) as a dynamic bounding rectangle inside another map frame (e.g. statewide overview).",
        "يعرض عنصر Extent Indicator النطاق الجغرافي لإطار خريطة معين (مثل خريطة المدينة التفصيلية) كمستطيل ديناميكي داخل إطار خريطة آخر (مثل خريطة الولاية الإقليمية العامة).",
        {"B": ["Scale bars measure distances.", "شريط المقياس يقيس المسافات."], "C": ["North arrows indicate orientation.", "سهم الشمال يوضح الاتجاه."], "D": ["Table frames display tabular attribute records.", "إطار الجدول يعرض سجلات البيانات."]},
        "layouts"
    ),
    # 18: Map Series Clip to Index Feature
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Tool-based", ["Spatial Map Series"],
        "In a Spatial Map Series, how can an analyst mask and hide all features lying outside the current page's index polygon so each page shows only the active municipality?",
        "في سلسلة الخرائط المكانية، كيف يمكن للمحلل إخفاء وحجب كافة المعالم الواقعة خارج مضلع الفهرس للصفحة الحالية بحيث تعرض كل صفحة بلدية واحدة فقط دون جوارها؟",
        [["Enable 'Clip to current map series index feature' in the Map Frame properties", "تفعيل خيار 'Clip to current map series index feature' في خصائص إطار الخريطة"], ["Delete surrounding municipalities using the Delete tool", "حذف البلديات المجاورة بأداة Delete"], ["Apply a 100% brightness filter to the entire monitor", "تطبيق فلتر سطوع بنسبة 100% على الشاشة"], ["Convert the index layer to a CAD drawing", "تحويل طبقة الفهرس إلى رسم CAD"]],
        "A",
        "ArcGIS Pro allows clipping the map frame display dynamically to the active map series index feature, automatically masking out all data outside the current page's boundary polygon.",
        "يتيح ArcGIS Pro قص عرض إطار الخريطة ديناميكياً عند حدود معلم الفهرس النشط للصفحة، مما يحجب كافة المعالم الواقعة خارج حدود مضلع الصفحة الحالية تلقائياً وبشكل مؤقت.",
        {"B": ["Deleting features permanently destroys underlying data.", "حذف المعالم يدمر البيانات الأصلية."], "C": ["Monitor brightness affects physical hardware display.", "سطوع الشاشة يؤثر على العتاد."], "D": ["CAD conversion does not manage layout clipping.", "تحويل CAD لا يدير إخراج اللوحات."]},
        "mapseries"
    ),
    # 19: Export to AIX format
    (
        "Identify how to export data, maps, and scenes to different formats", "Intermediate", "Tool-based", ["Export Layout"],
        "Which export file format is specifically designed to transfer ArcGIS Pro vector layouts directly into Adobe Illustrator for professional graphic design, preserving organized vector artwork layers?",
        "أي صيغة تصدير مصممة خصيصاً لنقل لوحات خرائط ArcGIS Pro المتجهة مباشرة إلى برنامج Adobe Illustrator للتصميم الجرافيكي المتقدم مع الحفاظ على تنظيم طبقات الرسم؟",
        [["Adobe Illustrator Exchange (.aix)", "Adobe Illustrator Exchange (.aix)"], ["JPEG (.jpg)", "JPEG (.jpg)"], ["TIFF (.tif)", "TIFF (.tif)"], ["BMP (.bmp)", "BMP (.bmp)"]],
        "A",
        "The .aix format (used with the ArcGIS Maps for Adobe Creative Cloud extension) converts map and layout vector art into organized, native Adobe Illustrator layers, paths, and text.",
        "صيغة .aix (المستخدمة مع إضافة ArcGIS Maps for Adobe Creative Cloud) تنقل مسارات ورسوم ونصوص الخريطة إلى طبقات متجهة أصلية منظمة داخل برنامج أدوبي إليستريتور.",
        {"B": ["JPEG is a compressed lossy raster format.", "JPEG صيغة راستر نقطية مضغوطة."], "C": ["TIFF is a raster format, not editable Illustrator vectors.", "TIFF صيغة راستر وليست متجهات."], "D": ["BMP is an uncompressed raster bitmap.", "BMP صيغة نقطية خام."]},
        "exporting"
    ),
    # 20: Layer File (.lyrx) vs Layer Package (.lpkx)
    (
        "Choose how to share content from ArcGIS Pro", "Beginner", "Conceptual", ["Layer File"],
        "What is the key difference between a Layer File (.lyrx) and a Layer Package (.lpkx)?",
        "ما هو الفرق الجوهري بين ملف الطبقة (.lyrx) وحزمة الطبقة (.lpkx)؟",
        [["A .lyrx file stores only symbology, labeling, and a pointer to the data source; an .lpkx file bundles the symbology AND packages the physical dataset inside the file", "يخزن ملف .lyrx إعدادات الرموز والتسميات ومسار البيانات فقط؛ بينما تجمع حزمة .lpkx إعدادات الرموز وتدمج معها ملف البيانات الفعلي داخل الحزمة"], ["A .lyrx file can only be opened in Microsoft Word", "يفتح ملف .lyrx في برنامج وورد فقط"], ["A .lpkx file deletes all attributes", "تحذف حزمة .lpkx كافة السمات"], ["There is no difference between them", "لا يوجد أي فرق بينهما"]],
        "A",
        "A layer file (.lyrx) is a lightweight pointer storing symbology and properties without copying data (if the source data moves, the link breaks). A layer package (.lpkx) embeds the actual dataset inside the archive file, making it self-contained.",
        "ملف .lyrx هو ملف إعدادات خفيف يخزن الرموز ومسار البيانات فقط دون نسخها (وينقطع إذا تغير مسار البيانات)؛ أما حزمة .lpkx فتدمج ملف البيانات الفعلي بداخلها لتكون مستقلة تماماً وقابلة للنقل لأي جهاز.",
        {"B": ["Layer files are exclusive to ArcGIS software.", "ملفات الطبقات خاصة ببرمجيات ArcGIS."], "C": ["Layer packages preserve all attribute tables and schemas.", "تحافظ حزم الطبقات على كافة البيانات الوصفية."], "D": ["They have distinct architectures (pointer vs self-contained data archive).", "تختلفان جوهرياً (مؤشر مسار مقابل حزمة بيانات مدمجة)."]},
        "packages"
    ),
    # 21: Web Map vs Web Scene
    (
        "Choose how to share content from ArcGIS Pro", "Beginner", "Conceptual", ["Web Map"],
        "What is the distinguishing difference between sharing content as a Web Map versus sharing as a Web Scene to ArcGIS Online?",
        "ما هو الفرق المميز بين مشاركة المحتوى كخريطة ويب (Web Map) ومشاركته كمشهد ويب (Web Scene) إلى ArcGIS Online؟",
        [["Web Maps display 2D geospatial content; Web Scenes display 3D geographic content with terrain elevation and 3D symbology", "تعرض خرائط الويب محتوى جغرافياً ثنائي الأبعاد 2D؛ بينما تعرض مشاهد الويب محتوى ثلاثي الأبعاد 3D مع تضاريس الارتفاع والرموز المجسمة"], ["Web Maps only work on iPhones", "خرائط الويب تعمل على هواتف آيفون فقط"], ["Web Scenes cannot be viewed in web browsers", "لا يمكن عرض مشاهد الويب في متصفحات الإنترنت"], ["Web Maps require a database server", "تتطلب خرائط الويب خادم قواعد بيانات"]],
        "A",
        "Web Maps are 2D interactive maps authored from Pro 2D maps. Web Scenes are 3D interactive experiences authored from Pro Local or Global scenes that support 3D layers, elevation surfaces, and lighting.",
        "خرائط الويب (Web Maps) هي خرائط تفاعلية ثنائية الأبعاد 2D؛ بينما مشاهد الويب (Web Scenes) هي بيئات تفاعلية ثلاثية الأبعاد 3D مبنية من مشاهد Pro وتدعم أسطح الارتفاع والمجسمات وإضاءة الشمس.",
        {"B": ["Web Maps work on all desktop and mobile web browsers.", "تعمل خرائط الويب على كافة المتصفحات."], "C": ["Web Scenes are designed specifically for modern WebGL browser viewing.", "صُممت مشاهد الويب للعرض في المتصفحات عبر تقنية WebGL."], "D": ["Web maps are hosted cloud services.", "خرائط الويب خدمات سحابية مستضافة."]},
        "weblayers"
    ),
    # 22: Feature Layer vs Map Image Layer
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Conceptual", ["Web Layer"],
        "When publishing to ArcGIS Enterprise, which service type sends vector geometry and attributes directly to the client browser for client-side rendering and interactive editing?",
        "عند النشر إلى ArcGIS Enterprise، أي نوع خدمة يرسل إحداثيات المعالم المتجهة وسماتها مباشرة إلى متصفح العميل للرسم المحلي ودعم التحرير التفاعلي؟",
        [["Feature Layer (Feature Service)", "طبقة المعالم Feature Layer (Feature Service)"], ["Map Image Layer (Map Service)", "طبقة صورة الخريطة Map Image Layer (Map Service)"], ["Tile Layer", "طبقة البلاطات Tile Layer"], ["Vector Tile Layer", "طبقة البلاطات المتجهة Vector Tile Layer"]],
        "A",
        "Feature Layers stream individual vector geometries (points, lines, polygons) and attributes directly to client apps, supporting client-side filtering, interactive symbology styling, and transactional editing.",
        "ترسل خدمات المعالم (Feature Layers) الإحداثيات والسمات المتجهة مباشرة إلى جهاز المستخدم، مما يتيح التحرير الميداني، والتصفية اللحظية، وتغيير أنماط الرموز تفاعلياً داخل المتصفح.",
        {"B": ["Map Image layers render maps as static raster images on the server before sending to client.", "خدمات Map Image ترسم الخريطة كصورة على الخادم قبل إرسالها."], "C": ["Tile layers stream pre-cached image tiles.", "طبقات البلاطات ترسل صوراً مخزنة مؤقتاً."], "D": ["Vector tile layers are read-only basemap caches.", "البلاطات المتجهة خرائط أساس للقراءة فقط."]},
        "weblayers"
    ),
    # 23: Map Image Layer server rendering
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Technical", ["Web Layer"],
        "What is the primary advantage of publishing a Map Image Layer (Map Service) from an enterprise geodatabase containing millions of complex utility features?",
        "ما هي الميزة الأساسية لنشر طبقة صورة خريطة (Map Image Layer) من قاعدة بيانات مؤسسية تحتوي على ملايين معالم شبكات البنية التحتية المعقدة؟",
        [["The server renders the complex symbology into an image on demand, avoiding the overhead of streaming millions of vector vertices over the network to the browser", "يقوم الخادم برسم الرموز المعقدة كصورة حسب الطلب، متجنباً عبء إرسال ملايين إحداثيات المتجهات عبر الشبكة إلى المتصفح"], ["It automatically deletes retired utility poles", "تحذف أعمدة الإنارة القديمة تلقائياً"], ["It converts polyline features into 3D multipatches", "تحول الخطوط إلى مجسمات ثلاثية الأبعاد"], ["It translates attribute table column names to French", "تترجم أسماء الأعمدة إلى الفرنسية"]],
        "A",
        "Map Image Layers leverage the server's computing power to dynamically draw and rasterize complex symbology into a lightweight image, delivering fast performance over narrow bandwidth for massive datasets.",
        "تستغل طبقات Map Image قدرة معالجة الخادم لرسم الرموز الكارتوغرافية المعقدة في صورة واحدة خفيفة تُرسل للعميل، مما يضمن سرعة التصفح لشبكات المرافق الضخمة دون استهلاك حزمة الإنترنت.",
        {"B": ["Publishing services does not delete features.", "النشر لا يحذف المعالم."], "C": ["Map Image layers render existing 2D/3D vectors.", "ترسم المعالم ولا تحول أنواعها الهندسية."], "D": ["Schema translation is not automated.", "لا تترجم أسماء الأعمدة تلقائياً."]},
        "weblayers"
    ),
    # 24: PDF Export: Embed Fonts
    (
        "Identify how to export data, maps, and scenes to different formats", "Beginner", "Technical", ["Export Layout"],
        "Why is it essential to check 'Embed fonts' when exporting a map layout containing specialized cartographic fonts to PDF?",
        "لماذا يُعد تفعيل خيار 'تضمين الخطوط' (Embed fonts) أمراً ضرورياً عند تصدير لوحة خريطة تحتوي على خطوط كارتوغرافية مخصصة إلى PDF؟",
        [["To ensure text renders accurately with the exact designed styling on recipient computers that do not have those fonts installed", "لضمان ظهور النصوص بدقة وبنفس التنسيق المصمم على أجهزة المستلمين التي لا تملك تلك الخطوط مثبتة"], ["To prevent the PDF file from being opened on Mondays", "لمنع فتح ملف PDF في أيام محددة"], ["To reduce the PDF file size to 1 kilobyte", "لتقليص حجم ملف PDF إلى 1 كيلوبايت"], ["To convert the PDF to an executable program", "لتحويل ملف PDF إلى برنامج تنفيذي"]],
        "A",
        "Embedding fonts packs the character glyphs directly inside the PDF file, preventing PDF viewers on foreign machines from substituting missing fonts with generic system fonts.",
        "يؤدي تضمين الخطوط (Embed fonts) إلى حفظ أشكال الحروف ومحارفها داخل ملف PDF، مما يمنع برامج قراءة PDF على أجهزة المستخدمين الآخرين من استبدال الخطوط المخصصة بخطوط افتراضية تشوه التصميم.",
        {"B": ["PDFs have no weekday restrictions.", "لا توجد قيود زمنية لفتح ملفات PDF."], "C": ["Embedding fonts slightly increases file size, rather than shrinking it to 1 KB.", "تضمين الخطوط يزيد حجم الملف قليلاً."], "D": ["PDFs remain static document files.", "تبقى ملفات PDF وثائق رقمية وليست برامج تنفيذية."]},
        "exporting"
    ),
    # 25: Grids and Graticules
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Tool-based", ["Grids and Graticules"],
        "What is the difference between a Graticule and a Measured Grid when added to a Map Frame in a layout?",
        "ما هو الفرق بين شبكة خطوط الطول والعرض (Graticule) وشبكة الإحداثيات المترية (Measured Grid) عند إضافتها لإطار خريطة باللوحة؟",
        [["A Graticule displays lines of geographic latitude and longitude (degrees); a Measured Grid displays projected grid coordinates (e.g. UTM meters or State Plane feet)", "تعرض شبكة Graticule خطوط الطول ودوائر العرض الجغرافية (بالدرجات)؛ بينما تعرض شبكة Measured Grid إحداثيات الشبكة المسقطة (مثل أمتار UTM أو أقدام State Plane)"], ["A Graticule only works in the Southern Hemisphere", "تعمل Graticule في نصف الكرة الجنوبي فقط"], ["A Measured Grid cannot have tick marks", "لا يمكن لشبكة Measured Grid احتواء علامات تأشير"], ["Both grid types display identical degree coordinates", "تعرض كلتا الشبكتين إحداثيات متطابقة بالدرجات"]],
        "A",
        "Graticules depict geographic coordinates (angular units: degrees/minutes/seconds). Measured Grids depict linear projected coordinate intervals (meters, feet) matching the projected coordinate system of the map.",
        "تعرض شبكة Graticule الإحداثيات الجغرافية الكروية (درجات، دقائق، ثوانٍ)؛ بينما تعرض شبكة Measured Grid فواصل الإحداثيات المسقطة المستوية (بالأمتار أو الأقدام) المتطابقة مع نظام إسقاط الخريطة.",
        {"B": ["Graticules function globally across all hemispheres.", "تعمل شبكات Graticule على مستوى العالم."], "C": ["Measured grids fully support ticks, sub-ticks, and labels.", "تدعم علامات التأشير والأرقام."], "D": ["They represent fundamentally different coordinate measurement units (angular vs linear).", "تختلفان في وحدات القياس (زوايا جغرافية مقابل مسافات خطية)."]},
        "layouts"
    )
]

# We have 25 layout questions so far. Let's add 20 more to reach exactly 45 (LS-001 to LS-045).
more_ls = [
    # 26: Map Series: Page Numbering Field
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Technical", ["Spatial Map Series"],
        "In a Spatial Map Series, which field configuration controls the sequence and order in which pages are organized and exported?",
        "في سلسلة الخرائط المكانية، أي إعداد حقل يتحكم في تسلسل وترتيب الصفحات أثناء العرض والتصدير؟",
        [["Sort Field", "Sort Field (حقل الترتيب)"], ["Shape_Area field", "حقل المساحة Shape_Area"], ["GlobalID field", "حقل GlobalID"], ["OBJECTID field", "حقل OBJECTID"]],
        "A",
        "The Sort Field parameter in Map Series properties specifies which attribute field dictates the sequential order (ascending or descending) of pages in the series.",
        "يحدد خيار Sort Field في خصائص سلسلة الخرائط الحقل السماتي الذي يحكم الترتيب التسلسلي للصفحات (تصاعدياً أو تنازلياً) في الأطلس المخرج.",
        {"B": ["Shape_Area sorts by size only if explicitly chosen as Sort Field.", "حقل المساحة يرتب حسب الحجم فقط إذا تم اختياره كحقل ترتيب."], "C": ["GlobalID values are random hexadecimal strings unsuitable for sequential sorting.", "معرفات GlobalID عشوائية ولا تصلح للترتيب التسلسلي."], "D": ["OBJECTID reflects database insertion order, not logical atlas page order.", "حقل OBJECTID يعكس ترتيب الإدخال في قاعدة البيانات."]},
        "mapseries"
    ),
    # 27: Web Scene: Global vs Local
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Technical", ["Web Scene"],
        "When publishing a 3D Scene to ArcGIS Online, can a Local Scene using a custom projected coordinate system be shared as a Web Scene?",
        "عند نشر مشهد ثلاثي الأبعاد إلى ArcGIS Online، هل يمكن مشاركة مشهد محلي (Local Scene) بنظام إحداثيات مسقط مخصص كمشهد ويب؟",
        [["Yes, ArcGIS Online fully supports hosting both Global and Local Web Scenes with projected coordinate systems", "نعم، يدعم ArcGIS Online استضافة مشاهد الويب العالمية والمحلية ذات أنظمة الإحداثيات المسقطة"], ["No, ArcGIS Online only supports 2D flat maps", "لا، فمنصة ArcGIS Online تدعم الخرائط ثنائية الأبعاد فقط"], ["Only if all buildings are extruded to exactly 100 meters", "فقط إذا تم بثق المباني لارتفاع 100 متر بالضبط"], ["Only if published from ArcMap 10.8", "فقط إذا تم النشر من برنامج ArcMap 10.8"]],
        "A",
        "ArcGIS Online and Enterprise support publishing Local Web Scenes in projected coordinate systems (with custom local clipping extents) as well as Global Web Scenes in WGS84 or Web Mercator.",
        "تدعم منصات ArcGIS Online و Enterprise استضافة مشاهد الويب المحلية (Local Web Scenes) بأنظمة إحداثيات مسقطة مع نطاقات قص محلية، بالإضافة إلى المشاهد العالمية.",
        {"B": ["ArcGIS Online provides rich 3D Scene viewing capabilities.", "توفر المنصة قدرات عرض ثلاثية الأبعاد متقدمة."], "C": ["Extrusion heights can vary dynamically.", "ارتفاعات البثق متغيرة بحرية."], "D": ["ArcGIS Pro is the modern publishing platform for web scenes.", "برنامج Pro هو المنصة الأساسية لنشر المشاهد."]},
        "weblayers"
    ),
    # 28: Tile Layer Caching
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Conceptual", ["Tile Layer"],
        "Why would an organization publish an imagery basemap as a Tile Layer rather than a dynamic Map Image Layer?",
        "لماذا تفضل المؤسسة نشر خريطة أساس من الصور الجوية كطبقة بلاطات (Tile Layer) بدلاً من طبقة صورة خريطة ديناميكية (Map Image Layer)؟",
        [["Because pre-rendered cached tiles deliver near-instantaneous pan and zoom performance to thousands of concurrent users without consuming server CPU per request", "لأن البلاطات المخزنة مسبقاً توفر سرعة تصفح فورية لآلاف المستخدمين المتزامنين دون استهلاك معالج الخادم في كل طلب"], ["Because Tile Layers allow real-time vector editing", "لأن طبقات البلاطات تتيح التحرير اللحظي للمتجهات"], ["Because Tile Layers store live GPS locations", "لأن طبقات البلاطات تخزن مواقع GPS الحية"], ["Because Tile Layers automatically translate labels into 50 languages", "لأن طبقات البلاطات تترجم التسميات تلقائياً"]],
        "A",
        "Tile Layers serve static pre-generated raster images (cache) from disk or cloud storage, offloading rendering burden from the server and providing blistering speed under heavy public traffic.",
        "تقدم طبقات البلاطات (Tile Layers) صوراً جاهزة ومخزنة مسبقاً (Cache)، مما يرفع العبء الحسابي عن معالج الخادم ويوفر سرعة تصفح فائقة تحت ضغط آلاف المستخدمين في وقت واحد.",
        {"B": ["Tile layers are static raster images and do not support vector editing.", "البلاطات صور ثابتة ولا تدعم التحرير."], "C": ["Live GPS tracking uses Stream Layers.", "تتبع GPS المباشر يعتمد على طبقات البث."], "D": ["Tile layers do not perform automatic translation.", "لا تترجم اللغات تلقائياً."]},
        "weblayers"
    ),
    # 29: Export Layout to TIFF: World File
    (
        "Identify how to export data, maps, and scenes to different formats", "Intermediate", "Technical", ["Export Layout"],
        "When exporting a map to a TIFF image, which option outputs an auxiliary world file (.tfw) to allow other GIS applications to georeference the image?",
        "عند تصدير خريطة إلى صورة TIFF، أي خيار يُخرج ملف توجيه مكاني مصاحب (.tfw) لتمكين برامج نظم المعلومات الجغرافية الأخرى من مطابقة الصورة مكانياً؟",
        [["Write World File", "Write World File (كتابة ملف التوجيه)"], ["Compress with JPEG", "Compress with JPEG"], ["Convert to Grayscale", "Convert to Grayscale"], ["Clip to Map Frame", "Clip to Map Frame"]],
        "A",
        "Checking 'Write World File' exports an accompanying .tfw file (or embeds GeoTIFF header tags) storing the image extent coordinates, pixel size, and spatial reference coefficients.",
        "يؤدي اختيار 'Write World File' إلى تصدير ملف توجيه مكاني (.tfw) أو تضمين وسوم GeoTIFF التي تخزن إحداثيات أركان الصورة وأبعاد البكسل لإسقاطها جغرافياً في أي برنامج GIS.",
        {"B": ["JPEG compression compresses image data, it does not write spatial metadata files.", "ضغط JPEG يقلل حجم الملف ولا يكتب بيانات مكانية."], "C": ["Grayscale adjusts color channels.", "التدرج الرمادي يعدل قنوات الألوان."], "D": ["Clip cuts the graphic boundary.", "قص الحدود يقتطع الصورة فقط."]},
        "exporting"
    ),
    # 30: Map Series: Best Fit Margin
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Technical", ["Spatial Map Series"],
        "When configuring page extents in a Spatial Map Series, what does the 'Best Fit Margin' parameter control?",
        "عند تهيئة نطاقات الصفحات في سلسلة الخرائط المكانية، في ماذا يتحكم معامل 'Best Fit Margin'؟",
        [["It adds a buffer percentage or distance around each index feature so the feature does not touch the edge of the map frame", "يضيف هامش أمان بنسبة مئوية أو مسافة حول معلم الفهرس حتى لا يلامس المعلم حواف إطار الخريطة"], ["It automatically aligns the north arrow to true magnetic north", "يحاذي سهم الشمال تلقائياً للشمال المغناطيسي"], ["It locks the legend text against editing", "يقفل نصوص مفتاح الخريطة ضد التعديل"], ["It deletes empty attribute columns", "يحذف أعمدة السمات الفارغة"]],
        "A",
        "Best Fit Margin applies padding (specified as a percentage of the feature size or in page units) between the index feature boundary and the border of the layout map frame, ensuring breathing room.",
        "يضيف معامل Best Fit Margin مسافة هامشية (كنسبة مئوية من حجم المعلم أو بوحدات الصفحة) بين حدود معلم الفهرس وإطار الخريطة، لضمان عدم التصاق المعلم بحواف الإطار وظهوره بأريحية.",
        {"B": ["North arrows are aligned via orientation settings.", "سهم الشمال يضبط من إعدادات الاتجاه."], "C": ["Legend editing is managed in legend properties.", "مفتاح الخريطة يدار من خصائصه."], "D": ["Attribute columns are unaffected by layout margins.", "الأعمدة السماتية لا تتأثر بهوامش اللوحة."]},
        "mapseries"
    ),
    # 31: Layer File (.lyrx) schema dependence
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Technical", ["Layer File"],
        "If you share a Layer File (.lyrx) with a colleague who has access to the exact same enterprise geodatabase connection, what happens when they add the .lyrx to their project?",
        "إذا شاركت ملف طبقة (.lyrx) مع زميل لديه حق الوصول لنفس اتصال قاعدة البيانات المؤسسية، ماذا يحدث عند إضافة ملف .lyrx لمشروعه؟",
        [["The layer connects to the database and displays with the exact symbology, labels, and definition queries you authored", "تتصل الطبقة بقاعدة البيانات وتعرض المعالم بنفس الرموز والتسميات والاستعلامات التعريفية التي قمت بإعدادها تماماً"], ["The database tables are duplicated on their desktop hard drive", "تتكرر جداول قاعدة البيانات على قرصه الصلب"], ["All attribute rules are permanently removed", "تُحذف جميع القواعد السماتية بشكل دائم"], ["The colleague's user license is upgraded to Advanced", "تتم ترقية ترخيص الزميل إلى المستوى المتقدم"]],
        "A",
        "Because the colleague has access to the underlying data source, the .lyrx file re-establishes the connection and applies all preserved symbology, labeling properties, and query definitions seamlessly.",
        "نظراً لامتلاك الزميل صلاحية الوصول لمصدر البيانات الأصلي، يقوم ملف .lyrx بإعادة الربط وتطبيق كافة تنسيقات الرموز وخصائص التسميات والاستعلامات المحفوظة بسلاسة تامة.",
        {"B": ["Layer files do not copy underlying data.", "ملفات الطبقات لا تنسخ البيانات."], "C": ["Attribute rules reside in the geodatabase schema and are unaffected.", "القواعد السماتية مخزنة في قاعدة البيانات ولا تتأثر."], "D": ["User licenses are managed by the organization administrator.", "تراخيص المستخدمين تدار من قبل مسؤولي المؤسسة."]},
        "packages"
    ),
    # 32: Geoprocessing Package (.gpkx)
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Tool-based", ["Geoprocessing Package"],
        "Which package type allows an analyst to share a custom ModelBuilder model or Python geoprocessing tool along with required reference datasets and tool execution history?",
        "أي نوع من الحزم يتيح للمحلل مشاركة نموذج ModelBuilder مخصص أو أداة بايثون مع مجموعات البيانات المرجعية المطلوبة وسجل تنفيذ الأداة؟",
        [["Geoprocessing Package (.gpkx)", "حزمة المعالجة الجغرافية Geoprocessing Package (.gpkx)"], ["Project Package (.ppkx)", "Project Package (.ppkx)"], ["Map Package (.mpkx)", "Map Package (.mpkx)"], ["Locator Package (.gcpk)", "Locator Package (.gcpk)"]],
        "A",
        "A Geoprocessing Package (.gpkx) encapsulates one or more successful tool execution results from History, packaging the underlying model/script, input data, and parameter schema.",
        "تجمع حزمة المعالجة الجغرافية (.gpkx) نتيجة تشغيل أداة ناجحة من سجل History، دامجة معها النموذج أو السكربت البرمجي والبيانات المرجعية لضمان عملها لدى الآخرين.",
        {"B": ["Project packages share the whole workspace.", "حزم المشاريع تشارك مساحة العمل كاملة."], "C": ["Map packages share 2D maps.", "حزم الخرائط تشارك الخرائط ثنائية الأبعاد."], "D": ["Locator packages share address locators.", "حزم محددات العناوين تشارك أدوات العنونة."]},
        "packages"
    ),
    # 33: Export to KML / KMZ
    (
        "Identify how to export data, maps, and scenes to different formats", "Beginner", "Tool-based", ["Layer To KML"],
        "Which tool in ArcGIS Pro converts a symbolized vector layer into a KMZ file for viewing in Google Earth?",
        "أي أداة في ArcGIS Pro تحول طبقة معالم اتجاهية مُمثلة برموزها إلى ملف KMZ للعرض في برنامج Google Earth؟",
        [["Layer To KML", "Layer To KML"], ["Export Features", "Export Features"], ["Table To Table", "Table To Table"], ["Project Raster", "Project Raster"]],
        "A",
        "Layer To KML (and Map To KML) translates ArcGIS layers into Keyhole Markup Language (.kmz / .kml) archives, preserving symbols and popup attributes for Google Earth.",
        "تحول أداة Layer To KML طبقات ArcGIS برموزها ونوافذها المنبثقة إلى ملفات KML/KMZ المضغوطة المتوافقة مع برنامج Google Earth.",
        {"B": ["Export Features outputs geodatabase feature classes or shapefiles.", "تُخرج Export Features فئات معالم جيوداتابيس."], "C": ["Table To Table converts attribute tables.", "تحول Table To Table الجداول."], "D": ["Project Raster reprojects raster grids.", "تعيد Project Raster إسقاط الراستر."]},
        "exporting"
    ),
    # 34: Export Layout to SVG
    (
        "Identify how to export data, maps, and scenes to different formats", "Intermediate", "Conceptual", ["Export Layout"],
        "Why is Scalable Vector Graphics (SVG) format advantageous when embedding interactive web maps or technical diagrams on responsive websites?",
        "لماذا تُعد صيغة الرسوميات المتجهة القابلة للتحجيم (SVG) ميزة كبرى عند تضمين الخرائط التخطيطية في المواقع الإلكترونية المتجاوبة؟",
        [["Because SVG is an XML-based vector format that scales infinitely without resolution loss and can be styled via CSS", "لأن SVG صيغة متجهة قائمة على XML تتوسع وتتحجم بلا حدود دون فقدان للدقة ويمكن تنسيقها عبر كود CSS"], ["Because SVG can only display black and white pixels", "لأن SVG تعرض بكسلات سوداء وبيضاء فقط"], ["Because SVG requires proprietary desktop software to open", "لأن SVG تتطلب برامج مكتبية مدفوعة لفتحها"], ["Because SVG converts polygon features into satellite imagery", "لأن SVG تحول المضلعات إلى صور فضائية"]],
        "A",
        "SVG represents 2D graphics as XML text vectors. It scales seamlessly across any browser window resolution without blurring, and paths can be styled or animated using web CSS and JavaScript.",
        "تمثل صيغة SVG المعالم كمتجهات برمجية بصيغة XML؛ فتتكيف بدقة ونقاء فائق مع أي حجم شاشة أو نافذة متصفح، وتدعم التنسيق والتحريك عبر أكواد الويب CSS و JavaScript.",
        {"B": ["SVG supports rich RGB and alpha color definitions.", "تدعم SVG ملايين الألوان والشفافية."], "C": ["SVG is an open W3C standard natively supported by all modern browsers.", "صيغة معيارية مفتوحة تدعمها كافة المتصفحات."], "D": ["SVG is a vector document, not satellite imagery.", "صيغة رسوميات متجهة وليست صور أقمار صناعية."]},
        "exporting"
    ),
    # 35: Layout Guides
    (
        "Determine how to create and manage map layouts and map series", "Beginner", "Tool-based", ["Layout Guides"],
        "How do Layout Guides assist cartographers when arranging multiple map frames, legends, and title blocks on a page layout?",
        "كيف تساعد خطوط الإرشاد (Layout Guides) رسامي الخرائط عند ترتيب عدة إطارات خرائط ومفاتيح تصميم وعناوين في لوحة الإخراج؟",
        [["They provide magnetic alignment lines that snap elements cleanly to consistent margins and grid intervals across the page", "توفر خطوط محاذاة مغناطيسية تجذب العناصر وتطابقها بدقة مع هوامش وفواصل متناسقة عبر الصفحة"], ["They automatically calculate the coordinate system transformation", "تحسب تحويلات أنظمة الإحداثيات تلقائياً"], ["They export the layout to social media platforms", "تنشر اللوحة على منصات التواصل الاجتماعي"], ["They convert 2D points into 3D buildings", "تحول النقاط إلى مبانٍ ثلاثية الأبعاد"]],
        "A",
        "Guides are non-printing ruler lines placed on the layout. Elements snap to guides, enabling precise alignment of margins, headers, map frames, and neatlines.",
        "خطوط الإرشاد (Guides) هي خطوط مسطرية غير قابلة للطباعة توضع على اللوحة؛ وتنجذب إليها العناصر تلقائياً لضبط الهوامش والعناوين والإطارات بمحاذاة كارتوغرافية هندسية دقيقة.",
        {"B": ["Guides are visual layout alignment tools, not projection engines.", "أدوات محاذاة تصميمية وليست محركات إسقاط."], "C": ["Sharing tools handle publication, not ruler guides.", "أدوات المشاركة هي المسؤولة عن النشر."], "D": ["3D extrusion is handled in scenes.", "البثق ثلاثي الأبعاد يُدار في المشاهد."]},
        "layouts"
    ),
    # 36: Scene Layer Package (.slpk)
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Tool-based", ["Scene Layer Package"],
        "Which package type is optimized for publishing and streaming massive 3D datasets (such as integrated meshes, 3D buildings, or lidar point clouds) to web scenes?",
        "أي نوع من الحزم مُحسن لنشر وبث مجموعات البيانات ثلاثية الأبعاد الضخمة (مثل الشبكات المدمجة ومجسمات المباني وسحب نقاط ليدار) إلى مشاهد الويب؟",
        [["Scene Layer Package (.slpk)", "Scene Layer Package (.slpk)"], ["Tile Package (.tpkx)", "Tile Package (.tpkx)"], ["Map Package (.mpkx)", "Map Package (.mpkx)"], ["Vector Tile Package (.vtpk)", "Vector Tile Package (.vtpk)"]],
        "A",
        "Scene Layer Packages (.slpk) use Indexed 3D Scene Layers (I3S) format, an open standard specifically engineered for streaming massive 3D content efficiently across the web.",
        "تعتمد حزم Scene Layer Packages (.slpk) على معيار I3S المفتوح المخصص لضغط وبث الكتل والمجسمات ثلاثية الأبعاد وسحب نقاط الليدار بكفاءة عالية عبر متصفحات الإنترنت.",
        {"B": ["Tile packages stream 2D cached raster tiles.", "حزم البلاطات لبث صور الخرائط ثنائية الأبعاد."], "C": ["Map packages are for 2D desktop maps.", "حزم الخرائط للخرائط المكتبية."], "D": ["Vector tile packages stream 2D basemaps.", "حزم البلاطات المتجهة لخرائط الأساس ثنائية الأبعاد."]},
        "packages"
    ),
    # 37: Web Layer Overwrite
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Tool-based", ["Overwrite Web Layer"],
        "When an analyst needs to update the symbology and schema of an existing published Web Layer on ArcGIS Online without breaking downstream dashboards or changing its item ID URL, which workflow must be used?",
        "عندما يحتاج محلل لتحديث رموز وهيكل طبقة ويب منشورة مسبقاً على ArcGIS Online دون تعطيل لوحات المؤشرات (Dashboards) المرتبطة بها أو تغيير معرف الرابط URL، ما مسار العمل الصحيح؟",
        [["Use 'Overwrite Web Layer' from the Share ribbon tab", "استخدام أمر 'Overwrite Web Layer' من تبويب المشاركة Share"], ["Delete the web layer from ArcGIS Online and publish a new layer", "حذف طبقة الويب من ArcGIS Online ونشر طبقة جديدة"], ["Rename the local file geodatabase", "إعادة تسمية قاعدة البيانات المحلية"], ["Export the map to a georeferenced PDF", "تصدير الخريطة إلى ملف PDF جغرافي"]],
        "A",
        "'Overwrite Web Layer' replaces the service definitions and data of an existing hosted web layer in-place, preserving its item ID, service URL, and all dependent web maps and dashboards.",
        "يقوم أمر 'Overwrite Web Layer' باستبدال تعريفات وبيانات خدمة الويب القائمة في مكانها، مع الحفاظ التام على معرف العنصر (Item ID) ورابط الخدمة، مما يمنع تعطل لوحات المؤشرات والتطبيقات المرتبطة بها.",
        {"B": ["Deleting and republishing generates a new item ID, permanently breaking all linked apps and dashboards.", "الحذف وإعادة النشر ينشئ معرفاً جديداً ويعطل كافة التطبيقات المرتبطة."], "C": ["Renaming local files does not update web cloud services.", "إعادة التسمية المحلية لا تحدث الخدمات السحابية."], "D": ["PDF export creates static documents.", "تصدير PDF ينشئ وثيقة ثابتة."]},
        "weblayers"
    ),
    # 38: Sharing: Summary and Tags requirement
    (
        "Choose how to share content from ArcGIS Pro", "Beginner", "Technical", ["Share Web Layer"],
        "When sharing any web layer, map package, or web map from ArcGIS Pro, which metadata fields are strictly mandatory before publishing can proceed?",
        "عند مشاركة أي طبقة ويب أو حزمة خريطة أو خريطة ويب من ArcGIS Pro، ما هي حقول البيانات الوصفية الإلزامية تماماً قبل إمكانية المتابعة والنشر؟",
        [["Title, Summary, and Tags", "Title (العنوان)، Summary (الملخص)، و Tags (الكلمات الدلالية)"], ["Database password and server port", "كلمة مرور قاعدة البيانات ورقم المنفذ"], ["Operating system serial number", "الرقم التسلسلي لنظام التشغيل"], ["Elevation vertical datum name", "اسم المرجع الرأسي للارتفاعات"]],
        "A",
        "ArcGIS item discovery requires three mandatory metadata fields: Title (item name), Summary (short description), and Tags (search keywords). The Share pane disables the publish button until all three are populated.",
        "تتطلب منصات ArcGIS ثلاثة حقول وصفية إلزامية لفهرسة العناصر والبحث عنها: Title (العنوان)، و Summary (الملخص)، و Tags (الكلمات الدلالية)؛ ويتعطل زر النشر حتى يتم ملؤها جميعاً.",
        {"B": ["Database credentials are not required in general sharing metadata.", "بيانات الخادم لا تدخل في البيانات الوصفية العامة."], "C": ["OS serial numbers are private and unrelated.", "الأرقام التسلسلية للحاسب لا علاقة لها بالنشر."], "D": ["Vertical datums are optional spatial reference properties.", "المراجع الرأسية خصائص مكانية اختيارية."]},
        "weblayers"
    ),
    # 39: Print Layout: Tile across pages
    (
        "Identify how to export data, maps, and scenes to different formats", "Intermediate", "Tool-based", ["Print Layout"],
        "When printing a large wall map layout (e.g. 36x48 inches) on a standard office desktop printer that only supports letter-size paper (8.5x11 inches), which print setting tiles the layout across multiple sheets with cut marks?",
        "عند طباعة لوحة حائطية جدارية كبيرة (مثل 36×48 بوصة) باستخدام طابعة مكتبية عادية تدعم ورق Letter فقط (8.5×11 بوصة)، أي إعداد طباعة يقسم اللوحة إلى بلاطات عبر عدة ورقات مع علامات للقص؟",
        [["Tile: Tile all pages (or Tile oversized pages)", "Tile: تجزئة كل الصفحات (Tile oversized pages)"], ["Fit to paper size", "ملاءمة لحجم الورق Fit to paper size"], ["Export to ASCII grid", "التصدير إلى شبكة ASCII"], ["Print black and white only", "الطباعة بالأبيض والأسود فقط"]],
        "A",
        "The Tile oversized pages print option splits a layout larger than the printer's sheet size into a grid of overlapping printed pages, including alignment guidelines and crop marks for assembling the physical wall poster.",
        "يتيح خيار تجزئة الصفحات الكبيرة (Tile oversized pages) تقسيم اللوحات الضخمة إلى شبكة من الورقات المتداخلة مع علامات إرشادية للمحاذاة والقص لتجميع الخريطة الجدارية يدوياً.",
        {"B": ["Fit to paper size shrinks the 48-inch map down to 11 inches, making text unreadably tiny.", "تصغير الصفحة يقلص الخريطة إلى حجم ورقة صغيرة ويجعل النصوص غير مقروءة."], "C": ["ASCII grid is a raster export format.", "شبكة ASCII صيغة تصدير راستر."], "D": ["Color options do not handle physical paper tiling.", "خيارات الألوان لا تقسم الورق."]},
        "exporting"
    ),
    # 40: Map Series: Bookmark Map Series
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Tool-based", ["Bookmark Map Series"],
        "In addition to an Index Layer, what alternative method can be used to generate pages in an ArcGIS Pro Map Series?",
        "بالإضافة إلى استخدام طبقة الفهرس (Index Layer)، ما هي الطريقة البديلة المتاحة لإنشاء صفحات في سلسلة خرائط ArcGIS Pro؟",
        [["Bookmark Map Series (using saved map bookmarks)", "سلسلة خرائط العلامات المرجعية Bookmark Map Series (باستخدام العلامات المرجعية المحفوظة)"], ["Python while loop", "حلقة تكرار بايثون while"], ["Random coordinate generator", "مولد الإحداثيات العشوائية"], ["Buffer analysis", "تحليل النطاق Buffer"]],
        "A",
        "ArcGIS Pro supports Bookmark Map Series, which creates a multi-page series using the extents, scales, and camera angles of bookmarks saved in the map, without requiring an index polygon layer.",
        "يدعم ArcGIS Pro نمط Bookmark Map Series، الذي ينشئ أطلس خرائط متعدد الصفحات بالاعتماد على العلامات المرجعية (Bookmarks) المحفوظة في الخريطة دون الحاجة لوجود طبقة مضلعات فهرس.",
        {"B": ["Bookmark series is built directly in the UI without coding.", "تُبنى سلسلة العلامات المرجعية مباشرة من الواجهة."], "C": ["Random coordinates cannot generate meaningful pages.", "الإحداثيات العشوائية لا تنتج خرائط هادفة."], "D": ["Buffer creates proximity zones.", "النطاق ينشئ مساحات حرم."]},
        "mapseries"
    ),
    # 41: Export Map: Clip to map extent
    (
        "Identify how to export data, maps, and scenes to different formats", "Beginner", "Technical", ["Export Map"],
        "When exporting a 2D Map view directly from the Map tab (without a page layout) to PNG, how do you define the exact geographic bounds of the exported image?",
        "عند تصدير عرض خريطة ثنائية الأبعاد مباشرة من تبويب الخريطة (دون لوحة إخراج) إلى صيغة PNG، كيف تحدد الحدود الجغرافية الدقيقة للصورة المصدرة؟",
        [["Set the 'Clip to extent' parameter in the Export Map pane using custom coordinates or current view extent", "ضبط معامل 'Clip to extent' في نافذة Export Map باستخدام إحداثيات مخصصة أو النطاق المعروض حالياً"], ["Turn the computer monitor upside down", "قلب شاشة الحاسوب"], ["Change the layer transparency to 50%", "تغيير شفافية الطبقة إلى 50%"], ["Export to an Excel file first", "التصدير إلى ملف إكسل أولاً"]],
        "A",
        "In the Export Map pane, the Clip to extent option restricts exported image pixels to a designated coordinate box, current map view, or an existing layer's boundary.",
        "في نافذة تصدير الخريطة (Export Map)، يتيح خيار 'Clip to extent' تقييد حدود الصورة المصدرة بإحداثيات مستطيل مخصص، أو نطاق العرض الحالي، أو حدود طبقة معينة.",
        {"B": ["Physical monitor movement has no effect on software raster export.", "تحريك الشاشة لا يؤثر على التصدير البرمجي."], "C": ["Transparency does not define geographic bounding boxes.", "الشفافية لا تحدد النطاق الجغرافي."], "D": ["Excel does not manage PNG map extents.", "ملفات إكسل لا تدير تصدير صور الخرائط."]},
        "exporting"
    ),
    # 42: Sharing: Vector Tile Layer indexing
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Technical", ["Vector Tile Package"],
        "When creating a Vector Tile Package (.vtpk), what is the function of the Index Polygons generated during the caching process?",
        "عند إنشاء حزمة بلاطات متجهة (.vtpk)، ما وظيفة مضلعات الفهرس (Index Polygons) التي يتم إنشاؤها أثناء عملية بناء الكاش؟",
        [["They optimize tile creation by creating smaller, denser tiles in areas with high feature density and larger tiles in sparse areas", "تحسن عملية بناء البلاطات بإنشاء بلاطات أصغر وأكثر تفصيلاً في المناطق عالية كثافة المعالم وبلاطات أوسع في المناطق المتناثرة"], ["They delete all attributes from point features", "تحذف كافة السمات من المعالم النقطية"], ["They convert line features into raster contours", "تحول الخطوط إلى خطوط كنتور راستر"], ["They calculate real estate property taxes", "تحسب الضرائب العقارية للأراضي"]],
        "A",
        "Vector tile indexing analyzes feature vertex density and builds an optimized quad-tree index, creating appropriately sized tiles that balance visual detail and download speed.",
        "تحلل مضلعات الفهرسة كثافة رؤوس المعالم وتبني شجرة فهارس رباعية (Quad-tree) محسنة، مما يولد بلاطات متجهة متوازنة الحجم تجمع بين التفاصيل العالية وسرعة التنزيل عبر الإنترنت.",
        {"B": ["Indexing does not delete attributes.", "الفهرسة لا تحذف البيانات."], "C": ["Vector tiles remain vector data.", "البلاطات المتجهة تظل بيانات اتجاهية."], "D": ["Tax calculations are outside tile generation.", "حساب الضرائب ليس من وظائف الفهرسة الكارتوغرافية."]},
        "packages"
    ),
    # 43: Layout Pictures: Stored paths
    (
        "Determine how to create and manage map layouts and map series", "Beginner", "Technical", ["Layout Pictures"],
        "When inserting an organization's logo image onto a page layout, what setting ensures the logo remains visible even if the image file on the local hard drive is later moved or deleted?",
        "عند إدراج شعار المؤسسة كصورة في لوحة إخراج، ما الإعداد الذي يضمن بقاء الشعار ظاهراً حتى لو تم نقل ملف الصورة أو حذفه لاحقاً من القرص الصلب؟",
        [["Check 'Save image with document' (embed image) in Picture element properties", "تفعيل خيار 'Save image with document' (تضمين الصورة) في خصائص عنصر الصورة"], ["Rename the picture file with a .txt extension", "إعادة تسمية الصورة بلاحقة .txt"], ["Lock the Windows desktop wallpaper", "قفل خلفية سطح مكتب ويندوز"], ["Export the project to a CSV file", "تصدير المشروع إلى ملف CSV"]],
        "A",
        "Checking 'Save image with document' embeds the picture data directly into the ArcGIS Pro project file (.aprx), severing dependence on the original external file path.",
        "يؤدي اختيار 'Save image with document' إلى تضمين بيانات الصورة مباشرة داخل ملف مشروع ArcGIS Pro (.aprx)، مما يلغي الاعتماد على المسار الخارجي للملف ويمنع تعطل الرابط عند نقل المشروع.",
        {"B": ["Renaming image extensions corrupts the graphic format.", "تغيير لاحقة الملف يتلف تنسيق الصورة."], "C": ["Desktop wallpapers are unrelated to GIS layouts.", "خلفية الشاشة لا علاقة لها بلوحات التصميم."], "D": ["CSV files store tabular text, not image graphics.", "ملفات CSV تخزن نصوصاً جدولية وليست صوراً."]},
        "layouts"
    ),
    # 44: Dynamic Text: Coordinate System format
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Technical", ["Dynamic Text"],
        "Which dynamic text tag automatically reads and displays the projected coordinate system name and projection parameters of the main map frame on the layout border?",
        "أي وسم نص ديناميكي يقرأ ويعرض تلقائياً اسم نظام الإحداثيات المسقط ومعاملات الإسقاط لإطار الخريطة الرئيسي على هامش اللوحة؟",
        [["<dyn type=\"mapFrame\" name=\"Main Map\" property=\"spatialReference\"/>", "<dyn type=\"mapFrame\" name=\"Main Map\" property=\"spatialReference\"/>"], ["<dyn type=\"projection\" name=\"EPSG\"/>", "<dyn type=\"projection\" name=\"EPSG\"/>"], ["$MAP.COORDINATES", "$MAP.COORDINATES"], ["%SpatialReference%", "%SpatialReference%"]],
        "A",
        "ArcGIS Pro dynamic text tags for spatial reference query the map frame properties using `<dyn type=\"mapFrame\" name=\"<FrameName>\" property=\"spatialReference\"/>`, updating automatically if the projection changes.",
        "تستعلم وسوم النصوص الديناميكية للمرجع المكاني عن إطار الخريطة باستخدام الصياغة `<dyn type=\"mapFrame\" name=\"اسم الإطار\" property=\"spatialReference\"/>`، وتتحدث تلقائياً إذا تغير نظام إسقاط الخريطة.",
        {"B": ["This is not a valid ArcGIS Pro dynamic text syntax.", "ليست صياغة وسوم نص ديناميكي صحيحة في البرنامج."], "C": ["Dollar syntax belongs to Arcade.", "صيغة الدولار خاصة بلغة Arcade."], "D": ["Percent syntax is for ModelBuilder.", "صيغة النسبة المئوية خاصة بـ ModelBuilder."]},
        "layouts"
    ),
    # 45: Sharing: Web Map Layer Dependencies
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Technical", ["Web Map"],
        "When sharing an entire 2D map as a Web Map to ArcGIS Online, what happens to feature layers whose underlying data sources are stored in local File Geodatabases on your C: drive?",
        "عند مشاركة خريطة ثنائية الأبعاد بالكامل كخريطة ويب (Web Map) إلى ArcGIS Online، ماذا يحدث لطبقات المعالم المخزنة في قواعد بيانات جغرافية ملفية محلية على القرص C:؟",
        [["Their features and schema are automatically copied and published as hosted feature layers in ArcGIS Online", "يتم نسخ معالمها وهيكلها تلقائياً ونشرها كطبقات معالم مستضافة (Hosted Feature Layers) على سحابة ArcGIS Online"], ["The layers fail to draw and are skipped without notice", "تفشل الطبقات في الظهور ويتم تجاهلها دون تنبيه"], ["The local C: drive is made publicly accessible over the internet", "يصبح قرص الحاسوب C متاحاً للعامة عبر الإنترنت"], ["The feature layers are permanently converted into CAD DXF files", "تتحول طبقات المعالم بشكل دائم إلى ملفات CAD DXF"]],
        "A",
        "ArcGIS Online cannot access local workstation C: drives; therefore, the sharing engine packages the vector features and publishes them as cloud-hosted feature layers associated with the new web map.",
        "نظراً لعدم قدرة منصة ArcGIS Online السحابية على الوصول للقرص المحلي C، يقوم محرك النشر بنسخ المعالم ورفعها تلقائياً كطبقات معالم مستضافة (Hosted Feature Layers) ترتبط بخريطة الويب المنشورة.",
        {"B": ["The sharing wizard handles data upload automatically.", "يتولى معالج النشر رفع البيانات تلقائياً."], "C": ["Local workstations are never exposed to public internet access.", "لا يتم كشف القرص المحلي على الإنترنت."], "D": ["Data is published as web layers, not CAD files.", "تُنشر البيانات كخدمات ويب وليس ملفات CAD."]},
        "weblayers"
    )
]

for i, t in enumerate(ls_data):
    qid = f"LS-{i+1:03d}"
    questions.append(make_q(qid, t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11]))

for i, t in enumerate(more_ls):
    qid = f"LS-{i+26:03d}"
    questions.append(make_q(qid, t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11]))

print(f"Total Layouts & Sharing MCQs built: {len(questions)} (expected 45)")

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Saved layouts-sharing.json successfully.")

