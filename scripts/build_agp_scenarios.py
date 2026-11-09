# -*- coding: utf-8 -*-
"""
Generate all 37 Analysis and Geoprocessing Scenarios (AGP-S-001 through AGP-S-037) for EAPA_2025.
"""
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_file = os.path.join(base_dir, 'public', 'data', 'scenarios', 'analysis-geoprocessing.json')

ref_map = {
    "env": {"title": "Geoprocessing environment settings, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/analysis/geoprocessing/basics/geoprocessing-environment-settings.htm", "kind": "official"},
    "model": {"title": "What is ModelBuilder?, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/analysis/modelbuilder/what-is-modelbuilder.htm", "kind": "official"},
    "raster": {"title": "What are raster functions?, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/analysis/raster-functions/what-are-raster-functions.htm", "kind": "official"},
    "surface": {"title": "An overview of the Surface toolset, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/an-overview-of-the-surface-tools.htm", "kind": "official"},
    "overlay": {"title": "An overview of the Overlay toolset, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/an-overview-of-the-overlay-toolset.htm", "kind": "official"},
    "proximity": {"title": "An overview of the Proximity toolset, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/an-overview-of-the-proximity-toolset.htm", "kind": "official"},
    "spatial_stats": {"title": "Spatial Statistics toolbox overview, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/an-overview-of-the-spatial-statistics-toolbox.htm", "kind": "official"},
    "network": {"title": "What is the ArcGIS Network Analyst extension?, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/analysis/networks/what-is-network-analyst.htm", "kind": "official"},
    "arcpy": {"title": "What is ArcPy?, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm", "kind": "official"},
    "tasks": {"title": "What is a task?, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/analysis/tasks/what-is-a-task.htm", "kind": "official"}
}

