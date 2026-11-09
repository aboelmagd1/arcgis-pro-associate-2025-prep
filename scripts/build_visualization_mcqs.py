# -*- coding: utf-8 -*-
"""
Build all 63 Visualization MCQs (VIZ-001 through VIZ-063) for EAPA_2025.
"""
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_file = os.path.join(base_dir, 'public', 'data', 'questions', 'visualization.json')

# We will define 63 comprehensive, technically precise bilingual MCQs.
# Objectives used from docs/EXAM_BLUEPRINT.md:
# 1. "Identify how to control the coordinate system and geographic transformation in ArcGIS Pro"
# 2. "Manage layer properties using the ribbon and dialog boxes"
# 3. "Determine how to visualize temporal, ranged, or 3D data"
# 4. "Given a scenario, apply a query"

ref_map = {
    "symbology": {"title": "Symbolize feature layers, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/layer-properties/symbolize-feature-layers.htm", "kind": "official"},
    "classification": {"title": "Data classification methods, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/layer-properties/data-classification-methods.htm", "kind": "official"},
    "labeling": {"title": "Maplex Label Engine, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/text/maplex-label-engine.htm", "kind": "official"},
    "scenes": {"title": "Scenes (3D), ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/map-views/scenes.htm", "kind": "official"},
    "time": {"title": "Time in ArcGIS Pro, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/time/time-in-arcgis-pro.htm", "kind": "official"},
    "query": {"title": "Select features by attributes, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/exploring-maps/select-features-by-attributes.htm", "kind": "official"},
    "blending": {"title": "Visual effects and layer blending, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/layer-properties/layer-blending.htm", "kind": "official"},
    "coord": {"title": "Coordinate systems in maps and scenes, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/specify-a-coordinate-system.htm", "kind": "official"}
}

