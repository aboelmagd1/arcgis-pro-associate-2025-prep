# -*- coding: utf-8 -*-
"""
Generate DM-040 to DM-080 to bring Data Management MCQs to exactly 80.
"""
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_file = os.path.join(base_dir, 'public', 'data', 'questions', 'data-management.json')
with open(target_file, 'r', encoding='utf-8') as f:
    existing = json.load(f)

print(f"Current existing DM questions: {len(existing)}")

dm_questions_to_add = [
    {
        "id": "DM-040", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Beginner", "type": "Technical", "tools": ["Create File Geodatabase"],
        "question": {
            "en": "What is the default maximum storage capacity of a single table or raster dataset in a File Geodatabase (.gdb)?",
            "ar": "ما هي السعة التخزينية القصوى الافتراضية لجدول واحد أو مجموعة بيانات راستر في قاعدة بيانات جغرافية ملفية (.gdb)؟"
        },
        "options": [
            {"id": "A", "text": {"en": "2 GB", "ar": "2 جيجابايت"}},
            {"id": "B", "text": {"en": "1 TB", "ar": "1 تيرابايت"}},
            {"id": "C", "text": {"en": "256 TB", "ar": "256 تيرابايت"}},
            {"id": "D", "text": {"en": "Unlimited depending only on operating system RAM", "ar": "غير محدود ويعتمد فقط على ذاكرة RAM لنظام التشغيل"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "By default, every table and raster dataset in a File Geodatabase has a 1 TB size limit. This can be configured up to 256 TB using the MAX_FILE_SIZE_256TB configuration keyword.",
            "ar": "افتراضياً، يكون الحد الأقصى لسعة كل جدول أو راستر في قاعدة بيانات File GDB هو 1 تيرابايت. ويمكن رفعها إلى 256 تيرابايت باستخدام الكلمة المفتاحية MAX_FILE_SIZE_256TB."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "2 GB is the file size limit for shapefile component files (.shp, .dbf), not File Geodatabase tables.",
                "C": "256 TB is the maximum achievable capacity when using the MAX_FILE_SIZE_256TB keyword, not the default.",
                "D": "File Geodatabase capacity is governed by dataset configuration keywords and disk storage, not RAM."
            },
            "ar": {
                "A": "2 جيجابايت هو الحد الأقصى لملفات shapefile وليس لجداول File Geodatabase.",
                "C": "256 تيرابايت هو الحد الأقصى بعد الترقية بالكلمة المفتاحية وليس الحد الافتراضي.",
                "D": "سعة قاعدة البيانات محكومة بكلمات التهيئة والمساحة التخزينية وليس بذاكرة RAM."
            }
        },
        "references": [{"title": "File geodatabase size and name limits, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-file-gdb/file-geodatabase-size-and-name-limits.htm", "kind": "official"}]
    },
    {
        "id": "DM-041", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Compact"],
        "question": {
            "en": "What is the primary effect of executing the Compact tool on a File Geodatabase?",
            "ar": "ما هو الأثر الأساسي لتشغيل أداة Compact على قاعدة بيانات جغرافية ملفية؟"
        },
        "options": [
            {"id": "A", "text": {"en": "It compresses vector data into read-only compressed geodatabase format", "ar": "تضغط البيانات الاتجاهية إلى صيغة مضغوطة للقراءة فقط"}},
            {"id": "B", "text": {"en": "It removes free space, reorganizes records, and rebuilds spatial indexes", "ar": "تزيل المساحات الفارغة غير المستخدمة وتعيد ترتيب السجلات وبناء الفهارس"}},
            {"id": "C", "text": {"en": "It zips the .gdb directory into a .zip archive on disk", "ar": "تضغط مجلد .gdb إلى أرشيف مضغوط .zip على القرص"}},
            {"id": "D", "text": {"en": "It archives retired historical versions of branch-versioned feature classes", "ar": "تؤرشف الإصدارات التاريخية القديمة لفئات المعالم ذات الإصدارات الفرعية"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "The Compact tool cleans up fragmented storage, recovers unused disk space left after edits and deletes, and rebuilds internal database indexes to optimize query performance.",
            "ar": "تقوم أداة Compact بتنظيف التخزين المجزأ واستعادة المساحات الفارغة بعد الحذف والتحرير وإعادة بناء الفهارس لتحسين أداء الاستعلامات."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Compress File Geodatabase Data is the tool that converts data to read-only compressed format, not Compact.",
                "C": "Compact does not create a ZIP archive; it defragments internal storage files inside the .gdb directory.",
                "D": "Version archiving and reconciliation are Enterprise Geodatabase versioning functions."
            },
            "ar": {
                "A": "أداة Compress File Geodatabase Data هي المسؤولة عن تحويل البيانات إلى صيغة للقراءة فقط.",
                "C": "أداة Compact لا تنشئ ملف ZIP بل تلغي تجزئة الملفات الداخلية في مجلد .gdb.",
                "D": "أرشفة الإصدارات تتعلق بقواعد بيانات Enterprise Geodatabase."
            }
        },
        "references": [{"title": "Compact (Data Management), ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/compact.htm", "kind": "official"}]
    },
    {
        "id": "DM-042", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Beginner", "type": "Conceptual", "tools": ["Create Mobile Geodatabase"],
        "question": {
            "en": "What underlying database technology is used by an ArcGIS Pro Mobile Geodatabase (.geodatabase)?",
            "ar": "ما هي تقنية قواعد البيانات الأساسية التي تعتمد عليها قاعدة البيانات الجغرافية المحمولة (.geodatabase) في ArcGIS Pro؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Microsoft Access JET engine", "ar": "محرك Microsoft Access JET"}},
            {"id": "B", "text": {"en": "SQLite / SpatiaLite", "ar": "SQLite / SpatiaLite"}},
            {"id": "C", "text": {"en": "PostgreSQL with PostGIS", "ar": "PostgreSQL مع PostGIS"}},
            {"id": "D", "text": {"en": "Apache Derby", "ar": "Apache Derby"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Mobile Geodatabases are built on the SQLite database engine using SpatiaLite spatial geometry, stored as a single cross-platform .geodatabase file ideal for mobile and offline workflows.",
            "ar": "تبنى قواعد البيانات الجغرافية المحمولة على محرك SQLite مع مكتبة SpatiaLite المكانية كملف فردي واحد .geodatabase مثالي للأجهزة المحمولة والعمل دون اتصال."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Personal Geodatabase (.mdb) used the MS Access JET engine and is deprecated in 64-bit ArcGIS Pro.",
                "C": "PostgreSQL is an Enterprise RDBMS, not the file format of a mobile geodatabase.",
                "D": "Apache Derby is a Java relational database not used for Esri mobile geodatabases."
            },
            "ar": {
                "A": "قواعد البيانات الشخصية Personal GDB القديمة كانت تستخدم MS Access وهي غير مدعومة في ArcGIS Pro.",
                "C": "PostgreSQL نظام مؤسسي متعدد المستخدمين وليس صيغة ملف محمولة.",
                "D": "Apache Derby قاعدة بيانات جافا ولا تستخدمها Esri في قواعد البيانات المحمولة."
            }
        },
        "references": [{"title": "Mobile geodatabases, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-mobile-gdb/mobile-geodatabases.htm", "kind": "official"}]
    },
    {
        "id": "DM-043", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Create Feature Dataset"],
        "question": {
            "en": "Which statement correctly describes the spatial reference requirement for feature classes inside a Feature Dataset?",
            "ar": "أي عبارة تصف بشكل صحيح شرط المرجع المكاني لفئات المعالم داخل طقم المعالم (Feature Dataset)؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Each feature class can have a different projected coordinate system as long as they share the same geographic datum", "ar": "يمكن لكل فئة معالم أن تمتلك نظام إسقاط مختلف طالما تشترك في نفس المرجع الجغرافي"}},
            {"id": "B", "text": {"en": "All feature classes in a feature dataset must share the identical coordinate system and spatial tolerance settings", "ar": "يجب أن تشترك كافة فئات المعالم في نفس نظام الإحداثيات وإعدادات التسامح المكاني تماماً"}},
            {"id": "C", "text": {"en": "Feature datasets only enforce coordinate systems if a geodatabase topology is created", "ar": "لا يفرض طقم المعالم نظام الإحداثيات إلا إذا تم إنشاء طوبولوجيا بداخله"}},
            {"id": "D", "text": {"en": "Feature datasets support vector feature classes in any coordinate system via automatic on-the-fly projection", "ar": "يدعم طقم المعالم فئات المعالم بأي نظام إحداثيات عبر الإسقاط اللحظي التلقائي"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "A Feature Dataset enforces an identical spatial reference (coordinate system, XY tolerance, and resolution) on all feature classes stored within it, which is essential for geodatabase topology and utility networks.",
            "ar": "يفرض طقم المعالم مرجعاً مكانياً موحداً ومطابقاً (نظام الإحداثيات، التسامح، والدقة) على جميع فئات المعالم بداخله، وهو متطلب إلزامي للطوبولوجيا وشبكات المرافق."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Different projected systems are not permitted; the spatial reference must match exactly.",
                "C": "The coordinate system is enforced at the feature dataset level upon creation, even without topology.",
                "D": "On-the-fly projection is a map display feature; physical storage in a feature dataset strictly prohibits mixed coordinate systems."
            },
            "ar": {
                "A": "لا يُسمح باختلاف نظم الإسقاط إطلاقاً داخل طقم المعالم الواحد.",
                "C": "يُفرض نظام الإحداثيات عند إنشاء طقم المعالم مباشرة حتى لو لم تكن هناك طوبولوجيا.",
                "D": "الإسقاط اللحظي خاص بعرض الخريطة فقط، أما التخزين داخل طقم المعالم فيمنع تماماً خلط النظم."
            }
        },
        "references": [{"title": "Feature dataset basics, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/feature-dataset-basics.htm", "kind": "official"}]
    },
    {
        "id": "DM-044", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Conceptual", "tools": ["Add Global IDs"],
        "question": {
            "en": "What is the key functional distinction between an ObjectID and a GlobalID field in a geodatabase?",
            "ar": "ما هو الفارق الوظيفي الجوهري بين حقل ObjectID وحقل GlobalID في قاعدة البيانات الجغرافية؟"
        },
        "options": [
            {"id": "A", "text": {"en": "ObjectID is a 36-character string; GlobalID is a sequential integer", "ar": "ObjectID نص مكون من 36 حرفاً، بينما GlobalID رقم صحيح تسلسلي"}},
            {"id": "B", "text": {"en": "ObjectID is unique only within a specific table and can change upon export; GlobalID is globally unique across databases and replication", "ar": "ObjectID فريد فقط داخل الجدول الواحد وقد يتغير عند التصدير، بينما GlobalID فريد عالمياً عبر قواعد البيانات والنسخ المتماثل"}},
            {"id": "C", "text": {"en": "ObjectID is user-editable; GlobalID is automatically locked by Windows", "ar": "ObjectID قابل للتعديل بواسطة المستخدم، بينما GlobalID مقفل تلقائياً بنظام Windows"}},
            {"id": "D", "text": {"en": "GlobalID is required for shapefiles; ObjectID is required for geodatabases", "ar": "GlobalID إلزامي لملفات shapefile، بينما ObjectID إلزامي لقواعد البيانات الجغرافية"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "An ObjectID is managed sequentially per table and may be re-indexed during export. A GlobalID is a 36-character globally unique identifier (GUID) preserved across database replication, offline synchronization, and relationship classes.",
            "ar": "حقل ObjectID رقم تسلسلي يدار لكل جدول بشكل مستقل وقد يعاد ترقيمه عند التصدير، بينما GlobalID معرف فريد عالمياً (GUID) يظل ثابتاً عبر المزامنة والنسخ المتماثل وفئات العلاقات."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "This inverts the types: ObjectID is a sequential integer, while GlobalID is a 36-character GUID string.",
                "C": "Neither field is user-editable; both are system-maintained by the geodatabase software.",
                "D": "Shapefiles do not support native GlobalID fields; both are geodatabase constructs (shapefiles use FID)."
            },
            "ar": {
                "A": "هذا يعكس الأنواع؛ فـ ObjectID رقم تسلسلي و GlobalID نص GUID من 36 رمزاً.",
                "C": "كلا الحقلين غير قابل للتعديل المباشر من المستخدم بل يدار بواسطة نظام قاعدة البيانات.",
                "D": "ملفات shapefile لا تدعم حقول GlobalID وتستخدم حقل FID."
            }
        },
        "references": [{"title": "ArcGIS field data types, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/arcgis-field-data-types.htm", "kind": "official"}]
    },
    {
        "id": "DM-045", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Workflow-based", "tools": ["Enable Attachments"],
        "question": {
            "en": "When Enable Attachments is executed on a feature class, which two items does ArcGIS Pro automatically create in the geodatabase?",
            "ar": "عند تنفيذ أداة تفعيل المرفقات (Enable Attachments) على فئة معالم، ما العنصران اللذان ينشئهما ArcGIS Pro تلقائياً في قاعدة البيانات؟"
        },
        "options": [
            {"id": "A", "text": {"en": "A BLOB field in the source table and a file folder on the local drive", "ar": "حقل BLOB في الجدول المصدر ومجلد ملفات على القرص المحلي"}},
            {"id": "B", "text": {"en": "An attachment table named [FeatureClass]_ATTACH and a composite relationship class linking the table to the features", "ar": "جدول مرفقات يسمى [FeatureClass]_ATTACH وفئة علاقات تركيبية تربط الجدول بالمعالم"}},
            {"id": "C", "text": {"en": "A Hyperlink field and a spatial index on the attachment directory", "ar": "حقل ارتباط تشعبي وفهرس مكاني على دليل المرفقات"}},
            {"id": "D", "text": {"en": "An XML metadata document and a raster catalog", "ar": "وثيقة بيانات وصفية XML وكتالوج راستر"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Enabling attachments creates an attachment table named '[FeatureClass]_ATTACH' containing the binary attachment data and a composite relationship class linking feature GlobalIDs to the attachment records.",
            "ar": "يؤدي تفعيل المرفقات إلى إنشاء جدول سمات مرفقات يحمل الاسم '[FeatureClass]_ATTACH' وفئة علاقات تركيبية تربط المعالم بملفات المرفقات عبر حقل GlobalID."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Attachments are stored in a dedicated geodatabase table, not directly in a BLOB field in the main feature class, and not in external OS folders.",
                "C": "ArcGIS Pro attachments do not use Hyperlink fields; they use binary storage in an attachment table.",
                "D": "Attachments have nothing to do with raster catalogs or XML metadata documents."
            },
            "ar": {
                "A": "تخزن المرفقات في جدول مخصص بقاعدة البيانات وليس كحقل مباشر في الطبقة أو مجلد خارجي.",
                "C": "لا تعتمد المرفقات على حقول الارتباط التشعبي بل على جدول تخزين ثنائي مخصص.",
                "D": "المرفقات لا علاقة لها بكتالوجات الراستر أو وثائق XML."
            }
        },
        "references": [{"title": "Enable Attachments (Data Management), ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/enable-attachments.htm", "kind": "official"}]
    },
    {
        "id": "DM-046", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Export XML Workspace Document"],
        "question": {
            "en": "Why would an administrator choose the 'Schema Only' option when running Export XML Workspace Document?",
            "ar": "لماذا يختار مسؤول قواعد البيانات خيار 'Schema Only' عند تشغيل أداة تصدير وثيقة مساحة العمل XML Workspace Document؟"
        },
        "options": [
            {"id": "A", "text": {"en": "To export only the spatial coordinates and exclude attribute tables", "ar": "لتصدير الإحداثيات المكانية فقط واستبعاد جداول السمات"}},
            {"id": "B", "text": {"en": "To replicate the structural definitions (tables, domains, subtypes, and rules) without copying any data rows", "ar": "لاستنساخ الهيكل التصميمي (الجداول والنطاقات والفئات والقواعد) دون نسخ أي صفوف بيانات"}},
            {"id": "C", "text": {"en": "To compress raster datasets into JPEG format", "ar": "لضغط مجموعات بيانات الراستر إلى صيغة JPEG"}},
            {"id": "D", "text": {"en": "To convert geodatabase topology into shapefiles", "ar": "لتحويل طوبولوجيا قاعدة البيانات إلى ملفات shapefile"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "The 'Schema Only' option exports the complete structural definition of the geodatabase—including tables, feature classes, domains, subtypes, relationship classes, and topology rules—creating an empty template without transferring data records.",
            "ar": "خيار 'Schema Only' يصدر الهيكل التعريفي الكامل لقاعدة البيانات بما في ذلك الجداول والنطاقات والفئات والعلاقات وقواعد الطوبولوجيا كقالب فارغ دون نقل أي سجلات بيانات."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Schema Only includes table structures, field definitions, and properties, but excludes all row records and coordinate data.",
                "C": "XML Workspace documents are structural XML files, not raster compression utilities.",
                "D": "XML Workspace documents preserve geodatabase schema; shapefiles do not support topology rules."
            },
            "ar": {
                "A": "خيار Schema Only يتضمن هياكل الجداول والحقول والخصائص ويستبعد السجلات والإحداثيات.",
                "C": "وثائق XML ملفات توصيف هيكلي وليست أدوات لضغط الراستر.",
                "D": "وثيقة XML تحافظ على بنية قاعدة البيانات، وملفات shapefile لا تدعم قواعد الطوبولوجيا."
            }
        },
        "references": [{"title": "Export XML Workspace Document, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/export-xml-workspace-document.htm", "kind": "official"}]
    },
    {
        "id": "DM-047", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Conceptual", "tools": ["Create Topology"],
        "question": {
            "en": "In a Geodatabase Topology, what does the 'Cluster Tolerance' parameter represent?",
            "ar": "في طوبولوجيا قاعدة البيانات الجغرافية، ما الذي يمثله معامل 'Cluster Tolerance' (تسامح التجميع)؟"
        },
        "options": [
            {"id": "A", "text": {"en": "The maximum number of errors permitted before validation fails", "ar": "الحد الأقصى لعدد الأخطاء المسموح بها قبل توقف عملية التحقق"}},
            {"id": "B", "text": {"en": "The distance within which all vertices and edges are considered geometrically coincident", "ar": "المسافة التي تعتبر القمم والحواف الواقعة ضمنها متطابقة هندسياً"}},
            {"id": "C", "text": {"en": "The maximum distance allowed between disconnected line dangles", "ar": "الحد الأقصى للمسافة المسموحة بين نهايات الخطوط المعلقة"}},
            {"id": "D", "text": {"en": "The buffer distance applied when exporting topology error layers", "ar": "مسافة الحرم المطبقة عند تصدير طبقات أخطاء الطوبولوجيا"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "The cluster tolerance is the distance within which coordinates (vertices and boundaries) are determined to be coincident during topology validation. Vertices falling closer than this tolerance snap together.",
            "ar": "تسامح التجميع هو المسافة التي تعتبر القمم والحدود الواقعة ضمنها متطابقة هندسياً أثناء التحقق الطوبولوجي، حيث تلتصق القمم ببعضها إذا كانت المسافة بينها أقل من هذه القيمة."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Validation processes all features regardless of the number of errors detected.",
                "C": "Cluster tolerance applies to all vertices across all participating layers, not just line endpoints or dangles.",
                "D": "Cluster tolerance is a geometric processing threshold, not an export buffer distance."
            },
            "ar": {
                "A": "عملية التحقق تفحص كافة المعالم بغض النظر عن عدد الأخطاء المكتشفة.",
                "C": "التسامح يطبق على كافة القمم في الطبقات المشاركة وليس على نهايات الخطوط فقط.",
                "D": "التسامح عتبة معالجة هندسية وليس مسافة حرم عند التصدير."
            }
        },
        "references": [{"title": "Geodatabase topology cluster tolerance, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/geodatabase-topology-basics.htm", "kind": "official"}]
    },
    {
        "id": "DM-048", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Tool-based", "tools": ["Add Rule To Topology"],
        "question": {
            "en": "Which topology rule should you apply to prevent land parcel polygons from having overlapping boundaries?",
            "ar": "أي قاعدة طوبولوجية يجب تطبيقها لمنع تداخل حدود مضلعات قطع الأراضي المساحية؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Must Not Have Gaps", "ar": "Must Not Have Gaps"}},
            {"id": "B", "text": {"en": "Must Not Overlap", "ar": "Must Not Overlap"}},
            {"id": "C", "text": {"en": "Must Be Covered By Feature Class Of", "ar": "Must Be Covered By Feature Class Of"}},
            {"id": "D", "text": {"en": "Contains One Point", "ar": "Contains One Point"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "The 'Must Not Overlap' polygon topology rule requires that interior areas of polygons in the same feature class do not overlap each other, flagging shared interior overlapping spaces as errors.",
            "ar": "تشترط قاعدة 'Must Not Overlap' للمضلعات عدم تداخل المساحات الداخلية للمضلعات في نفس فئة المعالم، وتميز أي مساحات تداخل مشتركة كأخطاء طوبولوجية."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Must Not Have Gaps checks for void spaces between adjacent polygons, not overlaps.",
                "C": "Must Be Covered By Feature Class Of validates that polygons are completely enclosed by a polygon in a second feature class.",
                "D": "Contains One Point checks that each polygon contains exactly one point from another layer."
            },
            "ar": {
                "A": "قاعدة Must Not Have Gaps تفحص الفراغات البينية بين المضلعات وليس التداخلات.",
                "C": "قاعدة Must Be Covered By Feature Class Of تتحقق من وقوع المضلعات بالكامل داخل مضلع من طبقة أخرى.",
                "D": "قاعدة Contains One Point تفحص احتواء كل مضلع على نقطة واحدة من طبقة أخرى."
            }
        },
        "references": [{"title": "Geodatabase topology rules for polygon features, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/geodatabase-topology-rules-for-polygon-features.htm", "kind": "official"}]
    },
    {
        "id": "DM-049", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Tool-based", "tools": ["Add Rule To Topology"],
        "question": {
            "en": "Which topology rule validates that road centerline polylines connect at endpoints and do not have unjoined overshoot or undershoot dangles?",
            "ar": "أي قاعدة طوبولوجية تتحقق من اتصال خطوط شبكة الطرق عند النهايات وعدم وجود نهايات معلقة (overshoots أو undershoots)؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Must Not Have Dangles", "ar": "Must Not Have Dangles"}},
            {"id": "B", "text": {"en": "Must Not Intersect", "ar": "Must Not Intersect"}},
            {"id": "C", "text": {"en": "Must Be Single Part", "ar": "Must Be Single Part"}},
            {"id": "D", "text": {"en": "Endpoint Must Be Covered By", "ar": "Endpoint Must Be Covered By"}}
        ],
        "correctAnswer": "A",
        "explanation": {
            "en": "The 'Must Not Have Dangles' line topology rule requires that a line feature must touch lines from the same feature class at both endpoints. Dangles at genuine dead-ends (cul-de-sacs) can be marked as exceptions.",
            "ar": "تتطلب قاعدة 'Must Not Have Dangles' للخطوط اتصال نهايات الخطوط بخطوط أخرى في نفس الطبقة، ويمكن تعليم النهايات الميتة الحقيقية كاستثناءات."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "B": "Must Not Intersect requires that lines do not cross or overlap each other.",
                "C": "Must Be Single Part requires that lines do not have multipart geometry.",
                "D": "Endpoint Must Be Covered By requires endpoints to be covered by points from another feature class."
            },
            "ar": {
                "B": "قاعدة Must Not Intersect تشترط عدم تقاطع الخطوط مع بعضها البعض.",
                "C": "قاعدة Must Be Single Part تشترط أن تكون الخطوط أحادية الجزء وليست متعددة.",
                "D": "قاعدة Endpoint Must Be Covered By تشترط تغطية نهايات الخطوط بنقاط من طبقة أخرى."
            }
        },
        "references": [{"title": "Geodatabase topology rules for polyline features, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/geodatabase-topology-rules-for-polyline-features.htm", "kind": "official"}]
    },
    {
        "id": "DM-050", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Advanced", "type": "Technical", "tools": ["Add Feature Class To Topology"],
        "question": {
            "en": "When configuring coordinate ranks (1 to 50) for feature classes participating in a topology, how does rank affect vertex movement during validation?",
            "ar": "عند تعيين رتب الإحداثيات (من 1 إلى 50) لفئات المعالم المشاركة في الطوبولوجيا، كيف تؤثر الرتبة على حركة القمم أثناء التحقق؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Rank 50 features never move; rank 1 features always move to snap to rank 50", "ar": "معالم الرتبة 50 لا تتحرك أبداً، ومعالم الرتبة 1 تتحرك دائماً للالتصاق بالرتبة 50"}},
            {"id": "B", "text": {"en": "Rank 1 is the highest accuracy; vertices of lower rank features snap to vertices of higher rank features within the cluster tolerance", "ar": "الرتبة 1 هي الأعلى دقة؛ وتتحرك قمم الطبقات ذات الرتب الأدنى لتلتصق بقمم الطبقات ذات الرتب الأعلى ضمن مسافة التسامح"}},
            {"id": "C", "text": {"en": "Rank has no effect on vertex position and only determines the order of error reporting", "ar": "لا تؤثر الرتبة على موقع القمم وإنما تحدد فقط ترتيب إظهار تقارير الأخطاء"}},
            {"id": "D", "text": {"en": "Features with equal rank are deleted automatically if they overlap", "ar": "تحذف المعالم ذات الرتب المتساوية تلقائياً إذا تداخلت"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Rank 1 denotes the highest accuracy level. During topology validation, lower-ranked features (e.g. Rank 2, 3) will have their vertices moved to match the positions of higher-ranked features (e.g. Rank 1) within the cluster tolerance.",
            "ar": "تمثل الرتبة 1 أعلى مستوى للدقة الهندسية. وأثناء التحقق الطوبولوجي تتحرك قمم الطبقات ذات الرتب الأدنى (مثل 2 و 3) لتلتصق بمواقع قمم الطبقات الأعلى دقة (مثل 1) ضمن مسافة التسامح."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "This inverts the ranking system: Rank 1 is the highest accuracy, not Rank 50.",
                "C": "Rank directly controls coordinate geometry movement during clustering.",
                "D": "Topology validation never deletes features automatically; it flags rule violations as errors."
            },
            "ar": {
                "A": "هذا يعكس النظام؛ فالرتبة 1 هي الأعلى دقة وليست الرتبة 50.",
                "C": "تتحكم الرتبة بشكل مباشر في حركة الإحداثيات والقمم أثناء التجميع.",
                "D": "التحقق الطوبولوجي لا يحذف المعالم تلقائياً بل يحدد الأخطاء فقط."
            }
        },
        "references": [{"title": "Topology coordinate ranks, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/geodatabase-topology-basics.htm", "kind": "official"}]
    }
]