def s(sid, obj, diff, qtype, tools, ctx_en, ctx_ar, q_en, q_ar, opts, ans, exp_en, exp_ar, why, rkey):
    return {
        "id": sid,
        "kind": "scenario",
        "domain": "Analysis and Geoprocessing",
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
    # 1: Geoprocessing Environment Precedence
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Technical", ["Geoprocessing Environments"],
        "An analyst configures an application-level Cell Size environment of 30 meters under Analysis > Environments. However, when opening the Slope tool, the analyst navigates to the tool's individual Environments tab and enters a Cell Size of 10 meters.",
        "قام محلل بضبط بيئة حجم الخلية (Cell Size) على مستوى التطبيق بقيمة 30 متراً عبر Analysis > Environments؛ ولكن عند فتح أداة Slope، انتقل إلى تبويب البيئات الخاص بالأداة وأدخل حجم خلية 10 أمتار.",
        "What will be the cell resolution of the resulting output slope raster dataset?",
        "ما هي دقة الخلية الناتجة لراستر الانحدار الناتج من هذه العملية؟",
        [["10 meters, because tool-level environment settings override application-level environments", "10 أمتار، لأن إعدادات البيئة على مستوى الأداة تلغي وتهيمن على إعدادات بيئة التطبيق العامة"], ["30 meters, because application-level settings take universal precedence", "30 متراً، لأن إعدادات التطبيق تأخذ أولوية عليا مطلقة"], ["20 meters, because ArcGIS Pro calculates the mathematical average of conflicting settings", "20 متراً، لأن البرنامج يحسب المتوسط الرياضي للإعدادات المتضاربة"], ["The tool execution will fail with an environment conflict error", "ستفشل الأداة في التنفيذ بسبب خطأ تضارب في البيئات"]],
        "A",
        "Geoprocessing environments follow a strict hierarchy: Tool parameters > Tool-level environments > Model/Script environments > Application-level environments. The tool-level setting (10m) overrides the project setting (30m).",
        "تتبع بيئات المعالجة الجغرافية تسلسلاً هرمياً صارماً: معاملات الأداة > بيئات مستوى الأداة > بيئات النموذج/السكربت > بيئات التطبيق العامة. وبناءً عليه يلغي إعداد الأداة (10م) إعداد المشروع (30م).",
        {"B": ["Application settings have lower precedence than tool-level environments.", "إعدادات التطبيق ذات أولوية أدنى من إعدادات الأداة."], "C": ["ArcGIS Pro never averages differing environment settings.", "لا يحسب البرنامج متوسطات للبيئات المتعارضة."], "D": ["Overriding settings is normal expected behavior, not an error.", "تجاوز الإعدادات سلوك نظامي طبيعي وليس خطأ برمجياً."]},
        "env"
    ),

    # 2: Snap Raster Half-Cell Registration Shift
    (
        "Apply raster functions for raster and image processing", "Intermediate", "Troubleshooting", ["Snap Raster", "Raster Calculator"],
        "A spatial analyst combines a 10m land cover raster and a 10m slope raster in Raster Calculator. Upon inspecting the result, the output raster cells do not align with either input grid, displaying an offset of 3.2 meters and causing resampling artifacts.",
        "دمج محلل مكاني راستر غطاء أرضي بدقة 10م وراستر انحدار بدقة 10م باستخدام Raster Calculator؛ وعند فحص النتيجة، وجد أن خلايا الراستر الناتج غير محاذاة لشبكتي المدخلات مع وجود إزاحة 3.2 متر وتشوهات في إعادة أخذ العينات.",
        "Which geoprocessing environment setting should have been configured to prevent this grid registration shift?",
        "ما هو إعداد بيئة المعالجة الجغرافية الذي كان يجب ضبطه لمنع إزاحة محاذاة شبكة الخلايا؟",
        [["Snap Raster set to the master land cover raster", "ضبط بيئة الراستر المرجعي للمحاذاة (Snap Raster) على راستر الغطاء الأرضي الرئيسي"], ["Processing Extent set to Union of Inputs", "ضبط نطاق المعالجة Processing Extent على اتحاد المدخلات"], ["Mask set to the county boundary polygon", "ضبط بيئة القناع Mask على مضلع حدود المقاطعة"], ["Cell Size set to Maximum of Inputs", "ضبط حجم الخلية Cell Size على أقصى حجم للمدخلات"]],
        "A",
        "The Snap Raster environment aligns the cell corners and origin of the output raster precisely with an existing reference raster grid, preventing unwanted fractional-cell offsets.",
        "تعمل بيئة الراستر المرجعي (Snap Raster) على محاذاة زوايا الخلايا ونقطة الأصل للراستر الناتج بدقة متناهية مع شبكة راستر مرجعية موجودة، مما يمنع إزاحة أجزاء الخلايا.",
        {"B": ["Processing Extent defines the bounding box coordinates, not cell corner registration.", "يحدد Processing Extent الحدود الخارجية ولا يحاذي زوايا الخلايا."], "C": ["Mask limits analysis to within a boundary, ignoring cell grid alignment.", "يقيد القناع التحليل داخل حدود معينة دون محاذاة الشبكة."], "D": ["Cell Size sets cell dimensions, not its origin coordinates.", "يحدد Cell Size أبعاد الخلية وليس إحداثيات بدايتها."]},
        "env"
    ),

    # 3: ModelBuilder Inline Variable Substitution
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Tool-based", ["ModelBuilder"],
        "A GIS specialist designs a ModelBuilder model with an Iterate Feature Classes iterator to process 40 municipal zoning shapefiles. The model buffers each zone and exports it into a project File Geodatabase.",
        "صمم أخصائي نظم معلومات نموذجاً في ModelBuilder يحتوي على مكرر Iterate Feature Classes لمعالجة 40 ملف shapefile لمناطق التخطيط؛ ويقوم النموذج بعمل نطاق عازل وتصدير كل منطقة لقاعدة بيانات المشروع.",
        "How should the output path in the Buffer tool be specified to name each output feature class after its source file dynamically?",
        "كيف يجب كتابة مسار الإخراج في أداة Buffer لتسمية كل فئة معالم ناتجة باسم ملف المصدر ديناميكياً؟",
        [["%workspace%/Buffer_%Name%", "%workspace%/Buffer_%Name%"], ["%workspace%/Buffer_!Name!", "%workspace%/Buffer_!Name!"], ["%workspace%/Buffer_[Name]", "%workspace%/Buffer_[Name]"], ["%workspace%/Buffer_{Name}", "%workspace%/Buffer_{Name}"]],
        "A",
        "ModelBuilder uses percent signs (%VariableName%) for inline variable substitution. The Iterate Feature Classes tool generates a system variable named Name, which is referenced as %Name%.",
        "يستخدم ModelBuilder علامتي النسبة المئوية (%VariableName%) للاستبدال الضمني للمتغيرات؛ وتولد أداة التكرار متغيراً باسم Name يتم استدعاؤه كـ %Name%.",
        {"B": ["Exclamation marks (!Field!) are used in Calculate Field expressions, not ModelBuilder paths.", "تُستخدم علامات التعجب في حساب الحقول وليس مسارات النماذج."], "C": ["Square brackets are used in SQL queries.", "تُستخدم الأقواس المربعة في استعلامات SQL."], "D": ["Curly braces are used in Python string formatting.", "تُستخدم الأقواس المتعرجة في تنسيق نصوص بايثون."]},
        "model"
    ),

    # 4: ModelBuilder Model Parameter 'P' Badge
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Beginner", "Conceptual", ["ModelBuilder"],
        "An analyst builds a ModelBuilder tool to automate stormwater catchment delineation. When colleagues run the model from the Catalog pane by double-clicking it, no dialog box opens to allow them to select their own input DEM or stream network.",
        "بنى محلل نموذجاً في ModelBuilder لأتمتة تحديد أحواض تصريف مياه الأمطار؛ وعندما حاول زملاؤه تشغيل النموذج من نافذة الكتالوج بالنقر المزدوج، لم تظهر أي نافذة لإدخال راستر الارتفاع الرقمي أو شبكة المجاري الخاصة بهم.",
        "What configuration must the author perform in ModelBuilder to expose input variables as parameters in the tool dialog?",
        "ما الإجراء الذي يجب على مصمم النموذج تنفيذه في ModelBuilder لإظهار متغيرات الإدخال كمعاملات في نافذة الأداة؟",
        [["Right-click the input variable ovals and check 'Model Parameter' so the letter 'P' appears", "النقر بالزر الأيمن على أشكال المتغيرات البيضاوية وتفعيل خيار 'Model Parameter' حتى يظهر حرف 'P'"], ["Export the model to a Python script file", "تصدير النموذج إلى ملف سكربت بايثون"], ["Rename the model elements to uppercase letters", "إعادة تسمية عناصر النموذج بأحرف كبيرة"], ["Check 'Add To Display' on all tool elements", "تفعيل خيار Add To Display على جميع عناصر الأدوات"]],
        "A",
        "Marking a variable as a 'Model Parameter' exposes it in the tool dialog box when executed from the Catalog or Geoprocessing pane, represented by a 'P' badge on the model element.",
        "يؤدي تعليم المتغير كـ 'Model Parameter' إلى إظهاره كمعامل إدخال في نافذة تشغيل الأداة من نافذة الكتالوج أو المعالجة، ويُميز بشارة الحرف 'P' بجوار العنصر في النموذج.",
        {"B": ["Exporting to Python loses the visual ModelBuilder interface.", "التصدير لبايثون يفقد واجهة النموذج البصرية."], "C": ["Uppercase letters do not alter parameter exposure.", "تغيير حالة الأحرف لا يظهر المعاملات."], "D": ["Add To Display adds outputs to map views upon completion.", "إضافة للعرض تعرض الطبقات بعد انتهاء التشغيل فقط."]},
        "model"
    ),

    # 5: ModelBuilder Intermediate Data Cleanup
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Tool-based", ["ModelBuilder"],
        "A complex ModelBuilder workflow generates eight intermediate scratch feature classes during spatial intersections, buffers, and dissolves before creating the final deliverable polygon layer.",
        "ينتج نموذج ModelBuilder معقد ثماني طبقات مؤقتة أثناء عمليات التقاطع والنطاق والدمج قبل إنشاء طبقة المضلعات النهائية المطلوبة للتسليم.",
        "How can the analyst configure the model so that these temporary scratch datasets are deleted automatically from disk upon model completion?",
        "كيف يمكن للمحلل ضبط النموذج بحيث يتم حذف هذه البيانات المؤقتة تلقائياً من القرص الصلب فور اكتمال تشغيل النموذج؟",
        [["Right-click each temporary output variable oval and ensure 'Intermediate' is checked", "النقر بالزر الأيمن على كل متغير إخراج مؤقت والتأكد من تفعيل خيار 'Intermediate'"], ["Write a separate Python script to delete each layer manually", "كتابة سكربت بايثون منفصل لحذف كل طبقة يدوياً"], ["Store all intermediate data on an external USB flash drive", "تخزين البيانات المؤقتة على ذاكرة فلاش خارجية"], ["Set the layer transparency of intermediate variables to 100%", "ضبط شفافية المتغيرات المؤقتة على 100%"]],
        "A",
        "Flagging output variables as 'Intermediate' instructs ArcGIS Pro to automatically delete those temporary datasets from the scratch geodatabase once the model finishes executing.",
        "يؤدي تعليم متغيرات الإخراج كـ 'Intermediate' إلى توجيه ArcGIS Pro لحذف تلك البيانات المؤقتة تلقائياً من قاعدة البيانات المؤقتة فور انتهاء تشغيل النموذج.",
        {"B": ["Writing manual deletion scripts is redundant when ModelBuilder handles it natively.", "كتابة سكربتات حذف يدوي إجراء مكرر وغير ضروري."], "C": ["USB drives do not automatically delete temporary files.", "وسائط التخزين الخارجية لا تحذف الملفات تلقائياً."], "D": ["Transparency affects cartographic display, not disk storage.", "الشفافية للعرض فقط ولا تحذف ملفات القرص."]},
        "model"
    ),

    # 6: ModelBuilder Preconditions
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Tool-based", ["ModelBuilder"],
        "In a ModelBuilder model, Tool B must not begin processing until Tool A has completely finished updating and compressing an enterprise feature class. However, Tool B does not use the output of Tool A as direct input data.",
        "في نموذج ModelBuilder، يجب ألا تبدأ الأداة (ب) في المعالجة إلا بعد اكتمال قيام الأداة (أ) بتحديث وضغط فئة معالم مؤسسية بالكامل؛ مع العلم أن الأداة (ب) لا تستخدم مخرجات الأداة (أ) كبيانات إدخال مباشرة.",
        "How should the analyst establish this execution sequence requirement in ModelBuilder?",
        "كيف يجب على المحلل ربط وتحديد شرط تسلسل التنفيذ هذا في ModelBuilder؟",
        [["Connect the output of Tool A to Tool B and designate it as a 'Precondition' (dashed connector line)", "توصيل مخرج الأداة (أ) بالأداة (ب) وتعيينه كشرط مسبق 'Precondition' (خط ربط متقطع)"], ["Run Tool A on Monday and Tool B on Tuesday", "تشغيل الأداة (أ) يوم الاثنين والأداة (ب) يوم الثلاثاء"], ["Place both tools in a single ZIP archive", "وضع كلا الأداتين داخل ملف مضغوط واحد"], ["Convert Tool B to a personal geodatabase", "تحويل الأداة (ب) إلى قاعدة بيانات شخصية"]],
        "A",
        "A Precondition (visualized as a dashed connector arrow) forces a tool to wait until the designated precondition variable exists or completes before executing.",
        "يفرض الشرط المسبق (Precondition)، والذي يظهر كخط توصيل متقطع، على الأداة الانتظار حتى يكتمل تنفيذ المتغير المشروط بنجاح قبل أن تبدأ الأداة التالية عملها.",
        {"B": ["Scheduling days is manual and unreliable.", "الجدولة اليدوية غير عملية وغير موثوقة."], "C": ["ZIP archives cannot control execution flow.", "الملفات المضغوطة لا تدير تسلسل المعالجة."], "D": ["Personal geodatabases (.mdb) are deprecated and irrelevant.", "قواعد البيانات الشخصية ملغاة ولا علاقة لها بالنمذجة."]},
        "model"
    ),

    # 7: ModelBuilder Multiple Iterators Constraint
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Advanced", "Conceptual", ["ModelBuilder"],
        "An analyst attempts to add both an 'Iterate Feature Classes' iterator and an 'Iterate Fields' iterator inside the same ModelBuilder canvas. The iterator option for the second iterator is grayed out and disabled.",
        "حاول محلل إضافة مكررين معاً داخل نفس لوحة ModelBuilder: مكرر Iterate Feature Classes ومكرر Iterate Fields؛ فظهر خيار المكرر الثاني معطلاً وغير متاح.",
        "What architectural rule governs iterators in ModelBuilder, and how can this multi-loop requirement be achieved?",
        "ما هي القاعدة الهيكلية التي تحكم المكررات في ModelBuilder، وكيف يمكن تحقيق متطلب التكرار المزدوج هذا؟",
        [["A model can contain only one iterator; multi-loop workflows require creating a submodel containing one iterator and embedding it within the main model", "يمكن للنموذج احتواء مكرر واحد فقط؛ وتتطلب التكرارات المتعددة إنشاء نموذج فرعي يحوي مكرراً ودمجه داخل النموذج الرئيسي"], ["Iterators require an ArcGIS Pro Advanced license to run multiple instances", "تتطلب المكررات ترخيص Advanced لتشغيل عدة مكررات معاً"], ["Iterators cannot be used on file geodatabases", "لا يمكن استخدام المكررات مع قواعد البيانات الجغرافية"], ["The analyst must reboot the operating system", "يجب على المحلل إعادة تشغيل نظام التشغيل"]],
        "A",
        "ArcGIS Pro enforces a strict rule: only one iterator is permitted per model. To build nested loops, create a submodel with the secondary iterator and drag it into the master model.",
        "يفرض ArcGIS Pro قاعدة صارمة: يُسمح بمكرر واحد فقط في كل نموذج؛ ولإنشاء حلقات تكرارية متداخلة، يجب بناء نموذج فرعي بالمكرر الثانوي ودمجه داخل النموذج الرئيسي.",
        {"B": ["License levels do not lift the single-iterator architectural rule.", "مستويات الترخيص لا تغير قاعدة المكرر الواحد الهيكلية."], "C": ["Iterators work perfectly across all geodatabase types.", "المكررات تعمل مع كافة قواعد البيانات."], "D": ["Rebooting does not change core software architecture rules.", "إعادة التشغيل لا تغير القواعد الهندسية للبرنامج."]},
        "model"
    ),

    # 8: Spatial Join Match Options
    (
        "Compare table joins and relates, relationship classes, and spatial joins", "Intermediate", "Tool-based", ["Spatial Join"],
        "A municipal housing agency needs to find the nearest public park for each residential parcel and calculate the exact distance between each home and its closest park boundary.",
        "تحتاج إدارة إسكان بلدي لتحديد أقرب حديقة عامة لكل قطعة أرض سكنية، وحساب المسافة الدقيقة بين كل منزل وحدود أقرب حديقة له.",
        "Which tool and match option should be selected to append the park attributes and distance to the parcel records?",
        "ما هي الأداة وخيار المطابقة المناسبين لإلحاق بيانات الحديقة والمسافة إلى سجلات قطع الأراضي؟",
        [["Spatial Join with Match Option: 'Closest' (Distance field output populated)", "أداة Spatial Join مع اختيار خيار المطابقة: 'Closest' (مع ملء حقل المسافة الناتج)"], ["Add Join based on OBJECTID", "أداة Add Join بالاعتماد على حقل OBJECTID"], ["Buffer with 1-mile fixed radius", "أداة Buffer بمسافة ثابتة قدرها ميل واحد"], ["Intersect tool with default parameters", "أداة Intersect بالمعاملات الافتراضية"]],
        "A",
        "Spatial Join with the 'Closest' match option finds the nearest target feature and automatically generates a Distance field measuring the distance between input and join features.",
        "تقوم أداة Spatial Join بخيار المطابقة 'Closest' بالبحث عن أقرب معلم مستهدف وتنشئ تلقائياً حقلاً للمسافة يحسب البعد الدقيق بين المعلم المدخل ومعلم الربط.",
        {"B": ["Add Join requires shared attribute keys, not geometric proximity.", "يتطلب Add Join مفاتيح جدولية مشتركة وليس التقارب المكاني."], "C": ["Buffer creates zone geometries without identifying closest features.", "تنشئ Buffer مضلعات نطاقية دون تحديد أقرب معلم."], "D": ["Intersect only finds physically overlapping features, failing for separated parcels.", "تتطلب Intersect التراكب المباشر وتفشل مع العقارات المتباعدة."]},
        "proximity"
    ),

    # 9: Spatial Join One-To-Many vs One-To-One Merge Rules
    (
        "Compare table joins and relates, relationship classes, and spatial joins", "Intermediate", "Technical", ["Spatial Join"],
        "A health researcher joins demographic census tract polygons to a layer of air quality monitoring sensor points. Some census tracts contain 3 to 5 monitoring stations.",
        "يربط باحث صحي مضلعات مناطق التعداد السكاني بطبقة نقاط مجسات جودة الهواء؛ وتحتوي بعض مضلعات التعداد على 3 إلى 5 محطات رصد داخل حدودها.",
        "If the researcher performs a Spatial Join with 'Join One to One' and needs the average PM2.5 pollution reading across all sensors within each tract, what configuration is required?",
        "إذا أجرى الباحث ربطاً مكانياً (Spatial Join) بنمط 'Join One to One' وأراد حساب متوسط قراءة التلوث PM2.5 لكافة المجسات داخل كل قطاع، فما الإعداد المطلوب؟",
        [["Set the Field Map merge rule for the PM2.5 attribute to 'Mean'", "ضبط قاعدة الدمج (Merge Rule) في خريطة الحقول لحقل PM2.5 على المتوسط 'Mean'"], ["Set the Join Operation to 'Join One to Many'", "ضبط عملية الربط على واحد لمتعدد (Join One to Many)"], ["Delete sensors with low readings", "حذف المجسات ذات القراءات المنخفضة"], ["Set the coordinate system to WGS 1984", "ضبط نظام الإحداثيات على WGS 1984"]],
        "A",
        "In a One-to-One Spatial Join where multiple join features overlap an input feature, configuring Field Map merge rules (e.g. Mean, Sum, Count, Min, Max) aggregates overlapping values into a single summary attribute.",
        "في الربط المكاني بنمط (One-to-One) عند تراكب عدة معالم مع المعلم المدخل، يتيح ضبط قواعد دمج الحقول (مثل Mean أو Sum) تجميع وحساب متوسط أو مجموع القيم في سجل وحيد.",
        {"B": ["Join One to Many duplicates the census tract polygons for every sensor.", "نمط واحد لمتعدد يكرر مضلعات التعداد لكل مجس."], "C": ["Deleting data corrupts study integrity.", "حذف البيانات يفسد نزاهة الدراسة."], "D": ["Coordinate systems do not perform attribute statistical aggregation.", "نظام الإحداثيات لا يحسب المتوسطات الحسابية."]},
        "overlay"
    ),

    # 10: Clip vs Intersect Geometric Differences
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Beginner", "Conceptual", ["Clip", "Intersect"],
        "A cartographer needs to trim a statewide soil polygon dataset to the boundaries of a county. The cartographer wants to keep all original soil attributes intact, but strictly does NOT want any county boundary attribute fields appended to the output table.",
        "يحتاج رسام خرائط لقص طبقة تربة على مستوى الولاية عند حدود إحدى المقاطعات؛ ويريد الاحتفاظ بكافة بيانات سمات التربة الأصلية، ولكنه يرفض تماماً إضافة أي حقول سمات من طبقة المقاطعة إلى جدول النتائج.",
        "Which geoprocessing tool satisfies this specific requirement?",
        "ما هي أداة المعالجة الجغرافية التي تحقق هذا المتطلب تحديداً؟",
        [["Clip", "أداة القص (Clip)"], ["Intersect", "أداة التقاطع (Intersect)"], ["Union", "أداة الاتحاد (Union)"], ["Identity", "أداة الهوية (Identity)"]],
        "A",
        "Clip cuts spatial features like a cookie cutter, preserving only the input layer's geometry within the clip boundary and carrying over ONLY the input layer's attributes (no attributes from the clip feature).",
        "تعمل أداة Clip كقالب البسكويت؛ فتقص معالم الإدخال عند حدود القص وتحتفظ ببيانات وسمات طبقة الإدخال فقط دون إلحاق أي سمات من طبقة القص.",
        {"B": ["Intersect combines and appends attribute fields from both layers.", "تدمج Intersect وتلحق حقول السمات من كلتا الطبقتين."], "C": ["Union combines geometries and attributes from all input layers.", "تدمج Union كافة المعالم والسمات."], "D": ["Identity transfers attributes from the identity layer.", "تلحق Identity سمات طبقة الهوية."]},
        "overlay"
    ),

    # 11: Union Polygon Requirement & Null Attributes
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Technical", ["Union"],
        "An environmental consultant runs the Union tool on two overlapping polygon layers: Industrial Parcels and Wetland Buffers. In the output attribute table, several rows display <Null> values in the Industrial Parcels fields.",
        "أجرى مستشار بيئي أداة Union على طبقتي مضلعات متراكبتين: الأراضي الصناعية ومناطق حماية المستنقعات؛ وفي جدول النتائج، ظهرت قيم <Null> في حقول الأراضي الصناعية لعدة سجلات.",
        "Why do these <Null> attribute values appear in the Union output?",
        "لماذا تظهر قيم <Null> السماتية هذه في مخرجات أداة Union؟",
        [["Because Union outputs all non-overlapping areas from each input layer, populating attributes with Null where that specific layer had no overlapping geometry", "لأن أداة Union تخرج كافة المساحات غير المتراكبة من كلتا الطبقتين، وتملأ السمات بقيم فارغة (Null) في الأجزاء التي لم يكن للطبقة فيها وجود مكاني"], ["Because the geodatabase ran out of disk space", "لأن مساحة قاعدة البيانات على القرص قد نفدت"], ["Because Union requires polyline datasets", "لأن أداة Union تتطلب بيانات خطية"], ["Because the geometry of the wetlands was invalid", "لأن هندسة المستنقعات كانت غير صالحة"]],
        "A",
        "Union computes the geometric union of polygon layers, writing all areas whether overlapping or unique to each layer. Areas where a layer does not exist naturally receive Null attribute values.",
        "تحسب أداة Union الاتحاد الهندسي الشامل لطبقات المضلعات؛ فتبرز المساحات المتراكبة والمنفردة لكل طبقة، وتأخذ المساحات المنفردة قيماً فارغة (Null) لحقول الطبقة الأخرى غير الموجودة مكانياً في تلك البقعة.",
        {"B": ["Disk space exhaustion throws a fatal write error.", "نفاد القرص يوقف العملية بخطأ كتابة."], "C": ["Union strictly requires polygon feature classes.", "تتطلب Union مضلعات فقط."], "D": ["Invalid geometry causes tool failure, not null attributes.", "العيوب الهندسية تفشل الأداة ولا تنتج قيماً فارغة بانتظام."]},
        "overlay"
    ),

    # 12: Erase License Workaround
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Troubleshooting", ["Erase", "Symmetrical Difference"],
        "A technician with an ArcGIS Pro Standard license needs to remove flood zone polygons from proposed development parcels (removing overlapping areas). When searching for the Erase tool, it is not available because Erase requires an Advanced license.",
        "يحتاج فني بترخيص ArcGIS Pro Standard لاستبعاد مضلعات مناطق الفيضان من قطع الأراضي المقترحة للتطوير (إزالة الأجزاء المتراكبة)؛ وعند البحث عن أداة Erase لم يجدها لأنها تتطلب ترخيص Advanced.",
        "Which geoprocessing workflow achieves the exact same spatial removal result without an Advanced license?",
        "أي مسار عمل للمعالجة الجغرافية يحقق نفس نتيجة الحذف المكاني الدقيقة دون الحاجة لترخيص Advanced؟",
        [["Use Intersect to isolate flood areas within parcels, then use Erase alternatives like Symmetrical Difference or Update with polygon negation", "استخدام أداة Intersect لعزل مناطق الفيضان داخل العقارات، ثم استخدام بدائل مثل Symmetrical Difference أو التحديد والعكس"], ["Convert all features to KML format", "تحويل كافة المعالم إلى صيغة KML"], ["Export the layers to Excel spreadsheets", "تصدير الطبقات إلى جداول إكسل"], ["Delete all parcels manually", "حذف كافة قطع الأراضي يدوياً"]],
        "A",
        "The Erase tool requires an Advanced license. Users on Basic or Standard licenses can replicate the result using workflows like Symmetrical Difference, Identity, or spatial selection with inversion.",
        "تتطلب أداة Erase ترخيص Advanced حصراً؛ ويمكن لمستخدمي تراخيص Basic و Standard الحصول على نفس النتيجة باستخدام أدوات بديلة مثل Symmetrical Difference أو التحديد المكاني المعكوس.",
        {"B": ["KML conversion is a display format, not spatial overlay.", "صيغة KML للعرض وليست للتحليل."], "C": ["Excel spreadsheets strip spatial geometry completely.", "إكسل يفقد البيانات هندستها المكانية."], "D": ["Manual deletion is error-prone and unscalable.", "الحذف اليدوي عرضة للخطأ ولا يصلح للمشاريع."]},
        "overlay"
    ),

    # 13: Multiple Ring Buffer vs Buffer Dissolve
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Beginner", "Tool-based", ["Buffer", "Multiple Ring Buffer"],
        "An airport planning authority needs to create noise contour zones at distances of 1, 3, and 5 miles around runway centerlines. The authority requires concentric non-overlapping rings where each ring forms a distinct polygon band with a distance attribute field.",
        "تحتاج إدارة تخطيط المطارات لإنشاء نطاقات ضوضاء على مسافات 1 و 3 و 5 أميال حول خطوط مدارج الطائرات؛ وتشترط الإدارة تكوين حلقات متحدة المركز غير متداخلة بحيث تشكل كل حلقة نطاقاً مضلعياً مستقلاً يحتوي على حقل بقيمة المسافة.",
        "Which tool creates this concentric multi-distance ring dataset directly?",
        "ما هي الأداة التي تنشئ طبقة الحلقات متحدة المركز متعددة المسافات هذه مباشرة؟",
        [["Multiple Ring Buffer with Buffer Distances (1, 3, 5) and Outside Polygons Only", "أداة Multiple Ring Buffer بتحديد المسافات (1, 3, 5) واختيار حلقات خارجية فقط"], ["Standard Buffer tool executed once with distance of 5 miles", "أداة Buffer العادية بتنفيذها مرة واحدة بمسافة 5 أميال"], ["Near tool with search radius of 5 miles", "أداة Near بنصف قطر بحث 5 أميال"], ["Spatial Join with closest match option", "أداة Spatial Join بخيار أقرب تطابق"]],
        "A",
        "The Multiple Ring Buffer tool creates a series of concentric buffer rings at specified distance intervals around input features, populating a distance attribute field for each discrete ring band.",
        "تنشئ أداة Multiple Ring Buffer سلسلة من حلقات النطاق متحدة المركز عند فواصل مسافات محددة حول المعالم، وتملأ حقلاً بقيمة مسافة كل حلقة نطاقية منفصلة.",
        {"B": ["A single 5-mile buffer creates one large polygon without 1-mile or 3-mile subdivisions.", "النطاق المنفرد ينشئ مضلعاً واحداً دون فواصل 1 و 3 أميال."], "C": ["Near measures point distances without generating polygon geometry.", "أداة Near تقيس المسافات ولا تنشئ مضلعات."], "D": ["Spatial Join transfers attributes, not buffer rings.", "الربط المكاني ينقل السمات ولا ينشئ حلقات."]},
        "proximity"
    ),

    # 14: Near vs Generate Near Table Output Architecture
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Technical", ["Near", "Generate Near Table"],
        "A logistics analyst measures distances from 1,000 retail stores to 50 regional warehouses. The analyst needs to find ALL warehouses located within 25 miles of each store (which may produce 0, 1, 2, or up to 5 matching warehouse pairs per store).",
        "يقيس محلل لوجستي المسافات من 1,000 متجر تجزئة إلى 50 مستودعاً إقليمياً؛ ويحتاج لحصر كافة المستودعات الواقعة على مسافة 25 ميلاً من كل متجر (مما قد ينتج 0 أو 1 أو 2 أو حتى 5 مستودعات مطابقة للمتجر الواحد).",
        "Why must the analyst use 'Generate Near Table' instead of the standard 'Near' tool?",
        "لماذا يجب على المحلل استخدام أداة 'Generate Near Table' بدلاً من أداة 'Near' القياسية؟",
        [["Because the standard Near tool only writes the single closest feature onto the input table, whereas Generate Near Table creates a new table supporting multiple 1:Many near records within search radius", "لأن أداة Near القياسية تكتب أقرب معلم واحد فقط على جدول المدخلات، بينما تنشئ Generate Near Table جدولاً جديداً يدعم علاقة واحد لمتعدد (1:Many) لكافة المعالم ضمن نصف القطر"], ["Because the Near tool only works on raster datasets", "لأن أداة Near تعمل على بيانات الراستر فقط"], ["Because Generate Near Table is a 3D-only tool", "لأن أداة Generate Near Table ثلاثية الأبعاد فقط"], ["Because the Near tool requires an enterprise geodatabase", "لأن أداة Near تتطلب قاعدة بيانات مؤسسية"]],
        "A",
        "The Near tool only appends NEAR_FID and NEAR_DIST for the single nearest feature directly into the input table. Generate Near Table produces a standalone table capable of recording multiple matches per input feature.",
        "تضيف أداة Near حقلي NEAR_FID و NEAR_DIST لأقرب معلم واحد فقط داخل جدول الإدخال نفسه؛ بينما تنشئ أداة Generate Near Table جدولاً مستقلاً قادراً على تسجيل عدة معالم مطابقة لكل معلم إدخال.",
        {"B": ["Near works on vector points, lines, and polygons.", "تعمل أداة Near على النقاط والخطوط والمضلعات."], "C": ["Generate Near Table is fully functional in 2D and 3D.", "تعمل الأداة في البيئتين ثنائية وثلاثية الأبعاد."], "D": ["Near works across all geodatabase types.", "تعمل الأداة على كافة قواعد البيانات."]},
        "proximity"
    ),

    # 15: Raster Functions vs Geoprocessing Tools Architecture
    (
        "Apply raster functions for raster and image processing", "Intermediate", "Conceptual", ["Raster Functions"],
        "A satellite imagery team needs to calculate NDVI and apply dynamic hillshading across 500 GB of multi-spectral drone rasters. The team needs to visualize and explore results immediately on the screen, but has very limited local hard drive space.",
        "يحتاج فريق صور أقمار صناعية لحساب مؤشر NDVI وتطبيق تظليل تضاريسي ديناميكي على 500 جيجابايت من صور الدرون؛ ويريد الفريق استعراض النتائج فورياً على الشاشة مع وجود مساحة تخزين محدودة جداً على القرص الصلب.",
        "Why should the team use Raster Functions instead of standard Geoprocessing tools?",
        "لماذا يجب على الفريق استخدام دوال الراستر (Raster Functions) بدلاً من أدوات المعالجة الجغرافية القياسية؟",
        [["Raster functions process pixels on-the-fly in-memory for the current display extent without writing intermediate or output raster files to disk", "تعالج دوال الراستر البكسلات فورياً داخل الذاكرة لنطاق العرض الحالي دون كتابة ملفات راستر مؤقتة أو نهائية على القرص"], ["Raster functions convert rasters into vector shapefiles", "تحول دوال الراستر الصور إلى ملفات shapefile اتجاهية"], ["Raster functions automatically delete cloud cover from aerial photos", "تحذف دوال الراستر الغيوم تلقائياً من الصور"], ["Raster functions only work with an Internet connection", "تعمل دوال الراستر عبر اتصال الإنترنت فقط"]],
        "A",
        "Raster functions apply pixel operations dynamically in-memory at display resolution, saving massive disk space and delivering instant visual results without writing new raster files to storage.",
        "تطبق دوال الراستر (Raster Functions) العمليات الحسابية على البكسلات في الذاكرة فورياً وبدقة شاشة العرض فقط، مما يوفر مساحات تخزين هائلة ويمنح نتائج مرئية فورية دون كتابة ملفات راستر على القرص.",
        {"B": ["Raster functions do not vectorize imagery.", "لا تحول دوال الراستر البيانات إلى متجهات."], "C": ["Cloud removal requires dedicated multispectral masking algorithms.", "إزالة الغيوم تتطلب خوارزميات معالجة خاصة."], "D": ["Raster functions run entirely locally offline.", "تعمل دوال الراستر محلياً دون الحاجة للإنترنت."]},
        "raster"
    ),

    # 16: Raster Calculator Conditional Con Expression
    (
        "Apply raster functions for raster and image processing", "Intermediate", "Technical", ["Raster Calculator"],
        "A slope suitability analyst needs to create a binary suitability raster from an elevation DEM. Slopes greater than 15 degrees must be assigned a value of 0 (unsuitable), while slopes 15 degrees or less must be assigned a value of 1 (suitable).",
        "يحتاج محلل ملاءمة انحدار لإنشاء راستر ثنائي للملاءمة من نموذج ارتفاع رقمي؛ بحيث تأخذ الانحدارات الأكبر من 15 درجة القيمة 0 (غير ملائم)، بينما تأخذ الانحدارات 15 درجة أو أقل القيمة 1 (ملائم).",
        "Which Map Algebra expression in Raster Calculator evaluates this condition correctly?",
        "أي تعبير جبر الخرائط (Map Algebra) في Raster Calculator ينفذ هذا الشرط بشكل صحيح؟",
        [["Con(\"Slope\" > 15, 0, 1)", "Con(\"Slope\" > 15, 0, 1)"], ["IF \"Slope\" > 15 THEN 0 ELSE 1", "IF \"Slope\" > 15 THEN 0 ELSE 1"], ["WHERE \"Slope\" > 15 = 0 AND <= 15 = 1", "WHERE \"Slope\" > 15 = 0 AND <= 15 = 1"], ["CASE WHEN \"Slope\" > 15: 0; ELSE: 1", "CASE WHEN \"Slope\" > 15: 0; ELSE: 1"]],
        "A",
        "ArcGIS Pro Map Algebra evaluates conditional logic using the Con() function: `Con(conditional_statement, true_value, false_value)`. Here, `Con(\"Slope\" > 15, 0, 1)` assigns 0 when >15 and 1 otherwise.",
        "يقيم جبر الخرائط في ArcGIS Pro الشروط المنطقية باستخدام دالة Con: بالصيغة `Con(شرط_منطقي, قيمة_الصواب, قيمة_الخطأ)`، وبذلك فإن `Con(\"Slope\" > 15, 0, 1)` تمنح 0 للأكبر من 15 و 1 لما دون ذلك.",
        {"B": ["IF/THEN syntax is not valid Map Algebra in Raster Calculator.", "صيغة IF/THEN ليست صيغة صحيحة في جبر الخرائط."], "C": ["WHERE is standard database SQL, not raster algebra.", "جملة WHERE تستخدم في قواعد بيانات SQL وليس في راستر."], "D": ["CASE WHEN belongs to SQL expressions.", "صيغة CASE WHEN تتبع لغة استعلامات SQL."]},
        "raster"
    ),

    # 17: Zonal Statistics as Table Mechanics
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Zonal Statistics as Table"],
        "A regional forestry agency maintains watershed polygon boundaries and a continuous annual rainfall raster grid. The agency needs a standalone summary table showing the Mean, Minimum, and Maximum rainfall values for each individual watershed.",
        "تدير هيئة غابات إقليمية حدود مضلعات أحواض تصريف مائية وراستر مستمر لمعدلات هطول الأمطار السنوية؛ وتحتاج الهيئة إلى جدول إحصائي ملخص يوضح متوسط وأدنى وأعلى قيمة مطر لكل حوض تصريف على حدة.",
        "Which geoprocessing tool generates this multi-metric summary table?",
        "ما هي أداة المعالجة الجغرافية التي تنشئ هذا الجدول الإحصائي متعدد المؤشرات؟",
        [["Zonal Statistics as Table", "أداة Zonal Statistics as Table"], ["Zonal Statistics", "أداة Zonal Statistics"], ["Surface Volume", "أداة Surface Volume"], ["Extract Multi Values to Points", "أداة Extract Multi Values to Points"]],
        "A",
        "Zonal Statistics as Table summarizes cell values from an input value raster within the boundaries of designated zone features, outputting a standalone table containing multiple requested statistics (Mean, Min, Max, Sum, etc.).",
        "تلخص أداة Zonal Statistics as Table قيم خلايا راستر القيم المدخل داخل حدود معالم النطاقات المحددة، وتنتج جدولاً مستقلاً يحوي كافة المؤشرات الإحصائية المطلوبة (المتوسط، الأدنى، الأعلى، المجموع، إلخ).",
        {"B": ["Zonal Statistics outputs a raster grid rather than a standalone table.", "تنتج أداة Zonal Statistics راستر وليس جدولاً مستقلاً."], "C": ["Surface Volume calculates volumes between a raster and reference plane.", "تحسب أداة Surface Volume الحجوم بين السطح ومستوى مرجعي."], "D": ["Extract to Points requires vector point inputs, not polygon zones.", "تتطلب أداة Extract نقاطاً اتجاهية وليس مضلعات نطاقية."]},
        "surface"
    ),

    # 18: Reclassify for Suitability Modeling
    (
        "Apply raster functions for raster and image processing", "Beginner", "Tool-based", ["Reclassify"],
        "An analyst models wildlife habitat suitability by combining continuous elevation, slope, and land cover rasters. Before combining them in a weighted sum model, all continuous variables must be transformed into standardized integer ranks from 1 (poor) to 5 (optimal).",
        "ينمذج محلل ملاءمة موائل الحياة الفطرية بدمج راستر الارتفاع المستمر والانحدار والغطاء الأرضي؛ وقبل دمجها في نموذج جمع موزون، يجب تحويل كافة المتغيرات المستمرة إلى رتب رقمية صحيحة معيارية من 1 (ضعيف) إلى 5 (مثالي).",
        "Which tool converts continuous floating-point raster ranges into discrete categorical integer scale classes?",
        "ما الأداة التي تحول فترات قيم الراستر العشرية المستمرة إلى فئات أرقام صحيحة تصنيفية قياسية؟",
        [["Reclassify", "أداة إعادة التصنيف (Reclassify)"], ["Resample", "أداة إعادة أخذ العينات (Resample)"], ["Clip Raster", "أداة قص الراستر (Clip Raster)"], ["Raster to Polygon", "أداة تحويل الراستر إلى مضلعات (Raster to Polygon)"]],
        "A",
        "The Reclassify tool replaces old cell values or continuous numeric ranges with new discrete integer class values, standardizing disparate raster datasets into uniform rating scales for suitability modeling.",
        "تستبدل أداة Reclassify قيم الخلايا القديمة أو الفترات الرقمية المستمرة بقيم أرقام صحيحة جديدة، مما يوحد مقاييس طبقات الراستر المختلفة ضمن مقياس رتب موحد لنماذج الملاءمة المكانية.",
        {"B": ["Resample alters spatial resolution (cell size), not class rating values.", "تغير أداة Resample حجم الخلية وليس رتب الفئات."], "C": ["Clip Raster extracts a spatial sub-extent.", "تقص أداة Clip نطاقاً جغرافياً فقط."], "D": ["Raster to Polygon converts raster grids to vector shapes.", "تحول أداة Raster to Polygon البيانات إلى متجهات."]},
        "raster"
    ),

    # 19: Slope: Degrees vs Percent Rise
    (
        "Apply raster functions for raster and image processing", "Beginner", "Conceptual", ["Slope"],
        "A civil engineering department designs a wheelchair-accessible ramp adhering to building codes that limit maximum incline to an 8.33% grade (a rise of 1 foot per 12 feet of run).",
        "تصمم إدارة هندسة مدنية ممشى لذوي الاحتياجات الخاصة وفق اشتراطات البناء التي تقيد أقصى انحدار بنسبة 8.33% (ارتفاع قدم واحد لكل 12 قدماً أفقياً).",
        "Which parameter setting in the Slope geoprocessing tool ensures slope values are calculated in grade percentage rather than angular degrees?",
        "ما هو خيار المعامل في أداة Slope الذي يضمن حساب قيم الانحدار كنسبة مئوية بدلاً من الدرجات الزاوية؟",
        [["Output measurement: 'PERCENT_RISE'", "وحدة القياس الناتجة: 'PERCENT_RISE' (نسبة الارتفاع المئوية)"], ["Output measurement: 'DEGREE'", "وحدة القياس الناتجة: 'DEGREE' (درجات)"], ["Z-Factor set to 0.0", "ضبط معامل Z على 0.0"], ["Method set to Geodesic", "ضبط الطريقة على جيوديسية Geodesic"]],
        "A",
        "The Slope tool provides two output measurement options: DEGREE (0 to 90 degrees) and PERCENT_RISE (rise divided by run multiplied by 100, where 45 degrees equals 100% rise).",
        "توفر أداة Slope خيارين لوحدة القياس: DEGREE (من 0 إلى 90 درجة زاوية) و PERCENT_RISE (الارتفاع مقسوماً على المسافة الأفقية × 100، حيث تعادل زاوية 45 درجة نسبة 100%).",
        {"B": ["DEGREE outputs angular incline from 0 to 90, not percentage grade.", "تقيس وحدة DEGREE الزوايا وليس النسبة المئوية."], "C": ["A Z-Factor of 0 flattens the surface entirely.", "معامل Z بقيمة 0 يجعل السطح مستوياً تماماً."], "D": ["Geodesic controls curvature computation, not percentage unit.", "تتحكم الطريقة الجيوديسية في كروية الأرض وليس نوع الوحدة."]},
        "surface"
    ),

    # 20: Aspect Azimuth and Flat Areas (-1)
    (
        "Apply raster functions for raster and image processing", "Intermediate", "Technical", ["Aspect"],
        "An agricultural climatologist analyzes solar exposure for vineyard planting. Cells facing due South receive optimal warmth. In the output Aspect raster, the climatologist notices several cells in valley bottoms assigned a value of -1.",
        "يحلل باحث مناخ زراعي التعرض الشمسي لزراعة الكروم؛ حيث تتلقى المنحدرات المتجهة جنوباً الدفء الأمثل؛ وفي راستر الواجهة الجغرافية (Aspect) الناتج، لاحظ الباحث خلايا في قيعان الوديان تحمل القيمة -1.",
        "What do cell values of -1 represent in an Aspect raster?",
        "ماذا تمثل قيم الخلايا -1 في راستر الواجهة الجغرافية (Aspect)؟",
        [["Flat terrain surfaces with zero slope incline where no downslope compass direction exists", "أسطح تضاريس مستوية تماماً ذات انحدار صفري حيث لا يوجد اتجاه هبوط بوصلة"], ["Cells located below mean sea level", "خلايا تقع تحت مستوى سطح البحر"], ["Corrupted cells caused by missing DEM tiles", "خلايا تالفة بسبب فقدان أجزاء من نموذج الارتفاع"], ["Cells facing true magnetic North", "خلايا تواجه اتجاه الشمال المغناطيسي"]],
        "A",
        "In ArcGIS Pro, the Aspect tool calculates the downhill compass direction of maximum rate of change (0 to 360 degrees). Completely flat areas with zero slope have no slope direction and are coded as -1.",
        "في ArcGIS Pro، تحسب أداة Aspect الاتجاه البوصلتي لأقصى انحدار هبوطاً (من 0 إلى 360 درجة)؛ والمناطق المستوية تماماً ذات الانحدار الصفري ليس لها اتجاه هبوط وتُعطى القيمة -1.",
        {"B": ["Depressions below sea level have elevations, not -1 aspect values.", "المناطق تحت سطح البحر لها مناسيب سالبة وليس واجهة -1."], "C": ["Corrupted or missing pixels are represented by NoData, not -1.", "الخلايا المفقودة تأخذ قيمة NoData وليس -1."], "D": ["True North is assigned values near 0 or 360 degrees.", "يأخذ الشمال الحقيقي قيماً تقترب من 0 أو 360 درجة."]},
        "surface"
    ),

    # 21: Hillshade Z-Factor Unit Mismatch
    (
        "Apply raster functions for raster and image processing", "Intermediate", "Troubleshooting", ["Hillshade"],
        "A GIS technician generates a Hillshade from an elevation raster. The raster's horizontal coordinates (X and Y) are in State Plane feet, but the vertical elevation values (Z) stored in the raster are in meters. The technician uses the default Z-Factor of 1.0, producing a severely exaggerated and spiky surface.",
        "أنشأ فني تظليلاً تضاريسياً (Hillshade) من راستر ارتفاع؛ وكانت إحداثيات الراستر الأفقية (X و Y) بأقدام State Plane، بينما قيم الارتفاع الرأسية (Z) مخزنة بالأمتار؛ واستخدم الفني معامل Z الافتراضي 1.0 فظهر السطح مشوهاً ومبالغاً في حدته وتسننه بشكل مفرط.",
        "What mathematical adjustment should be made to the Z-Factor to correct for this unit discrepancy (feet vs meters)?",
        "ما هو التعديل الرياضي الذي يجب تطبيقه على معامل Z لتصحيح عدم تطابق الوحدات هذا (أقدام مقابل أمتار)؟",
        [["Set the Z-Factor to 3.28084 (converting meters to feet)", "ضبط معامل Z على 3.28084 (لتحويل الأمتار إلى أقدام)"], ["Set the Z-Factor to 0.0", "ضبط معامل Z على 0.0"], ["Set the Z-Factor to -1.0", "ضبط معامل Z على -1.0"], ["Increase the Sun Azimuth to 360 degrees", "زيادة سمت الشمس إلى 360 درجة"]],
        "A",
        "The Z-Factor reconciles differences between horizontal ground units (XY) and vertical elevation units (Z). Since 1 meter equals 3.28084 feet, multiplying Z by 3.28084 scales vertical elevations to match horizontal feet.",
        "يعادل معامل Z الفروق بين وحدات القياس الأفقية (XY) والوحدات الرأسية للارتفاع (Z)؛ وبما أن المتر الواحد يعادل 3.28084 قدماً، فإن ضرب Z في 3.28084 يحول الارتفاعات لتطابق الأقدام الأفقية.",
        {"B": ["A Z-Factor of 0 creates a completely flat gray image.", "معامل Z بقيمة 0 ينتج صورة رمادية مسطحة."], "C": ["Negative Z-factors invert terrain, turning hills into valleys.", "المعامل السالب يعكس التضاريس محولاً التلال لوديان."], "D": ["Sun Azimuth controls lighting angle, not vertical unit scaling.", "سمت الشمس يحدد زاوية الضوء ولا يصحح الوحدات."]},
        "surface"
    ),

    # 22: Hydrology Drainage Workflow Sequence
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Workflow-based", ["Hydrology"],
        "A hydrologist delineates catchment basins from a raw digital elevation model. If the hydrologist runs the Flow Direction tool directly on the raw DEM, internal depressions and single-cell pits interrupt flow routing, producing broken stream networks.",
        "يحدد باحث هيدرولوجيا أحواض تصريف مائية من نموذج ارتفاع رقمي خام؛ وإذا قام بتشغيل أداة Flow Direction مباشرة على الراستر الخام، فإن الحفر والمنخفضات الداخلية تعترض مسار الجريان وتنتج شبكة مجارٍ مقطوعة.",
        "Which preprocessing tool must be executed first to remove spurious surface depressions before running Flow Direction?",
        "ما هي أداة المعالجة الأولية التي يجب تنفيذها أولاً لإزالة المنخفضات والحفر السطحية الوهمية قبل تشغيل Flow Direction؟",
        [["Fill", "أداة ملء المنخفضات (Fill)"], ["Sink", "أداة Sink"], ["Flow Accumulation", "أداة Flow Accumulation"], ["Snap Pour Point", "أداة Snap Pour Point"]],
        "A",
        "The standard Esri hydrology workflow begins with the Fill tool, which fills sinks and surface pits in the DEM to ensure continuous hydrological drainage across the entire terrain model.",
        "يبدأ مسار العمل الهيدرولوجي القياسي في Esri بأداة Fill لملء المنخفضات والحفر السطحية غير الحقيقية في نموذج الارتفاع، مما يضمن جرياناً مائياً متصلاً عبر التضاريس بأكملها.",
        {"B": ["Sink identifies depressions but does not fill them.", "تحدد أداة Sink المنخفضات دون أن تملأها."], "C": ["Flow Accumulation requires a valid Flow Direction raster as input.", "تتطلب Flow Accumulation راستر اتجاه جريان مسبقاً."], "D": ["Snap Pour Point aligns pour points to cells of high flow accumulation.", "تحاذي Snap Pour Point نقاط المصب مع خلايا التجمع العالي."]},
        "surface"
    ),

    # 23: Create Space Time Cube Mechanics (.nc)
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Technical", ["Create Space Time Cube"],
        "A crime intelligence analyst prepares 5 years of burglaries (with XY coordinates and timestamps) for spatio-temporal trend analysis. The analyst uses 'Create Space Time Cube By Aggregating Points' to bin incidents into 1-mile spatial bins and 1-month time steps.",
        "يجهز محلل جرائم بيانات سطو على مدى 5 سنوات (تحوي إحداثيات وتواريخ) لتحليل الاتجاهات المكانية والزمانية؛ ويستخدم أداة 'Create Space Time Cube By Aggregating Points' لتجميع الحوادث في أوعية مكانية بمساحة ميل وفواصل زمنية شهرية.",
        "What file format is produced by this tool to store the multidimensional space-time lattice?",
        "ما هي صيغة الملف التي تنتجها هذه الأداة لتخزين الشبكة المكانية الزمانية متعددة الأبعاد؟",
        [["Network Common Data Form (.nc) file", "ملف NetCDF بصيغة Network Common Data Form (.nc)"], ["Shapefile (.shp)", "ملف Shapefile (.shp)"], ["AutoCAD Drawing (.dwg)", "ملف أوتوكاد (.dwg)"], ["Comma-Separated Values (.csv)", "ملف نصي مفصول بفواصل (.csv)"]],
        "A",
        "ArcGIS Pro Space Time pattern mining tools store 3D multidimensional cubes as NetCDF (.nc) files, encoding spatial bin coordinates (X, Y) and chronological time slices (Z/Time).",
        "تخزن أدوات التنقيب عن الأنماط المكانية الزمانية في ArcGIS Pro المكعبات ثلاثية الأبعاد بصيغة ملفات NetCDF (.nc)، والتي تشفر إحداثيات الخلايا المكانية (X, Y) والشرائح الزمنية (Z/Time).",
        {"B": ["Shapefiles are 2D flat vector formats limited to 2 GB.", "ملفات Shapefile ثنائية الأبعاد ومحدودة بـ 2 جيجابايت."], "C": ["DWG is a CAD engineering format.", "صيغة DWG للرسومات الهندسية."], "D": ["CSV files are flat 2D tabular text files.", "ملفات CSV جداول نصية ثنائية مسطحة."]},
        "spatial_stats"
    ),

    # 24: Emerging Hot Spot Analysis Patterns
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Advanced", "Conceptual", ["Emerging Hot Spot Analysis"],
        "A public health epidemiologist analyzes a NetCDF space-time cube of influenza hospitalizations over the winter season. The tool identifies a specific neighborhood as an 'Intensifying Hot Spot'.",
        "يحلل باحث وبائيات مكعب NetCDF مكاني زماني لحالات التنويم بالإنفلونزا خلال فصل الشتاء؛ وصنفت الأداة حياً معيناً كـ 'بؤرة ساخنة متصاعدة' (Intensifying Hot Spot).",
        "What does the 'Intensifying Hot Spot' category indicate about this neighborhood's temporal trend?",
        "ماذا يعني تصنيف 'بؤرة ساخنة متصاعدة' (Intensifying Hot Spot) بالنسبة للاتجاه الزمني لهذا الحي؟",
        [["The location has been a statistically significant hot spot for 90% of the time steps, and the intensity of clustering of high counts is increasing overall", "كان الموقع بؤرة ساخنة ذات دلالة إحصائية في 90% من الفترات الزمنية، وتتزايد شدة تجمع الحالات العالية فيه بشكل تصاعدي عام"], ["The location became a hot spot for the very first time in the final time step", "أصبح الموقع بؤرة ساخنة لأول مرة في الفترة الزمنية الأخيرة فقط"], ["The location was a cold spot that abruptly flipped to a hot spot", "كان الموقع بؤرة باردة ثم انقلب فجأة إلى بؤرة ساخنة"], ["The location has zero reported incidents", "الموقع لم يسجل أي حالات إصابة إطلاقاً"]],
        "A",
        "An Intensifying Hot Spot designates a location that has been a statistically significant hot spot for ninety percent of the time-step intervals, including the final time step, with a statistically significant increase in clustering intensity.",
        "تعرف 'البؤرة الساخنة المتصاعدة' بأنها موقع كان بؤرة ساخنة ذات دلالة إحصائية طوال 90% من الفترات الزمنية بما فيها الفترة الأخيرة، مع زيادة ذات دلالة إحصائية في شدة تركز القيم العالية.",
        {"B": ["First-time hot spots are categorized as 'New Hot Spots'.", "البؤرة للمرة الأولى تصنف كـ New Hot Spot."], "C": ["Flipping patterns are categorized as Oscillating Hot Spots.", "الانقلاب بين الساخن والبارد يصنف كـ Oscillating."], "D": ["Zero incidents would register as cold or not significant.", "غياب الحالات ينتج عدم دلالة أو بؤراً باردة."]},
        "spatial_stats"
    ),

    # 25: Hot Spot Analysis (Getis-Ord Gi*) P-values & Z-scores
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Technical", ["Hot Spot Analysis"],
        "An analyst runs Hot Spot Analysis (Getis-Ord Gi*) on traffic accidents. A cluster of intersections yields a Z-score of +3.45 and a p-value of 0.0005.",
        "أجرى محلل أداة التحليل البؤري Hot Spot Analysis (Getis-Ord Gi*) على حوادث المرور؛ وأظهر تجمع من التقاطعات درجة معيارية Z-score بلغت +3.45 مع قيمة احتمالية p-value قدرها 0.0005.",
        "How should the analyst interpret these statistical results at a 99% confidence level?",
        "كيف يجب على المحلل تفسير هذه النتائج الإحصائية عند مستوى ثقة 99%؟",
        [["Statistically significant hot spot cluster; the probability that this high concentration occurred by random chance is less than 0.1%", "تجمع بؤرة ساخنة ذو دلالة إحصائية؛ واحتمال حدوث هذا التركز العالي بمحض الصدفة العشوائية أقل من 0.1%"], ["Statistically significant cold spot cluster", "تجمع بؤرة باردة ذو دلالة إحصائية"], ["Random spatial noise with no statistical significance", "تشويش مكاني عشوائي لا يحمل أي دلالة إحصائية"], ["Data corruption error in coordinate registration", "خطأ تلف في البيانات في تسجيل الإحداثيات"]],
        "A",
        "In Getis-Ord Gi*, a high positive Z-score (> +2.58) combined with a tiny p-value (< 0.01) indicates a statistically significant hot spot cluster where high values cluster beyond what can be explained by random chance.",
        "في اختبار Getis-Ord Gi*، تدل الدرجة المعيارية الموجبة المرتفعة (أكبر من 2.58) مع قيمة p صغيرة (أقل من 0.01) على بؤرة ساخنة ذات دلالة إحصائية فائقة، يستحيل تفسيرها بالصدفة العشوائية.",
        {"B": ["Cold spots require large negative Z-scores (e.g. < -2.58).", "تتطلب البؤر الباردة درجات معيارية سالبة."], "C": ["Z-score of +3.45 is far outside the random null range (-1.96 to +1.96).", "الدرجة +3.45 تتجاوز بكثير النطاق العشوائي المحايد."], "D": ["High Z-scores reflect valid spatial statistics, not data corruption.", "تعبر الدرجات العالية عن إحصاء مكاني سليم وليس تلفاً."]},
        "spatial_stats"
    ),

    # 26: Spatial Autocorrelation (Global Moran's I) Null Hypothesis
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Conceptual", ["Spatial Autocorrelation"],
        "Before conducting local hot spot mapping, an analyst runs the Spatial Autocorrelation (Global Moran's I) tool on property crime rates across a city. The report produces a Z-score of 0.42 and a p-value of 0.67.",
        "قبل رسم البؤر المحلية، شغل محلل أداة الارتباط الذاتي المكاني (Global Moran's I) على معدلات جرائم الأموال في المدينة؛ وأظهر التقرير درجة Z بلغت 0.42 وقيمة p بلغت 0.67.",
        "What does this result conclude regarding the spatial pattern of crimes across the city?",
        "ماذا تستنتج هذه النتيجة بخصوص النمط المكاني للجرائم عبر المدينة؟",
        [["The null hypothesis cannot be rejected; the spatial distribution of crime values is completely random", "لا يمكن رفض الفرضية الصفرية (Null Hypothesis)؛ والتوزيع المكاني لقيم الجرائم عشوائي تماماً"], ["Crimes are strongly clustered in the central business district", "الجرائم متجمعة بقوة في منطقة الأعمال المركزية"], ["Crimes are perfectly dispersed like a checkerboard", "الجرائم مشتتة ومتباعدة بانتظام كلوحة الشطرنج"], ["The crime rate has doubled over the past year", "تضاعف معدل الجريمة خلال العام الماضي"]],
        "A",
        "A Moran's I Z-score near zero (-1.96 < Z < +1.96) and a large p-value (> 0.05) indicates that the null hypothesis (complete spatial randomness) cannot be rejected.",
        "تشير درجة Moran's I المعيارية القريبة من الصفر وقيمة p الكبيرة (أكبر من 0.05) إلى أنه لا يمكن رفض الفرضية الصفرية، مما يؤكد أن النمط المكاني للبيانات عشوائي ولا يظهر تكتلاً أو تشتتاً.",
        {"B": ["Clustering requires positive Z-scores > +1.96 with p < 0.05.", "يتطلب التجمع درجات Z موجبة تتجاوز 1.96 مع p أقل من 0.05."], "C": ["Dispersion requires negative Z-scores < -1.96.", "يتطلب التشتت درجات سالبة تقل عن -1.96."], "D": ["Global Moran's I measures spatial patterns, not temporal crime rate changes.", "يقيس Moran's I النمط المكاني وليس التغير الزمني."]},
        "spatial_stats"
    ),

    # 27: Network Analyst Service Area Solver
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Beginner", "Tool-based", ["Network Analyst"],
        "An emergency medical services agency needs to evaluate ambulance response times. The agency needs to create 4-minute and 8-minute travel catchment polygons radiating outward from 12 paramedic stations along the municipal road network.",
        "تحتاج هيئة إسعاف طوارئ لتقييم أزمنة استجابة سيارات الإسعاف؛ وتريد إنشاء مضلعات نطاقات تغطية زمنية تمتد لـ 4 دقائق و 8 دقائق انطلاقاً من 12 محطة إسعاف عبر شبكة طرق المدينة.",
        "Which Network Analyst solver calculates these travel-time catchment polygons?",
        "أي محلل في Network Analyst يحسب مضلعات نطاقات التغطية الزمنية هذه؟",
        [["Service Area Solver", "محلل نطاق الخدمة (Service Area Solver)"], ["Route Solver", "محلل المسار (Route Solver)"], ["Closest Facility Solver", "محلل أقرب منشأة (Closest Facility Solver)"], ["Location-Allocation Solver", "محلل التخصيص المكاني (Location-Allocation Solver)"]],
        "A",
        "The Service Area solver generates network catchment polygons (isochrones) representing all accessible street segments within specified travel time or distance cutoffs outward from facilities.",
        "ينشئ محلل نطاق الخدمة (Service Area) مضلعات تغطية عبر الشبكة تمثل كافة أجزاء الشوارع التي يمكن الوصول إليها خلال أزمنة انتقال أو مسافات محددة (مثل 4 و 8 دقائق) انطلاقاً من المنشآت.",
        {"B": ["Route Solver finds the optimal path connecting a sequence of stops.", "يحسب Route Solver أفضل مسار يربط بين محطات."], "C": ["Closest Facility finds paths between incidents and facilities.", "يقيس Closest Facility المسارات بين الحوادث وأقرب منشأة."], "D": ["Location-Allocation selects optimal facility sites based on demand.", "يحدد Location-Allocation أفضل مواقع المنشآت."]},
        "network"
    ),

    # 28: Network Analyst Closest Facility Solver
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Network Analyst"],
        "A 911 dispatch center receives an emergency accident report. The dispatch system must instantly find the 3 nearest available police patrol cruisers to the accident site, calculate exact driving times, and output turn-by-turn navigation directions.",
        "تلقى مركز تلقي بلاغات الطوارئ 911 بلاغ حادث؛ ويجب على النظام تحديد أقرب 3 دوريات أمنية لموقع الحادث فوراً، وحساب زمن القيادة الدقيق، وإصدار توجيهات الملاحة خطوة بخطوة.",
        "Which Network Analyst solver solves this incident-to-facility proximity routing problem?",
        "أي محلل في Network Analyst يحل مشكلة قياس القرب وتوجيه المسارات من الحادث إلى المنشآت هذه؟",
        [["Closest Facility Solver", "محلل أقرب منشأة (Closest Facility Solver)"], ["Origin-Destination Cost Matrix Solver", "محلل مصفوفة التكلفة (OD Cost Matrix)"], ["Service Area Solver", "محلل نطاق الخدمة (Service Area)"], ["Multiple Ring Buffer tool", "أداة Multiple Ring Buffer"]],
        "A",
        "The Closest Facility solver measures travel cost between incidents and facilities, identifies the specified number of closest candidates, and generates driving routes and directions.",
        "يقيس محلل أقرب منشأة (Closest Facility) تكلفة الانتقال بين الحوادث والمنشآت، ويحدد العدد المطلوب من أقرب المرشحين، ويولد مسارات القيادة وتوجيهات الانعطاف التفصيلية.",
        {"B": ["OD Cost Matrix outputs a distance/time table without geometric route lines or directions.", "تخرج مصفوفة التكلفة جدول أزمنة دون مسارات أو توجيهات."], "C": ["Service Area generates polygon catchment areas, not routes.", "ينشئ Service Area مضلعات تغطية وليس مسارات."], "D": ["Buffer uses Euclidean straight-line distance, ignoring roads.", "تستخدم Buffer مسافات خطية مستقيمة متجاهلة الطرق."]},
        "network"
    ),

    # 29: Network Analyst Traveling Salesperson Sequence Optimization
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Tool-based", ["Network Analyst"],
        "A municipal water meter inspector must visit 25 homes across town during an 8-hour shift. The inspector starts and ends at the public works depot. The order of visits is flexible, but the total driving time must be minimized.",
        "يجب على مفتش عدادات مياه بلدي زيارة 25 منزلاً في المدينة خلال نوبة عمل من 8 ساعات؛ ويبدأ المفتش من مستودع الأشغال العامة وينتهي فيه؛ وترتيب الزيارات مرن ولكن يجب تقليص زمن القيادة الإجمالي لأدنى حد.",
        "Which Network Analyst capability solves this Traveling Salesperson Problem (TSP)?",
        "أي إمكانية في Network Analyst تحل مسألة البائع المتجول (TSP) لترتيب المحطات هذه؟",
        [["Route Solver with 'Reorder Stops to Find Optimal Route' checked", "محلل المسار (Route Solver) مع تفعيل خيار 'إعادة ترتيب المحطات لإيجاد المسار الأمثل'"], ["Closest Facility Solver", "محلل أقرب منشأة (Closest Facility Solver)"], ["Service Area Solver", "محلل نطاق الخدمة (Service Area Solver)"], ["Generate Near Table", "أداة Generate Near Table"]],
        "A",
        "The Route solver includes a stop reordering capability that solves the Traveling Salesperson Problem, finding the most efficient sequence of intermediate stops between defined start and end points.",
        "يتضمن محلل المسار (Route Solver) ميزة إعادة ترتيب المحطات لحل مسألة البائع المتجول، مما يحدد الترتيب الأكثر كفاءة لزيارة المحطات لتقليص زمن ومسافة القيادة الإجمالية.",
        {"B": ["Closest Facility pairs incidents with facilities, not sequential stops.", "يربط Closest Facility الحوادث بالمنشآت وليس محطات متتالية."], "C": ["Service Area produces travel-time catchment polygons.", "ينشئ Service Area نطاقات زمنية."], "D": ["Generate Near Table produces tabular straight-line distances.", "تنتج Near Table مسافات خطية في جدول."]},
        "network"
    ),

    # 30: Network Analyst Barrier Types
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Intermediate", "Technical", ["Network Analyst"],
        "A city hosts a street marathon that completely closes Main Street for 6 hours, while allowing traffic across an adjacent bridge to continue moving but at a 50% slower speed due to pedestrian spectator congestion.",
        "تستضيف مدينة سباق ماراثون يؤدي للإغلاق التام للشارع الرئيسي لمدة 6 ساعات، مع السماح بمرور حركة السير عبر جسر مجاور ولكن بسرعة أبطأ بنسبة 50% بسبب ازدحام المشاة.",
        "How should these two obstacles be modeled in the Network Analysis layer?",
        "كيف يجب تمثيل هذين العائقين في طبقة التحليل الشبكي؟",
        [["Main Street as a 'Restriction' Barrier, and the bridge as a 'Scaled Cost' Barrier (multiplier = 2.0)", "الشارع الرئيسي كعائق مقيد (Restriction Barrier)، والجسر كعائق تكلفة مدرجة (Scaled Cost Barrier) بمعامل ضرب 2.0"], ["Both as standard Euclidean polygon buffers", "كلاهما كنطاقات مضلعية إقليدية عادية"], ["Both as temporary annotation layers", "كلاهما كطبقات ملاحظات مؤقتة"], ["Delete the street features permanently from the geodatabase", "حذف معالم الشوارع نهائياً من قاعدة البيانات"]],
        "A",
        "Restriction barriers completely prohibit travel across network elements (closed street). Scaled Cost barriers multiply the underlying impedance by a factor (e.g. 2.0x cost = 50% slower speed).",
        "تمنع عوائق التقييد (Restriction) المرور تماماً عبر عناصر الشبكة (الشارع المغلق)؛ بينما تضاعف عوائق التكلفة المدرجة (Scaled Cost) قيمة الإعاقة بمعامل محدد (مثل مضاعفة الزمن بـ 2.0x ليعبر عن هبوط السرعة للنصف).",
        {"B": ["Buffers are geometric circles, not network obstacles.", "النطاقات دوائر هندسية وليست عوائق شبكية."], "C": ["Annotation layers are graphic text labels.", "طبقات الملاحظات نصوص وصفية للعرض."], "D": ["Deleting street features destroys the city network dataset.", "حذف الشوارع يدمر بيانات الشبكة الحيوية."]},
        "network"
    ),

    # 31: ArcGIS Pro Tasks Step Execution Modes
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Tool-based", ["Tasks"],
        "A GIS manager creates an ArcGIS Pro Task to train seasonal interns on digitizing building permits. Step 3 opens the 'Create Features' pane. The manager wants the Task to advance to Step 4 automatically the moment the intern finishes sketching and saves the polygon.",
        "أنشأ مدير نظم معلومات مهمة (Task) في ArcGIS Pro لتدريب المتدربين على رقمنة تصاريح البناء؛ وتقوم الخطوة 3 بفتح نافذة 'Create Features'؛ ويريد المدير انتقال المهمة للخطوة 4 تلقائياً فور قيام المتدرب بإنهاء الرسم وحفظ المضلع.",
        "Which step transition property in the Task Designer configures this automatic advancement?",
        "ما هي خاصية الانتقال في مصمم المهام (Task Designer) التي تفعل هذا الانتقال التلقائي فور إتمام الإجراء؟",
        [["Set Step Execution to 'Auto-Proceed'", "ضبط نمط تنفيذ الخطوة على الانتقال التلقائي 'Auto-Proceed'"], ["Set Step Execution to 'Manual'", "ضبط تنفيذ الخطوة على اليدوي 'Manual'"], ["Lock the user screen with a password", "قفل شاشة المستخدم بكلمة مرور"], ["Convert the project to a web map", "تحويل المشروع إلى خريطة ويب"]],
        "A",
        "In ArcGIS Pro Tasks, 'Auto-Proceed' causes the task engine to advance to the next step automatically as soon as the current step's action or tool completes.",
        "في مهام ArcGIS Pro (Tasks)، يؤدي خيار 'Auto-Proceed' إلى انتقال محرك المهام تلقائياً إلى الخطوة التالية فور اكتمال تنفيذ الإجراء أو الأداة في الخطوة الحالية دون الحاجة لنقر المتدرب على 'Next'.",
        {"B": ["Manual requires the user to click the 'Next Step' button manually.", "يتطلب الوضع اليدوي نقر المستخدم على زر الخطوة التالية."], "C": ["Screen locking is an OS security feature, not a Task setting.", "قفل الشاشة أمان نظام وليس إعداد مهام."], "D": ["Web maps do not control desktop Task steps.", "خرائط الويب لا تدير مهام الديسكتوب."]},
        "tasks"
    ),

    # 32: ArcPy SearchCursor Read Lock and Optimization
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Technical", ["ArcPy"],
        "A Python developer writes an automation script to inspect 200,000 parcels and export delinquent records to a summary report. The script only reads parcel values and must never modify parcel data. Other editors will be editing parcels concurrently.",
        "كتب مبرمج بايثون سكربت أتمتة لفحص 200,000 قطعة أرض واستخراج السجلات المتأخرة في تقرير؛ والسكربت يقرأ البيانات فقط ولا يعدلها مطلقاً؛ ويقوم محررون آخرون بتحرير البيانات في نفس الوقت.",
        "Which data access cursor should the developer implement for fast, read-only performance without placing exclusive locks?",
        "أي مؤشر وصول للبيانات (Cursor) يجب على المطور استخدامه لأداء سريع للقراءة فقط دون فرض أقفال حصرية؟",
        [["arcpy.da.SearchCursor inside a 'with' context manager", "استخدام arcpy.da.SearchCursor داخل مدير السياق 'with'"], ["arcpy.da.UpdateCursor", "استخدام arcpy.da.UpdateCursor"], ["arcpy.da.InsertCursor", "استخدام arcpy.da.InsertCursor"], ["arcpy.CalculateField_management", "أداة arcpy.CalculateField_management"]],
        "A",
        "arcpy.da.SearchCursor provides fast, read-only iteration over feature classes and tables, applying shared read locks that do not block concurrent editor transactions.",
        "يوفر مؤشر arcpy.da.SearchCursor قراءة سريعة ومحسنة للسجلات، ويفرض قفل قراءة مشتركاً لا يعطل ولا يمنع عمليات التحرير المتزامنة للمستخدمين الآخرين.",
        {"B": ["UpdateCursor acquires exclusive locks to write attribute changes.", "يفرض UpdateCursor قفلاً حصرياً لتعديل البيانات."], "C": ["InsertCursor is exclusively for inserting new records.", "يستخدم InsertCursor لإضافة سجلات جديدة فقط."], "D": ["CalculateField modifies attributes in batch, acquiring locks.", "تعدل CalculateField البيانات وتفرض أقفالاً."]},
        "arcpy"
    ),

    # 33: ArcPy UpdateCursor Row Modification Workflow
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Technical", ["ArcPy"],
        "A Python developer loops through utility poles with arcpy.da.UpdateCursor to update the INSPECTION_STATUS field from 'Pending' to 'Completed'. In the loop, the developer writes `row[0] = 'Completed'`. However, when checking the table after script execution, none of the records were updated.",
        "استخدم مبرمج مؤشر arcpy.da.UpdateCursor لتحديث حقل INSPECTION_STATUS من 'Pending' إلى 'Completed'؛ وكتب داخل الحلقة `row[0] = 'Completed'`؛ ولكن عند فحص الجدول بعد تشغيل السكربت، تبين عدم تحديث أي سجل.",
        "What critical method call was omitted inside the cursor loop to commit the changes to the database?",
        "ما هو استدعاء الدالة الحاسم الذي نسيه المبرمج داخل حلقة المؤشر لتثبيت التعديلات في قاعدة البيانات؟",
        [["cursor.updateRow(row)", "استدعاء دالة cursor.updateRow(row)"], ["arcpy.env.overwriteOutput = True", "استدعاء arcpy.env.overwriteOutput = True"], ["arcpy.RefreshTOC()", "استدعاء arcpy.RefreshTOC()"], ["cursor.deleteRow(row)", "استدعاء دالة cursor.deleteRow(row)"]],
        "A",
        "Modifying a cursor row tuple in Python (`row[0] = ...`) only alters the local in-memory object. Changes must be committed to the underlying geodatabase table by calling `cursor.updateRow(row)`.",
        "تعديل مصفوفة السجل في بايثون (`row[0] = ...`) يغير القيمة في ذاكرة بايثون المؤقتة فقط؛ ولحفظ التعديل في جدول قاعدة البيانات يجب استدعاء `cursor.updateRow(row)` صراحة.",
        {"B": ["overwriteOutput controls file replacement on disk, not cursor row edits.", "تتحكم overwriteOutput باستبدال الملفات وليس سطور المؤشر."], "C": ["RefreshTOC refreshes the map table of contents display.", "تحدث RefreshTOC شجرة المحتويات بالخريطة."], "D": ["deleteRow deletes the entire feature from the database.", "تحذف deleteRow المعلم بالكامل من قاعدة البيانات."]},
        "arcpy"
    ),

    # 34: ArcPy InsertCursor Point Creation
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Technical", ["ArcPy"],
        "A script parses an external API stream of real-time GPS coordinates and writes new vehicle tracking breadcrumbs into a point feature class.",
        "يقرأ سكربت بايثون تدفقاً من واجهة API لإحداثيات GPS آنية ويريد كتابة نقاط تتبع المركبات الجديدة في فئة معالم نقطية.",
        "Which cursor and geometry construction syntax correctly appends a new point feature?",
        "أي مؤشر وصيغة بناء هندسي تضيف معلماً نقطياً جديداً بشكل صحيح؟",
        [["arcpy.da.InsertCursor with cursor.insertRow([arcpy.Point(x, y), vehicle_id])", "مؤشر arcpy.da.InsertCursor مع cursor.insertRow([arcpy.Point(x, y), vehicle_id])"], ["arcpy.da.SearchCursor with cursor.insertRow()", "مؤشر arcpy.da.SearchCursor مع cursor.insertRow()"], ["arcpy.da.UpdateCursor with cursor.newRow()", "مؤشر arcpy.da.UpdateCursor مع cursor.newRow()"], ["arcpy.Append_management on a text file", "أداة arcpy.Append_management على ملف نصي"]],
        "A",
        "New rows and features are added using `arcpy.da.InsertCursor`. To insert spatial geometry, pass an `arcpy.Point` or `arcpy.PointGeometry` object in the row list corresponding to the SHAPE@ field.",
        "تتم إضافة السجلات والمعالم الجديدة باستخدام `arcpy.da.InsertCursor`؛ ولإضافة الهندسة المكانية يُمرر كائن `arcpy.Point` في مصفوفة السجل المقابلة لحقل الهندسة SHAPE@.",
        {"B": ["SearchCursor is read-only and lacks an insertRow method.", "SearchCursor للقراءة فقط ولا يملك دالة insertRow."], "C": ["UpdateCursor is for modifying existing rows, not creating new ones.", "UpdateCursor لتعديل السجلات الموجودة وليس لإضافة جديدة."], "D": ["Append requires pre-existing GIS layers.", "تتطلب أداة Append وجود طبقات مكانية مسبقاً."]},
        "arcpy"
    ),

    # 35: arcpy.env.overwriteOutput = True
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Beginner", "Technical", ["ArcPy"],
        "An analyst schedules a nightly Python script to regenerate a citywide road buffer layer: `arcpy.analysis.Buffer('Roads', 'Roads_Buffer50m', '50 Meters')`. On night 2, the script crashes with Geoprocessing Error 000258: 'Output Roads_Buffer50m already exists'.",
        "جدول محلل سكربت بايثون ليلياً لإعادة إنشاء طبقة نطاق الطرق: `arcpy.analysis.Buffer('Roads', 'Roads_Buffer50m', '50 Meters')`؛ وفي الليلة الثانية تعطل السكربت بخطأ المعالجة 000258: 'المخرج موجود بالفعل'.",
        "Which line of code added at the beginning of the script resolves this error permanently?",
        "ما هو سطر الكود الذي إذا أُضيف في بداية السكربت يحل هذا الخطأ بشكل دائم؟",
        [["arcpy.env.overwriteOutput = True", "arcpy.env.overwriteOutput = True"], ["arcpy.env.workspace = 'OVERWRITE'", "arcpy.env.workspace = 'OVERWRITE'"], ["del arcpy", "del arcpy"], ["arcpy.CheckExtension('Spatial') = True", "arcpy.CheckExtension('Spatial') = True"]],
        "A",
        "Setting `arcpy.env.overwriteOutput = True` grants ArcPy permission to automatically overwrite and replace existing datasets on disk, preventing Error 000258 in automated recurring scripts.",
        "يؤدي ضبط `arcpy.env.overwriteOutput = True` إلى منح بايثون الصلاحية لاستبدال وإعادة كتابة الملفات الموجودة مسبقاً على القرص، مما يمنع حدوث الخطأ 000258 في السكربتات المجدولة المتكررة.",
        {"B": ["Workspace specifies database paths, not overwrite permissions.", "تحدد Workspace مسار قاعدة البيانات وليس إذن الاستبدال."], "C": ["del arcpy unloads the module and breaks the script.", "أمر del يحذف مكتبة arcpy من الذاكرة ويعطل البرنامج."], "D": ["CheckExtension checks license availability, not file overwrite.", "تفحص CheckExtension حالة التراخيص وليس استبدال الملفات."]},
        "arcpy"
    ),

    # 36: Script Tool GPFeatureRecordSetLayer Interactive Input
    (
        "Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow", "Intermediate", "Tool-based", ["ArcPy", "Custom Tools"],
        "A GIS developer creates a custom Python Script Tool that calculates wildfire evacuation routes. The developer wants users to be able to click directly on the map to place an interactive incident point, rather than forcing them to pick an existing pre-made layer from disk.",
        "أنشأ مطور نظم معلومات أداة سكربت بايثون مخصصة تحسب مسارات الإخلاء من حرائق الغابات؛ ويريد المطور تمكين المستخدمين من النقر التفاعلي المباشر على الخريطة لوضع نقطة الحادث، بدلاً من إجبارهم على اختيار طبقة جاهزة مخزنة مسبقاً.",
        "Which parameter data type must the developer choose in the Script Tool properties?",
        "ما هو نوع بيانات المعامل (Data Type) الذي يجب على المطور اختياره في خصائص أداة السكربت؟",
        [["Feature Set (GPFeatureRecordSetLayer)", "مجموعة معالم Feature Set (GPFeatureRecordSetLayer)"], ["String", "نص String"], ["Workspace", "مساحة عمل Workspace"], ["Long Integer", "رقم صحيح طويل Long Integer"]],
        "A",
        "The Feature Set data type (GPFeatureRecordSetLayer) enables interactive feature entry, allowing end users to digitize points, lines, or polygons directly on the active map view inside the tool pane.",
        "يتيح نوع البيانات Feature Set (GPFeatureRecordSetLayer) إدخال المعالم تفاعلياً؛ حيث يُمكّن المستخدم من النقر والرسم المباشر للنقاط أو الخطوط أو المضلعات على شاشة الخريطة داخل نافذة الأداة مباشرة.",
        {"B": ["String accepts text input only.", "يقبل نوع String نصوصاً فقط."], "C": ["Workspace accepts folder or geodatabase paths.", "يقبل نوع Workspace مسارات مجلدات فقط."], "D": ["Long Integer accepts numeric integers.", "يقبل Long Integer أرقاماً صحيحة."]},
        "arcpy"
    ),

    # 37: Geoprocessing History Pane Capabilities
    (
        "Given a scenario, determine the appropriate geoprocessing tool", "Beginner", "Tool-based", ["History Pane"],
        "An analyst runs a complicated multi-parameter spatial overlay tool, but the tool fails with an error message. Later, the analyst needs to review the exact parameters that were passed, inspect the full system error log, and copy the equivalent Python code snippet.",
        "شغل محلل أداة تراكب مكاني معقدة متعددة المعاملات، ولكن الأداة فشلت وظهرت رسالة خطأ؛ وفي وقت لاحق، احتاج المحلل لمراجعة المعاملات الدقيقة التي أُدخلت، وفحص سجل رسائل الخطأ التفصيلي، ونسخ كود بايثون المقابل.",
        "Where in ArcGIS Pro is the complete historical record of all tool executions, messages, and Python syntax preserved?",
        "أين يتم الاحتفاظ بالسجل التاريخي الكامل لكافة عمليات تشغيل الأدوات والرسائل وكود بايثون المقابل في ArcGIS Pro؟",
        [["History tab in the Catalog pane (Analysis > History)", "تبويب السجل (History) في نافذة الكتالوج (Analysis > History)"], ["Windows Event Viewer", "سجل أحداث ويندوز Windows Event Viewer"], ["Folder Connections in Catalog", "اتصالات المجلدات في الكتالوج"], ["Layout Properties dialog", "نافذة خصائص لوحة الطباعة Layout Properties"]],
        "A",
        "The Geoprocessing History pane logs every tool execution in the project, displaying start/end times, input/output parameters, warning and error diagnostic messages, and allowing users to copy Python commands or drag tools into ModelBuilder.",
        "تسجل نافذة تاريخ المعالجة الجغرافية (History) كافة الأدوات المنفذة في المشروع، وتعرض أوقات التشغيل والمعاملات والرسائل التحذيرية وأخطاء النظام، وتتيح نسخ أوامر بايثون المقابلة أو سحب الأداة مباشرة إلى ModelBuilder.",
        {"B": ["Windows Event Viewer logs OS events, not ArcGIS Pro GP parameters.", "يسجل عارض أحداث ويندوز أحداث نظام التشغيل وليس معاملات الأدوات."], "C": ["Folder Connections manages directory links on disk.", "تدير اتصالات المجلدات روابط الملفات."], "D": ["Layout Properties manages print margins and canvas sizes.", "تدير خصائص اللوحة أبعاد الطباعة وهوامش الصفحة."]},
        "tasks"
    )
]

items = []
for i, item in enumerate(scenarios_data):
    qid = f"AGP-S-{i+1:03d}"
    items.append(s(qid, item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]))

print(f"Total AGP Scenarios: {len(items)} (target 37)")

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Saved scenarios/analysis-geoprocessing.json successfully.")
