# -*- coding: utf-8 -*-
"""
Generate all 48 Data Management Scenarios (DM-S-001 through DM-S-048) for EAPA_2025.
"""
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_file = os.path.join(base_dir, 'public', 'data', 'scenarios', 'data-management.json')

ref_map = {
    "gdb": {"title": "Geodatabase architecture and schema design, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-file-gdb/file-geodatabases.htm", "kind": "official"},
    "domains": {"title": "Subtypes and attribute domains, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-file-gdb/subtypes.htm", "kind": "official"},
    "topology": {"title": "Geodatabase topology and error inspection, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-file-gdb/topology-in-arcgis.htm", "kind": "official"},
    "rules": {"title": "Attribute rules for data integrity, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-file-gdb/an-overview-of-attribute-rules.htm", "kind": "official"},
    "coords": {"title": "Map projections and coordinate systems, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/specify-a-coordinate-system.htm", "kind": "official"},
    "editing": {"title": "Editing workflows and tools, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/overview-of-desktop-editing.htm", "kind": "official"},
    "geocoding": {"title": "Geocoding and locators, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geocoding/what-is-geocoding-.htm", "kind": "official"},
    "linear": {"title": "Linear referencing and dynamic segmentation, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/an-overview-of-linear-referencing.htm", "kind": "official"}
}

