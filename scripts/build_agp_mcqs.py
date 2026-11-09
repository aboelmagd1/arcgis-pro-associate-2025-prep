# -*- coding: utf-8 -*-
"""
Build all 62 Analysis & Geoprocessing MCQs (AGP-001 through AGP-062) for EAPA_2025.
"""
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_file = os.path.join(base_dir, 'public', 'data', 'questions', 'analysis-geoprocessing.json')

ref_map = {
    "joins": {"title": "Joins and relates overview, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/tables/joins-and-relates-overview.htm", "kind": "official"},
    "overlay": {"title": "An overview of the Overlay toolset, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/an-overview-of-the-overlay-toolset.htm", "kind": "official"},
    "proximity": {"title": "An overview of the Proximity toolset, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/an-overview-of-the-proximity-toolset.htm", "kind": "official"},
    "modelbuilder": {"title": "What is ModelBuilder?, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/analysis/geoprocessing/modelbuilder/what-is-modelbuilder-.htm", "kind": "official"},
    "environments": {"title": "Geoprocessing environment settings, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/analysis/geoprocessing/basics/geoprocessing-environment-settings.htm", "kind": "official"},
    "rasterfunc": {"title": "Raster functions, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/analysis/raster-functions/raster-functions.htm", "kind": "official"},
    "tasks": {"title": "What is a task?, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/analysis/tasks/what-is-a-task-.htm", "kind": "official"}
}

