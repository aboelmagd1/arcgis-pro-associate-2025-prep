# -*- coding: utf-8 -*-
"""
Generate all 30 Practical GIS Workflow Walkthroughs (WF-001 through WF-030) for EAPA_2025.
"""
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_file = os.path.join(base_dir, 'public', 'data', 'workflows', 'workflows.json')

ref_map = {
    "gdb": {"title": "File geodatabases, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/file-geodatabases.htm", "kind": "official"},
    "cad": {"title": "Supported CAD data formats, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/cad/supported-cad-formats.htm", "kind": "official"},
    "proj": {"title": "Define Projection, ArcGIS Pro tool reference", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/define-projection.htm", "kind": "official"},
    "domains": {"title": "An overview of attribute domains, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/an-overview-of-attribute-domains.htm", "kind": "official"},
    "subtypes": {"title": "Introduction to subtypes, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/introduction-to-subtypes.htm", "kind": "official"},
    "contingent": {"title": "Contingent values, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/contingent-values.htm", "kind": "official"},
    "topology": {"title": "Geodatabase topology, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/geodatabase-topology.htm", "kind": "official"},
    "rules": {"title": "An overview of attribute rules, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/an-overview-of-attribute-rules.htm", "kind": "official"},
    "rel": {"title": "Relationship classes, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/relationship-classes.htm", "kind": "official"},
    "cogo": {"title": "COGO in ArcGIS Pro, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/cogo-overview.htm", "kind": "official"},
    "symbology": {"title": "Symbolize feature layers, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/layer-properties/symbolize-feature-layers.htm", "kind": "official"},
    "labeling": {"title": "Maplex Label Engine, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/text/maplex-label-engine.htm", "kind": "official"},
    "scenes": {"title": "Scenes (3D), ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/map-views/scenes.htm", "kind": "official"},
    "time": {"title": "Time in ArcGIS Pro, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/time/time-in-arcgis-pro.htm", "kind": "official"},
    "geocoding": {"title": "Geocoding in ArcGIS Pro, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geocoding/what-is-geocoding.htm", "kind": "official"},
    "raster": {"title": "What are raster functions?, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/analysis/raster-functions/what-are-raster-functions.htm", "kind": "official"},
    "hydrology": {"title": "An overview of the Hydrology toolset, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/an-overview-of-the-hydrology-tools.htm", "kind": "official"},
    "surface": {"title": "An overview of the Surface toolset, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/an-overview-of-the-surface-tools.htm", "kind": "official"},
    "spacetime": {"title": "Space Time Pattern Mining toolbox, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/space-time-pattern-mining/an-overview-of-the-space-time-pattern-mining-toolbox.htm", "kind": "official"},
    "network": {"title": "What is the ArcGIS Network Analyst extension?, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/analysis/networks/what-is-network-analyst.htm", "kind": "official"},
    "model": {"title": "What is ModelBuilder?, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/analysis/modelbuilder/what-is-modelbuilder.htm", "kind": "official"},
    "arcpy": {"title": "What is ArcPy?, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/what-is-arcpy-.htm", "kind": "official"},
    "layouts": {"title": "Layouts in ArcGIS Pro, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/layouts/layouts-in-arcgis-pro.htm", "kind": "official"},
    "mapseries": {"title": "Map series, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/layouts/map-series.htm", "kind": "official"},
    "weblayers": {"title": "Share a web layer, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/sharing/overview/share-a-web-layer.htm", "kind": "official"},
    "vectortiles": {"title": "Vector tile layers, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/layer-properties/vector-tile-layers.htm", "kind": "official"},
    "packages": {"title": "Package a project, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/sharing/overview/package-a-project.htm", "kind": "official"}
}

def make_workflow(wfid, domain, diff, tools, rel_objs, ref_keys, title, obj, data, start, steps, expected, qc, mistakes, alt):
    return {
        "id": wfid,
        "domain": domain,
        "difficulty": diff,
        "tools": tools,
        "relatedObjectives": rel_objs,
        "references": [ref_map[k] for k in ref_keys],
        "title": {"en": title[0], "ar": title[1]},
        "objective": {"en": obj[0], "ar": obj[1]},
        "initialData": {"en": data[0], "ar": data[1]},
        "startingConditions": {"en": start[0], "ar": start[1]},
        "steps": [
            {
                "stepNumber": i + 1,
                "title": {"en": st[0], "ar": st[1]},
                "instruction": {"en": st[2], "ar": st[3]},
                "uiPath": st[4],
                "tool": st[5],
                "parameters": st[6]
            }
            for i, st in enumerate(steps)
        ],
        "expectedOutput": {"en": expected[0], "ar": expected[1]},
        "qualityControl": {"en": qc[0], "ar": qc[1]},
        "commonMistakes": {"en": mistakes[0], "ar": mistakes[1]},
        "alternativeApproaches": {"en": alt[0], "ar": alt[1]}
    }

workflows_list = []

# WF-001: Create and Configure File Geodatabase with 256TB Keyword
workflows_list.append(make_workflow(
    "WF-001", "Data Management", "Beginner",
    ["Create File Geodatabase", "Enable Feature Class To Geodatabase"],
    ["Identify how to manage spatial and non-spatial data", "Describe geodatabase architecture and storage types"],
    ["gdb"],
    ("Create and Configure an Enterprise-Scale File Geodatabase with High-Capacity Keywords", "إنشاء وتهيئة قاعدة بيانات جغرافية موسعة باستخدام معامِلات السعة العالية"),
    ("Set up a new File Geodatabase (.gdb) on local storage, configure project default database, and enable MAX_FILE_SIZE_256TB configuration keyword for large spatial datasets.", "إنشاء قاعدة بيانات جغرافية (.gdb) على القرص المحلي، وتعيينها كقاعدة بيانات افتراضية للمشروع، وتفعيل كلمة التهيئة MAX_FILE_SIZE_256TB للجداول الضخمة."),
    ("ArcGIS Pro 3.3 installed, write access to local directory C:/Data.", "تثبيت ArcGIS Pro 3.3 وتوفر صلاحية الكتابة في المجلد C:/Data."),
    ("New empty project opened with Map template.", "فتح مشروع جديد فارغ باستخدام قالب الخريطة (Map template)."),
    [
        ("Create File Geodatabase", "إنشاء قاعدة بيانات جغرافية", "Open Catalog pane, right-click target folder, select New > File Geodatabase. Name it 'Regional_Master.gdb'.", "افتح نافذة الكتالوج، انقر بالزر الأيمن على المجلد واختَر New > File Geodatabase باسم Regional_Master.gdb.", "Catalog Pane > Databases > New File Geodatabase", "Create File Geodatabase", {"File GDB Name": "Regional_Master.gdb", "File GDB Version": "CURRENT"}),
        ("Set as Default Geodatabase", "التعيين كقاعدة بيانات افتراضية", "Right-click Regional_Master.gdb in Catalog pane and select 'Make Default Geodatabase' so all future geoprocessing outputs write here.", "انقر بالزر الأيمن على القاعدة في الكتالوج واختر Make Default Geodatabase لتوجيه كافة المخرجات إليها.", "Catalog Pane > Databases > Regional_Master.gdb > Make Default", "Set Default GDB", {}),
        ("Configure High Capacity Keyword", "تهيئة كلمة السعة العالية 256TB", "Open Geoprocessing pane, search for 'Create Feature Class', under Configuration Keyword enter 'MAX_FILE_SIZE_256TB' to exceed the standard 1TB per-table limit.", "افتح نافذة المعالجة، وابحث عن أداة Create Feature Class، وتحت معامِل Configuration Keyword أدخل MAX_FILE_SIZE_256TB لتجاوز حد 1 تيرابايت للجدول.", "Geoprocessing Pane > Data Management Tools > Feature Class > Create Feature Class", "Create Feature Class", {"Output Location": "Regional_Master.gdb", "Feature Class Name": "County_Parcels", "Geometry Type": "Polygon", "Configuration Keyword": "MAX_FILE_SIZE_256TB"})
    ],
    ("Regional_Master.gdb initialized as default project database, with County_Parcels feature class configured for up to 256TB storage.", "إنشاء Regional_Master.gdb كقاعدة افتراضية، وتهيئة فئة معالم County_Parcels بسعة تخزين تصل إلى 256 تيرابايت."),
    ("Verify in Catalog Pane that Regional_Master.gdb displays with home icon indicating default database, and inspect dataset properties in Database Properties.", "تأكد من ظهور أيقونة المنزل على قاعدة البيانات في الكتالوج، وافحص خصائص فئة المعالم للتأكد من سعة التخزين."),
    ("Leaving default keyword which limits individual tables to 1TB; attempting to set 256TB on shapefiles.", "ترك كلمة التهيئة فارغة مما يحدد الجدول بـ 1 تيرابايت فقط؛ أو محاولة تطبيقها على ملفات shapefile التي تقتصر على 2 جيجابايت."),
    ("Use Python: arcpy.management.CreateFileGDB() and arcpy.management.CreateFeatureclass(config_keyword='MAX_FILE_SIZE_256TB').", "استخدام سكربت بايثون مع تحديد معامِل config_keyword='MAX_FILE_SIZE_256TB'.")
))

# WF-002: Import CAD DWG Drawings and Migrate to Geodatabase Feature Classes
workflows_list.append(make_workflow(
    "WF-002", "Data Management", "Intermediate",
    ["CAD To Geodatabase", "Make Feature Layer"],
    ["Identify how to manage spatial and non-spatial data", "Import CAD drawings and clean up geometry"],
    ["cad"],
    ("Import AutoCAD DWG Drawings and Migrate to Geodatabase Feature Classes", "استيراد رسومات AutoCAD DWG وتحويلها إلى فئات معالم داخل قاعدة البيانات"),
    ("Import civil engineering CAD drawings (.dwg), filter drawing layers, and convert CAD polylines into clean GIS parcel boundaries.", "استيراد مخطط هندسي أوتوكاد (.dwg)، وتصفية طبقات الرسم، وتحويل خطوط CAD إلى حدود أراضٍ رقمية نظيفة."),
    ("An AutoCAD .dwg file containing parcel lines, text annotations, and utility layers.", "ملف أوتوكاد .dwg يحتوي على خطوط قطع أراضٍ ونصوص ومرافق."),
    ("Project geodatabase connected, spatial reference of CAD drawing confirmed.", "اتصال قاعدة بيانات المشروع، والتحقق من المرجع الإسقاطي لملف الرسم."),
    [
        ("Inspect CAD Dataset in Catalog", "فحص طبقات CAD في الكتالوج", "Expand the .dwg file in Catalog pane to view the 5 virtual feature classes: Point, Polyline, Polygon, MultiPatch, and Annotation.", "قم بتوسيع ملف .dwg في نافذة الكتالوج لمعاينة الطبقات الافتراضية الخمس: Point و Polyline و Polygon و MultiPatch و Annotation.", "Catalog Pane > Folder Connections > Engineering.dwg", "Catalog Inspection", {}),
        ("Apply Definition Query to CAD Polyline", "تصفية خطوط الأراضي عبر استعلام تعريفي", "Add Polyline layer to map, open Properties > Definition Query, filter: `Layer = 'PROP_LINE'` to isolate boundary vectors.", "أضف طبقة Polyline للخريطة، وافتح الخصائص > Definition Query، وصفّ البيانات: Layer = 'PROP_LINE' لعزل خطوط الملكية.", "Layer Properties > Definition Queries > New Query", "Set Definition Query", {"Where Clause": "Layer = 'PROP_LINE'"}),
        ("Execute CAD To Geodatabase Tool", "تنفيذ أداة CAD To Geodatabase", "Run CAD To Geodatabase tool, specifying the input CAD drawing, target geodatabase, and reference scale.", "شغل أداة CAD To Geodatabase مع تحديد ملف CAD المدخل وقاعدة البيانات المستهدفة ومقياس الرسم المرجعي.", "Geoprocessing > Conversion Tools > To Geodatabase > CAD To Geodatabase", "CAD To Geodatabase", {"Input CAD Files": "Engineering.dwg", "Output Geodatabase": "Regional_Master.gdb", "Dataset": "Engineering_Plan", "Reference Scale": "1000"})
    ],
    ("Clean polygon and polyline feature classes imported into a new Feature Dataset inside Regional_Master.gdb.", "فئات معالم نظيفة مستوردة داخل Feature Dataset جديد في قاعدة البيانات الجغرافية."),
    ("Verify feature count and attribute fields (CAD layer names, elevations, colors) are properly transferred.", "تأكد من عدد المعالم المنقولة وانتقال حقول السمات الأصلية مثل اسم الطبقة والارتفاع والألوان بدقة."),
    ("Converting the whole CAD drawing without filtering layers, resulting in thousands of title block border lines in parcels.", "تحويل ملف CAD بالكامل دون تصفية الطبقات مما يؤدي إلى تداخل خطوط ترويسة اللوحة مع حدود الأراضي."),
    ("Use Feature Class To Feature Class with an SQL expression for lightweight individual layer extraction.", "استخدام أداة Feature Class To Feature Class مع تعبير SQL لاستخراج طبقة منفردة بسرعة.")
))

# WF-003: Resolve Spatial Reference Issues: Define Projection vs Project
workflows_list.append(make_workflow(
    "WF-003", "Data Management", "Beginner",
    ["Define Projection", "Project"],
    ["Identify how to manage spatial and non-spatial data", "Control coordinate systems and geographic transformations"],
    ["proj"],
    ("Diagnose and Resolve Spatial Reference Mismatches: Define Projection vs Project", "تشخيص وحل مشكلات الإسناد المكاني: الفرق بين Define Projection و Project"),
    ("Differentiate between repairing missing coordinate metadata (Define Projection) and transforming coordinates to a new coordinate system (Project).", "التمييز الدقيق بين إصلاح بيانات الإسقاط الوصفية المفقودة (Define Projection) والتحويل الفعلي للإحداثيات (Project)."),
    ("Historical municipal shapefile displaying 'Unknown Coordinate System' with coordinate extents in State Plane feet (X: 2,150,000; Y: 680,000).", "ملف shapefile يعرض إحداثيات مجهولة Unknown Coordinate System رغم أن قيمه تمثل أقدام State Plane."),
    ("ArcGIS Pro project map set to NAD 1983 State Plane Texas Central (US Feet).", "خريطة المشروع مضبوطة على نظام State Plane Texas Central (أقدام)."),
    [
        ("Inspect Layer Coordinate Properties", "فحص خصائص إحداثيات الطبقة", "Right-click layer > Properties > Source > Spatial Reference. Verify 'Unknown Coordinate System' and inspect XY Extent values.", "انقر بالزر الأيمن على الطبقة > Properties > Source > Spatial Reference وتأكد من حالة Unknown وافحص قيم المدى.", "Layer Properties > Source > Spatial Reference", "Examine Metadata", {}),
        ("Execute Define Projection", "تنفيذ أداة Define Projection", "Run Define Projection to assign NAD 1983 State Plane Texas Central without recalculating raw coordinate numbers.", "شغل أداة Define Projection لتعيين نظام State Plane Texas Central الصحيح دون تعديل أرقام الإحداثيات.", "Geoprocessing > Data Management > Projections and Transformations > Define Projection", "Define Projection", {"Input Dataset": "Historical_Parcels.shp", "Coordinate System": "NAD 1983 State Plane Texas Central (US Feet)"}),
        ("Execute Project to Reproject to WGS 1984 Web Mercator", "تنفيذ أداة Project لإعادة الإسقاط إلى Web Mercator", "Run Project tool to transform the dataset into WGS 1984 Web Mercator Auxiliary Sphere, specifying geographic transformation NAD_1983_To_WGS_1984_5.", "شغل أداة Project لتحويل البيانات إلى Web Mercator مع اختيار طريقة تحويل المرجع NAD_1983_To_WGS_1984_5.", "Geoprocessing > Data Management > Projections and Transformations > Project", "Project", {"Input Dataset": "Historical_Parcels.shp", "Output Dataset": "Parcels_WebMercator", "Output Coordinate System": "WGS 1984 Web Mercator Auxiliary Sphere", "Geographic Transformation": "NAD_1983_To_WGS_1984_5"})
    ],
    ("Correctly defined spatial metadata on source layer, and a new reprojected feature class in Web Mercator with valid transformation.", "تصحيح البيانات الوصفية للمصدر، وإنشاء فئة معالم جديدة مسقطة بنظام Web Mercator مع تحويل مرجع سليم."),
    ("Overlay both layers over the World Imagery basemap to verify precise boundary alignment with zero datum shift.", "مطابقة الطبقتين فوق مصور الأقمار الصناعية للتحقق من انطباق الحدود بدقة وانعدام أي إزاحة للمرجع."),
    ("Running Project on an Unknown Coordinate System dataset, corrupting the geometry permanently.", "تشغيل أداة Project على بيانات مجهولة الإحداثيات مما يؤدي إلى تشويه وتلف الإحداثيات نهائياً."),
    ("Rely on On-the-Fly projection for temporary visualization, but run Project when performing area calculations.", "الاعتماد على الإسقاط الآني للعرض المؤقت، ولكن تشغيل Project عند الحاجة لحساب المساحات الدقيقة.")
))

# Generate remaining workflows up to 30
# Helper function to bulk append workflows
def add_wf(wfid, domain, diff, tools, rel_objs, ref_keys, title, obj, data, start, steps, expected, qc, mistakes, alt):
    workflows_list.append(make_workflow(wfid, domain, diff, tools, rel_objs, ref_keys, title, obj, data, start, steps, expected, qc, mistakes, alt))

# WF-004: Domains
add_wf("WF-004", "Data Management", "Beginner", ["Create Coded Value Domain", "Assign Domain To Field"],
       ["Describe geodatabase architecture and storage types"], ["domains"],
       ("Configure Attribute Domains with Custom Split and Merge Policies", "تهيئة مجالات السمات مع سياسات الانقسام والدمج المخصصة"),
       ("Enforce data integrity on pipe materials and diameter using Coded Value and Range domains with Geometry Ratio split policies.", "فرض نزاهة البيانات على أقطار وأنابيب المياه عبر مجالات القيم الكودية والنطاقات وسياسات الانقسام الهندسي."),
       ("Water_Mains feature class in a File Geodatabase.", "فئة معالم Water_Mains داخل قاعدة بيانات جغرافية."),
       ("Geodatabase Domains view opened in ArcGIS Pro.", "فتح نافذة Domains view لقاعدة البيانات."),
       [
           ("Create Coded Value Domain", "إنشاء مجال قيم مشفرة", "In Domains view, add 'dm_PipeMaterial' (Field Type: Text), add codes: PVC (Polyvinyl Chloride), DI (Ductile Iron), ST (Steel).", "في نافذة المجالات، أضف dm_PipeMaterial بنوع Text وأضف الأكواد: PVC و DI و ST.", "Catalog > GDB > Domains", "Add Domain", {"Domain Name": "dm_PipeMaterial", "Field Type": "Text"}),
           ("Configure Split/Merge Policies", "ضبط سياسات الانقسام والدمج", "Set Split Policy to 'Geometry Ratio' for pipe length/cost, and Merge Policy to 'Sum Values'.", "اضبط سياسة الانقسام على Geometry Ratio لخصائص الطول والتكلفة، وسياسة الدمج على Sum Values.", "Domains View > Split/Merge", "Configure Policy", {"Split Policy": "Geometry Ratio", "Merge Policy": "Sum Values"}),
           ("Assign Domain to Layer Field", "ربط المجال بحقل الطبقة", "Open Fields view of Water_Mains, select MATERIAL field, assign 'dm_PipeMaterial'.", "افتح نافذة الحقول للطبقة، وحدد حقل MATERIAL واربطه بمجال dm_PipeMaterial.", "Layer > Fields View > Domain Dropdown", "Assign Domain", {"Field": "MATERIAL", "Domain": "dm_PipeMaterial"})
       ],
       ("Restricted dropdown menu in attribute table preventing typos, with automated proportional splitting on edits.", "قائمة خيارات منسدلة في جدول السمات تمنع الأخطاء الكتابية وتوزع القيم نسبياً عند تقسيم الأنابيب."),
       ("Create a test feature in Edit tab and confirm dropdown displays only valid domain codes.", "أنشئ معلماً تجريبياً في شريط التحرير وتأكد من ظهور الأكواد الصحيحة فقط في القائمة المنسدلة."),
       ("Setting Range domains on Text fields; forgetting to save changes in Fields tab ribbon.", "محاولة تطبيق مجال النطاق الرقمي على حقل نصي؛ أو نسيان النقر على زر Save في شريط Fields."),
       ("Apply Domains via Python: arcpy.management.CreateDomain() and arcpy.management.AssignDomainToField().", "تطبيق المجالات عبر بايثون باستخدام CreateDomain و AssignDomainToField.")
)

# WF-005: Subtypes
add_wf("WF-005", "Data Management", "Intermediate", ["Set Subtype Field", "Add Subtype"],
       ["Describe geodatabase architecture and storage types"], ["subtypes"],
       ("Configure Geodatabase Subtypes for Asset Categorization", "تهيئة الأنماط الفرعية (Subtypes) لتصنيف الأصول وإدارة الخصائص"),
       ("Classify Road Centerlines into Local, Arterial, and Highway subtypes with distinct default speed limits and domains.", "تصنيف خطوط محاور الطرق إلى شوارع محلية وشريانية وسريعة مع سرعات افتراضية ومجالات سمات مختلفة لكل نمط."),
       ("Road_Centerlines feature class with a Long Integer field named 'ROAD_CLASS'.", "فئة معالم محاور الطرق مع حقل رقم صحيح Long Integer باسم ROAD_CLASS."),
       ("Road layer added to map, Subtypes view opened.", "إضافة طبقة الطرق للخريطة وفتح نافذة Subtypes."),
       [
           ("Set Subtype Field", "تحديد حقل النمط الفرعي", "In Subtypes view, set Subtype Field to 'ROAD_CLASS'.", "في نافذة Subtypes، حدد حقل النمط الفرعي ليكون ROAD_CLASS.", "Design Ribbon > Subtypes View", "Set Subtype Field", {"Field": "ROAD_CLASS"}),
           ("Define Subtype Codes", "تعريف أكواد الأنماط الفرعية", "Add Code 1: Local (Default Speed: 25), Code 2: Arterial (Default Speed: 45), Code 3: Highway (Default Speed: 65).", "أضف كود 1: Local (السرعة 25)، وكود 2: Arterial (السرعة 45)، وكود 3: Highway (السرعة 65).", "Subtypes Grid", "Add Subtype Rows", {"1": "Local", "2": "Arterial", "3": "Highway"}),
           ("Assign Specific Domains Per Subtype", "تخصيص مجالات مختلفة لكل نمط", "For Code 1 (Local), restrict LANES domain to 2; for Code 3 (Highway), restrict LANES domain to 4-8.", "للنمط 1 حدد عدد المسارات بـ 2، وللنمط 3 حدد المسارات بين 4 و 8 مسارات.", "Subtypes Field Tab", "Set Domain Per Subtype", {})
       ],
       ("Roads layer categorized into 3 subtypes, automatically generating 3 feature templates in Create Features pane.", "تصنيف طبقة الطرق إلى 3 أنماط فرعية وتوليد 3 قوالب رسم تلقائياً في نافذة إنشاء المعالم."),
       ("Open Create Features pane and verify three separate road templates appear with their default speed limits populated.", "افتح نافذة Create Features وتأكد من ظهور 3 قوالب مستقلة بالسرعات الافتراضية المحددة."),
       ("Attempting to use a Text or Float field as the subtype field instead of Short or Long Integer.", "محاولة استخدام حقل نصي أو عشري لحقل النمط الفرعي بدلاً من الأرقام الصحيحة."),
       ("Configure subtypes programmatically using arcpy.management.SetSubtypeField().", "تهيئة الأنماط الفرعية برمجياً عبر بايثون باستخدام SetSubtypeField.")
)

# WF-006: Contingent Values
add_wf("WF-006", "Data Management", "Advanced", ["Create Field Group", "Add Contingent Value"],
       ["Describe geodatabase architecture and storage types"], ["contingent"],
       ("Configure Contingent Values for Dependent Hierarchical Attributes", "تهيئة القيم الشرطية (Contingent Values) للسمات التابعة هرمياً"),
       ("Build a Field Group linking Pole Material, Pole Height, and Transformer Class to eliminate invalid field combinations.", "بناء مجموعة حقول تربط مادة العمود وارتفاعه وفئة المحول الكهربائي لمنع إدخال توليفات سمات غير متوافقة."),
       ("Utility_Poles feature class with fields: MATERIAL, HEIGHT, TRANSFORMER.", "فئة معالم أعمدة الكهرباء بحقول المادة والارتفاع وفئة المحول."),
       ("Fields already configured with their individual Coded Value Domains.", "ربط الحقول مسبقاً بمجالات القيم الكودية الخاصة بها."),
       [
           ("Create Field Group", "إنشاء مجموعة الحقول", "Open Contingent Values view, click 'Field Groups' > New, name it 'fg_PoleConfiguration', add fields: MATERIAL, HEIGHT, TRANSFORMER.", "افتح نافذة Contingent Values، وانقر Field Groups > New باسم fg_PoleConfiguration واختر الحقول الثلاثة.", "Data Ribbon > Contingent Values > Field Groups", "Create Field Group", {"Group Name": "fg_PoleConfiguration"}),
           ("Define Valid Combinations", "تعريف التوليفات الصالحة", "Add valid rows: Wood -> 35ft -> SinglePhase; Concrete -> 50ft -> ThreePhase. Restrict Wood poles from holding heavy ThreePhase transformers.", "أضف التوليفات الصحيحة: خشب -> 35 قدم -> SinglePhase؛ خرسانة -> 50 قدم -> ThreePhase، مع منع الأعمدة الخشبية من حمل محولات 3 فاز.", "Contingent Values Grid", "Add Contingent Values", {}),
           ("Verify in Editing Session", "التحقق أثناء جلسة التحرير", "Create a new pole feature in map, select 'Wood', observe that HEIGHT and TRANSFORMER filter to matching valid choices.", "أنشئ عموداً جديداً واختَر 'Wood' ولاحظ اقتصار خيارات الارتفاع والمحول على القيم المتوافقة فقط.", "Edit > Create Features", "Interactive Test", {})
       ],
       ("Dynamic cascading dropdown filters in Attributes pane that reject invalid equipment configurations.", "قوائم منسدلة ديناميكية مترابطة في نافذة السمات تمنع اختيار معدات غير متطابقة هندسياً."),
       ("Attempt to enter an invalid combination and verify ArcGIS Pro flags the record with a yellow warning badge.", "حاول إدخال توليفة غير صالحة وتأكد من قيام البرنامج بوضع علامة تحذير صفراء على السجل."),
       ("Forgetting to define domains before setting up field groups.", "نسيان إنشاء مجالات السمات أولاً قبل تهيئة مجموعات الحقول الشرطية."),
       ("Use Attribute Rules with Arcade as an alternative constraint check.", "استخدام قواعد السمات مع Arcade كبديل لفرض قيود الإدخال.")
)

# WF-007: Topology
add_wf("WF-007", "Data Management", "Intermediate", ["Create Topology", "Validate Topology"],
       ["Identify how to manage spatial and non-spatial data", "Validate topology and clean up errors"], ["topology"],
       ("Build, Validate, and Fix Geodatabase Topology for Land Parcels", "بناء وفحص وتصحيح طوبولوجيا قاعدة البيانات الجغرافية لقطع الأراضي"),
       ("Ensure municipal parcel polygons do not overlap and have no unintended interior sliver gaps using Geodatabase Topology.", "ضمان عدم تداخل مضلعات الأراضي وخلوها من الفجوات والشرائح البينية باستخدام طوبولوجيا قاعدة البيانات."),
       ("Parcels feature class inside a Feature Dataset in a File Geodatabase.", "فئة معالم قطع الأراضي داخل Feature Dataset في قاعدة بيانات جغرافية."),
       ("Feature Dataset created with correct coordinate system.", "إنشاء Feature Dataset بنظام الإحداثيات المعتمد."),
       [
           ("Create Topology Item", "إنشاء عنصر الطوبولوجيا", "In Catalog pane, right-click Feature Dataset > New > Topology. Name it 'Parcels_Topology', set Cluster Tolerance to 0.001m.", "في الكتالوج، انقر بالزر الأيمن على Feature Dataset > New > Topology باسم Parcels_Topology وتسامح 0.001م.", "Catalog > Feature Dataset > New > Topology", "Create Topology", {"Cluster Tolerance": "0.001 Meters"}),
           ("Add Topology Rules", "إضافة القواعد الطوبولوجية", "Add rules: 1. 'Must Not Overlap' and 2. 'Must Not Have Gaps' (with boundary exception).", "أضف قاعدتي: 1. 'Must Not Overlap' و 2. 'Must Not Have Gaps' (مع استثناء الحدود الخارجية).", "Topology Wizard > Rules", "Add Rules", {"Rule 1": "Must Not Overlap", "Rule 2": "Must Not Have Gaps"}),
           ("Validate and Inspect Errors", "فحص وتصحيح الأخطاء عبر Error Inspector", "Add topology to map, open Edit > Error Inspector, click Validate. Use Fix: Create Feature for gaps, or Merge for overlaps.", "أضف الطوبولوجيا للخريطة، وافتح Error Inspector، وانقر Validate؛ واستخدم Merge للتداخلات أو Create Feature للفجوات.", "Edit Ribbon > Error Inspector", "Validate Topology", {"Scope": "Full Extent"})
       ],
       ("Topology error-free parcel fabric dataset, with verified boundary adjacency and zero slivers.", "طبقة مضلعات أراضٍ نظيفة وخالية من أخطاء الطوبولوجيا مع تطابق تام للحواف وانعدام الفجوات."),
       ("Run Validate on Full Extent and confirm Error Inspector displays '0 Errors Found'.", "شغل أداة الفحص لكامل النطاق وتأكد من أن نافذة فاحص الأخطاء تعرض 0 Errors Found."),
       ("Trying to create a Geodatabase Topology on standalone feature classes outside a Feature Dataset.", "محاولة إنشاء طوبولوجيا قاعدة البيانات على فئات معالم منفردة خارج Feature Dataset."),
       ("Use Map Topology on the fly for simple shared-edge alignment during active editing.", "استخدام طوبولوجيا الخريطة (Map Topology) للمحاذاة السريعة أثناء التحرير العادي.")
)

# WF-008: Attribute Rules
add_wf("WF-008", "Data Management", "Advanced", ["Add Attribute Rule"],
       ["Identify how to manage spatial and non-spatial data", "Apply attribute rules where appropriate"], ["rules"],
       ("Implement Arcade-Based Immediate Calculation and Constraint Attribute Rules", "إنشاء قواعد السمات للحساب الفوري والقيود باستخدام لغة Arcade"),
       ("Automatically calculate the geodesic area in acres on parcel sketch completion, and block creation of parcels under 0.25 acres.", "حساب المساحة الجيوديسية بالفدان آلياً فور رسم المضلع، ومنع إنشاء أي عقار تقل مساحته عن 0.25 فدان."),
       ("Parcels feature class with an 'ACREAGE' double field, GlobalIDs enabled.", "فئة معالم الأراضي بحقل ACREAGE من نوع Double وتفعيل معرفات GlobalID."),
       ("Attribute Rules view opened for Parcels layer.", "فتح نافذة Attribute Rules لطبقة الأراضي."),
       [
           ("Create Calculation Rule", "إنشاء قاعدة حساب فوري للمساحة", "Add Calculation Rule 'calc_Acreage', Trigger: Insert, Update. Script: `return Round(AreaGeodetic($feature, 'acres'), 2);` targeting ACREAGE field.", "أضف قاعدة حساب calc_Acreage عند الإنشاء والتعديل، بكود: Round(AreaGeodetic($feature, 'acres'), 2) مستهدفاً حقل ACREAGE.", "Design > Attribute Rules > Calculation", "Add Rule", {"Name": "calc_Acreage", "Field": "ACREAGE"}),
           ("Create Constraint Rule", "إنشاء قاعدة قيد لمنع المساحات الصغيرة", "Add Constraint Rule 'check_MinLotSize', Trigger: Insert. Script: `if (AreaGeodetic($feature, 'acres') < 0.25) { return false; } return true;` with Error 1001.", "أضف قاعدة قيد check_MinLotSize لمنع أي مضلع أقل من ربع فدان مع رسالة خطأ واضحة برقم 1001.", "Design > Attribute Rules > Constraint", "Add Rule", {"Name": "check_MinLotSize", "Error Number": "1001"}),
           ("Save and Test in Editor", "حفظ القواعد واختبارها بالتحرير", "Click Save on ribbon. Digitize a 0.1-acre polygon and verify save rejection; sketch a 2-acre parcel and verify acreage calculates instantly.", "احفظ القواعد؛ ارسم مضلعاً بمساحة 0.1 فدان وتأكد من رفض الحفظ، ثم ارسم مضلعاً بمساحة فدانين وتأكد من حساب المساحة آلياً.", "Edit > Create Features", "Test Rule", {})
       ],
       ("Enforced business logic preventing substandard lot splits and eliminating manual area recalculations.", "فرض منطق عمل يمنع الأراضي العشوائية دون مساحة معتمدة ويلغي الحاجة لحساب المساحات يدوياً."),
       ("Inspect acreage field immediately after saving edit to ensure value is populated with 2 decimal places.", "افحص حقل المساحة فور حفظ المعلم للتأكد من حساب القيمة بدقة منزلتين عشريتين."),
       ("Forgetting to enable GlobalIDs prior to creating attribute rules; forgetting to check Insert/Update triggers.", "نسيان تفعيل GlobalIDs قبل إنشاء القواعد؛ أو نسيان تحديد محفزات التحرير Insert و Update."),
       ("Use Calculate Field in geoprocessing batch mode for retroactive processing of existing legacy features.", "استخدام أداة Calculate Field لمعالجة المعالم القديمة الموجودة مسبقاً دفعة واحدة.")
)

# WF-009: Relationship Class & Attachments
add_wf("WF-009", "Data Management", "Intermediate", ["Create Relationship Class", "Enable Attachments"],
       ["Describe geodatabase architecture and storage types"], ["rel"],
       ("Configure 1:Many Relationship Class with Photo Attachments", "تهيئة فئة علاقات (1:Many) مع تفعيل المرفقات والصور الميدانية"),
       ("Link Tax Parcels to historical building permit records (1:Many) and enable photo attachments for code compliance inspections.", "ربط قطع الأراضي بسجلات تصاريح البناء التاريخية وتفعيل إرفاق الصور لمخالفات كود البناء."),
       ("Parcels feature class (Origin) and Building_Permits standalone table (Destination) with PARCEL_ID key.", "فئة معالم الأراضي وجدول تصاريح البناء بحقل مفتاح مشترك PARCEL_ID."),
       ("Both tables reside within the same File Geodatabase.", "وجود الطبقتين داخل نفس قاعدة البيانات الجغرافية."),
       [
           ("Create Relationship Class", "إنشاء فئة العلاقات", "Run Create Relationship Class tool: Origin: Parcels, Destination: Building_Permits, Type: Simple, Cardinality: One to Many (1:M).", "شغل أداة Create Relationship Class: الأصل Parcels، والهدف Building_Permits، بنمط Simple وعلاقة 1:M.", "Geoprocessing > Data Management > Relationship Classes", "Create Relationship Class", {"Origin Table": "Parcels", "Destination Table": "Building_Permits", "Cardinality": "ONE_TO_MANY", "Origin Primary Key": "PARCEL_ID", "Origin Foreign Key": "PARCEL_ID"}),
           ("Enable Attachments on Permits", "تفعيل المرفقات على جدول التصاريح", "Run Enable Attachments tool on Building_Permits table, generating the _ATTACH table and relationship class.", "شغل أداة Enable Attachments على جدول التصاريح لتوليد جدول المرفقات وعلاقة الربط التلقائية.", "Geoprocessing > Data Management > Attachments > Enable Attachments", "Enable Attachments", {"Input Dataset": "Building_Permits"}),
           ("Verify in Attributes Pane", "التحقق في نافذة السمات", "Select a parcel in map, open Attributes pane, expand parcel node to see related permits and add photo attachments.", "حدد قطعة أرض في الخريطة، وافتح نافذة السمات وتأكد من ظهور التصاريح المرتبطة وزر إرفاق الصور.", "Map > Select > Attributes Pane", "Inspect Relationships", {})
       ],
       ("Bi-directional relationship linking parcels to inspection records with embedded photo viewing capabilities.", "علاقة ارتباط ثنائية الاتجاه تربط الأراضي بالتصاريح مع إمكانية استعراض وإضافة الصور المرفقة."),
       ("Select a parcel, verify related permit records expand hierarchically in Attributes pane tree view.", "حدد عقاراً وتأكد من فتح شجرة السجلات المرتبطة به في نافذة السمات بسلاسة."),
       ("Using Composite relationship when child records should survive independent parcel sales (use Simple instead).", "استخدام علاقة Composite بدلاً من Simple مما قد يؤدي لحذف التصاريح عند حذف الأرض."),
       ("Use Add Relate for quick ad-hoc map-level relating without geodatabase schema modification.", "استخدام Add Relate للربط المؤقت على مستوى الخريطة دون تعديل هيكل قاعدة البيانات.")
)

# WF-010: COGO Traversing
add_wf("WF-010", "Data Management", "Intermediate", ["Enable COGO", "Traverse"],
       ["Identify how to manage spatial and non-spatial data", "Create and edit vector features"], ["cogo"],
       ("Precision Land Survey Boundary Digitizing using COGO Traverse", "رقمنة حدود مساحية دقيقة لقطع الأراضي باستخدام تقنية COGO Traverse"),
       ("Enter legal deed survey metes-and-bounds descriptions (bearings and quadrant distances) using the Traverse tool.", "إدخال حدود الملكية القانونية من صك مساحي (زوايا الاتجاه ومسافات الأضلاع) باستخدام أداة Traverse."),
       ("Boundary_Lines polyline feature class enabled with COGO fields (Direction, Distance, Radius).", "فئة معالم خطية مفعل عليها حقول COGO (الاتجاه، المسافة، نصف القطر)."),
       ("Legal deed metes-and-bounds survey call sheet with starting point coordinates.", "صك مساحي قانوني يحدد إحداثيات نقطة البداية وقراءات الأضلاع."),
       [
           ("Enable COGO on Layer", "تفعيل حقول COGO على الطبقة", "Run Enable COGO tool to populate standard survey fields (Direction, Distance, Curve parameters).", "شغل أداة Enable COGO لإضافة الحقول المساحية القياسية للطبقة.", "Geoprocessing > Data Management > Fields > Enable COGO", "Enable COGO", {"Input Layer": "Boundary_Lines"}),
           ("Launch Traverse Tool", "تشغيل أداة المسار المساحي Traverse", "In Edit ribbon, open Tools > Traverse. Set Starting Point coordinates from the deed legal description.", "في شريط Edit، افتح Traverse وحدد إحداثيات نقطة البداية المذكورة في الصك.", "Edit Ribbon > Tools > Traverse", "Set Start Point", {"Start X": "2154300.5", "Start Y": "685210.2"}),
           ("Enter Survey Legs and Close", "إدخال أضلاع المسار والإغلاق", "Input calls: N 45-30-15 E 250.00 ft; S 88-12-00 E 180.50 ft; S 15-00-00 W 240.00 ft; Close back to start.", "أدخل قراءات الأضلاع بدقة بالاتجاه والمسافة، ثم اضغط Close لإغلاق المضلع وحساب خطأ الإغلاق.", "Traverse Grid", "Input Legs", {"1": "N45-30-15E 250.00", "2": "S88-12-00E 180.50", "3": "Close"})
       ],
       ("Survey-grade parcel boundary with recorded COGO attributes and misclosure error report.", "حدود عقارية دقيقة هندسياً ومطابقة للصك مع تسجيل سمات COGO وتقرير خطأ الإغلاق المساحي."),
       ("Examine Traverse misclosure ratio (e.g. 1:25,000) to verify survey closure tolerances.", "افحص نسبة خطأ الإغلاق في تقرير المسار للتأكد من مطابقتها للمعايير المساحية المقبولة."),
       ("Entering polar arithmetic angles instead of quadrant bearings (e.g. N 45° E vs 45°).", "إدخال الزوايا بنظام الإحداثيات القطبية بدلاً من زوايا الأرباع المساحية (Quadrant Bearings)."),
       ("Use Ground to Grid correction to adjust survey distances for elevation scale factors and grid convergence.", "تفعيل تصحيح Ground to Grid لتعديل مسافات القياس الميداني لتطابق شبكة الإسقاط.")
)

# WF-011: Graduated Colors & Normalization
add_wf("WF-011", "Visualization", "Beginner", ["Apply Symbology From Layer", "Graduated Colors"],
       ["Manage layer properties using the ribbon and dialog boxes"], ["symbology"],
       ("Quantitative Choropleth Mapping with Graduated Colors and Normalization", "تصميم خرائط كوروبليث الكمية بالألوان المتدرجة وتوحيد البيانات بالنسب"),
       ("Map regional population density by dividing total population by land area (Normalization) to avoid misleading raw count representations.", "تمثيل الكثافة السكانية بقسمة عدد السكان على المساحة (Normalization) لمنع التضليل الكارتوغرافي للأرقام المطلقة."),
       ("Counties polygon feature class with 'TOT_POP' and 'SQ_MILES' numeric fields.", "فئة معالم المقاطعات مع حقلي عدد السكان والمساحة بالميل المربع."),
       ("Counties layer added to map with default Single Symbol.", "إضافة طبقة المقاطعات للخريطة بالترميز الافتراضي."),
       [
           ("Open Symbology Pane", "فتح نافذة الرموز", "Right-click Counties > Symbology. Select Primary symbology: 'Graduated Colors'.", "انقر بالزر الأيمن على الطبقة > Symbology واختَر Graduated Colors.", "Layer Context Menu > Symbology", "Set Symbology Type", {"Type": "Graduated Colors"}),
           ("Configure Field and Normalization", "تحديد حقل التصنيف وحقل التوحيد", "Set Field to 'TOT_POP', set Normalization to 'SQ_MILES' (calculating Population per Square Mile).", "حدد الحقل ليكون TOT_POP وحقل التوحيد ليكون SQ_MILES (لحساب الكثافة لكل ميل مربع).", "Symbology Pane > Primary Tab", "Set Fields", {"Field": "TOT_POP", "Normalization": "SQ_MILES"}),
           ("Select Classification and Ramp", "اختيار طريقة التصنيف ومدرج الألوان", "Choose Method: 'Natural Breaks (Jenks)', Classes: 5, Color scheme: Light yellow to dark purple sequential ramp.", "اختَر طريقة Natural Breaks (Jenks) بـ 5 فئات ومدرج ألوان متسلسل من الأصفر الفاتح إلى البنفسجي الداكن.", "Symbology Pane > Classes", "Configure Breaks", {"Method": "Natural Breaks (Jenks)", "Classes": "5"})
       ],
       ("Statistically sound choropleth map showing true population density without polygon size bias.", "خريطة كوروبليث علمية سليمة تبرز الكثافة السكانية الحقيقية دون انحياز لمساحات المقاطعات."),
       ("Inspect class breaks in histogram view to confirm breaks match natural valleys in the data distribution.", "افحص المدرج التكراري للبيانات للتأكد من وقوع فواصل الفئات عند الفجوات الطبيعية للتوزيع."),
       ("Mapping raw counts (total population) with graduated colors without normalization, biasing large area polygons.", "تمثيل الأرقام المطلقة بتدرج لوني دون قسمتها على المساحة مما يضلل القارئ لصالح المضلعات الكبيرة."),
       ("Use Dot Density symbology as an alternative quantitative representation of raw population counts.", "استخدام رموز كثافة النقط (Dot Density) كبديل بصري ممتاز لتمثيل الأعداد المطلقة.")
)

# WF-012: Vary Symbology by Attribute
add_wf("WF-012", "Visualization", "Intermediate", ["Vary Symbology By Attribute"],
       ["Manage layer properties using the ribbon and dialog boxes"], ["symbology"],
       ("Multi-Variable Visualization: Driving Symbol Size and Rotation Concurrently", "التمثيل البصري متعدد المتغيرات: التحكم المتزامن في حجم الرمز وزاوية دورانه"),
       ("Symbolize weather station points using directional wind arrows where symbol size reflects wind speed and rotation reflects wind direction.", "تمثيل محطات الأرصاد بأسهم رياح يتناسب حجمها مع سرعة الرياح وتدور زاوية السهم باتجاه هبوب الرياح."),
       ("Weather_Stations point layer with 'WIND_SPEED' (knots) and 'WIND_DIR' (degrees 0-360).", "طبقة نقاط محطات الأرصاد مع حقلي سرعة الرياح وزاوية اتجاهها."),
       ("Layer symbolized with an arrow directional marker symbol.", "ترميز الطبقة برمز سهم توجيهي."),
       [
           ("Open Vary Symbology Tab", "فتح تبويب التباين بالسمات", "In Symbology pane, click the 'Vary symbology by attribute' icon (three sliders).", "في نافذة الرموز، انقر على أيقونة Vary symbology by attribute (أيقونة المنزلقات الثلاثة).", "Symbology Pane > Vary Symbology Tab", "Open Vary Tab", {}),
           ("Configure Size Variation", "ضبط تباين الحجم وفق السرعة", "Expand Size, check 'Vary size by attribute', select Field: 'WIND_SPEED'. Set min size 8pt and max size 36pt.", "افتح قسم Size، وفعل تباين الحجم، وحدد حقل WIND_SPEED مع ضبط الحجم بين 8 و 36 نقطة.", "Vary Tab > Size", "Configure Size", {"Field": "WIND_SPEED", "Min Size": "8 pt", "Max Size": "36 pt"}),
           ("Configure Rotation Variation", "ضبط زاوية التدوير وفق الاتجاه", "Expand Rotation, check 'Vary rotation by attribute', select Field: 'WIND_DIR', Rotation Type: 'Geographic' (0 = North, clockwise).", "افتح قسم Rotation، وحدد حقل WIND_DIR بنمط Geographic (0 شمالاً مع عقارب الساعة).", "Vary Tab > Rotation", "Configure Rotation", {"Field": "WIND_DIR", "Type": "Geographic"})
       ],
       ("Dynamic bivariate map displaying wind velocity and directional heading simultaneously on a single layer.", "خريطة ثنائية المتغيرات تعرض سرعة الرياح واتجاه حركتها في آن واحد على نفس الطبقة."),
       ("Verify that a station with 0° wind points due North, and 90° points due East.", "تأكد من أن المحطة ذات الزاوية 0 تشير شمالاً والمحطة ذات الزاوية 90 تشير شرقاً."),
       ("Selecting 'Arithmetic' rotation (0 = East, counter-clockwise) for compass data, resulting in 90-degree reversed headings.", "اختيار التدوير الحسابي (Arithmetic) لبيانات البوصلة مما يعكس اتجاهات الرياح بمقدار 90 درجة."),
       ("Use Dictionary Symbology when standard military or emergency symbol rules govern multi-attribute styling.", "استخدام رموز القاموس (Dictionary Symbology) للرموز المعيارية العسكرية المعقدة.")
)

# WF-013: Maplex Label Expressions & Conflicts
add_wf("WF-013", "Visualization", "Intermediate", ["Maplex Label Engine", "Label Expression"],
       ["Manage layer properties using the ribbon and dialog boxes"], ["labeling"],
       ("Advanced Maplex Labeling with Arcade Expressions and Conflict Resolution", "تسميات Maplex المتقدمة باستخدام لغة Arcade وحل تصادم التسميات"),
       ("Label commercial parcels with multi-line formatted text (Parcel ID in bold, owner name, assessed value formatted as currency) and prevent label overlaps.", "كتابة تسميات عقارية متعددة الأسطر (رقم الأرض عريضاً، واسم المالك، والقيمة النقدية) ومنع تداخل التسميات."),
       ("Parcels polygon layer with 'PARCEL_ID', 'OWNER', and 'ASSESSED_VAL' fields.", "طبقة مضلعات الأراضي بحقول رقم العقار والمالك والقيمة."),
       ("Maplex Label Engine enabled on the map view.", "تفعيل محرك التسميات Maplex Label Engine في الخريطة."),
       [
           ("Enable Labeling and Open Expression", "تفعيل التسميات وفتح نافذة Arcade", "Turn on labeling for Parcels. In Labeling ribbon, click Expression button, set Language: 'Arcade'.", "فعل تسميات الطبقة، وانقر على زر التعبير في شريط Labeling مع اختيار لغة Arcade.", "Labeling Ribbon > Expression", "Set Expression Language", {"Language": "Arcade"}),
           ("Write Formatted Arcade Script", "كتابة كود التنسيق بلغة Arcade", "Input: `<BOL>` + $feature.PARCEL_ID + `</BOL>` + TextFormatting.NewLine + $feature.OWNER + TextFormatting.NewLine + Text($feature.ASSESSED_VAL, '$#,###');", "أدخل كود Arcade لتنسيق الخط العريض والسطر الجديد وتنسيق العملة.", "Label Expression Builder", "Write Arcade", {}),
           ("Configure Maplex Placement and Fitting", "ضبط قواعد الموضع والملاءمة في Maplex", "Set Placement: 'Horizontal in polygon'. In Fitting Strategy, enable 'Font reduction' (lower limit: 7pt) and 'Abbreviation dictionary'.", "اضبط الموضع داخل المضلع، وفعل استراتيجية تقليص الخط حتى 7 نقاط وقاموس الاختصارات.", "Labeling Properties > Placement", "Configure Maplex", {"Placement": "Horizontal in polygon", "Min Font": "7 pt"})
       ],
       ("High-density legible parcel labels showing rich multi-line financial information without overlaps.", "تسميات عقارية منسقة واضحة تبرز البيانات المالية بدقة ودون أي تصادم أو حجب."),
       ("Pan across dense parcel blocks; verify that labels shrink gracefully to fit small parcels without truncation.", "تحرك عبر أحياء الأراضي الكثيفة وتأكد من تصغير الخط تلقائياً ليناسب القطع الصغيرة دون تشويه."),
       ("Forgetting to close HTML formatting tags (e.g. `<BOL>` without `</BOL>`), corrupting label rendering.", "نسيان إغلاق وسوم التنسيق مثل `<BOL>` دون `</BOL>` مما يعطل رسم التسميات."),
       ("Convert labels to Geodatabase Annotation when individual manual text placement adjustments are required.", "تحويل التسميات إلى ملاحظات (Annotation) عند الحاجة لتحريك بعض التسميات يدوياً للطباعة النهائية.")
)

# WF-014: 3D Local Scene & Extrusions
add_wf("WF-014", "Visualization", "Intermediate", ["Extrusion", "Local Scene"],
       ["Determine how to visualize temporal, ranged, or 3D data"], ["scenes"],
       ("Build an Interactive 3D Local Scene with Building Footprint Extrusions", "بناء مشهد محلي ثلاثي الأبعاد مع بثق مساقط المباني"),
       ("Convert 2D building footprints into a realistic 3D cityscape draped over a digital elevation surface with height extrusions.", "تحويل مساقط مبانٍ ثنائية الأبعاد إلى مجسمات ثلاثية الأبعاد تستند لسطح التضاريس مع بثق الارتفاعات."),
       ("Building_Footprints polygon feature class with 'STOREYS' or 'HEIGHT_M' numeric fields, and a 10m DEM surface.", "فئة معالم مساقط المباني بحقل عدد الطوابق أو الارتفاع، مع راستر تضاريس 10م."),
       ("New empty 3D Local Scene view opened in ArcGIS Pro.", "فتح مشهد محلي ثلاثي الأبعاد (Local Scene) جديد."),
       [
           ("Add Data and Set Elevation Surface", "إضافة البيانات وتحديد سطح الارتفاع", "Add DEM to 'Ground' elevation surfaces in Contents pane. Add Building_Footprints into '2D Layers'.", "أضف راستر DEM لسطح الأرض Ground، وأضف مساقط المباني في قسم 2D Layers.", "Contents Pane > Elevation Surfaces > Ground", "Add Elevation Surface", {"Surface": "10m_DEM.tif"}),
           ("Configure Layer Elevation Properties", "ضبط خصائص ارتفاع قاعدة المباني", "Open Layer Properties > Elevation. Set 'Features are: On the ground' so polygon bases conform to terrain slope.", "افتح خصائص الطبقة > Elevation واختَر Features are: On the ground لتلتصق القواعد بالتضاريس.", "Layer Properties > Elevation", "Set Elevation Mode", {"Mode": "On the ground"}),
           ("Configure Extrusion Method", "ضبط طريقة ومعامل بثق الجدران", "In Feature Layer Appearance ribbon > Extrusion. Type: 'Base height', Expression: `$feature.STOREYS * 3.5` (or HEIGHT_M field).", "في شريط Appearance، اختر Type: Base height، واكتب التعبير: $feature.STOREYS * 3.5 لأمتار الارتفاع.", "Appearance Ribbon > Extrusion", "Set Extrusion", {"Type": "Base height", "Expression": "$feature.STOREYS * 3.5"})
       ],
       ("Realistic 3D urban skyline where building heights reflect true structural dimensions anchored to terrain.", "مشهد عمراني مجسم ثلاثي الأبعاد تعبر فيه ارتفاعات المباني عن واقعها الهندسي وتستند بثبات على التضاريس."),
       ("Tilt scene camera to oblique perspective; verify buildings rise vertically from hillsides without floating.", "قم بإمالة الكاميرا وتأكد من ارتفاع جدران المباني رأسياً من سفوح التلال دون أن تطفو في الهواء."),
       ("Setting elevation to 'At an absolute height' of 0 meters, causing buildings to be buried inside hillsides.", "ضبط الارتفاع على منسوب مطلق 0 متر مما يدفن المباني داخل التلال المرتفعة."),
       ("Convert extruded polygons into permanent 3D MultiPatch geometries using the 'Layer 3D To Feature Class' tool.", "تحويل المضلعات المبثوقة إلى مجسمات MultiPatch دائمة باستخدام أداة Layer 3D To Feature Class.")
)

# WF-015: Time Slider Animation
add_wf("WF-015", "Visualization", "Intermediate", ["Time Slider", "Layer Properties Time"],
       ["Determine how to visualize temporal, ranged, or 3D data"], ["time"],
       ("Configure Temporal Visualization and Smooth Playback with the Time Slider", "تهيئة العرض الزمني والرسوم المتحركة التفاعلية باستخدام منزلق الوقت"),
       ("Configure time properties on historical seismic earthquake events to animate chronological progression over a 30-day period.", "ضبط الخصائص الزمنية لبيانات الزلازل التاريخية لتحريك مسار حدوثها زمنياً على مدار 30 يوماً."),
       ("Earthquakes point feature class with 'EVENT_DATE' timestamp field.", "فئة معالم نقاط الزلازل مع حقل تاريخ وتوقيت الحدث EVENT_DATE."),
       ("Earthquakes layer displayed in map view.", "عرض طبقة الزلازل على خريطة المشروع."),
       [
           ("Enable Time on Layer", "تفعيل الزمن في خصائص الطبقة", "Open Layer Properties > Time. Select 'Each feature has a single time field', set Time Field to 'EVENT_DATE'.", "افتح خصائص الطبقة > Time، واختَر حقل زمن منفرد وحدد حقل EVENT_DATE.", "Layer Properties > Time", "Configure Time", {"Layer Time": "Each feature has a single time field", "Time Field": "EVENT_DATE"}),
           ("Configure On-Screen Time Slider", "ضبط منزلق الوقت في واجهة العرض", "On the Time ribbon tab, set Start Time and End Time extents. Set Step Interval to '1 Days'.", "في شريط Time، اضبط نطاق البداية والنهاية، واضبط خطوة الانتقال الزمني Step Interval على يوم واحد.", "Time Ribbon > Step Interval", "Configure Slider Steps", {"Step": "1 Days"}),
           ("Configure Cumulative Playback", "ضبط العرض التراكمي للبيانات التاريخية", "Check 'Show data cumulatively' so earlier earthquake points remain visible as new ones appear.", "فعل خيار Show data cumulatively لتظل الزلازل السابقة ظاهرة مع ظهور الهزات الجديدة.", "Time Ribbon > Playback Settings", "Set Cumulative", {})
       ],
       ("Interactive chronological playback revealing seismic wave fault line progression across the study area.", "عرض زمني متحرك يكشف تسلسل انتشار بؤر الهزات الارتدادية عبر خطوط الصدع الجيولوجي."),
       ("Click Play on the Time Slider control; confirm features appear and accumulate in synchrony with date stamps.", "انقر تشغيل وتأكد من ظهور وتراكم النقاط على الخريطة بتزامن تام مع تقدم عداد الأيام."),
       ("Selecting 'Each feature has start and end time fields' when the dataset only contains an instantaneous event point in time.", "اختيار حقول بداية ونهاية لبيانات لحظية لا تحوي سوى تاريخ حدوث واحد فقط."),
       ("Export the temporal progression to an MP4 video or animated GIF via the Animation ribbon tab.", "تصدير العرض الزمني إلى فيديو MP4 أو صورة متحركة GIF عبر شريط Animation.")
)

# WF-016: Range Slider Filtering
add_wf("WF-016", "Visualization", "Intermediate", ["Range Slider"],
       ["Determine how to visualize temporal, ranged, or 3D data"], ["time"],
       ("Interactive Facility Floor Inspection Using the Range Slider", "فحص طوابق المباني الداخلية تفاعلياً باستخدام منزلق المدى (Range Slider)"),
       ("Isolate and inspect indoor utility assets (security cameras, fire valves) floor-by-floor using an integer level range slider.", "عزل وفحص أصول المباني الداخلية (كاميرات المراقبة، محابس الحريق) طابقاً بطابق باستخدام منزلق المدى الرقمي."),
       ("Indoor_Assets 3D point layer with an integer 'FLOOR_LEVEL' field (values 1 through 10).", "طبقة مجسمات أصول داخلية مع حقل رقمي FLOOR_LEVEL للأدوار من 1 إلى 10."),
       ("Assets displayed in a 3D building interior view.", "عرض الأصول داخل مشهد مجسم للمبنى."),
       [
           ("Enable Range on Layer", "تفعيل المدى في خصائص الطبقة", "Open Layer Properties > Range. Set Range Field to 'FLOOR_LEVEL'.", "افتح خصائص الطبقة > Range وحدد حقل FLOOR_LEVEL.", "Layer Properties > Range", "Set Range Field", {"Range Field": "FLOOR_LEVEL"}),
           ("Configure Range Slider Bounds", "ضبط حدود منزلق المدى", "On the Range ribbon tab, set Minimum: 1, Maximum: 10, Step: 1.", "في شريط Range، اضبط الحد الأدنى 1 والأعلى 10 وخطوة الانتقال بـ 1.", "Range Ribbon > Extents", "Configure Range", {"Min": "1", "Max": "10", "Step": "1"}),
           ("Step Through Floors", "التنقل التفاعلي بين الأدوار", "Use the on-screen Range Slider arrows to step from floor 1 to floor 5, isolating single floor levels.", "استخدم أسهم منزلق المدى على الشاشة للانتقال بين الطوابق وعزل أصول كل طابق على حدة.", "On-Screen Range Control", "Step Range", {})
       ],
       ("Clear, clutter-free inspection of interior floor plans with zero visual occlusion from adjacent levels.", "رؤية بصرية واضحة لأصول الطابق المستهدف دون تداخل أو حجب من طوابق المبنى الأخرى."),
       ("Step to Floor 3; verify that all assets on floors 1, 2, 4, and 5 are completely hidden from view.", "انتقل للطابق 3 وتأكد من اختفاء أصول كافة الطوابق الأخرى تماماً من شاشة العرض."),
       ("Attempting to configure Range on a Text field (Range requires numeric Short, Long, or Float fields).", "محاولة تطبيق منزلق المدى على حقل نصي؛ فالمنزلق يتطلب حقولاً رقمية صحيحة أو عشرية."),
       ("Combine Range Slider and Time Slider concurrently to filter multi-story buildings over time.", "دمج منزلق المدى مع منزلق الوقت لفحص تطابق المباني عبر فترات زمنية متعاقبة.")
)

# WF-017: Address Geocoding & Rematch
add_wf("WF-017", "Visualization", "Intermediate", ["Create Locator", "Geocode Addresses", "Rematch Addresses"],
       ["Given a scenario, apply a query"], ["geocoding"],
       ("Build Custom Address Locator and Rematch Unmatched Addresses", "بناء محدد عناوين مخصص ومطابقة العناوين غير المطابقة"),
       ("Create a PointAddress locator from municipal address points, batch geocode customer CSV records, and resolve candidate ties.", "إنشاء محدد عناوين من نقاط العناوين البلدية، وتكويد جدول عملاء، وحسم حالات التعادل في المطابقة."),
       ("City_Address_Points feature class and Customer_List.csv with ADDRESS, CITY, STATE, ZIP columns.", "طبقة نقاط العناوين وجدول العملاء CSV متضمناً أعمدة العنوان والمدينة والرمز البريدي."),
       ("ArcGIS Pro project connected to local data folder.", "اتصال المشروع بمجلد البيانات المحلي."),
       [
           ("Create Locator", "إنشاء محدد العناوين", "Run Create Locator tool: Role: Point Address, Reference Data: City_Address_Points, map HouseNumber and StreetName fields.", "شغل أداة Create Locator: الدور Point Address، والبيانات المرجعية نقاط العناوين مع مطابقة الحقول.", "Geoprocessing > Geocoding Tools > Create Locator", "Create Locator", {"Role": "Point Address", "Output Locator": "City_Locator"}),
           ("Batch Geocode Addresses", "تكويد جدول العناوين دفعة واحدة", "Run Geocode Addresses tool using City_Locator and Customer_List.csv, producing Geocoded_Customers feature class.", "شغل أداة Geocode Addresses باستخدام المحدد المنشأ وجدول العملاء لإنتاج طبقة العملاء المكانية.", "Geoprocessing > Geocoding Tools > Geocode Addresses", "Geocode Addresses", {"Input Table": "Customer_List.csv", "Input Address Locator": "City_Locator"}),
           ("Rematch Unmatched and Tied Records", "إعادة مطابقة العناوين غير المطابقة والمتعادلة", "Open Data ribbon > Rematch Addresses pane. Review 'Tied' and 'Unmatched' records, select correct candidates, and click Match.", "افتح نافذة Rematch Addresses، وراجع السجلات المتعادلة وغير المطابقة، وحدد المرشح الصحيح يدوياً واضغط Match.", "Data Ribbon > Rematch Addresses Pane", "Interactive Rematch", {})
       ],
       ("Fully geocoded customer point feature class with 100% matched score verification.", "طبقة معالم نقطية لجميع العملاء بمواقع مكانية دقيقة ونسبة مطابقة مكتملة 100%."),
       ("Examine Rematch pane summary statistics to ensure 0 Unmatched and 0 Tied records remain.", "افحص إحصائيات نافذة إعادة المطابقة للتأكد من وصول العناوين غير المطابقة والمتعادلة إلى صفر."),
       ("Assuming Tied addresses match automatically; candidate ties must be reviewed and confirmed manually.", "الاعتقاد بأن العناوين المتعادلة تُطابق آلياً؛ بل يجب فحصها واعتماد المرشح الصحيح يدوياً."),
       ("Use ArcGIS World Geocoding Service for global addresses when local reference data is unavailable.", "استخدام خدمة التكويد العالمية لـ ArcGIS Online في حال عدم توفر بيانات عناوين محلية.")
)

# WF-018: Multi-Criteria Raster Suitability
add_wf("WF-018", "Analysis and Geoprocessing", "Intermediate", ["Raster Calculator", "Reclassify"],
       ["Apply raster functions for raster and image processing"], ["raster"],
       ("Multi-Criteria Habitat Suitability Modeling with Map Algebra", "نمذجة الملاءمة المكانية متعددة المعايير باستخدام جبر الخرائط"),
       ("Combine reclassified slope, elevation, and vegetation rasters using Raster Calculator to identify optimal wildlife conservation sites.", "دمج طبقات الانحدار والارتفاع والغطاء النباتي المعاد تصنيفها باستخدام جبر الخرائط لتحديد مناطق المحميات المثالية."),
       ("DEM elevation raster, Slope raster (degrees), and Land_Cover categorical raster.", "راستر الارتفاع والانحدار بالدرجات والغطاء الأرضي."),
       ("Spatial Analyst extension enabled in project.", "تفعيل ترخيص Spatial Analyst بالمشروع."),
       [
           ("Reclassify Continuous Inputs", "إعادة تصنيف المدخلات المستمرة", "Run Reclassify on Slope: slopes 0-5° -> 5 (optimal), 5-15° -> 3, >15° -> 1 (poor). Save as 'Reclass_Slope'.", "شغل Reclassify على الانحدار: من 0-5 درجات القيمة 5، ومن 5-15 القيمة 3، وأكبر من 15 القيمة 1.", "Geoprocessing > Spatial Analyst > Reclass > Reclassify", "Reclassify", {"Input Raster": "Slope", "Reclass field": "VALUE"}),
           ("Configure Snap Raster Environment", "ضبط بيئة محاذاة الراستر Snap Raster", "In Environments tab of Raster Calculator, set Snap Raster to 'DEM' and Extent to 'DEM' to prevent cell registration shift.", "في تبويب بيئات Raster Calculator، اضبط Snap Raster على DEM لمنع إزاحة محاذاة الخلايا.", "Tool Environments Tab", "Set Snap Raster", {"Snap Raster": "DEM.tif"}),
           ("Execute Map Algebra Expression", "تنفيذ معادلة جبر الخرائط الموزونة", "Run Raster Calculator: `(\"Reclass_Slope\" * 0.4) + (\"Reclass_Elev\" * 0.3) + (\"Reclass_Cover\" * 0.3)`.", "نفذ معادلة الجمع الموزون في Raster Calculator لحساب درجات الملاءمة المركبة.", "Geoprocessing > Spatial Analyst > Map Algebra > Raster Calculator", "Raster Calculator", {"Expression": "(\"Reclass_Slope\" * 0.4) + (\"Reclass_Elev\" * 0.3) + (\"Reclass_Cover\" * 0.3)"})
       ],
       ("Standardized composite suitability raster with pixel values ranked from 1.0 (unsuitable) to 5.0 (optimal).", "راستر ملاءمة نهائي موحد تتراوح قيمه بين 1.0 (غير ملائم) و 5.0 (ملائم ومثالي)."),
       ("Verify that output raster cell boundaries align seamlessly with input DEM cells with zero pixel displacement.", "تأكد من انطباق حدود خلايا الراستر الناتج تماماً مع خلايا DEM دون أي إزاحة بكسلية."),
       ("Combining continuous rasters with different measurement scales without reclassifying them first.", "جمع طبقات الراستر المستمرة ذات الوحدات المختلفة دون توحيد مقاييسها بإعادة التصنيف أولاً."),
       ("Use the 'Weighted Overlay' or 'Suitability Modeler' interactive pane for visual sensitivity weighting.", "استخدام أداة Weighted Overlay أو واجهة Suitability Modeler للأوزان التفاعلية.")
)

# WF-019: Hydrology Watershed Delineation
add_wf("WF-019", "Analysis and Geoprocessing", "Intermediate", ["Flow Direction", "Flow Accumulation", "Watershed"],
       ["Given a scenario, determine the appropriate geoprocessing tool"], ["hydrology"],
       ("Automated Drainage Basin and Watershed Delineation", "تحديد أحواض التصريف وشبكات المجاري المائية آلياً"),
       ("Process a raw digital elevation model to remove pits, calculate surface drainage routing, and delineate watershed boundaries.", "معالجة نموذج الارتفاع الرقمي لملء الحفر، وحساب اتجاه وتجمع الجريان، واستخلاص أحواض التصريف."),
       ("Hydrologically clean 10m DEM and a pour point feature class (reservoir intake point).", "راستر DEM بدقة 10م ونقاط مصب مائية (نقطة مأخذ خزان المياه)."),
       ("Project spatial reference set to a projected coordinate system (UTM or State Plane).", "ضبط نظام إحداثيات المشروع على نظام مسقط بأمتار أو أقدام."),
       [
           ("Fill Sinks in DEM", "ملء منخفضات وحفر السطح", "Run Fill tool on raw DEM to eliminate spurious depressions and ensure continuous downslope flow.", "شغل أداة Fill لملء الحفر والمنخفضات الوهمية لضمان استمرار الجريان الهيدرولوجي السطحي.", "Geoprocessing > Spatial Analyst > Hydrology > Fill", "Fill", {"Input Surface Raster": "Raw_DEM.tif"}),
           ("Calculate Flow Direction and Accumulation", "حساب اتجاه وتجمع الجريان السطحي", "Run Flow Direction (D8 method) on Filled DEM. Then run Flow Accumulation on Flow Direction raster.", "شغل Flow Direction بطريقة D8، ثم شغل Flow Accumulation لحساب الخلايا المتدفقة لكل بكسل.", "Geoprocessing > Spatial Analyst > Hydrology", "Flow Direction & Accumulation", {"Method": "D8"}),
           ("Delineate Watershed Polygon", "استخلاص حوض التصريف المائي", "Run Snap Pour Point on intake point, then run Watershed using Flow Direction and snapped pour point.", "شغل Snap Pour Point لمحاذاة نقطة المأخذ مع مجرى الجريان، ثم شغل أداة Watershed.", "Geoprocessing > Spatial Analyst > Hydrology > Watershed", "Watershed", {"Input Flow Direction": "FlowDir.tif"})
       ],
       ("Accurate drainage basin raster representing all terrain areas contributing runoff to the reservoir intake.", "راستر حوض تصريف دقيق يمثل كافة مساحات التضاريس التي تصب مياهها في خزان السد."),
       ("Convert watershed raster to polygon and verify that the pour point sits precisely at the basin outlet throat.", "حول راستر الحوض لمضلع وتأكد من وقوع نقطة المصب عند مخرج الحوض بدقة متناهية."),
       ("Running Flow Direction on raw un-filled DEM, producing fragmented flow vectors terminated at micro-pits.", "تشغيل اتجاه الجريان على راستر خام دون ملء الحفر مما يقطع شبكة الأودية عند المنخفضات الوهمية."),
       ("Use the online Hydrology Analysis tasks in ArcGIS Online for rapid server-based delineation.", "استخدام أدوات التحليل الهيدرولوجي السحابية في ArcGIS Online للاستخلاص السريع.")
)

# WF-020: Surface Slope & Aspect
add_wf("WF-020", "Analysis and Geoprocessing", "Beginner", ["Slope", "Aspect"],
       ["Apply raster functions for raster and image processing"], ["surface"],
       ("Terrain Morphometry: Slope Percentage and Solar Aspect Modeling", "تحليل مورفومترية التضاريس: حساب نسبة الانحدار والواجهة الشمسية"),
       ("Calculate ground slope in percent rise for road grading compliance and determine compass aspect for solar energy capture.", "حساب انحدار الأرض كنسبة مئوية لتصميم الطرق وتحديد الواجهة الجغرافية لتركيب ألواح الطاقة الشمسية."),
       ("High-resolution LiDAR bare-earth DEM.", "نموذج ارتفاع رقمي عالي الدقة من مسح ليدار."),
       ("Spatial reference in planar linear meters.", "نظام الإحداثيات بوحدات قياس مترية مستوية."),
       [
           ("Calculate Slope in Percent Rise", "حساب الانحدار كنسبة مئوية", "Run Slope tool: Output measurement: 'PERCENT_RISE', Method: Geodesic. Z-Factor: 1.0.", "شغل أداة Slope مع اختيار قياس PERCENT_RISE وطريقة جيوديسية ومعامل Z بقيمة 1.0.", "Geoprocessing > Spatial Analyst > Surface > Slope", "Slope", {"Output measurement": "PERCENT_RISE", "Method": "GEODESIC"}),
           ("Calculate Solar Aspect", "حساب واجهة الانحدار Aspect", "Run Aspect tool on DEM with Geodesic method, producing azimuths 0-360 degrees and -1 for flat cells.", "شغل أداة Aspect على نموذج الارتفاع لإنتاج زوايا السمت من 0 إلى 360 درجة وقيمة -1 للمستوي.", "Geoprocessing > Spatial Analyst > Surface > Aspect", "Aspect", {"Method": "GEODESIC"}),
           ("Filter Optimal Solar Cells", "عزل الخلايا الملائمة شمسياً", "Use Con in Raster Calculator to select cells where Slope < 10% AND Aspect between 135° and 225° (South-facing).", "استخدم دالة Con في Raster Calculator لعزل الخلايا ذات الانحدار أقل من 10% والواجهة الجنوبية.", "Raster Calculator", "Select Solar Sites", {"Expression": "Con((\"Slope_Pct\" < 10) & (\"Aspect\" >= 135) & (\"Aspect\" <= 225), 1, 0)"})
       ],
       ("Binary suitability raster identifying gentle south-facing slopes optimal for solar farm construction.", "راستر ملاءمة ثنائي يحدد المنحدرات اللطيفة المواجهة للجنوب والمثالية لبناء محطات الطاقة الشمسية."),
       ("Verify flat water reservoirs in the Aspect raster evaluate to -1 and are excluded from solar suitability.", "تأكد من أن المسطحات المائية المستوية أخذت القيمة -1 في راستر الواجهة واستُبعدت من الملاءمة."),
       ("Confusing DEGREE (0-90) with PERCENT_RISE (where 45° = 100%), miscalculating engineering grade constraints.", "الخلط بين الدرجات الزاوية ونسبة الارتفاع المئوية مما يفسد حسابات الانحدار الهندسي."),
       ("Use dynamic Surface Raster Functions for zero-disk instant visual feedback.", "استخدام دوال راستر السطح التفاعلية (Surface Raster Functions) للمعاينة الفورية دون كتابة ملفات.")
)

# WF-021: Space-Time Cubes & Hot Spots
add_wf("WF-021", "Analysis and Geoprocessing", "Advanced", ["Create Space Time Cube By Aggregating Points", "Emerging Hot Spot Analysis"],
       ["Given a scenario, determine the appropriate geoprocessing tool"], ["spacetime"],
       ("Spatio-Temporal Trend Analysis: Space-Time Cubes and Emerging Hot Spots", "تحليل الاتجاهات المكانية الزمانية: مكعبات الزمان والمكان والبؤر الساخنة المتصاعدة"),
       ("Aggregate 10 years of vehicle theft points into a 3D NetCDF space-time lattice and detect intensifying vs diminishing hot spots.", "تجميع بيانات سرقات السيارات على مدى 10 سنوات في مكعب NetCDF واكتشاف البؤر الساخنة المتصاعدة والمتلاشية."),
       ("Vehicle_Thefts point layer with 'INCIDENT_DATETIME' timestamp across a metropolitan county.", "طبقة نقاط جرائم سرقة المركبات متضمنة حقل التاريخ والوقت."),
       ("Time and coordinate fields populated without nulls.", "خلو حقول التواريخ والإحداثيات من القيم الفارغة."),
       [
           ("Create Space Time Cube", "إنشاء مكعب الزمان والمكان", "Run Create Space Time Cube By Aggregating Points: Distance Interval: 1000m, Time Step: 1 Months, Aggregation Shape: Hexagon.", "شغل أداة Create Space Time Cube: مسافة الخلية 1000م، والخطوة الزمنية شهر واحد، بشكل أشكال سداسية.", "Geoprocessing > Space Time Pattern Mining", "Create Space Time Cube", {"Time Step Interval": "1 Months", "Distance Interval": "1000 Meters", "Aggregation Shape": "HEXAGON_GRID"}),
           ("Execute Emerging Hot Spot Analysis", "تحليل البؤر الساخنة الصاعدة", "Run Emerging Hot Spot Analysis using the generated .nc cube and Conceptualization of Spatial Relationships: Fixed Distance.", "شغل أداة Emerging Hot Spot Analysis على ملف .nc المنشأ مع تحديد علاقة المسافة الثابتة.", "Geoprocessing > Space Time Pattern Mining", "Emerging Hot Spot Analysis", {"Input Space Time Cube": "Thefts.nc", "Analysis Variable": "COUNT"}),
           ("Interpret Categorical Trend Results", "تفسير نتائج أنماط الاتجاهات", "Symbolize results to identify 'New Hot Spots' (emerged in latest month) vs 'Intensifying Hot Spots' (long-term upward trend).", "رمز النتائج لتمييز البؤر الساخنة الجديدة (ظهرت مؤخراً) عن البؤر المتصاعدة (ذات اتجاه تصاعدي مزمن).", "Map Symbology", "Symbolize Trends", {})
       ],
       ("Actionable predictive crime map classifying neighborhoods into 17 spatio-temporal trend categories.", "خريطة تنبؤية أمنية تصنف الأحياء إلى 17 نمطاً مكانياً زمانياً لدعم توجيه الدوريات."),
       ("Review output summary charts and verify that statistical Mann-Kendall trend tests are statistically significant.", "راجع الرسوم البيانية وتأكد من أن اختبارات مان-كندال الإحصائية للاتجاه ذات دلالة موثوقة."),
       ("Specifying a time-step interval that is too small (e.g. 1 hour) resulting in an empty, sparse cube with zero variance.", "اختيار خطوة زمنية ضيقة جداً كساعة واحدة مما ينتج مكعباً مخلخلاً بأوعية فارغة تنعدم فيها الدلالة."),
       ("Visualize the 3D NetCDF cube directly in an ArcGIS Pro 3D Local Scene using the 'Visualize Space Time Cube in 3D' tool.", "عرض المكعب ثلاثي الأبعاد في مشهد محلي باستخدام أداة Visualize Space Time Cube in 3D.")
)

# WF-022: Network Analyst Service Area
add_wf("WF-022", "Analysis and Geoprocessing", "Intermediate", ["Make Service Area Analysis Layer", "Solve"],
       ["Given a scenario, determine the appropriate geoprocessing tool"], ["network"],
       ("Multi-Modal Isochrone Catchment Modeling with Network Analyst", "نمذجة نطاقات التغطية الزمنية المتعددة باستخدام محلل الشبكات"),
       ("Generate 5-minute, 10-minute, and 15-minute emergency ambulance drive-time coverage catchments around medical centers.", "إنشاء نطاقات وصول سيارات الإسعاف خلال 5 و 10 و 15 دقيقة قيادة حول المستشفيات المركزية."),
       ("Streets network dataset with travel time impedance, and Hospital point facilities.", "شبكة طرق معرف عليها زمن الانتقال، وطبقة نقاط المستشفيات."),
       ("Network Analyst extension licensed and enabled.", "تفعيل ترخيص Network Analyst بالمشروع."),
       [
           ("Create Service Area Layer", "إنشاء طبقة تحليل نطاق الخدمة", "In Analysis ribbon > Network Analysis dropdown, select 'Service Area'.", "في شريط Analysis، انقر على Network Analysis واختَر Service Area.", "Analysis Ribbon > Network Analysis > Service Area", "Make Service Area", {}),
           ("Load Facilities and Set Cutoffs", "تحميل المنشآت وضبط فترات الوصول", "Open 'Import Facilities', load Hospitals. In Travel Settings, set Cutoffs: '5 10 15', Travel Mode: 'Driving Time', Direction: 'Away From Facilities'.", "حمل المستشفيات في Facilities؛ وفي الإعدادات حدد Cutoffs: 5 10 15، ونمط Driving Time، والاتجاه بعيداً عن المنشآت.", "Service Area Ribbon > Cutoffs", "Configure Cutoffs", {"Cutoffs": "5 10 15", "Travel Mode": "Driving Time"}),
           ("Solve and Dissolve Polygons", "حل الشبكة ودمج المضلعات المتطابقة", "Set Polygon Output: 'Dissolve' (to merge overlapping hospital catchments), click 'Solve'.", "اضبط نمط المضلعات على Dissolve لدمج النطاقات المتداخلة، ثم اضغط على زر Solve.", "Service Area Ribbon > Solve", "Solve Network", {"Polygon Mode": "Dissolve"})
       ],
       ("Three concentric travel-time polygon rings detailing ambulance accessibility under realistic traffic speed limits.", "ثلاث حلقات مضلعية متحدة المركز تمثل أزمنة وصول الإسعاف وفق حدود سرعات الشوارع الحقيقية."),
       ("Inspect highway corridors; verify that isochrone fingers extend further along high-speed expressways than local streets.", "تأكد من امتداد أذرع النطاق لمسافات أطول على الطرق السريعة مقارنة بالشوارع المحلية الضيقة."),
       ("Using Euclidean buffer tool instead of network solver, completely ignoring street layout and one-way restrictions.", "استخدام أداة النطاق الإقليدي الدائري العادي متجاهلاً مسارات الشوارع والاتجاهات الإجبارية."),
       ("Use 'Origin-Destination Cost Matrix' when calculating travel times without needing visual polygon geometries.", "استخدام مصفوفة التكلفة (OD Cost Matrix) عند الحاجة لحساب أزمنة السفر في جداول دون مضلعات.")
)

# WF-023: ModelBuilder Batch Processing
add_wf("WF-023", "Analysis and Geoprocessing", "Intermediate", ["ModelBuilder", "Iterate Feature Classes"],
       ["Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow"], ["model"],
       ("Build an Automated Multi-Layer Batch Pipeline with ModelBuilder", "بناء مسار أتمتة لمعالجة طبقات متعددة دفعة واحدة في ModelBuilder"),
       ("Iterate through 20 district shapefiles, reproject to State Plane, buffer by 500m, and export using inline substitution `%Name%`.", "التكرار عبر 20 ملف shapefile، وإعادة إسقاطها، وإنشاء نطاق عازل 500م، وتصديرها بأسماء ديناميكية."),
       ("Folder containing 20 raw district polygon shapefiles.", "مجلد يحتوي على 20 ملف shapefile لدوائر إدارية."),
       ("ModelBuilder canvas opened from Analysis ribbon.", "فتح لوحة ModelBuilder من شريط Analysis."),
       [
           ("Add Iterator", "إضافة أداة التكرار", "In ModelBuilder ribbon > Insert > Iterators > select 'Iterate Feature Classes'. Set input folder and wildcard.", "في شريط ModelBuilder، اختر Iterators > Iterate Feature Classes مع تحديد مجلد المدخلات.", "ModelBuilder Ribbon > Iterators", "Iterate Feature Classes", {"Feature Type": "Polygon"}),
           ("Add Project and Buffer Tools", "إضافة أدوات الإسقاط والنطاق العازل", "Drag Project and Buffer tools onto canvas. Connect Iterator output to Project, and Project output to Buffer.", "اسحب أداتي Project و Buffer للوحة؛ ووصل مخرج المكرر بـ Project ثم بـ Buffer.", "Catalog Pane > Drag Tools", "Connect Tools", {}),
           ("Configure Dynamic Output Paths", "ضبط مسار المخرجات بالاستبدال الضمني", "In Buffer output path, enter: `%workspace%/Buffer_500m_%Name%` to name each file after its source shapefile.", "في مسار مخرج Buffer، اكتب: `%workspace%/Buffer_500m_%Name%` لتسمية النتائج آلياً.", "Buffer Tool Dialog", "Set Output Path", {"Output": "%workspace%/Buffer_500m_%Name%"}),
           ("Run and Verify", "تشغيل النموذج والتحقق", "Click 'Run' on ribbon. Observe tools flash in sequence, producing 20 distinct feature classes in the target geodatabase.", "انقر Run، ولاحظ إضاءة الأدوات بالتتابع وتوليد 20 فئة معالم مستقلة في قاعدة البيانات.", "ModelBuilder Ribbon > Run", "Run Model", {})
       ],
       ("20 uniformly reprojected and buffered feature classes generated automatically in minutes without repetitive manual clicks.", "20 فئة معالم مسقطة ومحاطة بنطاق 500م أُنشئت آلياً في دقائق معدودة دون نقرات يدوية مكررة."),
       ("Open target geodatabase in Catalog and verify exactly 20 new feature classes exist with correct '%Name%' suffixes.", "افتح قاعدة البيانات وتأكد من وجود 20 فئة معالم جديدة بالأسماء المستبدلة ديناميكياً بدقة."),
       ("Attempting to add two iterators into the same model without nesting one inside a submodel.", "محاولة إضافة مكررين في نفس النموذج دون بناء نموذج فرعي مما يعطل تشغيل النموذج."),
       ("Export the validated model to a clean Python script using 'Export To Python File' for server scheduling.", "تصدير النموذج إلى سكربت بايثون عبر Export To Python File لجدولته على الخوادم.")
)

# WF-024: ArcPy Cursor Automation
add_wf("WF-024", "Analysis and Geoprocessing", "Intermediate", ["ArcPy", "UpdateCursor"],
       ["Given a scenario, use tasks, batch processing, models, or scripts for a complex workflow"], ["arcpy"],
       ("Automate Feature Attribute Updates and Data Cleanup with ArcPy Cursors", "أتمتة تحديث السمات وتنظيف البيانات برمجياً باستخدام مؤشرات ArcPy"),
       ("Write a standalone Python script to scan utility pipelines, flag missing pressure values, and calculate replacement costs.", "كتابة سكربت بايثون لفحص خطوط الأنابيب، وتحديد قيم الضغط المفقودة، وحساب تكاليف الاستبدال التقديرية."),
       ("Water_Mains feature class with LENGTH_FT, DIAMETER_IN, and REPLACEMENT_COST fields.", "فئة معالم أنابيب المياه مع حقول الطول والقطر وتكلفة الاستبدال."),
       ("Python window or external IDE (VS Code) open with arcpy environment.", "نافذة بايثون في ArcGIS Pro أو محرر خارجي متصل ببيئة arcpy."),
       [
           ("Import ArcPy and Set Workspace", "استيراد المكتبة وضبط مساحة العمل", "Import arcpy, set `arcpy.env.workspace = r'C:/Data/Water.gdb'` and `arcpy.env.overwriteOutput = True`.", "استورد arcpy واضبط مسار قاعدة البيانات وسماحية استبدال الملفات.", "Python Script Header", "Setup Environment", {}),
           ("Construct UpdateCursor with Context Manager", "بناء مؤشر التحديث داخل مدير السياق with", "Define fields: `['DIAMETER_IN', 'LENGTH_FT', 'REPLACEMENT_COST']`. Open cursor: `with arcpy.da.UpdateCursor('Water_Mains', fields) as cursor:`.", "حدد الحقول المطلوبة، وافتح المؤشر باستخدام صيغة with لضمان تحرير أقفال قاعدة البيانات آلياً.", "Python Loop Structure", "Initialize Cursor", {"Fields": "['DIAMETER_IN', 'LENGTH_FT', 'REPLACEMENT_COST']"}),
           ("Compute Values and Commit Edits", "حساب القيم وحفظ التعديلات في السجلات", "Inside loop: `cost_per_foot = row[0] * 12.5; row[2] = row[1] * cost_per_foot; cursor.updateRow(row)`.", "داخل الحلقة: احسب التكلفة بناءً على القطر والطول، ثم استدعِ cursor.updateRow(row) لتثبيت الحفظ.", "Cursor Iteration Body", "Update Row", {})
       ],
       ("Fully updated feature class with thousands of replacement cost calculations executed in seconds with zero locks.", "تحديث آلاف السجلات وحساب تكاليف الاستبدال بدقة متناهية وفي ثوانٍ معدودة مع فك الأقفال تلقائياً."),
       ("Open attribute table in ArcGIS Pro and confirm that all REPLACEMENT_COST cells contain positive numeric values.", "افتح جدول الطبقة وتأكد من ملء حقل التكلفة بقيم رقمية صحيحة لكافة السجلات دون أي خانات فارغة."),
       ("Modifying row array (`row[2] = ...`) without calling `cursor.updateRow(row)`, resulting in silent failure to save changes.", "تعديل مصفوفة السجل دون استدعاء دالة cursor.updateRow(row) مما يؤدي لعدم حفظ التعديلات."),
       ("Use 'Calculate Field' geoprocessing tool with an Arcade or Python expression if coding a standalone script is not required.", "استخدام أداة Calculate Field مع تعبير Arcade كبديل سريع دون الحاجة لكتابة سكربت كامل.")
)

# WF-025: Professional Map Layout Design
add_wf("WF-025", "Layouts and Sharing", "Beginner", ["New Layout", "Insert Map Frame", "Insert Scale Bar"],
       ["Determine how to create and manage map layouts and map series"], ["layouts"],
       ("Design a Publication-Grade Map Layout with Multiple Linked Frames", "تصميم لوحة خريطة احترافية للطباعة مع أطر متعددة مترابطة"),
       ("Compose an ANSI D (24x36 inch) presentation layout containing a main detailed map frame, overview locator frame, dynamic legend, and north arrow.", "تصميم لوحة طباعة بمقاس 24×36 بوصة تحتوي إطار خريطة رئيسياً، وخريطة دليلية، ومقياس رسم ديناميكياً، وسهم الشمال."),
       ("Completed 2D project map with styled layers and balanced visual hierarchy.", "خريطة مشروع ثنائية مكتملة الرموز وذات تسلسل بصري متوازن."),
       ("ArcGIS Pro project opened with Insert ribbon tab active.", "فتح المشروع وتفعيل شريط Insert."),
       [
           ("Create New Layout", "إنشاء لوحة طباعة جديدة", "Navigate to Insert > New Layout. Select ANSI D Landscape (36 x 24 inches).", "انتقل إلى Insert > New Layout واختَر قياس ANSI D أفقي (36 × 24 بوصة).", "Insert Ribbon > New Layout", "Create Layout", {"Page Size": "ANSI D Landscape (36 x 24 in)"}),
           ("Insert and Lock Main Map Frame", "إدراج وتثبيت إطار الخريطة الرئيسي", "Click Insert > Map Frame, draw large rectangle. Activate frame, zoom to 1:10,000 scale, and lock extent.", "أدرج إطار الخريطة الرئيسي، واضبط مقياس الرسم على 1:10,000 واقفل الإطار لمنع تحريكه بالخطأ.", "Insert Ribbon > Map Frame", "Insert Main Frame", {"Scale": "1:10,000"}),
           ("Insert Linked Overview Frame and Extent Indicator", "إدراج خريطة الدليل ومؤشر النطاق", "Insert a small 4x4 inch overview frame at 1:100,000 scale. Click Insert > Extent Indicator, link it to Main Map Frame.", "أدرج إطار دليل صغيراً بمقياس 1:100,000، وأدرج Extent Indicator واربطه بالإطار الرئيسي.", "Insert Ribbon > Extent Indicator", "Link Extent Indicator", {"Source Frame": "Main Map Frame"}),
           ("Add Scale Bar and Dynamic Legend", "إضافة مقياس الرسم ودليل الخريطة الديناميكي", "Insert Alternating Scale Bar linked to Main Frame. Insert Legend, check 'Only show features visible in map extent'.", "أدرج مقياس رسم مرتبطاً بالإطار الرئيسي، ودليل خريطة مفعل عليه خيار إظهار المعالم المرئية فقط.", "Insert Ribbon > Map Surrounds", "Add Surrounds", {})
       ],
       ("Publication-ready cartographic layout meeting municipal presentation standards with dynamic element linking.", "لوحة كارتوغرافية جاهزة للطباعة والنشر مطابقة للمعايير البلدية مع ارتباط ديناميكي لكافة العناصر."),
       ("Pan the main map frame in an activated state; verify that the red extent indicator rectangle on the overview locator moves concurrently.", "حرك الخريطة الرئيسية وتأكد من تحرك مستطيل مؤشر النطاق على الخريطة الدليلية بتزامن تام."),
       ("Linking the scale bar to the overview locator frame instead of the main frame, displaying incorrect scales.", "ربط مقياس الرسم بخريطة الدليل بدلاً من الخريطة الرئيسية مما ينتج مقاييس رسم خاطئة تماماً."),
       ("Save the completed layout as a Layout File (.pagx) to reuse the layout composition across other department projects.", "حفظ اللوحة كملف Layout File (.pagx) لإعادة استخدام تصميم وهوية اللوحة في مشاريع أخرى.")
)

# WF-026: Spatial Map Series Automation
add_wf("WF-026", "Layouts and Sharing", "Intermediate", ["Spatial Map Series", "Dynamic Text"],
       ["Determine how to create and manage map layouts and map series"], ["mapseries"],
       ("Automate a Multi-Page Spatial Map Series with Dynamic Border Text", "أتمتة إنتاج أطلس متعدد الصفحات عبر سلسلة الخرائط المكانية والنصوص الديناميكية"),
       ("Generate a 40-page county parcel map book from a single layout using parcel grid tiles as the index layer.", "إنشاء أطلس عقاري للمقاطعة من 40 صفحة باستخدام شبكة مربعات الأراضي كطبقة فهرس عبر لوحة طباعة موحدة."),
       ("Layout containing a Map Frame, and a Grid_Index polygon layer with 'PAGE_NAME' and 'PAGE_NUM' attributes.", "لوحة طباعة مع طبقة شبكة الفهرس Grid_Index تحوي حقلي اسم ورقم الصفحة."),
       ("Grid tiles completely cover the municipal jurisdiction.", "تغطية شبكة الفهرس لكامل النطاق الجغرافي للبلدية."),
       [
           ("Enable Spatial Map Series", "تفعيل سلسلة الخرائط المكانية", "In Layout view, click Layout ribbon > Map Series dropdown > 'Spatial'.", "في شريط Layout، انقر على قائمة Map Series واختَر Spatial.", "Layout Ribbon > Map Series > Spatial", "Enable Map Series", {}),
           ("Configure Map Series Parameters", "ضبط معاملات ومعايير السلسلة", "Set Map Frame: 'Main Frame', Index Layer: 'Grid_Index', Name Field: 'PAGE_NAME', Sort Field: 'PAGE_NUM'.", "حدد إطار الخريطة الرئيسي، وطبقة الفهرس Grid_Index، وحقل الاسم PAGE_NAME وحقل الترتيب PAGE_NUM.", "Map Series Options Pane", "Set Index Parameters", {"Index Layer": "Grid_Index", "Name Field": "PAGE_NAME", "Sort Field": "PAGE_NUM"}),
           ("Insert Dynamic Title and Page Counters", "إدراج العنوان وأرقام الصفحات الديناميكية", "Insert Dynamic Text: Sheet `<dyn type=\"page\" property=\"name\"/>` and Page `<dyn type=\"page\" property=\"number\"/> of <dyn type=\"page\" property=\"count\"/>`.", "أدرج نصوصاً ديناميكية لاسم اللوحة ورقم الصفحة الحالية وإجمالي عدد الصفحات.", "Insert Ribbon > Dynamic Text", "Insert Page Tags", {}),
           ("Export Multi-Page PDF Atlas", "تصدير الأطلس كاملاً إلى ملف PDF", "Click Share > Export Layout. Format: PDF, under Map Series export: 'All (40 pages)' into a single multi-page PDF document.", "انقر Export Layout، واختَر صيغة PDF، وتحت خيارات Map Series حدد تصدير All (40 pages) في ملف مدمج.", "Share Ribbon > Export Layout", "Export Multi-Page PDF", {"Pages": "All", "File": "County_Atlas.pdf"})
       ],
       ("Complete 40-page indexed PDF map book generated automatically in a single export operation.", "أطلس خرائط متكامل من 40 صفحة مفهرسة ومصدرة آلياً في عملية تصدير موحدة."),
       ("Open the exported PDF; flip through consecutive pages and verify that titles, map extents, and page numbers increment accurately.", "افتح ملف PDF وتصفح الصفحات وتأكد من تغير عناوين اللوحات وأرقام الصفحات ومواقع الخريطة بدقة."),
       ("Selecting a Sort Field with non-sequential or null values, causing jumbled and missing page sequences.", "اختيار حقل ترتيب يحتوي على قيم فارغة أو غير متسلسلة مما يخل بترتيب صفحات الأطلس."),
       ("Configure a 'Clip to index feature' under Map Frame properties to visually hide features outside the active page boundary.", "تفعيل خيار Clip to index feature في خصائص الإطار لحجب المعالم الواقعة خارج مربع الصفحة الحالية.")
)

# WF-027: Publish Web Feature Layer with Sync
add_wf("WF-027", "Layouts and Sharing", "Intermediate", ["Share Web Layer", "Analyzer"],
       ["Choose how to share content from ArcGIS Pro"], ["weblayers"],
       ("Publish an Editable Web Feature Layer with Offline Sync Enabled", "نشر طبقة معالم ويب تفاعلية وقابلة للتحرير الميداني مع تفعيل المزامنة"),
       ("Publish asset layers to ArcGIS Online/Enterprise for mobile field inspections in ArcGIS Field Maps with offline capabilities.", "نشر طبقة أصول إلى السحابة أو الخادم المؤسسي للاستخدام في تطبيق Field Maps مع دعم العمل دون إنترنت."),
       ("Water_Valves feature class with GlobalIDs and Editor Tracking enabled.", "فئة معالم محابس المياه مع تفعيل معرفات GlobalID وتتبع المحررين."),
       ("Signed in to ArcGIS Online or ArcGIS Enterprise with Publisher/Administrator privileges.", "تسجيل الدخول في البرنامج بحساب يملك صلاحيات النشر والإدارة."),
       [
           ("Open Share Web Layer Pane", "فتح نافذة مشاركة طبقة ويب", "Right-click Water_Valves > Sharing > Share As Web Layer.", "انقر بالزر الأيمن على الطبقة > Sharing > Share As Web Layer.", "Layer Context Menu > Sharing > Share As Web Layer", "Open Share Pane", {}),
           ("Configure Layer Type and Metadata", "ضبط نوع الطبقة والبيانات الوصفية", "Set Item Name: 'Water_Valves_Field', Summary and Tags. Under Layer Type, ensure 'Feature' is checked.", "حدد اسم العنصر والوصف والوسوم، وتأكد من تفعيل نوع Feature في خانات الاختيار.", "Share Pane > General Tab", "Set Details", {"Layer Type": "Feature"}),
           ("Enable Editing and Sync Capabilities", "تفعيل صلاحيات التحرير والمزامنة الميدانية", "In Configuration tab > Feature Properties, check 'Enable editing' and check 'Enable Sync' (required for offline maps).", "في تبويب Configuration، فعل خياري Enable editing و Enable Sync لدعم التحميل الميداني دون إنترنت.", "Share Pane > Configuration > Feature Properties", "Set Capabilities", {"Enable Editing": True, "Enable Sync": True}),
           ("Analyze and Publish", "فحص الأخطاء والنشر", "Click 'Analyze'. Ensure 0 red errors appear. Click 'Publish'.", "انقر Analyze، وتأكد من خلو الفاحص من أي أخطاء حمراء، ثم انقر Publish لبدء الرفع.", "Share Pane > Analyze & Publish", "Publish Layer", {})
       ],
       ("Operational hosted Feature Service ready for immediate interactive data collection in web and mobile field apps.", "خدمة معالم سحابية منشورة وجاهزة لجمع وتحديث البيانات الميدانية عبر الهواتف وتطبيقات الويب."),
       ("Open ArcGIS Online / Enterprise portal, inspect service item page, and confirm 'Sync' is listed under capabilities.", "افتح صفحة العنصر في بوابة المؤسسة وتأكد من إدراج خاصية Sync ضمن إمكانيات الخدمة."),
       ("Forgetting to add GlobalIDs before attempting to enable Sync, triggering fatal Error 00231 in the Analyzer.", "نسيان إضافة GlobalIDs قبل تفعيل المزامنة مما يطلق الخطأ الأحمر القاتل Error 00231 في الفاحص."),
       ("Choose 'Reference registered data' instead of 'Copy all data' when connecting to enterprise SQL Server databases.", "اختيار Reference registered data بدلاً من نسخ البيانات عند الاتصال بقواعد بيانات مؤسسية حية.")
)

# WF-028: Vector Tile Basemap Publishing
add_wf("WF-028", "Layouts and Sharing", "Intermediate", ["Create Vector Tile Package", "Share Package"],
       ["Choose how to share content from ArcGIS Pro"], ["vectortiles"],
       ("Build, Package, and Host a High-Performance Vector Tile Basemap", "بناء وتحزيم ونشر خريطة أساس متجهة فائقة الأداء (Vector Tiles)"),
       ("Compile multi-scale city road and land use vectors into a compressed vector tile package (.vtpk) for high-DPI displays.", "تجميع طبقات الطرق واستخدامات الأراضي في حزمة قوالب متجهة (.vtpk) لعرضها بدقة فائقة على شاشات الهواتف."),
       ("Map view with scale-dependent visibility ranges configured across road and parcel layers.", "خريطة مهيأة بنطاقات ظهور معتمدة على مقياس الرسم لكافة الطبقات."),
       ("Tiling scheme (ArcGIS Online / Bing Maps / Google Maps) confirmed.", "تحديد نظام التقطيع القياسي للقوالب."),
       [
           ("Set Scale Dependencies", "ضبط حدود مقاييس ظهور الطبقات", "Ensure detailed building footprints only draw at 1:5,000 or closer; major highways draw at all scales.", "اضبط مساقط المباني لتظهر فقط عند مقياس 1:5,000 فما دون، والطرق السريعة في كافة المقاييس.", "Layer Properties > General > Visibility Range", "Set Scale Limits", {}),
           ("Execute Create Vector Tile Package", "إنشاء حزمة القوالب المتجهة vtpk", "Run Create Vector Tile Package tool. Tiling Format: 'INDEXED', Min Scale: 1:500,000, Max Scale: 1:1,000.", "شغل أداة Create Vector Tile Package بنمط INDEXED، ومقياس يبدأ من 1:500,000 حتى 1:1,000.", "Geoprocessing > Data Management > Packaging", "Create Vector Tile Package", {"Tiling Format": "INDEXED", "Min Cached Scale": "500000", "Max Cached Scale": "1000"}),
           ("Share Vector Tile Package to Portal", "مشاركة ورفع الحزمة للبوابة", "Run Share Package tool to upload the .vtpk file to ArcGIS Online and automatically publish a Vector Tile Service.", "شغل أداة Share Package لرفع ملف .vtpk إلى السحابة ونشر خدمة القوالب المتجهة تلقائياً.", "Geoprocessing > Data Management > Packaging > Share Package", "Share Package", {"Publish web layer": True})
       ],
       ("Ultra-lightweight vector tile basemap delivering crisp rendering on retina displays with client-side restyling support.", "خريطة أساس متجهة خفيفة وسريعة توفر رسومات بالغة الحدة على شاشات Retina مع دعم تغيير الألوان فورياً."),
       ("Open the published vector tile layer in Map Viewer; zoom in to 1:500 scale and verify zero pixelation occurs.", "افتح الطبقة في Map Viewer وكبر حتى 1:500 وتأكد من بقاء الخطوط والرموز حادة تماماً دون أي بكسلة."),
       ("Using 'FLAT' tiling format instead of 'INDEXED' for areas with uneven data distribution, inflating file size.", "استخدام نمط التقطيع FLAT بدلاً من INDEXED في المناطق غير المتجانسة مما يضخم حجم الملف دون فائدة."),
       ("Customize the color palette in seconds without rebuilding tiles using the ArcGIS Vector Tile Style Editor.", "تعديل ألوان خريطة الأساس في ثوانٍ باستخدام أداة ArcGIS Vector Tile Style Editor دون إعادة بناء القوالب.")
)

# WF-029: Sharing Analyzer Troubleshooting
add_wf("WF-029", "Layouts and Sharing", "Intermediate", ["Share Web Layer", "Analyzer"],
       ["Choose how to share content from ArcGIS Pro"], ["weblayers"],
       ("Diagnose and Resolve Fatal Errors in the Sharing Analyzer Pane", "تشخيص ومعالجة الأخطاء القاتلة في نافذة فاحص المشاركة (Sharing Analyzer)"),
       ("Troubleshoot common web layer publishing blockers including missing spatial references and unsupported layer types.", "معالجة المعوقات الشائعة التي تعطل نشر طبقات الويب مثل غياب المرجع الإسقاطي أو الطبقات غير المدعومة."),
       ("Map containing a scratch CAD layer, a shapefile missing unique integer IDs, and a layer with an unprojected GCS.", "خريطة تضم طبقة CAD مؤقتة، وملف shapefile يفتقر لمعرف فريد، وطبقة بإحداثيات غير مسقطة."),
       ("Share As Web Layer pane opened with Publish button disabled.", "فتح نافذة مشاركة طبقة ويب وظهور زر Publish معطلاً."),
       [
           ("Click Analyze and Identify Red Errors", "فحص الخريطة وتحديد الأخطاء الحمراء القاتلة", "Click Analyze button. Review the Messages tab. Identify Error 00068 (missing projection) and Error 00160 (unsupported layer format).", "انقر Analyze، وافحص رسائل الخطأ، وحدد Error 00068 (غياب الإسقاط) و Error 00160 (صيغة غير مدعومة).", "Share Web Layer Pane > Analyze", "Run Analyzer", {}),
           ("Resolve Error 00160 (Unsupported Layer)", "حل خطأ 00160 بحذف أو تحويل الطبقة غير المدعومة", "Right-click Error 00160. Select 'Select Layer in Contents'. Export CAD layer to a geodatabase feature class and remove the raw CAD drawing.", "انقر بالزر الأيمن على الخطأ 00160، وحدد الطبقة في المحتويات، وقم بتصدير طبقة CAD إلى قاعدة البيانات واحذف الملف الخام.", "Contents Pane > Remove Layer", "Fix Unsupported Format", {}),
           ("Resolve Error 00068 (Coordinate System)", "حل خطأ 00068 بتعيين نظام إحداثيات سليم", "Right-click Error 00068 > Select Layer. Open Layer Properties > Source > Spatial Reference, or run Define Projection to assign valid coordinates.", "انقر بالزر الأيمن على الخطأ 00068، وعين نظام إحداثيات معتمداً للطبقة عبر أداة Define Projection.", "Geoprocessing > Define Projection", "Fix Spatial Reference", {}),
           ("Re-Analyze and Confirm Clearance", "إعادة الفحص والتأكد من تفعيل زر النشر", "Click 'Analyze' again. Confirm all red errors disappear. Warnings (yellow triangles) may remain. Click 'Publish'.", "انقر Analyze مجدداً؛ وتأكد من زوال الأخطاء الحمراء بالكامل وتفعيل زر Publish للمتابعة.", "Share Web Layer Pane", "Re-Analyze", {})
       ],
       ("Fully validated map configuration with all publishing roadblocks cleared, successfully published to portal.", "خريطة مستوفية لكافة المعايير البرمجية مع حل كافة العقبات ونشر الخدمة بنجاح إلى البوابة المؤسسية."),
       ("Verify in Sharing pane that the red error count is 0 and the blue 'Publish' button is enabled and clickable.", "تأكد من أن عدد الأخطاء الحمراء في الفاحص أصبح صفراً وزر النشر الأزرق أصبح متاحاً للنقر."),
       ("Attempting to bypass red errors; ArcGIS Pro strictly disables publishing until every red error is corrected.", "محاولة تجاهل الأخطاء الحمراء؛ فالبرنامج يمنع النشر تماماً حتى إصلاح كافة الأخطاء الحمراء دون استثناء."),
       ("Yellow warnings do not block publishing and can often be safely ignored if minor symbology changes are acceptable.", "التحذيرات الصفراء استشارية ولا تمنع النشر ويمكن تجاوزها إذا كان تبسيط بعض الرموز مقبولاً.")
)

# WF-030: Package Project (.ppkx) Archive
add_wf("WF-030", "Layouts and Sharing", "Beginner", ["Package Project"],
       ["Choose how to share content from ArcGIS Pro"], ["packages"],
       ("Package and Archive a Complete Workspace as a Compressed Project Package (.ppkx)", "تحزيم وأرشفة مساحة العمل المتكاملة في حزمة مشروع مدمجة (.ppkx)"),
       ("Bundle all 2D maps, 3D scenes, print layouts, custom Python tools, attachments, and underlying geodatabases into a single portable deliverable.", "دمج كافة الخرائط والمشاهد واللوحات وأدوات بايثون والمرفقات وقواعد البيانات في ملف أرشيف واحد للتسليم."),
       ("Multi-map engineering project ready for final archive and client delivery.", "مشروع هندسي مكتمل الخرائط وجاهز للأرشفة النهائية والتسليم للعميل."),
       ("Write permissions to local archive folder or active portal connection.", "توفر صلاحية الكتابة في مجلد الأرشيف أو الاتصال بالبوابة السحابية."),
       [
           ("Open Package Project Tool", "فتح أداة تحزيم المشروع", "Navigate to Share ribbon tab > Package group > click 'Project'.", "انتقل إلى شريط Share، ومن مجموعة Package انقر على زر Project.", "Share Ribbon > Package > Project", "Launch Package Tool", {}),
           ("Configure Packaging Options", "ضبط خيارات وضغط الحزمة", "Select 'Save package to file' and specify output path: `C:/Archive/Master_Project.ppkx`. Enter Summary and Description tags.", "حدد خيار الحفظ كملف محلي باسم Master_Project.ppkx، وأدخل ملخص المشروع والوسوم المطلوبة.", "Package Project Pane", "Set Package Options", {"Output File": "Master_Project.ppkx"}),
           ("Configure Data Inclusion and Geoprocessing History", "تضمين البيانات وسجل المعالجة الجغرافية", "Under Project Items, check 'Include toolboxes' and ensure 'Consolidate and package data' is selected so source files are bundled.", "تحت عناصر المشروع، فعل تضمين صناديق الأدوات، وتأكد من تفعيل دمج وتحزيم البيانات لنسخ ملفات المصدر.", "Package Project Settings", "Set Data Options", {"Consolidate Data": True}),
           ("Analyze and Package", "فحص الحزمة وضغط الملف النهائي", "Click 'Analyze' to verify paths, then click 'Package'. The tool consolidates databases and compresses into a single `.ppkx` file.", "انقر Analyze للتأكد من سلامة المسارات، ثم انقر Package لضغط وتوليد ملف .ppkx النهائي.", "Package Project Pane > Package", "Execute Packaging", {})
       ],
       ("Single self-contained .ppkx archive file that can be emailed or opened on any workstation with zero broken data links.", "ملف حزمة مشروع .ppkx مدمج ومكتفٍ ذاتياً يمكن إرساله وفتحه على أي جهاز دون أي مسارات مكسورة."),
       ("Double-click the .ppkx file on another computer or clean test folder; verify all maps, scenes, and layouts load immediately.", "انقر نقراً مزدوجاً على ملف .ppkx وتأكد من فتح كافة الخرائط واللوحات وعملها فورياً دون فقدان للبيانات."),
       ("Unchecking 'Consolidate and package data', which leaves underlying datasets on local drives and produces broken paths for clients.", "إلغاء خيار دمج البيانات مما يترك ملفات المصدر على القرص القديم وينتج مسارات معطلة لدى العميل."),
       ("Use 'Package Map' (.mpkx) when only a single map needs to be shared rather than the entire project workspace.", "استخدام حزمة الخريطة (.mpkx) عند الرغبة في مشاركة خريطة واحدة فقط بدلاً من كامل المشروع.")
)

print(f"Total Workflows defined: {len(workflows_list)} (target 30)")

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(workflows_list, f, ensure_ascii=False, indent=2)

print("Saved workflows/workflows.json successfully.")

