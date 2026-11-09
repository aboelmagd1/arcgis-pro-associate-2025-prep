# -*- coding: utf-8 -*-
"""
Generate all 27 Layouts and Sharing Scenarios (LS-S-001 through LS-S-027) for EAPA_2025.
"""
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_file = os.path.join(base_dir, 'public', 'data', 'scenarios', 'layouts-sharing.json')

ref_map = {
    "layouts": {"title": "Layouts in ArcGIS Pro, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/layouts/layouts-in-arcgis-pro.htm", "kind": "official"},
    "map_series": {"title": "Map series, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/layouts/map-series.htm", "kind": "official"},
    "sharing": {"title": "Share with ArcGIS Pro, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/sharing/overview/share-with-arcgis-pro.htm", "kind": "official"},
    "web_layers": {"title": "Share a web layer, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/sharing/overview/share-a-web-layer.htm", "kind": "official"},
    "packages": {"title": "Package a project, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/sharing/overview/package-a-project.htm", "kind": "official"},
    "export": {"title": "Export a layout or map, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/layouts/export-a-layout-or-map.htm", "kind": "official"}
}

def s(sid, obj, diff, qtype, tools, ctx_en, ctx_ar, q_en, q_ar, opts, ans, exp_en, exp_ar, why, rkey):
    return {
        "id": sid,
        "kind": "scenario",
        "domain": "Layouts and Sharing",
        "objective": obj,
        "difficulty": diff,
        "type": qtype,
        "tools": tools,
        "context": {"en": ctx_en.strip(), "ar": ctx_ar.strip()},
        "question": {"en": q_en.strip(), "ar": q_ar.strip()},
        "options": [
            {"id": "A", "text": {"en": opts[0][0], "ar": opts[0][1]}},
            {"id": "B", "text": {"en": opts[1][0], "ar": opts[1][1]}},
            {"id": "C", "text": {"en": opts[2][0], "ar": opts[2][1]}},
            {"id": "D", "text": {"en": opts[3][0], "ar": opts[3][1]}}
        ],
        "correctAnswer": ans,
        "explanation": {"en": exp_en.strip(), "ar": exp_ar.strip()},
        "incorrectOptionsExplanation": {
            "en": {k: v[0] for k, v in why.items()},
            "ar": {k: v[1] for k, v in why.items()}
        },
        "references": [ref_map[rkey]]
    }

