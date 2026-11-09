# -*- coding: utf-8 -*-
"""
Complete Data Management MCQs (DM-040 through DM-080)
"""
import json
import os
import sys

# Import DM-040 to DM-060 from generate_dm_part1
sys.path.append(os.path.dirname(__file__))
from generate_dm_part1 import dm_questions_to_add as dm_40_60

dm_61_80 = [
    {
        "id": "DM-061", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Add Global IDs"],
        "question": {
            "en": "Why is adding a GlobalID field required before enabling Branch Versioning or two-way Geodatabase Replication?",
            "ar": "لماذا يُعد إضافة حقل GlobalID متطلباً إلزامياً قبل تفعيل التفريع النسخي (Branch Versioning) أو النسخ المتماثل المتبادل للبيانات الجغرافية؟"
        },
        "options": [
            {"id": "A", "text": {"en": "To accelerate spatial query performance within local map extents", "ar": "لتسريع أداء الاستعلامات المكانية ضمن نطاق الخريطة المحلي"}},
            {"id": "B", "text": {"en": "To maintain globally unique feature identification across multiple databases and disconnected replicas", "ar": "للحفاظ على معرف فريد عالمياً لكل معلم عبر مختلف قواعد البيانات والنسخ غير المتصلة"}},
            {"id": "C", "text": {"en": "To enforce sequential numbering starting from 1 for newly inserted rows", "ar": "لفرض ترقيم تسلسلي يبدأ من الرقم 1 للصفوف الجديدة"}},
            {"id": "D", "text": {"en": "To store the username and timestamp of the editor who created each feature", "ar": "لتخزين اسم المستخدم والوقت والتاريخ للمحرر الذي أنشأ كل معلم"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "OBJECTID is only unique within a single table in a single geodatabase. GlobalID uses a 36-character globally unique identifier (UUID) that guarantees uniqueness across all databases, which is mandatory for branch versioning, replication, and offline sync.",
            "ar": "معرف OBJECTID فريد فقط داخل الجدول الواحد في قاعدة البيانات الواحدة. أما GlobalID فيستخدم معرف UUID مكوناً من 36 حرفاً فريداً على مستوى العالم، وهو متطلب إلزامي للتفريع النسخي والمزامنة والنسخ المتماثل."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Spatial indexation (not GlobalID) is responsible for optimizing spatial queries.",
                "C": "OBJECTID provides sequential integer IDs, whereas GlobalID values are non-sequential 128-bit hexadecimal strings.",
                "D": "Editor Tracking fields (created_user, created_date) store editor identity and timestamps, not GlobalID."
            },
            "ar": {
                "A": "الفهرس المكاني هو المسؤول عن تسريع الاستعلامات المكانية وليس GlobalID.",
                "C": "حقل OBJECTID هو الذي يقدم أرقاماً تسلسلية بينما GlobalID يولد سلاسل نصية سداسية عشرية غير تسلسلية.",
                "D": "حقول تتبع التحرير (Editor Tracking) هي المسؤولة عن تسجيل المستخدم والتاريخ وليس GlobalID."
            }
        },
        "references": [{"title": "Global IDs, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-file-gdb/global-ids.htm", "kind": "official"}]
    },
    {
        "id": "DM-062", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Conceptual", "tools": ["Create Relationship Class"],
        "question": {
            "en": "What happens when an origin feature is deleted in a Composite Relationship Class?",
            "ar": "ما الذي يحدث عند حذف معلم المصدر (Origin) في فئة علاقات مركبة (Composite Relationship Class)؟"
        },
        "options": [
            {"id": "A", "text": {"en": "The destination records are preserved and their foreign keys are set to NULL", "ar": "يتم الحفاظ على سجلات الهدف وتعيين المفتاح الأجنبي لها كقيمة NULL"}},
            {"id": "B", "text": {"en": "The related destination records are automatically deleted in a cascade deletion", "ar": "تُحذف سجلات الهدف المرتبطة تلقائياً في عملية حذف تسلسلي (Cascade Delete)"}},
            {"id": "C", "text": {"en": "The deletion is cancelled and an error message is thrown", "ar": "يتم إلغاء عملية الحذف وظهور رسالة خطأ"}},
            {"id": "D", "text": {"en": "The relationship class is permanently converted into a Simple relationship class", "ar": "تتحول فئة العلاقة بشكل دائم إلى فئة علاقة بسيطة (Simple)"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "In a Composite Relationship Class, the lifetime of the destination object depends entirely on the lifetime of the origin object. Deleting the origin feature automatically cascade-deletes all associated destination records.",
            "ar": "في فئات العلاقات المركبة (Composite)، ترتبط دورة حياة كائن الهدف بوجود كائن المصدر تماماً؛ لذا يؤدي حذف معلم المصدر إلى حذف تسلسلي (Cascade Delete) لجميع السجلات المرتبطة به في الهدف."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Preserving destination records with foreign key unlinking is the behavior of a Simple relationship class, not Composite.",
                "C": "ArcGIS Pro does not block deletion in composite relationships; it cascades the delete automatically.",
                "D": "Relationship class type (Simple vs Composite) cannot dynamically change during editing."
            },
            "ar": {
                "A": "الحفاظ على سجلات الهدف وفك الارتباط هو سلوك العلاقة البسيطة (Simple) وليس المركبة.",
                "C": "لا يمنع ArcGIS Pro عملية الحذف، بل ينفذ الحذف التتابعي للسجلات المرتبطة.",
                "D": "نوع فئة العلاقة ثابت ولا يتحول تلقائياً أثناء التحرير."
            }
        },
        "references": [{"title": "Relationship class properties, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-file-gdb/relationship-class-properties.htm", "kind": "official"}]
    },
    {
        "id": "DM-063", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Create Relationship Class"],
        "question": {
            "en": "When establishing a Many-to-Many (M:N) relationship class, where are the relationship pairs stored in the geodatabase?",
            "ar": "عند إنشاء فئة علاقة من نوع متعدد إلى متعدد (M:N)، أين يتم تخزين أزواج العلاقات في قاعدة البيانات الجغرافية؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Directly inside an array field in the origin feature class", "ar": "مباشرة داخل حقل مصفوفة في فئة معالم المصدر"}},
            {"id": "B", "text": {"en": "In an automatically created intermediate bridge table", "ar": "في جدول وسيط رابط (Bridge Table) يُنشأ تلقائياً"}},
            {"id": "C", "text": {"en": "In the destination table's GlobalID field", "ar": "في حقل GlobalID لجدول الهدف"}},
            {"id": "D", "text": {"en": "Inside the project metadata file (.aprx)", "ar": "داخل ملف البيانات الوصفية للمشروع (.aprx)"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Many-to-Many relationships cannot store foreign keys directly in either the origin or destination tables. ArcGIS Pro automatically creates an intermediate bridge table in the geodatabase containing origin foreign key and destination foreign key pairs.",
            "ar": "لا يمكن لعلاقات متعدد إلى متعدد تخزين المفاتيح الأجنبية مباشرة في جدول المصدر أو الهدف، لذلك ينشئ ArcGIS Pro تلقائياً جدولاً وسيطاً (Bridge Table) يحتوي على أزواج المفاتيح الأجنبية."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Standard geodatabase tables do not support array fields for relational linkages.",
                "C": "The destination GlobalID cannot hold multiple foreign keys for an M:N cardinality.",
                "D": "Relationship classes are geodatabase objects stored inside the .gdb, completely independent of the .aprx project file."
            },
            "ar": {
                "A": "جداول الجيوداتابيس القياسية لا تدعم حقول المصفوفات لتخزين المفاتيح.",
                "C": "حقل GlobalID للهدف لا يستوعب قيماً متعددة لعلاقات M:N.",
                "D": "فئات العلاقات تُخزن كعناصر جيوداتابيس داخل .gdb وليست في ملف المشروع .aprx."
            }
        },
        "references": [{"title": "Create a relationship class, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-file-gdb/create-a-relationship-class.htm", "kind": "official"}]
    },
    {
        "id": "DM-064", "kind": "mcq", "domain": "Data Management",
        "objective": "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes",
        "difficulty": "Intermediate", "type": "Tool-based", "tools": ["Traverse"],
        "question": {
            "en": "Which ArcGIS Pro editing tool allows entering survey boundary descriptions using bearing, distance, and curve parameters directly from legal deeds?",
            "ar": "أي أداة تحرير في ArcGIS Pro تتيح إدخال أوصاف حدود المسح العقاري باستخدام زوايا الانحراف والمسافات ومعاملات المنحنيات مباشرة من الصكوك القانونية؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Reshape", "ar": "Reshape (إعادة التشكيل)"}},
            {"id": "B", "text": {"en": "Traverse", "ar": "Traverse (المضلع المساحي)"}},
            {"id": "C", "text": {"en": "Generalize", "ar": "Generalize (التعميم)"}},
            {"id": "D", "text": {"en": "Align Edge", "ar": "Align Edge (محاذاة الحافة)"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "The Traverse tool in the Modify Features pane creates continuous parcel boundaries or centerlines by entering courses consisting of directions, distances, radii, and chord lengths directly from survey records.",
            "ar": "تتيح أداة Traverse في نافذة Modify Features إنشاء حدود الأراضي أو خطوط المركز عن طريق إدخال أضلاع المسار (الاتجاه، المسافة، نصف القطر، طول الوتر) مباشرة من سجلات المسح العقاري."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Reshape replaces a portion of an existing feature's geometry using a sketched line.",
                "C": "Generalize simplifies feature geometry by removing redundant vertices within a specified tolerance.",
                "D": "Align Edge matches an edge to a coincident edge in another layer within a search tolerance."
            },
            "ar": {
                "A": "أداة Reshape تستبدل جزءاً من هندسة المعلم القائم بخط مرسوم جديد.",
                "C": "أداة Generalize تبسط الخطوط والمضلعات بإزالة نقاط الرؤوس الزائدة.",
                "D": "أداة Align Edge تطابق حافة معلم مع حافة أخرى في طبقة ثانية ضمن مسافة تسامح."
            }
        },
        "references": [{"title": "Traverse, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/create-traverse-features.htm", "kind": "official"}]
    },
    {
        "id": "DM-065", "kind": "mcq", "domain": "Data Management",
        "objective": "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes",
        "difficulty": "Intermediate", "type": "Tool-based", "tools": ["Enable COGO"],
        "question": {
            "en": "What fields does the Enable COGO tool add to a line feature class to store coordinate geometry measurements?",
            "ar": "ما هي الحقول التي تضيفها أداة Enable COGO إلى فئة معالم خطية لتخزين قياسات الهندسة الإحداثية؟"
        },
        "options": [
            {"id": "A", "text": {"en": "SHAPE_Length, Area, Perimeter, and Centroid_X", "ar": "SHAPE_Length و Area و Perimeter و Centroid_X"}},
            {"id": "B", "text": {"en": "Direction, Distance, Radius, Arclength, Radius2, and Tangent", "ar": "Direction و Distance و Radius و Arclength و Radius2 و Tangent"}},
            {"id": "C", "text": {"en": "Elevation, Slope, Aspect, and Hillshade", "ar": "Elevation و Slope و Aspect و Hillshade"}},
            {"id": "D", "text": {"en": "Start_Node, End_Node, Left_Poly, and Right_Poly", "ar": "Start_Node و End_Node و Left_Poly و Right_Poly"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "The Enable COGO tool adds standard COGO attribute fields (Direction, Distance, Radius, Arclength, Radius2, Tangent) to line layers, enabling survey dimension capture and COGO labeling.",
            "ar": "تضيف أداة Enable COGO حقول السمات القياسية للهندسة الإحداثية (الاتجاه، المسافة، نصف القطر، طول القوس، نصف القطر الثاني، والمماس) للطبقات الخطية لتمكين تسجيل أبعاد المسح."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Shape_Length is automatically managed by the geodatabase; Area and Perimeter do not apply to lines.",
                "C": "Elevation and slope are surface terrain parameters, not COGO dimensions.",
                "D": "Node and polygon topology fields belong to coverage datasets, not ArcGIS Pro COGO lines."
            },
            "ar": {
                "A": "Shape_Length يُدار تلقائياً، وحقول المساحة والمحيط لا تنطبق على الخطوط.",
                "C": "الارتفاع والانحدار من خصائص التضاريس والأسطح وليس قياسات COGO.",
                "D": "حقول العقد والمضلعات تنتمي لتراكيب التغطيات القديمة (Coverages) وليست لخطوط COGO."
            }
        },
        "references": [{"title": "Enable COGO, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/enable-cogo.htm", "kind": "official"}]
    },
    {
        "id": "DM-066", "kind": "mcq", "domain": "Data Management",
        "objective": "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes",
        "difficulty": "Intermediate", "type": "Tool-based", "tools": ["Divide"],
        "question": {
            "en": "An analyst needs to divide a 10-acre parcel polygon into two lots such that one lot is exactly 4.0 acres. Which method in the Divide tool should be chosen?",
            "ar": "يحتاج محلل إلى تقسيم مضلع قطعة أرض مساحتها 10 أفدنة إلى قطعتين بحيث تكون إحداهما بمساحة 4.0 أفدنة بالضبط. أي خيار في أداة Divide يجب اختياره؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Equal Width", "ar": "العرض المتساوي (Equal Width)"}},
            {"id": "B", "text": {"en": "Proportional Area", "ar": "المساحة التناسبية (Proportional Area)"}},
            {"id": "C", "text": {"en": "Specified Area", "ar": "المساحة المحددة (Specified Area)"}},
            {"id": "D", "text": {"en": "Buffer Distance", "ar": "مسافة الحرم (Buffer Distance)"}}
        ],
        "correctAnswer": "C",
        "explanation": {
            "en": "The Divide tool's Specified Area method allows dividing a polygon by creating a new part with an exact specified geographic area measurement (e.g., 4.0 acres), splitting along a user-specified directional angle.",
            "ar": "يتيح خيار Specified Area في أداة Divide تقسيم المضلع بإنشاء جزء جديد بمساحة رقمية محددة بدقة (مثل 4.0 أفدنة) بطول زاوية اتجاه يحددها المستخدم."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Equal Width divides a polygon into strips of equal linear width, not exact area values.",
                "B": "Proportional Area divides a polygon into parts based on percentage ratios (e.g., 40% and 60%), not absolute square units.",
                "D": "Buffer is a proximity analysis tool, not an editing polygon divide method."
            },
            "ar": {
                "A": "خيار Equal Width يقسم المضلع إلى شرائح متساوية العرض الخطي وليس بمساحة رقمية محددة.",
                "B": "خيار Proportional Area يقسم بناءً على نسب مئوية وليس وحدات مساحة مطلقة.",
                "D": "أداة النطاق Buffer هي أداة تحليل مكاني وليست خيار تقسيم في التحرير."
            }
        },
        "references": [{"title": "Divide a polygon, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/divide-a-polygon.htm", "kind": "official"}]
    },
    {
        "id": "DM-067", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Check Geometry", "Repair Geometry"],
        "question": {
            "en": "What is the key functional difference between Check Geometry and Repair Geometry?",
            "ar": "ما هو الفرق الوظيفي الجوهري بين أداتي Check Geometry و Repair Geometry؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Check Geometry writes invalid geometries to a report table without modifying features; Repair Geometry fixes geometries in-place", "ar": "أداة Check Geometry تُخرج تقريراً بالأخطاء الهندسية في جدول دون تعديل المعالم؛ بينما Repair Geometry تصلح المعالم مباشرة في نفس الطبقة"}},
            {"id": "B", "text": {"en": "Check Geometry only works on shapefiles; Repair Geometry only works on enterprise geodatabases", "ar": "أداة Check Geometry تعمل على ملفات shapefile فقط؛ بينما Repair Geometry تعمل على قواعد البيانات المؤسسية فقط"}},
            {"id": "C", "text": {"en": "Check Geometry repairs errors automatically while Repair Geometry creates a new copy of the layer", "ar": "أداة Check Geometry تصلح الأخطاء تلقائياً بينما Repair Geometry تنشئ نسخة جديدة من الطبقة"}},
            {"id": "D", "text": {"en": "Both tools produce identical new output feature classes in the scratch geodatabase", "ar": "تنتج كلتا الأداتين فئات معالم جديدة متطابقة في قاعدة البيانات المؤقتة"}},
        ],
        "correctAnswer": "A",
        "explanation": {
            "en": "Check Geometry generates a standalone table listing geometric anomalies (self-intersections, null geometry, unclosed rings) without altering data. Repair Geometry modifies the input feature class in-place, removing invalid vertices or fixing exterior ring orientations.",
            "ar": "تنشئ أداة Check Geometry جدولاً منفصلاً يسرد المشكلات الهندسية (كالتقاطعات الذاتية والحلقات غير المغلقة) دون المساس بالبيانات؛ بينما أداة Repair Geometry تعدل بيانات الإدخال مباشرة في مكانها لإصلاح الخلل."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "B": "Both tools work on shapefiles, file geodatabases, and enterprise geodatabases.",
                "C": "This statement reverses the functions of the two tools.",
                "D": "Neither tool creates a new feature class; Check Geometry creates a table and Repair Geometry updates in-place."
            },
            "ar": {
                "B": "تعمل كلتا الأداتين على ملفات shapefile وقواعد البيانات الملفية والمؤسسية على حد سواء.",
                "C": "هذه العبارة تعكس وظيفتي الأداتين تماماً.",
                "D": "لا تنشئ أي منهما فئة معالم جديدة؛ Check Geometry تنشئ جدولاً و Repair Geometry تعدل البيانات الأصلية."
            }
        },
        "references": [{"title": "Repair Geometry, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/repair-geometry.htm", "kind": "official"}]
    },
    {
        "id": "DM-068", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Linear Referencing"],
        "question": {
            "en": "Which geometry attribute is required on polyline features to enable Linear Referencing and dynamic segmentation?",
            "ar": "ما هي خاصية الهندسة الإلزامية في معالم الخطوط لتمكين الإسناد الخطي (Linear Referencing) والتجزئة الديناميكية؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Z-values (Elevations)", "ar": "قيم Z (الارتفاعات)"}},
            {"id": "B", "text": {"en": "M-values (Measures)", "ar": "قيم M (المقاييس)"}},
            {"id": "C", "text": {"en": "COGO Direction angles", "ar": "زوايا اتجاهات COGO"}},
            {"id": "D", "text": {"en": "GlobalID GUIDs", "ar": "معرفات GlobalID الفريدة"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Linear referencing relies on M-values (measures) stored at vertices along route polyline geometries. These measures represent mileposts, kilometer markers, or stationing independent of horizontal coordinate distance.",
            "ar": "يعتمد الإسناد الخطي على قيم M (المقاييس) المخزنة عند نقاط الرؤوس على طول الخطوط، والتي تمثل علامات الأميال أو الكيلومترات أو المحطات بشكل مستقل عن مسافات الإسقاط الأفقي."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Z-values store height/depth elevation above a vertical datum, not linear referencing measures.",
                "C": "COGO directions store compass bearings, which are not used for dynamic segmentation routes.",
                "D": "GlobalIDs provide unique row identification, not distance positioning along line routes."
            },
            "ar": {
                "A": "تخزن قيم Z الارتفاع أو الانخفاض عن المرجع الرأسي وليست مقاييس مسافات خطية.",
                "C": "تخزن اتجاهات COGO الانحرافات البوصلية ولا تستخدم لتحديد المسافات على المسارات.",
                "D": "توفر معرفات GlobalID تعريفاً فريداً للسجل وليست لتحديد المواقع النسبية على الطرق."
            }
        },
        "references": [{"title": "An overview of linear referencing, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/an-overview-of-linear-referencing.htm", "kind": "official"}]
    },
    {
        "id": "DM-069", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Tool-based", "tools": ["Make Route Event Layer"],
        "question": {
            "en": "Which tool dynamically displays event tables containing milepost locations as spatial point or line features on top of a route layer?",
            "ar": "أي أداة تعرض جداول الأحداث المحتوية على مواقع علامات الأميال كمعالم نقطية أو خطية مكانية بشكل ديناميكي فوق طبقة المسارات؟"
        },
        "options": [
            {"id": "A", "text": {"en": "XY Table To Point", "ar": "XY Table To Point"}},
            {"id": "B", "text": {"en": "Make Route Event Layer", "ar": "Make Route Event Layer"}},
            {"id": "C", "text": {"en": "Geocode Addresses", "ar": "Geocode Addresses"}},
            {"id": "D", "text": {"en": "Locate Features Along Routes", "ar": "Locate Features Along Routes"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Make Route Event Layer calculates spatial positions dynamically by matching route identifiers and M-values from an event table against a route feature layer, creating a temporary in-memory feature layer.",
            "ar": "تقوم أداة Make Route Event Layer باحتساب المواقع المكانية ديناميكياً بمطابقة معرف المسار وقيم M من جدول الأحداث مع طبقة معالم المسار، مما ينشئ طبقة معالم مؤقتة في الذاكرة."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "XY Table To Point plots static coordinates from X and Y numeric columns, not linear M-values along routes.",
                "C": "Geocode Addresses matches text street addresses to an address locator.",
                "D": "Locate Features Along Routes does the reverse: it computes route and measure attributes from existing points or lines and writes them to a new table."
            },
            "ar": {
                "A": "أداة XY Table To Point تسقط النقاط من أعمدة الإحداثيات X و Y الثابتة وليس من قيم M الخطية.",
                "C": "أداة Geocode Addresses تطابق العناوين النصية عبر محدد المواقع.",
                "D": "أداة Locate Features Along Routes تقوم بالعملية العكسية بحساب قيم المسار والمقياس لمعالم قائمة وحفظها في جدول."
            }
        },
        "references": [{"title": "Make Route Event Layer, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/linear-referencing/make-route-event-layer.htm", "kind": "official"}]
    },
    {
        "id": "DM-070", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Tool-based", "tools": ["Create Locator"],
        "question": {
            "en": "Which modern ArcGIS Pro tool replaces the legacy Create Address Locator tool and builds locator files (.loc) supporting multi-role address parsing?",
            "ar": "أي أداة حديثة في ArcGIS Pro تحل محل الأداة القديمة Create Address Locator وتنشئ ملفات محدد المواقع (.loc) الداعمة لأدوار العنونة المتعددة؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Create Feature Locator", "ar": "Create Feature Locator"}},
            {"id": "B", "text": {"en": "Create Locator", "ar": "Create Locator"}},
            {"id": "C", "text": {"en": "Standardize Addresses", "ar": "Standardize Addresses"}},
            {"id": "D", "text": {"en": "Consolidate Locator", "ar": "Consolidate Locator"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "The Create Locator tool in ArcGIS Pro builds advanced .loc locators that support multiple locator roles (Point Address, Street Address, Postal, etc.) and enhanced auto-complete suggestions.",
            "ar": "تبني أداة Create Locator في ArcGIS Pro ملفات .loc متطورة تدعم أدوار عنونة متعددة (عناوين النقاط، الشوارع، الرموز البريدية) مع ميزات الإكمال التلقائي المحسنة."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Create Feature Locator is not an ArcGIS Pro tool name.",
                "C": "Standardize Addresses is an older geocoding preparation utility, not the tool that builds .loc files.",
                "D": "Consolidate Locator is a packaging tool, not a locator creation tool."
            },
            "ar": {
                "A": "Create Feature Locator ليس اسماً لأداة موجودة في ArcGIS Pro.",
                "C": "أداة Standardize Addresses هي أداة قديمة لتجهيز العناوين وليست لبناء ملف .loc.",
                "D": "أداة Consolidate Locator مخصصة لتجميع محدد المواقع وحزمه وليست لإنشائه."
            }
        },
        "references": [{"title": "Create Locator, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/geocoding/create-locator.htm", "kind": "official"}]
    },
    {
        "id": "DM-071", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Workflow-based", "tools": ["Rematch Addresses"],
        "question": {
            "en": "In the Rematch Addresses pane, what does a status of 'Tied' indicate for a geocoded address?",
            "ar": "في نافذة Rematch Addresses، إلى ماذا تشير حالة 'Tied' لعنوان تم تكويده جغرافياً؟"
        },
        "options": [
            {"id": "A", "text": {"en": "The address failed to match any feature in the reference locator", "ar": "فشل العنوان في التطابق مع أي معلم في محدد المواقع المرجعي"}},
            {"id": "B", "text": {"en": "Two or more candidate locations scored the exact same highest match score", "ar": "تساوى موقعان مرشحان أو أكثر في الحصول على أعلى درجة تطابق بالتساوي"}},
            {"id": "C", "text": {"en": "The address coordinates are tied to a linear referencing route", "ar": "إحداثيات العنوان مرتبطة بمسار إسناد خطي"}},
            {"id": "D", "text": {"en": "The record was manually matched and locked against automatic re-geocoding", "ar": "تمت مطابقة السجل يدوياً وقفله ضد إعادة التكويد التلقائي"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "A Tied status occurs when the geocoding engine finds multiple reference candidates with the exact same maximum match score, requiring user intervention to manually review candidates and pick the correct location.",
            "ar": "تحدث حالة التعادل (Tied) عندما يجد محرك التكويد الجغرافي عدة مواقع مرشحة تشترك في نفس أعلى درجة تطابق، مما يتطلب تدخلاً يدوياً لاختيار الموقع الصحيح."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Addresses that do not find any suitable candidates receive the 'Unmatched' status.",
                "C": "Tied in geocoding refers to candidate score ties, completely unrelated to linear referencing.",
                "D": "Manually matched records are designated as 'Matched' with user-confirmed status."
            },
            "ar": {
                "A": "العناوين التي لا تجد أي مرشح مطابق تأخذ حالة 'Unmatched'.",
                "C": "حالة التعادل Tied في التكويد تعني تساوي الدرجات ولا علاقة لها بالإسناد الخطي.",
                "D": "السجلات المطابقة يدوياً تأخذ حالة 'Matched' مؤكدة من المستخدم."
            }
        },
        "references": [{"title": "Rematch an address, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geocoding/rematch-an-address.htm", "kind": "official"}]
    },
    {
        "id": "DM-072", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Create Feature Dataset"],
        "question": {
            "en": "What restriction applies to the spatial reference of all feature classes created within or imported into the same Feature Dataset?",
            "ar": "ما هو القيد المفروض على المرجع المكاني لجميع فئات المعالم المنشأة أو المستوردة داخل نفس مجموعة بيانات المعالم (Feature Dataset)؟"
        },
        "options": [
            {"id": "A", "text": {"en": "They can use different projected coordinate systems as long as they share the same datum", "ar": "يمكنها استخدام أنظمة إحداثيات مسقطة مختلفة طالما أنها تشترك في نفس المرجع"}},
            {"id": "B", "text": {"en": "They must share the exact same spatial reference, including coordinate system, resolution, and tolerance", "ar": "يجب أن تشترك تماماً في نفس المرجع المكاني، بما في ذلك نظام الإحداثيات والدقة وحد التسامح"}},
            {"id": "C", "text": {"en": "Vector line and polygon layers can differ in coordinate systems, but points cannot", "ar": "يمكن لطبقات الخطوط والمضلعات أن تختلف في نظام الإحداثيات، ولكن النقاط لا يمكنها ذلك"}},
            {"id": "D", "text": {"en": "The coordinate system is defined per feature class and the feature dataset has no spatial reference", "ar": "نظام الإحداثيات يُحدد لكل فئة معالم على حدة ومجموعة البيانات ليس لها مرجع مكاني"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "A Feature Dataset enforces a common spatial reference. Every feature class inside a feature dataset must share identical coordinate system definition, XY resolution, and XY tolerance values to participate in topologies, geometric networks, or utility networks.",
            "ar": "تفرض مجموعة بيانات المعالم (Feature Dataset) مرجعاً مكانياً موحداً؛ لذا يجب أن تتطابق جميع فئات المعالم بداخلها في نظام الإحداثيات وقيم الدقة والتسامح للمشاركة في الطوبولوجيا والشبكات."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Different projected systems are strictly prohibited inside the same feature dataset.",
                "C": "Geometry type has no bearing on this rule; all geometry types inside the dataset must match the spatial reference.",
                "D": "The feature dataset itself holds the master spatial reference definition, which governs all contents."
            },
            "ar": {
                "A": "يُحظر تماماً وجود أنظمة إحداثيات مسقطة مختلفة داخل نفس Feature Dataset.",
                "C": "نوع الهندسة لا يغير من القاعدة شيئاً، فكل الأنواع ملزمة بالتطابق المكاني التام.",
                "D": "مجموعة البيانات نفسها هي الحاضن للمرجع المكاني الرئيسي الذي يلزم جميع محتوياتها."
            }
        },
        "references": [{"title": "Feature dataset basics, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-file-gdb/feature-dataset-basics.htm", "kind": "official"}]
    },
    {
        "id": "DM-073", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Create Mosaic Dataset"],
        "question": {
            "en": "What is the primary architectural advantage of a Mosaic Dataset over a single large merged Raster Dataset?",
            "ar": "ما هي الميزة الهيكلية الأساسية لمجموعة بيانات الموزاييك (Mosaic Dataset) مقارنة براستر مفرد ضخم مدمج (Raster Dataset)؟"
        },
        "options": [
            {"id": "A", "text": {"en": "It permanently duplicates and embeds all imagery pixels inside the geodatabase file", "ar": "تكرر وتدمج جميع بكسلات الصور بشكل دائم داخل ملف قاعدة البيانات"}},
            {"id": "B", "text": {"en": "It manages imagery as a catalog of references without copying source pixels, supporting dynamic on-the-fly mosaicking and raster functions", "ar": "تدير الصور ككتالوج مراجع دون تكرار تخزين البكسلات الأصلية، وتدعم دمج العرض وتطبيق دوال الراستر ديناميكياً"}},
            {"id": "C", "text": {"en": "It converts all rasters into vector polygon contours automatically", "ar": "تحول جميع ملفات الراستر إلى مضلعات كنتورية اتجاهية تلقائياً"}},
            {"id": "D", "text": {"en": "It limits raster resolution to a maximum of 30 meters to optimize rendering speed", "ar": "تحدد دقة الراستر بحد أقصى 30 متراً لتسريع سرعة العرض"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "A Mosaic Dataset models collections of rasters by indexing their footprints, metadata, and file paths. Source pixels remain in their original file format and location, allowing dynamic on-the-fly orthorectification, pan-sharpening, and mosaic blending without data duplication.",
            "ar": "تدير مجموعة بيانات الموزاييك مجموعات الراستر بفهرسة حدودها وبياناتها الوصفية ومساراتها؛ وتبقى البكسلات الأصلية في مكانها دون تكرار، مما يتيح التعديل والدمج وتطبيق الفلاتر اللحظية ديناميكياً."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Embedding pixels directly is how managed raster datasets work, not mosaic datasets.",
                "C": "Mosaic datasets handle raster pixels and do not convert imagery into vector contour lines.",
                "D": "Mosaic datasets preserve native pixel resolution and do not artificially restrict cell size to 30 meters."
            },
            "ar": {
                "A": "دمج البكسلات مباشرة هو أسلوب Raster Dataset التقليدي وليس الموزاييك.",
                "C": "مجموعات الموزاييك تتعامل مع صور الراستر ولا تحولها إلى خطوط كونتور اتجاهية.",
                "D": "تحافظ الموزاييك على دقة البكسل الأصلية للصور ولا تجبرها على حجم 30 متراً."
            }
        },
        "references": [{"title": "What is a mosaic dataset?, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/imagery/what-is-a-mosaic-dataset.htm", "kind": "official"}]
    },
    {
        "id": "DM-074", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Build Overviews"],
        "question": {
            "en": "In a Mosaic Dataset, what is the role of Overviews compared to Pyramids in a standalone raster?",
            "ar": "في مجموعة بيانات الموزاييك، ما هو دور المناظر العامة (Overviews) مقارنة بالأهرامات (Pyramids) في الراستر المفرد؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Overviews are lower-resolution raster datasets generated across the entire mosaicked collection to speed up zoomed-out display", "ar": "المناظر العامة (Overviews) هي مجموعات بيانات راستر منخفضة الدقة تُنشأ للمجموعة المدمجة ككل لتسريع العرض عند التصغير"}},
            {"id": "B", "text": {"en": "Overviews store spatial index grids for vector boundary footprints", "ar": "تخزن المناظر العامة شبكات الفهارس المكانية لحدود المعالم الاتجاهية"}},
            {"id": "C", "text": {"en": "Overviews compress TIFF imagery into MrSID format", "ar": "تضغط المناظر العامة صور TIFF إلى صيغة MrSID"}},
            {"id": "D", "text": {"en": "Overviews convert multispectral rasters into single-band grayscale images", "ar": "تحول المناظر العامة الصور متعددة الأطياف إلى صور تدرج رمادي أحادية النطاق"}}
        ],
        "correctAnswer": "A",
        "explanation": {
            "en": "While pyramids accelerate display for an individual raster file, Overviews are reduced-resolution raster tiles built specifically for the mosaic dataset as a whole, enabling fast display when zoomed out beyond the scale of individual raster items.",
            "ar": "بينما تسرع الأهرامات (Pyramids) عرض ملف الراستر الفردي، فإن الـ Overviews هي مستويات دقة مخفضة تُبنى للموزاييك ككل لتسريع العرض عند التصغير لمقاييس رسم واسعة تتجاوز إطارات الصور الفردية."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "B": "Spatial indexes are managed via database indexing, not raster overviews.",
                "C": "Overviews do not convert source rasters into third-party proprietary MrSID files.",
                "D": "Overviews maintain the spectral band structure of the mosaic dataset."
            },
            "ar": {
                "B": "الفهارس المكانية تُدار عبر فهارس قواعد البيانات وليس عبر ملفات الـ Overviews.",
                "C": "لا تحول Overviews ملفات الصور إلى صيغ MrSID التجارية.",
                "D": "تحافظ الـ Overviews على البنية الطيفية لنطاقات مجموعة الموزاييك."
            }
        },
        "references": [{"title": "Mosaic dataset overviews, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/imagery/mosaic-dataset-overviews.htm", "kind": "official"}]
    },
    {
        "id": "DM-075", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage coordinate systems to preserve the desired spatial properties",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Project Raster"],
        "question": {
            "en": "When using Project Raster on a discrete Land Use classification raster, which resampling technique MUST be used to prevent creating non-existent artificial land cover codes?",
            "ar": "عند استخدام أداة Project Raster على راستر تصنيف استخدامات الأراضي (بيانات فئوية منفصلة)، أي طريقة إعادة استعيان (Resampling) يجب استخدامها لمنع استحداث رموز تصنيف وهمية غير موجودة؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Bilinear Interpolation", "ar": "Bilinear Interpolation (الاستيفاء الخطي الثنائي)"}},
            {"id": "B", "text": {"en": "Cubic Convolution", "ar": "Cubic Convolution (الالتفاف التكعيبي)"}},
            {"id": "C", "text": {"en": "Nearest Neighbor", "ar": "Nearest Neighbor (الجار الأقرب)"}},
            {"id": "D", "text": {"en": "Majority", "ar": "Majority (الأغلبية)"}}
        ],
        "correctAnswer": "C",
        "explanation": {
            "en": "Nearest Neighbor retains original cell values without mathematical averaging. Bilinear Interpolation and Cubic Convolution calculate weighted averages of surrounding cells, which would produce fractional or non-existent class codes when applied to categorical/discrete data like Land Use.",
            "ar": "تحافظ طريقة الجار الأقرب (Nearest Neighbor) على قيم الخلايا الأصلية دون تعديل؛ بينما تحسب الطرق الأخرى (Bilinear و Cubic) متوسطات حسابية موزونة، مما يؤدي لاستحداث قيم كسرية أو فئات تصنيف وهمية لا وجود لها في البيانات الفئوية."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Bilinear interpolates values using 4 neighboring cells; strictly suitable for continuous elevation or temperature rasters.",
                "B": "Cubic convolution fits a smooth curve through 16 cells; suitable for continuous imagery, not categorical codes.",
                "D": "Majority is a post-processing filtering method, not the standard projection resampling choice."
            },
            "ar": {
                "A": "طريقة Bilinear تستوفي القيم من 4 خلايا مجاورة وهي مناسبة للبيانات المستمرة كالحرارة والارتفاع فقط.",
                "B": "طريقة Cubic تنعم القيم بناءً على 16 خلية وتصلح للصور الفضائية المستمرة وليس الأكواد الفئوية.",
                "D": "طريقة Majority تُستخدم كفلتر إحصائي بعدي وليست خيار إعادة الاستعيان القياسي للإسقاط."
            }
        },
        "references": [{"title": "Project Raster, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/project-raster.htm", "kind": "official"}]
    },
    {
        "id": "DM-076", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Geodatabase Topology"],
        "question": {
            "en": "In a Geodatabase Topology, what is the role of Coordinate Ranks (ranging from 1 to 50)?",
            "ar": "في طوبولوجيا قواعد البيانات الجغرافية (Geodatabase Topology)، ما هو دور رتب الإحداثيات (Coordinate Ranks) التي تتراوح من 1 إلى 50؟"
        },
        "options": [
            {"id": "A", "text": {"en": "They determine the rendering order of layers in the Contents pane", "ar": "تحدد ترتيب رسم الطبقات في نافذة المحتويات"}},
            {"id": "B", "text": {"en": "They control which feature vertices remain fixed and which vertices snap during topology validation", "ar": "تتحكم في أي رؤوس المعالم تظل ثابتة في مكانها وأيها تنجذب وتتحرك أثناء التحقق من الطوبولوجيا"}},
            {"id": "C", "text": {"en": "They assign the administrative editing permissions to geodatabase users", "ar": "تحدد صلاحيات التحرير الإدارية لمستخدمي قاعدة البيانات"}},
            {"id": "D", "text": {"en": "They specify the number of attribute validation rules assigned per feature", "ar": "تحدد عدد قواعد التحقق السماتي المسموح بها لكل معلم"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Coordinate ranks control vertex movement during topology validation: Rank 1 indicates highest reliability (highest accuracy; vertices will not move), while features with lower ranks (larger numbers up to 50) will have their vertices adjusted and snapped to higher-ranked features within the cluster tolerance.",
            "ar": "تتحكم رتب الإحداثيات في حركة رؤوس المعالم أثناء التحقق؛ فالرتبة 1 تمثل الدقة الأعلى (لا تتحرك رؤوسها)، بينما المعالم ذات الرتب الأقل (أرقام أكبر حتى 50) تتحرك وتنجذب رؤوسها نحو المعالم الأعلى دقة ضمن حد التسامح العنقودي."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Layer drawing order is determined in the Contents pane, completely independent of topology ranks.",
                "C": "User editing permissions are managed in Enterprise RDBMS security, not topology coordinate ranks.",
                "D": "Ranks govern spatial cluster snapping, not attribute rules."
            },
            "ar": {
                "A": "ترتيب رسم الطبقات يُحدد في نافذة المحتويات ولا يرتبط برتب الطوبولوجيا.",
                "C": "صلاحيات المستخدمين تُدار في خادم قاعدة البيانات RDBMS وليس برتب الإحداثيات.",
                "D": "تتحكم الرتب في الانجذاب المكاني العنقودي وليس في قواعد السمات."
            }
        },
        "references": [{"title": "Topology coordinate ranks, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-file-gdb/topology-in-arcgis.htm", "kind": "official"}]
    },
    {
        "id": "DM-077", "kind": "mcq", "domain": "Data Management",
        "objective": "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes",
        "difficulty": "Intermediate", "type": "Tool-based", "tools": ["Merge"],
        "question": {
            "en": "What is the key difference between the editing 'Merge' tool in the Modify Features pane and the 'Merge' geoprocessing tool in the Data Management toolbox?",
            "ar": "ما هو الفرق الرئيسي بين أداة 'Merge' للتحرير في نافذة Modify Features وأداة 'Merge' في صندوق أدوات التحليل الجغرافي Data Management؟"
        },
        "options": [
            {"id": "A", "text": {"en": "The editing Merge tool combines selected features within the same layer in-place; the geoprocessing Merge tool combines multiple datasets into a new output dataset", "ar": "أداة Merge في التحرير تدمج معالم محددة داخل نفس الطبقة مباشرة؛ بينما أداة Merge في التحليل تجمع عدة طبقات مستقلة في ملف مخرجات جديد"}},
            {"id": "B", "text": {"en": "The editing Merge tool creates raster pyramids; the geoprocessing Merge tool edits vector vertices", "ar": "أداة التحرير تنشئ أهرامات راستر، وأداة التحليل تعدل رؤوس المعالم الاتجاهية"}},
            {"id": "C", "text": {"en": "The editing Merge tool only works on point features; the geoprocessing Merge tool only works on polygons", "ar": "أداة التحرير تعمل على النقاط فقط، وأداة التحليل تعمل على المضلعات فقط"}},
            {"id": "D", "text": {"en": "Both tools perform identical operations and exist only for user convenience", "ar": "تؤدي الأداتان نفس الوظيفة تماماً ووجودهما مجرد تكرار لتسهيل الوصول"}}
        ],
        "correctAnswer": "A",
        "explanation": {
            "en": "The editing Merge tool acts in-place on two or more selected features within the currently editable layer, replacing them with a single feature. The geoprocessing Merge tool takes multiple input feature classes or tables and writes them into an entirely new output dataset.",
            "ar": "أداة Merge في التحرير تدمج معالم محددة في الطبقة النشطة وتحولها لمعلم واحد في مكانها دون إنشاء ملف جديد. أما أداة Merge في أدوات Geoprocessing فتأخذ عدة فئات معالم وتدمج سجلاتها معاً في طبقة مخرجات جديدة كلياً."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "B": "Neither merge tool deals with raster pyramids.",
                "C": "Both tools support points, lines, and polygons.",
                "D": "They operate under completely different mechanisms (in-place feature edit vs dataset-level new file creation)."
            },
            "ar": {
                "B": "لا تتعامل أي من أداتي الدمج مع أهرامات الراستر.",
                "C": "تدعم كلتا الأداتين النقاط والخطوط والمضلعات.",
                "D": "تختلف الأداتان جوهرياً في آلية العمل (تعديل داخلي للمعالم مقابل إنشاء ملف جديد بالكامل)."
            }
        },
        "references": [{"title": "Merge features into one feature, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/merge-features-into-one-feature.htm", "kind": "official"}]
    },
    {
        "id": "DM-078", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage coordinate systems to preserve the desired spatial properties",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Map Properties"],
        "question": {
            "en": "When a new, empty Map is created in ArcGIS Pro, what determines its initial coordinate system?",
            "ar": "عند إنشاء خريطة جديدة فارغة في ArcGIS Pro، ما الذي يحدد نظام إحداثياتها الأولي؟"
        },
        "options": [
            {"id": "A", "text": {"en": "It is permanently locked to WGS 1984 Web Mercator Auxiliary Sphere", "ar": "تُقفل بشكل دائم على نظام WGS 1984 Web Mercator Auxiliary Sphere"}},
            {"id": "B", "text": {"en": "It adopts the coordinate system of the first non-basemap layer added to the map", "ar": "تكتسب نظام إحداثيات أول طبقة بيانات (غير خريطة الأساس) تُضاف إلى الخريطة"}},
            {"id": "C", "text": {"en": "It defaults to the operating system's regional settings", "ar": "تأخذ الإعدادات الافتراضية للمنطقة الزمنية لنظام التشغيل"}},
            {"id": "D", "text": {"en": "It is determined by the ArcGIS Pro user license level", "ar": "يحدده مستوى ترخيص المستخدم لـ ArcGIS Pro"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "An empty map initializes with no coordinate system, but adopts the spatial reference of the first layer added to the map (excluding the default basemap, which defaults to Web Mercator if basemaps are configured in application options).",
            "ar": "تبدأ الخريطة الفارغة بدون نظام إحداثيات ثابت، وتكتسب تلقائياً المرجع المكاني لأول طبقة بيانات تُضاف إليها (باستثناء خريطة الأساس الافتراضية إذا كانت مفعلة في خيارات التطبيق)."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Web Mercator is common for default Esri basemaps, but the map coordinate system is never permanently locked and can be modified at any time.",
                "C": "Operating system locale settings do not control GIS coordinate systems.",
                "D": "License levels (Basic, Standard, Advanced) do not alter map projection mechanics."
            },
            "ar": {
                "A": "نظام Web Mercator خاص بخرائط الأساس فقط، ولكن نظام إحداثيات الخريطة ليس مقفلاً ويمكن تغييره دائماً.",
                "C": "إعدادات نظام التشغيل لا تتحكم بأنظمة الإحداثيات الجغرافية.",
                "D": "مستويات التراخيص لا تؤثر على آلية تعيين الإسقاط للخريطة."
            }
        },
        "references": [{"title": "Specify a coordinate system, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/mapping/properties/specify-a-coordinate-system.htm", "kind": "official"}]
    },
    {
        "id": "DM-079", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Attribute Rules"],
        "question": {
            "en": "Which Arcade global profile variable is used in Attribute Rules to inspect the type of edit operation being performed ($editcontext.editType)?",
            "ar": "ما هو المتغير العام في ملف تعريف Arcade المستخدم في القواعد السماتية لمعرفة نوع عملية التحرير الجارية ($editcontext.editType)؟"
        },
        "options": [
            {"id": "A", "text": {"en": "$feature", "ar": "$feature"}},
            {"id": "B", "text": {"en": "$editcontext.editType", "ar": "$editcontext.editType"}},
            {"id": "C", "text": {"en": "$datastore", "ar": "$datastore"}},
            {"id": "D", "text": {"en": "$layer", "ar": "$layer"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "In ArcGIS Pro attribute rule expressions, $editcontext.editType returns 'INSERT', 'UPDATE', or 'DELETE', allowing script logic to conditionally execute code depending on whether a feature is newly created or modified.",
            "ar": "في تعبيرات القواعد السماتية بـ ArcGIS Pro، يعيد المتغير $editcontext.editType القيم 'INSERT' أو 'UPDATE' أو 'DELETE'، مما يسمح بتنفيذ منطق برمجي مخصص بحسب ما إذا كان المعلم قد أُنشئ حديثاً أو تم تعديله."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "$feature provides access to the attributes and geometry of the current record, not the edit operation type.",
                "C": "$datastore represents the parent geodatabase connection object for executing cross-table queries.",
                "D": "$layer represents the map layer in visualization profiles, not attribute rules."
            },
            "ar": {
                "A": "المتغير $feature يوفر الوصول لسمات وهندسة المعلم الحالي وليس لنوع عملية التحرير.",
                "C": "المتغير $datastore يمثل اتصال قاعدة البيانات للاستعلام عبر الجداول الأخرى.",
                "D": "المتغير $layer يمثل طبقة الخريطة في ملفات العرض البصري وليس في قواعد السمات."
            }
        },
        "references": [{"title": "Attribute rule script expression, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-file-gdb/attribute-rule-script-expressions.htm", "kind": "official"}]
    },
    {
        "id": "DM-080", "kind": "mcq", "domain": "Data Management",
        "objective": "Given a scenario, determine the appropriate existing geodatabase elements to use",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Attribute Rules"],
        "question": {
            "en": "Which Arcade geometry function calculates geodesic area in square meters directly on ellipsoidal coordinates without requiring a planar projection?",
            "ar": "أي دالة هندسية في Arcade تحسب المساحة الجيوديسية بالمتر المربع مباشرة على إحداثيات المجسم الإهليلجي دون الحاجة لإسقاط مستوٍ؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Area($feature, 'square-meters')", "ar": "Area($feature, 'square-meters')"}},
            {"id": "B", "text": {"en": "AreaGeodetic($feature, 'square-meters')", "ar": "AreaGeodetic($feature, 'square-meters')"}},
            {"id": "C", "text": {"en": "BufferGeodetic($feature)", "ar": "BufferGeodetic($feature)"}},
            {"id": "D", "text": {"en": "LengthGeodetic($feature, 'meters')", "ar": "LengthGeodetic($feature, 'meters')"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "AreaGeodetic calculates the surface area of a polygon geometry taking the earth's curvature into account according to the underlying ellipsoid, returning accurate geodesic area measurements regardless of projection distortion.",
            "ar": "تحسب دالة AreaGeodetic مساحة سطح المضلع مع مراعاة انحناء الأرض وفقاً للمجسم الإهليلجي، مما يعطي قياسات مساحية جيوديسية دقيقة بغض النظر عن تشوهات الإسقاط."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Area calculates planar area, which is subject to distortion in projected systems and invalid for geographic systems.",
                "C": "BufferGeodetic constructs a buffer zone polygon, it does not calculate area.",
                "D": "LengthGeodetic measures linear distance along lines, not polygonal area."
            },
            "ar": {
                "A": "دالة Area تحسب المساحة المستوية المتأثرة بتشوهات الإسقاط وتكون غير دقيقة في الأنظمة الجغرافية.",
                "C": "دالة BufferGeodetic تنشئ مضلع حرم جيوديسي ولا تحسب المساحة.",
                "D": "دالة LengthGeodetic تقيس الأطوال الخطية وليس مساحات المضلعات."
            }
        },
        "references": [{"title": "Arcade Geometry functions, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/arcpy/spatial-analyst/arcade-functions.htm", "kind": "official"}]
    }
]

# Load existing
target_file = 'public/data/questions/data-management.json'
with open(target_file, 'r', encoding='utf-8') as f:
    existing = json.load(f)

existing_ids = set(q['id'] for q in existing)
all_new = [q for q in dm_40_60 if q['id'] not in existing_ids] + [q for q in dm_61_80 if q['id'] not in existing_ids]

combined = existing + all_new
# Sort by ID
combined.sort(key=lambda x: int(x['id'].split('-')[1]))

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

print(f"Data Management MCQs successfully written: {len(combined)} questions (expected 80).")