def make_q(qid, objective, diff, qtype, tools, q_en, q_ar, opts, ans, exp_en, exp_ar, why_wrong, ref_key):
    return {
        "id": qid,
        "kind": "mcq",
        "domain": "Analysis and Geoprocessing",
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

# AGP-001 to AGP-015: In-depth Joins, Relates & Overlay
questions.append(make_q(
    "AGP-001", "Compare table joins and relates, relationship classes, and spatial joins", "Intermediate", "Conceptual",
    ["Add Join", "Add Relate"],
    "An analyst needs to link a parcel feature class to an external table of property sales where each parcel has had multiple sales transactions over the past 10 years (1-to-Many cardinality). Why is Add Join inappropriate for this workflow?",
    "يحتاج محلل إلى ربط طبقة قطع الأراضي بجدول مبيعات خارجي حيث تمت عدة صفقات بيع لكل قطعة خلال السنوات العشر الماضية (علاقة 1 إلى متعدد). لماذا يُعد أمر Add Join غير مناسب لهذا العمل؟",
    [
        ["Add Join is designed for 1-to-1 or Many-to-1 relationships and only appends the first matching record for each feature", "أمر Add Join مصمم لعلاقات 1 إلى 1 أو متعدد إلى 1 ويقوم بإلحاق السجل المطابق الأول فقط لكل معلم متجاهلاً بقية السجلات"],
        ["Add Join permanently deletes non-matching rows from the geodatabase", "يحذف Add Join الصفوف غير المتطابقة نهائياً من قاعدة البيانات"],
        ["Add Join can only join tables stored in Oracle databases", "يعمل Add Join فقط مع الجداول المخزنة في قواعد بيانات Oracle"],
        ["Add Join requires both layers to have spatial polygon geometry", "يتطلب Add Join أن يكون لكلا الطبقتين هندسة مضلعات مكانية"]
    ],
    "A",
    "Add Join creates a flat virtual table join. In a 1-to-Many situation, only the first matching record from the join table is appended to the layer attribute table, hiding subsequent matching rows. An Add Relate or Geodatabase Relationship Class is required.",
    "ينشئ Add Join ضماً جدولياً افتراضياً مسطحاً؛ وفي علاقات 1 إلى متعدد، يتم إلحاق السجل المطابق الأول فقط بجدول المعالم وإخفاء بقية السجلات المرتبطة. لذا يجب استخدام Add Relate أو فئات العلاقات.",
    {
        "B": ["Add Join is a temporary session join and never deletes records.", "أمر Add Join ضم مؤقت في جلسة العمل ولا يحذف أي سجلات."],
        "C": ["Add Join works across file geodatabases, mobile geodatabases, shapefiles, Excel, and enterprise DBMS.", "يعمل مع مختلف صيغ الملفات وقواعد البيانات."],
        "D": ["Tables joined via Add Join can be standalone non-spatial attribute tables.", "يمكن للجدول المضموم أن يكون جدولاً سماتياً مجرداً بلا هندسة."]
    },
    "joins"
))

questions.append(make_q(
    "AGP-002", "Compare table joins and relates, relationship classes, and spatial joins", "Intermediate", "Tool-based",
    ["Spatial Join"],
    "An analyst needs to count how many crime incident points occurred within each police precinct polygon and calculate the average incident response time per precinct. Which tool and configuration achieves this in one step?",
    "يحتاج محلل لحساب عدد نقاط بلاغات الجرائم داخل كل مضلع من مضلعات أقسام الشرطة مع حساب متوسط زمن الاستجابة لكل قسم. أي أداة وإعداد يحقق ذلك في خطوة واحدة؟",
    [
        ["Spatial Join with Target: Precincts, Join: Crimes, Join Operation: Join one to one, and Mean merge rule on response time", "Spatial Join مع تحديد الهدف: Precincts، والمصدر: Crimes، وعملية الضم: Join one to one، وتطبيق قاعدة الدمج Mean على زمن الاستجابة"],
        ["Clip tool with Input: Crimes, Clip Features: Precincts", "أداة Clip مع تحديد المدخل: Crimes، ومعالم القص: Precincts"],
        ["Add Join on Police_ID field", "أمر Add Join على حقل Police_ID"],
        ["Intersect tool with Output Type: Point", "أداة Intersect مع تحديد نوع المخرجات Point"]
    ],
    "A",
    "Spatial Join with target polygons and join points using 'Join one to one' computes the Join_Count field (total points in polygon) and allows specifying field merge rules (such as Mean, Sum, or Max) on numerical attributes of the join features.",
    "تنتج أداة Spatial Join عند ضبط المضلعات كهدف والنقاط كمعالم ضم مع خيار 'Join one to one' حقلاً تلقائياً اسمه Join_Count يحسب عدد النقاط، مع إمكانية تطبيق قواعد دمج (مثل المتوسط Mean) على الحقول الرقمية.",
    {
        "B": ["Clip cuts points by boundary but does not append summary statistics or counts to the polygons.", "تقص أداة Clip النقاط ولكنها لا تحسب إحصائيات ولا تضيف حقولاً للمضلعات."],
        "C": ["Add Join requires an existing common foreign key attribute, not spatial containment.", "يتطلب Add Join وجود مفتاح جدولي مشترك ولا يعتمد على الاحتواء المكاني."],
        "D": ["Intersect outputs intersected geometries, not polygon summaries with count fields.", "تنتج Intersect معالم التقاطع ولا تضيف حقلاً لعدد النقاط الملخصة."]
    },
    "joins"
))

questions.append(make_q(
    "AGP-003", "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based",
    ["Clip", "Intersect"],
    "What is the key difference in output attributes between the Clip tool and the Intersect tool when clipping soil polygons by a county study area boundary?",
    "ما هو الفرق الجوهري في السمات الجدولية للنتائج بين أداتي Clip و Intersect عند قص مضلعات التربة بحدود منطقة دراسة المحافظة؟",
    [
        ["Clip retains attributes ONLY from the input soil layer; Intersect preserves attributes from BOTH the soil and county layers", "تحتفظ أداة Clip بسمات طبقة التربة المدخلة فقط؛ بينما تحتفظ أداة Intersect بسمات كلا الطبقتين (التربة والمحافظة) معاً"],
        ["Clip only outputs line features; Intersect only outputs raster cells", "تُخرج أداة Clip معالم خطية فقط؛ وتُخرج أداة Intersect خلايا راستر فقط"],
        ["Intersect deletes all overlapping areas; Clip combines them", "تحذف أداة Intersect المساحات المتداخلة وتدمجها أداة Clip"],
        ["Both tools produce identical attribute tables", "تنتج كلتا الأداتين جداول بيانات وصفية متطابقة تماماً"]
    ],
    "A",
    "Clip acts like a cookie cutter: it slices the input geometries to the boundary of the clip features, but passes through attributes only from the Input layer. Intersect performs an analytical overlay, writing combined attributes from all participating layers into the output table.",
    "تعمل أداة Clip كقالب تقطيع: تقتطع هندسة المدخلات عند حدود معالم القص، لكنها تحتفظ فقط ببيانات طبقة الإدخال. بينما أداة Intersect تجري تحليلاً تراكبياً يدمج سمات جميع الطبقات المشاركة في جدول المخرجات.",
    {
        "B": ["Both tools support polygon-to-polygon operations outputting polygons.", "تدعم كلتا الأداتين العمليات بين المضلعات وتنتجان مضلعات."],
        "C": ["Intersect preserves overlapping areas; Erase is the tool that removes them.", "تحتفظ Intersect بالمناطق المتداخلة، بينما Erase هي التي تحذفها."],
        "D": ["Clip tables omit attributes from the boundary layer, making them fundamentally different from Intersect tables.", "تتجاهل جداول Clip بيانات طبقة الحدود فتختلف جوهرياً عن Intersect."]
    },
    "overlay"
))

questions.append(make_q(
    "AGP-004", "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Conceptual",
    ["Geoprocessing Environments"],
    "In ArcGIS Pro geoprocessing environment precedence, which level has the highest priority and will override all others?",
    "في التسلسل الهرمي لأسبقية بيئات المعالجة الجغرافية بـ ArcGIS Pro، أي مستوى له الأولوية القصوى ويلغي جميع المستويات الأخرى؟",
    [
        ["Application-level Environment (Analysis > Environments)", "بيئة مستوى التطبيق (Analysis > Environments)"],
        ["Individual Tool Parameter", "معامل الأداة الفردي (Tool Parameter)"],
        ["Model-level Environment", "بيئة مستوى النموذج (Model-level Environment)"],
        ["Operating System Environment Variable", "متغيرات بيئة نظام التشغيل (OS Environment Variable)"]
    ],
    "B",
    "Environment settings follow a 4-level hierarchy: Level 1 (Highest) is explicit Tool Parameters; Level 2 is Tool-level environments; Level 3 is Model/Script environments; Level 4 (Lowest) is Application-level project environments.",
    "تتبع بيئات التحليل تسلسلاً هرمياً من 4 مستويات: المستوى 1 (الأعلى) هو معاملات الأداة المباشرة؛ المستوى 2 بيئات الأداة الفردية؛ المستوى 3 بيئات النموذج/السكربت؛ المستوى 4 (الأدنى) بيئة المشروع العامة للتطبيق.",
    {
        "A": ["Application-level environments are Level 4, the lowest priority override.", "بيئة التطبيق تقع في المستوى الرابع وهي الأقل أولوية."],
        "C": ["Model environments are Level 3, overridden by tool environments and tool parameters.", "بيئة النموذج في المستوى الثالث وتلغيها معاملات الأداة المباشرة."],
        "D": ["OS variables do not override explicit geoprocessing tool parameters.", "متغيرات نظام التشغيل لا تلغي معاملات أدوات التحليل."]
    },
    "environments"
))

questions.append(make_q(
    "AGP-005", "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Advanced", "Technical",
    ["Snap Raster"],
    "During multi-criteria raster suitability modeling, what critical error is prevented by setting the 'Snap Raster' environment setting to a master elevation grid?",
    "أثناء نمذجة الملاءمة المكانية للراستر متعددة المعايير، ما الخطأ الجسيم الذي يتم تجنبه بضبط بيئة 'Snap Raster' على شبكة الارتفاع الرئيسية؟",
    [
        ["Unintended half-cell registration shift and resampling distortion between overlapping rasters", "انزياح محاذاة البكسل بمقدار نصف خلية وتشوهات إعادة الاستعيان بين طبقات الراستر المتراكبة"],
        ["Accidental deletion of the coordinate system .prj file", "الحذف غير المقصود لملف نظام الإحداثيات .prj"],
        ["Exceeding the 2 GB shapefile size limit", "تجاوز الحد الأقصى لسعة ملف shapefile البالغة 2 جيجابايت"],
        ["Overwriting the source geodatabase lock files", "الكتابة فوق ملفات القفل لقاعدة البيانات الأصلية"]
    ],
    "A",
    "Snap Raster aligns the cell corners and origin of the output raster precisely with an existing reference raster. Without Snap Raster, overlapping grids with slight extent discrepancies cause an unintended half-cell spatial shift and resampling artifacts.",
    "تقوم بيئة Snap Raster بمطابقة زوايا الخلايا ونقطة الأصل للراستر الناتج تماماً مع راستر مرجعي قائم. وبدونها، يؤدي التفاوت البسيط في حدود النطاق إلى انزياح مكاني بمقدار نصف خلية وتشوهات استعيان.",
    {
        "B": ["Snap Raster controls raster grid origin alignment, not .prj metadata files.", "تتحكم Snap Raster بمحاذاة شبكة الخلايا ولا علاقة لها بملفات .prj."],
        "C": ["Raster processing does not involve shapefile 2GB table limits.", "معالجة الراستر لا ترتبط بحدود حجم ملفات shapefile."],
        "D": ["Schema locks are managed by the geodatabase engine, not Snap Raster.", "أقفال المخطط يديرها محرك قواعد البيانات."]
    },
    "environments"
))

questions.append(make_q(
    "AGP-006", "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Technical",
    ["ModelBuilder"],
    "In an ArcGIS Pro ModelBuilder workflow, what does a small blue letter 'P' displayed next to an input variable indicate?",
    "في نموذج ModelBuilder بـ ArcGIS Pro، إلى ماذا يشير حرف 'P' الأزرق الصغير الظاهر بجوار متغير الإدخال؟",
    [
        ["The variable is exposed as a user-configurable Model Parameter when run from the Geoprocessing pane", "المتغير معرّف كمعامل نموذج (Model Parameter) يظهر للمستخدم لضبطه عند تشغيل الأداة من نافذة التحليل"],
        ["The variable is marked as a Precondition for all tools in the model", "المتغير محدد كشرط مسبق (Precondition) لجميع أدوات النموذج"],
        ["The variable will be purged permanently upon model completion as Intermediate Data", "سيتم حذف المتغير نهائياً كبيانات وسيطة عند اكتمال تشغيل النموذج"],
        ["The variable is password-protected against editing", "المتغير محمي بكلمة مرور ضد التعديل"]
    ],
    "A",
    "Flagging an element as 'Model Parameter' attaches the 'P' badge, exposing it as an input or output parameter in the geoprocessing tool dialog when other analysts execute the model.",
    "يؤدي تعيين العنصر كـ 'Model Parameter' إلى ظهور علامة 'P'، مما يجعله مدخلاً أو مخرجاً يظهر في نافذة تشغيل الأداة ليتمكن المستخدمون الآخرون من تخصيصه.",
    {
        "B": ["Preconditions are visualized as dashed connecting lines, not the 'P' badge.", "الشروط المسبقة تظهر كخطوط متقطعة وليس كحرف P."],
        "C": ["Intermediate data is indicated by a flag in the model element properties, not 'P'.", "البيانات الوسيطة تُحدد بخيار في الخصائص."],
        "D": ["Password protection is set on the toolbox level, not by the 'P' icon.", "حماية كلمة المرور تضبط على مستوى صندوق الأدوات."]
    },
    "modelbuilder"
))

questions.append(make_q(
    "AGP-007", "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Technical",
    ["ModelBuilder"],
    "What visual cue in ModelBuilder indicates that a tool element and its output dataset have successfully executed and now physically exist on disk?",
    "ما العلامة البصرية في ModelBuilder التي تشير إلى أن عنصر الأداة ومخرجاتها قد تم تنفيذها بنجاح وأصبحت موجودة فعلياً على القرص؟",
    [
        ["The tool and output elements display a distinct drop shadow behind them", "تظهر خلف عنصر الأداة ومخرجاتها ظلال مسقطة مميزة (Drop Shadow)"],
        ["The tool element turns bright red", "يتحول عنصر الأداة إلى اللون الأحمر الفاقع"],
        ["The output oval changes from green to blue", "يتغير لون الشكل البيضاوي للمخرجات من الأخضر إلى الأزرق"],
        ["A padlock icon appears on the canvas", "يظهر رمز قفل على مساحة العمل"]
    ],
    "A",
    "ModelBuilder uses distinct states: White elements = Not ready to run; Solid yellow/green/blue = Ready to run; Elements with Drop Shadows = Has run (executed and output generated on disk).",
    "يستخدم ModelBuilder حالات بصرية محددة: العناصر البيضاء = غير جاهزة للتشغيل؛ العناصر الملونة بدون ظلال = جاهزة للتشغيل؛ والعناصر ذات الظلال المسقطة (Drop Shadow) = تم تشغيلها ووجود المخرجات على القرص.",
    {
        "B": ["Red indicates an execution error or failure.", "اللون الأحمر يشير إلى حدوث خطأ أو فشل في التنفيذ."],
        "C": ["Outputs remain green; blue represents inputs.", "المخرجات تظل خضراء واللون الأزرق للمدخلات."],
        "D": ["Padlock icons indicate locked geoprocessing files, not completed execution.", "رمز القفل يشير لملفات مقفلة."]
    },
    "modelbuilder"
))

questions.append(make_q(
    "AGP-008", "Apply raster functions for raster and image processing", "Intermediate", "Conceptual",
    ["Raster Functions"],
    "What is the key functional difference between executing a Raster Function and running a Geoprocessing Tool on satellite imagery?",
    "ما هو الفرق الوظيفي الجوهري بين تنفيذ دالة راستر (Raster Function) وتشغيل أداة معالجة جغرافية (Geoprocessing Tool) على الصور الفضائية؟",
    [
        ["Raster Functions process pixels on-the-fly in memory at display resolution without writing new files; GP tools process the entire dataset and write new files to disk", "تعالج دوال الراستر البكسلات لحظياً في الذاكرة بدقة العرض دون كتابة ملفات؛ بينما تعالج أدوات التحليل كامل البيانات وتنشئ ملفات جديدة على القرص"],
        ["Raster Functions only work on vector point layers", "تعمل دوال الراستر على طبقات النقاط الاتجاهية فقط"],
        ["Geoprocessing tools can only be run once per calendar year", "يمكن تشغيل أدوات المعالجة الجغرافية مرة واحدة فقط كل عام"],
        ["Raster Functions permanently delete source imagery bands", "تحذف دوال الراستر نطاقات الصور الأصلية بشكل دائم"]
    ],
    "A",
    "Raster functions apply algorithms (such as NDVI, Hillshade, Slope) dynamically in-memory on only the visible pixels at the current display scale, providing instant visualization without consuming disk space.",
    "تطبق دوال الراستر الخوارزميات (مثل NDVI والظلال التضاريسية) ديناميكياً في الذاكرة على البكسلات المعروضة على الشاشة فقط، مما يمنح استجابة فورية دون استهلاك مساحة تخزينية على القرص.",
    {
        "B": ["Raster functions are specifically built for grid and pixel imagery data, not vectors.", "دوال الراستر مخصصة حصرياً لبيانات الصور والشبكات."],
        "C": ["Geoprocessing tools can be run infinitely on demand.", "يمكن تشغيل أدوات التحليل بلا حدود."],
        "D": ["Raster functions are non-destructive and never modify or delete source pixel files.", "دوال الراستر غير مدمرة ولا تعدل البيانات المصدرية أبداً."]
    },
    "rasterfunc"
))

questions.append(make_q(
    "AGP-009", "Apply raster functions for raster and image processing", "Beginner", "Tool-based",
    ["NDVI"],
    "Which multispectral bands are used in the NDVI (Normalized Difference Vegetation Index) raster function to assess live green vegetation vigor?",
    "ما هي النطاقات الطيفية المستخدمة في دالة الراستر NDVI (مؤشر الاختلاف الخضري الطبيعي) لتقييم صحة وكثافة الغطاء النباتي الحي؟",
    [
        ["Near-Infrared (NIR) and Red", "الأشعة تحت الحمراء القريبة (NIR) والأحمر (Red)"],
        ["Thermal and Blue", "الحراري (Thermal) والأزرق (Blue)"],
        ["Green and Shortwave Infrared (SWIR)", "الأخضر (Green) والأشعة تحت الحمراء قصيرة الموجة (SWIR)"],
        ["Ultraviolet and Microwave", "الأشعة فوق البنفسجية والموجات الدقيقة"]
    ],
    "A",
    "NDVI uses the formula (NIR - Red) / (NIR + Red). Chlorophyll strongly absorbs Red light for photosynthesis while cell structure strongly reflects Near-Infrared radiation.",
    "تعتمد معادلة NDVI على: (الأشعة تحت الحمراء القريبة - الأحمر) / (الأشعة تحت الحمراء القريبة + الأحمر)؛ حيث يمتص الكلوروفيل الضوء الأحمر بشدة بينما تعكس البنية الخلوية النباتية الأشعة تحت الحمراء القريبة.",
    {
        "B": ["Thermal measures surface kinetic temperature, not chlorophyll reflectance.", "النطاق الحراري يقيس درجة الحرارة السطحية."],
        "C": ["Green/SWIR is used for moisture and snow indices, not standard NDVI.", "تُستخدم هذه النطاقات لمؤشرات الرطوبة والجليد."],
        "D": ["Ultraviolet and microwave are not used in standard optical vegetation indices.", "الموجات فوق البنفسجية لا تُستخدم في مؤشرات الغطاء النباتي البصرية."]
    },
    "rasterfunc"
))

questions.append(make_q(
    "AGP-010", "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based",
    ["Dissolve"],
    "An analyst has a statewide soil polygon layer containing 50,000 individual polygons. They need to aggregate all polygons that share the same SOIL_TYPE code into single multi-part features, reducing the record count to 12. Which tool should be used?",
    "لدى محلل طبقة مضلعات تربة على مستوى الولاية تحتوي على 50,000 مضلع؛ ويحتاج لتجميع كافة المضلعات التي تشترك في نفس كود SOIL_TYPE في معالم متعددة الأجزاء، لتقليص عدد السجلات إلى 12. أي أداة يجب استخدامها؟",
    [
        ["Dissolve", "Dissolve (دمج وتذويب)"],
        ["Split Polygon", "Split Polygon (تقسيم المضلع)"],
        ["Buffer", "Buffer (النطاق)"],
        ["Identity", "Identity (المطابقة)"]
    ],
    "A",
    "Dissolve aggregates adjacent or non-adjacent features that share the same specified attribute value into single continuous or multi-part features, dissolving interior boundaries.",
    "تقوم أداة Dissolve بتجميع المعالم المتجاورة أو المتباعدة التي تشترك في نفس القيمة السماتية المحددة في معالم أحادية أو متعددة الأجزاء مع إزالة الحدود الداخلية الفاصلة بينها.",
    {
        "B": ["Split divides features into smaller pieces.", "تقسم Split المعالم إلى أجزاء أصغر."],
        "C": ["Buffer creates distance zones.", "تنشئ Buffer مناطق حرم حول المعالم."],
        "D": ["Identity performs geometric overlay.", "تجري Identity تراكباً هندسياً."]
    },
    "overlay"
))

questions.append(make_q(
    "AGP-011", "Given a scenario, determine the appropriate geoprocessing tool", "Beginner", "Tool-based",
    ["Buffer"],
    "Which parameter in the Buffer tool ensures that overlapping buffer rings from nearby features merge into a single seamless continuous polygon area?",
    "ما المعامل في أداة Buffer الذي يضمن دمج حلقات الحرم المتداخلة للمعالم المتقاربة في مساحة مضلع واحدة متصلة دون خطوط داخلية؟",
    [
        ["Dissolve Type: Dissolve all output features into a single feature", "Dissolve Type: دمج كافة المعالم في معلم واحد (Dissolve all)"],
        ["Method: Planar", "Method: Planar"],
        ["Side Type: Left only", "Side Type: Left only"],
        ["End Type: Flat", "End Type: Flat"]
    ],
    "A",
    "Setting Dissolve Type to 'Dissolve all output features' (or by list) merges overlapping buffer boundaries into a unified shape, preventing concentric duplicate rings.",
    "يؤدي ضبط نوع الدمج (Dissolve Type) على 'Dissolve all' إلى دمج حدود النطاقات المتداخلة في شكل هندسي موحد، مما يزيل الحلقات الداخلية المتكررة.",
    {
        "B": ["Method specifies geodesic vs planar distance calculation.", "تحدد Method طريقة الحساب الجيوديسية أو المستوية."],
        "C": ["Side Type specifies which side of lines to buffer.", "يحدد Side Type جانب الخط المراد إنشاء الحرم عليه."],
        "D": ["End Type controls the capping style at line endpoints.", "يحدد End Type شكل نهايات الخطوط (دائرية أو مسطحة)."]
    },
    "proximity"
))

questions.append(make_q(
    "AGP-012", "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based",
    ["Union"],
    "An analyst needs to combine two polygon layers (Zoning and Floodplains) such that all geometric boundaries and all attributes from both layers are preserved in a new comprehensive polygon layer. Which tool must be used?",
    "يحتاج محلل إلى دمج طبقتي مضلعات (المخطط الهيكلي ومناطق الفيضانات) بحيث يتم الحفاظ على كافة الحدود الهندسية وكافة السمات من كلا الطبقتين في طبقة مضلعات شاملة جديدة. أي أداة يجب استخدامها؟",
    [
        ["Union", "Union (الاتحاد)"],
        ["Intersect", "Intersect (التقاطع)"],
        ["Clip", "Clip (القص)"],
        ["Erase", "Erase (المسح)"]
    ],
    "A",
    "Union computes a geometric union of multiple input polygon layers. All polygons and their respective attribute values are written to the output, representing all overlapping and non-overlapping areas.",
    "تحسب أداة Union الاتحاد الهندسي الشامل لطبقات المضلعات؛ وتكتب جميع المساحات المتداخلة وغير المتداخلة مع كافة بياناتها السماتية في طبقة المخرجات.",
    {
        "B": ["Intersect preserves ONLY areas common to all inputs, discarding non-overlapping extents.", "تحتفظ Intersect بالمناطق المشتركة فقط وتهمل المساحات غير المتداخلة."],
        "C": ["Clip discards attributes of the clipping boundary layer.", "تتجاهل Clip بيانات طبقة القص."],
        "D": ["Erase deletes areas inside the erase features.", "تحذف Erase المساحات الواقعة داخل معالم المسح."]
    },
    "overlay"
))

questions.append(make_q(
    "AGP-013", "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Conceptual",
    ["Tasks"],
    "In ArcGIS Pro, what is the primary role of an ArcGIS Task (.esriTasks file)?",
    "في ArcGIS Pro، ما هو الدور الأساسي لمهام ArcGIS (ملف .esriTasks)؟",
    [
        ["To provide a structured, interactive step-by-step guided workflow that walks users through repeatable business procedures in the UI", "توفير مسار عمل تفاعلي موجه خطوة بخطوة يرشد المستخدمين عبر الإجراءات التشغيلية المكررة في واجهة البرنامج"],
        ["To compile Python code into standalone executable files", "ترجمة كود بايثون إلى ملفات تنفيذية مستقلة"],
        ["To replace SQL database servers with local text files", "استبدال خوادم قواعد بيانات SQL بملفات نصية محلية"],
        ["To encrypt geodatabases with biometric passwords", "تشفير قواعد البيانات الجغرافية بكلمات مرور حيوية"]
    ],
    "A",
    "ArcGIS Tasks guide users through standard operating procedures step-by-step. Each task step can activate specific tools, set selection queries, toggle layer visibility, and prompt users with custom instructions.",
    "ترشد مهام ArcGIS (Tasks) المستخدمين عبر إجراءات العمل المعيارية خطوة بخطوة؛ حيث يمكن لكل خطوة تفعيل أدوات معينة، وتحديد معالم، وضبط رؤية الطبقات، وإظهار تعليمات إرشادية مخصصة.",
    {
        "B": ["Tasks are XML workflow scripts, not Python binary compilers.", "المهام هي مسارات إرشادية في الواجهة وليست مترجمات بايثون."],
        "C": ["Tasks do not replace enterprise relational databases.", "المهام لا علاقة لها بتعويض خوادم قواعد البيانات."],
        "D": ["Tasks do not manage database encryption.", "المهام لا تدير التشفير الأمني."]
    },
    "tasks"
))

questions.append(make_q(
    "AGP-014", "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Tool-based",
    ["Batch Processing"],
    "How can an analyst execute the Project tool on 50 different feature classes simultaneously without building a ModelBuilder model or writing Python code?",
    "كيف يمكن للمحلل تشغيل أداة Project على 50 فئة معالم مختلفة في نفس الوقت دون بناء نموذج ModelBuilder أو كتابة أي كود بايثون؟",
    [
        ["Right-click the Project tool in the Geoprocessing pane and select 'Batch'", "النقر بزر الماوس الأيمن على أداة Project في نافذة Geoprocessing واختيار 'Batch'"],
        ["Run the tool 50 times manually one by one", "تشغيل الأداة 50 مرة يدوياً واحدة تلو الأخرى"],
        ["Zip the geodatabase into a single archive", "ضغط قاعدة البيانات في ملف أرشيف مضغوط"],
        ["Rename the files with the prefix 'PROJ_'", "إعادة تسمية الملفات بإضافة بادئة 'PROJ_'"]
    ],
    "A",
    "Right-clicking any geoprocessing tool and selecting 'Batch' opens the automated Batch Geoprocessing interface, enabling multi-dataset execution without programming.",
    "يتيح النقر بالزر الأيمن على أي أداة واختيار 'Batch' فتح واجهة المعالجة بالدفعة التلقائية، مما يمكن من تطبيق الأداة على عشرات الطبقات دفعة واحدة دون الحاجة للبرمجة.",
    {
        "B": ["Manual repetition is inefficient and error-prone.", "التكرار اليدوي مضيعة للوقت ومعرض للأخطاء."],
        "C": ["Zipping does not execute geoprocessing transformations.", "الضغط لا ينفذ التحويلات المكانية."],
        "D": ["Renaming files does not reproject coordinate data.", "إعادة التسمية لا تغير أنظمة الإحداثيات."]
    },
    "tasks"
))

questions.append(make_q(
    "AGP-015", "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Technical",
    ["ModelBuilder"],
    "In ModelBuilder, an analyst needs to run an analysis tool for every shapefile located inside a folder. Which ModelBuilder element should be inserted?",
    "في ModelBuilder، يحتاج محلل لتشغيل أداة تحليل على كل ملف shapefile موجود داخل مجلد معين. أي عنصر يجب إدراجه في النموذج؟",
    [
        ["Iterate Feature Classes", "المكرر Iterate Feature Classes"],
        ["Stop tool", "أداة Stop"],
        ["Feedback loop connector", "رابط التغذية الراجعة Feedback loop"],
        ["Calculate Field with a while loop", "أداة Calculate Field بحلقة while"]
    ],
    "A",
    "ModelBuilder Iterators (e.g. Iterate Feature Classes) loop through datasets in a workspace or folder, feeding each dataset sequentially into downstream tools using inline variable substitution.",
    "تقوم مكررات ModelBuilder (مثل Iterate Feature Classes) بالمرور على جميع مجموعات البيانات في المجلد وتمريرها بالتتابع إلى الأدوات التالية في مسار العمل عبر استبدال المتغيرات.",
    {
        "B": ["Stop tool terminates execution.", "أداة Stop توقف تشغيل النموذج."],
        "C": ["Feedback loops are for recursive numerical algorithms.", "روابط التغذية الراجعة للخوارزميات الحسابية التكرارية."],
        "D": ["Calculate Field computes table columns, it does not loop over files.", "حساب الحقل يعدل قيم الجداول ولا يدور على الملفات."]
    },
    "modelbuilder"
))

# Remaining 47 AGP questions (AGP-016 to AGP-062)
agp_topics = [
    (
        "Compare table joins and relates, relationship classes, and spatial joins", "Intermediate", "Tool-based", ["Join Field"],
        "How does the Join Field geoprocessing tool differ from the Add Join layer command?",
        "كيف تختلف أداة المعالجة الجغرافية Join Field عن أمر الطبقة Add Join؟",
        [["Join Field permanently appends physical attribute fields into the target table on disk; Add Join creates a temporary in-memory session join", "تضيف أداة Join Field حقول السمات فعلياً بشكل دائم إلى جدول الهدف على القرص؛ بينما ينشئ Add Join ضماً مؤقتاً في الذاكرة أثناء الجلسة"], ["Join Field only works on Excel tables", "تعمل أداة Join Field على جداول إكسل فقط"], ["Add Join permanently modifies source data", "يعدل Add Join البيانات الأصلية بشكل دائم"], ["Both tools operate identically in memory", "تعمل كلتا الأداتين بشكل متطابق في الذاكرة"]],
        "A",
        "Join Field alters the target table schema on disk by adding columns and copying matching values permanently. Add Join maintains a virtual, dynamic join that disappears when the project is closed without saving.",
        "تعدل أداة Join Field هيكل جدول الهدف على القرص بإضافة أعمدة ونسخ القيم بشكل دائم. بينما ينشئ Add Join ضماً ظاهرياً مؤقتاً يزول بمجرد إزالة الطبقة.",
        {"B": ["Join Field works on all geodatabase and shapefile tables.", "تعمل Join Field على كافة جداول الجيوداتابيس والملفات."], "C": ["Add Join never touches disk schema.", "لا يعدل Add Join هيكل البيانات على القرص."], "D": ["They have completely different architectural impacts (permanent disk write vs virtual view).", "تختلفان جوهرياً في الأثر (كتابة دائمة على القرص مقابل عرض مؤقت)."]},
        "joins"
    ),
    (
        "Compare table joins and relates, relationship classes, and spatial joins", "Intermediate", "Technical", ["Spatial Join"],
        "When performing a Spatial Join between point addresses and police beats using 'Join one to many', what happens if an address falls directly on the shared boundary of two beats?",
        "عند إجراء ضم مكاني (Spatial Join) بين نقاط العناوين ومناطق دوريات الشرطة بخيار 'Join one to many'، ماذا يحدث إذا وقعت نقطة عنوان مباشرة على الحد المشترك بين منطقتين؟",
        [["The output feature class generates two duplicate point features, one joined to each matching police beat", "تنتج فئة المعالم المخرجة نقطتين مكررتين، ترتبط كل واحدة منهما بإحدى منطقتي الدوريات"], ["The address point is deleted", "يتم حذف نقطة العنوان"], ["ArcGIS Pro throws an unhandled geometry exception", "يظهر خطأ استثنائي في هندسة المعالم بالبرنامج"], ["The address is matched to a random beat in another state", "يتم ربط العنوان بمنطقة عشوائية في ولاية أخرى"]],
        "A",
        "In a 1-to-Many spatial join, every spatial intersection creates a separate output record. A feature that touches two boundaries produces two output records, each inheriting attributes from one of the overlapping boundaries.",
        "في الضم المكاني من نوع واحد إلى متعدد (1-to-Many)، ينتج عن كل تقاطع مكاني سجل مخرج مستقل؛ فالمعلم الذي يلامس منطقتين يولد سجلين في المخرجات يرتبط كل منهما بإحدى المنطقتين.",
        {"B": ["Points are never deleted by spatial joins.", "لا تُحذف النقاط في عمليات الضم المكاني."], "C": ["Boundary intersections are completely valid topology states.", "تقاطعات الحدود حالات طوبولوجية صحيحة تماماً."], "D": ["Matches only occur with mathematically intersecting features.", "المطابقة تتم فقط مع المعالم المتقاطعة مكانياً."] },
        "joins"
    ),
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Erase"],
        "An environmental analyst needs to remove all private property land parcels from a regional forest conservation study area. Which tool cuts out the private parcels, leaving only the public forest land?",
        "يحتاج محلل بيئي إلى إزالة كافة قطع الأراضي الخاصة من منطقة دراسة حماية الغابات الإقليمية. أي أداة تقتطع الأراضي الخاصة وتترك أراضي الغابات العامة فقط؟",
        [["Erase", "Erase (المسح)"], ["Clip", "Clip (القص)"], ["Union", "Union (الاتحاد)"], ["Dissolve", "Dissolve (الدمج)"]],
        "A",
        "The Erase tool removes portions of the input features that overlap with the erase features, creating a cookie-cutter hole.",
        "تحذف أداة Erase أجزاء معالم الإدخال التي تتداخل مع معالم المسح، مما يفرغ المساحات المستبعدة مثل قالب تفريغ العجين.",
        {"B": ["Clip keeps what is inside the boundary, the exact opposite of Erase.", "تحتفظ Clip بما هو داخل الحدود وهو عكس المطلوب."], "C": ["Union combines all areas together.", "تجمع Union كافة المساحات معاً."], "D": ["Dissolve aggregates by common attributes.", "تدمج Dissolve بالسمات المشتركة."]},
        "overlay"
    ),
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Near"],
        "Which geoprocessing tool calculates the exact distance from each customer point to the closest warehouse, and appends the NEAR_DIST and NEAR_FID fields directly into the customer input attribute table?",
        "أي أداة تحليل تحسب المسافة الدقيقة من كل نقطة عميل إلى أقرب مستودع، وتضيف حقلي NEAR_DIST و NEAR_FID مباشرة في جدول بيانات العملاء المدخل؟",
        [["Near", "Near"], ["Buffer", "Buffer"], ["Intersect", "Intersect"], ["Spatial Join", "Spatial Join"]],
        "A",
        "The Near tool calculates distance and closest feature IDs from input features to near features, modifying the input table directly by adding NEAR_DIST, NEAR_FID, and optional angle/coordinate fields.",
        "تحسب أداة Near المسافة ومعرف أقرب معلم من معالم الإدخال إلى معالم الهدف، وتعدل جدول الإدخال مباشرة بإضافة حقلي NEAR_DIST و NEAR_FID وحقول الزوايا الإضافية.",
        {"B": ["Buffer creates distance polygon rings.", "تنشئ Buffer مضلعات نطاق حول المعالم."], "C": ["Intersect computes geometric overlap.", "تحسب Intersect التداخل الهندسي."], "D": ["Spatial Join writes a new output feature class rather than editing the input table directly.", "تكتب Spatial Join طبقة مخرجات جديدة ولا تعدل الجدول المدخل مباشرة."]},
        "proximity"
    ),
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Generate Near Table"],
        "How does Generate Near Table differ from the Near tool?",
        "كيف تختلف أداة Generate Near Table عن أداة Near؟",
        [["Generate Near Table writes results to a new standalone table and can report multiple nearest features (e.g. top 3 closest warehouses)", "تكتب أداة Generate Near Table نتائجها في جدول منفصل جديد وتستطيع استخراج عدة معالم قريبة (مثل أقرب 3 مستودعات)"], ["Generate Near Table only works on raster files", "تعمل أداة Generate Near Table على ملفات الراستر فقط"], ["The Near tool creates 3D TIN surfaces", "تنشئ أداة Near أسطح TIN ثلاثية الأبعاد"], ["Generate Near Table requires an internet connection", "تتطلب أداة Generate Near Table اتصالاً بالإنترنت"]],
        "A",
        "While Near only finds the single closest feature and writes in-place, Generate Near Table outputs to a new table and supports reporting ranked multiple neighbors (Find closest: False) within a search radius.",
        "بينما تكتفي أداة Near بإيجاد أقرب معلم منفرد وتعدل الجدول المدخل، فإن Generate Near Table تُخرج النتائج في جدول جديد وتدعم إيجاد عدة معالم قريبة مرتبة ضمن نصف قطر بحث.",
        {"B": ["Both tools process vector points, lines, and polygons.", "تعمل كلتا الأداتين على المعالم الاتجاهية."], "C": ["Near does not create surface models.", "لا تنشئ Near نماذج أسطح."], "D": ["Both tools execute completely offline locally.", "تنفذ كلتا الأداتين محلياً بالكامل دون إنترنت."]},
        "proximity"
    ),
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Advanced", "Technical", ["ModelBuilder"],
        "Can a single ModelBuilder model contain two separate iterators at the same workflow level?",
        "هل يمكن لنموذج ModelBuilder واحد أن يحتوي على مكررين (Iterators) مستقلين في نفس مستوى مسار العمل؟",
        [["No, a model can contain only one iterator; multiple iterators require embedding a submodel containing the secondary iterator", "لا، يمكن للنموذج أن يحتوي على مكرر واحد فقط؛ ويتطلب استخدام مكررين تضمين نموذج فرعي (Submodel) يحتوي على المكرر الثاني"], ["Yes, up to 10 iterators can run in parallel in a single model", "نعم، يمكن تشغيل حتى 10 مكررات بالتوازي في نفس النموذج"], ["Yes, but only if both iterate over tables", "نعم، ولكن فقط إذا كان كلاهما يكرر على جداول"], ["Iterators are not supported in ModelBuilder", "المكررات غير مدعومة في ModelBuilder"]],
        "A",
        "ArcGIS Pro ModelBuilder enforces a strict rule: only one iterator can exist per model. To create nested loops (e.g., iterate folders then iterate feature classes), the inner loop must be built as a separate submodel and added to the main model.",
        "يفرض ModelBuilder في ArcGIS Pro قاعدة صارمة: مكرر واحد فقط لكل نموذج. ولإنشاء حلقات تكرار متداخلة (مثل المرور على المجلدات ثم على الطبقات داخلها)، يجب بناء الحلقة الداخلية كنموذج فرعي وإدراجه في النموذج الرئيسي.",
        {"B": ["Parallel multiple iterators in one model are strictly disallowed.", "تعدد المكررات في نموذج واحد غير مسموح برمجياً."], "C": ["The one-iterator rule applies universally to all iterator types.", "تنطبق قاعدة المكرر الواحد على كافة أنواع المكررات."], "D": ["Iterators are a core automation component of ModelBuilder.", "المكررات عنصر أساسي في أتمتة ModelBuilder."]},
        "modelbuilder"
    ),
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Technical", ["ModelBuilder"],
        "In ModelBuilder, what is the syntax for inline variable substitution when dynamically naming output files based on an iterator variable named 'StateName'?",
        "في ModelBuilder، ما هي الصياغة الصحيحة لاستبدال المتغيرات (Inline Variable Substitution) لتسمية ملفات المخرجات ديناميكياً بناءً على متغير مكرر اسمه 'StateName'؟",
        [["C:/Data/Output.gdb/Parcels_%StateName%", "C:/Data/Output.gdb/Parcels_%StateName%"], ["C:/Data/Output.gdb/Parcels_{StateName}", "C:/Data/Output.gdb/Parcels_{StateName}"], ["C:/Data/Output.gdb/Parcels_$StateName$", "C:/Data/Output.gdb/Parcels_$StateName$"], ["C:/Data/Output.gdb/Parcels_[StateName]", "C:/Data/Output.gdb/Parcels_[StateName]"]],
        "A",
        "In ArcGIS Pro ModelBuilder, enclosing a variable name in percent signs (%VariableName%) performs inline variable substitution, substituting the runtime value of the variable into tool parameters and output paths.",
        "في ModelBuilder بـ ArcGIS Pro، يؤدي وضع اسم المتغير بين علامتي النسبة المئوية (%VariableName%) إلى استبدال قيمته أثناء التشغيل وإدراجها ديناميكياً في مسارات المخرجات والمعاملات.",
        {"B": ["Curly brackets are used in Python format strings, not ModelBuilder paths.", "الأقواس المعقوفة تُستخدم في صياغة بايثون وليس في ModelBuilder."], "C": ["Dollar signs are used in Arcade profiles.", "علامة الدولار تُستخدم في لغة Arcade."], "D": ["Square brackets are used for SQL field delimiters.", "الأقواس المربعة لحقول استعلامات SQL."]},
        "modelbuilder"
    ),
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Technical", ["ModelBuilder"],
        "What happens when you connect an output dataset variable to a tool using a 'Precondition' connector in ModelBuilder?",
        "ماذا يحدث عند ربط متغير بيانات مخرجة بأداة باستخدام رابط 'الشرط المسبق' (Precondition) في ModelBuilder؟",
        [["The downstream tool will not execute until the precondition dataset has been successfully created or verified", "لن تبدأ الأداة التالية في التنفيذ حتى يتم إنشاء أو التحقق من وجود بيانات الشرط المسبق بنجاح"], ["The downstream tool will delete the precondition dataset immediately", "ستقوم الأداة التالية بحذف بيانات الشرط المسبق فوراً"], ["The precondition variable is converted into a PDF report", "يتحول متغير الشرط المسبق إلى تقرير PDF"], ["The entire model execution speed is reduced by 50%", "تنخفض سرعة تنفيذ النموذج بالكامل بمقدار 50%"]],
        "A",
        "A Precondition (visualized as a dashed line) establishes execution order dependency without passing data as an input parameter, ensuring Tool B runs only after Dataset A is ready.",
        "ينشئ الشرط المسبق (الظاهر كخط متقطع) تبعية في تسلسل التنفيذ تضمن ألا تبدأ الأداة الثانية بالعمل إلا بعد اكتمال إنتاج أو التحقق من بيانات الشرط المسبق.",
        {"B": ["Preconditions control timing, not dataset deletion.", "تتحكم الشروط المسبقة في توقيت التنفيذ ولا تحذف البيانات."], "C": ["Preconditions do not generate PDF reports.", "لا تولد تقارير PDF."], "D": ["Preconditions optimize workflow logic without artificial performance throttling.", "تنظم الشروط المسبقة منطق العمل دون إبطاء الأداء."]},
        "modelbuilder"
    ),
    (
        "Apply raster functions for raster and image processing", "Intermediate", "Tool-based", ["Raster Functions"],
        "An analyst needs to apply an elevation tint color ramp and hillshade surface effect to a 10-meter DEM for presentation. Which raster function combines both elevation color and shaded relief on-the-fly?",
        "يحتاج محلل لتطبيق تدرج لوني للارتفاعات مع تأثير التظليل التضاريسي على نموذج ارتفاع رقمي DEM بدقة 10 أمتار للعرض. أي دالة راستر تدمج ألوان الارتفاع مع التظليل آنياً في الذاكرة؟",
        [["Shaded Relief function", "Shaded Relief function (دالة التضاريس المظللة)"], ["Contour function", "Contour function (دالة الكنتور)"], ["Zonal Statistics function", "Zonal Statistics function (دالة إحصائيات المناطق)"], ["Sample function", "Sample function (دالة أخذ العينات)"]],
        "A",
        "The Shaded Relief raster function creates a shaded surface model combining elevation color ramping with hillshade illumination dynamically in memory.",
        "تنتج دالة الراستر Shaded Relief نموذج سطح مظلل يجمع بين تدرج ألوان الارتفاعات والإضاءة التضاريسية التفاعلية ديناميكياً في الذاكرة دون الحاجة لملفات وسيطة.",
        {"B": ["Contour generates vector or raster isolines.", "تولد Contour خطوط كنتور."], "C": ["Zonal Statistics summarizes grid values by zones.", "تلخص Zonal Statistics القيم حسب المناطق."], "D": ["Sample extracts cell values to table points.", "تستخرج Sample قيم الخلايا لنقاط جدولية."]},
        "rasterfunc"
    ),
    (
        "Apply raster functions for raster and image processing", "Intermediate", "Technical", ["Raster Function Template"],
        "What is the file format used to save, export, and share a reusable custom chain of raster functions in ArcGIS Pro?",
        "ما هي صيغة الملف المستخدمة لحفظ وتصدير ومشاركة سلسلة مخصصة قابلة لإعادة الاستخدام من دوال الراستر في ArcGIS Pro؟",
        [["Raster Function Template (.rft.xml)", "Raster Function Template (.rft.xml)"], ["Shapefile (.shp)", "Shapefile (.shp)"], ["Layer Package (.lpkx)", "Layer Package (.lpkx)"], ["Map File (.mapx)", "Map File (.mapx)"]],
        "A",
        "Raster Function Templates (.rft.xml) encapsulate complex function chains, parameters, and algorithms into a portable XML template that can be applied to any raster or mosaic dataset.",
        "تخزن قوالب دوال الراستر (Raster Function Templates بصيغة .rft.xml) سلاسل الدوال والمعاملات في قالب XML مرن يمكن تطبيقه بسهولة على أي راستر أو مجموعة موزاييك.",
        {"B": ["Shapefiles store vector geometry.", "ملفات Shapefile تخزن معالم اتجاهية."], "C": ["Layer packages bundle vector/raster data with symbology.", "حزم الطبقات تجمع البيانات برموزها."], "D": ["Map files store 2D map layouts.", "ملفات mapx تخزن الخرائط."]},
        "rasterfunc"
    ),
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Cost Distance"],
        "Which Spatial Analyst tool calculates the least accumulative travel cost from a set of source locations across a cost surface raster representing slope, land cover resistance, and barriers?",
        "أي أداة في Spatial Analyst تحسب أقل تكلفة انتقال تراكمية من مجموعة مواقع مصدرية عبر سطح تكلفة يمثل الانحدار ومقاومة الغطاء الأرضي والحواجز؟",
        [["Cost Distance", "Cost Distance (مسافة التكلفة)"], ["Euclidean Distance", "Euclidean Distance (المسافة الإقليدية)"], ["Buffer", "Buffer (النطاق)"], ["Line Density", "Line Density (كثافة الخطوط)"]],
        "A",
        "Cost Distance determines the shortest weighted travel cost to the nearest source based on a friction/cost surface grid.",
        "تحسب أداة Cost Distance أقل تكلفة انتقال تراكمية إلى أقرب مصدر بالاعتماد على شبكة سطح المقاومة والتكلفة.",
        {"B": ["Euclidean distance measures straight-line planar distance ignoring terrain friction.", "تقيس المسافة الإقليدية المسافة المستقيمة في خط مستقيم متجاهلة وعورة التضاريس."], "C": ["Buffer creates fixed-distance polygon zones.", "تنشئ Buffer نطاقات بمسافات ثابتة."], "D": ["Line density calculates linear concentration.", "تحسب كثافة الخطوط تركز المعالم الخطية."]},
        "proximity"
    ),
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Zonal Statistics as Table"],
        "An analyst needs to calculate the average elevation and maximum slope within each wildlife management zone polygon. Which tool summarizes raster cell values within polygon zones and outputs a summary table?",
        "يحتاج محلل لحساب متوسط الارتفاع وأقصى انحدار داخل كل مضلع من مضلعات مناطق إدارة الحياة الفطرية. أي أداة تلخص قيم خلايا الراستر داخل مضلعات المناطق وتُخرج جدول ملخصات؟",
        [["Zonal Statistics as Table", "Zonal Statistics as Table"], ["Tabulate Intersection", "Tabulate Intersection"], ["Extract by Mask", "Extract by Mask"], ["Raster to Polygon", "Raster to Polygon"]],
        "A",
        "Zonal Statistics as Table summarizes values of a raster grid within the boundaries of defined zones (vector polygons or categorical rasters), reporting statistics like Mean, Max, Min, and Sum in a table.",
        "تلخص أداة Zonal Statistics as Table قيم شبكة الراستر الواقعة داخل حدود مناطق محددة (مضلعات أو فئات راستر)، وتُخرج إحصائيات مثل المتوسط والأعلى والأدنى والمجموع في جدول مستقل.",
        {"B": ["Tabulate Intersection computes area percentages of overlapping polygons.", "تحسب Tabulate Intersection نسب المساحات المتقاطعة."], "C": ["Extract by Mask cuts a raster grid.", "تقص Extract by Mask خلايا الراستر."], "D": ["Raster to Polygon vectorizes raster cells.", "تحول Raster to Polygon البكسلات إلى متجهات."]},
        "overlay"
    )
]