scenarios_data = [
    # 1: Spatial Map Series Core Prerequisites
    (
        "Determine how to create and manage map layouts and map series", "Beginner", "Tool-based", ["Spatial Map Series"],
        "A county GIS department needs to automate the generation of a 45-page zoning atlas book using a standardized layout template. Each page must center on an individual voting precinct.",
        "تحتاج إدارة نظم معلومات جغرافية في مقاطعة إلى أتمتة إنتاج أطلس تخطيطي من 45 صفحة باستخدام قالب لوحة طباعة موحد؛ بحيث تركز كل صفحة على مركز دائرة انتخابية محددة.",
        "What two mandatory settings must be configured to enable a Spatial Map Series?",
        "ما هما الإعدادان الإلزاميان اللذان يجب ضبطهما لتفعيل سلسلة الخرائط المكانية (Spatial Map Series)؟",
        [["An Index Layer (e.g. voting precincts) and a Name Field to identify each page", "طبقة فهرس Index Layer (مثل الدوائر الانتخابية) وحقل اسم Name Field لتمييز كل صفحة"], ["A 3D Local Scene and a TIN surface", "مشهد محلي ثلاثي الأبعاد وسطح TIN"], ["A Python script tool and an SQLite database", "أداة سكربت بايثون وقاعدة بيانات SQLite"], ["A Web Feature Service and an enterprise geodatabase", "خدمة معالم ويب وقاعدة بيانات مؤسسية"]],
        "A",
        "A Spatial Map Series requires an Index Layer (polygon or line feature class defining the geographic extent of each page) and a Name Field specifying each page's unique title or identifier.",
        "تتطلب سلسلة الخرائط المكانية (Spatial Map Series) تحديد طبقة فهرس (Index Layer) تحدد المدى الجغرافي لكل صفحة، وحقل اسم (Name Field) يحدد العنوان أو المعرف الفريد لكل صفحة في الأطلس.",
        {"B": ["Map series operate on 2D map frames, not 3D scenes.", "تعمل سلاسل الخرائط على أطر ثنائية الأبعاد وليس مشاهد ثلاثية."], "C": ["Python scripting is optional; map series is native UI.", "البرمجة اختيارية ومحرك السلاسل مدمج بالواجهة."], "D": ["Map series runs entirely on local project data.", "تعمل السلاسل بالكامل على بيانات المشروع المحلية."]},
        "map_series"
    ),

    # 2: Dynamic Text for Map Series Page Numbering
    (
        "Determine how to create and manage map layouts and map series", "Beginner", "Technical", ["Dynamic Text"],
        "A cartographer designs a layout for a 60-page municipal tax parcel map series. The footer of each page must dynamically display 'Page X of 60' as users flip through pages or export the atlas.",
        "يصمم رسام خرائط لوحة لسلسلة خرائط قطع أراضي عقارية من 60 صفحة؛ ويجب أن يعرض تذييل كل صفحة نصاً ديناميكياً بصيغة 'Page X of 60' مع تقليب الصفحات أو تصدير الأطلس.",
        "Which dynamic text tag syntax correctly formats this page numbering?",
        "أي صيغة لوسوم النصوص الديناميكية تصيغ ترقيم الصفحات هذا بشكل صحيح؟",
        [["Page <dyn type=\"page\" property=\"number\"/> of <dyn type=\"page\" property=\"count\"/>", "Page <dyn type=\"page\" property=\"number\"/> of <dyn type=\"page\" property=\"count\"/>"], ["Page [PAGE_NUM] of [TOTAL_PAGES]", "Page [PAGE_NUM] of [TOTAL_PAGES]"], ["Page %PageNumber% of %TotalCount%", "Page %PageNumber% of %TotalCount%"], ["Page {page.number} of {page.count}", "Page {page.number} of {page.count}"]],
        "A",
        "ArcGIS Pro dynamic text uses XML-based tags: `<dyn type=\"page\" property=\"number\"/>` for the current page number and `<dyn type=\"page\" property=\"count\"/>` for total pages in the series.",
        "تستخدم النصوص الديناميكية في ArcGIS Pro وسوماً مبنية على XML: حيث يعبر `<dyn type=\"page\" property=\"number\"/>` عن رقم الصفحة الحالية، و `<dyn type=\"page\" property=\"count\"/>` عن إجمالي صفحات السلسلة.",
        {"B": ["Square brackets are used in label expressions, not layout dynamic text.", "تُستخدم الأقواس المربعة في التسميات وليس النصوص الديناميكية."], "C": ["Percent signs are used in ModelBuilder substitution.", "تُستخدم النسبة المئوية في ModelBuilder."], "D": ["Curly braces are Python format strings.", "الأقواس المتعرجة تتبع تنسيق بايثون."]},
        "map_series"
    ),

    # 3: Dynamic Text Extracting Index Layer Attribute
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Technical", ["Dynamic Text"],
        "In a county road maintenance map series, the index layer contains an attribute field named 'DISTRICT_ENGINEER'. The layout title block must dynamically display the responsible engineer's name for whatever district is currently shown on the page.",
        "في سلسلة خرائط صيانة طرق المقاطعة، تحتوي طبقة الفهرس على حقل باسم 'DISTRICT_ENGINEER'؛ ويجب أن يعرض مربع عنوان اللوحة اسم المهندس المسؤول عن الدائرة المعروضة حالياً في الصفحة ديناميكياً.",
        "Which dynamic text tag correctly extracts this attribute value from the active page's index feature?",
        "أي وسم نص ديناميكي يستخرج قيمة هذه السمة من معلم الفهرس للصفحة النشطة بشكل صحيح؟",
        [["<dyn type=\"page\" property=\"attribute\" field=\"DISTRICT_ENGINEER\"/>", "<dyn type=\"page\" property=\"attribute\" field=\"DISTRICT_ENGINEER\"/>"], ["<dyn type=\"map\" field=\"DISTRICT_ENGINEER\"/>", "<dyn type=\"map\" field=\"DISTRICT_ENGINEER\"/>"], ["$feature.DISTRICT_ENGINEER", "$feature.DISTRICT_ENGINEER"], ["!DISTRICT_ENGINEER!", "!DISTRICT_ENGINEER!"]],
        "A",
        "The `<dyn type=\"page\" property=\"attribute\" field=\"FieldName\"/>` tag extracts attribute values from the active map series index feature, updating seamlessly across pages.",
        "يستخرج الوسم `<dyn type=\"page\" property=\"attribute\" field=\"FieldName\"/>` قيم السمات مباشرة من معلم فهرس الصفحة الحالية النشطة في سلسلة الخرائط، ويتغير تلقائياً مع كل صفحة.",
        {"B": ["type='map' extracts map properties (scale, coordinate system), not index record fields.", "يستخرج نوع map خصائص الخريطة كالمقياس وليس سمات الفهرس."], "C": ["$feature is Arcade syntax for pop-ups and labeling.", "$feature يتبع تعبيرات Arcade للنوافذ والتسميات."], "D": ["Exclamation marks are used in Calculate Field.", "علامات التعجب لحساب الحقول."]},
        "map_series"
    ),

    # 4: Page Definition Query on Non-Index Layers
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Tool-based", ["Map Series", "Page Query"],
        "A planner creates a map series of school districts. The map also includes a layer of citywide school inspection points containing a 'DISTRICT_ID' attribute. On each page, the planner wants the map to display ONLY the school points that belong to that specific district, hiding schools in adjacent districts.",
        "أنشأ مخطط سلسلة خرائط للمناطق التعليمية؛ وتتضمن الخريطة أيضاً طبقة لنقاط تفتيش المدارس على مستوى المدينة تحوي حقلاً باسم 'DISTRICT_ID'؛ ويريد المخطط في كل صفحة عرض نقاط المدارس التابعة لتلك المنطقة فقط وإخفاء مدارس المناطق المجاورة.",
        "Which layer property in the School Points layer achieves this automatic page-based filtering?",
        "ما هي خاصية الطبقة في نقاط المدارس التي تحقق هذه التصفية التلقائية بناءً على صفحة السلسلة؟",
        [["Configure a Page Definition query in the layer properties matching 'DISTRICT_ID'", "تهيئة استعلام تعريف الصفحة (Page Definition) في خصائص الطبقة بمطابقة حقل 'DISTRICT_ID'"], ["Set the layer transparency to 90%", "ضبط شفافية الطبقة على 90%"], ["Export 50 individual shapefiles manually", "تصدير 50 ملف shapefile يدوياً"], ["Create 50 separate layouts in the project", "إنشاء 50 لوحة طباعة منفصلة في المشروع"]],
        "A",
        "Page Definition queries filter non-index layer features based on an attribute match with the current map series index feature, automatically showing only features belonging to the active page.",
        "يعمل استعلام تعريف الصفحة (Page Definition) على تصفية معالم الطبقات الأخرى بناءً على مطابقة حقل سماتي مع معلم الفهرس للصفحة النشطة، مما يظهر فقط المعالم التابعة للصفحة الحالية آلياً.",
        {"B": ["Transparency dims features across the entire map, failing to isolate districts.", "الشفافية تبهت المعالم ولا تعزل المناطق."], "C": ["Exporting shapefiles is redundant and inefficient.", "تصدير الملفات إجراء مكرر وغير عملي."], "D": ["Creating 50 layouts defeats the purpose of Map Series automation.", "إنشاء 50 لوحة يناقض الغرض من أتمتة السلاسل."]},
        "map_series"
    ),

    # 5: Dynamic Legend Visible Extent Filtering
    (
        "Determine how to create and manage map layouts and map series", "Beginner", "Tool-based", ["Legend Properties"],
        "A cartographer adds a comprehensive municipal land use legend containing 45 distinct zoning classes to a layout. On an inset map focused on a residential subdivision, only 3 zoning classes exist, yet the legend occupies half the layout page displaying all 45 classes.",
        "أضاف رسام خرائط دليلاً شاملاً لاستخدامات الأراضي يحوي 45 فئة تخطيطية إلى اللوحة؛ وفي خريطة تفصيلية تركز على حي سكني لا يوجد به سوى 3 فئات فقط، شغل الدليل نصف الصفحة بعرض كافة الفئات الـ 45.",
        "Which setting in the Legend properties restricts the legend items to show only classes present in the visible view?",
        "ما هو الخيار في خصائص دليل الخريطة (Legend) الذي يقصر عناصر الدليل على عرض الفئات الموجودة في النطاق المرئي فقط؟",
        [["Check 'Only show features visible in the map extent'", "تفعيل خيار 'إظهار المعالم المرئية في نطاق الخريطة فقط' (Only show features visible in the map extent)"], ["Convert the legend to static graphics and delete 42 items manually", "تحويل الدليل إلى رسومات ثابتة وحذف 42 عنصراً يدوياً"], ["Change the layout page orientation from Portrait to Landscape", "تغيير اتجاه صفحة اللوحة من رأسي إلى أفقي"], ["Delete the 42 unused classes from the master database", "حذف الفئات الـ 42 غير المستخدمة من قاعدة البيانات الرئيسية"]],
        "A",
        "Checking 'Only show features visible in the map extent' in Legend Properties dynamically filters the legend to include only layers and symbology classes that currently draw within the visible map frame.",
        "يؤدي تفعيل خيار 'إظهار المعالم المرئية في نطاق الخريطة فقط' في خصائص الدليل إلى تصفيته ديناميكياً ليقتصر على الطبقات وفئات الرموز التي تظهر حالياً داخل الإطار المرئي للخريطة فقط.",
        {"B": ["Converting to graphics breaks dynamic updates when panning or zooming.", "تحويل الدليل لرسومات يقطع التحديث الديناميكي عند التحريك."], "C": ["Page orientation does not filter legend classes.", "اتجاه الصفحة لا يصفي فئات الدليل."], "D": ["Deleting database records corrupts GIS corporate data.", "حذف البيانات يدمر قاعدة البيانات المؤسسية."]},
        "layouts"
    ),

    # 6: Scale Bar Map Frame Association
    (
        "Determine how to create and manage map layouts and map series", "Beginner", "Troubleshooting", ["Scale Bar"],
        "A layout contains two map frames: 'Detail_Frame' (scale 1:2,400) and 'Overview_Locator' (scale 1:100,000). When the cartographer adds a scale bar, it displays distances in hundreds of miles even though it sits directly under 'Detail_Frame'.",
        "تحتوي لوحة طباعة على إطاري خريطة: 'Detail_Frame' (بمقياس 1:2,400) و 'Overview_Locator' (بمقياس 1:100,000)؛ وعندما أضاف الكارتوغرافي مقياس رسم، أظهر مسافات بمئات الأميال رغم وضعه أسفل الإطار التفصيلي مباشرة.",
        "What caused this incorrect scale representation, and how is it corrected?",
        "ما سبب هذا العرض الخاطئ لمقياس الرسم، وكيف يتم تصحيحه؟",
        [["The scale bar is linked to Overview_Locator; change the 'Map Frame' property in the Scale Bar properties to Detail_Frame", "مقياس الرسم مرتبط بـ Overview_Locator؛ ويجب تغيير خاصية 'Map Frame' في خصائص مقياس الرسم إلى Detail_Frame"], ["The computer monitor resolution is too low", "دقة شاشة الحاسوب منخفضة للغاية"], ["The layout must be saved as a PDF first", "يجب حفظ اللوحة كملف PDF أولاً"], ["Scale bars cannot operate in layouts with two map frames", "لا يمكن لمقاييس الرسم العمل في لوحات تحوي إطارين"]],
        "A",
        "Every scale bar is explicitly associated with a single Map Frame. When multiple frames exist, ensure the scale bar's Map Frame dropdown points to the intended detailed frame.",
        "يرتبط كل مقياس رسم في اللوحة بإطار خريطة محدد؛ وعند وجود أكثر من إطار خريطة، يجب التأكد من ضبط القائمة المنسدلة 'Map Frame' في خصائص المقياس على الإطار التفصيلي المطلوب.",
        {"B": ["Hardware monitor resolution does not alter layout cartographic math.", "دقة الشاشة لا تغير الحسابات الكارتوغرافية."], "C": ["PDF export renders the layout as currently configured.", "تصدير PDF يطبع اللوحة بحالتها الراهنة."], "D": ["ArcGIS Pro supports unlimited map frames and associated scale bars.", "يدعم البرنامج عدداً غير محدود من الأطر والمقاييس."]},
        "layouts"
    ),

    # 7: North Arrow Orientations (Map vs True vs Magnetic)
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Conceptual", ["North Arrow"],
        "A cartographer designs a topographic search-and-rescue map in an Arctic region where the map frame is rotated by 35 degrees and geographic longitude meridians converge sharply.",
        "يصمم كارتوغرافي خريطة بحث وإنقاذ طبوغرافية في منطقة قطبية؛ حيث تم تدوير إطار الخريطة بزاوية 35 درجة وتتقارب خطوط الطول الجغرافية بحدة.",
        "What is the difference between setting the North Arrow to 'Map North' versus 'True North'?",
        "ما الفرق بين ضبط سهم الشمال على 'Map North' مقارنة بـ 'True North'؟",
        [["Map North points toward the top edge of the layout page, whereas True North calculates the direction toward the North Pole based on projection equations at the map center", "يشير Map North نحو الحافة العلوية لصفحة اللوحة، بينما يحسب True North الاتجاه نحو القطب الشمالي الجغرافي بناءً على معادلات الإسقاط عند مركز الخريطة"], ["Map North points toward magnetic North", "يشير Map North نحو الشمال المغناطيسي"], ["True North points toward magnetic declination", "يشير True North نحو الانحراف المغناطيسي"], ["Both options produce 100% identical angles at all times", "كلا الخيارين ينتجان زوايا متطابقة تماماً في كافة الأوقات"]],
        "A",
        "Map North points straight up relative to the page orientation. True North calculates the geodetic direction to the geographic North Pole based on the map's coordinate system and central meridian.",
        "يشير Map North رأسياً للأعلى بالنسبة لاتجاه الصفحة؛ بينما يحسب True North الاتجاه الجيوديسي الحقيقي نحو القطب الشمالي الجغرافي وفقاً لنظام إحداثيات الخريطة وخط الزوال المركزي.",
        {"B": ["Magnetic North points toward Earth's magnetic pole using geomagnetic models.", "يشير الشمال المغناطيسي للقطب المغناطيسي."], "C": ["Declination is the difference between True and Magnetic North.", "الانحراف هو الفرق بين الشمالين الحقيقي والمغناطيسي."], "D": ["In rotated or polar projections, Map North and True North diverge significantly.", "في الخرائط المدورة والقطبية يختلف الشمالان بوضوح."]},
        "layouts"
    ),

    # 8: Extent Indicator on Overview Map Frame
    (
        "Determine how to create and manage map layouts and map series", "Beginner", "Tool-based", ["Extent Indicator"],
        "A layout features a large detailed engineering map frame and a small regional overview locator map frame in the bottom corner. The cartographer needs a dynamic rectangle on the regional overview map that shows the exact geographic boundary of the detailed map.",
        "تتضمن لوحة طباعة إطار خريطة هندسية تفصيلية كبيراً، وإطار خريطة دليلية إقليمية صغيرة في الزاوية؛ ويحتاج الكارتوغرافي لمستطيل ديناميكي على الخريطة الإقليمية يوضح الحدود الجغرافية الدقيقة للخريطة التفصيلية.",
        "Which layout element feature accomplishes this dynamic boundary display?",
        "ما هي ميزة عناصر اللوحة التي تحقق هذا العرض الديناميكي للحدود؟",
        [["Select the regional overview map frame, navigate to Insert > Extent Indicator, and link it to the detailed map frame", "تحديد إطار الخريطة الإقليمية، والانتقال إلى Insert > Extent Indicator، وربطه بإطار الخريطة التفصيلية"], ["Draw a static graphic rectangle with the pencil tool", "رسم مستطيل رسومي ثابت بأداة القلم"], ["Export the detailed map to JPEG and insert as a picture", "تصدير الخريطة التفصيلية كصورة JPEG وإدراجها كصورة"], ["Change the coordinate system of both frames to Web Mercator", "تغيير نظام إحداثيات كلا الإطارين إلى Web Mercator"]],
        "A",
        "An Extent Indicator draws a dynamic bounding box or outline on an overview map frame, automatically tracking and displaying the visible geographic extent of another linked map frame.",
        "يرسم مؤشر النطاق (Extent Indicator) مستطيلاً أو حداً ديناميكياً على إطار خريطة الدليل، حيث يتتبع ويحدث تلقائياً المدى الجغرافي المرئي لإطار الخريطة التفصيلي المرتبط به.",
        {"B": ["Graphic rectangles do not update dynamically when the detailed map pans or zooms.", "المستطيلات الرسومية ثابتة ولا تتحدث عند تحريك الخريطة."], "C": ["Static pictures do not track map extent changes.", "الصور الثابتة لا تتتبع تغيرات المدى."], "D": ["Coordinate systems do not create visual extent indicator boxes.", "أنظمة الإحداثيات لا تنشئ مستطيلات مؤشر النطاق."]},
        "layouts"
    ),

    # 9: Measured Grids vs Graticules
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Conceptual", ["Grids and Graticules"],
        "A surveyor prepares a legal boundary map layout and needs grid reference lines across the map frame showing coordinates in State Plane feet (e.g. 2,150,000 ft E, 680,000 ft N).",
        "يعد مساح لوحة خريطة حدود قانونية ويحتاج لخطوط شبكة إحداثية عبر إطار الخريطة تعرض الإحداثيات بأقدام State Plane (مثل 2,150,000 قدم شرقاً و 680,000 قدم شمالاً).",
        "Which grid type must be added to the map frame?",
        "أي نوع من الشبكات يجب إضافته لإطار الخريطة؟",
        [["Measured Grid", "شبكة إحداثيات مسقطة (Measured Grid)"], ["Graticule", "شبكة خطوط الطول والعرض (Graticule)"], ["MGRS Grid", "شبكة MGRS"], ["Custom Overlay Grid", "شبكة تراكب مخصصة"]],
        "A",
        "A Measured Grid displays projected Cartesian coordinates (such as UTM meters or State Plane feet). A Graticule displays geographic coordinates (latitude and longitude in degrees, minutes, seconds).",
        "تعرض الشبكة المسقطة (Measured Grid) الإحداثيات الكارتيزية المسقطة (مثل أمتار UTM أو أقدام State Plane)؛ بينما تعرض Graticule الإحداثيات الجغرافية (خطوط الطول ودوائر العرض بالدرجات والدقائق والثواني).",
        {"B": ["Graticules display angular latitude/longitude, not planar linear feet.", "تعرض Graticule درجات خطوط الطول والعرض وليس الأقدام."], "C": ["MGRS displays military grid reference alphanumeric strings.", "تعرض MGRS رموز الشبكة العسكرية."], "D": ["Custom overlay is used for arbitrary reference keys.", "تُستخدم الشبكة المخصصة للمفاتيح المرجعية العامة."]},
        "layouts"
    ),

    # 10: Project Package (.ppkx) Sharing Scope
    (
        "Choose how to share content from ArcGIS Pro", "Beginner", "Conceptual", ["Project Package"],
        "An engineering consulting firm completes a regional highway expansion study containing 6 separate 2D maps, two 3D scenes, 4 page layouts, custom Python toolboxes, and geodatabase datasets. The firm must deliver the entire workspace to the client as a single portable file.",
        "أكملت شركة استشارات هندسية دراسة توسعة طريق سريع تضم 6 خرائط ثنائية، ومشهدين ثلاثيين، و 4 لوحات طباعة، وصناديق أدوات بايثون مخصصة، وبيانات جغرافية؛ وتريد تسليم مساحة العمل بأكملها للعميل في ملف مدمج واحد.",
        "Which sharing package encapsulates this complete workspace into a single deliverable file?",
        "ما هي حزمة المشاركة التي تدمج مساحة العمل الكاملة هذه في ملف تسليم وحيد؟",
        [["Project Package (.ppkx)", "حزمة المشروع Project Package (.ppkx)"], ["Map Package (.mpkx)", "حزمة الخريطة Map Package (.mpkx)"], ["Layer Package (.lpkx)", "حزمة الطبقة Layer Package (.lpkx)"], ["Geoprocessing Package (.gpkx)", "حزمة المعالجة الجغرافية Geoprocessing Package (.gpkx)"]],
        "A",
        "A Project Package (.ppkx) encapsulates the complete ArcGIS Pro project: all maps, scenes, layouts, custom toolboxes, folder connections, and a consolidated geodatabase containing all underlying datasets.",
        "تجمع حزمة المشروع (.ppkx) مشروع ArcGIS Pro كاملاً: كافة الخرائط والمشاهد ولوحات الطباعة وصناديق الأدوات المخصصة وقاعدة بيانات جغرافية موحدة تحوي كافة البيانات المكانية.",
        {"B": ["A Map Package (.mpkx) contains only a single 2D map or 3D scene.", "تحتوي حزمة الخريطة على خريطة واحدة فقط."], "C": ["A Layer Package (.lpkx) contains only a single layer.", "تحتوي حزمة الطبقة على طبقة واحدة فقط."], "D": ["A GP Package (.gpkx) bundles a single geoprocessing tool.", "تحزم GP Package أداة معالجة جغرافية فقط."]},
        "packages"
    ),

    # 11: Map Package (.mpkx) vs Layer Package (.lpkx)
    (
        "Choose how to share content from ArcGIS Pro", "Beginner", "Conceptual", ["Map Package", "Layer Package"],
        "An analyst needs to share a single environmental sensitivity map (including 5 thematic layers, custom group layer symbology, and standalone lookup tables) with a partner organization, while excluding proprietary business layouts and confidential operational maps stored in the same project.",
        "يحتاج محلل لمشاركة خريطة حساسية بيئية واحدة (تضم 5 طبقات موضوعية، ورموز مخصصة لمجموعات الطبقات، وجداول وصفية) مع جهة شريكة، مع استبعاد لوحات الطباعة والخرائط السرية الأخرى الموجودة في نفس المشروع.",
        "Which package type is appropriate?",
        "ما هو نوع الحزمة الأنسب لتحقيق هذا الغرض؟",
        [["Map Package (.mpkx)", "حزمة الخريطة Map Package (.mpkx)"], ["Project Package (.ppkx)", "حزمة المشروع Project Package (.ppkx)"], ["Style file (.stylx)", "ملف النمط (.stylx)"], ["Layout file (.pagx)", "ملف لوحة الطباعة (.pagx)"]],
        "A",
        "A Map Package (.mpkx) packages a single map or scene along with all its operational layers, tables, symbology, and underlying source datasets, without sharing the rest of the project.",
        "تحزم حزمة الخريطة (.mpkx) خريطة أو مشهداً واحداً بجميع طبقاته التشغيلية وجداوله ورموزه ومصادر بياناته الأصلية، دون مشاركة باقي محتويات المشروع أو اللوحات السرية الأخرى.",
        {"B": ["Project Package shares all maps and confidential layouts in the project.", "تشارك حزمة المشروع كافة الخرائط واللوحات السرية."], "C": ["Style files only store symbol palettes without spatial data.", "تخزن ملفات النمط الرموز فقط دون بيانات مكانية."], "D": ["Layout files (.pagx) do not package underlying data sources.", "لا تحزم ملفات اللوحة مصادر البيانات الأصلية."]},
        "packages"
    ),

    # 12: Layer Package (.lpkx) Corporate Basemap Distribution
    (
        "Choose how to share content from ArcGIS Pro", "Beginner", "Tool-based", ["Layer Package"],
        "A GIS administrator establishes a standardized corporate layer for city boundaries, complete with approved symbol outlines, transparency settings, and labeling rules. Department technicians across various offices need to add this identical layer and its underlying shapefile/gdb data into their own local projects with one click.",
        "أنشأ مسؤول نظم معلومات طبقة موحدة لحدود المدينة برموز معتمدة ونسب شفافية وقواعد تسميات دقيقة؛ ويحتاج فنيو الأقسام في المكاتب المختلفة لإضافة هذه الطبقة المتطابقة وبياناتها المكانية لمشاريعهم بنقرة واحدة.",
        "Which sharing format packages a single operational layer with both its visual symbology and source dataset?",
        "ما هي صيغة المشاركة التي تحزم طبقة تشغيلية واحدة مع رموزها البصرية ومصدر بياناتها المكاني معاً؟",
        [["Layer Package (.lpkx)", "حزمة الطبقة Layer Package (.lpkx)"], ["Layer File (.lyrx)", "ملف الطبقة Layer File (.lyrx)"], ["CSV File (.csv)", "ملف نصي (.csv)"], ["KML File (.kml)", "ملف KML"]],
        "A",
        "A Layer Package (.lpkx) bundles the layer definition (symbology, labeling, queries) AND the underlying source data into a single compressed file. A Layer File (.lyrx) only references external data paths without packaging data.",
        "تجمع حزمة الطبقة (.lpkx) خصائص الطبقة (الرموز، التسميات، الاستعلامات) وبيانات المصدر المكانية معاً في ملف مضغوط واحد؛ بينما يكتفي ملف الطبقة (.lyrx) بتخزين المسار فقط دون تضمين البيانات.",
        {"B": ["Layer files (.lyrx) break when sent to users who lack network access to source paths.", "تنكسر ملفات .lyrx لعدم تضمينها البيانات."], "C": ["CSV files lose symbology and labeling rules completely.", "تفقد ملفات CSV الرموز والتسميات."], "D": ["KML converts GIS features into Google Earth graphic markup.", "يحول KML المعالم لرسومات جوجل إيرث."]},
        "packages"
    ),

    # 13: Geoprocessing Package (.gpkx) Automation Hand-off
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Tool-based", ["Geoprocessing Package"],
        "A spatial modeler creates a custom ModelBuilder tool that automates flood risk prediction. To ensure colleagues can run the model successfully on their workstations, the modeler must package the tool, its execution environment, tool dependencies, and sample test datasets into a single file.",
        "صمم متخصص نمذجة أداة ModelBuilder مخصصة تؤتمت التنبؤ بمخاطر الفيضانات؛ ولضمان قدرة زملائه على تشغيل النموذج بنجاح على أجهزتهم، يجب عليه تحزيم الأداة وبيئة تنفيذها وملفات الارتباط وعينات بيانات الاختبار في ملف واحد.",
        "Which package format packages a geoprocessing workflow and its execution history?",
        "ما هي صيغة الحزمة التي تحزم مسار عمل المعالجة الجغرافية وتاريخ تنفيذه؟",
        [["Geoprocessing Package (.gpkx)", "حزمة المعالجة الجغرافية Geoprocessing Package (.gpkx)"], ["Project Package (.ppkx)", "حزمة المشروع Project Package (.ppkx)"], ["Map Package (.mpkx)", "حزمة الخريطة Map Package (.mpkx)"], ["Desktop Application (.exe)", "تطبيق حاسوب (.exe)"]],
        "A",
        "A Geoprocessing Package (.gpkx) encapsulates custom tools, scripts, models, tool history, and required input/output datasets so workflows can be shared and executed reliably across systems.",
        "تحزم حزمة المعالجة الجغرافية (.gpkx) الأدوات المخصصة والسكربتات والنماذج وسجل التشغيل وبيانات الاختبار المطلوبة لضمان تشغيل مسارات العمل البرمجية بنجاح عبر مختلف الأجهزة.",
        {"B": ["Project Package packages all maps and layouts unnecessarily.", "تحزم حزمة المشروع كافة الخرائط واللوحات بلا داعٍ."], "C": ["Map Package bundles cartographic maps, not GP tools.", "تحزم حزمة الخريطة الخرائط وليس أدوات GP."], "D": ["ArcGIS Pro tools are not compiled into Windows executable .exe files.", "لا تُجمع أدوات ArcGIS Pro كملفات exe تنفيذية."]},
        "packages"
    ),

    # 14: Web Feature Layer for Mobile Field Editing
    (
        "Choose how to share content from ArcGIS Pro", "Beginner", "Technical", ["Web Layers"],
        "A municipal public works department requires field utility crews using ArcGIS Field Maps on mobile tablets to inspect water valves and edit valve status attributes in real time.",
        "تحتاج إدارة أشغال عامة لتمكين فرق الصيانة الميدانية التي تستخدم تطبيق ArcGIS Field Maps على الأجهزة اللوحية من فحص محابس المياه وتعديل سمات حالتها آنياً في الميدان.",
        "Which web layer type must be published from ArcGIS Pro to support web and mobile vector editing?",
        "ما هو نوع طبقة الويب التي يجب نشرها من ArcGIS Pro لدعم تحرير المتجهات عبر الويب والميدان؟",
        [["Web Feature Layer (Feature Service)", "طبقة معالم ويب Web Feature Layer (خدمة معالم)"], ["Tile Layer", "طبقة قوالب Tile Layer"], ["Vector Tile Layer", "طبقة قوالب متجهة Vector Tile Layer"], ["Web Scene", "مشهد ويب Web Scene"]],
        "A",
        "A Web Feature Layer exposes vector geometry and tabular attributes to web and mobile clients, enabling interactive spatial querying, pop-ups, and field editing (geometry and attribute modifications).",
        "تتيح طبقة معالم الويب (Web Feature Layer) هندسة المتجهات وجداول السمات لتطبيقات الويب والميدان، مما يمكن المستخدمين من الاستعلام المكاني، والنوافذ المنبثقة، والتحرير الميداني المباشر للبيانات.",
        {"B": ["Tile Layers are static pre-rendered image caches that do not support editing.", "طبقات البلاطات صور ثابتة ومسبقة المعالجة ولا تدعم التحرير."], "C": ["Vector Tile Layers provide high-speed basemaps but are read-only.", "القوالب المتجهة للقراءة فقط كخرائط أساس."], "D": ["Web Scenes are 3D displays.", "مشاهد الويب للعرض ثلاثي الأبعاد."]},
        "web_layers"
    ),

    # 15: Vector Tile Layer vs Raster Tile Layer Benefits
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Conceptual", ["Vector Tile Layer"],
        "A regional transit authority designs a detailed vector basemap covering a metropolitan area. The authority wants the basemap to render smoothly and crisply at all zoom levels on high-DPI retina mobile screens, and wants the ability to toggle daytime and nighttime color themes dynamically in web browsers without regenerating server tiles.",
        "تصمم هيئة نقل إقليمية خريطة أساس متجهة تفصيلية لمنطقة حضرية؛ وتريد عرض خريطة الأساس بسلاسة ودقة فائقة عند كافة مستويات التكبير على شاشات الهواتف عالية الدقة، مع القدرة على تبديل سمات الألوان ليلياً ونهارياً ديناميكياً في المتصفح دون إعادة بناء القوالب على الخادم.",
        "Which publishing format provides these specific capabilities?",
        "ما هي صيغة النشر التي توفر هذه الإمكانيات المحددة؟",
        [["Vector Tile Layer", "طبقة قوالب متجهة (Vector Tile Layer)"], ["Raster Tile Layer", "طبقة قوالب نقطية (Raster Tile Layer)"], ["Map Image Layer", "طبقة صور الخريطة (Map Image Layer)"], ["KML Network Link", "رابط شبكة KML"]],
        "A",
        "Vector Tile Layers package vector data into compressed binary tiles. They deliver crisp resolution on high-DPI displays at any scale, require minimal server storage, and support dynamic client-side restyling without regenerating tiles.",
        "تحزم طبقات القوالب المتجهة (Vector Tile Layers) البيانات المتجهة في قوالب ثنائية مضغوطة؛ وتوفر وضوحاً فائقاً على الشاشات عالية الدقة عند أي مقياس، مع حجم تخزين صغير، وتدعم إعادة التلوين وتغيير الأنماط من جهة العميل فورياً دون إعادة بناء القوالب.",
        {"B": ["Raster Tile Layers store pre-rendered static PNG/JPEG images that pixelate when zoomed.", "القوالب النقطية صور بكسلية تبهت وتتشوه بالتكبير."], "C": ["Map Image Layers generate dynamic server images on each pan/zoom, requiring Enterprise.", "تولد Map Image Layer صوراً ديناميكية تستهلك موارد الخادم."], "D": ["KML Network links do not provide scalable vector tile styling.", "روابط KML لا تدعم أنماط القوالب المتجهة."]},
        "web_layers"
    ),

    # 16: Sharing Analyzer Errors vs Warnings
    (
        "Choose how to share content from ArcGIS Pro", "Beginner", "Technical", ["Sharing Analyzer"],
        "When an analyst clicks 'Analyze' in the Share As Web Layer pane, the Analyzer tab reports one red error icon (Error 00068: 'Layer's spatial reference does not match') and two yellow warning icons (Warning 24036: 'Layer uses a complex line symbol that will be downgraded').",
        "عندما نقر محلل على 'Analyze' في نافذة مشاركة طبقة ويب (Share As Web Layer)، أظهر تبويب الفاحص أيقونة خطأ حمراء (Error 00068: مرجع الطبقة الإسقاطي غير متطابق) وأيقونتي تحذير صفراوين (Warning 24036: الطبقة تستخدم رمز خط معقداً سيتم تبسيطه).",
        "What is the operational difference between the red error and yellow warnings regarding the 'Publish' button?",
        "ما هو الفرق الإجرائي بين الخطأ الأحمر والتحذيرات الصفراء بالنسبة لزر النشر 'Publish'؟",
        [["Red errors are fatal and disable the Publish button until resolved; yellow warnings do not block publishing and the analyst can proceed without fixing them", "الأخطاء الحمراء قاتلة وتعطل زر النشر تماماً حتى يتم حلها؛ بينما التحذيرات الصفراء لا تمنع النشر ويمكن للمحلل المتابعة دون معالجتها"], ["Yellow warnings block publishing, while red errors are informational only", "التحذيرات الصفراء تمنع النشر بينما الأخطاء الحمراء إرشادية فقط"], ["Both errors and warnings permanently disable the Publish button", "كلا الخطأ والتحذير يعطلان زر النشر بشكل دائم"], ["Neither errors nor warnings affect the Publish button", "لا تؤثر الأخطاء ولا التحذيرات على زر النشر مطلقاً"]],
        "A",
        "In the ArcGIS Pro Sharing Analyzer, Errors (red circles with X) represent fatal issues that completely disable the Publish button until corrected. Warnings (yellow triangles) are advisory notices that do not prevent publishing.",
        "في فاحص المشاركة (Sharing Analyzer) بـ ArcGIS Pro، تمثل الأخطاء الحمراء مشاكل جوهرية قاتلة تعطل زر النشر تماماً حتى معالجتها؛ بينما تمثل التحذيرات الصفراء تنبيهات إرشادية لا تمنع النشر وتسمح بالمتابعة.",
        {"B": ["Red errors block publishing, not warnings.", "الأخطاء الحمراء هي التي تمنع النشر وليس التحذيرات."], "C": ["Warnings do not disable the Publish button.", "التحذيرات لا تعطل زر النشر."], "D": ["Red errors strictly prevent publishing.", "الأخطاء الحمراء تمنع النشر بصرامة."]},
        "web_layers"
    ),

    # 17: Reference Registered Data vs Copy All Data
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Conceptual", ["Sharing to Enterprise"],
        "An enterprise GIS architect publishes 10 feature layers stored in an enterprise Microsoft SQL Server geodatabase to ArcGIS Enterprise. The database is actively updated by 50 staff editors. The architect needs web layers to display live edits immediately without uploading static duplicate snapshots.",
        "ينشر مهندس نظم معلومات مؤسسية 10 طبقات معالم مخزنة في قاعدة بيانات SQL Server مؤسسية إلى ArcGIS Enterprise؛ وتُعدل قاعدة البيانات باستمرار بواسطة 50 محرراً؛ ويجب أن تعرض طبقات الويب التعديلات الحية فورياً دون رفع نسخ مكررة ثابتة.",
        "Which data sharing option must be chosen in the Share As Web Layer pane?",
        "ما هو خيار مشاركة البيانات الذي يجب اختياره في نافذة مشاركة طبقة ويب؟",
        [["'Reference registered data'", "خيار 'الإشارة إلى البيانات المسجلة' ('Reference registered data')"], ["'Copy all data'", "خيار 'نسخ كافة البيانات' ('Copy all data')"], ["'Convert to shapefile'", "خيار 'التحويل إلى shapefile'"], ["'Export to KML'", "خيار 'التصدير إلى KML'"]],
        "A",
        "Choosing 'Reference registered data' configures ArcGIS Enterprise services to read directly from the registered enterprise geodatabase, ensuring web clients view and edit live underlying database records.",
        "يؤدي اختيار 'الإشارة إلى البيانات المسجلة' (Reference registered data) إلى جعل خدمات ArcGIS Enterprise تقرأ مباشرة من قاعدة البيانات المؤسسية المسجلة، مما يضمن عرض وتعديل السجلات الحية فورياً دون نسخ البيانات.",
        {"B": ["'Copy all data' extracts a static snapshot and uploads it to hosted storage, severing live DBMS connections.", "خيار نسخ البيانات يرفع لقطة ثابتة ويقطع الاتصال المباشر."], "C": ["Shapefiles lack enterprise multi-user editing.", "ملفات shapefile لا تدعم التحرير المؤسسي المتزامن."], "D": ["KML is a graphic format, not an enterprise DBMS link.", "صيغة KML للعرض وليست للربط المؤسسي."]},
        "web_layers"
    ),

    # 18: PDF Vector Layers and Text Font Embedding
    (
        "Identify how to export data, maps, and scenes to different formats", "Intermediate", "Tool-based", ["Export Layout"],
        "A cartographer exports a detailed architectural map layout to PDF for professional high-resolution printing. When opening the PDF on the printing company's computers, all custom symbology labels appear substituted with generic courier fonts and road line vectors appear pixelated.",
        "صدر كارتوغرافي لوحة خريطة تفصيلية إلى PDF للطباعة الاحترافية عالية الدقة؛ وعند فتح الملف في مطبعة تجارية، استُبدلت خطوط التسميات بخطوط عادية مشوهة وظهرت خطوط الطرق مبكسلة وفاقدة لحدة المتجهات.",
        "Which two PDF export settings in ArcGIS Pro guarantee crisp vector rendering and prevent font substitution?",
        "ما هما إعدادا تصدير PDF في ArcGIS Pro اللذان يضمنان حدة خطوط المتجهات ويمنعان استبدال الخطوط؟",
        [["Check 'Embed fonts' and select 'Export vector data' (or set Output Image Quality to Best)", "تفعيل خيار 'تضمين الخطوط' (Embed fonts) واختيار 'تصدير البيانات كمتجهات' (Export vector data) أو ضبط جودة الصورة على الأفضل"], ["Increase computer volume to maximum", "رفع مستوى صوت الحاسوب للأعلى"], ["Set layout transparency to 100%", "ضبط شفافية اللوحة على 100%"], ["Export as a monochrome BMP file", "التصدير كملف BMP أحادي اللون"]],
        "A",
        "Checking 'Embed fonts' embeds font glyphs into the PDF document to prevent font substitution, while choosing vector export preserves razor-sharp vector geometries at any print resolution.",
        "يؤدي تفعيل 'تضمين الخطوط' (Embed fonts) إلى دمج الخطوط داخل ملف PDF لمنع استبدالها بخطوط أخرى في أجهزة الطباعة، بينما يضمن تصدير المتجهات بقاء الخطوط والحدود حادة عند أي دقة طباعة.",
        {"B": ["Volume controls audio output, having zero effect on graphics.", "مستوى الصوت للوسائط ولا علاقة له بالرسوم."], "C": ["100% transparency renders the entire document invisible.", "الشفافية الكاملة تخفي محتوى الوثيقة."], "D": ["BMP is an uncompressed raster format that pixelates heavily.", "صيغة BMP راستر وتفقد حدة المتجهات."]},
        "export"
    ),

    # 19: GeoTIFF Spatial Reference Header
    (
        "Identify how to export data, maps, and scenes to different formats", "Beginner", "Technical", ["Export Map"],
        "A remote sensing analyst exports a satellite orthomosaic from an ArcGIS Pro map view as a TIFF image to share with a CAD technician. When the technician adds the TIFF into their CAD software, the image does not align with the engineering drawing, floating at coordinates (0, 0).",
        "صدر محلل استشعار عن بعد صورة فضائية مصححة من خريطة ArcGIS Pro كصورة TIFF لمشاركتها مع مهندس CAD؛ وعند إضافة الصورة لبرنامج CAD لم تتطابق مع الرسم الهندسي وظهرت عائمة عند الإحداثيات (0, 0).",
        "Which export option should the analyst have enabled during the TIFF export to embed georeferencing coordinates directly into the file?",
        "ما هو خيار التصدير الذي كان يجب على المحلل تفعيله أثناء تصدير TIFF لتضمين إحداثيات الإسناد الجغرافي داخل الملف مباشرة؟",
        [["Check 'Write GeoTIFF tags' (or 'Write world file')", "تفعيل خيار 'كتابة وسوم GeoTIFF' (Write GeoTIFF tags) أو كتابة ملف الإسناد العالمي"], ["Export as a JPEG file", "التصدير بصيغة JPEG"], ["Set color depth to 1-bit", "ضبط عمق الألوان على 1 بت"], ["Delete the spatial reference of the map", "حذف المرجع الإسقاطي للخريطة"]],
        "A",
        "GeoTIFF tags embed spatial reference metadata and coordinate bounds directly into the TIFF file header, enabling GIS and CAD software to place and align the raster geographically without floating at (0,0).",
        "تدمج وسوم GeoTIFF بيانات المرجع الإسقاطي وحدود الإحداثيات مباشرة داخل ترويسة ملف TIFF، مما يمكن برامج GIS و CAD من تحديد الموقع الجغرافي للراستر بدقة ومحاذاته مكانياً دون وضعه عند النقطة (0,0).",
        {"B": ["Standard JPEG files without world files lack spatial reference.", "ملفات JPEG العادية تفتقر للإسناد المكاني."], "C": ["1-bit depth converts images to binary black-and-white.", "عمق 1 بت يحول الصورة للأبيض والأسود."], "D": ["Deleting spatial reference strips coordinates entirely.", "حذف الإسناد يفقد الإحداثيات تماماً."]},
        "export"
    ),

    # 20: Offline Sync Capability for Web Feature Layers
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Tool-based", ["Web Layers", "Offline Sync"],
        "An environmental agency publishes a Web Feature Layer for wilderness rangers who inspect remote national park trails where cellular network connectivity is completely nonexistent.",
        "تنشر هيئة بيئية طبقة معالم ويب (Web Feature Layer) لمراقبي الحياة الفطرية الذين يتفقدون مسارات المتنزهات الوطنية النائية حيث تنعدم تغطية شبكات الاتصال الخلوية تماماً.",
        "Which configuration must be enabled in the Web Layer properties before publishing to allow rangers to download map areas and work completely offline?",
        "ما هو الإعداد الذي يجب تفعيله في خصائص طبقة الويب قبل النشر لتمكين المراقبين من تحميل مناطق الخريطة والعمل دون اتصال بالإنترنت تماماً؟",
        [["Enable the 'Sync' capability on the Feature Layer configuration", "تفعيل خاصية المزامنة 'Sync' في تهيئة طبقة المعالم"], ["Set the layer cache to 100 megabytes", "ضبط الذاكرة المؤقتة للطبقة على 100 ميجابايت"], ["Enable time animation on the layer", "تفعيل الرسوم المتحركة الزمنية"], ["Share as a static KML file", "المشاركة كملف KML ثابت"]],
        "A",
        "Enabling the 'Sync' capability on a Web Feature Layer allows mobile apps like ArcGIS Field Maps to download local offline geodatabase replicas to the device and synchronize edits back when connected.",
        "يسمح تفعيل ميزة المزامنة (Sync) على طبقة معالم الويب لتطبيقات الميدان مثل ArcGIS Field Maps بتحميل نسخة محلية من قاعدة البيانات على الجهاز للعمل بلا إنترنت، ثم مزامنة التعديلات آلياً فور توفر الاتصال.",
        {"B": ["Cache size does not enable offline vector transaction replication.", "حجم الكاش لا يفعل مزامنة تحرير المتجهات."], "C": ["Time animation handles temporal playback, not offline sync.", "التحكم الزمني للعرض وليس للمزامنة."], "D": ["KML files are static graphic overlays incapable of database sync.", "ملفات KML رسومات ثابتة لا تدعم المزامنة."]},
        "web_layers"
    ),

    # 21: Map Series Clip to Index Feature
    (
        "Determine how to create and manage map layouts and map series", "Intermediate", "Tool-based", ["Spatial Map Series"],
        "In a city tax assessment map series, each page represents a single city ward. The assessor wants features located outside the boundary of the current ward polygon to be visually masked or clipped out on that page, focusing attention solely on the active ward.",
        "في سلسلة خرائط تقدير العقارات بالمدينة، تمثل كل صفحة حياً بلدياً؛ ويريد المقيم العقاري إخفاء أو حجب كافة المعالم الواقعة خارج حدود مضلع الحي الحالي بصرياً في كل صفحة لتركيز الانتباه على الحي المعني فقط.",
        "Where is this visual masking configured in ArcGIS Pro?",
        "أين يتم ضبط هذا الحجب والإخفاء البصري لمحيط الصفحة في ArcGIS Pro؟",
        [["Map Frame Properties > Extent > Clip to current map series index feature", "خصائص إطار الخريطة Map Frame Properties > تبويب Extent > تفعيل القص وفق معلم فهرس سلسلة الخرائط الحالي (Clip to current map series index feature)"], ["Delete neighboring ward polygons from the database", "حذف مضلعات الأحياء المجاورة من قاعدة البيانات"], ["Apply a 100% transparency filter to all layers", "تطبيق شفافية 100% على كافة الطبقات"], ["Convert the map series to a 3D Global Scene", "تحويل سلسلة الخرائط إلى مشهد عالمي ثلاثي الأبعاد"]],
        "A",
        "Under Map Frame Properties > Extent, selecting 'Clip to current map series index feature' dynamically masks all layers outside the current page's index polygon on every page of the series.",
        "في خصائص إطار الخريطة تحت تبويب Extent، يتيح خيار 'Clip to current map series index feature' حجب وقص كافة الطبقات الواقعة خارج مضلع فهرس الصفحة الحالية ديناميكياً في كل صفحات السلسلة.",
        {"B": ["Deleting features permanently corrupts city boundaries.", "حذف المعالم يدمر بيانات المدينة."], "C": ["100% transparency hides the active ward as well.", "الشفافية الكاملة تخفي الحي النشط أيضاً."], "D": ["Map series requires 2D map frames.", "تتطلب سلاسل الخرائط أطراً ثنائية الأبعاد."]},
        "map_series"
    ),

    # 22: Vector Tile Style Editor Customization
    (
        "Choose how to share content from ArcGIS Pro", "Intermediate", "Tool-based", ["Vector Tiles"],
        "An organization hosts a statewide vector tile basemap. The marketing department requests that the primary highway color be changed from orange to corporate navy blue, and park greens be softened. Rebuilding the vector tile cache from scratch would take 14 hours.",
        "تستضيف مؤسسة خريطة أساس متجهة على مستوى الولاية؛ وطلب قسم التسويق تغيير لون الطرق السريعة الرئيسية من البرتقالي للأزرق الداكن للشركة، وتهدئة خضار الحدائق؛ وتستغرق إعادة بناء قوالب المتجهات من الصفر 14 ساعة كاملة.",
        "How can the GIS administrator update these colors instantly without regenerating the vector tile cache?",
        "كيف يمكن لمسؤول نظم المعلومات تحديث هذه الألوان فورياً دون الحاجة لإعادة بناء قوالب المتجهات من الصفر؟",
        [["Use the ArcGIS Vector Tile Style Editor web app to modify the layer style JSON and save a new style definition", "استخدام تطبيق الويب ArcGIS Vector Tile Style Editor لتعديل ملف نمط الألوان JSON وحفظ تعريف نمط جديد فورياً"], ["Re-run the Create Vector Tile Package tool", "إعادة تشغيل أداة Create Vector Tile Package"], ["Delete the vector tile service from ArcGIS Enterprise", "حذف خدمة القوالب المتجهة من الخادم"], ["Convert all highway polylines to point features", "تحويل كافة خطوط الطرق السريعة إلى نقاط"]],
        "A",
        "Because vector tiles store vector geometries and style rules independently, colors and fonts can be restyled instantly in seconds using the Vector Tile Style Editor by modifying style JSON rules without rebuilding the underlying tiles.",
        "نظراً لأن القوالب المتجهة تفصل بين البيانات الهندسية وقواعد الأنماط، يمكن تعديل الألوان والخطوط في ثوانٍ معدودة عبر محرر أنماط القوالب المتجهة (Vector Tile Style Editor) بتعديل ملف JSON دون الحاجة لإعادة معالجة القوالب.",
        {"B": ["Re-running the tool re-creates the entire 14-hour cache unnecessarily.", "إعادة تشغيل الأداة يستغرق 14 ساعة بلا داعٍ."], "C": ["Deleting the service destroys corporate basemaps.", "حذف الخدمة يدمر خريطة الأساس."], "D": ["Converting lines to points breaks road networks.", "تحويل الخطوط لنقاط يدمر شبكة الطرق."]},
        "web_layers"
    ),

    # 23: Map File (.mapx) vs Layout File (.pagx) Architecture
    (
        "Identify how to export data, maps, and scenes to different formats", "Intermediate", "Conceptual", ["Map and Layout Files"],
        "A university GIS lab instructor prepares standardized templates for an upcoming cartography exam. The instructor needs to provide students with a pre-configured layout template (with page margins, title block, legend placement, and north arrow), but students must supply and link their own data maps.",
        "يعد مدرس معمل جامعي قوالب معيارية لاختبار عملي في الكارتوغرافيا؛ ويحتاج لتزويد الطلاب بقالب لوحة طباعة جاهز (يحتوي هوامش الصفحة، ومربع العنوان، ومكان الدليل، وسهم الشمال)، على أن يقوم الطلاب بربط خرائط بياناتهم الخاصة به.",
        "Which template file format should the instructor distribute?",
        "ما هي صيغة ملف القالب التي يجب على المدرس توزيعها على الطلاب؟",
        [["Layout File (.pagx)", "ملف لوحة الطباعة Layout File (.pagx)"], ["Map File (.mapx)", "ملف الخريطة Map File (.mapx)"], ["Layer File (.lyrx)", "ملف الطبقة Layer File (.lyrx)"], ["Project Package (.ppkx)", "حزمة المشروع Project Package (.ppkx)"]],
        "A",
        "A Layout File (.pagx) saves the layout definition, canvas dimensions, surrounding graphic elements, and map frame arrangements without packaging underlying datasets.",
        "يحفظ ملف لوحة الطباعة (.pagx) هيكل وتصميم اللوحة، وأبعاد الصفحة، والعناصر الرسومية، وتوزيع وترتيب أطر الخرائط، دون تضمين أو تحزيم مجموعات البيانات الأصلية.",
        {"B": ["A Map File (.mapx) stores 2D map views and layer symbology, not page layout sheets.", "يخزن ملف الخريطة .mapx الخرائط وليس لوحات الطباعة."], "C": ["A Layer File (.lyrx) stores single-layer symbology definitions.", "يخزن ملف .lyrx خصائص طبقة واحدة فقط."], "D": ["Project Package includes all underlying data and maps.", "تحزم حزمة المشروع كافة البيانات والخرائط."]},
        "export"
    ),

    # 24: Sharing as Web Map vs Sharing as Web Layer
    (
        "Choose how to share content from ArcGIS Pro", "Beginner", "Conceptual", ["Web Maps"],
        "An analyst configures an ArcGIS Pro project containing 4 operational layers (Parcels, Zoning, Utilities, Flood Zones) overlaid on top of the Esri World Topographic Basemap, complete with configured pop-ups and layer order.",
        "جهز محلل مشروعاً في ArcGIS Pro يحوي 4 طبقات تشغيلية (عقارات، تخطيط، مرافق، فيضانات) مركبة فوق خريطة الأساس الطبوغرافية لـ Esri، مع تهيئة كاملة للنوافذ المنبثقة وترتيب الطبقات.",
        "What is the difference between choosing 'Share As Web Map' versus 'Share As Web Layer'?",
        "ما الفرق بين اختيار 'المشاركة كخريطة ويب' (Share As Web Map) مقارنة بـ 'المشاركة كطبقة ويب' (Share As Web Layer)؟",
        [["'Share As Web Map' publishes all operational layers together along with the basemap, pop-up configurations, and bookmarks as an interactive map ready for Map Viewer; 'Share As Web Layer' publishes a single individual service", "ينشر 'Share As Web Map' كافة الطبقات التشغيلية معاً متضمنة خريطة الأساس والنوافذ المنبثقة والإشارات كخريطة تفاعلية متكاملة لـ Map Viewer؛ بينما ينشر 'Share As Web Layer' خدمة فردية مستقلة"], ["'Share As Web Map' only works with 3D scenes", "تعمل خريطة الويب مع المشاهد ثلاثية الأبعاد فقط"], ["'Share As Web Layer' converts maps into static PDF documents", "تحول طبقة الويب الخرائط إلى وثائق PDF ثابتة"], ["Both options perform the exact same action", "كلا الخيارين ينفذان نفس الإجراء بالضبط"]],
        "A",
        "'Share As Web Map' packages an entire map composition (operational layers, basemap, pop-ups, tables, bookmarks) as a web map item. 'Share As Web Layer' publishes an individual layer or service.",
        "تجمع 'المشاركة كخريطة ويب' (Web Map) التكوين الكامل للخريطة (الطبقات التشغيلية، خريطة الأساس، النوافذ المنبثقة، الإشارات المرجعية) كعنصر خريطة ويب متكامل؛ بينما تنشر 'Web Layer' خدمة طبقة منفردة ومستقلة.",
        {"B": ["3D scenes are shared as Web Scenes, not Web Maps.", "تُشارك المشاهد ثلاثية الأبعاد كـ Web Scenes."], "C": ["Web layers are web services, not static PDF files.", "طبقات الويب خدمات رقمية وليست ملفات PDF."], "D": ["Web maps and web layers are distinct ArcGIS items with different scopes.", "خريطة الويب وطبقة الويب عنصران مختلفان تماماً."]},
        "web_layers"
    ),

    # 25: Multiple Layout Sizes in One Project
    (
        "Determine how to create and manage map layouts and map series", "Beginner", "Tool-based", ["Layouts"],
        "A municipal engineering department works on a capital improvement project. The team needs to produce an ANSI D (24 x 36 inch) architectural poster for public hearings AND an ANSI A (8.5 x 11 inch) portrait report sheet for executive board binders.",
        "يعمل قسم هندسة بلدية على مشروع تطوير رئيسي؛ ويحتاج الفريق لإنتاج ملصق معماري كبير قياس ANSI D (24 × 36 بوصة) لجلسات الاستماع العامة، وتقرير قياس ANSI A (8.5 × 11 بوصة) رأسي لملفات مجلس الإدارة.",
        "How can the team organize these two different paper sizes in ArcGIS Pro?",
        "كيف يمكن للفريق تنظيم هذين القياسين الورقيين المختلفين داخل ArcGIS Pro؟",
        [["Create two separate Layouts within the same single project, each referencing the shared map view at its own page size", "إنشاء لوحتي طباعة منفصلتين داخل نفس المشروع الواحد، تشير كل منهما إلى نفس خريطة العمل المشتركة بقياس الصفحة الخاص بها"], ["Create two entirely separate computer user accounts", "إنشاء حسابي مستخدم منفصلين على نظام التشغيل"], ["ArcGIS Pro projects are limited to exactly one layout size", "مشاريع ArcGIS Pro مقيدة بقياس لوحة طباعة واحد فقط"], ["Convert the project to an AutoCAD drawing", "تحويل المشروع إلى رسم أوتوكاد"]],
        "A",
        "An ArcGIS Pro project (.aprx) can contain multiple layouts of differing sizes, orientations, and aspect ratios, all referencing and displaying the same shared project maps simultaneously.",
        "يمكن لمشروع ArcGIS Pro (.aprx) احتواء عدة لوحات طباعة (Layouts) بقياسات واتجاهات ونسب أبعاد مختلفة، تشير جميعها إلى نفس خرائط المشروع المشتركة وتعرضها بالتزامن.",
        {"B": ["Operating system accounts do not manage layout dimensions.", "حسابات نظام التشغيل لا تدير قياسات الطباعة."], "C": ["ArcGIS Pro has no limit on the number or sizes of layouts in a project.", "لا يفرض البرنامج أي قيود على عدد أو قياسات اللوحات."], "D": ["AutoCAD conversion is unnecessary and loses layout dynamic linking.", "التحويل لأوتوكاد يفقد الربط الديناميكي للوحات."]},
        "layouts"
    ),

    # 26: Color Management: RGB vs CMYK in Export
    (
        "Identify how to export data, maps, and scenes to different formats", "Intermediate", "Conceptual", ["Export Color Management"],
        "A cartographer exports an official state atlas intended for high-end commercial four-color process offset printing presses.",
        "يصدر كارتوغرافي أطلساً رسمياً للولاية مخصصاً لطباعته في مطابع تجارية متقدمة تعمل بنظام الطباعة المزدوجة رباعية الألوان (Offset Press).",
        "Which color model destination profile should be selected during PDF layout export to avoid unexpected color shifts on the printing press?",
        "أي ملف وجهة لنموذج الألوان (Color Model) يجب اختياره أثناء تصدير لوحة PDF لتفادي أي انحرافات غير متوقعة في الألوان في المطبعة؟",
        [["CMYK (Cyan, Magenta, Yellow, Key/Black)", "نموذج ألوان CMYK (السماوي، الأرجواني، الأصفر، الأسود)"], ["RGB (Red, Green, Blue)", "نموذج ألوان RGB (الأحمر، الأخضر، الأزرق)"], ["Grayscale 8-bit", "التدرج الرمادي Grayscale 8-bit"], ["Monochrome 1-bit", "الأحادي 1-bit"]],
        "A",
        "CMYK is the standard subtractive color model for commercial physical printing presses. Selecting CMYK ensures color swatches separate accurately into physical ink plates without unexpected color shifts from RGB screen displays.",
        "يعد نموذج CMYK النموذج اللوني الطرحي القياسي للمطابع الفيزيائية والتجارية؛ ويضمن اختياره فرز الألوان بدقة على صفائح الأحبار دون حدوث انحرافات لونية ناتجة عن التحويل من شاشات RGB الرقمية.",
        {"B": ["RGB is an additive color model designed for digital screens, mobile devices, and the web.", "نموذج RGB مخصص للشاشات الرقمية والويب."], "C": ["Grayscale strips all color, producing shades of gray.", "التدرج الرمادي يفقد كافة الألوان."], "D": ["Monochrome converts everything to black and white.", "النمط الأحادي يحول كل شيء لأبيض وأسود."]},
        "export"
    ),

    # 27: Report Generation (.rptx) Capabilities
    (
        "Determine how to create and manage map layouts and map series", "Beginner", "Tool-based", ["Reports"],
        "A tax assessor needs a multi-page tabular document listing all taxable parcels sorted by district, complete with running page totals, subtotals of assessed land value per neighborhood, and an executive grand total.",
        "يحتاج مقيم ضرائب لوثيقة جدولية متعددة الصفحات تسرد كافة العقارات الخاضعة للضريبة مرتبة حسب الدوائر، مع حساب مجاميع تراكمية لكل صفحة، ومجاميع فرعية لقيم الأراضي بكل حي، وإجمالي عام تنفيذي.",
        "Which ArcGIS Pro project item provides this structured tabular document with grouping and summary calculations?",
        "ما هو عنصر المشروع في ArcGIS Pro الذي يوفر هذه الوثيقة الجدولية المنظمة مع التجميع والحسابات الإحصائية الملخصة؟",
        [["Report (.rptx)", "عنصر التقرير Report (.rptx)"], ["Layout (.pagx)", "لوحة الطباعة Layout (.pagx)"], ["Map (.mapx)", "الخريطة Map (.mapx)"], ["Style (.stylx)", "ملف النمط Style (.stylx)"]],
        "A",
        "An ArcGIS Pro Report generates formatted, multi-page tabular documents from a layer or table, featuring headers, footers, field groupings, and dynamic statistical aggregates (sums, averages, counts).",
        "ينشئ عنصر التقرير (Report) في ArcGIS Pro وثائق جدولية منسقة متعددة الصفحات من طبقة أو جدول، مع دعم الترويسات، والتذييلات، وتجميع الحقول، وحساب المؤشرات الإحصائية الديناميكية (المجموع، المتوسط، العدد).",
        {"B": ["Layouts are designed for spatial cartography and map frames rather than multi-page data tables.", "صُممت اللوحات للخرائط الكارتوغرافية وليس للجداول."], "C": ["Maps display spatial geometries.", "تعرض الخرائط المعالم المكانية."], "D": ["Styles store symbols and colors.", "تخزن الأنماط الرموز والألوان."]},
        "layouts"
    )
]

items = []
for i, item in enumerate(scenarios_data):
    qid = f"LS-S-{i+1:03d}"
    items.append(s(qid, item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]))

print(f"Total LS Scenarios: {len(items)} (target 27)")

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Saved scenarios/layouts-sharing.json successfully.")

