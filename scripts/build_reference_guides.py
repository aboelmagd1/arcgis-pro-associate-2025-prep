# -*- coding: utf-8 -*-
"""
Generate tool-comparisons.json, troubleshooting.json, and study-planner.json.
"""
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ref_dir = os.path.join(base_dir, 'public', 'data', 'references')
os.makedirs(ref_dir, exist_ok=True)

# 1. Tool Comparisons (12 critical exam comparison pairs)
tool_comparisons = [
    {
        "id": "TC-001",
        "title": {"en": "Define Projection vs. Project", "ar": "Define Projection مقابل Project"},
        "domain": "Data Management",
        "toolA": {"name": "Define Projection", "syntax": "arcpy.management.DefineProjection(in_dataset, coor_system)"},
        "toolB": {"name": "Project", "syntax": "arcpy.management.Project(in_dataset, out_dataset, out_coor_system, transform_method)"},
        "keyDifference": {
            "en": "Define Projection only updates coordinate system metadata headers without modifying raw coordinate numbers. Project creates a new output dataset and calculates coordinate transformations.",
            "ar": "تعدل أداة Define Projection البيانات الوصفية للإسقاط في الترويسة فقط دون تعديل أرقام الإحداثيات؛ بينما تنشئ أداة Project ملفاً جديداً وتحسب التحويلات الرياضية للإحداثيات."
        },
        "useCaseA": {"en": "Dataset with Unknown Spatial Reference whose coordinates are known.", "ar": "بيانات مجهولة الإسقاط ولكن إحداثياتها معروفة ومسجلة بشكل سليم."},
        "useCaseB": {"en": "Changing a dataset from GCS (degrees) to PCS (meters/feet) or between datums.", "ar": "تحويل البيانات من نظام جغرافي (درجات) إلى مسقط (أمتار) أو بين مراجع مختلفة."},
        "examTrap": {
            "en": "Running Project on an Unknown coordinate system corrupts the geometry permanently.",
            "ar": "تشغيل Project على بيانات مجهولة الإسقاط يشوه الإحداثيات ويتلف الطبقة نهائياً."
        }
    },
    {
        "id": "TC-002",
        "title": {"en": "Clip vs. Intersect", "ar": "Clip مقابل Intersect"},
        "domain": "Analysis and Geoprocessing",
        "toolA": {"name": "Clip", "syntax": "arcpy.analysis.Clip(in_features, clip_features, out_feature_class)"},
        "toolB": {"name": "Intersect", "syntax": "arcpy.analysis.Intersect(in_features, out_feature_class)"},
        "keyDifference": {
            "en": "Clip acts like a cookie cutter, retaining ONLY the input layer's attributes. Intersect computes geometric intersections and appends attributes from ALL input layers.",
            "ar": "تعمل Clip كقالب البسكويت وتحتفظ بسمات طبقة الإدخال فقط؛ بينما تدمج Intersect المساحات المشتركة وتلحق سمات كافة الطبقات المدخلة في جدول النتائج."
        },
        "useCaseA": {"en": "Trimming layers to a study area boundary without adding boundary fields.", "ar": "قص الطبقات عند حدود منطقة الدراسة دون إضافة حقول حدود المنطقة للجدول."},
        "useCaseB": {"en": "Multi-layer overlay determining which land use parcels fall inside flood zones.", "ar": "تراكب مكاني لمعرفة نوع استخدام الأراضي الواقع داخل مناطق الفيضان مع دمج البيانات."}
    },
    {
        "id": "TC-003",
        "title": {"en": "Spatial Join vs. Add Join", "ar": "Spatial Join مقابل Add Join"},
        "domain": "Data Management",
        "toolA": {"name": "Spatial Join", "syntax": "arcpy.analysis.SpatialJoin(target_features, join_features, out_feature_class)"},
        "toolB": {"name": "Add Join", "syntax": "arcpy.management.AddJoin(in_layer_or_view, in_field, join_table, join_field)"},
        "keyDifference": {
            "en": "Spatial Join matches records based on geometric spatial relationships (within distance, contains, intersects). Add Join matches records based on common attribute key values.",
            "ar": "يربط Spatial Join السجلات استناداً إلى العلاقات المكانية الهندسية (المسافة، الاحتواء، التقاطع)؛ بينما يربط Add Join السجلات بناءً على تطابق قيم حقل سماتي مشترك."
        },
        "useCaseA": {"en": "Finding the nearest hospital to each school.", "ar": "إيجاد أقرب مستشفى لكل مدرسة وحساب المسافة الفاصلة بينهما."},
        "useCaseB": {"en": "Attaching an external demographic Excel spreadsheet to census tracts using GEOID.", "ar": "ربط جدول إكسل خارجي بمضلعات التعداد السكاني باستخدام كود GEOID."}
    },
    {
        "id": "TC-004",
        "title": {"en": "Union vs. Intersect", "ar": "Union مقابل Intersect"},
        "domain": "Analysis and Geoprocessing",
        "toolA": {"name": "Union", "syntax": "arcpy.analysis.Union(in_features, out_feature_class)"},
        "toolB": {"name": "Intersect", "syntax": "arcpy.analysis.Intersect(in_features, out_feature_class)"},
        "keyDifference": {
            "en": "Union outputs all areas from all polygon inputs (non-overlapping areas receive Nulls). Intersect only outputs areas where all inputs overlap.",
            "ar": "تخرج أداة Union كافة المساحات المتراكبة والمنفردة لجميع الطبقات (مع ملء السمات غير الموجودة بـ Null)؛ بينما تقتصر Intersect على المساحات المتراكبة فقط."
        },
        "useCaseA": {"en": "Combining overlapping zoning and conservation polygons without losing any footprint.", "ar": "دمج مضلعات التخطيط والحماية دون فقدان أي مساحة جغرافية."},
        "useCaseB": {"en": "Finding exact zones where zoning AND flood hazard coincide.", "ar": "إيجاد المساحات المشتركة فقط التي يلتقي فيها التخطيط مع خطر الفيضان."}
    },
    {
        "id": "TC-005",
        "title": {"en": "Near vs. Generate Near Table", "ar": "Near مقابل Generate Near Table"},
        "domain": "Analysis and Geoprocessing",
        "toolA": {"name": "Near", "syntax": "arcpy.analysis.Near(in_features, near_features)"},
        "toolB": {"name": "Generate Near Table", "syntax": "arcpy.analysis.GenerateNearTable(in_features, near_features, out_table)"},
        "keyDifference": {
            "en": "Near writes NEAR_FID and NEAR_DIST directly onto the input table for the single closest feature. Generate Near Table outputs a standalone table supporting 1:Many matches within search radius.",
            "ar": "تكتب أداة Near أقرب معلم واحد فقط داخل جدول الطبقة المدخلة؛ بينما تنشئ Generate Near Table جدولاً مستقلاً يدعم علاقة 1:Many لكافة المعالم ضمن نصف القطر."
        },
        "useCaseA": {"en": "Quickly finding the nearest fire hydrant to each building.", "ar": "تحديد أقرب محبس حريق لكل مبنى بسرعة في الجدول نفسه."},
        "useCaseB": {"en": "Finding all competitors located within 5 miles of each retail store.", "ar": "حصر كافة المنافسين الواقعين على مسافة 5 أميال من كل متجر في جدول تفصيلي."}
    },
    {
        "id": "TC-006",
        "title": {"en": "Raster Functions vs. Geoprocessing Tools", "ar": "دوال الراستر مقابل أدوات المعالجة الجغرافية"},
        "domain": "Analysis and Geoprocessing",
        "toolA": {"name": "Raster Functions", "syntax": "ArcGIS Pro Image Analyst / Spatial Analyst dynamic functions"},
        "toolB": {"name": "Geoprocessing Tools", "syntax": "arcpy.sa.<tool_name>() writing to physical disk"},
        "keyDifference": {
            "en": "Raster Functions process pixels on-the-fly in-memory for the visible display extent with zero disk storage. Geoprocessing tools calculate all pixels across the entire file and write permanent files to disk.",
            "ar": "تعالج دوال الراستر البكسلات فورياً داخل الذاكرة لنطاق العرض الظاهر فقط وتستهلك مساحة تخزين صفرية؛ بينما تحسب أدوات المعالجة كافة خلايا الملف وتكتب ملفاً دائماً على القرص."
        },
        "useCaseA": {"en": "Real-time exploratory visualization, NDVI calculation on 500GB imagery.", "ar": "المعاينة والاستكشاف الفوري وحساب NDVI لصور فضائية ضخمة دون شغل القرص."},
        "useCaseB": {"en": "Producing permanent archive datasets required for downstream legacy modeling.", "ar": "إنتاج طبقات راستر نهائية ومحفوظة لاستخدامها في نماذج نمذجة خارجية."}
    },
    {
        "id": "TC-007",
        "title": {"en": "Local Scene vs. Global Scene", "ar": "المشهد المحلي مقابل المشهد العالمي ثلاثي الأبعاد"},
        "domain": "Visualization",
        "toolA": {"name": "Local Scene", "syntax": "ArcGIS Pro 3D Local View (Projected Coordinate System)"},
        "toolB": {"name": "Global Scene", "syntax": "ArcGIS Pro 3D Global View (WGS 1984 or CGCS 2000)"},
        "keyDifference": {
            "en": "Local Scenes support projected planar coordinates, custom rectangular clipping extents, underground views, and local engineering. Global Scenes model the entire spherical planet in GCS WGS 1984.",
            "ar": "تدعم المشاهد المحلية الإسقاطات المستوية، والقص عند حدود مستطيلة، وعرض البنى التحتية تحت الأرض؛ بينما تمثل المشاهد العالمية كوكب الأرض الكروي بالكامل بنظام WGS 1984."
        },
        "useCaseA": {"en": "City campus 3D buildings, mining tunnels, engineering excavations.", "ar": "المباني الحضرية، والأنفاق التعدينية، والحفريات الهندسية تحت السطح."},
        "useCaseB": {"en": "Global airline flight paths, hurricane tracks across continents.", "ar": "مسارات الطيران العالمية، وحركة الأعاصير عبر القارات."}
    },
    {
        "id": "TC-008",
        "title": {"en": "Coded Value Domains vs. Range Domains", "ar": "مجالات القيم الكودية مقابل مجالات النطاق"},
        "domain": "Data Management",
        "toolA": {"name": "Coded Value Domain", "syntax": "arcpy.management.CreateDomain(..., 'CODED')"},
        "toolB": {"name": "Range Domain", "syntax": "arcpy.management.CreateDomain(..., 'RANGE')"},
        "keyDifference": {
            "en": "Coded Value Domains restrict inputs to an explicit list of discrete code/description pairs (Text, Numeric). Range Domains enforce numeric minimum and maximum bounds (Numbers, Dates).",
            "ar": "تقيد مجالات القيم الكودية الإدخال بقائمة خيارات محددة ككود ووصف (للنصوص والأرقام)؛ بينما تفرض مجالات النطاق حداً أدنى وأعلى للقيم الرقمية أو التواريخ."
        },
        "useCaseA": {"en": "Pipe material: PVC, Steel, Ductile Iron.", "ar": "مادة الأنبوب: خيارات محددة مثل حديد زهر، بولي إيثيلين، صلب."},
        "useCaseB": {"en": "Water pressure: between 30 and 120 PSI.", "ar": "ضغط شبكة المياه: بين 30 و 120 رطل/بوصة مربعة."}
    },
    {
        "id": "TC-009",
        "title": {"en": "Geodatabase Topology vs. Map Topology", "ar": "طوبولوجيا قاعدة البيانات مقابل طوبولوجيا الخريطة"},
        "domain": "Data Management",
        "toolA": {"name": "Geodatabase Topology", "syntax": "arcpy.management.CreateTopology() in Feature Dataset"},
        "toolB": {"name": "Map Topology", "syntax": "Edit Ribbon > Topology dropdown > Map Topology"},
        "keyDifference": {
            "en": "Geodatabase Topology enforces persistent formal spatial integrity rules (Must Not Overlap, etc.) with validation error logging. Map Topology enables dynamic shared edge/vertex editing on the fly without rules.",
            "ar": "تفرض طوبولوجيا قاعدة البيانات قواعد سلامة مكانية دائمة ومسجلة مع فحص الأخطاء وحفظها؛ بينما تتيح طوبولوجيا الخريطة تحريك الحواف والرؤوس المشتركة تفاعلياً أثناء التحرير دون قواعد."
        },
        "useCaseA": {"en": "Corporate parcel fabric data quality compliance.", "ar": "ضمان الجودة المكانية الرسمية لقطع الأراضي المؤسسية ومنع التداخلات."},
        "useCaseB": {"en": "Quickly reshaping a boundary between a forest and road layer simultaneously.", "ar": "تعديل حافة مشتركة تفاعلياً بين طبقتي غابات وطرق في آن واحد."}
    },
    {
        "id": "TC-010",
        "title": {"en": "Web Feature Layer vs. Vector Tile Layer", "ar": "طبقة معالم ويب مقابل طبقة قوالب متجهة"},
        "domain": "Layouts and Sharing",
        "toolA": {"name": "Web Feature Layer", "syntax": "ArcGIS Online / Enterprise Feature Service"},
        "toolB": {"name": "Vector Tile Layer", "syntax": "ArcGIS Online / Enterprise Vector Tile Service"},
        "keyDifference": {
            "en": "Web Feature Layers support full geometry/attribute editing, field apps, and live spatial queries. Vector Tile Layers are pre-packaged compressed tiles optimized for high-speed basemaps and client-side styling.",
            "ar": "تدعم طبقة معالم الويب التحرير الميداني والاستعلامات التفاعلية وتعديل البيانات؛ بينما توفر القوالب المتجهة خرائط أساس فائقة السرعة وخفيفة مع دعم تعديل الألوان دون دعم التحرير."
        },
        "useCaseA": {"en": "Field inspections in ArcGIS Field Maps.", "ar": "التحرير وجمع البيانات الميدانية في تطبيق ArcGIS Field Maps."},
        "useCaseB": {"en": "High-DPI responsive corporate basemaps.", "ar": "خرائط أساس للمؤسسة سريعة التحميل على الهواتف والشاشات عالية الدقة."}
    },
    {
        "id": "TC-011",
        "title": {"en": "Project Package (.ppkx) vs. Map Package (.mpkx)", "ar": "حزمة المشروع مقابل حزمة الخريطة"},
        "domain": "Layouts and Sharing",
        "toolA": {"name": "Project Package (.ppkx)", "syntax": "arcpy.management.PackageProject()"},
        "toolB": {"name": "Map Package (.mpkx)", "syntax": "arcpy.management.PackageMap()"},
        "keyDifference": {
            "en": "Project Package bundles the entire project: all maps, scenes, layouts, custom toolboxes, and geodatabases. Map Package encapsulates a single 2D map or 3D scene with its operational data.",
            "ar": "تحزم حزمة المشروع (.ppkx) كامل المشروع بجميع خرائطه ومشاهده ولوحاته وصناديق أدواته؛ بينما تقتصر حزمة الخريطة (.mpkx) على خريطة أو مشهد منفرد وبياناته التشغيلية."
        },
        "useCaseA": {"en": "Handing off an entire consulting study with layouts to a client.", "ar": "تسليم دراسة هندسية متكاملة بجميع لوحات الطباعة للعميل."},
        "useCaseB": {"en": "Distributing one public map without exposing confidential layouts in the project.", "ar": "مشاركة خريطة معينة مع جهة خارجية دون إظهار اللوحات السرية الأخرى."}
    },
    {
        "id": "TC-012",
        "title": {"en": "Calculated Field vs. Attribute Rules", "ar": "أداة Calculate Field مقابل قواعد السمات Attribute Rules"},
        "domain": "Data Management",
        "toolA": {"name": "Calculate Field", "syntax": "arcpy.management.CalculateField(in_table, field, expression)"},
        "toolB": {"name": "Attribute Rules", "syntax": "arcpy.management.AddAttributeRule(in_table, name, type)"},
        "keyDifference": {
            "en": "Calculate Field is an ad-hoc batch geoprocessing tool executed manually or on a schedule. Attribute Rules are event-driven database behaviors that fire automatically upon feature creation, update, or deletion.",
            "ar": "Calculate Field أداة تشغيل يدوية لتحديث الحقول دفعة واحدة؛ بينما تعمل قواعد السمات كمعالجات تلقائية داخل قاعدة البيانات تعمل فورياً عند إنشاء أو تعديل أي معلم."
        },
        "useCaseA": {"en": "Retroactive recalculation of millions of existing legacy records.", "ar": "تحديث ملايين السجلات القديمة المخزنة مسبقاً في قاعدة البيانات دفعة واحدة."},
        "useCaseB": {"en": "Automating geodesic acreage calculation dynamically every time an editor draws a parcel.", "ar": "حساب المساحة الجيوديسية بالفدان تلقائياً في كل مرة يرسم فيها المحرر عقاراً جديداً."}
    }
]