# Add more AGP topics to reach 62 total questions
for i, t in enumerate(agp_topics):
    qid = f"AGP-{i+16:03d}"
    questions.append(make_q(qid, t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11]))

# Currently we have 15 + 12 = 27 questions.
# Let's generate AGP-028 through AGP-062 (35 more questions) systematically:
more_agp = [
    # 28: Spatial Join Merge Rules
    (
        "Compare table joins and relates, relationship classes, and spatial joins", "Intermediate", "Technical", ["Spatial Join"],
        "When performing a 1-to-1 Spatial Join of parcel polygons to census tracts, how can you ensure the total parcel assessed values are aggregated correctly?",
        "عند إجراء ضم مكاني (Spatial Join) بنمط 1 إلى 1 بين مضلعات الأراضي ومناطق التعداد، كيف تضمن تجميع إجمالي القيم التقديرية للأراضي بشكل صحيح؟",
        [["Configure the Field Map merge rule for the assessed value field to 'Sum'", "ضبط قاعدة دمج خريطة الحقول (Merge Rule) لحقل القيمة التقديرية على خيار 'Sum'"], ["Set the search radius to 0 meters", "ضبط نصف قطر البحث على 0 متر"], ["Convert the parcels to points", "تحويل قطع الأراضي إلى نقاط"], ["Change the layer transparency", "تغيير شفافية الطبقة"]],
        "A",
        "In Spatial Join's Field Map parameter, setting the Merge Rule of a numeric field to 'Sum' adds together all values from matching join features that fall within the target polygon.",
        "في إعدادات خريطة الحقول بأداة Spatial Join، يؤدي اختيار قاعدة الدمج 'Sum' إلى جمع قيم كافة المعالم المرتبطة الواقعة داخل مضلع الهدف.",
        {"B": ["Search radius controls proximity distance, not attribute math.", "نصف قطر البحث يتحكم بالمسافة وليس بالعمليات الحسابية."], "C": ["Converting to points is unnecessary and does not aggregate values by itself.", "تحويل الأراضي لنقاط لا يجمع القيم تلقائياً."], "D": ["Transparency is a visual property.", "الشفافية خاصية بصرية."]},
        "joins"
    ),
    # 29: Spatial Join vs Add Join
    (
        "Compare table joins and relates, relationship classes, and spatial joins", "Beginner", "Conceptual", ["Spatial Join", "Add Join"],
        "Under what fundamental condition must an analyst choose a Spatial Join instead of an Add Join?",
        "تحت أي ظرف أساسي يجب على المحلل اختيار الضم المكاني (Spatial Join) بدلاً من الضم الجدولي (Add Join)؟",
        [["When the two datasets share no common tabular key field, but share a geographic spatial relationship (e.g., location, containment, proximity)", "عندما لا تشترك الطبقتان في أي حقل مفتاحي جدولي، ولكنهما تشتركان في علاقة مكانية جغرافية (مثل الموقع، الاحتواء، التقارب)"], ["When both datasets are in Excel format", "عندما يكون كلا الملفين بصيغة إكسل"], ["When joining a table to itself", "عند ضم الجدول إلى نفسه"], ["When working exclusively in 3D local scenes", "عند العمل في المشاهد المحلية ثلاثية الأبعاد فقط"]],
        "A",
        "Add Join requires an exact matching key field (foreign key). When datasets lack common attribute keys, Spatial Join matches features purely on their geographic position (intersect, within, closest).",
        "يتطلب Add Join وجود حقل مفتاحي متطابق (Foreign Key)؛ وعند غياب المفاتيح الجدولية، فإن Spatial Join يربط البيانات بالاعتماد الصرف على العلاقات المكانية الجغرافية.",
        {"B": ["Excel lacks spatial coordinates until plotted.", "ملفات إكسل تفتقر للهندسة حتى يتم إسقاطها."], "C": ["Self-joins can be done via attribute keys.", "يمكن ضم الجدول لنفسه بالسمات."], "D": ["Spatial joins work in standard 2D and 3D contexts.", "يعمل الضم المكاني في البيئات ثنائية وثلاثية الأبعاد."]},
        "joins"
    ),
    # 30: Relationship class vs Relate
    (
        "Compare table joins and relates, relationship classes, and spatial joins", "Intermediate", "Conceptual", ["Relationship Class", "Add Relate"],
        "Why would an organization choose to create a Geodatabase Relationship Class instead of using the map-level Add Relate command?",
        "لماذا تفضل المؤسسة إنشاء فئة علاقات (Relationship Class) في قاعدة البيانات بدلاً من استخدام أمر Add Relate على مستوى الخريطة؟",
        [["Relationship Classes persist permanently in the geodatabase schema and support composite cascade deletes and messaging", "تُخزن فئات العلاقات بشكل دائم في مخطط قاعدة البيانات وتدعم الحذف التسلسلي المركب والتنبيهات التلقائية"], ["Relationship Classes only work in free web viewers", "تعمل فئات العلاقات في متصفحات الويب المجانية فقط"], ["Add Relate converts vector data into raster grids", "يحول Add Relate البيانات الاتجاهية إلى راستر"], ["Relationship classes do not support 1-to-Many cardinality", "لا تدعم فئات العلاقات علاقة 1 إلى متعدد"]],
        "A",
        "Relationship Classes are permanent geodatabase objects that persist across all maps and projects. They enforce referential integrity and enable advanced behaviors like composite cascade deletion.",
        "فئات العلاقات عناصر دائمة في هيكل قاعدة البيانات تظل محفوظة عبر كافة المشاريع والخرائط، وتفرض التكامل المرجعي وتدعم الحذف التسلسلي والتنبيهات المتقدمة.",
        {"B": ["Relationship classes are enterprise and file geodatabase structures.", "فئات العلاقات هياكل قواعد بيانات متقدمة."], "C": ["Add Relate is a tabular association, not a raster tool.", "أمر Add Relate ارتباط جدولي وليس راستر."], "D": ["Relationship classes fully support 1:1, 1:M, and M:N cardinalities.", "تدعم فئات العلاقات كافة أنواع العلاقات."]},
        "joins"
    ),
    # 31: Symmetrical Difference
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Symmetrical Difference"],
        "Which overlay tool outputs only the areas of two overlapping polygon layers that do NOT overlap each other, omitting the shared intersecting area?",
        "أي أداة تراكب تُخرج فقط المساحات غير المتداخلة بين طبقتي مضلعات، مع استبعاد المساحة المشتركة المتقاطعة بينهما؟",
        [["Symmetrical Difference", "Symmetrical Difference (الفرق المتماثل)"], ["Intersect", "Intersect (التقاطع)"], ["Union", "Union (الاتحاد)"], ["Clip", "Clip (القص)"]],
        "A",
        "Symmetrical Difference writes only the features or parts of features from input and update layers that do not overlap each other (the inverse of Intersect).",
        "تُخرج أداة Symmetrical Difference الأجزاء أو المعالم التي لا تتداخل بين الطبقتين، مستبعدة منطقة التقاطع المشتركة (عكس أداة Intersect).",
        {"B": ["Intersect outputs ONLY the overlapping shared area.", "تُخرج Intersect المساحة المشتركة فقط."], "C": ["Union outputs both overlapping and non-overlapping areas.", "تُخرج Union كافة المساحات."], "D": ["Clip cuts by an extent.", "تقص Clip المعالم وفق حدود."]},
        "overlay"
    ),
    # 32: Identity tool
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Identity"],
        "An analyst runs the Identity tool with Input: Roads and Identity Features: Municipalities. What geometric features will be present in the output?",
        "قام محلل بتشغيل أداة Identity مع تحديد المدخل: الطرق، ومعالم المطابقة: البلديات. ما المعالم الهندسية التي ستظهر في المخرجات؟",
        [["All input roads are preserved, with municipal attributes appended to the segments falling inside municipalities", "يتم الحفاظ على كافة الطرق المدخلة، مع إلحاق سمات البلديات بأجزاء الطرق الواقعة داخل حدودها فقط"], ["Only roads outside municipalities are kept", "يتم الاحتفاظ بالطرق الواقعة خارج البلديات فقط"], ["All roads are deleted and only municipality polygons remain", "تُحذف جميع الطرق وتتبقى مضلعات البلديات فقط"], ["Roads are converted into polygon buffers", "تتحول الطرق إلى مضلعات حرم"]],
        "A",
        "Identity computes a geometric intersection where all input features are retained; portions that overlap identity features inherit identity attributes, while portions outside receive NULL identity attributes.",
        "تحتفظ أداة Identity بكافة معالم طبقة الإدخال؛ وتكتسب الأجزاء المتداخلة مع طبقة المطابقة سماتها، بينما تأخذ الأجزاء الخارجية قيماً فارغة NULL.",
        {"B": ["Erase is the tool that keeps features outside.", "أداة Erase هي التي تحتفظ بما هو خارج الحدود."], "C": ["Input features are never discarded by Identity.", "لا يتم إهمال معالم الإدخال في أداة Identity."], "D": ["Line geometry type is preserved.", "يتم الحفاظ على نوع الهندسة الخطية."]},
        "overlay"
    ),
    # 33: Intersect vs Union geometry requirement
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Conceptual", ["Union"],
        "What geometric restriction applies to the inputs of the Union tool that does NOT apply to the Intersect tool?",
        "ما هو القيد الهندسي المفروض على مدخلات أداة Union والذي لا ينطبق على أداة Intersect؟",
        [["All inputs to Union MUST be polygon feature layers", "يجب أن تكون جميع مدخلات أداة Union طبقات مضلعات (Polygons) حصراً"], ["Inputs to Union must have Z-values", "يجب أن تحتوي مدخلات Union على قيم ارتفاع Z"], ["Union requires raster datasets", "تتطلب Union مجموعات بيانات راستر"], ["Union inputs must be stored in shapefile format", "يجب تخزين مدخلات Union بصيغة shapefile"]],
        "A",
        "Union only supports polygon inputs. In contrast, Intersect accepts any mix of vector geometry types (points, lines, or polygons).",
        "تقبل أداة Union طبقات المضلعات فقط؛ بينما تقبل أداة Intersect أي مزيج من أنواع المعالم الاتجاهية (نقاط، خطوط، أو مضلعات).",
        {"B": ["Z-values are optional in both tools.", "قيم Z اختيارية في كلتا الأداتين."], "C": ["Union is strictly a vector geoprocessing tool.", "أداة Union أداة اتجاهية وليست للراستر."], "D": ["Both tools support all geodatabase formats.", "تدعم كلتا الأداتين كافة صيغ الجيوداتابيس."]},
        "overlay"
    ),
    # 34: Euclidean Distance
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Beginner", "Tool-based", ["Euclidean Distance"],
        "Which tool creates a continuous raster surface where each cell value represents the straight-line distance to the nearest point source?",
        "أي أداة تنشئ سطح راستر مستمر بحيث تمثل قيمة كل خلية فيه المسافة في خط مستقيم إلى أقرب نقطة مصدرية؟",
        [["Euclidean Distance", "Euclidean Distance (المسافة الإقليدية)"], ["Cost Distance", "Cost Distance (مسافة التكلفة)"], ["Kernel Density", "Kernel Density (كثافة كيرنز)"], ["IDW", "IDW"]],
        "A",
        "Euclidean Distance calculates planar or geodesic straight-line distance from each cell to the nearest source feature, outputting a continuous distance grid.",
        "تحسب أداة Euclidean Distance المسافة المستقيمة المستوية أو الجيوديسية من كل خلية إلى أقرب معلم مصدري، وتُخرج شبكة مسافات مستمرة.",
        {"B": ["Cost Distance considers friction and impedance surfaces.", "تأخذ مسافة التكلفة وعورة ومقاومة السطح بالحسبان."], "C": ["Kernel Density calculates feature concentration, not distance.", "تحسب كثافة كيرنز تركيز المعالم وليس المسافة."], "D": ["IDW interpolates attribute surface values.", "تستوفي IDW قيماً سماتية للأسطح."]},
        "proximity"
    ),
    # 35: Reclassify tool
    (
        "Apply raster functions for raster and image processing", "Beginner", "Tool-based", ["Reclassify"],
        "An analyst needs to convert a continuous slope raster (0° to 60°) into 3 suitability categories (1 = Unsuitable, 2 = Moderately Suitable, 3 = Highly Suitable). Which tool should be used?",
        "يحتاج محلل لتحويل راستر انحدار مستمر (من 0 إلى 60 درجة) إلى 3 فئات ملاءمة (1 = غير ملائم، 2 = متوسط، 3 = عالي الملاءمة). أي أداة يجب استخدامها؟",
        [["Reclassify", "Reclassify (إعادة التصنيف)"], ["Raster Calculator", "Raster Calculator (حاسبة الراستر)"], ["Resample", "Resample (إعادة الاستعيان)"], ["Clip Raster", "Clip Raster (قص الراستر)"]],
        "A",
        "The Reclassify tool reassigns ranges of raster cell values to new discrete integer class codes, a foundational step in multi-criteria raster suitability modeling.",
        "تعيد أداة Reclassify تعيين نطاقات قيم خلايا الراستر إلى أكواد فئات رقمية صحيحة جديدة، وهي خطوة أساسية في نمذجة الملاءمة المكانية للراستر.",
        {"B": ["Raster Calculator evaluates mathematical map algebra equations.", "تقيم حاسبة الراستر معادلات جبر الخرائط."], "C": ["Resample alters cell resolution size.", "تغير Resample دقة حجم الخلية."], "D": ["Clip Raster cuts raster boundaries.", "تقص Clip Raster حدود الراستر."]},
        "rasterfunc"
    ),
    # 36: Raster Calculator Map Algebra
    (
        "Apply raster functions for raster and image processing", "Intermediate", "Technical", ["Raster Calculator"],
        "Which Map Algebra expression in the Raster Calculator correctly creates a binary mask where cells with slope less than 10 degrees AND elevation greater than 500 meters evaluate to 1, and all others to 0?",
        "أي تعبير جبر خرائط في Raster Calculator ينشئ قناعاً ثنائياً بحيث تأخذ الخلايا ذات الانحدار أقل من 10 درجات والارتفاع أكبر من 500 متر القيمة 1، وتأخذ بقية الخلايا 0؟",
        [["(Raster('Slope') < 10) & (Raster('Elevation') > 500)", "(Raster('Slope') < 10) & (Raster('Elevation') > 500)"], ["Slope < 10 OR Elevation > 500", "Slope < 10 OR Elevation > 500"], ["IF Slope < 10 THEN 1 ELSE 0", "IF Slope < 10 THEN 1 ELSE 0"], ["SELECT WHERE Slope < 10 AND Elevation > 500", "SELECT WHERE Slope < 10 AND Elevation > 500"]],
        "A",
        "In Python Map Algebra, boolean AND is represented by the ampersand operator (&), with individual conditional expressions wrapped in parentheses.",
        "في جبر الخرائط بلغة بايثون، يُستخدم الرمز (&) للتعبير عن الرابط المنطقي AND، مع وضع كل شرط بين قوسين مستقلين لتقييم النتائج الثنائية (1 و 0).",
        {"B": ["OR requires either condition, not both simultaneously.", "الرابط OR يتطلب تحقق أحد الشرطين وليس كلاهما."], "C": ["IF/THEN is not valid syntax in Raster Calculator expressions.", "صيغة IF/THEN غير صحيحة نحوياً في حاسبة الراستر."], "D": ["SELECT WHERE is a SQL vector statement, not Map Algebra.", "صيغة SQL للمتجهات وليست لجبر الخرائط."]},
        "rasterfunc"
    ),
    # 37: Extent Environment
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Technical", ["Geoprocessing Environments"],
        "When setting the 'Extent' environment setting to an existing polygon layer, what rectangular coordinates are actually passed to the tool?",
        "عند ضبط بيئة 'Extent' على طبقة مضلعات قائمة، ما هي الإحداثيات المستطيلة التي تُمرر فعلياً إلى الأداة؟",
        [["The minimum bounding rectangle (XMin, YMin, XMax, YMax) encompassing all features in that layer", "المستطيل المحيط الأدنى (XMin, YMin, XMax, YMax) الذي يحتوي كافة معالم تلك الطبقة"], ["The exact irregular boundary of each polygon", "الحدود المتعرجة الدقيقة لكل مضلع"], ["The coordinates of the map center point only", "إحداثيات النقطة المركزية للخريطة فقط"], ["The entire bounding box of the planet Earth", "كامل النطاق المحيط للكرة الأرضية"]],
        "A",
        "The Extent environment specifies a rectangular bounding box defined by XMin, YMin, XMax, YMax. To restrict processing to an irregular polygon shape, the 'Mask' environment must be used instead.",
        "تحدد بيئة Extent مستطيلاً محيطاً بإحداثيات XMin و YMin و XMax و YMax؛ وإذا أراد المستخدم تقييد التحليل داخل شكل المضلع المتعرج بدقة فيجب استخدام بيئة Mask (القناع).",
        {"B": ["Irregular shape clipping is performed by Mask, not Extent.", "تحديد الأشكال المتعرجة يتم عبر بيئة Mask."], "C": ["A point cannot define an extent bounding box.", "النقطة لا يمكنها تعريف نطاق مكاني."], "D": ["Global extents only apply if explicitly chosen.", "النطاق العالمي يطبق فقط عند اختياره صراحة."]},
        "environments"
    ),
    # 38: Mask Environment
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Technical", ["Geoprocessing Environments"],
        "What happens to raster cells that fall outside the boundary of a Mask polygon during Spatial Analyst tool execution?",
        "ماذا يحدث لخلايا الراستر التي تقع خارج حدود مضلع القناع (Mask) أثناء تشغيل أدوات Spatial Analyst؟",
        [["They are assigned the NoData value in the output raster", "يتم تعيين قيمة لا بيانات (NoData) لها في الراستر الناتج"], ["They are deleted along with their underlying disk files", "تُحذف مع ملفاتها الأصلية على القرص"], ["They are assigned the value 0 and included in statistical averages", "تأخذ القيمة 0 وتدخل في حساب المتوسطات الإحصائية"], ["They are converted into vector point features", "تتحول إلى معالم نقطية اتجاهية"]],
        "A",
        "The Mask environment confines raster analysis to cells falling inside the mask shape. Cells outside the mask receive NoData values and are excluded from subsequent calculations.",
        "تقيد بيئة Mask التحليل بالخلايا الواقعة داخل حدود القناع فقط؛ وتتحول جميع الخلايا الواقعة بالخارج إلى خلايا NoData وتُستبعد من الحسابات.",
        {"B": ["Mask does not delete source files.", "القناع لا يحذف الملفات الأصلية."], "C": ["Zero is a real numeric value that would skew averages; NoData is correctly assigned.", "الصفر قيمة عددية تشوه المتوسطات بينما NoData تمثل غياب البيانات."], "D": ["Vector conversion requires conversion tools.", "التحويل لمتجهات يتطلب أدوات تحويل مستقلة."]},
        "environments"
    ),
    # 39: ModelBuilder Intermediate Data
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Technical", ["ModelBuilder"],
        "Why should temporary intermediate scratch datasets in a long ModelBuilder workflow be flagged as 'Intermediate Data'?",
        "لماذا يجب تمييز مجموعات البيانات المؤقتة في مسار ModelBuilder الطويل بأنها 'Intermediate Data'؟",
        [["So ArcGIS Pro automatically purges the temporary datasets from disk once the entire model run finishes", "حتى يقوم ArcGIS Pro بحذف وتطهير هذه الملفات المؤقتة تلقائياً من القرص بمجرد اكتمال تشغيل النموذج"], ["To prevent the model from completing successfully", "لمنع النموذج من الاكتمال بنجاح"], ["To publish the temporary data directly to ArcGIS Online", "لنشر البيانات المؤقتة مباشرة إلى ArcGIS Online"], ["To convert vector files to raster format", "لتحويل الملفات الاتجاهية إلى راستر"]],
        "A",
        "Marking outputs as Intermediate ensures that temporary scratch files created by intervening tools are deleted automatically upon completion, saving disk space.",
        "يضمن تمييز المخرجات كوسيطة (Intermediate) قيام ArcGIS Pro بحذف الملفات المؤقتة الناتجة عن الأدوات البينية تلقائياً فور انتهاء التشغيل، مما يوفر مساحة التخزين.",
        {"B": ["Intermediate flags improve workflow hygiene and do not cause errors.", "البيانات الوسيطة تحسن تنظيم الملفات ولا تسبب أخطاء."], "C": ["Publishing requires explicit sharing tools.", "النشر يتطلب أدوات مشاركة صريحة."], "D": ["Conversion requires conversion tools.", "التحويل يتطلب أدوات تحويل."]},
        "modelbuilder"
    ),
    # 40: Viewshed analysis
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Viewshed"],
        "Which tool in Spatial Analyst determines which terrain raster cells can be seen from one or more observation point locations, taking observer elevation and surface topography into account?",
        "أي أداة في Spatial Analyst تحدد خلايا الراستر التضاريسية التي يمكن رؤيتها من نقطة رصد أو أكثر، آخذة بعين الاعتبار ارتفاع الراصد وتضاريس السطح؟",
        [["Viewshed", "Viewshed (مجال الرؤية)"], ["Slope", "Slope (الانحدار)"], ["Aspect", "Aspect (اتجاه الانحدار)"], ["Hillshade", "Hillshade (التظليل التضاريسي)"]],
        "A",
        "Viewshed identifies visible raster cells on an elevation surface from observer points or lines, factoring in observer height offsets (OFFSETA), target heights (OFFSETB), and view angles.",
        "تحدد أداة Viewshed الخلايا المرئية على سطح الارتفاع من نقاط أو خطوط المراقبة، مع مراعاة ارتفاع الراصد وارتفاع الهدف وزوايا الرؤية.",
        {"B": ["Slope measures rate of elevation change.", "يقيس الانحدار معدل التغير الرأسي."], "C": ["Aspect identifies downslope compass direction.", "يحدد Aspect الاتجاه البوصلي للانحدار."], "D": ["Hillshade calculates visual illumination shadows.", "يحسب Hillshade إضاءة وظلال التضاريس."]},
        "overlay"
    ),
    # 41: Slope tool output measurement
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Beginner", "Technical", ["Slope"],
        "What two measurement unit options are available for the output of the Slope geoprocessing tool?",
        "ما هما خيارا وحدات القياس المتاحان لمخرجات أداة التحليل Slope؟",
        [["Degree and Percent rise", "الدرجات (Degree) والنسبة المئوية (Percent rise)"], ["Meters and Feet", "الأمتار والأقدام"], ["Radians and Gradians", "الراديان والغراديان"], ["Acres and Hectares", "الأفدنة والهكتارات"]],
        "A",
        "The Slope tool outputs terrain steepness either as Degrees of slope (0° to 90°) or as Percent rise (0% to infinity).",
        "تُخرج أداة Slope درجة وعورة التضاريس إما بالدرجات الزاوية (Degree من 0 إلى 90) أو بالنسبة المئوية للميل (Percent rise من 0 إلى ما لا نهاية).",
        {"B": ["Meters and feet are linear elevation distance units.", "الأمتار والأقدام وحدات مسافة خطية."], "C": ["Radians are not standard output choices in the Slope tool.", "الراديان ليس خياراً متاحاً في الأداة."], "D": ["Acres and hectares are area measurements.", "الأفدنة والهكتارات وحدات مساحة."]},
        "overlay"
    ),
    # 42: Aspect tool
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Beginner", "Conceptual", ["Aspect"],
        "What does the Aspect tool calculate on a digital elevation model (DEM)?",
        "ماذا تحسب أداة Aspect على نموذج الارتفاع الرقمي (DEM)؟",
        [["The compass direction that the downhill slope face points (0° to 360°)", "الاتجاه البوصلي الذي يواجهه انحدار السطح نحو الأسفل (من 0 إلى 360 درجة)"], ["The depth of underground water tables", "عمق المياه الجوفية تحت الأرض"], ["The volume of cut and fill soil", "حجم الحفر والردم للتربة"], ["The atmospheric barometric pressure", "الضغط الجوي للغلاف الجوي"]],
        "A",
        "Aspect identifies the compass direction of the maximum rate of change in elevation from each cell to its neighbors (0° is North, 90° is East, 180° is South, 270° is West; flat areas evaluate to -1).",
        "تحسب أداة Aspect الاتجاه البوصلي لأقصى ميل للسطح نحو الأسفل (0 للشمال، 90 للشرق، 180 للجنوب، 270 للغرب؛ والمناطق المستوية تأخذ -1).",
        {"B": ["Aspect does not measure subsurface hydrology.", "لا تقيس المياه الجوفية."], "C": ["Cut and Fill tool calculates earthwork volumes.", "أداة Cut and Fill هي المسؤولة عن حجوم الحفر والردم."], "D": ["Aspect is purely geometric terrain orientation.", "أداة Aspect اتجاه تضاريسي صرف."]},
        "overlay"
    ),
    # 43: Contour tool
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Beginner", "Tool-based", ["Contour"],
        "Which tool creates a polyline feature class of elevation isolines connecting points of equal height from a continuous raster surface?",
        "أي أداة تنشئ فئة معالم خطية تمثل خطوط تساوي الارتفاع التي تربط النقاط ذات الارتفاع المتطابق من سطح راستر مستمر؟",
        [["Contour", "Contour (خطوط الكنتور)"], ["Slope", "Slope (الانحدار)"], ["Buffer", "Buffer (النطاق)"], ["Viewshed", "Viewshed (مجال الرؤية)"]],
        "A",
        "The Contour tool generates isolines (lines of equal elevation) from a raster surface grid based on a specified contour interval.",
        "تولد أداة Contour خطوط الكنتور (خطوط المناسيب المتساوية) من شبكة راستر بناءً على فاصل كنتوري محدد.",
        {"B": ["Slope measures angle steepness.", "يقيس الانحدار زاوية الميل."], "C": ["Buffer creates proximity zones.", "تنشئ Buffer مناطق حرم."], "D": ["Viewshed evaluates visibility.", "تحسب Viewshed مناطق الرؤية."]},
        "overlay"
    ),
    # 44: Split By Attributes
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Split By Attributes"],
        "An analyst needs to divide a nationwide counties feature class into separate individual feature classes for each state and save them into a geodatabase. Which tool performs this in one step?",
        "يحتاج محلل إلى تقسيم فئة معالم المقاطعات على مستوى الدولة إلى فئات معالم منفصلة لكل ولاية على حدة وحفظها في قاعدة بيانات. أي أداة تؤدي ذلك في خطوة واحدة؟",
        [["Split By Attributes", "Split By Attributes (تقسيم حسب السمات)"], ["Dissolve", "Dissolve (الدمج)"], ["Merge", "Merge (الجمع)"], ["Intersect", "Intersect (التقاطع)"]],
        "A",
        "Split By Attributes splits an input dataset into multiple individual feature classes based on unique values in one or more attribute fields.",
        "تقسم أداة Split By Attributes مجموعة بيانات الإدخال إلى عدة فئات معالم مستقلة بناءً على القيم الفريدة في حقل أو أكثر من حقول السمات.",
        {"B": ["Dissolve aggregates features into a single layer.", "تدمج Dissolve المعالم في طبقة واحدة."], "C": ["Merge combines multiple layers into one.", "تجمع Merge عدة طبقات في ملف واحد."], "D": ["Intersect computes overlay.", "تحسب Intersect التراكب المكاني."]},
        "overlay"
    ),
    # 45: Spatial Join Match Rules
    (
        "Compare table joins and relates, relationship classes, and spatial joins", "Intermediate", "Technical", ["Spatial Join"],
        "Which spatial match rule in the Spatial Join tool should be selected when joining parcel polygon attributes to building centroid points that fall entirely within them?",
        "أي قاعدة مطابقة مكانية في أداة Spatial Join يجب اختيارها عند ضم بيانات مضلعات الأراضي لنقاط مراكز المباني الواقعة بالكامل بداخلها؟",
        [["Completely contains (or Within)", "Completely contains (أو Within)"], ["Shares a line segment with", "Shares a line segment with (تشترك في قطعة خطية)"], ["Crosses outline of", "Crosses outline of (تقطع حدود)"], ["Are identical to", "Are identical to (تتطابق مع)"]],
        "A",
        "When points are enclosed within polygons, 'Within' (or 'Completely contains' depending on which is Target vs Join) establishes accurate interior spatial relationship.",
        "عندما تكون النقاط محاطة بمضلعات، فإن علاقة 'Within' أو 'Completely contains' (بحسب تحديد الهدف والمصدر) تحدد الاحتواء المكاني الداخلي بدقة.",
        {"B": ["Points have no line segments to share.", "النقاط ليس لها قطع خطية لتشترك فيها."], "C": ["Points cannot cross outlines.", "النقاط لا تقطع الحدود."], "D": ["Point and polygon geometries cannot be geometrically identical.", "النقاط والمضلعات تختلف في نوع الهندسة ولا يمكن أن تتطابق."]},
        "joins"
    ),
    # 46: Tabulate Intersection
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Tabulate Intersection"],
        "Which tool computes the exact area and percentage of overlap between two polygon layers (e.g. percentage of each school district covered by wetlands) and outputs the results in a cross-tabulated table?",
        "أي أداة تحسب المساحة الدقيقة ونسبة التداخل المئوية بين طبقتي مضلعات (مثل نسبة تغطية الأراضي الرطبة في كل منطقة تعليمية) وتُخرج النتائج في جدول متقاطع؟",
        [["Tabulate Intersection", "Tabulate Intersection"], ["Clip", "Clip"], ["Buffer", "Buffer"], ["Erase", "Erase"]],
        "A",
        "Tabulate Intersection cross-tabulates the intersection between two feature classes, calculating overlapping area, length, and percentage of the input area occupied.",
        "تحسب أداة Tabulate Intersection التداخل المتقاطع بين طبقتين، وتستخرج المساحة والطول ونسبة التداخل المئوية من مساحة معالم الإدخال.",
        {"B": ["Clip creates clipped features without cross-tabulation percentages.", "تقتطع Clip المعالم ولا تحسب نسب مئوية جدولية."], "C": ["Buffer creates distance rings.", "تنشئ Buffer مساحات حرم."], "D": ["Erase removes areas.", "تحذف Erase المساحات."]},
        "overlay"
    ),
    # 47: Cellular automata / Raster Resampling
    (
        "Apply raster functions for raster and image processing", "Intermediate", "Technical", ["Resample"],
        "When changing a raster's cell size from 30 meters to 10 meters using the Resample tool, does this operation increase the real spatial detail of the original sensor capture?",
        "عند تغيير حجم خلية الراستر من 30 متراً إلى 10 أمتار باستخدام أداة Resample، هل تؤدي هذه العملية إلى زيادة التفاصيل المكانية الحقيقية لالتقاط الحساس الأصلي؟",
        [["No, it divides existing pixels into smaller interpolated cells without adding new real-world spatial information", "لا، بل تقسم البكسلات القائمة إلى خلايا أصغر مستوفاة رياضياً دون إضافة أي معلومات مكانية حقيقية جديدة"], ["Yes, it increases satellite sensor resolution by 300%", "نعم، تزيد دقة الحساس الفضائي بنسبة 300%"], ["Yes, but only if run on a weekend", "نعم، ولكن فقط إذا شُغلت في عطلة نهاية الأسبوع"], ["It converts the raster to vector contours automatically", "تحول الراستر إلى خطوط كنتور تلقائياً"]],
        "A",
        "Downsampling or refining cell size divides cells mathematically (using nearest neighbor, bilinear, or cubic methods), but cannot recreate fine-grained spatial information not captured by the physical sensor.",
        "إن تصغير حجم الخلية يقسم البكسلات حسابياً عبر الاستيفاء الرياضي، لكنه لا يستطيع استحداث تفاصيل مكانية حقيقية لم يلتقطها الحساس الأصلي.",
        {"B": ["Software resampling cannot alter physical satellite optics.", "إعادة الاستعيان البرمجية لا تغير بصريات الأقمار الصناعية."], "C": ["Calendar timing is irrelevant to algorithms.", "التوقيت لا علاقة له بالخوارزميات."], "D": ["Resample preserves raster structure.", "تحافظ أداة Resample على بنية الراستر."]},
        "rasterfunc"
    ),
    # 48: Focal Statistics
    (
        "Apply raster functions for raster and image processing", "Intermediate", "Tool-based", ["Focal Statistics"],
        "Which Spatial Analyst tool calculates neighborhood statistics (e.g., Mean, Majority, Standard Deviation) for each raster cell based on the values within a specified roving moving window (such as a 3x3 rectangle)?",
        "أي أداة في Spatial Analyst تحسب إحصائيات الجوار (مثل المتوسط، الأغلبية، الانحراف المعياري) لكل خلية راستر بناءً على القيم الواقعة ضمن نافذة متحركة محددة (مثل مستطيل 3x3)؟",
        [["Focal Statistics", "Focal Statistics (إحصائيات الجوار البؤرية)"], ["Zonal Statistics", "Zonal Statistics (إحصائيات المناطق)"], ["Summary Statistics", "Summary Statistics (إحصائيات الملخص)"], ["Tabulate Area", "Tabulate Area (جدولة المساحة)"]],
        "A",
        "Focal Statistics calculates statistics for each input cell location based on values within a defined moving neighborhood around that cell (roving window smoothing or filtering).",
        "تحسب أداة Focal Statistics إحصائيات لكل خلية بناءً على قيم الخلايا المجاورة الواقعة ضمن نافذة متحركة محددة حولها (لتنعيم الأسطح أو ترشيح الشوائب).",
        {"B": ["Zonal Statistics uses fixed irregular zone boundaries, not a roving window.", "تستخدم إحصائيات المناطق حدوداً ثابتة وليس نافذة متحركة."], "C": ["Summary Statistics works on standalone tables.", "تعمل إحصائيات الملخص على الجداول."], "D": ["Tabulate Area cross-tabulates zone areas.", "تحسب Tabulate Area مساحات المناطق."]},
        "rasterfunc"
    ),
    # 49: Block Statistics vs Focal Statistics
    (
        "Apply raster functions for raster and image processing", "Advanced", "Conceptual", ["Focal Statistics"],
        "What is the difference between Focal Statistics and Block Statistics?",
        "ما هو الفرق بين إحصائيات الجوار البؤرية (Focal Statistics) وإحصائيات الكتل (Block Statistics)؟",
        [["Focal Statistics moves cell-by-cell in an overlapping roving window; Block Statistics processes mutually exclusive non-overlapping blocks", "تتحرك Focal Statistics خلية بخلية في نافذة متداخلة متحركة؛ بينما تعالج Block Statistics كُتلاً مستقلة غير متداخلة"], ["Focal Statistics only works on vector files", "تعمل Focal Statistics على الملفات الاتجاهية فقط"], ["Block Statistics is obsolete and removed from Pro", "أداة Block Statistics ملغاة من البرنامج"], ["Both tools produce mathematically identical surfaces", "تنتج كلتا الأداتين أسطحاً متطابقة رياضياً"]],
        "A",
        "Focal Statistics uses a sliding overlapping neighborhood centered on each cell, producing smooth continuous surfaces. Block Statistics divides the raster into distinct non-overlapping blocks, assigning the calculated statistic to all cells in that block.",
        "تستخدم Focal Statistics نافذة متحركة متداخلة متمحورة حول كل خلية فتنتج أسطحاً ناعمة؛ بينما تقسم Block Statistics الراستر إلى كتل مربعة منفصلة غير متداخلة وتعطي كل خلية في الكتلة نفس القيمة المحسوبة.",
        {"B": ["Both tools process raster grids.", "تعمل كلتا الأداتين على شبكات الراستر."], "C": ["Block statistics is an active core tool in ArcGIS Pro.", "أداة Block Statistics أداة قائمة ومعتمدة."], "D": ["Their outputs look fundamentally different (smooth continuous vs blocky mosaic).", "تختلف مخرجاتهما جوهرياً (سطح ناعم مقابل كتل مجزأة)."]},
        "rasterfunc"
    ),
    # 50: Fill tool (Hydrology)
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Fill"],
        "Before performing Flow Direction and Flow Accumulation modeling on a DEM, which tool should be run to eliminate small surface depressions and artificial pits?",
        "قبل إجراء نمذجة اتجاه الجريان وتراكم الجريان السطحي على نموذج الارتفاع DEM، أي أداة يجب تشغيلها لإزالة المنخفضات السطحية الصغيرة والبرك الاصطناعية؟",
        [["Fill", "Fill (ملء المنخفضات)"], ["Sink", "Sink (تحديد المصارف)"], ["Flow Length", "Flow Length (طول الجريان)"], ["Basin", "Basin (حوض التصريف)"]],
        "A",
        "The Fill tool fills sinks and depressions in an elevation raster to remove imperfect pits where water would get trapped, creating a continuous hydrologically correct surface.",
        "تملأ أداة Fill المنخفضات والبرك غير المنفذة في راستر الارتفاع لمنع احتباس تدفق المياه الافتراضي، مما ينتج سطحاً هيدرولوجياً متصلاً وسليماً.",
        {"B": ["Sink identifies depressions but does not fill them.", "تحدد أداة Sink المنخفضات ولكنها لا تسويها."], "C": ["Flow Length measures upstream or downstream flow path distance.", "تقيس Flow Length مسافة مسار الجريان."], "D": ["Basin delineates drainage basins.", "تحدد Basin أحواض التصريف المائي."]},
        "overlay"
    ),
    # 51: Flow Direction
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Technical", ["Flow Direction"],
        "In ArcGIS Pro hydrological modeling using the D8 flow method, how many discrete flow directions are modeled from each cell to its steepest downslope neighbor?",
        "في النمذجة الهيدرولوجية بـ ArcGIS Pro باستخدام طريقة D8، كم عدد اتجاهات الجريان المنفصلة التي يتم نمذجتها من كل خلية إلى الخلية المجاورة الأكثر انحداراً؟",
        [["8 valid directional codes (1, 2, 4, 8, 16, 32, 64, 128)", "8 أكواد اتجاهية صالحة (1، 2، 4، 8، 16، 32، 64، 128)"], ["360 continuous degrees", "360 درجة مستمرة"], ["4 cardinal directions only", "4 اتجاهات رئيسية فقط"], ["Unlimited directions based on wind speed", "اتجاهات غير محدودة بناءً على سرعة الرياح"]],
        "A",
        "The D8 algorithm models water flowing from each cell to one of its eight neighboring cells, encoding directions as powers of two (East=1, SE=2, South=4, SW=8, West=16, NW=32, North=64, NE=128).",
        "تنمذج خوارزمية D8 تدفق المياه من كل خلية نحو إحدى الخلايا الثماني المجاورة لها، مستخدمة قوى الرقم 2 لترميز الاتجاهات (الشرق=1، الجنوب الشرقي=2، الجنوب=4، ... والشمال الشرقي=128).",
        {"B": ["D8 uses 8 discrete integer codes, not continuous floating-point angles.", "تستخدم D8 أكواداً صحيحة منفصلة وليس زوايا كسرية."], "C": ["D8 includes 4 cardinal and 4 diagonal directions (8 total).", "تشمل D8 الاتجاهات الأربعة الرئيسية والأربعة الفرعية."], "D": ["Surface hydrology is driven by gravity and topography, not wind.", "تعتمد الهيدرولوجيا على التضاريس والجاذبية وليس الرياح."]},
        "overlay"
    ),
    # 52: Flow Accumulation
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Conceptual", ["Flow Accumulation"],
        "What does a high cell value in a Flow Accumulation raster represent?",
        "ماذا تمثل القيمة العالية للخلية في راستر تراكم الجريان (Flow Accumulation)؟",
        [["A high number of upstream cells drain through that cell, indicating a stream channel or concentrated drainage path", "تصريف عدد كبير من الخلايا العليا عبر هذه الخلية، مما يشير إلى وجود مجرى مائي أو مسار تصريف رئيسي"], ["An area of extreme high elevation on a mountain peak", "منطقة ذات منسوب ارتفاع شاهق على قمة جبل"], ["An area where rain never falls", "منطقة لا تسقط عليها الأمطار إطلاقاً"], ["A cell with high vegetation canopy density", "خلية ذات كثافة غطاء نباتي مرتفعة"]],
        "A",
        "Flow Accumulation calculates accumulated flow as the accumulated weight of all upstream cells flowing into each downslope cell. Cells with high accumulation identify concentrated stream channels and rivers.",
        "تحسب Flow Accumulation التدفق التراكمي كوزن مجمع لكافة الخلايا العليا المتدفقة نحو كل خلية؛ وتشير القيم المرتفعة إلى مجاري الأودية ومسارات الأنهار المركزة.",
        {"B": ["Mountain peaks have an accumulation of 0 because no cells drain into them.", "قمم الجبال تأخذ قيمة تراكم 0 لعدم وجود خلايا تصب فيها."], "C": ["Accumulation models terrain drainage, not weather rainfall absence.", "النموذج يمثل تضاريس التصريف وليس الجفاف."], "D": ["Vegetation canopy is measured by NDVI, not Flow Accumulation.", "الغطاء النباتي يقاس بـ NDVI."]},
        "overlay"
    ),
    # 53: Aggregate Points tool
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Aggregate Points"],
        "Which cartographic geoprocessing tool aggregates clusters of point features into polygon shapes based on a specified clustering distance?",
        "أي أداة معالجة كارتوغرافية تجمع كتل المعالم النقطية المتقاربة في أشكال مضلعات بناءً على مسافة تجميع محددة؟",
        [["Aggregate Points", "Aggregate Points (تجميع النقاط)"], ["Buffer", "Buffer (النطاق)"], ["Spatial Join", "Spatial Join (الضم المكاني)"], ["Dissolve", "Dissolve (الدمج)"]],
        "A",
        "Aggregate Points creates polygons representing clusters of proximate points within a specified distance threshold.",
        "تنشئ أداة Aggregate Points مضلعات تعبر عن تجمعات النقاط المتقاربة ضمن مسافة محددة.",
        {"B": ["Buffer creates circular zones around individual points.", "تنشئ Buffer دوائر حول النقاط."], "C": ["Spatial Join attaches attributes.", "يربط Spatial Join السمات."], "D": ["Dissolve operates on existing polygons/lines with common attributes.", "تدمج Dissolve معالم قائمة تشترك في السمات."]},
        "overlay"
    ),
    # 54: Calculate Field with Arcade
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Technical", ["Calculate Field"],
        "In the Calculate Field tool, which expression language is the modern default and recommended standard for cross-platform ArcGIS field calculations?",
        "في أداة Calculate Field، ما هي لغة التعبير التي تُعد الخيار الافتراضي الحديث والمعيار الموصى به لحسابات الحقول عبر منصات ArcGIS؟",
        [["Arcade", "Arcade"], ["VBScript", "VBScript"], ["Fortran", "Fortran"], ["COBOL", "COBOL"]],
        "A",
        "Arcade is Esri's lightweight, secure expression language designed specifically for use across all ArcGIS platforms (Pro, Online, Enterprise, Field Maps). Python 3 is also supported for advanced desktop automation.",
        "تعد Arcade لغة التعبيرات الآمنة والخفيفة من Esri المصممة للعمل عبر كافة منصات ArcGIS (المكتبي، السحابي، المؤسسي، والميداني).",
        {"B": ["VBScript is deprecated and only supported in legacy 32-bit ArcMap.", "لغة VBScript مهملة ومدعومة في ArcMap القديم فقط."], "C": ["Fortran is not a GIS expression language.", "ليست لغة تعبيرات جغرافية."], "D": ["COBOL is a legacy business language.", "لغة تجارية قديمة لا علاقة لها بنظم المعلومات الجغرافية."]},
        "joins"
    ),
    # 55: Feature to Point tool
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Beginner", "Tool-based", ["Feature To Point"],
        "An analyst needs to generate a point feature class where each point represents the geographic center of a parcel polygon. Which tool should be used, and what option ensures the point falls strictly inside irregular C-shaped parcels?",
        "يحتاج محلل لتوليد فئة معالم نقطية تمثل المراكز الجغرافية لمضلعات الأراضي. أي أداة يجب استخدامها، وما الخيار الذي يضمن وقوع النقطة داخل المضلعات غير المنتظمة (كالمضلعات على شكل حرف C)؟",
        [["Feature To Point with 'Inside' parameter checked", "أداة Feature To Point مع تفعيل خيار 'Inside'"], ["Buffer with negative distance", "أداة Buffer بمسافة سالبة"], ["Add Join on centroid field", "أمر Add Join على حقل المركز"], ["XY Table To Point", "أداة XY Table To Point"]],
        "A",
        "Feature To Point creates centroids. When 'Inside' is checked, it guarantees the generated point falls strictly inside the polygon boundary rather than at the mathematical center outside a concave or donut shape.",
        "تولد أداة Feature To Point مراكز المعالم؛ ويضمن تفعيل خيار 'Inside' وقوع النقطة حتماً داخل حدود المضلع، متجنباً وقوعها خارج المضلعات الهلالية أو ذات الفجوات.",
        {"B": ["Negative buffer shrinks polygons but does not output point feature classes.", "الحرم السالب يقلص المضلع ولا يُخرج طبقة نقاط."], "C": ["Add Join joins attributes.", "يربط Add Join الجداول."], "D": ["XY Table to Point reads X/Y table coordinates.", "تسقط XY Table to Point النقاط من إحداثيات الجدول."]},
        "overlay"
    ),
    # 56: Point Distance tool
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Point Distance"],
        "Which tool computes point-to-point distances between every point in an input layer and every point in a near layer, outputting a complete matrix table of all distances?",
        "أي أداة تحسب المسافات من نقطة إلى نقطة بين كل نقطة في طبقة الإدخال وكل نقطة في طبقة الهدف، وتُخرج مصفوفة جدولية كاملة لجميع المسافات؟",
        [["Point Distance", "Point Distance"], ["Clip", "Clip"], ["Dissolve", "Dissolve"], ["Union", "Union"]],
        "A",
        "Point Distance computes the distance from each point in the input features to all points in the near features within a specified search radius, outputting a table with INPUT_FID, NEAR_FID, and DISTANCE.",
        "تحسب أداة Point Distance المسافة من كل نقطة مدخلة إلى كافة نقاط طبقة المقارنة ضمن مسافة بحث محددة، وتُخرج جدولاً يحتوي على معرفات النقاط والمسافة المحسوبة بين كل زوج.",
        {"B": ["Clip cuts features.", "تقص Clip المعالم."], "C": ["Dissolve aggregates geometries.", "تدمج Dissolve الأشكال."], "D": ["Union overlays polygons.", "تجري Union تراكباً للمضلعات."]},
        "proximity"
    ),
    # 57: Appending features
    (
        "Compare table joins and relates, relationship classes, and spatial joins", "Beginner", "Tool-based", ["Append"],
        "An analyst has field survey points collected today in a shapefile and needs to append them directly into an existing enterprise geodatabase feature class schema. Which tool should be used?",
        "لدى محلل نقاط مسح ميداني جُمعت اليوم في ملف shapefile ويحتاج لإضافتها مباشرة إلى فئة معالم قائمة في قاعدة بيانات مؤسسية. أي أداة يجب استخدامها؟",
        [["Append", "Append (إلحاق السجلات)"], ["Spatial Join", "Spatial Join"], ["Intersect", "Intersect"], ["Create Feature Class", "Create Feature Class"]],
        "A",
        "Append inserts features and records from one or more input datasets into an existing target dataset, with field mapping capabilities (TEST or NO_TEST schema matching).",
        "تضيف أداة Append المعالم والسجلات من طبقة أو أكثر إلى طبقة هدف قائمة بالفعل، مع دعم مطابقة الحقول (بخياري TEST أو NO_TEST).",
        {"B": ["Spatial Join creates a new file.", "ينشئ Spatial Join ملفاً جديداً."], "C": ["Intersect calculates geometric intersections.", "تحسب Intersect التقاطع الهندسي."], "D": ["Create Feature Class creates an empty schema.", "تنشئ Create Feature Class مخططاً فارغاً."]},
        "joins"
    ),
    # 58: Merge geoprocessing vs Append
    (
        "Compare table joins and relates, relationship classes, and spatial joins", "Intermediate", "Conceptual", ["Merge", "Append"],
        "What is the key operational difference between the Merge geoprocessing tool and the Append geoprocessing tool?",
        "ما هو الفرق التشغيلي الأساسي بين أداة Merge وأداة Append في المعالجة الجغرافية؟",
        [["Merge creates an entirely new output dataset; Append loads features into an already existing target dataset", "تنشئ أداة Merge ملف مخرجات جديد بالكامل؛ بينما تقوم أداة Append بتحميل وإضافة المعالم إلى طبقة هدف موجودة مسبقاً"], ["Merge only works on raster files; Append works on vector files", "تعمل Merge على الراستر فقط بينما Append على المتجهات"], ["Append deletes all original records in the target layer before writing", "تحذف أداة Append جميع السجلات الأصلية في الطبقة الهدف قبل الإضافة"], ["Both tools perform identical operations and exist only for backwards compatibility", "تؤدي كلتا الأداتين نفس العملية تماماً ووجودهما للتوافق مع الإصدارات القديمة فقط"]],
        "A",
        "Merge combines multiple input feature classes or tables into a brand new output dataset. Append adds rows directly into an existing target dataset without creating a new file.",
        "تجمع أداة Merge عدة فئات معالم أو جداول في ملف مخرجات جديد كلياً. بينما تضيف أداة Append الصفوف والمعالم مباشرة داخل طبقة هدف قائمة دون إنشاء ملف جديد.",
        {"B": ["Both tools are vector feature and tabular tools.", "كلتا الأداتين مخصصتان للبيانات الاتجاهية والجداول."], "C": ["Append preserves existing target records and appends new ones to the bottom.", "تحافظ أداة Append على السجلات القائمة وتضيف السجلات الجديدة إليها."], "D": ["They serve fundamentally different workflow roles (new file creation vs loading into existing schema).", "تختلفان وظيفياً (إنشاء ملف جديد مقابل تحميل بيانات في هيكل قائم)."]},
        "joins"
    ),
    # 59: Select Layer By Location invert
    (
        "Given a scenario, apply a query", "Intermediate", "Tool-based", ["Select Layer By Location"],
        "How can an analyst select all water wells that do NOT fall within a 500-meter contamination buffer zone using Select Layer By Location?",
        "كيف يمكن للمحلل تحديد كافة آبار المياه التي لا تقع ضمن نطاق التلوث البالغ 500 متر باستخدام أداة Select Layer By Location؟",
        [["Configure the spatial relationship to 'Within a distance' of 500 meters and check the 'Invert Spatial Relationship' box", "ضبط العلاقة المكانية على 'Within a distance' بمسافة 500 متر مع تفعيل خيار 'Invert Spatial Relationship'"], ["Delete the contamination buffer layer", "حذف طبقة حرم التلوث"], ["Change the wells symbology to red", "تغيير رموز الآبار إلى اللون الأحمر"], ["Export the wells to an Excel spreadsheet", "تصدير الآبار إلى جدول إكسل"]],
        "A",
        "Checking 'Invert Spatial Relationship' selects features that do NOT satisfy the specified spatial relationship, cleanly selecting all points situated outside the buffer.",
        "يؤدي تفعيل خيار 'Invert Spatial Relationship' إلى عكس نتيجة التحديد المكاني واختيار المعالم التي لا ينطبق عليها الشرط، مما يحدد كافة الآبار الواقعة خارج النطاق.",
        {"B": ["Deleting data loses spatial reference.", "حذف البيانات يفقد المرجع المكاني."], "C": ["Symbology is visual.", "الرموز للعرض البصري."], "D": ["Excel does not evaluate spatial proximity inversion.", "إكسل لا يعكس العلاقات المكانية."]},
        "joins"
    ),
    # 60: Polygon to Raster conversion
    (
        "Apply raster functions for raster and image processing", "Beginner", "Tool-based", ["Polygon to Raster"],
        "When using Polygon to Raster to convert land use polygons into a grid, which parameter dictates which attribute code is assigned to cells that overlap two different land use polygons?",
        "عند استخدام أداة Polygon to Raster لتحويل مضلعات استخدامات الأراضي إلى شبكة، أي معامل يحدد كود السمة الذي يُعطى للخلايا التي تتداخل مع مضلعي استخدام مختلفين؟",
        [["Cell assignment type (e.g. CELL_CENTER, MAXIMUM_AREA, MAXIMUM_COMBINED_AREA)", "نوع تخصيص الخلية (مثل CELL_CENTER، MAXIMUM_AREA، MAXIMUM_COMBINED_AREA)"], ["Output Coordinate System", "نظام الإحداثيات المخرج"], ["Geographic Transformation", "التحويل الجغرافي"], ["Spatial Reference Tolerance", "تسامح المرجع المكاني"]],
        "A",
        "The Cell Assignment Type parameter controls how the value of a cell is determined when more than one feature overlaps it (e.g., assigning based on which polygon covers the cell center or covers the largest surface area).",
        "يتحكم معامل Cell Assignment Type في كيفية تحديد قيمة الخلية عند اشتراك أكثر من معلم في تغطيتها (مثل تخصيص القيمة بناءً على المضلع الذي يغطي مركز الخلية أو يغطي المساحة الأكبر).",
        {"B": ["Coordinate system defines spatial reference, not cell assignment.", "نظام الإحداثيات يحدد الإسقاط."], "C": ["Datum transformation handles shifts.", "التحويل الجغرافي يعالج المراجع."], "D": ["Tolerance controls vertex snapping.", "التسامح يتحكم في الانجذاب."]},
        "rasterfunc"
    ),
    # 61: Multiple Ring Buffer
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Beginner", "Tool-based", ["Multiple Ring Buffer"],
        "Which tool creates a series of concentric buffer rings at multiple specified distances (e.g., 100m, 200m, and 500m) around a central fire station in a single execution?",
        "أي أداة تنشئ سلسلة من حلقات الحرم متحدة المركز بمسافات متعددة محددة (مثل 100م و 200م و 500م) حول مركز إطفاء في عملية تشغيل واحدة؟",
        [["Multiple Ring Buffer", "Multiple Ring Buffer (نطاقات الحلقات المتعددة)"], ["Buffer", "Buffer (النطاق البسيط)"], ["Clip", "Clip (القص)"], ["Near", "Near (الأقرب)"]],
        "A",
        "Multiple Ring Buffer creates multiple concentric buffer polygons at user-specified distance intervals around input features in one step.",
        "تنشئ أداة Multiple Ring Buffer عدة حلقات حرم متحدة المركز بمسافات يحددها المستخدم حول معالم الإدخال في خطوة واحدة.",
        {"B": ["Standard Buffer only supports a single distance parameter per execution.", "أداة Buffer القياسية تدعم مسافة واحدة فقط في كل تشغيل."], "C": ["Clip cuts boundaries.", "تقص Clip الحدود."], "D": ["Near calculates distances to points.", "تحسب Near المسافات للنقاط."]},
        "proximity"
    ),
    # 62: Spatial Analyst Con tool
    (
        "Apply raster functions for raster and image processing", "Intermediate", "Tool-based", ["Con"],
        "Which Spatial Analyst conditional tool performs an if/else conditional evaluation on raster cells, outputting one value if a condition is true and an alternative value if false?",
        "أي أداة شرطية في Spatial Analyst تجري تقييماً شرطياً (if/else) على خلايا الراستر، بحيث تُخرج قيمة معينة إذا تحقق الشرط وقيمة بديلة إذا لم يتحقق؟",
        [["Con", "Con (الأداة الشرطية)"], ["Set Null", "Set Null"], ["Pick", "Pick"], ["Test", "Test"]],
        "A",
        "The Con (Conditional) tool evaluates an input conditional raster expression and returns values from the 'true' raster/constant if true, or the 'false' raster/constant if false.",
        "تقوم أداة Con (الشرطية) بتقييم تعبير شرطي على الراستر وتُعيد قيمة مخصصة إذا كان الشرط صحيحاً (True)، أو قيمة بديلة إذا كان خاطئاً (False).",
        {"B": ["Set Null converts matching cells to NoData.", "تحول Set Null الخلايا المطابقة إلى NoData."], "C": ["Pick selects values from a list of rasters based on an index.", "تختار Pick قيماً من قائمة راستر."], "D": ["Test evaluates boolean true/false returning 1/0 only.", "ترجع Test القيمة 1 أو 0 فقط."]},
        "rasterfunc"
    )
]

for i, t in enumerate(more_agp):
    qid = f"AGP-{i+28:03d}"
    questions.append(make_q(qid, t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7], t[8], t[9], t[10], t[11]))

print(f"Total Analysis & Geoprocessing MCQs built: {len(questions)} (expected 62)")

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Saved analysis-geoprocessing.json successfully.")