# Let's add DM-051 to DM-080
more_dm = [
    {
        "id": "DM-051", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Tool-based", "tools": ["Validate Topology"],
        "question": {
            "en": "What is the result of choosing 'Mark as Exception' on a topology error in the Error Inspector?",
            "ar": "ما هي نتيجة اختيار 'Mark as Exception' (تعليم كاستثناء) على خطأ طوبولوجي في نافذة فحص الأخطاء (Error Inspector)؟"
        },
        "options": [
            {"id": "A", "text": {"en": "The feature is permanently deleted from the feature class", "ar": "يُحذف المعلم نهائياً من فئة المعالم"}},
            {"id": "B", "text": {"en": "The error remains stored in the topology but is ignored in subsequent validation cycles", "ar": "يظل الخطأ مخزناً في الطوبولوجيا ولكنه يتجاهل في جولات التحقق المستقبلية"}},
            {"id": "C", "text": {"en": "The topology rule is removed from the geodatabase schema", "ar": "تُحذف القاعدة الطوبولوجية من مخطط قاعدة البيانات"}},
            {"id": "D", "text": {"en": "The geometry is automatically split into singlepart components", "ar": "تُقسَم الهندسة تلقائياً إلى مكونات أحادية الجزء"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Marking an error as an exception acknowledges that the geometric condition violates a general topology rule but is legally or physically valid in that specific instance (e.g. cul-de-sacs for dangling lines). It will not be flagged again in future validation.",
            "ar": "تعليم الخطأ كاستثناء يعني الإقرار بأن الحالة الهندسية تخالف القاعدة العامة ولكنها صحيحة ومقبولة في هذه الحالة المحددة (مثل النهايات الميتة للطرق). ولن تظهر كخطأ في جولات الفحص اللاحقة."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Marking an exception does not delete any spatial feature.",
                "C": "The topology rule itself remains active for all other features in the layer.",
                "D": "Marking an exception modifies error status metadata, not geometry."
            },
            "ar": {
                "A": "تعليم الاستثناء لا يحذف أي معلم مكاني.",
                "C": "القاعدة الطوبولوجية تظل سارية على بقية معالم الطبقة.",
                "D": "الاستثناء يعدل حالة الخطأ في البيانات الوصفية ولا يغير الهندسة."
            }
        },
        "references": [{"title": "Manage topology errors, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/manage-topology-errors.htm", "kind": "official"}]
    },
    {
        "id": "DM-052", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Conceptual", "tools": ["Map Topology"],
        "question": {
            "en": "How does Map Topology differ fundamentally from Geodatabase Topology in ArcGIS Pro?",
            "ar": "كيف تختلف طوبولوجيا الخريطة (Map Topology) جوهرياً عن طوبولوجيا قاعدة البيانات (Geodatabase Topology) في ArcGIS Pro؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Map Topology creates permanent error datasets inside a Feature Dataset", "ar": "طوبولوجيا الخريطة تنشئ طبقات أخطاء دائمة داخل طقم المعالم"}},
            {"id": "B", "text": {"en": "Map Topology is an in-memory editing tool that allows editing shared edges across layers on the fly without database rules", "ar": "طوبولوجيا الخريطة أداة تحرير مؤقتة في الذاكرة تتيح تعديل الحواف المشتركة عبر الطبقات لحظياً دون قواعد في قاعدة البيانات"}},
            {"id": "C", "text": {"en": "Map Topology works only with CAD drawings and shapefiles", "ar": "طوبولوجيا الخريطة تعمل فقط مع ملفات CAD و shapefiles"}},
            {"id": "D", "text": {"en": "Map Topology requires an ArcGIS Pro Advanced license", "ar": "طوبولوجيا الخريطة تتطلب ترخيص ArcGIS Pro Advanced حصراً"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Map Topology is an on-the-fly editing capability that discovers coincident edges and nodes between visible layers in memory, enabling editors to reshape shared boundaries without creating topology objects in a geodatabase.",
            "ar": "طوبولوجيا الخريطة هي إمكانية تحرير لحظية في الذاكرة تكتشف الحواف والقمم المتطابقة بين الطبقات المعروضة، مما يسمح للمحررين بإعادة تشكيل الحدود المشتركة دون إنشاء كائنات طوبولوجيا في قاعدة البيانات."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Geodatabase Topology creates persistent error datasets, not Map Topology.",
                "C": "Map Topology works across any editable vector layers in the map including geodatabase feature classes.",
                "D": "Map Topology is available in ArcGIS Pro Basic, Standard, and Advanced."
            },
            "ar": {
                "A": "طوبولوجيا قاعدة البيانات هي التي تنشئ طبقات أخطاء دائمة.",
                "C": "طوبولوجيا الخريطة تعمل مع مختلف الطبقات المتجهة القابلة للتحرير بما فيها قواعد البيانات.",
                "D": "طوبولوجيا الخريطة متاحة في كافة مستويات تراخيص ArcGIS Pro."
            }
        },
        "references": [{"title": "Map topology, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/introduction-to-map-topology.htm", "kind": "official"}]
    },
    {
        "id": "DM-053", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Conceptual", "tools": ["Add Attribute Rule"],
        "question": {
            "en": "Which Attribute Rule type completely prevents an editor from committing an invalid attribute or geometry change by rolling back the transaction?",
            "ar": "أي نوع من قواعد السمات (Attribute Rules) يمنع المحرر تماماً من حفظ تعديل غير صالح للسمات أو الهندسة من خلال التراجع عن المعاملة (Rollback)؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Calculation Rule (Immediate)", "ar": "قاعدة حساب (Immediate)"}},
            {"id": "B", "text": {"en": "Constraint Rule", "ar": "قاعدة تقييد (Constraint Rule)"}},
            {"id": "C", "text": {"en": "Validation Rule", "ar": "قاعدة تحقق (Validation Rule)"}},
            {"id": "D", "text": {"en": "Calculation Rule (Batch)", "ar": "قاعدة حساب مجمعة (Batch)"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Constraint rules enforce data integrity directly during the edit transaction. If the Arcade script returns false, the edit is blocked, the transaction rolls back, and a user-configured error message and code are displayed.",
            "ar": "تفرض قواعد التقييد (Constraint rules) نزاهة البيانات مباشرة أثناء عملية التحرير، فإذا أعادت دالة Arcade القيمة false، يُلغى التعديل ويتم التراجع عن الحفظ مع إظهار رسالة وكود خطأ مخصص."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Calculation rules compute and populate values into fields; they do not block edits.",
                "C": "Validation rules evaluate features asynchronously in batch via Error Inspector without blocking the live edit.",
                "D": "Batch calculation rules populate values on-demand across existing datasets."
            },
            "ar": {
                "A": "قواعد الحساب تحسب وتملأ قيم الحقول ولا تمنع التحرير.",
                "C": "قواعد التحقق تفحص المعالم بشكل غير متزامن عبر فاحص الأخطاء دون إيقاف الحفظ اللحظي.",
                "D": "قواعد الحساب المجمعة تنفذ عند الطلب لملء البيانات السابقة."
            }
        },
        "references": [{"title": "Attribute rule types, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/an-overview-of-attribute-rules.htm", "kind": "official"}]
    },
    {
        "id": "DM-054",
        "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Add Attribute Rule"],
        "question": {
            "en": "In ArcGIS Pro, what scripting language is used to write expressions for Attribute Rules?",
            "ar": "في ArcGIS Pro، ما هي لغة البرمجة النصية المستخدمة لكتابة تعبيرات قواعد السمات (Attribute Rules)؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Python 3", "ar": "Python 3"}},
            {"id": "B", "text": {"en": "Arcade", "ar": "Arcade"}},
            {"id": "C", "text": {"en": "VBScript", "ar": "VBScript"}},
            {"id": "D", "text": {"en": "SQL (Transact-SQL)", "ar": "SQL (Transact-SQL)"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Arcade is the mandatory language for Attribute Rules across ArcGIS Pro and ArcGIS Enterprise. Its lightweight, secure, and cross-platform profile allows expressions to execute on desktop, server, and web clients consistently.",
            "ar": "تعد لغة Arcade اللغة الإلزامية لكتابة قواعد السمات عبر ArcGIS Pro و ArcGIS Enterprise، حيث تضمن بنيتها الخفيفة والآمنة التنفيذ الموحد عبر سطح المكتب والخادم وتطبيقات الويب."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Python is used for geoprocessing scripting and field calculation, but Attribute Rules do not support Python.",
                "C": "VBScript is deprecated and obsolete in ArcGIS Pro.",
                "D": "SQL is used for queries and definition queries, not for authoring attribute rules."
            },
            "ar": {
                "A": "تستخدم بايثون في سكريبتات المعالجة وحساب الحقول، ولكن قواعد السمات لا تدعم بايثون.",
                "C": "لغة VBScript مهجورة وغير مدعومة في ArcGIS Pro.",
                "D": "تستخدم SQL في الاستعلامات وليس في كتابة قواعد السمات."
            }
        },
        "references": [{"title": "Arcade profile for Attribute Rules, ArcGIS Developers", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/an-overview-of-attribute-rules.htm", "kind": "official"}]
    },
    {
        "id": "DM-055", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Advanced", "type": "Technical", "tools": ["Add Attribute Rule"],
        "question": {
            "en": "In an Arcade expression for an Attribute Rule, which global profile variable accesses the feature currently being created or modified?",
            "ar": "في تعبير Arcade لقاعدة سمات، أي متغير عام (Profile variable) يتيح الوصول إلى المعلم الجاري إنشاؤه أو تعديله حالياً؟"
        },
        "options": [
            {"id": "A", "text": {"en": "$feature", "ar": "$feature"}},
            {"id": "B", "text": {"en": "$layer", "ar": "$layer"}},
            {"id": "C", "text": {"en": "$geometry", "ar": "$geometry"}},
            {"id": "D", "text": {"en": "$target", "ar": "$target"}}
        ],
        "correctAnswer": "A",
        "explanation": {
            "en": "The $feature global variable represents the current feature undergoing evaluation. Editors access attribute fields using $feature.FieldName and geometry via Geometry($feature).",
            "ar": "يمثل المتغير العام $feature المعلم الحالي الخاضع للتقييم، ويصل المحررون إلى سمات الحقول عبر $feature.FieldName وإلى الهندسة عبر Geometry($feature)."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "B": "$layer is used in visualization and pop-up profiles, not as the primary feature accessor in attribute rules.",
                "C": "$geometry is not a global profile variable; geometry is accessed via Geometry($feature).",
                "D": "$target is not an Arcade global variable."
            },
            "ar": {
                "B": "المتغير $layer يستخدم في ملفات تعريف النوافذ المنبثقة وليس كمعلم أساسي في قواعد السمات.",
                "C": "لا يوجد متغير عام باسم $geometry بل يُحصل على الهندسة عبر Geometry($feature).",
                "D": "المتغير $target غير موجود في لغة Arcade."
            }
        },
        "references": [{"title": "Arcade profile for Attribute Rules, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/an-overview-of-attribute-rules.htm", "kind": "official"}]
    },
    {
        "id": "DM-056", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Workflow-based", "tools": ["Contingent Values"],
        "question": {
            "en": "What must be created on a feature class before any Contingent Values can be defined?",
            "ar": "ما الذي يجب إنشاؤه على فئة المعالم قبل التمكن من تعريف أي قيم احتمالية مشروطة (Contingent Values)؟"
        },
        "options": [
            {"id": "A", "text": {"en": "A composite relationship class", "ar": "فئة علاقات تركيبية"}},
            {"id": "B", "text": {"en": "A Field Group", "ar": "مجموعة حقول (Field Group)"}},
            {"id": "C", "text": {"en": "A geometric network", "ar": "شبكة هندسية"}},
            {"id": "D", "text": {"en": "A Spatial Index", "ar": "فهرس مكاني"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Before creating contingent values, you must create a Field Group that bundles the participating fields whose values will depend on each other.",
            "ar": "قبل إنشاء القيم الاحتمالية المشروطة، يجب أولاً إنشاء مجموعة حقول (Field Group) تجمع الحقول المشاركة التي ستعتمد قيمها على بعضها البعض."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Relationship classes link separate tables and are not required for contingent values.",
                "C": "Geometric networks are legacy technology replaced by Utility Networks and have no relation to contingent values.",
                "D": "Spatial indexes index spatial geometry coordinates, not attribute dropdown contingencies."
            },
            "ar": {
                "A": "فئات العلاقات تربط جداول منفصلة وليست شرطاً للقيم المشروطة.",
                "C": "الشبكات الهندسية تقنية قديمة استبدلت بشبكات المرافق ولا علاقة لها بالقيم المشروطة.",
                "D": "الفهارس المكانية تفهرس الإحداثيات وليس شاشات الاختيار السماتية."
            }
        },
        "references": [{"title": "Create and manage contingent values, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/create-and-manage-contingent-values.htm", "kind": "official"}]
    },
    {
        "id": "DM-057", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Conceptual", "tools": ["Contingent Values"],
        "question": {
            "en": "How do Contingent Values enhance standard Attribute Domains?",
            "ar": "كيف تطور ميزة القيم المشروطة (Contingent Values) قدرات نطاقات السمات (Attribute Domains) القياسية؟"
        },
        "options": [
            {"id": "A", "text": {"en": "They eliminate the need to define field data types in the table", "ar": "تلغي الحاجة لتحديد أنواع بيانات الحقول في الجدول"}},
            {"id": "B", "text": {"en": "They restrict the choices in one field based on the value previously chosen in another field", "ar": "تقيد الخيارات المتاحة في حقل معين بناءً على القيمة المختارة سابقاً في حقل آخر"}},
            {"id": "C", "text": {"en": "They convert text attributes into binary BLOB objects automatically", "ar": "تحول السمات النصية إلى كائنات BLOB ثنائية تلقائياً"}},
            {"id": "D", "text": {"en": "They bypass geodatabase schema locks during multi-user editing", "ar": "تتجاوز أقفال مخطط قاعدة البيانات أثناء التحرير المتعدد"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Contingent values make domain values dependent on one another across fields (e.g. selecting Tree Genus 'Quercus' restricts Species to Oak species only, rather than showing all tree species in the database).",
            "ar": "تجعل القيم المشروطة خيارات النطاقات معتمدة على بعضها عبر الحقول (مثل اختيار جنس الشجرة 'Quercus' يقصر خيارات حقل النوع على أشجار البلوط فقط بدلاً من عرض كافة أنواع الأشجار في القاعدة)."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Field data types are fundamental table schema and are always required.",
                "C": "Contingent values apply to standard text, numeric, and coded value fields, not BLOB objects.",
                "D": "Contingent values are data integrity rules and do not affect schema locking."
            },
            "ar": {
                "A": "أنواع بيانات الحقول جزء أساسي من بنية الجدول ولا يمكن الاستغناء عنها.",
                "C": "تطبق القيم المشروطة على الحقول النصية والرقمية العادية وليس كائنات BLOB.",
                "D": "القيم المشروطة قواعد لنزاهة البيانات ولا علاقة لها بأقفال المخطط."
            }
        },
        "references": [{"title": "Introduction to contingent values, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/overview/contingent-values.htm", "kind": "official"}]
    },
    {
        "id": "DM-058", "kind": "mcq", "domain": "Data Management",
        "objective": "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes",
        "difficulty": "Beginner", "type": "Tool-based", "tools": ["Traverse"],
        "question": {
            "en": "Which ArcGIS Pro editing tool is purpose-built to enter boundary lines from legal survey descriptions using directions, distances, and curve parameters?",
            "ar": "أي أداة تحرير في ArcGIS Pro مخصصة لرسم خطوط الحدود من واقع سجلات المساحة القانونية باستخدام الاتجاهات والمسافات ومعاملات المنحنيات؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Reshape", "ar": "Reshape"}},
            {"id": "B", "text": {"en": "Traverse", "ar": "Traverse"}},
            {"id": "C", "text": {"en": "Generalize", "ar": "Generalize"}},
            {"id": "D", "text": {"en": "Buffer", "ar": "Buffer"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "The Traverse tool in the Create Features pane allows COGO (Coordinate Geometry) boundary input using survey calls: bearing/direction, distance, radius, chord length, and deflection angle.",
            "ar": "أداة المسار المساحي (Traverse) في لوحة إنشاء المعالم مخصصة لإدخال حدود COGO من قياسات المساحة القانونية: الانحراف، المسافة، نصف القطر، طول الوتر، وزاوية الانحراف."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Reshape allows redrawing part of an existing feature geometry interactively.",
                "C": "Generalize simplifies feature geometry by reducing vertex count.",
                "D": "Buffer is a geoprocessing analysis tool that creates proximity offsets."
            },
            "ar": {
                "A": "أداة Reshape تعيد رسم جزء من هندسة معلَم قائم تفاعلياً.",
                "C": "أداة Generalize تبسط الهندسة بتقليل عدد القمم.",
                "D": "أداة Buffer أداة تحليل مكاني لإنشاء نطاقات حرم حول المعالم."
            }
        },
        "references": [{"title": "Create a traverse, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/create-a-traverse.htm", "kind": "official"}]
    },
    {
        "id": "DM-059", "kind": "mcq", "domain": "Data Management",
        "objective": "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes",
        "difficulty": "Intermediate", "type": "Tool-based", "tools": ["Align Edge"],
        "question": {
            "en": "You need to adjust an entire parcel boundary to match a newly surveyed road centerline without creating sliver overlaps or gaps. Which editing tool should you use?",
            "ar": "تحتاج إلى تعديل حد قطعة أرض بالكامل ليتطابق مع خط مسار طريق جرى مسحه حديثاً دون ترك فجوات أو تداخلات شريطية. أي أداة تحرير يجب استخدامها؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Align Edge", "ar": "Align Edge"}},
            {"id": "B", "text": {"en": "Smooth", "ar": "Smooth"}},
            {"id": "C", "text": {"en": "Buffer", "ar": "Buffer"}},
            {"id": "D", "text": {"en": "Erase", "ar": "Erase"}}
        ],
        "correctAnswer": "A",
        "explanation": {
            "en": "The Align Edge tool snaps and shapes an entire edge segment of a polygon or polyline to match an adjacent reference feature boundary, closing slivers and eliminating gaps.",
            "ar": "تقوم أداة Align Edge بمحاذاة والتقاط حافة بالكامل لمضلع أو خط لتتطابق تماماً مع حد المعلم المرجعي المجاور، مما يغلق الفراغات ويزيل التداخلات الشريطية."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "B": "Smooth rounds corners using Bezier or polynomial curves and does not snap to reference lines.",
                "C": "Buffer creates distance zones, not edge alignments.",
                "D": "Erase removes overlapping areas using an overlay operation."
            },
            "ar": {
                "B": "أداة Smooth تنعم الزوايا بمنحنيات ولا تلتقط بالخطوط المرجعية.",
                "C": "أداة Buffer تنشئ مناطق حرم بمسافة معينة ولا تحاذي الحواف.",
                "D": "أداة Erase تحذف الأجزاء المتداخلة عبر عملية تراكب."
            }
        },
        "references": [{"title": "Align an edge, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/align-an-edge.htm", "kind": "official"}]
    },
    {
        "id": "DM-060", "kind": "mcq", "domain": "Data Management",
        "objective": "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes",
        "difficulty": "Intermediate", "type": "Workflow-based", "tools": ["Construct Polygons"],
        "question": {
            "en": "What is the primary function of the 'Construct Polygons' tool in the ArcGIS Pro Modify Features pane?",
            "ar": "ما هي الوظيفة الأساسية لأداة 'Construct Polygons' في لوحة تعديل المعالم (Modify Features) في ArcGIS Pro؟"
        },
        "options": [
            {"id": "A", "text": {"en": "It converts 3D multipatches into flat 2D raster cells", "ar": "تحول مجسمات 3D multipatches إلى خلايا راستر ثنائية الأبعاد"}},
            {"id": "B", "text": {"en": "It creates new polygon features from closed boundary areas formed by intersecting polyline features", "ar": "تنشئ معالم مضلعات جديدة من المساحات المغلقة الناتجة عن تقاطع معالم الخطوط"}},
            {"id": "C", "text": {"en": "It merges attribute domains from two geodatabases", "ar": "تدمج نطاقات السمات من قاعدتي بيانات"}},
            {"id": "D", "text": {"en": "It dissolves adjacent polygons sharing identical attribute values", "ar": "تدمج وتذوب المضلعات المتجاورة المشتركة في نفس القيم السماتية"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Construct Polygons generates new polygon features in a target polygon layer using the enclosed boundary shapes defined by selected intersecting polyline features.",
            "ar": "تقوم أداة Construct Polygons بإنشاء معالم مضلعات جديدة في طبقة الهدف بالاعتماد على الحدود المغلقة الناتجة عن تقاطع معالم الخطوط المحددة."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Raster conversion is handled by conversion geoprocessing tools like Multipatch to Raster.",
                "C": "Domain management is performed in the Domains view, not Construct Polygons.",
                "D": "Dissolve is the geoprocessing tool for merging polygons with matching attributes."
            },
            "ar": {
                "A": "التحويل إلى راستر يتم بأدوات التحويل مثل Multipatch to Raster.",
                "C": "إدارة النطاقات تتم في نافذة Domains وليس بأداة إنشاء المضلعات.",
                "D": "أداة Dissolve هي المسؤولة عن دمج المضلعات ذات السمات المتطابقة."
            }
        },
        "references": [{"title": "Construct polygons from lines, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/construct-polygons-from-features.htm", "kind": "official"}]
    }
]

print(f"DM 40-60 ready ({len(dm_questions_to_add)} questions).")