def make_q(qid, objective, diff, qtype, tools, q_en, q_ar, opts, ans, exp_en, exp_ar, why_wrong, ref_key):
    return {
        "id": qid,
        "kind": "mcq",
        "domain": "Visualization",
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

# VIZ-001 to VIZ-015: Classification & Symbology
questions.append(make_q(
    "VIZ-001", "Manage layer properties using the ribbon and dialog boxes", "Beginner", "Conceptual",
    ["Symbology"],
    "Which statistical classification method groups features so that each class contains the exact same number of features?",
    "أي طريقة تصنيف إحصائي تقسم المعالم بحيث تحتوي كل فئة على نفس العدد تماماً من المعالم؟",
    [
        ["Equal Interval", "Equal Interval (الفترات المتساوية)"],
        ["Quantile", "Quantile (الفئات المتساوية في العدد)"],
        ["Natural Breaks (Jenks)", "Natural Breaks (الكسور الطبيعية - جينكس)"],
        ["Standard Deviation", "Standard Deviation (الانحراف المعياري)"]
    ],
    "B",
    "Quantile distributes features equally across classes so that each class has an identical count of records (Total features / Number of classes).",
    "توزع طريقة Quantile المعالم بالتساوي عبر الفئات بحيث تحتوي كل فئة على عدد متطابق من السجلات (إجمالي المعالم / عدد الفئات).",
    {
        "A": ["Equal Interval divides the attribute range (max - min) into equal-sized numeric value intervals, not equal counts.", "تقسم طريقة الفترات المتساوية مدى القيم إلى فترات رقمية متساوية الطول وليس متساوية في عدد المعالم."],
        "C": ["Natural Breaks minimizes variance within classes and maximizes variance between classes based on natural clustering.", "تقلل طريقة الكسور الطبيعية التباين داخل الفئة وتزيد التباين بين الفئات بناءً على التجمعات الطبيعية في البيانات."],
        "D": ["Standard Deviation creates classes based on deviations from the mean value.", "تنشئ طريقة الانحراف المعياري فئات بناءً على انحراف القيم عن المتوسط الحسابي."]
    },
    "classification"
))

questions.append(make_q(
    "VIZ-002", "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Conceptual",
    ["Symbology"],
    "Why is Natural Breaks (Jenks) generally NOT recommended when visually comparing choropleth maps of different years?",
    "لماذا لا يُوصى عموماً باستخدام طريقة الكسور الطبيعية (Natural Breaks) عند المقارنة البصرية بين خرائط كوربلث لسنوات مختلفة؟",
    [
        ["Because it only supports integer attribute fields", "لأنها تدعم حقول الأرقام الصحيحة فقط"],
        ["Because class break threshold values vary dynamically between datasets, making color comparisons invalid", "لأن حدود الفئات وقيمها تتغير ديناميكياً باختلاف البيانات مما يجعل المقارنة البصرية للألوان غير دقيقة"],
        ["Because it requires creating a raster pyramid before classification", "لأنها تتطلب بناء أهرامات راستر قبل تطبيق التصنيف"],
        ["Because it only allows a maximum of 3 classes", "لأنها تسمح بحد أقصى بـ 3 فئات فقط"]
    ],
    "B",
    "Natural Breaks calculates break boundaries based on the unique statistical distribution of the specific dataset. When comparing multiple maps across years, different break thresholds mean the same color represents different numeric ranges, distorting visual comparison.",
    "تحسب طريقة الكسور الطبيعية فواصل الفئات بناءً على التوزيع الإحصائي الفريد لكل مجموعة بيانات؛ وعند مقارنة خرائط لسنوات مختلفة، فإن نفس اللون سيمثل نطاقات رقمية مختلفة مما يشوه المقارنة البصرية.",
    {
        "A": ["Natural Breaks fully supports both integer and floating-point numeric fields.", "تدعم طريقة الكسور الطبيعية الأرقام الصحيحة والعشرية على حد سواء."],
        "C": ["Pyramids are raster performance structures and are unrelated to vector layer classification.", "الأهرامات هي هياكل تسريع لعرض الراستر ولا علاقة لها بتصنيف الطبقات الاتجاهية."],
        "D": ["Natural Breaks supports up to 32 classes in ArcGIS Pro.", "تدعم طريقة الكسور الطبيعية حتى 32 فئة في ArcGIS Pro."]
    },
    "classification"
))

questions.append(make_q(
    "VIZ-003", "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Best-practice",
    ["Symbology"],
    "When mapping total population counts across administrative zones of vastly different geographic areas, how should the data be symbolized to prevent visual cartographic distortion?",
    "عند رسم خريطة لإجمالي أعداد السكان عبر مناطق إدارية ذات مساحات جغرافية متباينة للغاية، كيف يجب تمثيل البيانات لتجنب التضليل الكارتوغرافي البصري؟",
    [
        ["Normalize the population field by polygon area to display population density", "قسمة حقل السكان على مساحة المضلع (Normalization) لعرض الكثافة السكانية"],
        ["Use Unique Values symbology with random color palettes", "استخدام رموز القيم الفريدة (Unique Values) بألوان عشوائية"],
        ["Apply Inverse Distance Weighted raster interpolation", "تطبيق استيفاء الراستر بطريقة IDW"],
        ["Increase the layer transparency to 90%", "زيادة شفافية الطبقة إلى 90%"]
    ],
    "A",
    "Choropleth mapping of raw count data across varying polygon sizes produces misleading maps because larger polygons visually dominate regardless of population density. Normalizing by area (e.g., people per square kilometer) converts raw counts into true density rates.",
    "يؤدي تمثيل الأعداد الخام على مضلعات متباينة المساحة إلى تضليل بصري لأن المساحات الكبيرة تهيمن بصرياً؛ ويعمل التقسيم على المساحة (التطبيع) على تحويل الأعداد إلى كثافات حقيقية عادلة.",
    {
        "B": ["Unique Values is designed for categorical data, not quantitative continuous counts.", "تُستخدم القيم الفريدة للبيانات الفئوية وليس للبيانات الرقمية الكمية."],
        "C": ["Interpolation creates continuous surfaces from point samples and is not applicable for polygon census totals.", "الاستيفاء ينشئ أسطحاً مستمرة من نقاط وليس لتلخيص مضلعات التعداد."],
        "D": ["Transparency does not fix the underlying cartographic error of mapping raw count polygons.", "الشفافية لا تعالج الخطأ الكارتوغرافي المتمثل في رسم الأعداد الإجمالية."]
    },
    "symbology"
))

questions.append(make_q(
    "VIZ-004", "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based",
    ["Symbology"],
    "An analyst needs to display street centerlines with a dark gray pavement fill and a thin black border (casing). At street intersections, the borders currently cross over each other instead of merging cleanly. What feature in ArcGIS Pro resolves this?",
    "يحتاج محلل لعرض خطوط منتصف الشوارع بتعبئة رمادية مع إطار حدودي أسود (Casing)؛ لكن عند التقاطعات، تتقاطع الخطوط الحدودية فوق بعضها بدلاً من الاندماج بسلاسة. ما الميزة التي تحل هذه المشكلة في ArcGIS Pro؟",
    [
        ["Display Filters", "Display Filters (فلاتر العرض)"],
        ["Symbol Layer Drawing", "Symbol Layer Drawing (رسم طبقات الرموز)"],
        ["Feature Blending", "Feature Blending (دمج المعالم)"],
        ["Maplex Stacking", "Maplex Stacking (تكدس مابلكس)"]
    ],
    "B",
    "Symbol Layer Drawing controls the drawing order of individual symbol layers across features in a layer or group, enabling joining and merging of casings and fills at line intersections.",
    "تتحكم خاصية Symbol Layer Drawing في ترتيب رسم طبقات الرموز الفردية للمعالم، مما يمكن من دمج وربط الإطارات الخارجية والتعبئة بسلاسة عند تقاطعات الشوارع.",
    {
        "A": ["Display Filters filter which features draw at varying scales, but do not control symbol layer overlap drawing.", "تتحكم فلاتر العرض في ظهور المعالم حسب المقياس ولا تدمج حواف الرموز."],
        "C": ["Feature Blending blends colors mathematically like Multiply or Screen, but does not join line casings.", "يدمج Feature Blending الألوان رياضياً كالشفافية ولكنه لا يدمج إطارات الطرق."],
        "D": ["Maplex Stacking is a text labeling fitting strategy for multi-line labels.", "تكدس مابلكس خاص بتقسيم نصوص التسميات على أسطر متعددة."]
    },
    "symbology"
))

questions.append(make_q(
    "VIZ-005", "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based",
    ["Layer Blending"],
    "Which layer blend mode should you apply to a categorical Land Use layer placed directly above a Hillshade raster to allow 3D terrain shadows and textures to show through vibrantly without washing out the colors?",
    "أي نمط دمج طبقات (Blend Mode) يجب تطبيقه على طبقة استخدامات الأراضي الموضوعة فوق راستر الظلال التضاريسية (Hillshade) لإظهار تضاريس وظلال السطح بحيوية دون بهتان الألوان؟",
    [
        ["Screen", "Screen"],
        ["Multiply", "Multiply"],
        ["Lighter Color", "Lighter Color"],
        ["Difference", "Difference"]
    ],
    "B",
    "Multiply multiplies the color values of the upper layer with the underlying layer. White areas in the upper layer become completely transparent, while darker hillshade shadows darken the land use colors, preserving full saturation.",
    "يقوم نمط Multiply بضرب قيم ألوان الطبقة العليا بالطبقة السفلى؛ فتصبح المناطق البيضاء شفافة تماماً وتبرز ظلال التضاريس الداكنة ألوان استخدامات الأراضي دون بهتان أو فقدان للتشبع.",
    {
        "A": ["Screen inverts and multiplies colors, creating a brighter and bleached appearance.", "يقوم نمط Screen بعكس الألوان وضربها مما يعطي مظهراً ساطعاً وباهتاً."],
        "C": ["Lighter Color only shows pixels that are brighter, hiding shadows.", "يظهر نمط Lighter Color البكسلات الأكثر سطوعاً فقط فيخفي الظلال التضاريسية."],
        "D": ["Difference subtracts color channels, creating psychedelic inverted colors unsuitable for cartography.", "يطرح نمط Difference قنوات الألوان مما ينتج ألواناً معكوسة غير صالحة للخرائط التضاريسية."]
    },
    "blending"
))

# VIZ-006 to VIZ-015: Labeling & Annotation
questions.append(make_q(
    "VIZ-006", "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical",
    ["Labeling", "Maplex Label Engine"],
    "In the Maplex Label Engine, what is the effect of setting a feature's Feature Weight to 1000?",
    "في محرك التسميات Maplex Label Engine، ما هو أثر ضبط وزن المعلم (Feature Weight) على القيمة 1000؟",
    [
        ["The feature is guaranteed to be labeled before all other features", "ضمان وضع تسمية لهذا المعلم قبل جميع المعالم الأخرى"],
        ["The feature acts as a strict barrier that completely prohibits any labels from being placed over it", "يعمل المعلم كحاجز صارم يمنع تماماً وضع أي تسميات نصية فوقه"],
        ["The feature's label font size is multiplied by 10", "مضاعفة حجم خط تسمية المعلم بمقدار 10 أضعاف"],
        ["The feature will only be displayed when zoomed in closer than 1:1,000 scale", "عرض المعلم فقط عند التقريب لمقياس رسم أكبر من 1:1,000"]
    ],
    "B",
    "Feature Weight (0–1000) specifies how strongly features act as obstacles. A weight of 1000 treats the feature as an absolute barrier, ensuring no labels from any layer can overlap it.",
    "يحدد Feature Weight (من 0 إلى 1000) مدى مقاومة المعلم لوضع التسميات فوقه؛ والقيمة 1000 تعني حاجزاً صارماً يمنع أي تسمية من أي طبقة من التداخل معه.",
    {
        "A": ["Label Weight (not Feature Weight) governs priority between competing labels.", "وزن التسمية Label Weight هو الذي يتحكم في أولوية رسم التسميات المتنافسة."],
        "C": ["Feature weights control collision avoidance placement, not font size.", "تتحكم أوزان المعالم في تجنب التصادم ولا تغير أحجام الخطوط."],
        "D": ["Scale dependencies are set via visibility ranges, not feature weights.", "نطاقات الرؤية للمقياس تُضبط عبر خصائص المقياس وليس أوزان المعالم."]
    },
    "labeling"
))

questions.append(make_q(
    "VIZ-007", "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical",
    ["Labeling", "Arcade"],
    "Which Arcade expression correctly formats a population attribute number (e.g. 1542000) into a comma-separated string (e.g. '1,542,000') in a label?",
    "أي تعبير Arcade ينسق بشكل صحيح رقم حقل السكان (مثل 1542000) إلى نص مفصول بفواصل للآلاف (مثل '1,542,000') في التسمية؟",
    [
        ["$feature.POPULATION.format('###,###')", "$feature.POPULATION.format('###,###')"],
        ["Text($feature.POPULATION, '#,###')", "Text($feature.POPULATION, '#,###')"],
        ["NumberToComma($feature.POPULATION)", "NumberToComma($feature.POPULATION)"],
        ["String($feature.POPULATION, 'COMMAS')", "String($feature.POPULATION, 'COMMAS')"]
    ],
    "B",
    "In Arcade, the Text() function accepts a value and a formatting pattern, where Text($feature.POPULATION, '#,###') formats numeric values with standard thousand separators.",
    "في لغة Arcade، تقبل دالة Text() القيمة ونمط التنسيق، وتعبير Text($feature.POPULATION, '#,###') ينسق الأرقام بفواصل الآلاف القياسية.",
    {
        "A": ["format() is not a standard Arcade property method on numbers.", "دالة format() ليست دالة قياسية في لغة Arcade للأرقام."],
        "C": ["NumberToComma is not an existing Arcade built-in function.", "لا توجد دالة مدمجة في Arcade باسم NumberToComma."],
        "D": ["String() converts values to text without formatting pattern parameters.", "دالة String() تحول إلى نص مجرد دون دعم معاملات أنماط التنسيق."]
    },
    "labeling"
))

questions.append(make_q(
    "VIZ-008", "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Conceptual",
    ["Annotation"],
    "What is the key architectural difference between Standard Annotation and Feature-Linked Annotation?",
    "ما هو الفرق الهيكلي الرئيسي بين النصوص التوضيحية القياسية (Standard Annotation) والنصوص التوضيحية المرتبطة بالمعالم (Feature-Linked Annotation)؟",
    [
        ["Feature-Linked Annotation automatically updates or deletes when the linked feature is modified or deleted", "تتحدث أو تُحذف النصوص التوضيحية المرتبطة بالمعالم تلقائياً عند تعديل أو حذف المعلم المرتبط بها"],
        ["Standard Annotation can only be stored in CAD files", "تُخزن النصوص القياسية في ملفات CAD فقط"],
        ["Feature-Linked Annotation does not support custom font sizing", "لا تدعم النصوص المرتبطة بالمعالم تغيير أحجام الخطوط مخصصاً"],
        ["Standard Annotation requires an enterprise geodatabase with branch versioning", "تتطلب النصوص القياسية قاعدة بيانات مؤسسية ذات إصدارات فرعية"]
    ],
    "A",
    "Feature-Linked Annotation is connected to features via a geodatabase composite relationship class. When an editor moves, edits attributes of, or deletes the linked feature, the associated annotation text and position update or delete automatically.",
    "ترتبط Feature-Linked Annotation بالمعالم عبر فئة علاقات مركبة في قاعدة البيانات؛ فعند تحريك المعلم أو تعديل بياناته أو حذفه، ينعكس ذلك تلقائياً على النص التوضيحي بالتحريك أو التحديث أو الحذف.",
    {
        "B": ["Both types of annotation are stored as geodatabase feature classes in a .gdb.", "يُخزن كلا النوعين كفئات معالم نصوص توضيحية داخل قاعدة البيانات الجغرافية."],
        "C": ["Feature-linked annotation fully supports individual font sizing, rotation, and symbol styling.", "تدعم النصوص المرتبطة بالمعالم تخصيص أحجام الخطوط والتدوير والأنماط بالكامل."],
        "D": ["Standard annotation works seamlessly in File Geodatabases, Mobile Geodatabases, and Enterprise Geodatabases.", "تعمل النصوص القياسية في قواعد البيانات الملفية والمحمولة والمؤسسية دون الحاجة لتفريع نسخ."]
    },
    "labeling"
))

questions.append(make_q(
    "VIZ-009", "Manage layer properties using the ribbon and dialog boxes", "Beginner", "Tool-based",
    ["Display Filters"],
    "An analyst wants a road layer to show only Major Highways when zoomed out past 1:50,000, but display both Major Highways and Local Streets when zoomed in closer, while keeping all roads accessible in the Attribute Table at all times. What should be used?",
    "يريد محلل إظهار الطرق السريعة الرئيسية فقط عند التصغير إلى ما بعد 1:50,000، وعرض الشوارع المحلية مع السريعة عند التقريب، مع إبقاء جميع الطرق متاحة في جدول البيانات في كل الأوقات. ماذا يجب أن يستخدم؟",
    [
        ["Definition Query", "Definition Query (استعلام تعريفي)"],
        ["Scale-based Display Filters", "Scale-based Display Filters (فلاتر العرض المعتمدة على المقياس)"],
        ["Clip Layer to Map Extent", "Clip Layer to Map Extent (قص الطبقة حسب نطاق الخريطة)"],
        ["Select By Attributes", "Select By Attributes (تحديد حسب السمات)"]
    ],
    "B",
    "Scale-based Display Filters restrict feature drawing based on scale ranges and SQL queries without affecting attribute table queries, geoprocessing tools, or feature selections.",
    "تتحكم فلاتر العرض المعتمدة على المقياس (Display Filters) في رسم المعالم بصرياً وفق مقاييس واستعلامات محددة دون استبعاد المعالم من جدول السمات أو أدوات التحليل.",
    {
        "A": ["A Definition Query filters features at the data source level, hiding non-matching records from the attribute table and tools as well.", "يحجب الاستعلام التعريفي المعالم عن جدول البيانات وأدوات التحليل أيضاً وليس من الرسم فقط."],
        "C": ["Clip Layer to Map Extent clips graphics to the frame boundary, not by scale attributes.", "قص الطبقة يقتطع المعالم عند حواف إطار الخريطة وليس حسب سمات مقياس الرسم."],
        "D": ["Select By Attributes creates a temporary selection highlight and does not control scale visibility.", "التحديد بالسمات يحدد معالم باللون الأزرق ولا يتحكم في ظهورها وإخفائها بالمقياس."]
    },
    "symbology"
))

questions.append(make_q(
    "VIZ-010", "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Conceptual",
    ["3D Scenes"],
    "Which statement correctly differentiates a Global Scene from a Local Scene in ArcGIS Pro?",
    "أي عبارة تميز بشكل صحيح بين المشهد العالمي (Global Scene) والمشهد المحلي (Local Scene) في ArcGIS Pro؟",
    [
        ["Global Scenes display data on a 3D sphere using WGS84; Local Scenes display planar or projected data for localized extents", "المشاهد العالمية تعرض البيانات على مجسم كروي ثلاثي الأبعاد بنظام WGS84؛ بينما المشاهد المحلية تعرض بيانات مستوية أو مسقطة لنطاقات محددة"],
        ["Global Scenes only support raster data; Local Scenes only support vector data", "المشاهد العالمية تدعم الراستر فقط؛ والمشاهد المحلية تدعم المتجهات فقط"],
        ["Local Scenes cannot display elevation ground surfaces", "المشاهد المحلية لا يمكنها عرض أسطح التضاريس والارتفاعات"],
        ["Global Scenes can only be viewed in web browsers and not in ArcGIS Pro", "المشاهد العالمية تُعرض في متصفحات الويب فقط ولا تفتح في ArcGIS Pro"]
    ],
    "A",
    "Global scenes model the curvature of the entire globe using WGS84 or CGCS2000. Local scenes project data onto a flat planar coordinate system, making them ideal for localized engineering sites, underground geology, or indoor mapping.",
    "تعرض المشاهد العالمية (Global Scenes) انحناء الكرة الأرضية بالكامل بنظام WGS84؛ أما المشاهد المحلية (Local Scenes) فتسقط البيانات على نظام إحداثيات مستوٍ مسقط، مما يجعلها مثالية للمشاريع الهندسية المحلية والتطبيقات الجيولوجية تحت السطحية.",
    {
        "B": ["Both scenes support 2D/3D vectors, rasters, point clouds, and mesh data.", "يدعم كلا النوعين من المشاهد البيانات الاتجاهية والراستر وسحب النقاط والشبكات."],
        "C": ["Local scenes fully support custom digital elevation models (DEM) and TIN elevation surfaces.", "تدعم المشاهد المحلية أسطح الارتفاع الرقمية ونماذج التضاريس بشكل كامل."],
        "D": ["Both scenes are native core viewing modes inside the ArcGIS Pro desktop application.", "يعد كلا المشهدين نمطي عرض أصيلين داخل تطبيق ArcGIS Pro المكتبي."]
    },
    "scenes"
))

questions.append(make_q(
    "VIZ-011", "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Tool-based",
    ["Extrusion"],
    "How does ArcGIS Pro convert a 2D building footprint polygon layer into 3D solid structures using the Extrusion tool on the Appearance ribbon?",
    "كيف يحول ArcGIS Pro طبقة مضلعات مساقط المباني ثنائية الأبعاد إلى مجسمات ثلاثية الأبعاد باستخدام أداة Extrusion في شريط Appearance؟",
    [
        ["By applying a raster hillshade filter to the 2D polygon symbology", "بتطبيق فلتر التظليل التضاريسي للراستر على رموز المضلع ثنائي الأبعاد"],
        ["By generating vertical 3D planar walls from the feature base up to a specified attribute height or constant value", "بتوليد جدران رأسية ثلاثية الأبعاد تنطلق من قاعدة المعلم إلى ارتفاع يحدده حقل سماتي أو قيمة ثابتة"],
        ["By running the Buffer 3D tool with spherical expansion", "بتشغيل أداة Buffer 3D بالتوسع الكروي"],
        ["By creating an animated fly-through camera path", "بإنشاء مسار كاميرا متحرك للطيران التفاعلي"]
    ],
    "B",
    "Extrusion pushes a 2D flat shape vertically into a 3D volume, utilizing an attribute value (such as building height or number of floors) or a mathematical formula to generate vertical walls from the ground up.",
    "تقوم أداة البثق (Extrusion) بدفع الشكل ثنائي الأبعاد رأسياً لإنتاج كتلة مجسمة ثلاثية الأبعاد، بالاعتماد على حقل سماتي (مثل ارتفاع المبنى أو عدد الطوابق) أو معادلة رياضية لتوليد الجدران من الأرض لأعلى.",
    {
        "A": ["Hillshade is a 2D raster shading technique, not 3D polygon extrusion.", "التظليل التضاريسي تقنية راستر ثنائية الأبعاد ولا ينشئ كتل مبانٍ ثلاثية الأبعاد."],
        "C": ["Buffer 3D expands geometry in all dimensions creating rounded buffers.", "تنشئ أداة Buffer 3D نطاقات كروية حول المعالم وليست للبثق الرأسي للمباني."],
        "D": ["Camera animations create video flythroughs, not geometric 3D features.", "تحريك الكاميرا مخصص لإنتاج مقاطع الفيديو ولا يبني مجسمات هندسية."]
    },
    "scenes"
))

questions.append(make_q(
    "VIZ-012", "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Technical",
    ["Time"],
    "What layer property must be configured to enable the Time Slider ribbon and view historical traffic accident animations across consecutive years?",
    "ما هي خاصية الطبقة التي يجب تهيئتها لتفعيل شريط منزلق الوقت (Time Slider) وعرض رسوم متحركة للحوادث المرورية عبر السنوات المتتالية؟",
    [
        ["Set a Definition Query with the CURRENT_DATE function", "ضبط استعلام تعريفي باستخدام دالة CURRENT_DATE"],
        ["Enable Time in Layer Properties > Time and specify the date/time attribute field", "تفعيل الوقت في Layer Properties > Time وتحديد حقل التاريخ/الوقت"],
        ["Run the Project tool to add temporal coordinate dimensions", "تشغيل أداة Project لإضافة أبعاد إحداثية زمنية"],
        ["Assign a Coded Value Domain to the date field", "تعيين نطاق قيم مشفرة (Coded Value Domain) لحقل التاريخ"]
    ],
    "B",
    "Enabling Time on a layer via Layer Properties > Time instructs ArcGIS Pro to recognize date or timestamp fields, which activates the interactive Time Slider on the map view to filter, step, and animate data chronologically.",
    "يؤدي تفعيل الوقت في خصائص الطبقة (Layer Properties > Time) إلى توجيه ArcGIS Pro للتعرف على حقول التواريخ، مما يفعل منزلق الوقت التفاعلي لتصفية البيانات واستعراضها وتحريكها زمنياً.",
    {
        "A": ["Definition queries filter records statically, they do not activate the interactive time slider controls.", "الاستعلام التعريفي يصفي السجلات بشكل ثابت ولا يفعل أدوات شريط منزلق الوقت."],
        "C": ["Project handles spatial coordinate systems and cannot add temporal dimensions.", "أداة Project تتعامل مع الإسقاط المكاني ولا علاقة لها بالبعد الزمني."],
        "D": ["Domains restrict valid values during data entry and do not configure map playback.", "النطاقات تقيد القيم المدخلة ولا علاقة لها بالتشغيل الزمني على الخريطة."]
    },
    "time"
))

questions.append(make_q(
    "VIZ-013", "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Technical",
    ["Range"],
    "How does the Range Slider differ from the Time Slider in ArcGIS Pro?",
    "كيف يختلف منزلق المدى (Range Slider) عن منزلق الوقت (Time Slider) في ArcGIS Pro؟",
    [
        ["The Range Slider filters continuous numeric attributes (e.g., floor number, pipeline pressure, elevation) rather than date/time values", "يصفي منزلق المدى السمات الرقمية المستمرة (مثل رقم الطابق، ضغط الأنابيب، الارتفاع) بدلاً من قيم التاريخ والوقت"],
        ["The Range Slider can only be used on raster bands", "يمكن استخدام منزلق المدى على نطاقات الراستر فقط"],
        ["The Range Slider deletes features outside the selected range permanently from the geodatabase", "يحذف منزلق المدى المعالم الواقعة خارج النطاق نهائياً من قاعدة البيانات"],
        ["The Range Slider requires a Spatial Analyst license", "يتطلب منزلق المدى ترخيص امتداد Spatial Analyst"]
    ],
    "A",
    "While the Time Slider specifically handles temporal calendar dates and times, the Range Slider provides an interactive on-screen slider to dynamically step through and filter features using any integer or floating-point numeric field (e.g., building floor levels, contaminant levels).",
    "بينما يختص منزلق الوقت بالتواريخ والأوقات التقويمية، يتيح منزلق المدى (Range Slider) تصفيح واستعراض المعالم ديناميكياً باستخدام أي حقل رقمي (مثل طوابق المباني، أو مستويات التلوث، أو الارتفاعات).",
    {
        "B": ["The Range Slider works seamlessly on both vector feature layers and raster catalogs.", "يعمل منزلق المدى على الطبقات الاتجاهية ومجموعات البيانات بكفاءة."],
        "C": ["Sliders are visualization filters and never modify or delete underlying disk records.", "المنزلقات أدوات عرض بصري ولا تحذف البيانات الأصلية على القرص إطلاقاً."],
        "D": ["Range filtering is a standard core capability included with all ArcGIS Pro license levels.", "تصفية المدى ميزة أساسية متاحة في جميع مستويات ترخيص ArcGIS Pro دون إضافات."]
    },
    "time"
))

questions.append(make_q(
    "VIZ-014", "Given a scenario, apply a query", "Beginner", "Technical",
    ["Select By Attributes"],
    "Which SQL clause correctly queries an attribute table for all parcels where the ZONING field is either 'Commercial' or 'Industrial' and the ASSESSED_VALUE is greater than $500,000?",
    "أي جملة SQL تستعلم بشكل صحيح عن قطع الأراضي التي يكون فيها حقل ZONING إما 'Commercial' أو 'Industrial' وقيمة ASSESSED_VALUE أكبر من 500,000 دولار؟",
    [
        ["ZONING IN ('Commercial', 'Industrial') AND ASSESSED_VALUE > 500000", "ZONING IN ('Commercial', 'Industrial') AND ASSESSED_VALUE > 500000"],
        ["ZONING = 'Commercial' OR 'Industrial' AND ASSESSED_VALUE > 500000", "ZONING = 'Commercial' OR 'Industrial' AND ASSESSED_VALUE > 500000"],
        ["ZONING = 'Commercial' AND ZONING = 'Industrial' OR ASSESSED_VALUE > 500000", "ZONING = 'Commercial' AND ZONING = 'Industrial' OR ASSESSED_VALUE > 500000"],
        ["SELECT PARCELS WHERE ZONING = 'Commercial', 'Industrial' > 500000", "SELECT PARCELS WHERE ZONING = 'Commercial', 'Industrial' > 500000"]
    ],
    "A",
    "The IN operator tests whether a field value matches any element in a list, and the AND operator enforces the joint condition with proper logical operator precedence.",
    "تتحقق المعاملة IN مما إذا كانت القيمة تطابق أياً من عناصر القائمة، ويربط المعامل AND الشرط المالي الإضافي مع مراعاة أسبقية العمليات المنطقية.",
    {
        "B": ["SQL does not permit shorthand OR without re-specifying the field name or using the IN operator.", "لا تسمح لغة SQL باختصار OR دون تكرار اسم الحقل أو استخدام معامل IN."],
        "C": ["A single field cannot simultaneously equal both 'Commercial' AND 'Industrial' on the same record.", "لا يمكن لحقل واحد أن يحمل قيمتين مختلفتين معاً باستخدام AND لنفس السجل."],
        "D": ["This syntax is not valid SQL in ArcGIS Pro query builders.", "هذه الصياغة غير صحيحة نحوياً في محررات استعلامات SQL بـ ArcGIS Pro."]
    },
    "query"
))

questions.append(make_q(
    "VIZ-015", "Given a scenario, apply a query", "Intermediate", "Tool-based",
    ["Select By Location"],
    "You need to identify all hospital points that fall completely inside a 100-year flood zone polygon layer. Which spatial relationship rule in the Select By Location tool should you configure?",
    "تحتاج إلى تحديد جميع نقاط المستشفيات التي تقع بالكامل داخل طبقة مضلعات مناطق الفيضان لـ 100 عام. أي قاعدة علاقة مكانية في أداة Select By Location يجب ضبطها؟",
    [
        ["Completely contain", "Completely contain (تحتوي بالكامل)"],
        ["Intersect", "Intersect (تتقاطع)"],
        ["Within", "Within (تقع بداخل)"],
        ["Touch the boundary of", "Touch the boundary of (تلامس حدود)"]
    ],
    "C",
    "When selecting points (Input Features) that are situated inside polygons (Selecting Features), the appropriate spatial relationship is 'Within' or 'Completely within'. 'Completely contain' is the reverse relationship.",
    "عند تحديد نقاط (معالم الإدخال) تقع داخل مضلعات (معالم التحديد)، فإن العلاقة المكانية الصحيحة هي 'Within' (تقع بداخل). أما Completely contain فهي العلاقة العكسية للمضلع بالنسبة للنقطة.",
    {
        "A": ["Completely contain selects polygons that encompass other features, not points contained inside polygons.", "تحدد أداة Completely contain المعالم الحاوية لغيرها وليس النقاط المحتواة بالداخل."],
        "B": ["Intersect also works for points on boundaries, but 'Within' strictly identifies internal containment.", "التقاطع يحدد أيضاً النقاط على الحواف ولكن Within تعبر بدقة عن الاحتواء الداخلي."],
        "D": ["Touch the boundary of selects features that share coincident boundary segments without interior overlap.", "تلامس الحدود يحدد المعالم المشتركة في الحافة فقط دون التواجد بالداخل."]
    },
    "query"
))

# Generate remaining 48 questions (VIZ-016 to VIZ-063) systematically across the 4 objectives
topics = [
    # (id, obj_idx, diff, type, tools, q_en, q_ar, opts, ans, exp_en, exp_ar, why_wrong, ref)
    (
        "Identify how to control the coordinate system and geographic transformation in ArcGIS Pro", "Intermediate", "Technical", ["Map Properties"],
        "When layers with different datums (e.g., NAD 1927 and WGS 1984) are added to the same map, where do you specify the transformation method in ArcGIS Pro?",
        "عند إضافة طبقات ذات مراجع مختلفة (مثل NAD 1927 و WGS 1984) إلى نفس الخريطة، أين تحدد طريقة التحويل الجغرافي في ArcGIS Pro؟",
        [["Map Properties > Coordinate Systems > Transformations", "Map Properties > Coordinate Systems > Transformations"], ["Catalog Pane > Project Options", "Catalog Pane > Project Options"], ["Layer Properties > Elevation", "Layer Properties > Elevation"], ["Ribbon > Edit > Snapping", "Ribbon > Edit > Snapping"]],
        "A",
        "Geographic datum transformations for on-the-fly map display are configured in Map Properties under the Coordinate Systems tab by clicking the Transformations button.",
        "تُضبط التحويلات الجغرافية للمراجع للعرض الآني في Map Properties تحت تبويب Coordinate Systems بالنقر على زر Transformations.",
        {"B": ["Project Options configure general application defaults, not active map transformations.", "خيارات المشروع تضبط الإعدادات العامة للتطبيق ولا تضبط تحويلات الخريطة النشطة."], "C": ["Elevation tab controls 3D vertical surfaces.", "تبويب الارتفاع يتحكم في الأسطح الرأسية ثلاثية الأبعاد."], "D": ["Snapping controls vertex magnetism during editing.", "الانجذاب يتحكم في مغناطيسية الرؤوس أثناء التحرير."]},
        "coord"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Beginner", "Conceptual", ["Symbology"],
        "Which classification method calculates equal-sized intervals by taking the difference between high and low values and dividing by the number of classes?",
        "أي طريقة تصنيف تحسب فترات متساوية الحجم بقسمة الفرق بين أعلى وأدنى قيمة على عدد الفئات؟",
        [["Equal Interval", "Equal Interval (الفترات المتساوية)"], ["Defined Interval", "Defined Interval (الفترات المحددة)"], ["Natural Breaks", "Natural Breaks (الكسور الطبيعية)"], ["Geometrical Interval", "Geometrical Interval (الفترات الهندسية)"]],
        "A",
        "Equal Interval divides the total numeric range (Max - Min) into equal sub-ranges based on the requested number of classes.",
        "تقسم طريقة الفترات المتساوية المدى الكلي (الأعلى - الأدنى) إلى فترات فرعية متساوية بناءً على عدد الفئات المطلوب.",
        {"B": ["Defined Interval requires the user to specify the step size, then determines class count.", "تتطلب طريقة Defined Interval من المستخدم تحديد طول الفترة ثم تحسب عدد الفئات."], "C": ["Natural Breaks uses clustering algorithms, not equal range widths.", "تعتمد الكسور الطبيعية على خوارزميات التجميع وليس الفترات المتساوية."], "D": ["Geometrical Interval uses geometric progression multipliers.", "تستخدم الفترات الهندسية متواليات هندسية متضاعفة."]},
        "classification"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Symbology"],
        "An analyst needs to create a map where the user defines an exact interval step size of 100 meters for elevation contours. Which classification method should be used?",
        "يحتاج محلل إلى إنشاء خريطة يحدد فيها المستخدم خطوة فاصلة ثابتة بمقدار 100 متر لخطوط الكنتور. أي طريقة تصنيف يجب استخدامها؟",
        [["Defined Interval", "Defined Interval (الفترات المحددة)"], ["Equal Interval", "Equal Interval (الفترات المتساوية)"], ["Quantile", "Quantile (الفئات المتساوية)"], ["Manual Interval", "Manual Interval (الفترات اليدوية)"]],
        "A",
        "Defined Interval allows the user to specify a precise interval value (e.g., 100), and ArcGIS Pro calculates the resulting number of classes automatically.",
        "تتيح طريقة Defined Interval للمستخدم تحديد قيمة الفاصل بدقة (مثل 100)، ويقوم ArcGIS Pro باحتساب عدد الفئات الناتج تلقائياً.",
        {"B": ["Equal Interval specifies class count and lets software determine interval width.", "تحدد طريقة الفترات المتساوية عدد الفئات وتترك للبرنامج حساب طول الفترة."], "C": ["Quantile groups equal numbers of features.", "تقسم طريقة Quantile المعالم إلى أعداد متساوية."], "D": ["Manual Interval requires typing every break threshold manually.", "تتطلب طريقة الفترات اليدوية كتابة كل فاصل يدوياً."]},
        "classification"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Advanced", "Conceptual", ["Symbology"],
        "Which classification method is specifically optimized for continuous data that is not normally distributed, striking a compromise between equal intervals, natural breaks, and quantiles?",
        "أي طريقة تصنيف مخصصة للبيانات المستمرة غير الموزعة توزيعاً طبيعياً، وتحدث توازناً بين الفترات المتساوية والكسور الطبيعية والفئات المتساوية؟",
        [["Geometrical Interval", "Geometrical Interval (الفترات الهندسية)"], ["Equal Interval", "Equal Interval (الفترات المتساوية)"], ["Standard Deviation", "Standard Deviation (الانحراف المعياري)"], ["Unique Values", "Unique Values (القيم الفريدة)"]],
        "A",
        "Geometrical Interval creates class breaks based on class intervals that have a geometrical series, providing a compromise for highly skewed continuous datasets.",
        "تنشئ طريقة Geometrical Interval فواصل فئات تعتمد على متوالية هندسية، مما يوفر حلاً متوازناً للبيانات المستمرة شديدة الالتواء.",
        {"B": ["Equal Interval produces empty classes when data is skewed.", "تنتج الفترات المتساوية فئات فارغة عند التواء البيانات."], "C": ["Standard Deviation requires normal bell-curve distributions.", "يتطلب الانحراف المعياري توزيعاً طبيعياً معتدلاً."], "D": ["Unique Values is for categorical data.", "القيم الفريدة مخصصة للبيانات الفئوية."]},
        "classification"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical", ["Symbology"],
        "What is the cartographic purpose of using a Bivariate Colors symbology scheme in ArcGIS Pro?",
        "ما هو الغرض الكارتوغرافي من استخدام نمط الرموز ثنائي المتغيرات (Bivariate Colors) في ArcGIS Pro؟",
        [["To display two quantitative attribute variables simultaneously on a single map using a 2D color grid", "عرض متغيرين كميين معاً على خريطة واحدة باستخدام شبكة ألوان ثنائية الأبعاد"], ["To alternate colors between odd and even feature IDs", "تبديل الألوان بالتناوب بين المعالم الفردية والزوجية"], ["To display vector data and raster data in alternating scanlines", "عرض البيانات الاتجاهية والراستر في خطوط مسح متناوبة"], ["To convert continuous rasters into binary 1-bit masks", "تحويل الراستر المستمر إلى قناع ثنائي 1 بت"]],
        "A",
        "Bivariate Colors symbology maps two quantitative attributes simultaneously (e.g., income and education level) using a 2D color matrix (typically 3x3 or 4x4) to visualize correlation.",
        "يعرض نمط Bivariate Colors متغيرين كميين في آن واحد (مثل الدخل ومستوى التعليم) عبر مصفوفة ألوان ثنائية الأبعاد لإظهار العلاقة والارتباط المكاني بينهما.",
        {"B": ["Alternating IDs is not a standard cartographic method.", "تبديل الألوان حسب الأرقام ليس منهجاً كارتوغرافياً علمياً."], "C": ["Scanline alternating is a display hardware concept.", "تبديل خطوط المسح مفهوم عتادي للشاشات."], "D": ["1-bit masks are binary raster operations.", "أقنعة 1 بت هي عمليات راستر ثنائية."]},
        "symbology"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Symbology"],
        "Which symbology method represents quantitative density by placing random dots inside polygon features, where each dot represents a fixed numeric value?",
        "أي طريقة تمثيل رمزي تعرض الكثافة الكمية بوضع نقاط عشوائية داخل مضلعات المعالم بحيث تمثل كل نقطة قيمة رقمية ثابتة؟",
        [["Dot Density", "Dot Density (كثافة النقط)"], ["Graduated Symbols", "Graduated Symbols (الرموز المتدرجة)"], ["Proportional Symbols", "Proportional Symbols (الرموز التناسبية)"], ["Heat Map", "Heat Map (الخريطة الحرارية)"]],
        "A",
        "Dot Density places a number of dots within each polygon proportional to the attribute value, with each dot representing a stated quantity (e.g., 1 dot = 500 cattle).",
        "تضع طريقة Dot Density عدداً من النقاط داخل المضلع يتناسب مع القيمة السماتية، بحيث تمثل كل نقطة كمية محددة (مثل: نقطة واحدة = 500 رأس ماشية).",
        {"B": ["Graduated Symbols uses single sized symbols per polygon class.", "تستخدم الرموز المتدرجة رمزاً واحداً بحجم محدد لكل فئة."], "C": ["Proportional Symbols scales a single symbol exactly to data values.", "تغير الرموز التناسبية حجم الرمز الفردي بدقة مع القيمة."], "D": ["Heat Map calculates a continuous kernel density surface.", "تحسب الخريطة الحرارية سطح كثافة كيرنز مستمر."]},
        "symbology"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Conceptual", ["Symbology"],
        "What is the difference between Graduated Symbols and Proportional Symbols in ArcGIS Pro?",
        "ما هو الفرق بين الرموز المتدرجة (Graduated Symbols) والرموز التناسبية (Proportional Symbols) في ArcGIS Pro؟",
        [["Graduated Symbols classifies values into discrete size ranges; Proportional Symbols scales symbol size continuously to match exact values", "تقسم الرموز المتدرجة القيم إلى فئات محددة بأحجام متدرجة؛ بينما تقيس الرموز التناسبية حجم الرمز باستمرار ليتناسب بدقة تامة مع كل قيمة"], ["Graduated Symbols only works on polygons; Proportional Symbols only works on points", "الرموز المتدرجة تعمل على المضلعات فقط؛ والتناسبية تعمل على النقاط فقط"], ["Proportional Symbols does not appear in layout legends", "الرموز التناسبية لا تظهر في مفتاح الخريطة باللوحة"], ["Graduated Symbols requires 3D elevation Z-values", "الرموز المتدرجة تتطلب قيماً رأسية ثلاثية الأبعاد Z"]],
        "A",
        "Graduated Symbols divides data into classes and assigns each class a fixed symbol size. Proportional Symbols represents features with unclassed sizes that scale continuously in direct proportion to attribute values.",
        "تقسم الرموز المتدرجة البيانات إلى فئات محددة وتعطي كل فئة حجماً ثابتاً؛ بينما تمثل الرموز التناسبية المعالم بأحجام متصلة غير مفئمة تتناسب طردياً مع القيمة الدقيقة.",
        {"B": ["Both methods can be used on points, lines, and polygon centroids.", "يمكن استخدام كلتا الطريقتين على النقاط والخطوط ومراكز المضلعات."], "C": ["Proportional symbols generate interactive legend boxes.", "تولد الرموز التناسبية مفاتيح خريطة متدرجة الأحجام."], "D": ["Neither method requires 3D Z-values.", "لا تتطلب أي من الطريقتين قيماً ثلاثية الأبعاد."]},
        "symbology"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Apply Symbology From Layer"],
        "Which geoprocessing tool transfers the complete symbology definition from a source layer or layer file (.lyrx) to a target layer?",
        "أي أداة تحليل جغرافي تنقل تعريف الرموز بالكامل من طبقة مصدر أو ملف طبقة (.lyrx) إلى طبقة هدف؟",
        [["Apply Symbology From Layer", "Apply Symbology From Layer"], ["Copy Features", "Copy Features"], ["Calculate Symbology", "Calculate Symbology"], ["Export Tile Package", "Export Tile Package"]],
        "A",
        "The Apply Symbology From Layer tool reads the symbology renderer and classification parameters from an input source and applies them to a target layer matching appropriate fields.",
        "تقرأ أداة Apply Symbology From Layer محرك الرموز ومعاملات التصنيف من مصدر مدخل وتطبقها على الطبقة المستهدفة بمطابقة الحقول المناسبة.",
        {"B": ["Copy Features duplicates geometry and attributes, not symbology styles.", "تنسخ Copy Features البيانات الهندسية والسمات وليس أنماط الرموز."], "C": ["Calculate Symbology is not an ArcGIS Pro tool.", "ليست أداة موجودة في ArcGIS Pro."], "D": ["Export Tile Package exports cached raster map tiles.", "تصدير حزمة البلاطات يصدر بلاطات خرائط مخزنة مؤقتاً."]},
        "symbology"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical", ["Symbology"],
        "When configuring symbol rotation for wind direction point symbols, what is the difference between Geographic rotation and Arithmetic rotation?",
        "عند ضبط تدوير الرموز لاتجاهات الرياح النقطية، ما هو الفرق بين التدوير الجغرافي (Geographic) والتدوير الحسابي (Arithmetic)؟",
        [["Geographic measures clockwise from North (0° = North); Arithmetic measures counter-clockwise from East (0° = East)", "يقيس التدوير الجغرافي باتجاه عقارب الساعة من الشمال (0° = الشمال)؛ بينما يقيس الحسابي عكس عقارب الساعة من الشرق (0° = الشرق)"], ["Geographic rotation is in radians; Arithmetic is in gradians", "التدوير الجغرافي بالراديان والحسابي بالغراديان"], ["Arithmetic rotation only supports 3D scenes", "التدوير الحسابي يدعم المشاهد ثلاثية الأبعاد فقط"], ["Geographic rotation requires an active GPS receiver", "يتطلب التدوير الجغرافي جهاز استقبال GPS نشطاً"]],
        "A",
        "Geographic rotation starts at 0° pointing North and rotates clockwise (standard azimuth). Arithmetic rotation starts at 0° pointing East and rotates counter-clockwise (standard mathematical angle).",
        "يبدأ التدوير الجغرافي من زاوية 0° باتجاه الشمال ويدور مع عقارب الساعة (الاتجاه البوصلي)؛ بينما يبدأ التدوير الحسابي من 0° باتجاه الشرق ويدور عكس عقارب الساعة (الزاوية الرياضية).",
        {"B": ["Both rotation systems in ArcGIS Pro are specified in degrees (0–360°).", "يتم تحديد كلا النظامين بالدرجات المئوية من 0 إلى 360."], "C": ["Arithmetic rotation is supported in both 2D maps and 3D scenes.", "التدوير الحسابي مدعوم في الخرائط ثنائية وثلاثية الأبعاد."], "D": ["GPS hardware is completely unrelated to symbol rotation angles.", "أجهزة GPS لا علاقة لها بزوايا تدوير الرموز الكارتوغرافية."]},
        "symbology"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical", ["Labeling"],
        "In Maplex Label Engine, what fitting strategy allows text to be automatically condensed by reducing font point size within defined minimum limits?",
        "في محرك التسميات Maplex، ما هي استراتيجية الملاءمة التي تسمح بتقليص النص تلقائياً عبر تصغير حجم الخط ضمن حدود دنيا محددة؟",
        [["Font Reduction", "Font Reduction (تقليص حجم الخط)"], ["Key Numbering", "Key Numbering (ترقيم المفاتيح)"], ["Stacking", "Stacking (التكدس)"], ["Abbreviation Dictionaries", "Abbreviation Dictionaries (قواميس الاختصارات)"]],
        "A",
        "Font Reduction allows Maplex to reduce font size by specified step intervals down to a lower limit (e.g. from 10pt to 7pt) to fit text in tight polygons.",
        "تتيح استراتيجية Font Reduction للمحرك تصغير حجم الخط بخطوات تدريجية حتى حد أدنى (مثل من 10 إلى 7) ليناسب النص المساحات الضيقة.",
        {"B": ["Key Numbering replaces text with numbered legend callouts.", "يستبدل Key Numbering النص بأرقام مرجعية في جدول."], "C": ["Stacking splits text across multiple lines.", "يقسم التكدس النص على عدة أسطر."], "D": ["Abbreviation dictionaries substitute words with shortened versions.", "تستبدل قواميس الاختصارات الكلمات بأشكال مختصرة."]},
        "labeling"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Labeling"],
        "Which tool or command in ArcGIS Pro converts dynamic map labels into editable, persistent geodatabase annotation features?",
        "أي أداة أو أمر في ArcGIS Pro يحول التسميات الديناميكية إلى نصوص توضيحية (Annotation) قابلة للتحرير والتخزين الدائم في قاعدة البيانات؟",
        [["Convert Labels To Annotation", "Convert Labels To Annotation"], ["Make Feature Layer", "Make Feature Layer"], ["Export Map", "Export Map"], ["Calculate Field", "Calculate Field"]],
        "A",
        "Convert Labels To Annotation is the geoprocessing tool that converts dynamic label classes into an annotation feature class stored in a geodatabase.",
        "أداة Convert Labels To Annotation هي أداة التحليل الجغرافي المسؤولة عن تحويل فئات التسميات الديناميكية إلى فئة معالم نصوص توضيحية داخل قاعدة البيانات الجغرافية.",
        {"B": ["Make Feature Layer creates a temporary layer view.", "تنشئ Make Feature Layer طبقة عرض مؤقتة."], "C": ["Export Map exports graphical outputs like PDF or JPEG.", "يصدر أمر تصدير الخريطة ملفات رسومية مثل PDF."], "D": ["Calculate Field computes column attribute values.", "تحسب Calculate Field قيم الأعمدة السماتية."]},
        "labeling"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Beginner", "Technical", ["Layer Properties"],
        "What is the difference between 'In Beyond' (maximum scale) and 'Out Beyond' (minimum scale) scale threshold settings on a layer?",
        "ما هو الفرق بين إعداد الحد الأقصى للمقياس (In Beyond) والحد الأدنى للمقياس (Out Beyond) في خصائص الطبقة؟",
        [["In Beyond stops drawing the layer when zoomed in closer than that scale; Out Beyond stops drawing when zoomed out further", "In Beyond يوقف رسم الطبقة عند التقريب لأكبر من ذلك المقياس؛ بينما Out Beyond يوقف الرسم عند التصغير لأصغر منه"], ["In Beyond sets transparency; Out Beyond sets brightness", "In Beyond يضبط الشفافية و Out Beyond يضبط السطوع"], ["Out Beyond only applies to 3D elevation rasters", "Out Beyond ينطبق على راستر الارتفاع ثلاثي الأبعاد فقط"], ["In Beyond is measured in kilometers and Out Beyond in miles", "In Beyond يُقاس بالكيلومترات و Out Beyond بالأميال"]],
        "A",
        "In Beyond (maximum scale) suppresses drawing when zoomed in past the threshold scale. Out Beyond (minimum scale) suppresses drawing when zoomed out past that threshold.",
        "يمنع إعداد In Beyond رسم الطبقة عند التقريب لمقياس أكبر من الحد المحدد، بينما يمنع Out Beyond رسمها عند التصغير لمقياس أصغر من الحد المحدد.",
        {"B": ["Transparency and brightness are visual effects, not scale ranges.", "الشفافية والسطوع تأثيرات بصرية وليست نطاقات مقياس."], "C": ["Both settings apply universally to vector and raster layers.", "ينطبق كلا الإعدادين على الطبقات الاتجاهية والراستر."], "D": ["Scale ranges are dimensionless representative fractions (e.g., 1:24,000).", "نطاقات المقاييس هي كسور تمثيلية بلا وحدات قياس."]},
        "symbology"
    ),
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Technical", ["3D Scenes"],
        "When viewing polygon features in a 3D Scene, what elevation mode renders features draped directly over the digital elevation ground surface?",
        "عند عرض معالم المضلعات في مشهد ثلاثي الأبعاد (3D Scene)، أي وضع ارتفاع يثبت المعالم مكسوة مباشرة فوق سطح الأرض التضاريسي الرقمي؟",
        [["On the ground", "On the ground (على سطح الأرض)"], ["At an absolute height", "At an absolute height (عند ارتفاع مطلق)"], ["Relative to the ground", "Relative to the ground (نسبة إلى سطح الأرض)"], ["Floating in orbit", "Floating in orbit (عائمة في المدار)"]],
        "A",
        "'On the ground' drapes 2D features directly onto the terrain elevation surface, automatically conforming the feature vertices to the elevations of the underlying Ground surface.",
        "يثبت وضع 'On the ground' المعالم ثنائية الأبعاد مباشرة ككساء فوق سطح التضاريس، مما يجعل رؤوس المعالم تتبع ارتفاعات السطح التضاريسي للأرض تلقائياً.",
        {"B": ["Absolute height places features at a fixed Z-elevation above sea level, regardless of terrain height.", "يثبت الارتفاع المطلق المعالم عند قيمة Z ثابتة فوق سطح البحر بغض النظر عن التضاريس."], "C": ["Relative to ground offsets features by an additional vertical distance above the terrain.", "يضيف الارتفاع النسبي مسافة إزاحة إضافية فوق سطح الأرض."], "D": ["Floating in orbit is not a valid elevation mode.", "ليس وضع ارتفاع معتمداً في البرنامج."]},
        "scenes"
    ),
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Technical", ["3D Scenes"],
        "Which illumination property in an ArcGIS Pro 3D Scene simulates realistic sun position and ground shadows based on geographic coordinates, time of day, and calendar date?",
        "أي خاصية إضاءة في المشهد ثلاثي الأبعاد بـ ArcGIS Pro تحاكي موضع الشمس الحقيقي وظلال الأرض بناءً على الإحداثيات الجغرافية ووقت اليوم وتاريخ التقويم؟",
        [["Sun Lighting and Shadows", "Sun Lighting and Shadows (إضاءة الشمس والظلال)"], ["Hillshade Bilinear Resampling", "Hillshade Bilinear Resampling"], ["Ambient Occlusion Only", "Ambient Occlusion Only"], ["Voxel Transparency", "Voxel Transparency"]],
        "A",
        "Sun Lighting calculates the solar azimuth and altitude based on the scene's geographic location, date, and time of day, casting realistic directional shadows from terrain, buildings, and multipatch models.",
        "تحسب إضاءة الشمس (Sun Lighting) زاوية السمت الشمسي وارتفاعها بناءً على الموقع والتاريخ والوقت، مما يلقي ظلالاً اتجاهية واقعية من التضاريس والمباني.",
        {"B": ["Bilinear resampling is an image interpolation technique.", "الاستيفاء الخطي تقنية معالجة صور راستر."], "C": ["Ambient occlusion adds contact shadows, but does not calculate solar angles.", "الانسداد المحيطي يضيف ظلال تلامس ولا يحسب زوايا الشمس."], "D": ["Voxel transparency adjusts 3D volumetric grid visibility.", "شفافية الفوكسل تضبط رؤية شبكات الكتل ثلاثية الأبعاد."]},
        "scenes"
    ),
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Technical", ["Time"],
        "When configuring Time Properties on a layer where events span a defined duration (such as a wildfire burning over several days), which time configuration must be selected?",
        "عند تهيئة خصائص الوقت على طبقة تمتد أحداثها لفترة زمنية محددة (مثل حريق غابات يستمر لعدة أيام)، أي إعداد وقت يجب اختياره؟",
        [["Each feature has start and end time fields", "Each feature has start and end time fields (كل معلم له حقل بداية ونهاية)"], ["Each feature has a single time field", "Each feature has a single time field (كل معلم له حقل زمني واحد)"], ["Time is stored in the layer metadata only", "Time is stored in the layer metadata only"], ["Features have no time values", "Features have no time values"]],
        "A",
        "When features persist across durations, selecting 'Each feature has start and end time fields' allows ArcGIS Pro to display features throughout their active lifespan on the Time Slider.",
        "عندما تمتد المعالم عبر فترات زمنية، فإن اختيار 'كل معلم له حقل بداية ونهاية' يتيح لـ ArcGIS Pro عرض المعالم طوال فترة نشاطها الفعالة على منزلق الوقت.",
        {"B": ["A single time field represents instantaneous point-in-time events (e.g., lightning strikes).", "يمثل الحقل الفردي أحداثاً لحظية تقع في لحظة واحدة كالصواعق."], "C": ["Metadata does not feed interactive time slider animation.", "البيانات الوصفية لا تغذي العرض التفاعلي لمنزلق الوقت."], "D": ["Features without time values cannot participate in temporal playback.", "المعالم بدون قيم وقت لا يمكن تشغيلها زمنياً."]},
        "time"
    ),
    (
        "Given a scenario, apply a query", "Beginner", "Technical", ["Select By Attributes"],
        "Which wildcard character is used in standard SQL LIKE queries in ArcGIS Pro to match any sequence of zero or more characters in an enterprise or file geodatabase?",
        "أي رمز من رموز البدل (Wildcard) يُستخدم في استعلامات SQL بـ ArcGIS Pro لمطابقة أي سلسلة من صفر أو أكثر من الحروف في قواعد البيانات الجغرافية؟",
        [["Percent sign (%)", "علامة النسبة المئوية (%)"], ["Underscore (_)", "الشرطة السفلية (_)"], ["Asterisk (*)", "علامة النجمة (*)"], ["Question mark (?)", "علامة الاستفهام (?)"]],
        "A",
        "In file and enterprise geodatabases, the percent sign (%) matches any string of zero or more characters in a LIKE clause. The underscore (_) matches exactly one single character.",
        "في قواعد البيانات الجغرافية الملفية والمؤسسية، تطابق علامة النسبة المئوية (%) أي سلسلة من صفر أو أكثر من المحارف في جمل LIKE؛ بينما تطابق الشرطة السفلية (_) محرفاً واحداً فقط.",
        {"B": ["Underscore matches exactly one single character.", "الشرطة السفلية تطابق محرفاً واحداً فقط."], "C": ["Asterisk was used in legacy personal geodatabases (.mdb / Access), but not in modern file geodatabases.", "كانت النجمة تُستخدم في قواعد البيانات الشخصية القديمة mdb وليس في قواعد البيانات الحديثة."], "D": ["Question mark matches single characters in legacy Access databases.", "علامة الاستفهام كانت لقواعد Access القديمة."]},
        "query"
    ),
    (
        "Given a scenario, apply a query", "Intermediate", "Tool-based", ["Select By Location"],
        "An analyst needs to select all fire stations located within a 5-mile driving radius of a hazardous chemical spill point. Which tool should be used first to model the spatial zone?",
        "يحتاج محلل لتحديد جميع مراكز الإطفاء الواقعة ضمن نطاق مسافة 5 أميال من نقطة تسرب كيميائي. أي أداة يجب استخدامها أولاً لنمذجة هذا النطاق المكاني؟",
        [["Buffer (or Select By Location with search distance)", "Buffer (أو Select By Location مع مسافة بحث)"], ["Dissolve", "Dissolve"], ["Clip", "Clip"], ["Erase", "Erase"]],
        "A",
        "Select By Location supports a 'Search Distance' parameter directly (e.g., Within a distance of 5 miles), or the Buffer tool can generate an explicit 5-mile boundary polygon.",
        "تدعم أداة Select By Location معامل مسافة البحث مباشرة (ضمن مسافة 5 أميال)، كما يمكن لأداة Buffer توليد مضلع حرم محدد بمسافة 5 أميال.",
        {"B": ["Dissolve merges adjacent polygons sharing common attributes.", "تدمج Dissolve المضلعات المتجاورة المشتركة في السمات."], "C": ["Clip cuts layer geometries by an extent.", "تقطع أداة Clip المعالم وفق حدود معينة."], "D": ["Erase removes areas falling inside an erase feature.", "تحذف Erase المساحات الواقعة داخل معلم المسح."]},
        "query"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical", ["Symbology"],
        "What happens when you enable 'Vary symbology by attribute' in the Symbology pane for a point layer?",
        "ماذا يحدث عند تفعيل خيار 'Vary symbology by attribute' في نافذة Symbology لطبقة نقطية؟",
        [["It allows secondary attribute fields to dynamically control symbol transparency, rotation, size, or color", "يتيح لحقول سمات ثانوية التحكم ديناميكياً في شفافية الرمز أو تدويره أو حجمه أو لونه"], ["It converts point symbols into polygon buffers", "يحول الرموز النقطية إلى مضلعات حرم"], ["It exports points into an Excel spreadsheet", "يصدر النقاط إلى جدول إكسل"], ["It changes the layer coordinate system", "يغير نظام إحداثيات الطبقة"]],
        "A",
        "'Vary symbology by attribute' allows mapping multiple data dimensions simultaneously on a single feature by driving visual variables (transparency, rotation, size, color) with separate attribute fields.",
        "يتيح خيار 'Vary symbology by attribute' تمثيل عدة أبعاد للبيانات معاً على نفس المعلم عبر ربط المتغيرات البصرية (الشفافية، التدوير، الحجم، اللون) بحقول سمات مختلفة.",
        {"B": ["Buffers are created by geoprocessing tools, not symbology variation.", "يتم إنشاء النطاقات بأدوات التحليل وليس بتغيير الرموز."], "C": ["Excel export is a data conversion workflow.", "تصدير إكسل عملية تحويل بيانات."], "D": ["Symbology does not modify coordinate systems.", "الترميز لا يغير أنظمة الإحداثيات."]},
        "symbology"
    )
]