with open(os.path.join(ref_dir, 'tool-comparisons.json'), 'w', encoding='utf-8') as f:
    json.dump(tool_comparisons, f, ensure_ascii=False, indent=2)
print("Saved public/data/references/tool-comparisons.json")

# 2. Troubleshooting Guides (12 comprehensive GIS troubleshooting workflows)
troubleshooting_guides = [
    {
        "id": "TB-001",
        "title": {"en": "Resolving Missing Datum Transformations (Datum Shift Error)", "ar": "حل مشكلة غياب تحويل المرجع الإسنادي (خطأ إزاحة المرجع)"},
        "domain": "Data Management",
        "symptom": {"en": "Layers do not align visually, displaying a systematic spatial offset of 10 to 100 meters, or ArcGIS Pro displays a missing transformation warning.", "ar": "عدم تطابق الطبقات مكانياً وظهور إزاحة منتظمة بمقدار 10 إلى 100 متر أو ظهور تحذير Missing Transformation."},
        "rootCause": {"en": "The layers use different underlying geographic datums (e.g. NAD 1927 vs NAD 1983) and no transformation method was configured.", "ar": "اعتماد الطبقات على مراجع جيوديسية مختلفة (مثل NAD 1927 و NAD 1983) دون تحديد معادلة تحويل المرجع المناسبة."},
        "resolutionSteps": [
            {"step": 1, "text": {"en": "Open Map Properties > Coordinate Systems > Transformations tab.", "ar": "افتح Map Properties وانتقل لتبويب Coordinate Systems ثم Transformations."}},
            {"step": 2, "text": {"en": "Identify the source and target datums.", "ar": "حدد المرجع الإسنادي للمصدر والمرجع المستهدف للخريطة."}},
            {"step": 3, "text": {"en": "Select the Esri-recommended transformation method (e.g. NAD_1983_To_WGS_1984_5).", "ar": "اختَر طريقة التحويل المعتمدة والموصى بها من Esri."}},
            {"step": 4, "text": {"en": "Click OK and verify features snap into precise spatial alignment.", "ar": "انقر موافق وتأكد من انطباق المعالم بدقة مع خريطة الأساس."}}
        ],
        "preventionTip": {"en": "Always standardize enterprise geodatabases on a single corporate coordinate system.", "ar": "توحيد نظام الإحداثيات والمرجع الإسنادي في قواعد البيانات المؤسسية دائماً."}
    },
    {
        "id": "TB-002",
        "title": {"en": "Fixing Geoprocessing Error 000258: Output Already Exists", "ar": "معالجة خطأ المعالجة الجغرافية 000258: الملف المخرج موجود مسبقاً"},
        "domain": "Analysis and Geoprocessing",
        "symptom": {"en": "Python scripts or ModelBuilder tools crash with 'ERROR 000258: Output dataset already exists'.", "ar": "توقف السكربت أو النموذج مع ظهور رسالة ERROR 000258: Output dataset already exists."},
        "rootCause": {"en": "ArcGIS Pro geoprocessing environment by default protects existing files from accidental overwriting.", "ar": "إعدادات الأمان الافتراضية للبرنامج تمنع استبدال الملفات الموجودة على القرص دون إذن صريح."},
        "resolutionSteps": [
            {"step": 1, "text": {"en": "In Python scripts, add `arcpy.env.overwriteOutput = True` at the top of the file.", "ar": "في سكربت بايثون، أضف السطر arcpy.env.overwriteOutput = True في بداية الكود."}},
            {"step": 2, "text": {"en": "In ArcGIS Pro desktop UI, open Analysis > Geoprocessing Options > check 'Overwrite the outputs of geoprocessing operations'.", "ar": "في واجهة البرنامج، افتح Analysis > Geoprocessing Options وفعل خيار السماح باستبدال المخرجات."}}
        ],
        "preventionTip": {"en": "Always initialize overwriteOutput = True in automated recurring scheduled scripts.", "ar": "احرص على تفعيل overwriteOutput = True في كافة السكربتات المجدولة آلياً."}
    },
    {
        "id": "TB-003",
        "title": {"en": "Clearing Schema Locks on Geodatabase Feature Classes", "ar": "فك أقفال المخطط (Schema Locks) العالقة على قواعد البيانات الجغرافية"},
        "domain": "Data Management",
        "symptom": {"en": "Cannot add fields, delete feature classes, or modify domains; error 'Cannot acquire a schema lock'.", "ar": "تعذر إضافة حقول أو حذف طبقات أو تعديل المجالات مع ظهور خطأ Cannot acquire a schema lock."},
        "rootCause": {"en": "Another application, user session, or unclosed ArcPy cursor holds an active exclusive or shared lock.", "ar": "وجود تطبيق آخر أو مستخدم أو مؤشر ArcPy لم يُغلق يحتفظ بقفل نشط على ملفات قاعدة البيانات."},
        "resolutionSteps": [
            {"step": 1, "text": {"en": "Ensure all ArcPy scripts use `with arcpy.da.UpdateCursor(...) as cursor:` context managers to guarantee automatic lock release.", "ar": "تأكد من استخدام صيغة with مع مؤشرات بايثون لضمان فك الأقفال تلقائياً فور انتهاء الحلقة."}},
            {"step": 2, "text": {"en": "Save edits and close all other ArcGIS Pro map views referencing the layer.", "ar": "احفظ التعديلات وأغلق أي خرائط أخرى تعرض نفس الطبقة."}},
            {"step": 3, "text": {"en": "If using File GDB, close ArcGIS Pro and check for orphaned `.lock` files in Windows Explorer.", "ar": "إذا كانت قاعدة ملفية، أغلق البرنامج وتأكد من حذف ملفات .lock العالقة من المجلد."}}
        ],
        "preventionTip": {"en": "Never leave active editing sessions open when modifying database schemas.", "ar": "تجنب تعديل هيكل الجداول أثناء وجود جلسات تحرير نشطة."}
    },
    {
        "id": "TB-004",
        "title": {"en": "Resolving Half-Cell Shift in Raster Analysis", "ar": "معالجة إزاحة أجزاء الخلايا في التحليل الراستري (Snap Raster)"},
        "domain": "Analysis and Geoprocessing",
        "symptom": {"en": "Output raster cells are misaligned with input rasters by fractional pixel distances, causing stair-stepped blur artifacts.", "ar": "عدم محاذاة خلايا الراستر الناتج مع المدخلات بكسور بكسلية وظهور تشوهات بصرية متدرجة."},
        "rootCause": {"en": "Snap Raster environment was not configured to match the master reference elevation grid.", "ar": "عدم ضبط بيئة الراستر المرجعي للمحاذاة Snap Raster لتطابق شبكة الارتفاع الرئيسية."},
        "resolutionSteps": [
            {"step": 1, "text": {"en": "Open tool Environments tab before running Raster Calculator or surface tools.", "ar": "افتح تبويب البيئات في أداة التحليل قبل تنفيذ العملية."}},
            {"step": 2, "text": {"en": "Set Snap Raster to the primary baseline raster dataset.", "ar": "حدد راستر الأساس في خيار Snap Raster."}},
            {"step": 3, "text": {"en": "Set Cell Size to match the snap raster resolution.", "ar": "اضبط حجم الخلية ليتطابق مع دقة الراستر المرجعي."}}
        ],
        "preventionTip": {"en": "Set Snap Raster in project-level environments (Analysis > Environments) before starting raster projects.", "ar": "اضبط Snap Raster على مستوى المشروع كاملاً قبل بدء أي نمذجة راستر."}
    },
    {
        "id": "TB-005",
        "title": {"en": "Clearing Sharing Analyzer Fatal Error 00068 (Invalid Spatial Reference)", "ar": "حل الخطأ القاتل 00068 في فاحص المشاركة (مرجع إسقاطي غير صالح)"},
        "domain": "Layouts and Sharing",
        "symptom": {"en": "The 'Publish' button in Share As Web Layer is disabled, and Analyzer lists Error 00068.", "ar": "تعطل زر النشر وظهور الخطأ 00068 في فاحص المشاركة عند محاولة نشر طبقة ويب."},
        "rootCause": {"en": "One of the map layers has an Unknown Coordinate System or lacks spatial reference metadata.", "ar": "إحدى طبقات الخريطة تفتقر لبيانات الإسقاط وتحمل حالة Unknown Coordinate System."},
        "resolutionSteps": [
            {"step": 1, "text": {"en": "Double-click Error 00068 in Analyzer to select the offending layer in Contents.", "ar": "انقر نقراً مزدوجاً على الخطأ في الفاحص لتحديد الطبقة المعنية في شجرة المحتويات."}},
            {"step": 2, "text": {"en": "Run Define Projection tool to assign the correct coordinate system metadata.", "ar": "شغل أداة Define Projection لتعيين نظام الإحداثيات المعتمد للطبقة."}},
            {"step": 3, "text": {"en": "Click Analyze again to verify the red error clears.", "ar": "أعد النقر على Analyze وتأكد من زوال الخطأ الأحمر وتفعيل زر النشر."}}
        ],
        "preventionTip": {"en": "Always verify layer source properties before sharing resources to web portals.", "ar": "افحص خصائص مصادر الطبقات وتأكد من تعريف إسنادها قبل بدء إجراءات النشر."}
    },
    {
        "id": "TB-006",
        "title": {"en": "Resolving Scale Bar Mismatch in Multi-Frame Layouts", "ar": "تصحيح عدم توافق مقياس الرسم في اللوحات متعددة الأطر"},
        "domain": "Layouts and Sharing",
        "symptom": {"en": "Scale bar displays distances that do not match the visual extent of the map underneath it.", "ar": "عرض مقياس الرسم لمسافات غير واقعية ولا تطابق المدى المرئي للخريطة أسفله."},
        "rootCause": {"en": "The scale bar is linked to the wrong Map Frame (e.g. linked to the overview locator frame instead of the main detail frame).", "ar": "ارتباط مقياس الرسم بإطار خريطة خاطئ كربطه بخريطة الدليل بدلاً من الخريطة الرئيسية التفصيلية."},
        "resolutionSteps": [
            {"step": 1, "text": {"en": "Select the Scale Bar in layout view.", "ar": "حدد عنصر مقياس الرسم في لوحة الطباعة."}},
            {"step": 2, "text": {"en": "Open Element Properties pane > Scale Bar tab.", "ar": "افتح نافذة خصائص العنصر وانتقل لتبويب مقياس الرسم."}},
            {"step": 3, "text": {"en": "Under 'Map Frame', change the dropdown selection to the correct detailed Map Frame.", "ar": "من القائمة المنسدلة Map Frame، اختر إطار الخريطة الرئيسي الصحيح."}}
        ],
        "preventionTip": {"en": "Always give descriptive names to Map Frames (e.g. 'Main_Detail_Frame' vs 'Overview_Frame') in the Contents pane.", "ar": "احرص على تسمية أطر الخرائط بأسماء واضحة في شجرة المحتويات لتمييزها فورياً."}
    },
    {
        "id": "TB-007",
        "title": {"en": "Fixing Broken Data Links (Red Exclamation Mark in Contents)", "ar": "إصلاح مسارات البيانات المقطوعة (علامة التعجب الحمراء)"},
        "domain": "Data Management",
        "symptom": {"en": "Layers display a red exclamation mark in Contents pane and fail to draw on the map.", "ar": "ظهور علامة تعجب حمراء بجوار الطبقة في المحتويات وفشلها في الظهور على الخريطة."},
        "rootCause": {"en": "The source geodatabase or shapefile was renamed, moved, or deleted on the file system.", "ar": "تغيير اسم أو مسار أو نقل مجلد قاعدة البيانات الجغرافية على القرص الصلب."},
        "resolutionSteps": [
            {"step": 1, "text": {"en": "Click the red exclamation mark next to the layer in Contents.", "ar": "انقر على علامة التعجب الحمراء بجوار الطبقة."}},
            {"step": 2, "text": {"en": "Browse to the new location of the source dataset and click OK.", "ar": "تصفح للوصول للمسار الجديد لملف البيانات واضغط موافق."}},
            {"step": 3, "text": {"en": "ArcGIS Pro will automatically repair paths for all other layers residing in the same geodatabase.", "ar": "سيقوم البرنامج تلقائياً بإصلاح مسارات كافة الطبقات الأخرى الموجودة في نفس القاعدة."}}
        ],
        "preventionTip": {"en": "Save projects with 'Store relative pathnames to data sources' enabled in Project Properties.", "ar": "فعل خيار حفظ المسارات النسبية (Store relative pathnames) في خصائص المشروع."}
    },
    {
        "id": "TB-008",
        "title": {"en": "Fixing Spiky and Exaggerated Hillshade Rasters", "ar": "معالجة التشوّه والتسنن المفرط في تظليل التضاريس (Z-Factor)"},
        "domain": "Analysis and Geoprocessing",
        "symptom": {"en": "Hillshade raster appears extremely spiky with harsh unnatural black shadows.", "ar": "ظهور راستر التظليل التضاريسي بظلال سوداء حادة وتسننات مشوهة وغير واقعية."},
        "rootCause": {"en": "Unit mismatch between horizontal ground coordinates (XY in feet or degrees) and vertical elevation coordinates (Z in meters), left with default Z-Factor 1.0.", "ar": "عدم تطابق وحدات القياس الأفقية (أقدام أو درجات) مع الارتفاع الرأسي (أمتار) مع ترك معامل Z بقيمته الافتراضية 1.0."},
        "resolutionSteps": [
            {"step": 1, "text": {"en": "Check XY and Z units in DEM Layer Properties > Source.", "ar": "افحص وحدات XY ووحدات Z في خصائص الراستر."}},
            {"step": 2, "text": {"en": "If XY is feet and Z is meters, set Z-Factor to 3.28084. If XY is degrees (GCS), apply the appropriate latitudinal conversion factor.", "ar": "إذا كانت الوحدات أقداماً والارتفاع أمتاراً اضبط معامل Z على 3.28084، أو معامل درجات العرض المناسب."}}
        ],
        "preventionTip": {"en": "Project elevation DEMs to a local Projected Coordinate System before running surface analysis.", "ar": "أعد إسقاط راستر الارتفاع إلى نظام مسقط محلي قبل بدء التحليلات السطحية."}
    },
    {
        "id": "TB-009",
        "title": {"en": "Resolving Offline Map Download Failures in Field Maps", "ar": "حل فشل تحميل الخرائط غير المتصلة في تطبيق Field Maps"},
        "domain": "Layouts and Sharing",
        "symptom": {"en": "Field workers receive 'Download Failed' when attempting to take map areas offline.", "ar": "ظهور رسالة فشل التحميل Download Failed للمحررين الميدانيين عند تنزيل الخريطة للعمل دون إنترنت."},
        "rootCause": {"en": "One of the feature layers in the web map lacks the 'Sync' capability or GlobalIDs.", "ar": "إحدى الطبقات المنشورة تفتقر لتفعيل خاصية المزامنة Sync أو تفتقر لمعرفات GlobalIDs."},
        "resolutionSteps": [
            {"step": 1, "text": {"en": "In ArcGIS Pro, run 'Add Global IDs' on all feature classes.", "ar": "شغل أداة Add Global IDs على كافة فئات المعالم في المشروع."}},
            {"step": 2, "text": {"en": "Re-share layer with 'Enable Sync' checked in Feature Properties.", "ar": "أعد نشر الطبقة مع التأكد من تفعيل خيار Enable Sync في الخصائص."}},
            {"step": 3, "text": {"en": "Ensure all layers reference the same enterprise geodatabase if using registered data.", "ar": "تأكد من أن كافة الطبقات ترتبط بنفس قاعدة البيانات عند استخدام البيانات المسجلة."}}
        ],
        "preventionTip": {"en": "Always run Add Global IDs before publishing layers intended for field workflows.", "ar": "احرص دائماً على إضافة Global IDs قبل نشر أي طبقة موجهة للعمل الميداني."}
    },
    {
        "id": "TB-010",
        "title": {"en": "Preventing Geometry Calculation Failures in Shapefiles", "ar": "تجنب أخطاء حساب المساحات والخصائص في ملفات Shapefile"},
        "domain": "Data Management",
        "symptom": {"en": "Field names truncated to 10 characters, or area calculations fail for files exceeding 2GB.", "ar": "اقتصار أسماء الحقول على 10 أحرف وتوقف الحسابات للبيانات الأكبر من 2 جيجابايت."},
        "rootCause": {"en": "Legacy Shapefile specifications impose strict 2GB file size limits, 10-character field name limits, and lack support for Null values.", "ar": "القيود التاريخية لصيغة Shapefile التي تفرض حداً أقصى 2 جيجابايت و10 أحرف للحقل ولا تدعم القيم الفارغة."},
        "resolutionSteps": [
            {"step": 1, "text": {"en": "Run 'Feature Class To Geodatabase' to migrate shapefiles into a File Geodatabase.", "ar": "شغل أداة Feature Class To Geodatabase لنقل البيانات إلى قاعدة بيانات جغرافية حديثة."}},
            {"step": 2, "text": {"en": "Perform all calculations and edits within the geodatabase environment.", "ar": "أجرِ كافة العمليات الحسابية والتحرير داخل بيئة قاعدة البيانات الجغرافية."}}
        ],
        "preventionTip": {"en": "Never use shapefiles for production GIS workflows; migrate all incoming data to File Geodatabases.", "ar": "تجنب استخدام shapefile في المشاريع الإنتاجية وقم بترحيلها لقواعد بيانات فور استلامها."}
    },
    {
        "id": "TB-011",
        "title": {"en": "Troubleshooting ModelBuilder Infinite Execution Loops", "ar": "استكشاف وحل الحلقات التكرارية اللانهائية في ModelBuilder"},
        "domain": "Analysis and Geoprocessing",
        "symptom": {"en": "ModelBuilder runs continuously without terminating, endlessly overwriting the same output file.", "ar": "استمرار النموذج في العمل دون توقف وإعادة كتابة نفس ملف المخرج باستمرار."},
        "rootCause": {"en": "The tool output was saved into the same folder being iterated over by the iterator, feeding new outputs back into the loop.", "ar": "حفظ ملفات الإخراج في نفس المجلد الذي يفحصه المكرر مما يعيد إدخال النتائج الجديدة في الحلقة."},
        "resolutionSteps": [
            {"step": 1, "text": {"en": "Save tool outputs into a separate destination folder or geodatabase outside the input directory.", "ar": "احفظ المخرجات في مجلد أو قاعدة بيانات منفصلة تماماً عن مجلد المدخلات."}},
            {"step": 2, "text": {"en": "Configure wildcards in the iterator to match only original source file patterns.", "ar": "اضبط محددات Wildcard في المكرر لمطابقة ملفات المصدر الأصلية فقط."}}
        ],
        "preventionTip": {"en": "Always isolate raw input data from derived analytical outputs in separate workspaces.", "ar": "افصل دائماً بين مجلدات البيانات الخام ومجلدات المخرجات التحليلية في مساحات عمل مستقلة."}
    },
    {
        "id": "TB-012",
        "title": {"en": "Fixing Broken Dynamic Text Expressions in Map Series", "ar": "إصلاح وسوم النصوص الديناميكية المعطلة في سلاسل الخرائط"},
        "domain": "Layouts and Sharing",
        "symptom": {"en": "Dynamic text displays raw XML tags (e.g. `<dyn type=\"page\".../>`) on the page layout rather than evaluated text.", "ar": "عرض وسوم XML النصية الخام على لوحة الطباعة بدلاً من تقييمها وعرض النصوص الصحيحة."},
        "rootCause": {"en": "Syntax typos in tag property names, unclosed tags, or referencing field names that do not exist in the index layer.", "ar": "خطأ إملائي في خصائص الوسم أو عدم إغلاق الوسم أو استدعاء حقل غير موجود في طبقة الفهرس."},
        "resolutionSteps": [
            {"step": 1, "text": {"en": "Verify that Spatial Map Series is actively enabled in Layout Properties.", "ar": "تأكد من تفعيل سلسلة الخرائط المكانية في خصائص اللوحة أولاً."}},
            {"step": 2, "text": {"en": "Check exact spelling and case sensitivity of attribute field names in the tag.", "ar": "تحقق من مطابقة اسم الحقل المكتوب في الوسم مع اسم حقل طبقة الفهرس بدقة."}},
            {"step": 3, "text": {"en": "Use Insert > Dynamic Text dropdown menu rather than manually typing raw XML strings.", "ar": "استخدم قائمة Insert > Dynamic Text لإدراج الوسوم الجاهزة بدلاً من كتابتها يدوياً."}}
        ],
        "preventionTip": {"en": "Select dynamic text presets directly from the ribbon to prevent syntax typos.", "ar": "اختر القوالب الجاهزة للنصوص الديناميكية من الشريط العلوي لتفادي الأخطاء الكتابية."}
    }
]

