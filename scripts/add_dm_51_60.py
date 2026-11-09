# -*- coding: utf-8 -*-
"""
Add DM-051 through DM-060 to reach exactly 80 Data Management MCQs.
"""
import json

dm_51_60 = [
    {
        "id": "DM-051", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Enable Attachments"],
        "question": {
            "en": "What underlying geodatabase objects are created when you run the Enable Attachments tool on a feature class?",
            "ar": "ما هي عناصر قاعدة البيانات الجغرافية التي يتم إنشاؤها في الخلفية عند تشغيل أداة Enable Attachments على فئة معالم؟"
        },
        "options": [
            {"id": "A", "text": {"en": "A new BLOB field inside the existing feature class table", "ar": "حقل BLOB جديد داخل جدول فئة المعالم الحالية"}},
            {"id": "B", "text": {"en": "An attachment table (_ATTACH) and a non-attributed composite relationship class linking the table to the feature class", "ar": "جدول مرفقات (_ATTACH) وفئة علاقات مركبة غير سماتية تربط الجدول بفئة المعالم"}},
            {"id": "C", "text": {"en": "A zip archive on disk containing document references", "ar": "أرشيف مضغوط zip على القرص الصلب يحتوي على مراجع الملفات"}},
            {"id": "D", "text": {"en": "An external hyperlinks XML schema file", "ar": "ملف مخطط XML خارجي للروابط التشعبية"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Enabling attachments creates a separate attachment table (named <featureclass>__ATTACH) containing the binary files and metadata, along with a composite relationship class (named <featureclass>__ATTACHREL) linking features to attachments.",
            "ar": "يؤدي تفعيل المرفقات إلى إنشاء جدول مرفقات مستقل (يحمل الاسم <featureclass>__ATTACH) لتخزين الملفات والبيانات الوصفية، بالإضافة إلى فئة علاقات مركبة تربط المعالم بمرفقاتها."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Attachments are stored in a dedicated auxiliary table, not as an in-line BLOB field in the main feature class table.",
                "C": "Files are stored internally inside the geodatabase repository, not as an external disk zip file.",
                "D": "ArcGIS Pro attachments use geodatabase tables and relationship classes, not external XML schemas."
            },
            "ar": {
                "A": "تُخزن المرفقات في جدول مساعد مستقل وليس في حقل BLOB داخلي بالجدول الرئيسي.",
                "C": "تُحفظ الملفات داخلياً في قاعدة البيانات وليس في أرشيف zip خارجي على القرص.",
                "D": "تعتمد المرفقات في ArcGIS Pro على جداول وفئات علاقات الجيوداتابيس وليس ملفات XML."
            }
        },
        "references": [{"title": "Enable Attachments, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/enable-attachments.htm", "kind": "official"}]
    },
    {
        "id": "DM-052", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Add Field"],
        "question": {
            "en": "Which field data type should be used when an organization requires embedding complex binary data such as digital signatures, photos, or CAD blocks directly in an attribute row?",
            "ar": "أي نوع بيانات للحقول يجب استخدامه عندما تتطلب المؤسسة تضمين بيانات ثنائية معقدة مثل التوقيعات الرقمية أو الصور أو كتل CAD مباشرة في صف السجل السماتي؟"
        },
        "options": [
            {"id": "A", "text": {"en": "GUID", "ar": "GUID"}},
            {"id": "B", "text": {"en": "Text (Length: 255)", "ar": "Text (بطول 255 حرفاً)"}},
            {"id": "C", "text": {"en": "BLOB (Binary Large Object)", "ar": "BLOB (Binary Large Object - كائن ثنائي كبير)"}},
            {"id": "D", "text": {"en": "Double", "ar": "Double (عشري مزدوج)"}}
        ],
        "correctAnswer": "C",
        "explanation": {
            "en": "The BLOB (Binary Large Object) field data type is designed to store machine-readable binary data, such as images, multimedia, or custom binary payloads directly in the geodatabase record.",
            "ar": "نوع الحقل BLOB (Binary Large Object) مخصص لتخزين البيانات الثنائية القابلة للقراءة آلياً، مثل الصور والملفات متعددة الوسائط أو الحزم الثنائية المخصصة مباشرة في سجل قاعدة البيانات الجغرافية."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "GUID stores 36-character globally unique identifier strings, not binary files.",
                "B": "Text fields store character alphanumeric strings and cannot reliably represent arbitrary binary data.",
                "D": "Double stores 64-bit double-precision floating-point numbers."
            },
            "ar": {
                "A": "حقل GUID يخزن سلاسل معرفات فريدة من 36 حرفاً وليس ملفات ثنائية.",
                "B": "الحقول النصية تخزن نصوصاً وأرقاماً أبجدية ولا يمكنها تمثيل البيانات الثنائية بأمان.",
                "D": "حقل Double يخزن أرقاماً عشرية ذات دقة مزدوجة."
            }
        },
        "references": [{"title": "ArcGIS field data types, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/data/geodatabases/manage-file-gdb/arcgis-field-data-types.htm", "kind": "official"}]
    },
    {
        "id": "DM-053", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Beginner", "type": "Tool-based", "tools": ["Feature Class To Geodatabase"],
        "question": {
            "en": "Which geoprocessing tool should you use to convert multiple shapefiles into geodatabase feature classes in a single batch operation?",
            "ar": "أي أداة تحليل جغرافي يجب استخدامها لتحويل عدة ملفات shapefile إلى فئات معالم داخل قاعدة بيانات جغرافية في عملية دفعة واحدة؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Feature Class To Geodatabase", "ar": "Feature Class To Geodatabase"}},
            {"id": "B", "text": {"en": "Create Feature Class", "ar": "Create Feature Class"}},
            {"id": "C", "text": {"en": "Append", "ar": "Append"}},
            {"id": "D", "text": {"en": "Copy Features", "ar": "Copy Features"}}
        ],
        "correctAnswer": "A",
        "explanation": {
            "en": "Feature Class To Geodatabase accepts a multi-value list of input feature classes or shapefiles and imports them all into a destination geodatabase simultaneously.",
            "ar": "تقبل أداة Feature Class To Geodatabase قائمة متعددة من ملفات shapefile أو فئات المعالم وتستوردها جميعاً إلى قاعدة البيانات الجغرافية المستهدفة في دفعة واحدة."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "B": "Create Feature Class creates a single new empty feature class schema.",
                "C": "Append inserts features from an input dataset into an already existing target feature class.",
                "D": "Copy Features copies a single feature class to another single output path."
            },
            "ar": {
                "B": "تنشئ Create Feature Class مخطط فئة معالم فارغة جديدة واحدة فقط.",
                "C": "تضيف أداة Append معالم إلى فئة معالم قائمة بالفعل ومعدة مسبقاً.",
                "D": "تنسخ أداة Copy Features فئة معالم واحدة إلى مخرج فردي واحد."
            }
        },
        "references": [{"title": "Feature Class To Geodatabase, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/feature-class-to-geodatabase.htm", "kind": "official"}]
    },
    {
        "id": "DM-054", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Enable Archiving"],
        "question": {
            "en": "What happens when you enable Geodatabase Archiving on a non-versioned feature class in an enterprise or file geodatabase?",
            "ar": "ماذا يحدث عند تفعيل الأرشفة (Geodatabase Archiving) على فئة معالم غير مفعل بها الإصدارات في قاعدة بيانات مؤسسية أو ملفية؟"
        },
        "options": [
            {"id": "A", "text": {"en": "The dataset is converted to a read-only ZIP file on disk", "ar": "يتم تحويل مجموعة البيانات إلى ملف ZIP للقراءة فقط على القرص"}},
            {"id": "B", "text": {"en": "An archive class (_H) is created and GDB_FROM_DATE and GDB_TO_DATE timestamp fields track all historical changes", "ar": "تُنشأ فئة أرشيف (_H) وحقول تواريخ زمنية (GDB_FROM_DATE و GDB_TO_DATE) لتتبع كافة التغييرات التاريخية"}},
            {"id": "C", "text": {"en": "All features older than 30 days are automatically deleted", "ar": "تُحذف جميع المعالم التي يزيد عمرها عن 30 يوماً تلقائياً"}},
            {"id": "D", "text": {"en": "The coordinate system is upgraded to a 4D vertical reference system", "ar": "تتم ترقية نظام الإحداثيات إلى نظام مرجعي رأسي رباعي الأبعاد"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Geodatabase archiving maintains an associated historical archive table (with an _H suffix) that logs every insert, update, and delete along with GDB_FROM_DATE and GDB_TO_DATE timestamps, preserving the complete lifecycle of data.",
            "ar": "تحتفظ أرشفة الجيوداتابيس بجدول تاريخي مرتبط (يحمل لاحقة _H) يسجل كل إضافة وتعديل وحذف مع تواريخ GDB_FROM_DATE و GDB_TO_DATE، مما يحفظ التاريخ الكامل للبيانات."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Archiving does not zip or make data read-only; editing continues normally in the base feature class.",
                "C": "Archiving preserves historical data indefinitely; it never deletes older records.",
                "D": "Coordinate systems and dimensionality (2D/3D) are unaffected by archiving."
            },
            "ar": {
                "A": "الأرشفة لا تضغط البيانات ولا تجعلها للقراءة فقط، بل يستمر التحرير بشكل طبيعي.",
                "C": "تحافظ الأرشفة على السجلات التاريخية بشكل دائم ولا تحذف السجلات القديمة أبداً.",
                "D": "أنظمة الإحداثيات والأبعاد الهندسية لا تتأثر بتفعيل الأرشفة."
            }
        },
        "references": [{"title": "Enable Archiving, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/enable-archiving.htm", "kind": "official"}]
    },
    {
        "id": "DM-055", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Best-practice", "tools": ["Add Attribute Index"],
        "question": {
            "en": "When should a GIS analyst create an Attribute Index on a specific field in a geodatabase feature class?",
            "ar": "متى يجب على محلل نظم المعلومات الجغرافية إنشاء فهرس سماتي (Attribute Index) على حقل معين في فئة معالم الجيوداتابيس؟"
        },
        "options": [
            {"id": "A", "text": {"en": "On fields that are frequently queried with WHERE clauses or used as foreign keys in table joins", "ar": "على الحقول المستخدمة بكثرة في استعلامات WHERE أو المستخدمة كمفاتيح ربط أجنبية في الضم الجدولي"}},
            {"id": "B", "text": {"en": "On every text field in every table regardless of table size", "ar": "على كل حقل نصي في جميع الجداول بغض النظر عن حجم الجدول"}},
            {"id": "C", "text": {"en": "Only on the Shape geometry field", "ar": "فقط على حقل هندسة الشكل (Shape)"}},
            {"id": "D", "text": {"en": "Only when publishing datasets to static PDF files", "ar": "فقط عند تصدير ونشر البيانات إلى ملفات PDF ثابتة"}}
        ],
        "correctAnswer": "A",
        "explanation": {
            "en": "Attribute indexes significantly speed up query execution (SQL queries, definition queries, and attribute joins) on frequently searched columns, especially in large tables with thousands or millions of records.",
            "ar": "تسرع الفهارس السماتية أداء الاستعلامات (مثل استعلامات SQL والتعريفات والضم الجدولي) على الأعمدة كثيرة البحث، خاصة في الجداول الضخمة التي تحتوي على آلاف أو ملايين السجلات."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "B": "Over-indexing every field increases file size and degrades editing performance, as each index must be rebuilt on edit.",
                "C": "The Shape field uses a Spatial Index, not an Attribute Index.",
                "D": "Attribute indexes are geodatabase search structures and have no effect on static exported PDF files."
            },
            "ar": {
                "B": "إنشاء فهارس على كل الحقول يستهلك مساحة ويبطئ التحرير لأن الفهارس يعاد بناؤها مع كل تعديل.",
                "C": "حقل Shape يعتمد على الفهرس المكاني (Spatial Index) وليس الفهرس السماتي.",
                "D": "فهارس السمات هي تراكيب بحث داخلية في الجيوداتابيس ولا علاقة لها بملفات PDF المصدرة."
            }
        },
        "references": [{"title": "Add Attribute Index, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-attribute-index.htm", "kind": "official"}]
    },
    {
        "id": "DM-056", "kind": "mcq", "domain": "Data Management",
        "objective": "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes",
        "difficulty": "Beginner", "type": "Tool-based", "tools": ["Snapping"],
        "question": {
            "en": "Which snapping mode in ArcGIS Pro snaps the pointer to the exact midpoint of a line segment or polygon boundary edge?",
            "ar": "أي نمط من أنماط الانجذاب (Snapping) في ArcGIS Pro يجذب المؤشر إلى نقطة المنتصف الدقيقة لقطعة خطية أو حافة مضلع؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Point Snapping", "ar": "Point Snapping (انجذاب للنقاط)"}},
            {"id": "B", "text": {"en": "Midpoint Snapping", "ar": "Midpoint Snapping (انجذاب للمنتصف)"}},
            {"id": "C", "text": {"en": "Vertex Snapping", "ar": "Vertex Snapping (انجذاب للرؤوس)"}},
            {"id": "D", "text": {"en": "Intersection Snapping", "ar": "Intersection Snapping (انجذاب للتقاطعات)"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Midpoint Snapping snaps the cursor directly to the halfway point between two consecutive vertices on a polyline or polygon edge.",
            "ar": "يجذب نمط Midpoint Snapping المؤشر مباشرة إلى النقطة المنصفة الدقيقة الواقعة بين رأسي خط أو حافة مضلع."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Point snapping snaps to point features or multipoint geometries.",
                "C": "Vertex snapping snaps to existing discrete vertices, not midpoints.",
                "D": "Intersection snapping snaps to points where two lines or edges cross."
            },
            "ar": {
                "A": "يجذب Point snapping إلى معالم النقاط المستقلة.",
                "C": "يجذب Vertex snapping إلى نقاط الرؤوس القائمة وليس إلى منتصف القطع.",
                "D": "يجذب Intersection snapping إلى نقاط تقاطع خطين أو حافتين."
            }
        },
        "references": [{"title": "Snapping settings, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/snapping.htm", "kind": "official"}]
    },
    {
        "id": "DM-057", "kind": "mcq", "domain": "Data Management",
        "objective": "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes",
        "difficulty": "Intermediate", "type": "Tool-based", "tools": ["Reshape"],
        "question": {
            "en": "When using the Reshape tool in the Modify Features pane to edit a polygon boundary, how must the sketched reshape line interact with the existing polygon?",
            "ar": "عند استخدام أداة Reshape في نافذة Modify Features لتعديل حدود مضلع، كيف يجب أن يتفاعل خط الرسم التعديلي مع المضلع القائم؟"
        },
        "options": [
            {"id": "A", "text": {"en": "The sketch must start and end at least twice across the boundary of the existing polygon", "ar": "يجب أن يبدأ خط الرسم وينتهي قاطعاً حدود المضلع القائم في نقطتين على الأقل"}},
            {"id": "B", "text": {"en": "The sketch must remain completely inside the interior of the polygon without touching boundaries", "ar": "يجب أن يقع خط الرسم بالكامل داخل المضلع دون لمس الحدود"}},
            {"id": "C", "text": {"en": "The sketch must be a closed polygon loop drawn entirely outside the feature", "ar": "يجب أن يكون خط الرسم حلقة مضلع مغلقة مرسومة بالكامل خارج المعلم"}},
            {"id": "D", "text": {"en": "The sketch must snap to the polygon centroid point", "ar": "يجب أن ينجذب خط الرسم إلى نقطة المركز الهندسي للمضلع"}}
        ],
        "correctAnswer": "A",
        "explanation": {
            "en": "To successfully reshape a polygon, the replacement sketch line must cross the polygon boundary at least twice; the section of the original boundary between the intersection points is replaced by the sketch.",
            "ar": "لإعادة تشكيل مضلع بنجاح، يجب أن يتقاطع خط الرسم مع حدود المضلع في نقطتين على الأقل؛ ويتم استبدال جزء الحد الأصلي المحصور بين نقطتي التقاطع بالمسار المرسوم الجديد."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "B": "A sketch drawn wholly inside cannot define boundary replacement and will fail.",
                "C": "A closed loop outside the polygon does not define boundary replacement.",
                "D": "Reshaping operates on exterior and interior boundaries, not centroid points."
            },
            "ar": {
                "B": "الرسم الواقع بالكامل داخل المضلع لا يمس الحدود ولا يمكنه استبدالها فيفشل الأمر.",
                "C": "الحلقة المغلقة الخارجية لا تعيد تشكيل الحد القائم.",
                "D": "تعديل التشكيل يتعامل مع الحدود الخارجية والداخلية وليس المراكز الهندسية."
            }
        },
        "references": [{"title": "Reshape a feature, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/reshape-a-feature.htm", "kind": "official"}]
    },
    {
        "id": "DM-058", "kind": "mcq", "domain": "Data Management",
        "objective": "Use ArcGIS Pro editing functionality to create, modify, and delete features and attributes",
        "difficulty": "Intermediate", "type": "Tool-based", "tools": ["Align Edge"],
        "question": {
            "en": "Which tool in the Modify Features pane allows an editor to eliminate sliver gaps between adjacent polygon boundaries by conforming an edge to match another layer's coincident path within a tolerance?",
            "ar": "أي أداة في نافذة Modify Features تتيح للمحرر إزالة فجوات الشرائح البينية (Sliver Gaps) بين حدود المضلعات المتجاورة بمطابقة حافة لتتبع مسار طبقة أخرى ضمن مسافة تسامح؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Align Edge", "ar": "Align Edge (محاذاة الحافة)"}},
            {"id": "B", "text": {"en": "Simplify", "ar": "Simplify (التبسيط)"}},
            {"id": "C", "text": {"en": "Buffer", "ar": "Buffer (النطاق)"}},
            {"id": "D", "text": {"en": "Clip", "ar": "Clip (القص)"}}
        ],
        "correctAnswer": "A",
        "explanation": {
            "en": "Align Edge conforms a selected polygon or polyline edge to match an adjacent target edge within a specified search tolerance distance, cleanly closing sliver gaps or overlaps without editing individual vertices manually.",
            "ar": "تطابق أداة Align Edge حافة مضلع أو خط محددة مع حافة مستهدفة مجاورة ضمن مسافة بحث محددة، مما يغلق الفجوات والتداخلات الشريطية بدقة دون الحاجة لتحريك الرؤوس يدوياً."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "B": "Simplify reduces vertex density to generalize shapes.",
                "C": "Buffer creates distance zones around features.",
                "D": "Clip cuts layers by a boundary or clips editing sketches."
            },
            "ar": {
                "B": "أداة Simplify تقلل كثافة الرؤوس لتعميم الأشكال.",
                "C": "أداة Buffer تنشئ مناطق حرم بمسافات محددة حول المعالم.",
                "D": "أداة Clip تقطع المعالم بناءً على حدود مضلع آخر."
            }
        },
        "references": [{"title": "Align an edge, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/help/editing/align-an-edge.htm", "kind": "official"}]
    },
    {
        "id": "DM-059", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Technical", "tools": ["Generalize"],
        "question": {
            "en": "Which simplification algorithm in the Generalize / Simplify Polygon tool is best suited for retaining natural geographic bends (such as river meanders or coastlines) while reducing vertex count?",
            "ar": "أي خوارزمية تبسيط في أداة Generalize / Simplify Polygon هي الأنسب للحفاظ على الانحناءات الجغرافية الطبيعية (مثل تعرجات الأنهار أو السواحل) مع تقليل عدد الرؤوس؟"
        },
        "options": [
            {"id": "A", "text": {"en": "Point Remove (Douglas-Peucker)", "ar": "Point Remove (دوغلاس-بيكر)"}},
            {"id": "B", "text": {"en": "Bend Simplify (Wang-Müller)", "ar": "Bend Simplify (وانغ-مولر)"}},
            {"id": "C", "text": {"en": "Weighted Average", "ar": "Weighted Average (المتوسط الموزون)"}},
            {"id": "D", "text": {"en": "Nearest Neighbor", "ar": "Nearest Neighbor (الجار الأقرب)"}}
        ],
        "correctAnswer": "B",
        "explanation": {
            "en": "Bend Simplify (based on the Wang-Müller algorithm) detects significant geometric bends and simplifies them while preserving natural curvature and aesthetic cartographic fidelity, unlike Point Remove which tends to produce angular zigzags.",
            "ar": "تتعرف خوارزمية Bend Simplify (المستندة إلى وانغ-مولر) على الانحناءات الهندسية الهامة وتبسطها مع الحفاظ على التعرجات الطبيعية والجمالية الكارتوغرافية، على عكس خوارزمية دوغلاس-بيكر التي تميل لإنتاج زوايا حادة."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "A": "Point Remove (Douglas-Peucker) simplifies based on perpendicular distance tolerance, which often flattens or creates sharp angular bends on natural features.",
                "C": "Weighted Average is a geodatabase merge policy, not a geometry simplification algorithm.",
                "D": "Nearest Neighbor is a raster resampling method, not a vector simplification algorithm."
            },
            "ar": {
                "A": "طريقة Point Remove (دوغلاس-بيكر) تبسط بالمسافة العمودية وغالباً ما تشوه التعرجات الطبيعية وتنتج زوايا حادة.",
                "C": "المتوسط الموزون هو سياسة دمج سمات وليس خوارزمية تبسيط هندسي.",
                "D": "الجار الأقرب هي طريقة استعيان راستر وليست خوارزمية تبسيط اتجاهي."
            }
        },
        "references": [{"title": "Simplify Polygon, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/cartography/simplify-polygon.htm", "kind": "official"}]
    },
    {
        "id": "DM-060", "kind": "mcq", "domain": "Data Management",
        "objective": "Manage geospatial data (raster, vector, tabular)",
        "difficulty": "Intermediate", "type": "Tool-based", "tools": ["Smooth Polygon"],
        "question": {
            "en": "Which algorithm in the Smooth Polygon tool uses a polynomial approximation to produce aesthetically pleasing organic curves without altering the overall position of vertices dramatically?",
            "ar": "أي خوارزمية في أداة Smooth Polygon تستخدم تقريباً متعدد الحدود (Polynomial Approximation) لإنتاج منحنيات انسيابية جمالية دون إزاحة مواضع الرؤوس بشكل كبير؟"
        },
        "options": [
            {"id": "A", "text": {"en": "PAEK (Polynomial Approximation with Exponential Kernel)", "ar": "PAEK (التقريب متعدد الحدود ذو النواة الأسية)"}},
            {"id": "B", "text": {"en": "Bilinear Resampling", "ar": "Bilinear Resampling"}},
            {"id": "C", "text": {"en": "Euclidean Allocation", "ar": "Euclidean Allocation"}},
            {"id": "D", "text": {"en": "Inverse Distance Weighted", "ar": "Inverse Distance Weighted"}}
        ],
        "correctAnswer": "A",
        "explanation": {
            "en": "PAEK (Polynomial Approximation with Exponential Kernel) calculates smooth curves that gently follow original vertices using polynomial equations with exponential weight, yielding organic cartographic lines.",
            "ar": "تحسب خوارزمية PAEK منحنيات ناعمة تتبع الرؤوس الأصلية بسلاسة باستخدام معادلات متعددة الحدود بوزن أسي، مما يعطي خطوطاً كارتوغرافية انسيابية وطبيعية."
        },
        "incorrectOptionsExplanation": {
            "en": {
                "B": "Bilinear resampling is an image processing technique for continuous raster grids.",
                "C": "Euclidean Allocation is a distance analysis tool for raster proximity surfaces.",
                "D": "Inverse Distance Weighted (IDW) is a surface interpolation technique."
            },
            "ar": {
                "B": "إعادة استعيان Bilinear هي تقنية معالجة صور لشبكات الراستر المستمرة.",
                "C": "أداة Euclidean Allocation هي أداة تحليل مسافات لأسطح التقارب.",
                "D": "طريقة IDW هي تقنية استيفاء أسطح وليست لتنعيم الخطوط."
            }
        },
        "references": [{"title": "Smooth Polygon, ArcGIS Pro documentation", "url": "https://pro.arcgis.com/en/pro-app/latest/tool-reference/cartography/smooth-polygon.htm", "kind": "official"}]
    }
]

target_file = 'public/data/questions/data-management.json'
with open(target_file, 'r', encoding='utf-8') as f:
    existing = json.load(f)

existing_ids = set(q['id'] for q in existing)
to_add = [q for q in dm_51_60 if q['id'] not in existing_ids]

combined = existing + to_add
combined.sort(key=lambda x: int(x['id'].split('-')[1]))

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

print(f"DM 51-60 added. Total DM questions now: {len(combined)} (target 80).")