# We need 63 total questions for Visualization.
# We already have 15 detailed questions + 18 topics = 33 questions.
# Let's generate another 30 high-impact exam questions covering:
# - Maplex placement (street name placement, polygon placement, line placement styles)
# - Symbology masking
# - Heat maps and kernel density rendering
# - Dictionary symbology (military/emergency standards)
# - Definition queries with compound logic
# - Selection sets and selection symbology
# - 3D local vs global scene coordinate reference
# - Vertical coordinate systems in scenes
# - Ground elevation surfaces vs custom surfaces
# - Multipatch and 3D objects
# - Voxel layers
# - Dynamic feature display cache
# - Vector Tile layer symbology

more_viz_topics = [
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Symbology Masking"],
        "An analyst needs to create a halo or visual cutout around contour line labels so the contour lines do not strike through the label text. Which technique is most effective in ArcGIS Pro?",
        "يحتاج محلل لإنشاء هالة أو تفريغ بصري حول نصوص خطوط الكنتور لمنع الخطوط من اختراق نصوص التسميات. ما هي التقنية الأكثر فاعلية في ArcGIS Pro؟",
        [["Symbology Masking", "Symbology Masking (أقنعة الرموز)"], ["Clip Raster", "Clip Raster"], ["Delete Vertices", "Delete Vertices"], ["Raster Calculator", "Raster Calculator"]],
        "A",
        "Symbology Masking allows an annotation or label layer to mask underlying feature symbol layers dynamically, creating a clean visual gap without modifying vector line geometry.",
        "تتيح تقنية أقنعة الرموز (Symbology Masking) لنصوص التسميات حجب طبقات الرموز التي تقع أسفلها ديناميكياً، مما ينشئ فراغاً بصرياً نظيفاً دون تشويه أو قطع الخطوط الأصلية.",
        {"B": ["Clip Raster is an imagery cutting tool.", "أداة قص الراستر تتعامل مع الصور."], "C": ["Deleting vertices damages line geometry.", "حذف الرؤوس يدمر هندسة الخطوط."], "D": ["Raster Calculator performs mathematical grid operations.", "حاسبة الراستر تجري عمليات حسابية على الشبكات."]},
        "symbology"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Conceptual", ["Heat Map"],
        "How does the Heat Map symbology renderer in ArcGIS Pro display point feature clusters dynamically across zoom levels?",
        "كيف يعرض محرك الرموز الحرارية (Heat Map) في ArcGIS Pro تجمعات المعالم النقطية ديناميكياً عبر مستويات التكبير والتصغير؟",
        [["It dynamically calculates a continuous kernel density surface on the fly, adjusting search radius as the user zooms", "يحسب ديناميكياً سطح كثافة كيرنز المستمر في الوقت الفعلي مع تعديل نصف قطر البحث أثناء التكبير والتصغير"], ["It permanently generates a raster file in the scratch workspace", "ينشئ ملف راستر دائم في مساحة العمل المؤقتة"], ["It filters points using a SQL statement", "يصفي النقاط باستخدام جمل استعلام SQL"], ["It measures point temperatures using an infrared sensor", "يقيس درجات حرارة النقاط بحساسات الأشعة تحت الحمراء"]],
        "A",
        "Heat Map symbology renders points as a continuous density surface calculated dynamically on-the-fly. As the map scale changes, the search radius recalculates automatically to maintain smooth hotspots.",
        "يعرض نمط الخريطة الحرارية النقاط كسطح كثافة مستمر يتم حسابه ديناميكياً؛ ومع تغير مقياس الخريطة يعاد حساب نصف قطر البحث تلقائياً للحفاظ على سلاسة بؤر التركز.",
        {"B": ["Heat Map renderer is purely visual and creates no disk rasters.", "الخريطة الحرارية عرض بصري خالص ولا تنشئ ملفات راستر على القرص."], "C": ["Definition queries filter points, not heat maps.", "الاستعلام التعريفي يصفي المعالم."], "D": ["GIS heat maps represent statistical density, not thermal physical heat.", "الخرائط الحرارية تمثل كثافة إحصائية وليست حرارة فيزيائية."]},
        "symbology"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Advanced", "Conceptual", ["Dictionary Symbology"],
        "Which symbology method is required when visualizing defense or emergency management datasets governed by standardized specifications like MIL-STD-2525D or App-6D?",
        "أي طريقة تمثيل رمزي مطلوبة عند عرض بيانات الدفاع أو الطوارئ المحكومة بمواصفات قياسية دولية مثل MIL-STD-2525D أو App-6D؟",
        [["Dictionary Symbology", "Dictionary Symbology (رموز القاموس)"], ["Single Symbol", "Single Symbol"], ["Graduated Colors", "Graduated Colors"], ["Dot Density", "Dot Density"]],
        "A",
        "Dictionary Symbology reads multiple attribute fields from each feature and passes them through a rule-based dictionary engine to assemble complex, standardized multi-part symbols.",
        "تقرأ رموز القاموس (Dictionary Symbology) حقولاً سماتية متعددة من كل معلم وتمررها عبر محرك قواعد لتجميع رموز معقدة ومعيارية تتوافق مع المواصفات العسكرية ومواصفات الطوارئ.",
        {"B": ["Single symbol uses one identical style for all features.", "الرمز المنفرد يطبق نمطاً موحداً على كل المعالم."], "C": ["Graduated colors is for numeric choropleth ranges.", "الألوان المتدرجة للخرائط الرقمية الكمية."], "D": ["Dot density is for population counts.", "كثافة النقط لأعداد السكان."]},
        "symbology"
    ),
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Technical", ["3D Scenes"],
        "When designing a 3D subsurface geological model in ArcGIS Pro, where should the subsurface stratum layers be placed in the elevation hierarchy?",
        "عند تصميم نموذج جيولوجي ثلاثي الأبعاد تحت سطحي في ArcGIS Pro، أين يجب وضع طبقات التكوينات الجيولوجية في التسلسل الهرمي للارتفاع؟",
        [["In a Custom Elevation Surface situated below the Ground surface", "في سطح ارتفاع مخصص (Custom Elevation Surface) يقع أسفل سطح الأرض"], ["In the Basemap group layer", "في مجموعة طبقات خريطة الأساس"], ["In an in-memory route event layer", "في طبقة أحداث مسار بالذاكرة"], ["Inside the 2D Layers category", "داخل فئة الطبقات ثنائية الأبعاد (2D Layers)"]],
        "A",
        "ArcGIS Pro allows adding Custom Elevation Surfaces (e.g., top of bedrock, groundwater table) in addition to the master Ground elevation surface, enabling true 3D subsurface and geologic visualization.",
        "يتيح ArcGIS Pro إضافة أسطح ارتفاع مخصصة (Custom Elevation Surfaces) إلى جانب سطح الأرض الأساسي، مما يمكن من العرض ثلاثي الأبعاد للطبقات الجيولوجية والمياه الجوفية تحت السطح.",
        {"B": ["Basemaps are 2D reference surfaces.", "خرائط الأساس أسطح مرجعية ثنائية الأبعاد."], "C": ["Route event layers are for linear dynamic segmentation.", "طبقات أحداث المسار للتجزئة الديناميكية."], "D": ["2D Layers do not render with 3D elevations.", "الطبقات ثنائية الأبعاد لا تستفيد من الارتفاعات ثلاثية الأبعاد."]},
        "scenes"
    ),
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Advanced", "Conceptual", ["3D Scenes"],
        "Which 3D layer type is specifically designed to store and display volumetric multidimensional data, such as atmospheric temperature clouds or 3D oceanic salinity grids?",
        "أي نوع من الطبقات ثلاثية الأبعاد مخصص لتخزين وعرض البيانات الحجمية متعددة الأبعاد، مثل سحب درجات الحرارة الجوية أو شبكات ملوحة المحيطات؟",
        [["Voxel Layer", "Voxel Layer (طبقة الفوكسل)"], ["Shapefile Polygon", "Shapefile Polygon"], ["Tile Package (.tpkx)", "Tile Package (.tpkx)"], ["Map Package (.mpkx)", "Map Package (.mpkx)"]],
        "A",
        "Voxel layers visualize complex 4D volumetric data (NetCDF cubes) as 3D discrete voxels, allowing slicing, sectioning, and isosurface extraction of atmospheric and oceanographic phenomena.",
        "تعرض طبقات الفوكسل (Voxel layers) البيانات الحجمية المعقدة (مكعبات NetCDF) كعناصر حجمية ثلاثية الأبعاد، وتتيح إجراء قطاعات واستخراج أسطح التساوي للظواهر الجوية والبحرية.",
        {"B": ["Shapefiles are 2D/3D surface vector boundaries, not volumetric grids.", "ملفات Shapefile معالم اتجاهية مساحية وليست حجوم شبكية."], "C": ["Tile packages are cached 2D map rasters.", "حزم البلاطات خرائط ثنائية الأبعاد مخزنة مؤقتاً."], "D": ["Map packages are sharing archives.", "حزم الخرائط ملفات أرشيف للمشاركة."]},
        "scenes"
    )
]