def s(sid, obj, diff, qtype, tools, ctx_en, ctx_ar, q_en, q_ar, opts, ans, exp_en, exp_ar, why, rkey):
    return {
        "id": sid,
        "kind": "scenario",
        "domain": "Data Management",
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

items = []

# 1
items.append(s(
    "DM-S-001", "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes", "Intermediate", "Troubleshooting",
    ["Split", "Split Policy"],
    "A municipal tax department splits a 20-acre commercial parcel with an assessed value of $1,000,000 into two equal 10-acre parcels using the Split editing tool. After saving edits, the attribute table shows that both new parcels list an assessed value of $1,000,000 each, artificially doubling the recorded value on the tax roll.",
    "قام قسم الضرائب العقارية بتقسيم قطعة أرض تجارية مساحتها 20 فداناً وقيمتها التقديرية 1,000,000 دولار إلى قطعتين متساويتين (10 أفدنة لكل منهما) باستخدام أداة Split. بعد حفظ التعديلات، أظهر جدول البيانات أن كلا القطعتين تحملان قيمة 1,000,000 دولار، مما ضاعف القيمة المسجلة.",
    "What geodatabase configuration error caused this duplicate valuation?",
    "ما هو خطأ تهيئة قاعدة البيانات الجغرافية الذي تسبب في هذه القيمة المكررة؟",
    [["The Split Policy for the assessed value field was set to Duplicate instead of Geometry Ratio", "كانت سياسة التقسيم (Split Policy) لحقل القيمة التقديرية مضبوطة على Duplicate بدلاً من Geometry Ratio"], ["The feature class was missing an attribute index", "كانت فئة المعالم تفتقر إلى فهرس سماتي"], ["The map coordinate system was set to WGS 1984 Web Mercator", "كان نظام إحداثيات الخريطة مضبوطاً على WGS 1984 Web Mercator"], ["Branch versioning was not enabled on the geodatabase", "لم يتم تفعيل التفريع النسخي على قاعدة البيانات"]],
    "A",
    "A field's Split Policy dictates attribute behavior when a feature is cut. The 'Duplicate' policy copies the original value into all resultant parts, whereas 'Geometry Ratio' divides the value proportionally based on the resulting area ratios.",
    "تحدد سياسة التقسيم (Split Policy) سلوك القيم عند قطع المعلم؛ وتنسخ سياسة Duplicate القيمة الأصلية بالكامل لكل جزء ناتج، بينما تقسم سياسة Geometry Ratio القيمة تناسبياً بحسب مساحة كل قطعة ناتجة.",
    {"B": ["Attribute indexes optimize search query speeds and do not govern editing split behaviors.", "الفهارس السماتية تسرع الاستعلامات ولا تتحكم في سلوك التقسيم."], "C": ["Coordinate projections do not alter attribute split policies.", "أنظمة الإحداثيات لا تغير سياسات تقسيم السمات."], "D": ["Branch versioning manages multi-user editing concurrency, not attribute division logic.", "التفريع النسخي يدير التزامن التحريري ولا يقسم السمات."]},
    "domains"
))

# 2
items.append(s(
    "DM-S-002", "Manage coordinate systems to preserve the desired spatial properties", "Beginner", "Troubleshooting",
    ["Define Projection"],
    "A GIS technician imports a civil engineering CAD drawing (.dwg) containing water mains into ArcGIS Pro. When added to the map, a warning appears stating 'Unknown Coordinate System'. Examining the layer extent reveals coordinate numbers such as X: 2,154,320 and Y: 685,410, which exactly match the local State Plane coordinate system in US Survey Feet.",
    "استورد فني GIS رسم CAD هندسي (.dwg) لشبكات مياه إلى ArcGIS Pro، وظهر تحذير 'نظام إحداثيات غير معروف'. وبفحص نطاق الطبقة تبين أن الأرقام مثل X: 2,154,320 و Y: 685,410 تتطابق تماماً مع نظام State Plane المحلي بالأقدام المساحية الأمريكية.",
    "What should the technician do to correctly register this dataset in ArcGIS Pro?",
    "ما الذي يجب على الفني فعله لتسجيل هذه البيانات بشكل صحيح في ArcGIS Pro؟",
    [["Run the Define Projection tool and assign the matching State Plane Projected Coordinate System", "تشغيل أداة Define Projection وتعيين نظام الإحداثيات المسقط State Plane المطابق"], ["Run the Project tool to reproject the dataset to WGS 1984", "تشغيل أداة Project لإعادة إسقاط البيانات إلى WGS 1984"], ["Change the Windows system locale to United States", "تغيير إعدادات المنطقة لنظام تشغيل ويندوز إلى الولايات المتحدة"], ["Delete the CAD file and request a shapefile instead", "حذف ملف CAD وطلب ملف shapefile بدلاً منه"]],
    "A",
    "The coordinates already physically exist in the correct coordinate space; only the metadata definition (.prj) is missing. Define Projection assigns the coordinate system definition without altering the coordinate values.",
    "الإحداثيات الفعلية موجودة بالفعل بالنظام الصحيح، والمفقود هو ملف التعريف (.prj) فقط؛ لذا تُستخدم أداة Define Projection لتعريف النظام دون المساس بأرقام الإحداثيات.",
    {"B": ["Running Project on an Unknown coordinate system produces invalid transformed data.", "تشغيل Project على نظام غير معروف ينتج بيانات مشوهة."], "C": ["Operating system regional locale does not define GIS projections.", "إعدادات نظام التشغيل لا تعرف الإسقاط."], "D": ["CAD files are fully supported natively in ArcGIS Pro.", "ملفات CAD مدعومة بالكامل في البرنامج."]},
    "coords"
))

# 3
items.append(s(
    "DM-S-003", "Given a scenario, determine the appropriate existing geodatabase elements to use", "Intermediate", "Workflow-based",
    ["Subtypes", "Coded Value Domain"],
    "A water utility maintains a single line feature class named Water_Mains. Transmission mains must only allow pipe diameters of 16, 24, 36, and 48 inches. Distribution mains must only allow diameters of 4, 6, 8, and 12 inches. Field workers must be prevented from entering invalid diameters.",
    "تدير شركة مياه فئة معالم خطية واحدة باسم Water_Mains. خطوط النقل الرئيسية يجب أن تسمح فقط بأقطار 16 و 24 و 36 و 48 بوصة؛ بينما خطوط التوزيع يجب أن تسمح فقط بأقطار 4 و 6 و 8 و 12 بوصة. ويجب منع العاملين من إدخال أقطار خاطئة.",
    "How should the geodatabase schema be architected to enforce this requirement within a single feature class?",
    "كيف يجب تصميم مخطط قاعدة البيانات لفرض هذا المتطلب داخل فئة معالم واحدة؟",
    [["Configure Subtypes on a Pipe_Type integer field, and assign distinct Coded Value Domains for diameter to each subtype", "تهيئة تصنيفات فرعية (Subtypes) على حقل Pipe_Type، وتعيين نطاقات قيم مشفرة (Domains) مختلفة للقطر لكل تصنيف"], ["Create two separate feature classes and link them with a relationship class", "إنشاء فئتي معالم منفصلتين وربطهما بفئة علاقة"], ["Configure a single Range Domain from 4 to 48 on the diameter field", "تهيئة نطاق مدى واحد (Range Domain) من 4 إلى 48 على حقل القطر"], ["Add an attribute rule in Python to restart the database on invalid edits", "إضافة قاعدة سمات ببايثون لإعادة تشغيل قاعدة البيانات عند الخطأ"]],
    "A",
    "Subtypes allow a single feature class to categorize features and assign unique default values and distinct Coded Value Domains to other fields based on the subtype category.",
    "تتيح التصنيفات الفرعية (Subtypes) تصنيف معالم الطبقة الواحدة وتعيين قيم افتراضية ونطاقات قيم مشفرة (Coded Value Domains) مستقلة لكل تصنيف على حدة لضبط جودة الإدخال.",
    {"B": ["Splitting into multiple feature classes creates unnecessary data fragmentation.", "تجزئة البيانات لفئات متعددة يسبب تشتت البيانات."], "C": ["A single range domain allows transmission pipes to mistakenly receive 4-inch diameters.", "نطاق المدى الواحد يسمح باختيار أقطار غير مناسبة لنوع الخط."], "D": ["Attribute rules run Arcade, not Python database restart scripts.", "قواعد السمات تعمل بـ Arcade ولا تعيد تشغيل الخوادم."]},
    "domains"
))

# 4
items.append(s(
    "DM-S-004", "Given a scenario, determine the appropriate existing geodatabase elements to use", "Intermediate", "Technical",
    ["Attribute Rules"],
    "A municipal gas pipeline operator requires that whenever an editor creates or edits a valve feature, the system must immediately reject the transaction, roll back the edit, and display an error message if the recorded pressure exceeds the maximum rated pressure of the connected pipe.",
    "تتطلب شركة أنابيب غاز أنه عند إنشاء أو تعديل محبس، يجب على النظام رفض العملية فوراً والتراجع عن التعديل وعرض رسالة خطأ للمحرر إذا تجاوز الضغط المسجل الحد الأقصى المسموح به للأنبوب المتصل.",
    "Which type of Geodatabase Attribute Rule must be implemented?",
    "أي نوع من قواعد السمات (Attribute Rules) في قاعدة البيانات الجغرافية يجب تطبيقه؟",
    [["Constraint Attribute Rule", "قاعدة سمات مقيدة (Constraint Attribute Rule)"], ["Calculation Attribute Rule (Immediate)", "قاعدة سمات حسابية فورية (Immediate Calculation)"], ["Validation Attribute Rule", "قاعدة سمات تحققية (Validation Attribute Rule)"], ["Batch Calculation Attribute Rule", "قاعدة سمات حسابية مجمعة (Batch Calculation)"]],
    "A",
    "Constraint rules evaluate Arcade expressions during the edit operation; if the expression evaluates to false, the edit is completely blocked, the transaction is rolled back, and a custom error message is presented.",
    "تُقيم قواعد القيد (Constraint Rules) تعبيرات Arcade أثناء عملية التحرير مباشرة؛ وإذا كانت النتيجة False، يتم حظر التعديل كلياً والتراجع عن المعاملة وإظهار رسالة خطأ مخصصة.",
    {"B": ["Calculation rules populate field values, they do not block invalid transactions.", "القواعد الحسابية تملأ قيم الحقول ولا تحظر المعاملات."], "C": ["Validation rules evaluate asynchronously via the Error Inspector without blocking the edit.", "قواعد التحقق تُقيم لاحقاً في Error Inspector دون منع الحفظ."], "D": ["Batch calculation runs on demand across multiple rows.", "الحساب المجمع يعمل عند الطلب ولا يحظر الإدخال المباشر."]},
    "rules"
))

# 5
items.append(s(
    "DM-S-005", "Given a scenario, determine the appropriate existing geodatabase elements to use", "Intermediate", "Troubleshooting",
    ["Geodatabase Topology"],
    "A county tax assessor's office requires that parcel boundaries must fit together seamlessly like a puzzle: no parcel polygon may overlap another, and no unintended empty gaps may exist between adjacent lots.",
    "يتطلب مكتب التقييم العقاري تطابق حدود قطع الأراضي بسلاسة كقطع الأحجية: لا يجوز لأي مضلع أرض التداخل مع آخر، ولا يجوز وجود فجوات فراغية بين القطع المتجاورة.",
    "Which pair of Geodatabase Topology rules should be created inside the parcel feature dataset?",
    "أي زوج من قواعد طوبولوجيا قاعدة البيانات الجغرافية يجب إنشاؤه داخل مجموعة بيانات الأراضي؟",
    [["'Must Not Overlap' and 'Must Not Have Gaps'", "'Must Not Overlap' و 'Must Not Have Gaps'"], ["'Point Must Be Covered By Line' and 'Must Not Self-Intersect'", "'Point Must Be Covered By Line' و 'Must Not Self-Intersect'"], ["'Must Be Inside' and 'Contains Point'", "'Must Be Inside' و 'Contains Point'"], ["'Must Be Larger Than 1 Acre' and 'Snap to Road'", "'Must Be Larger Than 1 Acre' و 'Snap to Road'"]],
    "A",
    "For cadastral parcel fabrics and parcel boundaries, 'Must Not Overlap' prevents overlapping property claims and 'Must Not Have Gaps' flags slivers and unmapped voids between lots.",
    "لقطع الأراضي المساحية، تمنع قاعدة 'Must Not Overlap' نزاعات الملكية الناتجة عن التداخل، وتكتشف قاعدة 'Must Not Have Gaps' الفجوات والشرائح غير الممسوحة بين القطع.",
    {"B": ["Point rules do not apply to polygon parcel boundaries.", "قواعد النقاط لا تنطبق على مضلعات الأراضي."], "C": ["These are not standard geodatabase topology rule names.", "ليست أسماء قواعد طوبولوجيا قياسية."], "D": ["Acreage thresholds are attribute constraints, not spatial topology rules.", "حدود المساحات قيود سمات وليست قواعد طوبولوجيا مكانية."]},
    "topology"
))

# 6
items.append(s(
    "DM-S-006", "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes", "Intermediate", "Tool-based",
    ["Error Inspector"],
    "During topology validation of a city road centerline layer with the rule 'Must Not Have Dangles', cul-de-sacs (dead-end streets) are correctly flagged as dangle errors. However, cul-de-sacs are legitimate design features that should remain unconnected.",
    "أثناء التحقق الطوبولوجي من طبقة محاور شوارع المدينة بقاعدة 'Must Not Have Dangles'، تم وضع علامة خطأ تعليق (Dangle) على الشوارع المسدودة (Cul-de-sacs)، مع أنها شوارع مصممة نظامياً كنهايات مغلقة.",
    "How should the GIS technician resolve these valid dead-end streets in the Error Inspector pane?",
    "كيف يجب على فني نظم المعلومات الجغرافية معالجة هذه الشوارع المسدودة النظامية في نافذة Error Inspector؟",
    [["Mark each valid dead-end street error as an Exception", "تمييز كل خطأ شارع مسدود نظامي كاستثناء (Mark as Exception)"], ["Delete the cul-de-sac features from the road network", "حذف معالم الشوارع المسدودة من شبكة الطرق"], ["Extend the dead ends until they cross a highway", "مد نهايات الشوارع المسدودة حتى تقطع طريقاً سريعاً"], ["Delete the geodatabase topology permanently", "حذف طوبولوجيا قاعدة البيانات نهائياً"]],
    "A",
    "In ArcGIS Pro topology management, real-world conditions that intentionally violate a rule (like genuine cul-de-sacs under a dangle rule) should be marked as Exceptions in the Error Inspector so they are excluded from future error reports.",
    "في إدارة الطوبولوجيا، تُعتبر الحالات الواقعية المصممة عمداً كاستثناءات (مثل النهايات المسدودة الطبيعية) معالم صحيحة؛ ويجب تمييزها كاستثناء (Mark as Exception) لإخفائها من تقارير الأخطاء اللاحقة.",
    {"B": ["Deleting valid streets destroys accurate transportation inventory.", "حذف الشوارع النظامية يدمر بيانات شبكة النقل."], "C": ["Artificially extending streets invents false geographic connections.", "مد الشوارع بشكل وهمي يختلق بيانات مضللة."], "D": ["Deleting topology removes quality control for the entire network.", "حذف الطوبولوجيا يلغي مراقبة الجودة عن كامل الشبكة."]},
    "topology"
))

# 7
items.append(s(
    "DM-S-007", "Given a scenario, determine the appropriate existing geodatabase elements to use", "Intermediate", "Technical",
    ["Contingent Values"],
    "An electric utility models utility poles. If Pole_Material is 'Wood', the Pole_Height field must only offer 30, 35, and 40 feet, and Pole_Class must offer 1, 2, and 3. If Pole_Material is 'Steel', Pole_Height must offer 60, 80, and 100 feet, and Pole_Class must offer A, B, and C.",
    "تدير شركة كهرباء أعمدة الإنارة. إذا كانت مادة العمود 'Wood'، يجب أن يقدم حقل الارتفاع خيارات 30 و 35 و 40 قدماً فقط، وحقل الفئة 1 و 2 و 3. وإذا كانت المادة 'Steel'، يجب أن يقدم الارتفاع 60 و 80 و 100 قدم، والفئة A و B و C.",
    "Which geodatabase feature capability configures interdependent drop-down domain lists across multiple related fields?",
    "أي ميزة في قاعدة البيانات الجغرافية تُهيئ قوائم منسدلة مترابطة ومرتهنة ببعضها عبر عدة حقول سماتية؟",
    [["Contingent Values (Field Groups)", "القيم المشروطة Contingent Values (مجموعات الحقول Field Groups)"], ["Subtypes alone without domains", "التصنيفات الفرعية بمفردها دون نطاقات"], ["Simple Relationship Class", "فئة علاقة بسيطة Simple Relationship Class"], ["Raster Mosaic Dataset", "مجموعة بيانات موزاييك راستر"]],
    "A",
    "Contingent Values create field groups where valid choices in secondary fields depend directly on the value selected in primary fields, preventing invalid combinations during editing.",
    "تنشئ القيم المشروطة (Contingent Values) مجموعات حقول مترابطة بحيث ترتهن الخيارات المتاحة في الحقول التابعة بالقيمة المختارة في الحقل الرئيسي، مما يمنع المدخلات غير المتوافقة.",
    {"B": ["Subtypes only branch on a single integer field, not multi-tier dependent choices.", "التصنيفات الفرعية تعتمد على حقل واحد فقط ولا تدعم اختيارات متسلسلة متعددة."], "C": ["Relationship classes link distinct tables, they do not filter in-line field domains.", "فئات العلاقات تربط جداول مستقلة ولا تدير قوائم منسدلة."], "D": ["Mosaic datasets manage imagery collections.", "مجموعات الموزاييك مخصصة للصور الفضائية."]},
    "domains"
))

# 8
items.append(s(
    "DM-S-008", "Manage geospatial data (raster, vector, tabular)", "Beginner", "Tool-based",
    ["Compact"],
    "An editor deletes 250,000 obsolete records from a large File Geodatabase table. However, checking Windows File Explorer reveals that the .gdb directory size on disk has not decreased at all.",
    "قام محرر بحذف 250,000 سجل قديم من جدول كبير في File Geodatabase؛ ولكن عند فحص حجم مجلد .gdb في متصفح ملفات ويندوز تبين أن المساحة المستهلكة على القرص لم تنقص إطلاقاً.",
    "Which tool must be executed to reclaim the unused disk space and reorganize internal database storage?",
    "أي أداة يجب تشغيلها لاستعادة المساحة الفارغة غير المستخدمة على القرص وإعادة تنظيم التخزين الداخلي لقاعدة البيانات؟",
    [["Compact", "Compact (ضغط وتنسيق قاعدة البيانات)"], ["Add Global IDs", "Add Global IDs"], ["Enable Archiving", "Enable Archiving"], ["Register As Versioned", "Register As Versioned"]],
    "A",
    "The Compact tool cleans up fragmented storage in file and mobile geodatabases, freeing unused disk space left behind after extensive deletes and edits, and rebuilds spatial and attribute indexes.",
    "تقوم أداة Compact بتنظيف التخزين المجزأ واستعادة المساحات الفارغة غير المستخدمة بعد عمليات الحذف الضخمة، وتعيد ترتيب السجلات وبناء الفهارس لتحسين الأداء وتقليص الحجم.",
    {"B": ["Global IDs add unique identifier columns.", "تضيف Global IDs أعمدة معرفات فريدة."], "C": ["Enable Archiving logs historical edits, which actually increases database size.", "تفعيل الأرشفة يسجل التغييرات ويزيد حجم القاعدة."], "D": ["Register As Versioned enables multi-user versioning.", "التسجيل بإصدارات يدير التحرير التشاركي."]},
    "gdb"
))

# 9
items.append(s(
    "DM-S-009", "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Troubleshooting",
    ["Repair Geometry"],
    "An analyst attempts to calculate polygon area using Calculate Field, but the tool fails with an error indicating 'Self-intersection' and 'Null geometry' in several features.",
    "حاول محلل حساب مساحة مضلعات باستخدام أداة Calculate Field، لكن الأداة فشلت وظهرت رسالة خطأ تفيد بوجود 'تقاطع ذاتي' (Self-intersection) وهندسة فارغة (Null geometry) في عدة معالم.",
    "Which tool should be run to inspect and automatically fix these invalid geometric vertices in the feature class?",
    "أي أداة يجب تشغيلها لفحص وإصلاح هذه الرؤوس الهندسية غير الصالحة تلقائياً في فئة المعالم؟",
    [["Repair Geometry", "Repair Geometry (إصلاح الهندسة)"], ["Project", "Project (إعادة الإسقاط)"], ["Add Field", "Add Field (إضافة حقل)"], ["Calculate Geometry Attributes", "Calculate Geometry Attributes"]],
    "A",
    "Repair Geometry modifies invalid geometries in-place, fixing self-intersections, removing null vertices, and correcting incorrect exterior/interior ring orientations.",
    "تعدل أداة Repair Geometry المعالم المعطوبة مباشرة في مكانها، فتصلح التقاطعات الذاتية وتحذف الرؤوس الفارغة وتصحح اتجاهات الحلقات الداخلية والخارجية للمضلعات.",
    {"B": ["Project transforms coordinate systems and will fail or corrupt invalid geometries.", "أداة Project ستفشل مع المعالم ذات الهندسة الفاسدة."], "C": ["Add Field creates new table columns.", "إضافة حقل تنشئ عموداً جديداً."], "D": ["Calculate Geometry Attributes calculates properties on valid geometries.", "حساب السمات الهندسية يتطلب هندسة سليمة أولاً."]},
    "editing"
))

# 10
items.append(s(
    "DM-S-010", "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Workflow-based",
    ["Make Route Event Layer"],
    "A Department of Transportation maintains a highway polyline layer calibrated with M-values representing mileposts. An Excel spreadsheet contains accident logs with fields: HIGHWAY_ID, MILEPOST, and ACCIDENT_SEVERITY.",
    "تدير وزارة النقل طبقة محاور طرق سريعة معايرة بقيم M تمثل علامات الأميال (Mileposts). ويحتوي جدول إكسل على سجلات الحوادث بحقول: HIGHWAY_ID، و MILEPOST، و ACCIDENT_SEVERITY.",
    "Which tool dynamically plots these accident locations along the highway lines based on their milepost values without requiring X/Y coordinates?",
    "أي أداة تسقط مواقع هذه الحوادث ديناميكياً على طول مسارات الطرق بالاعتماد على قيم علامات الأميال دون الحاجة لإحداثيات X و Y؟",
    [["Make Route Event Layer", "Make Route Event Layer"], ["XY Table To Point", "XY Table To Point"], ["Spatial Join", "Spatial Join"], ["Geocode Addresses", "Geocode Addresses"]],
    "A",
    "Make Route Event Layer matches route identifiers and measure values (M-values) from an event table against a measured route layer to dynamically generate point or line features (dynamic segmentation).",
    "تطابق أداة Make Route Event Layer معرفات الطرق وقيم المقاييس (قيم M) من جدول الأحداث مع طبقة المسارات المعايرة لتوليد معالم نقطية أو خطية ديناميكياً (التجزئة الديناميكية).",
    {"B": ["XY Table To Point requires explicit X/Y Cartesian coordinates.", "تتطلب XY Table To Point إحداثيات X و Y صريحة."], "C": ["Spatial Join requires pre-existing spatial geometries.", "يتطلب Spatial Join وجود هندسة مكانية مسبقة."], "D": ["Geocode Addresses requires street address text and locators.", "تتطلب Geocode Addresses عناوين نصية ومحدد مواقع."]},
    "linear"
))

# Let's add 38 more scenarios to complete all 48 Data Management scenarios!
# We will define a loop with concise data tuples where every tuple has:
# (obj, diff, qtype, tools, ctx_en, ctx_ar, q_en, q_ar, opts, ans, exp_en, exp_ar, why, rkey)
remaining_scenarios = [
    # 11
    (
        "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Technical", ["Create Feature Dataset"],
        "An analyst attempts to import a parcel shapefile projected in State Plane NAD 1983 into an existing Feature Dataset whose spatial reference is defined as UTM Zone 15N. The import tool throws a schema conflict error.",
        "حاول محلل استيراد ملف shapefile لقطع الأراضي مسقط بنظام State Plane NAD 1983 إلى Feature Dataset معرف بنظام UTM Zone 15N، ففشلت الأداة وظهر خطأ تعارض في المخطط.",
        "What is the cause of this error in ArcGIS Pro?",
        "ما هو سبب هذا الخطأ في ArcGIS Pro؟",
        [["All feature classes inside a Feature Dataset MUST share the exact same coordinate system and spatial reference", "يجب أن تشترك كافة فئات المعالم داخل Feature Dataset في نفس نظام الإحداثيات والمرجع المكاني تماماً"], ["Shapefiles cannot be imported into geodatabases", "لا يمكن استيراد ملفات shapefile إلى الجيوداتابيس"], ["Feature datasets only support raster data", "تدعم Feature datasets بيانات الراستر فقط"], ["The analyst's computer has insufficient RAM", "ذاكرة الحاسوب RAM غير كافية"]],
        "A",
        "A Feature Dataset enforces a common spatial reference. Every dataset inside must share identical coordinate system, resolution, and tolerance values.",
        "تفرض مجموعة بيانات المعالم (Feature Dataset) مرجعاً مكانياً موحداً؛ لذا يجب أن تتطابق جميع فئات المعالم بداخلها في نظام الإحداثيات وقيم الدقة والتسامح.",
        {"B": ["Shapefiles can be imported into geodatabases seamlessly.", "يمكن استيراد ملفات shapefile بسهولة."], "C": ["Feature datasets only hold vector feature classes.", "تحتوي مجموعات البيانات على معالم اتجاهية فقط."], "D": ["Schema rules are enforced by software logic, not RAM.", "قواعد المخطط يفرضها البرنامج ولا علاقة لها بالذاكرة."]},
        "gdb"
    ),
    # 12
    (
        "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Workflow-based", ["Rematch Addresses"],
        "After geocoding a table of 10,000 customer addresses against a composite locator, 350 addresses receive an 'Unmatched' status due to misspelled street names and missing postal codes.",
        "بعد تكويد جدول يحتوي على 10,000 عنوان عميل جغرافياً عبر محدد مواقع مركب، حصل 350 عنواناً على حالة 'Unmatched' بسبب أخطاء إملائية في أسماء الشوارع وغياب الرموز البريدية.",
        "What interface in ArcGIS Pro provides an interactive environment to review candidate matches, correct addresses, and match remaining records?",
        "ما هي الواجهة في ArcGIS Pro التي توفر بيئة تفاعلية لمراجعة العناوين المرشحة وتصحيح العناوين ومطابقة السجلات المتبقية؟",
        [["Rematch Addresses pane", "نافذة إعادة مطابقة العناوين Rematch Addresses"], ["Error Inspector pane", "نافذة Error Inspector"], ["Topology Properties dialog", "نافذة خصائص الطوبولوجيا"], ["Catalog Options", "خيارات الكتالوج"]],
        "A",
        "The Rematch Addresses pane allows filtering by status (Unmatched, Tied, Matched), reviewing candidate scores, manually correcting address text, and picking matched locations.",
        "تتيح نافذة Rematch Addresses تصفية العناوين بحسب حالتها (غير مطابقة، متعادلة، مطابقة)، واستعراض درجات المرشحين وتصحيح الأخطاء الإملائية وتأكيد المطابقة.",
        {"B": ["Error Inspector reviews topology errors, not geocoding results.", "نافذة Error Inspector خاصة بأخطاء الطوبولوجيا."], "C": ["Topology properties configure geometric rules.", "خصائص الطوبولوجيا لضبط القواعد المكانية."], "D": ["Catalog options manage project settings.", "خيارات الكتالوج تدير إعدادات المشروع."]},
        "geocoding"
    ),
    # 13
    (
        "Manage geospatial data (raster, vector, tabular)", "Beginner", "Tool-based", ["Enable Attachments"],
        "A building inspection department needs inspectors using mobile tablets to take multiple on-site photos of building violations and attach them directly to the corresponding parcel feature.",
        "يحتاج قسم تفتيش المباني لتمكين المفتشين الميدانيين عبر الأجهزة اللوحية من التقاط صور متعددة لمخالفات البناء وإرفاقها مباشرة بالمعلم الجغرافي المقابل لقطعة الأرض.",
        "What tool must be run on the parcel feature class to enable storing photo files?",
        "أي أداة يجب تشغيلها على فئة معالم قطع الأراضي لتمكين تخزين ملفات الصور المرفقة؟",
        [["Enable Attachments", "Enable Attachments (تفعيل المرفقات)"], ["Add Field of type Date", "إضافة حقل من نوع Date"], ["Export Features", "Export Features"], ["Compact", "Compact"]],
        "A",
        "Enable Attachments creates an attachment table (_ATTACH) and a composite relationship class linking features to multiple photos, documents, and media files.",
        "تنشئ أداة Enable Attachments جدول مرفقات مستقل وفئة علاقة مركبة تربط كل معلم بصور وملفات متعددة في قاعدة البيانات.",
        {"B": ["Date fields store timestamps, not binary photos.", "حقول التاريخ تخزن تواريخ وليس صوراً."], "C": ["Export Features copies data.", "تصدير المعالم ينسخ البيانات."], "D": ["Compact defragments disk space.", "أداة Compact تنظف المساحات الفارغة."]},
        "gdb"
    ),
    # 14
    (
        "Given a scenario, determine the appropriate existing geodatabase elements to use", "Intermediate", "Technical", ["Attribute Rules"],
        "Whenever a technician creates a new water meter point in ArcGIS Pro, the system must automatically populate its 'MUNICIPALITY' attribute field by performing a spatial query against an underlying city boundaries polygon layer.",
        "كلما أنشأ فني نقطة عداد مياه جديدة في ArcGIS Pro، يجب على النظام ملء حقل 'MUNICIPALITY' تلقائياً بإجراء استعلام مكاني على طبقة حدود البلديات الواقعة أسفل النقطة.",
        "Which type of Attribute Rule and Arcade feature-set function should be configured?",
        "أي نوع من القواعد السماتية ودوال Arcade لمجموعات المعالم يجب إعداده؟",
        [["Immediate Calculation Attribute Rule using FeatureSetByName() and Intersects()", "قاعدة حسابية فورية (Immediate Calculation) باستخدام دالتي FeatureSetByName() و Intersects()"], ["Constraint Attribute Rule using Length()", "قاعدة مقيدة باستخدام دالة Length()"], ["Validation Attribute Rule using AreaGeodetic()", "قاعدة تحقق باستخدام دالة AreaGeodetic()"], ["Topology rule 'Must Not Overlap'", "قاعدة طوبولوجيا 'Must Not Overlap'"]],
        "A",
        "Immediate Calculation rules execute during feature creation. Using FeatureSetByName($datastore, 'Cities') and Intersects() queries intersecting boundary attributes and populates the field instantly.",
        "تنفذ القواعد الحسابية الفورية (Immediate Calculation) عند إنشاء المعلم؛ وتتيح دالتا FeatureSetByName و Intersects استعلام بيانات مضلع البلدية المتقاطع وحفظ اسمه تلقائياً في حقل النقطة.",
        {"B": ["Constraint rules evaluate boolean conditions to block edits.", "قواعد القيد تقيم شروطاً منطقية لمنع التعديل."], "C": ["Validation rules evaluate asynchronously in batch.", "قواعد التحقق تعمل بشكل مجمع لاحقاً."], "D": ["Topology rules manage vector geometry coincident borders, not attribute transfer.", "قواعد الطوبولوجيا تدير الحدود الهندسية وليس نقل البيانات."]},
        "rules"
    ),
    # 15
    (
        "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes", "Intermediate", "Conceptual", ["Map Topology"],
        "An analyst needs to quickly move a shared boundary line between two zoning polygons in a standalone shapefile during an active edit session without creating a feature dataset or setting up persistent geodatabase rules.",
        "يحتاج محلل لتحريك حد مشترك سريعاً بين مضلعي مخطط هيكلي في ملف shapefile مستقل أثناء جلسة تحرير، دون الحاجة لإنشاء Feature Dataset أو ضبط قواعد جيوداتابيس معقدة.",
        "Which editing capability should the analyst activate on the Edit ribbon?",
        "أي ميزة تحرير يجب على المحلل تفعيلها في شريط التحرير (Edit Ribbon)؟",
        [["Map Topology", "طوبولوجيا الخريطة (Map Topology)"], ["Geodatabase Topology", "طوبولوجيا قاعدة البيانات (Geodatabase Topology)"], ["Branch Versioning", "التفريع النسخي (Branch Versioning)"], ["Raster Snapping", "انجذاب الراستر (Raster Snapping)"]],
        "A",
        "Map Topology allows editors to edit shared edges and vertices across coincident layers on-the-fly during an edit session without requiring geodatabase topology setups, working on shapefiles and CAD as well.",
        "تتيح طوبولوجيا الخريطة (Map Topology) للمحررين تعديل الحواف والرؤوس المشتركة بين الطبقات المتطابقة آنياً أثناء جلسة التحرير دون الحاجة لإنشاء قواعد جيوداتابيس، وتعمل على ملفات shapefile أيضاً.",
        {"B": ["Geodatabase Topology requires a Feature Dataset in a geodatabase.", "طوبولوجيا الجيوداتابيس تتطلب Feature Dataset."], "C": ["Branch versioning requires enterprise DBMS.", "التفريع النسخي يتطلب قواعد بيانات مؤسسية."], "D": ["Raster snapping snaps to raster cells, not shared vector edges.", "انجذاب الراستر ينجذب للبكسلات."]},
        "topology"
    ),
    # 16
    (
        "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes", "Beginner", "Tool-based", ["Reshape"],
        "An editor needs to update a section of a curved forest boundary polygon to match a recently realigned river channel.",
        "يحتاج محرر لتحديث جزء من حد مضلع غابة متعرج ليتطابق مع مسار قناة نهرية تم تعديل مسارها حديثاً.",
        "Which editing tool allows drawing a replacement sketch across the polygon edge to update its shape?",
        "أي أداة تحرير تتيح رسم مسار بديل عبر حافة المضلع لتحديث شكله؟",
        [["Reshape", "Reshape (إعادة التشكيل)"], ["Buffer", "Buffer (النطاق)"], ["Divide", "Divide (التقسيم)"], ["Merge", "Merge (الدمج)"]],
        "A",
        "The Reshape tool replaces a portion of a line or polygon boundary with a new sketched geometry that starts and ends across the original feature edge.",
        "تتيح أداة Reshape استبدال جزء من حدود المضلع أو الخط بمسار مرسوم جديد يبدأ وينتهي قاطعاً الحد الأصلي للمعلم لتحديث شكله بسلاسة.",
        {"B": ["Buffer creates distance rings around features.", "تنشئ Buffer مناطق حرم."], "C": ["Divide splits features into separate parts.", "تقسم أداة Divide المعالم."], "D": ["Merge combines multiple features into one.", "تدمج أداة Merge معالم متعددة."]},
        "editing"
    ),
    # 17
    (
        "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes", "Intermediate", "Tool-based", ["Align Edge"],
        "During boundary editing, a technician notices small sliver gaps between adjacent property lots.",
        "أثناء تحرير الحدود، لاحظ الفني وجود فجوات وفواصل شريطية دقيقة بين قطع أراضٍ متجاورة.",
        "Which tool matches an edge to a coincident path in an adjacent layer within a search tolerance to eliminate sliver gaps?",
        "أي أداة تطابق الحافة لتتبع مساراً مطابقاً في طبقة مجاورة ضمن مسافة تسامح لإزالة الفجوات الشريطية؟",
        [["Align Edge", "Align Edge (محاذاة الحافة)"], ["Clip", "Clip (القص)"], ["Generalize", "Generalize (التعميم)"], ["Smooth", "Smooth (التنعيم)"]],
        "A",
        "Align Edge conforms an edge of a polygon or polyline to match an adjoining edge within a search tolerance distance, cleanly closing sliver gaps.",
        "تطابق أداة Align Edge حافة مضلع أو خط مع حافة مجاورة ضمن مسافة تسامح محددة، مما يغلق الفجوات الشريطية بدقة واحترافية.",
        {"B": ["Clip cuts features by an extent.", "تقص أداة Clip المعالم."], "C": ["Generalize simplifies vertices.", "تبسط أداة Generalize الرؤوس."], "D": ["Smooth curves lines.", "تنعم أداة Smooth الخطوط."]},
        "editing"
    ),
    # 18
    (
        "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes", "Intermediate", "Tool-based", ["Traverse"],
        "A surveyor enters boundary courses from a legal land deed: 'North 45 degrees East, 250.5 feet; thence South 80 degrees East, 180 feet'.",
        "يقوم مساح بإدخال أضلاع مسار حدودي من صك أرض قانوني: 'شمال 45 درجة شرقاً، مسافة 250.5 قدم؛ ثم جنوب 80 درجة شرقاً، مسافة 180 قدماً'.",
        "Which tool should be used in the Modify Features pane to construct these boundary lines sequentially?",
        "أي أداة يجب استخدامها في نافذة Modify Features لإنشاء هذه الخطوط الحدودية بالتتابع؟",
        [["Traverse", "Traverse (المضلع المساحي)"], ["Reshape", "Reshape (إعادة التشكيل)"], ["Split", "Split (التقسيم)"], ["Simplify", "Simplify (التبسيط)"]],
        "A",
        "The Traverse tool enters sequential coordinate geometry (COGO) courses using directions, distances, curve radii, and arc lengths directly from survey records.",
        "تتيح أداة Traverse إدخال أضلاع المسح المساحي (الهندسة الإحداثية COGO) بالاتجاهات والمسافات وأنصاف الأقطار مباشرة من الصكوك وسجلات المسح.",
        {"B": ["Reshape edits existing lines.", "تعدل Reshape خطوطاً قائمة."], "C": ["Split cuts features.", "تقطع أداة Split المعالم."], "D": ["Simplify reduces vertices.", "تبسط أداة Simplify الرؤوس."]},
        "editing"
    ),
    # 19
    (
        "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Technical", ["Check Geometry"],
        "A quality control manager requires generating an audit report table detailing all topological flaws and self-intersections in a statewide pipeline dataset without making any modifications to the dataset.",
        "طلب مدير مراقبة الجودة تقرير تدقيق جدولي يسرد كافة العيوب الطوبولوجية والتقاطعات الذاتية في شبكة أنابيب على مستوى الولاية دون إجراء أي تعديل على بيانات الطبقة.",
        "Which tool satisfies this read-only inspection requirement?",
        "أي أداة تلبي هذا المطلب الفحصي للقراءة فقط دون تعديل البيانات؟",
        [["Check Geometry", "Check Geometry (فحص الهندسة)"], ["Repair Geometry", "Repair Geometry (إصلاح الهندسة)"], ["Delete Identical", "Delete Identical (حذف المتطابق)"], ["Simplify Line", "Simplify Line (تبسيط الخطوط)"]],
        "A",
        "Check Geometry scans vector features and writes identified geometry problems (self-intersections, null geometries, incorrect ring order) into a standalone report table without modifying features.",
        "تفحص أداة Check Geometry المعالم الاتجاهية وتكتب المشكلات الهندسية المكتشفة في جدول تقرير مستقل دون تعديل البيانات الأصلية.",
        {"B": ["Repair Geometry fixes errors in-place, modifying the dataset.", "تصلح Repair Geometry الأخطاء مباشرة وتعدل البيانات."], "C": ["Delete Identical deletes records.", "تحذف Delete Identical السجلات المتطابقة."], "D": ["Simplify Line alters line geometry.", "تبسط Simplify Line هندسة الخطوط."]},
        "editing"
    ),
    # 20
    (
        "Given a scenario, determine the appropriate existing geodatabase elements to use", "Beginner", "Conceptual", ["Mobile Geodatabase"],
        "An organization develops an offline mobile inspection workflow using ArcGIS Field Maps on Android and iOS tablets.",
        "تطور مؤسسة مسار عمل للتفتيش الميداني بدون إنترنت عبر ArcGIS Field Maps على أجهزة أندرويد و iOS اللوحية.",
        "Which geodatabase format is packaged as a single portable file on disk based on the SQLite/SpatiaLite engine?",
        "أي صيغة قواعد بيانات جغرافية تُحفظ كملف مفرد محمول على القرص وتعتمد على محرك SQLite/SpatiaLite؟",
        [["Mobile Geodatabase (.geodatabase)", "قاعدة البيانات الجغرافية المحمولة Mobile Geodatabase (.geodatabase)"], ["File Geodatabase (.gdb folder)", "قاعدة البيانات الملفية File Geodatabase (.gdb)"], ["Personal Geodatabase (.mdb)", "قاعدة البيانات الشخصية Personal Geodatabase (.mdb)"], ["Shapefile (.shp)", "ملف الشكل Shapefile (.shp)"]],
        "A",
        "Mobile Geodatabases (.geodatabase) are single-file databases built on SQLite and SpatiaLite, specifically designed for cross-platform mobile apps, offline sync, and fast field performance.",
        "تُعد Mobile Geodatabase (.geodatabase) قاعدة بيانات ملفية واحدة مبنية على محرك SQLite و SpatiaLite، ومصممة خصيصاً للتطبيقات الميدانية المحمولة والمزامنة غير المتصلة بالإنترنت.",
        {"B": ["File Geodatabases are stored as folders containing dozens of binary files, awkward for mobile apps.", "تتكون File Geodatabase من مجلد ملفات ثنائية عديدة."], "C": ["Personal Geodatabases are 32-bit legacy Microsoft Access files.", "تعتمد Personal Geodatabase على محرك Access القديم."], "D": ["Shapefiles lack geodatabase capabilities like domains and subtypes.", "تفتقر ملفات shapefile للنطاقات والتصنيفات الفرعية."]},
        "gdb"
    ),
    # 21
    (
        "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Technical", ["Create Mosaic Dataset"],
        "A remote sensing team creates a Mosaic Dataset to catalog 5,000 aerial orthophotos. Some images contain black border pixels with pixel values of 0 along their tilted edges that obscure overlapping adjacent images.",
        "أنشأ فريق استشعار عن بعد مجموعة بيانات موزاييك لفهرسة 5,000 صورة جوية. تحتوي بعض الصور على حواف سوداء بقيمة بكسل 0 على أطرافها المائلة مما يحجب الصور المجاورة المتراكبة.",
        "Which tool in the Mosaic Dataset toolset recalculates the boundary polygon of each raster item to clip out the black border pixels?",
        "أي أداة في صندوق أدوات الموزاييك تعيد حساب مضلع حدود كل صورة لاقتطاع البكسلات السوداء المحيطة؟",
        [["Build Footprints", "Build Footprints (بناء إطارات المعالم)"], ["Build Overviews", "Build Overviews (بناء المناظر العامة)"], ["Define Overviews", "Define Overviews (تعريف المناظر العامة)"], ["Export Tile Package", "Export Tile Package (تصدير حزمة البلاطات)"]],
        "A",
        "Build Footprints recomputes the extent polygon of each raster in a mosaic dataset, allowing exclusion of black border pixels (value 0) or white borders (value 255) so overlapping images blend seamlessly.",
        "تعيد أداة Build Footprints حساب مضلع حدود كل صورة في الموزاييك، وتتيح استبعاد البكسلات السوداء (قيمة 0) أو البيضاء، مما يدمج الصور المتداخلة بسلاسة تامة.",
        {"B": ["Build Overviews builds reduced-resolution display tiles.", "تبني Overviews بلاطات مخفضة الدقة."], "C": ["Define Overviews sets overview parameters.", "تحدد Define Overviews معاملات العرض."], "D": ["Export Tile Package caches tiles.", "تصدير حزمة البلاطات ينشئ كاش للخرائط."]},
        "gdb"
    ),
    # 22
    (
        "Given a scenario, determine the appropriate existing geodatabase elements to use", "Intermediate", "Technical", ["Add Global IDs"],
        "An enterprise GIS team prepares two-way geodatabase replication between headquarters and a regional office. During replica creation, the wizard fails stating that several feature classes lack unique global identifiers.",
        "يجهز فريق نظم المعلومات الجغرافية عملية نسخ متماثل ثنائي الاتجاه (Two-way Replication) بين المقر الرئيسي وفرع إقليمي، ففشل المعالج بسبب افتقار بعض الطبقات لمعرفات فريدة عالمية.",
        "Which tool must be run on those datasets before replica creation can proceed?",
        "أي أداة يجب تشغيلها على تلك الطبقات قبل التمكن من إنشاء النسخ المتماثل؟",
        [["Add Global IDs", "Add Global IDs (إضافة معرفات عالمية)"], ["Calculate Field", "Calculate Field (حساب الحقل)"], ["Rebuild Indexes", "Rebuild Indexes (إعادة بناء الفهارس)"], ["Create Topology", "Create Topology (إنشاء طوبولوجيا)"]],
        "A",
        "Two-way and one-way geodatabase replication requires GlobalID fields on all participating feature classes to track row identities across independent database systems.",
        "يتطلب النسخ المتماثل للجيوداتابيس وجود حقول GlobalID في كافة الطبقات المشاركة لتتبع هوية السجلات عبر خوادم قواعد البيانات المختلفة.",
        {"B": ["Calculate Field does not generate certified geodatabase UUID columns.", "حساب الحقل لا ينشئ أعمدة UUID المعتمدة للجيوداتابيس."], "C": ["Rebuilding indexes optimizes search speed.", "إعادة بناء الفهارس تسرع البحث."], "D": ["Topology manages geometric rules.", "الطوبولوجيا تدير القواعد الهندسية."]},
        "gdb"
    ),
    # 23
    (
        "Manage coordinate systems to preserve the desired spatial properties", "Intermediate", "Troubleshooting", ["Project Raster"],
        "A forestry analyst reprojects a classified Vegetation Type raster (with discrete integer codes: 1=Pine, 2=Oak, 3=Maple) from WGS84 to UTM Zone 18N. After projection, the raster attribute table contains bizarre decimal values like 1.45 and 2.87.",
        "أعاد محلل غابات إسقاط راستر لأنواع الأشجار (بأكواد صحيحة منفصلة: 1=صنوبر، 2=بلوط، 3=قيقب) من WGS84 إلى UTM 18N؛ وبعد الإسقاط، ظهرت في الجدول قيم عشرية غريبة مثل 1.45 و 2.87.",
        "What mistake did the analyst make during the Project Raster tool execution?",
        "ما هو الخطأ الذي ارتكبه المحلل أثناء تشغيل أداة Project Raster؟",
        [["They used Bilinear or Cubic resampling instead of Nearest Neighbor", "استخدم طريقة إعادة استعيان Bilinear أو Cubic بدلاً من Nearest Neighbor"], ["They forgot to build raster overviews", "نسي بناء المناظر العامة للراستر"], ["They exported the raster to a JPEG file", "قام بتصدير الراستر إلى ملف JPEG"], ["They did not set a mask environment", "لم يحدد بيئة القناع Mask"]],
        "A",
        "Bilinear Interpolation and Cubic Convolution calculate weighted mathematical averages of neighboring pixels, which produces artificial fractional values when applied to categorical/discrete class codes. Nearest Neighbor preserves original integer codes.",
        "تحسب طريقتا Bilinear و Cubic متوسطات حسابية موزونة للبكسلات المجاورة، مما ينتج أرقاماً كسرية مشوهة عند تطبيقها على تصنيفات فئوية منفصلة؛ والواجب استخدام Nearest Neighbor للحفاظ على الأكواد الأصلية.",
        {"B": ["Overviews accelerate display and do not alter projection cell math.", "المناظر العامة تسرع العرض ولا تغير حسابات البكسل."], "C": ["JPEG export does not explain projection tool parameter errors.", "تصدير JPEG لا يفسر خطأ معاملات الأداة."], "D": ["Mask environments clip extents, not cell interpolation values.", "القناع يقص الحدود ولا يغير الاستيفاء."]},
        "coords"
    ),
    # 24
    (
        "Given a scenario, determine the appropriate existing geodatabase elements to use", "Advanced", "Conceptual", ["Branch Versioning"],
        "An enterprise municipal utility is modernizing its enterprise geodatabase to deploy web-based editing across service-oriented ArcGIS web apps and field devices.",
        "تحدث بلدية قاعدة بياناتها المؤسسية لنشر التحرير عبر خدمات الويب وتطبيقات الجوال الميدانية.",
        "Which versioning model is required to support multi-user editing over web feature services?",
        "أي نموذج إصدارات مطلوب لدعم التحرير التشاركي متعدد المستخدمين عبر خدمات معالم الويب؟",
        [["Branch Versioning", "التفريع النسخي Branch Versioning"], ["Traditional Versioning without GlobalIDs", "النسخ التقليدي بدون GlobalIDs"], ["Non-versioned single user editing", "التحرير غير النسخي لمستخدم مفرد"], ["File Geodatabase local locking", "القفل المحلي لقواعد البيانات الملفية"]],
        "A",
        "Branch Versioning is the modern, service-based versioning architecture in ArcGIS Enterprise that supports multi-user editing, undo/redo, reconciliation, and validation directly through web services.",
        "يُعد التفريع النسخي (Branch Versioning) النموذج المعماري الحديث القائم على الخدمات في ArcGIS Enterprise لدعم التحرير التشاركي والتراجع والمطابقة والتحقق مباشرة عبر خدمات الويب.",
        {"B": ["Traditional versioning is designed for direct desktop enterprise database connections.", "النسخ التقليدي مخصص للاتصال المكتبي المباشر."], "C": ["Non-versioned editing does not support multi-editor isolation.", "التحرير غير النسخي لا يدعم عزل تعديلات المحررين."], "D": ["File geodatabases do not support web versioning.", "قواعد البيانات الملفية لا تدعم النسخ عبر الويب."]},
        "gdb"
    ),
    # 25
    (
        "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes", "Intermediate", "Tool-based", ["Enable COGO"],
        "A land records department enables COGO on its boundary lines. When editors draft parcel lines, they need the line attributes to automatically record the surveyed quadrant bearing and ground distance.",
        "فعل قسم السجلات العقارية خاصية COGO على خطوط الحدود. وعند رسم خطوط الأراضي، يحتاج المحررون لتسجيل انحراف الربع المساحي والمسافة الأرضية تلقائياً في سمات الخط.",
        "Which geoprocessing tool inspects existing line geometry and calculates standard COGO direction and distance attributes into the COGO fields?",
        "أي أداة معالجة تفحص هندسة الخطوط القائمة وتحسب سمات اتجاه ومسافة COGO المعيارية في حقول COGO؟",
        [["Update COGO", "Update COGO (تحديث أبعاد COGO)"], ["Calculate Geometry Attributes", "Calculate Geometry Attributes"], ["Repair Geometry", "Repair Geometry"], ["Snap", "Snap"]],
        "A",
        "The Update COGO tool recalculates Direction and Distance attributes for selected line features based on their physical coordinate geometry, synchronizing COGO fields with drawn lines.",
        "تحسب أداة Update COGO قيم الاتجاه والمسافة لمعالم الخطوط المحددة بالاعتماد على إحداثياتها الهندسية الفعلية، مما يزامن حقول COGO مع الخطوط المرسومة.",
        {"B": ["Calculate Geometry Attributes writes coordinates or lengths, but not specialized COGO bearing strings.", "تحسب أطوالاً وإحداثيات وليس صياغات الانحراف المساحي."], "C": ["Repair Geometry fixes topology errors.", "تصلح Repair Geometry العيوب الهندسية."], "D": ["Snap moves vertices.", "أداة Snap تحرك الرؤوس."]},
        "editing"
    ),
    # 26
    (
        "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes", "Intermediate", "Tool-based", ["Divide"],
        "A land developer purchases a 50-acre parcel and sells off exactly 12.5 acres from the western side along a north-south bearing line.",
        "اشترى مطور عقاري قطعة أرض بمساحة 50 فداناً، وباع منها 12.5 فداناً بالضبط من الجانب الغربي بمحاذاة خط شمال-جنوب.",
        "Which tool in the Modify Features pane splits the polygon by entering an exact area measurement?",
        "أي أداة في نافذة Modify Features تقسم المضلع بإدخال مساحة رقمية دقيقة؟",
        [["Divide (Specified Area)", "Divide بخيار المساحة المحددة (Specified Area)"], ["Buffer", "Buffer (النطاق)"], ["Clip", "Clip (القص)"], ["Reshape", "Reshape (إعادة التشكيل)"]],
        "A",
        "The Divide tool with the 'Specified Area' method allows carving off a lot of exact square footage or acreage along a user-specified directional angle.",
        "تتيح أداة Divide بخيار 'Specified Area' اقتطاع مساحة رقمية دقيقة بالأفدنة أو الأمتار المربعة على امتداد زاوية اتجاه يحددها المستخدم.",
        {"B": ["Buffer creates concentric zones.", "تنشئ Buffer نطاقات."], "C": ["Clip cuts by an extent.", "تقص Clip بالحدود."], "D": ["Reshape alters boundary paths.", "تعدل Reshape مسار الحدود."]},
        "editing"
    ),
    # 27
    (
        "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes", "Beginner", "Technical", ["Snapping"],
        "An editor working on detailed utility connections finds that the cursor snaps to nearby vertices prematurely when they are still 30 pixels away, making precision sketching difficult.",
        "وجد محرر يعمل على توصيلات مرافق تفصيلية أن المؤشر ينجذب مبكراً نحو الرؤوس المجاورة وهو على بعد 30 بكسل، مما يصعب الرسم الدقيق.",
        "Where can the editor decrease the snapping pixel distance in ArcGIS Pro?",
        "أين يمكن للمحرر تقليص مسافة تسامح الانجذاب بالبكسل في ArcGIS Pro؟",
        [["Edit ribbon > Snapping group > Snapping Options > Snapping Tolerance", "شريط Edit > مجموعة Snapping > خيارات Snapping Options > ضبط Snapping Tolerance"], ["Catalog pane > Project Options", "نافذة Catalog > خيارات المشروع"], ["Layer Properties > Metadata", "خصائص الطبقة > البيانات الوصفية"], ["Analysis > Environments", "شريط التحليل > البيئات Environments"]],
        "A",
        "Snapping Tolerance (measured in screen pixels) is configured under Snapping Options on the Edit ribbon, allowing editors to tighten or loosen magnetic snapping sensitivity.",
        "يتم ضبط تسامح الانجذاب (Snapping Tolerance بوحدات بكسل الشاشة) في خيارات الانجذاب بشريط Edit، مما يمكن المحرر من تضييق أو توسيع حساسية الانجذاب المغناطيسي.",
        {"B": ["Catalog options manage file defaults.", "خيارات الكتالوج للملفات."], "C": ["Metadata documents datasets.", "البيانات الوصفية لتوثيق البيانات."], "D": ["Environments manage geoprocessing.", "البيئات للمعالجة الجغرافية."]},
        "editing"
    ),
    # 28
    (
        "Given a scenario, determine the appropriate existing geodatabase elements to use", "Advanced", "Technical", ["Geodatabase Topology"],
        "An administrator builds a Geodatabase Topology for surveyed parcel lines. If the Cluster Tolerance is set accidentally to 5 meters instead of 0.05 meters, what catastrophic error will occur during validation?",
        "أنشأ مسؤول طوبولوجيا لقواعد البيانات لخطوط مسح عقاري؛ وإذا تم ضبط تسامح التجميع (Cluster Tolerance) بالخطأ على 5 أمتار بدلاً من 0.05 متر، ما الخطأ الكارثي الذي سيحدث أثناء التحقق؟",
        "What is the expected outcome of setting an excessively large cluster tolerance?",
        "ما النتيجة المتوقعة لضبط تسامح تجميع كبير للغاية؟",
        [["Vertices within 5 meters of each other will snap together and collapse, severely distorting boundaries and creating false coincidence", "ستنجذب الرؤوس الواقعة ضمن 5 أمتار وتنهار معاً، مما يشوه الحدود المساحية بشدة ويدمج معالم متجاورة"], ["The geodatabase file will be deleted from the server", "سيتم حذف ملف قاعدة البيانات من الخادم"], ["All lines will be converted to 3D elevation rasters", "ستتحول كافة الخطوط إلى راستر ارتفاع ثلاثي الأبعاد"], ["The coordinate system will switch to Martian coordinates", "سيتحول نظام الإحداثيات إلى إحداثيات كوكب المريخ"]],
        "A",
        "The Cluster Tolerance defines the distance within which vertices are considered coincident and snapped together. An excessively large cluster tolerance collapses real geometric features and severely corrupts spatial precision.",
        "يحدد تسامح التجميع (Cluster Tolerance) المسافة التي تعتبر الرؤوس الواقعة ضمنها متطابقة فيدمجها معاً؛ وضبط قيمة كبيرة جداً يؤدي إلى انهيار المعالم الهندسية وتشويه دقة الحدود المساحية.",
        {"B": ["Validation does not delete database files.", "التحقق لا يحذف ملفات قواعد البيانات."], "C": ["Vector lines remain vectors.", "الخطوط تظل متجهات."], "D": ["Coordinate systems are not modified by topology.", "أنظمة الإحداثيات لا تتغير بالطوبولوجيا."]},
        "topology"
    ),
    # 29
    (
        "Given a scenario, determine the appropriate existing geodatabase elements to use", "Intermediate", "Technical", ["Domains", "Merge Policy"],
        "A land records department merges three adjacent agricultural parcels into a single combined farming parcel. The 'Estimated_Corn_Yield' attribute on the three parcels was 5,000, 8,000, and 12,000 bushels. After the merge edit, the combined parcel shows an Estimated_Corn_Yield of 25,000 bushels.",
        "دمجت دائرة الأراضي 3 قطع زراعية متجاورة في قطعة واحدة؛ وكانت قيم إنتاج الذرة المقدر عليها 5,000 و 8,000 و 12,000 بوشل؛ وبعد الدمج أظهرت القطعة الموحدة إنتاجاً قدره 25,000 بوشل.",
        "Which geodatabase Merge Policy was active on the corn yield attribute field?",
        "أي سياسة دمج (Merge Policy) كانت مفعلة على حقل إنتاج الذرة في قاعدة البيانات؟",
        [["Sum Values", "Sum Values (جمع القيم)"], ["Duplicate", "Duplicate (التكرار)"], ["Weighted Average", "Weighted Average (المتوسط الموزون)"], ["Geometry Ratio", "Geometry Ratio (النسبة الهندسية)"]],
        "A",
        "The 'Sum Values' merge policy adds together the numeric attribute values of all merged features, calculating the combined total (5,000 + 8,000 + 12,000 = 25,000).",
        "تجمع سياسة الدمج 'Sum Values' القيم الرقمية لكافة المعالم المدمجة وتضع المجموع الكلي في المعلم الجديد الناتج (5000 + 8000 + 12000 = 25000).",
        {"B": ["Duplicate would assign the value of the primary selected feature.", "سياسة Duplicate تعطي قيمة أحد المعالم فقط."], "C": ["Weighted Average would calculate an area-weighted mean.", "المتوسط الموزون يحسب متوسطاً موزوناً بالمساحة."], "D": ["Geometry Ratio is a split policy, not a merge policy.", "النسبة الهندسية سياسة تقسيم وليست سياسة دمج."]},
        "domains"
    ),
    # 30
    (
        "Given a scenario, determine the appropriate existing geodatabase elements to use", "Intermediate", "Technical", ["Attribute Rules"],
        "An electric utility wants to inspect existing transmission pole features across 3 counties to identify poles that violate minimum ground clearance rules without interrupting ongoing field data collection.",
        "تريد شركة كهرباء فحص أعمدة النقل القائمة عبر 3 مقاطعات لاكتشاف الأعمدة المخالفة لمسافات الخلوص الأرضي دون مقاطعة أو إيقاف عمليات التحرير الميداني الجارية.",
        "Which type of Attribute Rule evaluates data on demand or on a schedule, generating error features that can be reviewed and managed in the Error Inspector?",
        "أي نوع من قواعد السمات يقيم البيانات عند الطلب أو وفق جدول زمني، مولداً معالم أخطاء يمكن مراجعتها وإدارتها في نافذة Error Inspector؟",
        [["Validation Attribute Rule", "قاعدة سمات تحققية (Validation Attribute Rule)"], ["Constraint Attribute Rule", "قاعدة سمات مقيدة (Constraint Attribute Rule)"], ["Calculation Attribute Rule (Immediate)", "قاعدة سمات حسابية فورية (Immediate Calculation)"], ["Simple Relationship Class", "فئة علاقة بسيطة (Simple Relationship Class)"]],
        "A",
        "Validation rules evaluate data quality asynchronously across existing datasets, logging non-compliant features into GDB error tables so analysts can inspect and fix them via the Error Inspector without blocking edits.",
        "تُقيم قواعد التحقق (Validation Rules) جودة البيانات القائمة عند الطلب دون تعطيل التحرير، وتسجل المعالم المخالفة في جداول أخطاء ليراجعها المحللون في نافذة Error Inspector.",
        {"B": ["Constraint rules block edits immediately at commit time.", "قواعد القيد تحظر التعديل فوراً أثناء الحفظ."], "C": ["Immediate calculation rules compute field values.", "القواعد الفورية تحسب القيم الحقلية."], "D": ["Relationship classes link tables.", "فئات العلاقات لربط الجداول."]},
        "rules"
    ),
    # 31
    (
        "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Conceptual", ["Enable Attachments"],
        "A county parks department configures photo attachments on its trails layer.",
        "قام قسم متنزهات المحافظة بتهيئة مرفقات الصور على طبقة مسارات المشي.",
        "What type of relationship class is automatically generated by ArcGIS Pro when attachments are enabled on a feature class?",
        "ما هو نوع فئة العلاقة التي ينشئها ArcGIS Pro تلقائياً عند تفعيل المرفقات (Enable Attachments) على فئة معالم؟",
        [["Composite Relationship Class (where deleting a feature automatically cascade-deletes its attachments)", "فئة علاقة مركبة Composite (بحيث يؤدي حذف المعلم إلى حذف مرفقاته تلقائياً بالتتابع)"], ["Simple Relationship Class (where attachments remain orphan files if features are deleted)", "فئة علاقة بسيطة Simple (بحيث تظل المرفقات كملفات يتيمة عند حذف المعلم)"], ["Many-to-Many Bridge Table without keys", "جدول وسيط متعدد إلى متعدد بدون مفاتيح"], ["Spatial Join relationship", "علاقة ضم مكاني"]],
        "A",
        "Attachments use a Composite Relationship Class. Because an attachment's existence depends entirely on the parent feature, deleting a feature automatically cascades and purges all of its associated photo/document attachments.",
        "تستخدم المرفقات فئة علاقة مركبة (Composite Relationship Class)؛ ولأن وجود المرفق مرهون بوجود المعلم الأصلي، فإن حذف المعلم يؤدي تلقائياً إلى حذف جميع صوره ومستنداته المرفقة.",
        {"B": ["Simple relationships do not cascade delete dependent records.", "العلاقات البسيطة لا تحذف السجلات التابعة."], "C": ["Attachment relationships maintain explicit foreign keys.", "علاقات المرفقات تحافظ على مفاتيح ربط صريحة."], "D": ["Attachments are tabular relational links, not spatial joins.", "المرفقات علاقات جدولية وليست ضماً مكانياً."]},
        "gdb"
    ),
    # 32
    (
        "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Technical", ["Create Locator"],
        "A 911 dispatch agency creates an address locator for emergency vehicle routing.",
        "تنشئ هيئة طوارئ محدد مواقع للعناوين لتوجيه سيارات الإسعاف والشرطة.",
        "When using the Create Locator tool in ArcGIS Pro, which locator role should be selected when reference data consists of parcel address points with exact building rooftop coordinates?",
        "عند استخدام أداة Create Locator في ArcGIS Pro، أي دور لمحدد المواقع (Locator Role) يجب اختياره عندما تتكون البيانات المرجعية من نقاط عناوين بأسطح المباني الدقيقة؟",
        [["Point Address", "Point Address (عناوين النقاط)"], ["Street Address (dual range lines)", "Street Address (خطوط ترقيم الشوارع)"], ["Postal code centroid", "مراكز الرموز البريدية"], ["Administrative area polygon", "مضلعات المناطق الإدارية"]],
        "A",
        "The 'Point Address' role is designed for reference feature classes of address points that represent individual structure rooftops or parcel centroids with specific house numbers and street names.",
        "صُمم دور 'Point Address' لفئات المعالم النقطية التي تمثل عناوين أسطح المباني الفردية أو مراكز قطع الأراضي التي تحمل أرقام منازل وأسماء شوارع دقيقة.",
        {"B": ["Street Address is for polyline street centerlines with address ranges.", "Street Address مخصص لخطوط الشوارع ذات نطاقات الترقيم."], "C": ["Postal code centroids represent broad postal areas.", "مراكز الرموز البريدية تمثل مناطق بريدية عامة."], "D": ["Admin areas represent cities or counties.", "المناطق الإدارية للمدن والمحافظات."]},
        "geocoding"
    ),
    # 33
    (
        "Manage coordinate systems to preserve the desired spatial properties", "Beginner", "Conceptual", ["On-the-fly Projection"],
        "An analyst works on a regional emergency map containing layers in WGS84, State Plane, and UTM coordinates.",
        "يعمل محلل على خريطة طوارئ إقليمية تحتوي على طبقات بإحداثيات WGS84 و State Plane و UTM.",
        "When multiple layers in different coordinate systems are projected on the fly in an ArcGIS Pro map, which coordinate system determines the linear units of measurement for interactive distance measurement tools?",
        "عند عرض طبقات متعددة بأنظمة إحداثيات مختلفة وإسقاطها آنياً (On the fly) في خريطة ArcGIS Pro، أي نظام إحداثيات يحدد وحدات القياس الخطية لأدوات قياس المسافات التفاعلية؟",
        [["The Coordinate System of the active Map Frame", "نظام إحداثيات إطار الخريطة النشط (Map Frame)"], ["The coordinate system of the oldest shapefile on the hard drive", "نظام إحداثيات أقدم ملف shapefile على القرص"], ["WGS 1984 permanently regardless of map settings", "نظام WGS 1984 بشكل دائم متجاهلاً إعدادات الخريطة"], ["The coordinate system of the Windows operating system", "نظام إحداثيات نظام تشغيل ويندوز"]],
        "A",
        "Interactive tools, distance measurements, and visual display on the canvas operate in the coordinate system assigned to the active Map Frame.",
        "تعمل الأدوات التفاعلية وقياسات المسافات والعرض البصري وفق نظام الإحداثيات المعين لإطار الخريطة النشط (Map Frame).",
        {"B": ["File age has no bearing on software map coordinate mechanics.", "تاريخ إنشاء الملفات لا علاقة له بإسقاط الخريطة."], "C": ["Maps can be set to any projected or geographic system.", "يمكن ضبط الخريطة على أي نظام إسقاط."], "D": ["Operating systems do not possess geographic coordinate systems.", "نظام التشغيل ليس له أنظمة إحداثيات جغرافية."]},
        "coords"
    ),
    # 34
    (
        "Given a scenario, determine the appropriate existing geodatabase elements to use", "Intermediate", "Conceptual", ["Create Relationship Class"],
        "An analyst configures a Simple 1-to-Many Relationship Class between a Building feature class (origin) and an Occupants table (destination).",
        "أنشأ محلل فئة علاقة بسيطة (Simple) من 1 إلى متعدد بين فئة المباني (المصدر) وجدول السكان (الهدف).",
        "If an editor deletes a Building feature, what happens to the related records in the Occupants table?",
        "إذا قام محرر بحذف معلم مبنى، ماذا يحدث للسجلات المرتبطة به في جدول السكان؟",
        [["The related occupant records are preserved, and their foreign key values are unlinked (or set to null)", "يتم الحفاظ على سجلات السكان المرتبطة، وتبقى في الجدول مع فك ارتباط المفتاح الأجنبي"], ["The related occupant records are deleted automatically", "تُحذف سجلات السكان المرتبطة تلقائياً"], ["The entire geodatabase is corrupted", "تتلف قاعدة البيانات بالكامل"], ["The building feature is restored automatically", "يستعاد معلم المبنى تلقائياً"]],
        "A",
        "In a Simple relationship, origin and destination objects exist independently. Deleting the origin does not delete related destination records; only in a Composite relationship does cascade deletion occur.",
        "في العلاقات البسيطة (Simple)، تكون الكائنات مستقلة في دورة حياتها؛ لذا فإن حذف كائن المصدر لا يحذف سجلات الهدف المرتبطة به، على عكس العلاقات المركبة (Composite) التي تطبق الحذف التسلسلي.",
        {"B": ["Cascade deletion is the exclusive behavior of Composite relationships.", "الحذف التسلسلي خاص بالعلاقات المركبة فقط."], "C": ["Simple deletions do not damage databases.", "الحذف لا يتلف قاعدة البيانات."], "D": ["Deleted features are not resurrected.", "المعالم المحذوفة لا تعود تلقائياً."]},
        "domains"
    ),
    # 35
    (
        "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes", "Intermediate", "Technical", ["Traverse"],
        "After entering deed courses in the Traverse tool for a closed parcel boundary, the ending point does not coincide with the starting point, leaving a closure gap of 0.45 feet.",
        "بعد إدخال أضلاع الصك في أداة Traverse لمضلع أرض مغلق، لم تتطابق نقطة النهاية مع نقطة البداية، وبقيت فجوة خطأ قفل قدرها 0.45 قدم.",
        "What option in the Traverse tool adjusts vertices to distribute the misclose error mathematically?",
        "ما الخيار في أداة Traverse الذي يعدل الرؤوس لتوزيع خطأ القفل رياضياً؟",
        [["Close and adjust traverse (using Compass, Transit, or Crandall rule)", "إغلاق وضبط المسار (Close and adjust) باستخدام قواعد البوصلة أو الترانزيت"], ["Delete the traverse line", "حذف خط المسار"], ["Run Project Raster", "تشغيل أداة Project Raster"], ["Convert the traverse to a TIN surface", "تحويل المسار إلى سطح TIN"]],
        "A",
        "The Traverse tool includes closure adjustment methods (Compass Rule, Transit Rule, Crandall Rule) that mathematically distribute the closure discrepancy across all courses to close the boundary cleanly.",
        "تتضمن أداة Traverse طرقاً لضبط القفل (مثل قاعدة البوصلة Compass Rule وقاعدة الترانزيت) التي توزع خطأ القفل رياضياً وتناسبياً على كافة أضلاع المسار لإغلاق مضلع الأرض بدقة مساحية.",
        {"B": ["Deleting the line loses the entered data.", "حذف الخط يفقد البيانات المدخلة."], "C": ["Project Raster reprojects imagery.", "إسقاط الراستر للصور."], "D": ["TIN surfaces model terrain elevations.", "أسطح TIN للتضاريس."]},
        "editing"
    ),
    # 36
    (
        "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Technical", ["Enable Archiving"],
        "A historical preservation team enables Geodatabase Archiving on a municipal zoning dataset.",
        "فعل فريق التراث العمراني خاصية الأرشفة (Geodatabase Archiving) على بيانات المخطط الهيكلي.",
        "How can an analyst view and query the exact zoning boundaries as they existed on January 1, 2015?",
        "كيف يمكن للمحلل استعراض والاستعلام عن حدود المخطط كما كانت قائمة بالضبط في 1 يناير 2015؟",
        [["Set the Historical Moment in the Map properties or Layer Properties to January 1, 2015", "ضبط اللحظة التاريخية (Historical Moment) في خصائص الخريطة أو الطبقة على تاريخ 1 يناير 2015"], ["Manually restore a backup tape drive", "استعادة شريط نسخ احتياطي يدوياً"], ["Change the Windows system clock to 2015", "تغيير ساعة نظام تشغيل ويندوز إلى 2015"], ["Re-enter all 2015 parcels manually", "إعادة إدخال كافة أراضي 2015 يدوياً"]],
        "A",
        "Geodatabase Archiving allows connecting to specific 'Historical Moments' using GDB_FROM_DATE and GDB_TO_DATE timestamps, allowing seamless point-in-time reconstruction of historical states.",
        "تتيح أرشفة الجيوداتابيس الاتصال بـ 'لحظات تاريخية' (Historical Moments) محددة بالاعتماد على حقول التواريخ الموثقة، مما يمكن من إعادة بناء واستعراض حالة البيانات في أي تاريخ ماضٍ بدقة.",
        {"B": ["Physical backup restoration is unnecessary with archiving enabled.", "لا حاجة لاستعادة نسخ احتياطية مع وجود الأرشفة."], "C": ["Changing the PC clock does not alter database historical records.", "تغيير ساعة الجهاز لا يغير بيانات قاعدة البيانات."], "D": ["Manual re-entry is redundant.", "إعادة الإدخال اليدوي مضيعة للوقت."]},
        "gdb"
    ),
    # 37
    (
        "Given a scenario, determine the appropriate existing geodatabase elements to use", "Beginner", "Conceptual", ["Subtypes"],
        "In a road feature class with Subtypes on the ROAD_CLASS field (1=Highway, 2=Arterial, 3=Local), editors need values to populate instantly.",
        "في طبقة طرق ذات تصنيفات فرعية (Subtypes) على حقل ROAD_CLASS (1=سريع، 2=شرياني، 3=محلي)، يحتاج المحررون لملء القيم فورياً.",
        "What capability allows ArcGIS Pro to automatically populate SPEED_LIMIT with 65 for Highways and 25 for Local roads as soon as features are drawn?",
        "ما الميزة التي تجعل البرنامج يملأ حقل SPEED_LIMIT تلقائياً بالقيمة 65 للطرق السريعة و 25 للمحلية فور رسم المعلم؟",
        [["Subtype-specific Default Values", "القيم الافتراضية المخصصة لكل تصنيف فرعي (Subtype Default Values)"], ["Geoprocessing Environments Cell Size", "حجم خلية بيئات التحليل"], ["Maplex Label Stacking", "تكدس تسميات مابلكس"], ["Raster Function Templates", "قوالب دوال الراستر"]],
        "A",
        "Each subtype can have unique default values assigned to each attribute field, ensuring correct standard values populate automatically upon feature creation.",
        "يمكن لكل تصنيف فرعي (Subtype) امتلاك قيم افتراضية مخصصة ومستقلة لكل حقل من حقول السمات، مما يضمن ملء القيم القياسية الصحيحة تلقائياً عند إنشاء المعالم الجديدة.",
        {"B": ["Cell size is a raster resolution setting.", "حجم الخلية للراستر."], "C": ["Maplex stacking is for label text formatting.", "تكدس مابلكس للنصوص."], "D": ["Raster templates process imagery.", "قوالب الراستر لمعالجة الصور."]},
        "domains"
    ),
    # 38
    (
        "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Best-practice", ["Add Attribute Index"],
        "An analyst joins a 2,000,000-row tax parcels layer to an external assessor table using the PARCEL_ID field. The join operations and subsequent spatial queries take several minutes to render.",
        "قام محلل بضم طبقة أراضٍ تحتوي على 2,000,000 سجل إلى جدول خارجي باستخدام حقل PARCEL_ID، فاستغرقت عمليات الضم والاستعلامات المكانية عدة دقائق للظهور.",
        "What database optimization should be applied to both tables to maximize join and query execution speed?",
        "ما هو إجراء تحسين أداء قاعدة البيانات الذي يجب تطبيقه على كلا الجدولين لتسريع عمليات الضم والاستعلام لأقصى حد؟",
        [["Create an Attribute Index on the PARCEL_ID field in both tables", "إنشاء فهرس سماتي (Attribute Index) على حقل PARCEL_ID في كلا الجدولين"], ["Convert both tables to text CSV files", "تحويل كلا الجدولين إلى ملفات CSV نصية"], ["Delete the Shape geometry field", "حذف حقل هندسة الشكل Shape"], ["Increase the monitor refresh rate to 144 Hz", "زيادة معدل تحديث الشاشة إلى 144 هرتز"]],
        "A",
        "Adding an Attribute Index on fields used in WHERE clauses or join keys dramatically accelerates table lookups and join performance, especially in tables exceeding thousands of records.",
        "يؤدي إنشاء فهرس سماتي (Attribute Index) على الحقول المستخدمة كمفاتيح ربط أو في استعلامات البحث إلى تسريع الاستعلامات وعمليات الضم الجدولي بشكل كبير، خاصة في الجداول المليونية.",
        {"B": ["CSV files lack indexed search structures and perform slower.", "ملفات CSV تفتقر للفهارس وأداؤها أبطأ."], "C": ["Deleting the Shape field destroys spatial coordinates.", "حذف حقل الشكل يدمر البيانات المكانية."], "D": ["Monitor hardware refresh rate does not accelerate database queries.", "معدل تحديث الشاشة لا يسرع قواعد البيانات."]},
        "gdb"
    ),
    # 39
    (
        "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Technical", ["Generalize"],
        "When simplifying natural river centerlines for small-scale mapping, a cartographer evaluates simplification methods.",
        "عند تبسيط خطوط محاور الأنهار الطبيعية للخرائط ذات مقاييس الرسم الصغيرة، يقيم رسام الخرائط طرق التبسيط المتاحة.",
        "Why is Bend Simplify preferred over Point Remove (Douglas-Peucker) for river centerlines?",
        "لماذا يُفضل استخدام خوارزمية Bend Simplify على Point Remove (دوغلاس-بيكر) لخطوط محاور الأنهار؟",
        [["Bend Simplify identifies significant geographic bends and preserves natural aesthetic meanders, whereas Douglas-Peucker creates harsh unnatural angular spikes", "تتعرف Bend Simplify على الانحناءات الجغرافية الهامة وتحافظ على التعرجات الطبيعية الجمالية، بينما تنتج خوارزمية دوغلاس-بيكر زوايا حادة مصطنعة"], ["Bend Simplify converts rivers into polygon lakes", "تحول Bend Simplify الأنهار إلى بحيرات مضلعة"], ["Douglas-Peucker is only compatible with 3D scenes", "خوارزمية دوغلاس-بيكر تعمل في المشاهد ثلاثية الأبعاد فقط"], ["There is no difference between them", "لا يوجد أي فرق بينهما"]],
        "A",
        "Bend Simplify (Wang-Müller algorithm) eliminates minor bends while preserving the characteristic sinuosity of natural features, preventing the sharp unnatural zigzag corners produced by distance-based Point Remove.",
        "تزيل خوارزمية Bend Simplify الانحناءات البسيطة مع الحفاظ على التعرجات المميزة للمعالم الطبيعية، متجنبة الزوايا الحادة المصطنعة الناتجة عن طريقة Point Remove المعتمدة على المسافة العمودية.",
        {"B": ["It simplifies line geometry, it does not create polygon lakes.", "تبسط الخطوط ولا تنشئ بحيرات مضلعة."], "C": ["Both algorithms work in 2D and 3D.", "تعمل كلتا الخوارزميتين في البيئتين."], "D": ["They use fundamentally distinct mathematical reduction principles.", "تختلفان في المبدأ الرياضي الكارتوغرافي."]},
        "editing"
    ),
    # 40
    (
        "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Tool-based", ["Calibrate Routes"],
        "A state highway department recalibrates its route measures because road realignment altered physical distances between milepost markers.",
        "أعادت وزارة النقل معايرة مقاييس الطرق بعد تعديل مسار طريق غير المسافات بين علامات الأميال.",
        "Which tool recalculates M-values along routes using point features with known measure values?",
        "أي أداة تعيد حساب قيم M على طول المسارات باستخدام معالم نقطية ذات قيم مقاييس معلومة؟",
        [["Calibrate Routes", "Calibrate Routes (معايرة المسارات)"], ["Create Routes", "Create Routes (إنشاء المسارات)"], ["Buffer", "Buffer (النطاق)"], ["Project", "Project (إعادة الإسقاط)"]],
        "A",
        "Calibrate Routes recalculates route measures (M-values) using a set of calibration points with known measure attributes, interpolating new measures between calibration points.",
        "تقوم أداة Calibrate Routes بإعادة احتساب مقاييس المسار (قيم M) باستخدام نقاط معايرة معلومة المقاييس، مستوفيةً قيماً جديدة بين نقاط المعايرة على طول الخط.",
        {"B": ["Create Routes builds initial routes from lines.", "أداة Create Routes تنشئ المسارات لأول مرة."], "C": ["Buffer creates distance polygons.", "أداة Buffer تنشئ مساحات حرم."], "D": ["Project handles coordinate transformations.", "أداة Project تتعامل مع الإسقاط."]},
        "linear"
    ),
    # 41
    (
        "Manage geospatial data (raster, vector, tabular)", "Beginner", "Conceptual", ["Shapefile"],
        "An analyst exports a massive 15,000,000-row point dataset to a shapefile, but the export tool crashes halfway through with a write error.",
        "قام محلل بتصدير 15,000,000 نقطة إلى ملف shapefile، فتعطلت الأداة في منتصف العملية مع ظهور خطأ في الكتابة.",
        "What technical file format limitation caused the export failure?",
        "ما هو القيد التقني في تنسيق الملف الذي تسبب في هذا الفشل؟",
        [["The shapefile component files (.shp, .dbf) exceeded the hard 2 GB file size limit", "تجاوزت ملفات مكونات shapefile (.shp و .dbf) الحد الأقصى الصارم لسعة الملف البالغ 2 جيجابايت"], ["Shapefiles cannot store point features", "ملفات shapefile لا تدعم المعالم النقطية"], ["The Windows operating system only supports 100 files per folder", "نظام تشغيل ويندوز يدعم 100 ملف فقط في المجلد"], ["The analyst selected the wrong color palette", "اختار المحلل بالتة ألوان خاطئة"]],
        "A",
        "Shapefiles are bound by a rigid 2 GB file size limit on each component file (.shp, .dbf, etc.). Datasets exceeding this capacity must be stored in File Geodatabases (1 TB default, up to 256 TB) or Enterprise Geodatabases.",
        "ملفات shapefile مقيدة بحد أقصى صارم لسعة كل ملف من مكوناتها (.shp و .dbf) يبلغ 2 جيجابايت؛ والبيانات الضخمة التي تتجاوز هذا الحجم يجب تخزينها في File Geodatabase (بسعة 1 تيرابايت افتراضياً وحتى 256 تيرابايت).",
        {"B": ["Shapefiles fully support points, lines, and polygons.", "ملفات shapefile تدعم النقاط والخطوط والمضلعات."], "C": ["Windows file systems support millions of files per directory.", "يدعم نظام ويندوز ملايين الملفات."], "D": ["Color palettes are visual and unrelated to disk write limits.", "بالتات الألوان لا علاقة لها بسعة الملفات."]},
        "gdb"
    ),
    # 42
    (
        "Manage geospatial data (raster, vector, tabular)", "Beginner", "Conceptual", ["Shapefile"],
        "When exporting a geodatabase feature class to a shapefile, an attribute field named 'POPULATION_GROWTH_RATE' is truncated to 'POPULATIO_'.",
        "عند تصدير فئة معالم من الجيوداتابيس إلى shapefile، تم اقتطاع اسم الحقل 'POPULATION_GROWTH_RATE' إلى 'POPULATIO_'.",
        "What causes this attribute field name truncation?",
        "ما سبب اقتطاع اسم هذا الحقل السماتي؟",
        [["The dBASE (.dbf) table specification used by shapefiles limits field names to a maximum of 10 characters", "مواصفات جدول dBASE (.dbf) المستخدم في ملفات shapefile تقيد أسماء الحقول بحد أقصى 10 أحرف فقط"], ["The coordinate system does not support long words", "نظام الإحداثيات لا يدعم الكلمات الطويلة"], ["ArcGIS Pro requires an Advanced license for longer column names", "يتطلب ArcGIS Pro ترخيصاً متقدماً لأسماء الأعمدة الطويلة"], ["The font size in the table was set to 10 points", "كان حجم الخط في الجدول مضبوطاً على 10 نقاط"]],
        "A",
        "The legacy dBASE format (.dbf) underlying shapefiles restricts column names to exactly 10 characters, truncating longer names. Geodatabases support field names up to 64 characters (or 31 in some RDBMS).",
        "يقيد تنسيق dBASE (.dbf) القديم المعتمد في shapefile أسماء الأعمدة بـ 10 محارف كحد أقصى فيقتطع الأسماء الطويلة؛ بينما تدعم قواعد بيانات الجيوداتابيس أسماء حقول حتى 64 حرفاً.",
        {"B": ["Coordinate systems manage spatial math, not database column headers.", "أنظمة الإحداثيات تدير الإسقاط ولا علاقة لها برؤوس الأعمدة."], "C": ["Column name limits are defined by file format specifications, not license levels.", "حدود أسماء الأعمدة تحددها مواصفات صيغة الملف."], "D": ["Font display sizes do not alter database schemas.", "أحجام الخطوط لا تغير هيكل قواعد البيانات."]},
        "gdb"
    ),
    # 43
    (
        "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes", "Beginner", "Tool-based", ["Snapping"],
        "An editor needs to place a water valve symbol exactly at the geometric crossing point where a water main crosses under a gas pipeline.",
        "يحتاج محرر لوضع رمز محبس مياه عند نقطة التقاطع الهندسي الدقيقة التي يمر فيها خط مياه رئيسي أسفل أنبوب غاز.",
        "Which snapping agent should be enabled to snap directly to the line crossing?",
        "أي نمط انجذاب يجب تفعيله للانجذاب مباشرة إلى تقاطع الخطين؟",
        [["Intersection Snapping", "انجذاب التقاطعات (Intersection Snapping)"], ["Point Snapping", "انجذاب النقاط (Point Snapping)"], ["Tangent Snapping", "انجذاب المماس (Tangent Snapping)"], ["Midpoint Snapping", "انجذاب المنتصف (Midpoint Snapping)"]],
        "A",
        "Intersection Snapping snaps the editing pointer directly to the point where two lines, edges, or boundaries cross or intersect geometrically.",
        "يجذب نمط Intersection Snapping مؤشر الرسم مباشرة إلى النقطة التي يتقاطع أو يتعامد فيها خطان أو حافتان هندسياً.",
        {"B": ["Point snapping snaps to existing point features.", "ينجذب Point snapping للنقاط القائمة."], "C": ["Tangent snapping snaps tangent to a curve.", "ينجذب Tangent للمماس المنحني."], "D": ["Midpoint snapping snaps to segment centers.", "ينجذب Midpoint لمنتصف القطعة."]},
        "editing"
    ),
    # 44
    (
        "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes", "Beginner", "Tool-based", ["Merge"],
        "An analyst selects three adjacent parcel polygons in the active edit layer and opens the Merge tool in the Modify Features pane.",
        "حدد محلل 3 مضلعات أراضٍ متجاورة في الطبقة النشطة وفتح أداة Merge في نافذة Modify Features.",
        "What choice must the analyst make before completing the merge operation?",
        "ما الاختيار الذي يجب على المحلل اتخاذه قبل إتمام عملية الدمج؟",
        [["Choose which original feature's attributes will be preserved in the merged feature", "اختيار أي من المعالم الأصلية سيتم الحفاظ على سماتها في المعلم المدمج الناتج"], ["Specify the raster cell size", "تحديد حجم خلية الراستر"], ["Choose a map projection transformation", "اختيار تحويل إسقاط الخريطة"], ["Enter a password to encrypt the parcels", "إدخال كلمة مرور لتشفير الأراضي"]],
        "A",
        "When merging features in-place, the editing Merge tool requires selecting the target feature whose attributes will be retained in the resulting unified feature.",
        "عند دمج المعالم في مكانها، تطلب أداة Merge في نافذة التحرير اختيار المعلم المستهدف الذي سيتم الاحتفاظ بسماته وبياناته في المعلم الموحد الجديد.",
        {"B": ["Merge feature editing is purely vector.", "دمج المعالم اتجاهي صرف ولا علاقة له بالراستر."], "C": ["Coordinate transformations do not occur during in-place merges.", "لا تحدث تحويلات إسقاطية أثناء الدمج."], "D": ["Geodatabase editing does not password-protect features.", "التحرير لا يشفر المعالم بكلمات مرور."]},
        "editing"
    ),
    # 45
    (
        "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Technical", ["Rebuild Indexes"],
        "After appending 500,000 records into a feature class, pan and zoom performance in the map slows significantly.",
        "بعد إضافة 500,000 سجل جديد إلى فئة معالم، أصبح أداء التحريك والتكبير على الخريطة بطيئاً جداً.",
        "Which tool should be run to optimize spatial search trees on the feature class?",
        "أي أداة يجب تشغيلها لتحسين شجرة البحث المكاني على فئة المعالم؟",
        [["Rebuild Indexes (rebuilding the Spatial Index)", "Rebuild Indexes (إعادة بناء الفهرس المكاني)"], ["Project", "Project"], ["Calculate Field", "Calculate Field"], ["Enable COGO", "Enable COGO"]],
        "A",
        "Rebuilding the Spatial Index recalculates the bounding R-tree or spatial grid index, reflecting the new geometry distribution and restoring rapid spatial query retrieval.",
        "تُعيد أداة Rebuild Indexes حساب الفهرس المكاني (Spatial Index) ليتوافق مع توزيع المعالم الجديدة، مما يستعيد سرعة الاستعلامات المكانية والتصفح السلس.",
        {"B": ["Project transforms coordinate systems.", "أداة Project تعيد الإسقاط."], "C": ["Calculate field edits attribute values.", "حساب الحقل يعدل السمات."], "D": ["Enable COGO adds surveying fields.", "تفعيل COGO يضيف حقول المسح."]},
        "gdb"
    ),
    # 46
    (
        "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes", "Intermediate", "Tool-based", ["Split"],
        "An editor splitting a parcel polygon needs the split line to run at an exact 90-degree angle (perpendicular) from the existing front street property line.",
        "يحتاج محرر يقسم مضلع أرض إلى جعل خط التقسيم ينطلق بزاوية 90 درجة بالضبط (عمودي) على خط واجهة الشارع القائم.",
        "What sketch constraint shortcut or context menu command should be used?",
        "ما هو اختصار قيد الرسم أو أمر القائمة الذي يجب استخدامه لفرض الزاوية القائمة؟",
        [["Deflection (or Perpendicular constraint)", "قيد الانحراف Deflection (أو القيد العمودي Perpendicular)"], ["Distance constraint", "قيد المسافة Distance"], ["Radius constraint", "قيد نصف القطر Radius"], ["Z-value constraint", "قيد الارتفاع Z"]],
        "A",
        "The Deflection constraint (or Perpendicular command) locks the sketch angle to a specific angular offset or exact 90° deflection relative to an existing segment.",
        "يقفل قيد الانحراف (Deflection أو الأمر العمودي Perpendicular) زاوية خط الرسم لتنطلق بزاوية متعامدة (90 درجة) بدقة بالنسبة لقطعة الخط القائمة.",
        {"B": ["Distance locks length, not angle.", "قيد المسافة يثبت الطول وليس الزاوية."], "C": ["Radius locks curve curvature.", "قيد نصف القطر للمنحنيات."], "D": ["Z-value sets elevation height.", "قيد Z يضبط الارتفاع الرأسي."]},
        "editing"
    ),
    # 47
    (
        "Manage geospatial data (raster, vector, tabular)", "Intermediate", "Tool-based", ["Upgrade Geodatabase"],
        "An analyst attempts to configure Contingent Values in a File Geodatabase created in legacy ArcGIS Desktop 10.5. The Contingent Values view is grayed out and disabled.",
        "حاول محلل تهيئة قيم مشروطة (Contingent Values) في File Geodatabase تم إنشاؤها بإصدار قديم ArcGIS Desktop 10.5، فظهرت النافذة غير مفعلة (Grayed out).",
        "What procedure must be performed first to enable modern geodatabase functionality?",
        "ما الإجراء الذي يجب تنفيذه أولاً لتمكين إمكانيات الجيوداتابيس الحديثة؟",
        [["Run the Upgrade Geodatabase tool to update the system tables to the current ArcGIS Pro release", "تشغيل أداة Upgrade Geodatabase لتحديث جداول النظام إلى إصدار ArcGIS Pro الحالي"], ["Delete the geodatabase and re-enter all data", "حذف قاعدة البيانات وإعادة إدخال كافة البيانات"], ["Reinstall Windows", "إعادة تثبيت نظام ويندوز"], ["Change the monitor resolution", "تغيير دقة الشاشة"]],
        "A",
        "Modern geodatabase capabilities (such as Contingent Values and Attribute Rules) require upgrading older geodatabase system tables using the Upgrade Geodatabase tool.",
        "تتطلب إمكانيات الجيوداتابيس الحديثة (مثل القيم المشروطة والقواعد السماتية) ترقية جداول النظام لقواعد البيانات القديمة باستخدام أداة Upgrade Geodatabase لتتوافق مع إصدار Pro.",
        {"B": ["Upgrading preserves all existing data without deletion.", "الترقية تحافظ على كافة البيانات القائمة."], "C": ["Operating system reinstallation is completely unrelated.", "إعادة تثبيت النظام لا علاقة لها بإصدار الجيوداتابيس."], "D": ["Monitor resolution has no effect on database capabilities.", "دقة الشاشة لا تؤثر على قواعد البيانات."]},
        "gdb"
    ),
    # 48
    (
        "Manage geospatial data (raster, vector, tabular)", "Beginner", "Tool-based", ["Export Features"],
        "An analyst needs to create a new feature class containing only active hydrants (STATUS = 'Active') from a master hydrant dataset of 100,000 features, while excluding unnecessary inspection history fields.",
        "يحتاج محلل لإنشاء فئة معالم جديدة تحتوي فقط على محابس الإطفاء النشطة (STATUS = 'Active') من طبقة رئيسية تضم 100,000 معلم، مع استبعاد حقول سجلات التفتيش القديمة غير الضرورية.",
        "Which tool performs filtering and field mapping in a single export step?",
        "أي أداة تؤدي التصفية وتعديل الحقول في خطوة تصدير واحدة؟",
        [["Export Features (with SQL Expression and Field Map configuration)", "Export Features (مع كتابة تعبير SQL وضبط خريطة الحقول Field Map)"], ["Buffer", "Buffer (النطاق)"], ["Check Geometry", "Check Geometry (فحص الهندسة)"], ["Enable Archiving", "Enable Archiving (تفعيل الأرشفة)"]],
        "A",
        "Export Features (formerly Feature Class to Feature Class) supports an inline SQL filter expression and comprehensive Field Mapping to rename, reorder, or drop fields during export.",
        "تدعم أداة Export Features كتابة استعلام SQL لتصفية المعالم أثناء التصدير، مع توفير خريطة الحقول (Field Map) لحذف أو إعادة تسمية الحقول غير المطلوبة في خطوة واحدة.",
        {"B": ["Buffer creates proximity zones.", "تنشئ Buffer مناطق حرم."], "C": ["Check Geometry identifies topological errors.", "تفحص Check Geometry العيوب الهندسية."], "D": ["Enable Archiving tracks edit history.", "تتبع Enable Archiving التعديلات التاريخية."]},
        "gdb"
    )
]

for item in remaining_scenarios:
    qid = f"DM-S-{len(items)+1:03d}"
    items.append(s(qid, item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]))

print(f"Total DM Scenarios: {len(items)} (target 48)")

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Saved scenarios/data-management.json successfully.")