with open(os.path.join(ref_dir, 'troubleshooting.json'), 'w', encoding='utf-8') as f:
    json.dump(troubleshooting_guides, f, ensure_ascii=False, indent=2)
print("Saved public/data/references/troubleshooting.json")

# 3. Study Planner (4-Week structured roadmap)
study_planner = {
    "title": {"en": "EAPA_2025 4-Week Accelerated Certification Study Schedule", "ar": "خطة المذاكرة المكثفة لاجتياز اختبار EAPA_2025 في 4 أسابيع"},
    "examOverview": {
        "code": "EAPA_2025",
        "title": "ArcGIS Pro Associate 2025",
        "questions": 75,
        "timeMinutes": 90,
        "passingScore": "~70%",
        "domainWeights": {
            "Data Management": 32,
            "Visualization": 25,
            "Analysis and Geoprocessing": 25,
            "Layouts and Sharing": 18
        }
    },
    "weeks": [
        {
            "weekNumber": 1,
            "domain": "Data Management (32%)",
            "title": {"en": "Week 1: Geodatabase Schemas, Integrity Rules & Precision Editing", "ar": "الأسبوع 1: هياكل قواعد البيانات، قواعد السلامة، والتحرير المساحي الدقيق"},
            "focusModules": ["M1", "M2", "M3", "M4"],
            "targetWorkflows": ["WF-001", "WF-002", "WF-003", "WF-004", "WF-005", "WF-006", "WF-007", "WF-008", "WF-009", "WF-010"],
            "dailyTasks": [
                {"day": 1, "task": {"en": "Study File Geodatabase vs Shapefile limitations (2GB, 10-char names) and capacity keywords.", "ar": "دراسة الفروق بين قواعد البيانات و Shapefile ومفتاح السعة 256TB."}},
                {"day": 2, "task": {"en": "Master Domains (Coded vs Range) and Subtypes (Short/Long integer) configuration.", "ar": "إتقان إعداد المجالات والأنماط الفرعية وسياسات الانقسام."}},
                {"day": 3, "task": {"en": "Build Geodatabase Topology and fix overlaps/gaps in Error Inspector.", "ar": "بناء طوبولوجيا قاعدة البيانات وتصحيح الأخطاء في Error Inspector."}},
                {"day": 4, "task": {"en": "Implement Arcade Calculation and Constraint Attribute Rules.", "ar": "كتابة قواعد السمات للحساب الفوري والقيود بلغة Arcade."}},
                {"day": 5, "task": {"en": "Master Coordinate Systems: Define Projection vs Project and Datum Transformations.", "ar": "التحكم في أنظمة الإحداثيات: Define Projection مقابل Project."}},
                {"day": 6, "task": {"en": "Complete 48 Data Management Scenarios and 80 MCQs in Exam Simulator.", "ar": "حل كافة أسئلة وسيناريوهات إدارة البيانات (128 سؤالاً) في المحاكي."}},
                {"day": 7, "task": {"en": "Weekly Diagnostic Review and weak topic reinforcement.", "ar": "مراجعة تقرير الأداء الأسبوعي وتثبيت النقاط الضعيفة."}}
            ]
        },
        {
            "weekNumber": 2,
            "domain": "Visualization (25%)",
            "title": {"en": "Week 2: Cartography, Advanced Symbology, Maplex & 3D Scenes", "ar": "الأسبوع 2: الكارتوغرافيا، الرموز المتقدمة، محرك Maplex، والمشاهد ثلاثية الأبعاد"},
            "focusModules": ["M5", "M6", "M7"],
            "targetWorkflows": ["WF-011", "WF-012", "WF-013", "WF-014", "WF-015", "WF-016", "WF-017"],
            "dailyTasks": [
                {"day": 8, "task": {"en": "Master all 7 classification methods (Jenks, Quantile, Equal, Standard Deviation).", "ar": "دراسة طرق التصنيف السبعة وفروقها الرياضية وحالات استخدامها."}},
                {"day": 9, "task": {"en": "Configure multi-variable symbology (driving size and rotation concurrently).", "ar": "تهيئة الرموز متعددة المتغيرات للتحكم بالحجم والتدوير معاً."}},
                {"day": 10, "task": {"en": "Build complex Maplex multi-line label expressions and resolve overlaps.", "ar": "كتابة تعبيرات تسميات Maplex متعددة الأسطر وحل التصادمات."}},
                {"day": 11, "task": {"en": "Set up 3D Local Scenes with extrusion, elevation draping, and illumination.", "ar": "بناء المشاهد ثلاثية الأبعاد مع بثق المباني والإضاءة الشمسية."}},
                {"day": 12, "task": {"en": "Configure Time Slider and Range Slider for temporal and indoor filtering.", "ar": "تهيئة منزلق الوقت ومنزلق المدى للفلترة الزمنية والأدوار."}},
                {"day": 13, "task": {"en": "Practice 38 Visualization Scenarios and 63 MCQs in Exam Simulator.", "ar": "حل كافة أسئلة وسيناريوهات العرض البصري (101 سؤال) في المحاكي."}},
                {"day": 14, "task": {"en": "Review cartographic visual hierarchy and color ramp guidelines.", "ar": "مراجعة قواعد التصميم الكارتوغرافي والتسلسل البصري."}}
            ]
        },
        {
            "weekNumber": 3,
            "domain": "Analysis and Geoprocessing (25%)",
            "title": {"en": "Week 3: Spatial Analysis, Raster Surface Modeling & Python Automation", "ar": "الأسبوع 3: التحليل المكاني، نمذجة أسطح الراستر، وأتمتة بايثون"},
            "focusModules": ["M8", "M9", "M10"],
            "targetWorkflows": ["WF-018", "WF-019", "WF-020", "WF-021", "WF-022", "WF-023", "WF-024"],
            "dailyTasks": [
                {"day": 15, "task": {"en": "Master environment precedence and Snap Raster half-cell shift prevention.", "ar": "إتقان أسبقية البيئات وضبط Snap Raster لمنع إزاحة الخلايا."}},
                {"day": 16, "task": {"en": "Execute multi-criteria raster suitability modeling with Map Algebra Con().", "ar": "تنفيذ نمذجة الملاءمة المكانية باستخدام دالة Con وجبر الخرائط."}},
                {"day": 17, "task": {"en": "Execute Hydrology workflow (Fill -> Flow Direction -> Flow Accumulation -> Watershed).", "ar": "إتقان مسار التحليل الهيدرولوجي واستخلاص أحواض التصريف."}},
                {"day": 18, "task": {"en": "Master Network Analyst solvers (Service Area, Closest Facility, Route TSP).", "ar": "إتقان محللات الشبكات (نطاق الخدمة، أقرب منشأة، المسار الأمثل)."}},
                {"day": 19, "task": {"en": "Build automated ModelBuilder models with iterators and `%Name%` substitution.", "ar": "بناء نماذج ModelBuilder بالمكررات والاستبدال الضمني %Name%."}},
                {"day": 20, "task": {"en": "Write ArcPy da.SearchCursor and da.UpdateCursor scripts with context managers.", "ar": "كتابة سكربتات بايثون باستخدام مؤشرات البيانات وإدارة الأقفال."}},
                {"day": 21, "task": {"en": "Complete 37 Analysis Scenarios and 62 MCQs in Exam Simulator.", "ar": "حل كافة أسئلة وسيناريوهات التحليل (99 سؤالاً) في المحاكي."}}
            ]
        },
        {
            "weekNumber": 4,
            "domain": "Layouts and Sharing (18%) & Final Readiness",
            "title": {"en": "Week 4: Layouts, Spatial Map Series, Web Publishing & Full Mock Exams", "ar": "الأسبوع 4: اللوحات، سلاسل الخرائط، النشر السحابي، والاختبارات التجريبية الكاملة"},
            "focusModules": ["M11", "M12"],
            "targetWorkflows": ["WF-025", "WF-026", "WF-027", "WF-028", "WF-029", "WF-030"],
            "dailyTasks": [
                {"day": 22, "task": {"en": "Design professional multi-frame layouts with dynamic legends and scale bars.", "ar": "تصميم لوحات طباعة متعددة الأطر مع ربط مقاييس الرسم والدليل."}},
                {"day": 23, "task": {"en": "Automate a multi-page Spatial Map Series with dynamic text tags.", "ar": "أتمتة سلاسل الخرائط المكانية مع وسوم النصوص الديناميكية."}},
                {"day": 24, "task": {"en": "Publish Web Feature Layers with offline sync and vector tile packages.", "ar": "نشر طبقات معالم الويب مع المزامنة وحزم القوالب المتجهة."}},
                {"day": 25, "task": {"en": "Troubleshoot Sharing Analyzer errors (fatal red) vs warnings (yellow).", "ar": "تشخيص وحل أخطاء فاحص المشاركة القاتلة والتحذيرات."}},
                {"day": 26, "task": {"en": "Review all 12 Tool Comparison guides and 12 Troubleshooting guides.", "ar": "مراجعة أدلة المقارنة الـ 12 وأدلة استكشاف الأخطاء الـ 12."}},
                {"day": 27, "task": {"en": "Run full 75-Question Timed Mock Exam in Pearson VUE Simulator mode.", "ar": "خوض اختبار تجريبي كامل من 75 سؤالاً ومؤقت 90 دقيقة في المحاكي."}},
                {"day": 28, "task": {"en": "Final flashcard speed drill (100 cards) and exam day checklist review.", "ar": "المراجعة السريعة لكافة البطاقات الـ 100 وجاهزية يوم الاختبار."}}
            ]
        }
    ]
}

with open(os.path.join(ref_dir, 'study-planner.json'), 'w', encoding='utf-8') as f:
    json.dump(study_planner, f, ensure_ascii=False, indent=2)
print("Saved public/data/references/study-planner.json")