# Assemble questions VIZ-016 to VIZ-033
for i, t in enumerate(topics):
    qid = f"VIZ-{i+16:03d}"
    questions.append(make_q(qid, t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11]))

# Assemble VIZ-034 to VIZ-038
for i, t in enumerate(more_viz_topics):
    qid = f"VIZ-{i+34:03d}"
    questions.append(make_q(qid, t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11]))

# Now we need VIZ-039 to VIZ-063 (25 questions) to hit exactly 63 questions.
# Let's generate 25 more focused, highly specific ArcGIS Pro visualization questions!
batch3 = [
    (
        "Manage layer properties using the ribbon and dialog boxes", "Beginner", "Tool-based", ["Symbology"],
        "How can you quickly import symbol colors and classifications from another layer in the current map without opening geoprocessing tools?",
        "كيف يمكنك استيراد ألوان وتصنيفات الرموز بسرعة من طبقة أخرى في نفس الخريطة دون فتح أدوات التحليل الجغرافي؟",
        [["Click the Symbology pane menu (hamburger icon) and select 'Import symbology...'", "النقر على قائمة نافذة الرموز (أيقونة الخيارات) واختيار 'Import symbology...'"], ["Restart ArcGIS Pro", "إعادة تشغيل ArcGIS Pro"], ["Export the layer to a CSV file", "تصدير الطبقة إلى ملف CSV"], ["Press Ctrl+Alt+Delete", "الضغط على Ctrl+Alt+Delete"]],
        "A",
        "In the Symbology pane, clicking the options menu provides an 'Import symbology...' command that links directly to the Apply Symbology From Layer tool functionality.",
        "في نافذة Symbology، يوفر زر الخيارات أمراً سريعاً لاستيراد الرموز (Import symbology) ينقل التصنيف مباشرة من طبقة أخرى.",
        {"B": ["Restarting does not import symbols.", "إعادة التشغيل لا تستورد الرموز."], "C": ["CSV files do not store cartographic symbology.", "ملفات CSV لا تخزن الرموز الكارتوغرافية."], "D": ["Ctrl+Alt+Delete opens OS task management.", "اختصار نظام التشغيل ولا علاقة له بالترميز."]},
        "symbology"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical", ["Labeling"],
        "In Maplex label placement, what option ensures that street names follow the natural curvature of winding roads?",
        "في موضع تسميات Maplex، ما الخيار الذي يضمن أن تتبع أسماء الشوارع التعرجات الطبيعية للطرق المنحنية؟",
        [["Curved placement", "Curved placement (الموضع المنحني)"], ["Horizontal placement", "Horizontal placement (الموضع الأفقي)"], ["Straight placement", "Straight placement (الموضع المستقيم)"], ["Perpendicular placement", "Perpendicular placement (الموضع العمودي)"]],
        "A",
        "Curved line placement bends the label character by character to follow the sinuous geometry of polyline features smoothly.",
        "يقوم خيار Curved placement بحني أحرف التسمية حرفاً بحرف لتتبع الهندسة الانسيابية للخطوط المنحنية بسلاسة كارتوغرافية.",
        {"B": ["Horizontal placement draws text parallel to the page coordinate axis.", "الموضع الأفقي يرسم النص موازياً لأفق الصفحة."], "C": ["Straight placement draws a single straight line along the trend angle.", "الموضع المستقيم يرسم النص في خط مستقيم مائل."], "D": ["Perpendicular places labels at a 90-degree angle crossing the road.", "الموضع العمودي يضع التسمية قاطعة للطريق بزاوية 90 درجة."]},
        "labeling"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical", ["Labeling"],
        "What is the effect of enabling 'Never remove (place overlapping)' on an emergency evacuation route label class?",
        "ما هو أثر تفعيل خيار 'Never remove (place overlapping)' على فئة تسميات مسارات الإخلاء في حالات الطوارئ؟",
        [["It forces the label to draw even if it collides with or overlaps other labels or features", "يفرض رسم التسمية إجبارياً حتى لو تصادمت أو تداخلت مع تسميات أو معالم أخرى"], ["It permanently deletes all conflicting features from the map", "يحذف جميع المعالم المتعارضة نهائياً من الخريطة"], ["It locks the label text against language translation", "يقفل النص ضد الترجمة اللغوية"], ["It converts the label into a 3D building model", "يحول التسمية إلى نموذج مبنى ثلاثي الأبعاد"]],
        "A",
        "'Never remove (place overlapping)' guarantees that essential labels are always rendered on screen regardless of space constraints or collisions.",
        "يضمن خيار 'Never remove' رسم التسميات الحيوية دائماً على الشاشة متجاهلاً قيود المساحة أو التصادم مع النصوص الأخرى لضمان عدم إخفائها.",
        {"B": ["It does not alter data features.", "لا يعدل معالم البيانات إطلاقاً."], "C": ["Language translation is unrelated to label placement.", "لا علاقة للغات بوضع التسميات."], "D": ["Labels remain text graphics, not 3D models.", "تبقى التسميات نصوصاً رسومية."]},
        "labeling"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Symbology"],
        "Which color scheme type should be chosen when symbolizing standardized poverty rates centered around a regional benchmark average?",
        "أي نوع من مخططات الألوان يجب اختياره عند تمثيل معدلات الفقر المعيارية التي تتمحور حول متوسط مرجعي إقليمي؟",
        [["Diverging color scheme", "Diverging color scheme (مخطط ألوان متباعد)"], ["Sequential color scheme", "Sequential color scheme (مخطط ألوان متسلسل)"], ["Qualitative color scheme", "Qualitative color scheme (مخطط ألوان نوعي)"], ["Binary monochrome scheme", "Binary monochrome scheme (مخطط أحادي ثنائي)"]],
        "A",
        "Diverging color schemes emphasize values above and below a critical midpoint (e.g. blue for below average, neutral for average, red for above average).",
        "تركز مخططات الألوان المتباعدة (Diverging) على إبراز القيم التي تقع أعلى وأدنى نقطة مركزية حرجة (مثل ألوان متباينة للأعلى والأسفل ولون محايد للمتوسط).",
        {"B": ["Sequential schemes show low-to-high progressions without a central critical threshold.", "تعرض المخططات المتسلسلة تدرجاً بسيطاً من الأقل للأعلى دون نقطة مركزية."], "C": ["Qualitative schemes are for unranked nominal categories.", "المخططات النوعية للفئات الاسمية غير المرتبة."], "D": ["Monochrome uses only black and white.", "المخطط الأحادي يستخدم لونين فقط."]},
        "symbology"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Conceptual", ["Symbology"],
        "Why is normalization required when creating a graduated colors choropleth map of COVID-19 cases by state?",
        "لماذا يُعد التطبيع (Normalization) مطلوباً عند إنشاء خريطة كوربلث بالألوان المتدرجة لحالات كوفيد-19 حسب الولايات؟",
        [["To account for differences in state populations and display infection rates rather than raw counts", "لمراعاة التفاوت في عدد سكان الولايات وعرض معدلات الإصابة بدلاً من الأعداد الإجمالية الخام"], ["To force all numbers into integer format", "لإجبار جميع الأرقام على التحول إلى أعداد صحيحة"], ["To eliminate zero values from the attribute table", "لحذف القيم الصفرية من جدول البيانات"], ["To rotate the north arrow automatically", "لتدوير سهم الشمال تلقائياً"]],
        "A",
        "Mapping raw counts gives a false impression because populous states naturally have more cases; normalizing by total population calculates true rates per capita.",
        "يعطي رسم الأعداد الخام انطباعاً مضللاً لأن الولايات الأكثر سكاناً ستضم بطبيعتها أعداداً أكبر؛ ويحسب التطبيع على عدد السكان معدل الإصابة الحقيقي لكل نسمة.",
        {"B": ["Normalization produces floating-point rates, not integers.", "ينتج عن التطبيع معدلات كسرية."], "C": ["Zero values are preserved as valid data points.", "يتم الحفاظ على القيم الصفرية كبيانات صحيحة."], "D": ["North arrows are layout elements.", "سهم الشمال عنصر في لوحة الطباعة ولا يرتبط بالتطبيع."]},
        "symbology"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Beginner", "Tool-based", ["Definition Query"],
        "Where in ArcGIS Pro do you configure a Definition Query for a feature layer?",
        "أين يتم ضبط الاستعلام التعريفي (Definition Query) لطبقة المعالم في ArcGIS Pro؟",
        [["Layer Properties > Definition Query", "Layer Properties > Definition Query"], ["Catalog Pane > Project Settings", "Catalog Pane > Project Settings"], ["Map Properties > Coordinate Systems", "Map Properties > Coordinate Systems"], ["Ribbon > Edit > Manage Templates", "Ribbon > Edit > Manage Templates"]],
        "A",
        "Definition Queries are set in the Layer Properties dialog under the Definition Query tab using the clause builder or SQL mode.",
        "يتم ضبط الاستعلامات التعريفية في نافذة خصائص الطبقة (Layer Properties) تحت تبويب Definition Query باستخدام منشئ الشروط أو محرر SQL.",
        {"B": ["Project settings do not manage individual layer queries.", "إعدادات المشروع لا تدير استعلامات الطبقات الفردية."], "C": ["Map coordinate systems control spatial projections.", "أنظمة الإحداثيات تتحكم بالإسقاط."], "D": ["Manage Templates creates editing feature construction templates.", "قوالب التحرير مخصصة لإنشاء المعالم الجديدة."]},
        "query"
    ),
    (
        "Given a scenario, apply a query", "Intermediate", "Technical", ["Select By Attributes"],
        "An analyst needs to select all roads where the SPEED_LIMIT field contains an unpopulated missing value. Which SQL clause is correct?",
        "يحتاج محلل لتحديد جميع الطرق التي يحتوي فيها حقل SPEED_LIMIT على قيمة مفقودة غير مدخلة. أي جملة SQL هي الصحيحة؟",
        [["SPEED_LIMIT IS NULL", "SPEED_LIMIT IS NULL"], ["SPEED_LIMIT = 'NULL'", "SPEED_LIMIT = 'NULL'"], ["SPEED_LIMIT == 0", "SPEED_LIMIT == 0"], ["SPEED_LIMIT IS EMPTY", "SPEED_LIMIT IS EMPTY"]],
        "A",
        "In SQL, missing or undefined database values are tested using the IS NULL operator, not equality operators.",
        "في لغة SQL، يتم فحص القيم المفقودة أو غير المحددة في قاعدة البيانات باستخدام المعامل IS NULL وليس معاملات المساواة.",
        {"B": ["'NULL' in quotes checks for a literal text string with the letters N-U-L-L.", "وضع 'NULL' بين علامتي تنصيص يبحث عن كلمة نصية مكونة من هذه الحروف."], "C": ["0 is a numeric value, completely different from a NULL database state.", "الرقم 0 قيمة عددية تختلف تماماً عن القيمة الفارغة."], "D": ["IS EMPTY is not standard SQL syntax in geodatabases.", "ليست صياغة قياسية في SQL للجيوداتابيس."]},
        "query"
    ),
    (
        "Given a scenario, apply a query", "Intermediate", "Tool-based", ["Select By Location"],
        "Which spatial selection method selects features that share any boundary segment or vertex with the selecting features without overlapping their interior?",
        "أي طريقة تحديد مكاني تختار المعالم التي تشترك في أي جزء من الحد الخارجي أو رأس مع معالم التحديد دون أي تداخل في أجزائها الداخلية؟",
        [["Touch the boundary of", "Touch the boundary of (تلامس حدود)"], ["Are completely within", "Are completely within (تقع بالكامل داخل)"], ["Have their centroid in", "Have their centroid in (يقع مركزها الهندسي في)"], ["Are identical to", "Are identical to (تتطابق تماماً مع)"]],
        "A",
        "'Touch the boundary of' selects features that meet or share boundary lines or vertices with the selector, but whose interior areas do not intersect.",
        "تحدد علاقة 'Touch the boundary of' المعالم التي تتلاقى أو تشترك في خطوط الحدود أو الرؤوس دون أي تداخل في المساحات الداخلية للمعالم.",
        {"B": ["Within requires interior containment.", "تتطلب Within احتواءً داخلياً."], "C": ["Centroid checks center point position.", "تفحص Centroid موضع النقطة المركزية."], "D": ["Identical requires matching exact geometry.", "تتطلب Identical تطابقاً هندسياً كاملاً."]},
        "query"
    ),
    (
        "Given a scenario, apply a query", "Intermediate", "Technical", ["Selection"],
        "How do you invert an active feature selection in an ArcGIS Pro attribute table?",
        "كيف تعكس التحديد النشط للمعالم (Invert Selection) في جدول بيانات ArcGIS Pro؟",
        [["Click the Switch Selection button on the table toolbar", "النقر على زر Switch Selection في شريط أدوات جدول البيانات"], ["Close and reopen the map", "إغلاق الخريطة وإعادة فتحها"], ["Delete the selected records", "حذف السجلات المحددة"], ["Press Esc twice", "الضغط على مفتاح Esc مرتين"]],
        "A",
        "The Switch Selection button (or shortcut) toggles the selection state, unselecting currently selected features and selecting all previously unselected features.",
        "يقوم زر تبديل التحديد (Switch Selection) بعكس حالة التحديد؛ فيلغي تحديد المعالم المختارة ويحدد كافة المعالم التي لم تكن محددة.",
        {"B": ["Reopening the map clears unsaved selections.", "إعادة فتح الخريطة تلغي التحديد."], "C": ["Deleting records destroys data.", "حذف السجلات يدمر البيانات."], "D": ["Esc clears the selection completely.", "مفتاح Esc يلغي التحديد بالكامل."]},
        "query"
    ),
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Beginner", "Technical", ["3D Scenes"],
        "What tool in the Map ribbon allows converting an existing 2D Map directly into a 3D Scene in ArcGIS Pro?",
        "ما الأداة في شريط الخريطة التي تتيح تحويل خريطة ثنائية الأبعاد حالية مباشرة إلى مشهد ثلاثي الأبعاد في ArcGIS Pro؟",
        [["Convert > To Global Scene or To Local Scene on the View tab", "Convert > To Global Scene أو To Local Scene في تبويب View"], ["Export Map", "Export Map"], ["Save As Template", "Save As Template"], ["Project Raster", "Project Raster"]],
        "A",
        "On the View tab, the Convert dropdown allows instantly duplicating a 2D map into either a Local Scene or Global Scene with all layers preserved.",
        "في تبويب View، تتيح قائمة Convert المنسدلة تحويل الخريطة ثنائية الأبعاد فوراً إلى مشهد محلي أو عالمي مع الحفاظ على جميع الطبقات.",
        {"B": ["Export Map creates static image or vector files.", "تصدير الخريطة ينشئ ملفات رسومية ثابتة."], "C": ["Save As Template creates project templates.", "حفظ كقالب ينشئ قوالب مشاريع."], "D": ["Project Raster reprojects imagery files.", "إسقاط الراستر يعيد إسقاط الصور."]},
        "scenes"
    ),
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Tool-based", ["Time"],
        "What happens when you lock the Time Extent on a specific map frame in a multi-frame page layout?",
        "ماذا يحدث عند قفل النطاق الزمني (Time Extent) على إطار خريطة معين في لوحة طباعة تحتوي على عدة إطارات خرائط؟",
        [["The locked map frame maintains its specific historical snapshot date regardless of changes to the global Time Slider", "يحافظ إطار الخريطة المقفل على تاريخ لقطته التاريخية المحددة بغض النظر عن تغييرات منزلق الوقت العام"], ["The map frame becomes completely invisible", "يصبح إطار الخريطة غير مرئي تماماً"], ["All vector features in the frame are converted to CAD format", "تتحول جميع المعالم في الإطار إلى ملفات CAD"], ["The scale bar stops updating dynamically", "يتوقف شريط المقياس عن التحديث ديناميكياً"]],
        "A",
        "Locking time on a map frame decouples it from the shared project time slider, allowing multi-frame layouts to compare side-by-side snapshots (e.g. 1990 vs 2025).",
        "يؤدي قفل الوقت على إطار الخريطة إلى فصله عن منزلق الوقت المشترك، مما يسمح بمقارنة لقطات زمنية جنباً إلى جنب في نفس اللوحة (مثل خريطة لعام 1990 بجوار خريطة لعام 2025).",
        {"B": ["The frame remains fully visible displaying its locked timestamp.", "يظل الإطار مرئياً بالكامل عارضاً توقيته المقفل."], "C": ["CAD conversion is unrelated to time locking.", "تحويل CAD لا علاقة له بقفل الوقت."], "D": ["Scale bars function normally based on spatial extent.", "يعمل مقياس الرسم بشكل طبيعي حسب النطاق المكاني."]},
        "time"
    ),
    (
        "Identify how to control the coordinate system and geographic transformation in ArcGIS Pro", "Beginner", "Conceptual", ["Map Properties"],
        "Does changing the coordinate system of a Map Frame in ArcGIS Pro physically modify the coordinate data of the underlying feature classes on disk?",
        "هل يؤدي تغيير نظام إحداثيات إطار الخريطة في ArcGIS Pro إلى تعديل إحداثيات فئات المعالم الأصلية المخزنة على القرص الصلب؟",
        [["No, it only changes how layers are projected on the fly for visual display", "لا، بل يغير فقط كيفية إسقاط وعرض الطبقات آنياً (On the fly) على الشاشة"], ["Yes, it permanently runs the Project tool on all datasets in the map", "نعم، حيث يقوم بتشغيل أداة Project بشكل دائم على جميع الطبقات"], ["Yes, but only for shapefiles and not geodatabases", "نعم، ولكن لملفات shapefile فقط وليس للجيوداتابيس"], ["Yes, and it deletes all vertical Z-values", "نعم، ويقوم بحذف جميع الارتفاعات الرأسية Z"]],
        "A",
        "Changing map properties alters only the visual display coordinate reference. The source datasets on disk remain completely untouched in their native coordinate systems.",
        "يغير تعديل خصائص الخريطة المرجع الإسقاطي للعرض البصري فقط؛ وتبقى مجموعات البيانات الأصلية على القرص في أنظمتها الإحداثية الأصلية دون أي تعديل.",
        {"B": ["Project tool must be run explicitly to alter disk coordinates.", "يجب تشغيل أداة Project صراحة لتعديل الإحداثيات على القرص."], "C": ["Data format has no bearing on on-the-fly projection mechanics.", "نوع تنسيق البيانات لا يغير آلية العرض الآني."], "D": ["Z-values are preserved intact in feature geometries.", "تظل قيم Z محفوظة كما هي في البيانات الأصلية."]},
        "coord"
    ),
    (
        "Identify how to control the coordinate system and geographic transformation in ArcGIS Pro", "Intermediate", "Technical", ["Map Properties"],
        "What visual symptom occurs on a map when two layers with different datums (e.g., NAD 27 and WGS 84) are displayed together without a datum transformation?",
        "ما العَرَض البصري الذي يظهر على الخريطة عند عرض طبقتين بمراجع مختلفة (مثل NAD 27 و WGS 84) معاً دون تطبيق تحويل للمرجع (Datum Transformation)؟",
        [["Features that should be coincident display with a noticeable spatial offset or misalignment (datum shift)", "المعالم التي يجب أن تكون متطابقة تظهر بإزاحة مكانية ملحوظة وعدم محاذاة (إزاحة المرجع)"], ["The entire map view turns completely black", "تتحول شاشة عرض الخريطة بالكامل إلى اللون الأسود"], ["Labels are converted into question marks", "تتحول نصوص التسميات إلى علامات استفهام"], ["The coordinate values in attribute tables are set to zero", "تتحول قيم الإحداثيات في جداول البيانات إلى أصفار"]],
        "A",
        "Without an appropriate datum transformation, features suffer a datum shift—an offset typically ranging from tens to hundreds of meters—causing roads and boundaries to misalign.",
        "دون تطبيق تحويل ملائم للمرجع، تعاني المعالم من إزاحة المرجع (Datum Shift) التي تتراوح بين عشرات ومئات الأمتار، مما يسبب عدم تطابق الطرق والحدود جغرافياً.",
        {"B": ["Black screens indicate graphics card driver issues, not datum shifts.", "الشاشة السوداء مشكلة في بطاقة الرسوميات."], "C": ["Question marks indicate font encoding issues.", "علامات الاستفهام مشكلة في ترميز الخطوط."], "D": ["Attribute table numbers are not affected by map display.", "جداول البيانات لا تتأثر بالعرض البصري."]},
        "coord"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Symbology"],
        "When using Graduated Colors symbology, which option allows excluding specific outlier values (e.g., -999 NoData codes) from participating in classification calculations?",
        "عند استخدام رموز الألوان المتدرجة، أي خيار يتيح استبعاد قيم شاذة معينة (مثل أكواد -999 للبيانات المفقودة) من الدخول في حسابات فئات التصنيف؟",
        [["Data Exclusion clause in Advanced Symbology Options", "Data Exclusion (استبعاد البيانات) في خيارات الرموز المتقدمة"], ["Delete Field geoprocessing tool", "أداة حذف الحقل Delete Field"], ["Set Layer Transparency to 100%", "ضبط شفافية الطبقة على 100%"], ["Export to KML", "التصدير إلى KML"]],
        "A",
        "The Data Exclusion setting in the Advanced Symbology tab allows writing a SQL expression (e.g., VALUE <> -999) to omit specific values from the classification statistics.",
        "يتيح إعداد استبعاد البيانات (Data Exclusion) في تبويب الرموز المتقدمة كتابة استعلام SQL لاستثناء قيم معينة من الحسابات الإحصائية لتصنيف الفئات.",
        {"B": ["Deleting the field destroys the attribute column.", "حذف الحقل يدمر عمود البيانات بالكامل."], "C": ["Transparency hides features visually but does not fix classification breaks.", "الشفافية تخفي المعالم بصرياً لكنها لا تصلح فواصل التصنيف."], "D": ["KML export does not configure classification.", "تصدير KML لا علاقة له بتصنيف الفئات."]},
        "symbology"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Beginner", "Technical", ["Layer Properties"],
        "Where can an analyst change the interactive selection color from the default cyan/blue to a custom color for a specific project?",
        "أين يمكن للمحلل تغيير لون التحديد التفاعلي من اللون الأزرق الافتراضي إلى لون مخصص لمشروع معين؟",
        [["Project > Options > Selection", "Project > Options > Selection"], ["Catalog Pane > Styles", "Catalog Pane > Styles"], ["Analysis > Environments", "Analysis > Environments"], ["Share > Package Project", "Share > Package Project"]],
        "A",
        "Application selection preferences, including default selection color, tolerance, and interactive selection modes, are configured under Project > Options > Selection.",
        "تُضبط تفضيلات التحديد للتطبيق، بما في ذلك لون التحديد الافتراضي ومسافة التسامح وأنماط التحديد، في نافذة Project > Options > Selection.",
        {"B": ["Styles manage symbols and color palettes.", "الأنماط تدير الرموز وبالتات الألوان."], "C": ["Environments manage geoprocessing execution parameters.", "بيئات التحليل تدير معاملات المعالجة الجغرافية."], "D": ["Package project creates shared archives.", "حزم المشروع مخصصة للمشاركة."]},
        "query"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical", ["Labeling"],
        "In Maplex label placement, what is the role of an Abbreviation Dictionary?",
        "في محرك التسميات Maplex، ما هو دور قاموس الاختصارات (Abbreviation Dictionary)؟",
        [["It automatically replaces long words with standard abbreviations (e.g., 'Street' to 'St') when label space is constrained", "يستبدل الكلمات الطويلة تلقائياً باختصارات معيارية (مثل 'Street' إلى 'St') عند ضيق مساحة التسمية"], ["It translates labels into foreign languages automatically", "يترجم التسميات إلى لغات أجنبية تلقائياً"], ["It converts uppercase labels to lowercase", "يحول الأحرف الكبيرة إلى صغيرة"], ["It fixes spelling errors in the attribute table", "يصلح الأخطاء الإملائية في جدول البيانات"]],
        "A",
        "Abbreviation Dictionaries specify word substitutions that Maplex can apply when space is too tight to place full text strings, preserving readable labels.",
        "تحدد قواميس الاختصارات بدائل الكلمات التي يمكن لمحرك Maplex استخدامها عند ضيق المساحة لتناسب النص دون حذفه (مثل تحويل Road إلى Rd).",
        {"B": ["It does not provide language translation.", "لا يوفر ترجمة لغوية."], "C": ["Text case formatting is done via Arcade expressions.", "تغيير حالة الأحرف يتم بتعبيرات Arcade."], "D": ["It does not modify underlying attribute table text.", "لا يعدل النصوص الأصلية في جدول البيانات."]},
        "labeling"
    ),
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Technical", ["3D Scenes"],
        "What type of layer in ArcGIS Pro stores optimized 3D geometric meshes (such as textured buildings, bridges, and monuments) with photo-realistic facade textures?",
        "ما نوع الطبقة في ArcGIS Pro الذي يخزن شبكات هندسية ثلاثية الأبعاد محسنة (مثل المباني والجسور والمعالم ذات الواجهات الواقعية)؟",
        [["Multipatch or 3D Object feature layer", "Multipatch أو طبقة معالم 3D Object"], ["Point feature layer with graduated colors", "طبقة معالم نقطية برموز متدرجة"], ["Dynamic Image Service layer", "طبقة خدمة صور ديناميكية"], ["Annotation feature layer", "طبقة معالم نصوص توضيحية"]],
        "A",
        "Multipatch feature classes and 3D Object layers store true 3D surface geometry meshes with material textures, photorealistic facades, and lighting reflection properties.",
        "تخزن فئات معالم Multipatch وطبقات 3D Object مجسمات هندسية ثلاثية الأبعاد حقيقية مع إكساءات المواد والواجهات الواقعية وخصائص انعكاس الإضاءة.",
        {"B": ["Point layers represent 0D discrete coordinates.", "الطبقات النقطية تمثل إحداثيات صفرية الأبعاد."], "C": ["Image services stream 2D raster grids.", "خدمات الصور تبث شبكات راستر ثنائية الأبعاد."], "D": ["Annotation layers represent text labels.", "طبقات النصوص التوضيحية تمثل نصوصاً."]},
        "scenes"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical", ["Symbology"],
        "What is the function of the 'Symbol layer drawing' advanced setting when symbolizing multi-lane freeway lines with thick outlines?",
        "ما وظيفة الإعداد المتقدم 'Symbol layer drawing' عند تمثيل خطوط الطرق السريعة متعددة المسارات بإطارات خارجية سميكة؟",
        [["It merges overlapping line outlines and fills seamlessly across intersections to eliminate internal borders", "يدمج حدود وتعبئة الخطوط المتداخلة بسلاسة عبر التقاطعات لإزالة الخطوط الفاصلة الداخلية"], ["It converts polyline features into raster elevation surfaces", "يحول معالم الخطوط إلى أسطح ارتفاع راستر"], ["It enforces topology rules during geometry edits", "يفرض قواعد الطوبولوجيا أثناء التحرير"], ["It calculates the driving travel time along each segment", "يحسب زمن القيادة على كل جزء من الطريق"]],
        "A",
        "Symbol layer drawing allows you to control the draw order of individual symbol layers across features, merging casings and fills cleanly at junctions.",
        "تسمح خاصية Symbol layer drawing بالتحكم في ترتيب رسم طبقات الرموز الفردية للمعالم، مما يدمج الحواف والتعبئة بسلاسة عند تقاطعات الشوارع.",
        {"B": ["It is a cartographic display setting, not a raster tool.", "إعداد كارتوغرافي وليس أداة راستر."], "C": ["Topology is managed in the geodatabase, not symbology.", "الطوبولوجيا تُدار في قاعدة البيانات."], "D": ["Network Analyst calculates drive times.", "تحليل الشبكات هو المسؤول عن حساب أزمنة القيادة."]},
        "symbology"
    ),
    (
        "Given a scenario, apply a query", "Beginner", "Technical", ["Select By Attributes"],
        "Which clause in an ArcGIS Pro SQL query selects records where the COUNTY field starts with the letter 'M'?",
        "أي شرط في استعلام SQL بـ ArcGIS Pro يحدد السجلات التي يبدأ فيها حقل COUNTY بحرف 'M'؟",
        [["COUNTY LIKE 'M%'", "COUNTY LIKE 'M%'"], ["COUNTY = 'M*'", "COUNTY = 'M*'"], ["COUNTY IN ('M')", "COUNTY IN ('M')"], ["COUNTY CONTAINS 'M'", "COUNTY CONTAINS 'M'"]],
        "A",
        "The LIKE operator paired with the percent wildcard (%) after the character 'M' matches any string beginning with 'M' followed by any characters.",
        "يقوم المعامل LIKE متبوعاً بحرف 'M' وعلامة النسبة المئوية (%) بمطابقة أي نص يبدأ بحرف M متبوعاً بأي عدد من الحروف.",
        {"B": ["Asterisk is not used for file geodatabase wildcards.", "علامة النجمة لا تُستخدم في قواعد البيانات الملفية."], "C": ["IN ('M') matches only the single exact letter 'M'.", "تطابق الحرف M بمفرده فقط."], "D": ["CONTAINS is not standard SQL syntax in this context.", "ليست صياغة قياسية في جمل SQL هنا."]},
        "query"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Beginner", "Tool-based", ["Transparency"],
        "Where is the interactive layer transparency slider located in the ArcGIS Pro interface when a feature layer is selected in the Contents pane?",
        "أين يقع منزلق شفافية الطبقة التفاعلي في واجهة ArcGIS Pro عند تحديد طبقة معالم في نافذة المحتويات؟",
        [["On the Feature Layer contextual ribbon under the Appearance tab", "في الشريط السياقي Feature Layer تحت تبويب Appearance"], ["In the Status bar at the bottom of the screen", "في شريط الحالة أسفل الشاشة"], ["In the Catalog pane", "في نافذة الكتالوج Catalog"], ["In the Python window", "في نافذة بايثون"]],
        "A",
        "When a feature layer is selected, the contextual Feature Layer tab group appears on the ribbon, where the Appearance tab contains the Transparency slider and Blend Mode controls.",
        "عند تحديد طبقة معالم، يظهر الشريط السياقي Feature Layer، ويحتوي تبويب Appearance على منزلق الشفافية وأدوات نمط الدمج.",
        {"B": ["The status bar displays coordinates and scale.", "شريط الحالة يعرض الإحداثيات ومقياس الرسم."], "C": ["Catalog pane manages project items and databases.", "نافذة الكتالوج تدير عناصر المشروع."], "D": ["Python window is for scripting.", "نافذة بايثون لكتابة الأوامر البرمجية."]},
        "symbology"
    ),
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Tool-based", ["Time"],
        "When playing a temporal animation on the Time Slider, what parameter controls the step size of each chronological frame advance?",
        "عند تشغيل عرض زمني متحرك على منزلق الوقت، ما المعامل الذي يتحكم في مقدار القفزة الزمنية لكل إطار متحرك؟",
        [["Time Step Interval", "Time Step Interval (الفاصل الزمني للخطوة)"], ["Map Scale", "Map Scale (مقياس الخريطة)"], ["Buffer Distance", "Buffer Distance (مسافة النطاق)"], ["Spatial Tolerance", "Spatial Tolerance (التسامح المكاني)"]],
        "A",
        "The Time Step Interval (e.g. 1 Day, 1 Month, 1 Year) dictates how far forward in time the slider advances between consecutive animation frames.",
        "يحدد الفاصل الزمني للخطوة (Time Step Interval) مقدار التقدم في الزمن بين كل إطار متحرك والذي يليه (مثل يوم واحد، أو شهر، أو سنة).",
        {"B": ["Map scale controls zoom level.", "مقياس الخريطة يتحكم في نسبة التقريب."], "C": ["Buffer distance is for proximity analysis.", "مسافة الحرم لتحليل التقارب."], "D": ["Spatial tolerance is for snapping and clustering.", "التسامح المكاني لعمليات الانجذاب والتجميع."]},
        "time"
    ),
    (
        "Identify how to control the coordinate system and geographic transformation in ArcGIS Pro", "Intermediate", "Technical", ["3D Scenes"],
        "Can a Local Scene use a projected coordinate system (such as State Plane or UTM) as its scene coordinate system?",
        "هل يمكن للمشهد المحلي (Local Scene) استخدام نظام إحداثيات مسقط (مثل State Plane أو UTM) كنظام إحداثيات للمشهد؟",
        [["Yes, Local Scenes are specifically designed to use projected coordinate systems for planar localized visualization", "نعم، فالمشاهد المحلية مصممة خصيصاً لاستخدام أنظمة الإحداثيات المسقطة للعرض المستوي المحلي"], ["No, all 3D scenes are permanently locked to WGS 1984 geographic coordinates", "لا، فجميع المشاهد ثلاثية الأبعاد مقفلة بشكل دائم على نظام WGS 1984 الجغرافي"], ["No, 3D scenes have no coordinate systems", "لا، فالمشاهد ثلاثية الأبعاد ليس لها أنظمة إحداثيات"], ["Only if all layers are CAD drawings", "فقط إذا كانت جميع الطبقات رسومات CAD"]],
        "A",
        "Unlike Global Scenes which require WGS84 or CGCS2000, Local Scenes can be set to any projected coordinate system, preventing projection distortion across localized engineering or municipal extents.",
        "على عكس المشاهد العالمية التي تتطلب WGS84، يمكن للمشاهد المحلية استخدام أي نظام إحداثيات مسقط، مما يمنع تشوهات الإسقاط في التطبيقات الهندسية والبلدية.",
        {"B": ["Only Global scenes are restricted to geographic ellipsoids.", "المشاهد العالمية فقط هي المقيدة بالنظام الجغرافي."], "C": ["All scenes require a valid spatial reference.", "تتطلب جميع المشاهد مرجعاً مكانياً صحيحاً."], "D": ["Local scenes support all standard GIS data formats.", "تدعم المشاهد المحلية كافة صيغ بيانات نظم المعلومات الجغرافية."]},
        "coord"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical", ["Labeling"],
        "In the Maplex Label Engine, how does 'Label Weight' differ from 'Feature Weight'?",
        "في محرك التسميات Maplex، كيف يختلف 'وزن التسمية' (Label Weight) عن 'وزن المعلم' (Feature Weight)؟",
        [["Label Weight determines which label wins when competing labels collide; Feature Weight determines how strongly a feature resists having labels placed over it", "وزن التسمية يحدد أي تسمية تُرسم عند تصادم تسميتين متنافستين؛ بينما وزن المعلم يحدد مدى مقاومة المعلم لوضع تسميات فوقه"], ["Label Weight sets the font thickness; Feature Weight sets line width", "وزن التسمية يحدد سمك الخط؛ ووزن المعلم يحدد عرض خط المعلم"], ["Label Weight only works on point layers; Feature Weight only works on polygons", "وزن التسمية يعمل على النقاط فقط؛ ووزن المعلم يعمل على المضلعات فقط"], ["Both weights perform identical functions and can be used interchangeably", "يؤدي كلا الوزنين نفس الوظيفة تماماً ويمكن التبديل بينهما"]],
        "A",
        "Label Weight resolves collisions between competing label texts (higher weight wins). Feature Weight defines whether the feature geometry itself serves as an obstacle against any labels crossing it.",
        "يحسم وزن التسمية (Label Weight) النزاع بين النصوص المتصادمة (الأعلى وزناً يفوز بالظهور)؛ بينما يحدد وزن المعلم (Feature Weight) مدى عمل هندسة المعلم كحاجز يمنع التسميات من تغطيته.",
        {"B": ["Weights control placement conflict rules, not graphic line widths or font weights.", "تتحكم الأوزان في قواعد تجنب النزاع وليس في سماكة الخطوط."], "C": ["Both weight properties are available across all vector geometry types.", "كلا الوزنين متاح لجميع أنواع المعالم الهندسية."], "D": ["They serve fundamentally distinct roles (label priority vs obstacle resistance).", "يؤدي كل منهما دوراً مختلفاً جوهرياً (أولوية التسمية مقابل مقاومة الحواجز)."]},
        "labeling"
    ),
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Symbology"],
        "Which classification method calculates class breaks so that the difference between the mean of each class and the values within that class is minimized?",
        "أي طريقة تصنيف تحسب فواصل الفئات بحيث تقلل الفروق بين متوسط كل فئة والقيم الواقعة داخل تلك الفئة لأدنى حد؟",
        [["Natural Breaks (Jenks)", "Natural Breaks (الكسور الطبيعية - جينكس)"], ["Quantile", "Quantile (الفئات المتساوية)"], ["Equal Interval", "Equal Interval (الفترات المتساوية)"], ["Standard Deviation", "Standard Deviation (الانحراف المعياري)"]],
        "A",
        "The Jenks optimization algorithm minimizes the sum of squared differences from the class means (variance within classes) while maximizing differences between classes.",
        "تقلل خوارزمية جينكس التباين الداخلي داخل كل فئة (مجموع مربعات الفروق عن متوسط الفئة) وتعظم التباين بين الفئات المختلفة لإبراز التجمعات الطبيعية.",
        {"B": ["Quantile focuses on equal counts, not variance minimization.", "تركز طريقة Quantile على تساوي الأعداد وليس تقليل التباين."], "C": ["Equal Interval divides range mathematically.", "تقسم الفترات المتساوية المدى حسابياً."], "D": ["Standard Deviation uses standard statistical units from the overall mean.", "يستخدم الانحراف المعياري وحدات إحصائية من المتوسط العام."]},
        "classification"
    ),
    (
        "Given a scenario, apply a query", "Intermediate", "Technical", ["Select By Location"],
        "An analyst runs Select By Location with the spatial relationship 'Intersect'. If a polygon's boundary merely touches the edge of another polygon without interior overlap, is it selected?",
        "قام محلل بتشغيل أداة Select By Location بالعلاقة المكانية 'Intersect'. إذا لامست حدود مضلع حافة مضلع آخر دون أي تداخل داخلي، فهل سيتم اختياره؟",
        [["Yes, because touching boundaries or sharing vertices satisfies the mathematical Intersect condition", "نعم، لأن ملامسة الحدود أو الاشتراك في الرؤوس يحقق شرط التقاطع الرياضي (Intersect)"], ["No, Intersect strictly requires overlapping interior area", "لا، فالتقاطع يتطلب حتماً تداخلاً في المساحة الداخلية"], ["Only if both polygons have the same area", "فقط إذا كان للمضلعين نفس المساحة"], ["Only in 3D Local Scenes", "فقط في المشاهد ثلاثية الأبعاد المحلية"]],
        "A",
        "In the OpenGIS dimensionally extended 9-intersection model (DE-9IM) used by ArcGIS, 'Intersect' returns true if any point of geometry A touches or crosses any point of geometry B, including boundaries.",
        "في النموذج الرياضي للتقاطع المكاني المعتمد بـ ArcGIS، تعتبر المعالم متقاطعة (Intersect) إذا اشتركت في أي نقطة أو حافة أو رأس، حتى لو لم تتداخل المساحات الداخلية.",
        {"B": ["Interior overlap is required for 'Overlaps', not 'Intersect'.", "التداخل الداخلي مطلوب لعلاقة Overlaps وليس Intersect."], "C": ["Area equality is irrelevant to topological intersections.", "تساوي المساحة لا علاقة له بالتقاطع الطوبولوجي."], "D": ["Topological relationships function identically in 2D and 3D.", "العلاقات المكانية تعمل بنفس القواعد في البيئتين."]},
        "query"
    )
]

for i, t in enumerate(batch3):
    qid = f"VIZ-{i+39:03d}"
    questions.append(make_q(qid, t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11]))

print(f"Total Visualization MCQs built: {len(questions)} (expected 63)")

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Saved visualization.json successfully.")

