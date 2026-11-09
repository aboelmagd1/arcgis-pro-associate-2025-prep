# -*- coding: utf-8 -*-
"""
Generate all 38 Visualization Scenarios (VIZ-S-001 through VIZ-S-038) for EAPA_2025.
"""
import json
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target_file = os.path.join(base_dir, 'public', 'data', 'scenarios', 'visualization.json')

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

def s(sid, obj, diff, qtype, tools, ctx_en, ctx_ar, q_en, q_ar, opts, ans, exp_en, exp_ar, why, rkey):
    return {
        "id": sid,
        "kind": "scenario",
        "domain": "Visualization",
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

def unpack_item(item, qid):
    if len(item) == 14:
        return (qid, item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13])
    elif len(item) == 12:
        full_en = item[4].strip()
        full_ar = item[5].strip()
        
        idx_en = full_en.rfind('. ')
        if idx_en == -1:
            idx_en = full_en.rfind('? ')
        if idx_en != -1 and '?' in full_en[idx_en:]:
            ctx_en = full_en[:idx_en+1].strip()
            q_en = full_en[idx_en+1:].strip()
        else:
            ctx_en = full_en
            q_en = "Which configuration or tool satisfies this requirement?"
            
        idx_ar = full_ar.rfind('. ')
        if idx_ar == -1:
            idx_ar = full_ar.rfind('؛ ')
        if idx_ar == -1:
            idx_ar = full_ar.rfind('؟ ')
        if idx_ar != -1 and ('؟' in full_ar[idx_ar:] or '?' in full_ar[idx_ar:]):
            ctx_ar = full_ar[:idx_ar+1].strip()
            q_ar = full_ar[idx_ar+1:].strip()
        else:
            ctx_ar = full_ar
            q_ar = "ما هي الأداة أو الإعداد المناسب لتحقيق هذا المتطلب؟"
            
        return (qid, item[0], item[1], item[2], item[3], ctx_en, ctx_ar, q_en, q_ar, item[6], item[7], item[8], item[9], item[10], item[11])
    else:
        raise ValueError(f"Unknown len: {len(item)}")

items = []

viz_scenarios_data = [
    # 1: Multi-story building interior range filtering
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Tool-based", ["Range Slider"],
        "An airport facilities management team maintains a 3D building model containing thousands of interior asset points (security cameras, gates, HVAC sensors) across 5 terminal floors. When viewing the entire building, assets from all floors overlap into an unreadable vertical cluster.",
        "يدير فريق مرافق المطار نموذج مبنى ثلاثي الأبعاد يحتوي على آلاف الأصول الداخلية (كاميرات المراقبة، البوابات، حساسات التكييف) موزعة على 5 طوابق؛ وعند عرض المبنى ككل، تتداخل أصول كافة الطوابق في كتلة رأسية متزاحمة غير مقروءة.",
        "How can the facilities team configure ArcGIS Pro to interactively isolate and display assets on Floor 3 only?",
        "كيف يمكن لفريق المرافق تهيئة ArcGIS Pro لعزل وعرض أصول الطابق الثالث تفاعلياً فقط؟",
        [["Enable Range on the layer properties using the FLOOR_NUMBER integer field and activate the on-screen Range Slider", "تفعيل خاصية Range في خصائص الطبقة باستخدام حقل FLOOR_NUMBER الرقمي وتشغيل منزلق المدى (Range Slider)"], ["Set a static definition query FLOOR_NUMBER = 3 permanently on all layers", "ضبط استعلام تعريفي ثابت FLOOR_NUMBER = 3 بشكل دائم على جميع الطبقات"], ["Convert the 3D scene to a 2D map view", "تحويل المشهد ثلاثي الأبعاد إلى خريطة ثنائية الأبعاد"], ["Delete assets on floors 1, 2, 4, and 5", "حذف أصول الطوابق 1 و 2 و 4 و 5"]],
        "A",
        "The Range Slider enables interactive filtering of features based on any continuous or discrete numeric attribute (such as building floor levels, pipe pressure, or depth), allowing users to step floor-by-floor dynamically.",
        "يتيح منزلق المدى (Range Slider) تصفية المعالم تفاعلياً بناءً على أي حقل رقمي (مثل طوابق المباني، أو مستويات العمق، أو الضغط)، مما يمكن المستخدمين من التنقل طابقاً بطابق ديناميكياً دون تعديل البيانات.",
        {"B": ["A static definition query requires opening properties dialogs repeatedly to change floors.", "الاستعلام الثابت يتطلب فتح نافذة الخصائص يدوياً في كل مرة لتغيير الطابق."], "C": ["Converting to 2D loses spatial floor separation entirely.", "التحويل للثنائي يفقد التمايز المكاني للطوابق."], "D": ["Deleting assets permanently destroys corporate facility inventory.", "حذف الأصول يدمر قاعدة بيانات المرافق."]},
        "time"
    ),
    # 2: Sunlight shadow analysis for proposed high-rise
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Technical", ["3D Scenes", "Illumination"],
        "A city planning commission evaluates a proposed 60-story skyscraper to assess whether its afternoon shadow will fall across a public historic park on the Winter Solstice (December 21) at 3:00 PM.",
        "تقيم لجنة تخطيط المدينة برجاً مقترحاً بارتفاع 60 طابقاً لتقييم ما إذا كان ظله في فترة بعد الظهيرة سيسقط على حديقة تاريخية عامة في يوم الانقلاب الشتوي (21 ديسمبر) عند الساعة 3:00 مساءً.",
        "How should the GIS analyst configure the 3D Scene in ArcGIS Pro to perform this visual impact assessment accurately?",
        "كيف يجب على محلل نظم المعلومات الجغرافية تهيئة المشهد ثلاثي الأبعاد في ArcGIS Pro لإجراء هذا التقييم البصري بدقة؟",
        [["Enable Sun Lighting and Shadows on the Scene illumination properties, and set the calendar date to December 21 and clock time to 3:00 PM", "تفعيل إضاءة الشمس والظلال (Sun Lighting and Shadows) في خصائص إضاءة المشهد، وضبط التاريخ على 21 ديسمبر والساعة على 3:00 مساءً"], ["Apply a transparent yellow color ramp to the building footprint", "تطبيق تدرج لوني أصفر شفاف على مسقط المبنى"], ["Run the Buffer tool with a 500-meter radius around the park", "تشغيل أداة Buffer بمسافة 500 متر حول الحديقة"], ["Convert the building polygon into a TIN surface", "تحويل مضلع المبنى إلى سطح TIN"]],
        "A",
        "ArcGIS Pro 3D Scenes include solar illumination models that calculate precise real-world solar azimuth and elevation angles for any geographic location, date, and time, accurately casting realistic shadows across terrain and 3D buildings.",
        "تتضمن المشاهد ثلاثية الأبعاد بـ ArcGIS Pro نماذج إضاءة شمسية تحسب زوايا السمت والارتفاع الشمسي الحقيقي لأي موقع جغرافي وتاريخ وساعة بدقة، مما يلقي ظلالاً واقعية تماماً للمباني على التضاريس والحدائق.",
        {"B": ["Color ramps only alter surface painting, not directional solar shadows.", "تدرج الألوان يلون الأسطح فقط ولا يحسب الظلال."], "C": ["Buffers represent arbitrary proximity distances, not solar shadow lengths.", "النطاق مسافة ثابتة ولا يمثل أطوال الظلال الشمسية."], "D": ["TIN surfaces model terrain elevations, not building shadow projections.", "أسطح TIN للتضاريس وليست لمجسمات المباني."]},
        "scenes"
    ),
    # 3: Wildfire progression temporal animation
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Workflow-based", ["Time Slider"],
        "An emergency management agency tracks a major forest wildfire that has burned across multiple counties over two weeks. The fire boundary dataset contains START_TIME and END_TIME timestamp fields recording the dynamic perimeter progression every 6 hours.",
        "تتابع هيئة طوارئ حريق غابات ضخماً امتد عبر عدة مقاطعات على مدى أسبوعين؛ وتحتوي بيانات حدود الحريق على حقلي تواريخ START_TIME و END_TIME تسجلان توسع محيط الحريق كل 6 ساعات.",
        "How should the analyst configure the layer so the fire's continuous spatial expansion animates smoothly on the map view?",
        "كيف يجب على المحلل تهيئة الطبقة بحيث تظهر حركة وتوسع محيط الحريق كرسوم متحركة متصلة وسلسة على الخريطة؟",
        [["In Layer Properties > Time, select 'Each feature has start and end time fields', and set the Time Slider step interval to 6 Hours", "في Layer Properties > Time، اختيار 'Each feature has start and end time fields'، وضبط خطوة منزلق الوقت على 6 ساعات"], ["Create 56 individual definition queries manually", "إنشاء 56 استعلاماً تعريفياً يدوياً منفصلاً"], ["Convert the vector perimeters to static CAD drawings", "تحويل الحدود الاتجاهية إلى رسومات CAD ثابتة"], ["Set the layer transparency to 100% and export to GIF", "ضبط شفافية الطبقة على 100% وتصديرها بصيغة GIF"]],
        "A",
        "Configuring 'start and end time fields' enables ArcGIS Pro to display features continuously over their active duration, and setting the Time Slider step to match data sampling frequency (6 hours) produces fluid chronological playback.",
        "يتيح اختيار 'حقول بداية ونهاية' لـ ArcGIS Pro عرض المعالم طوال فترة نشاطها الفعالة، وضبط خطوة منزلق الوقت لتطابق وتيرة الرصد (6 ساعات) يمنح عرضاً متحركاً سلساً لتقدم جبهة الحريق.",
        {"B": ["Manual definition queries cannot produce continuous animated playback.", "الاستعلامات اليدوية لا تنتج عرضاً متحركاً متصلاً."], "C": ["CAD drawings lose interactive temporal playback controls.", "رسومات CAD تفقد التحكم الزمني."], "D": ["100% transparency makes the fire completely invisible.", "الشفافية الكاملة تخفي الحريق تماماً."]},
        "time"
    ),
    # 4: Hillshade overlay with Multiply blending mode
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Layer Blending"],
        "A cartographer designs a topographic recreation map by overlaying a vibrant categorical Land Cover polygon layer directly above a grayscale Hillshade raster. When using standard 50% layer transparency, the land cover colors appear faded, washed out, and milky.",
        "يصمم رسام خرائط خريطة سياحية بوضع طبقة استخدامات غطاء أرضي ملونة فوق راستر تظليل تضاريسي (Hillshade)؛ وعند تطبيق شفافية 50% العادية، بدت ألوان الغطاء الأرضي باهتة ومغبرة وفاقدة للحيوية.",
        "What layer blending technique restores rich, fully saturated colors while allowing terrain shadows and textures to show through clearly?",
        "ما هي تقنية دمج الطبقات التي تستعيد تشبع الألوان وحيويتها الكاملة مع إبراز ظلال وتفاصيل التضاريس بوضوح فائق؟",
        [["Set the Land Cover layer's Blend Mode to 'Multiply' on the Appearance ribbon tab", "ضبط نمط دمج الطبقة (Blend Mode) للغطاء الأرضي على 'Multiply' في تبويب Appearance"], ["Convert the hillshade to a binary black-and-white grid", "تحويل راستر التضاريس إلى شبكة ثنائية بالأبيض والأسود فقط"], ["Increase the computer monitor contrast to 100%", "زيادة تباين شاشة الحاسوب إلى 100%"], ["Export the map to a black-and-white TIFF file", "تصدير الخريطة إلى ملف TIFF أحادي اللون"]],
        "A",
        "The Multiply blend mode multiplies the color values of the top layer with the bottom layer. Whites become transparent while darker shadows from the hillshade darken the land cover tones without washing out color saturation.",
        "يقوم نمط الدمج Multiply بضرب قيم ألوان الطبقة العليا بالطبقة السفلى؛ فتصبح المساحات البيضاء شفافة تماماً وتبرز ظلال التضاريس ألوان الغطاء الأرضي دون إضعاف تشبعها اللوني أو جعلها باهتة.",
        {"B": ["Binary grids lose all continuous elevation shadow shading.", "الشبكات الثنائية تفقد التدرجات التضاريسية."], "C": ["Hardware monitor tweaks do not fix exported digital cartography.", "تعديل الشاشة لا يصلح الملف المصدر."], "D": ["Monochrome TIFF removes all color information.", "ملف TIFF الأحادي يلغي كافة الألوان."]},
        "blending"
    ),
    # 5: High-density parcel label conflict resolution
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Workflow-based", ["Maplex Label Engine"],
        "In a dense urban tax mapping project, parcel polygons are too narrow for standard parcel identification numbers (PINs) to fit horizontally at 10pt font, causing hundreds of parcels to remain completely unlabeled.",
        "في مشروع خرائط عقارية حضرية كثيفة، تبين أن مضلعات قطع الأراضي ضيقة جداً بحيث لا تستوعب أرقام التعريف العقاري (PIN) أفقياً بخط 10pt، مما أدى لغياب التسميات عن مئات القطع.",
        "Which combination of Maplex fitting strategies should the cartographer enable to maximize label placement in tight parcels?",
        "أي مجموعة من استراتيجيات الملاءمة في محرك Maplex يجب على رسام الخرائط تفعيلها لزيادة ظهور التسميات في القطع الضيقة؟",
        [["Enable Stacking, allow Font Reduction down to 6pt, and allow Overrun beyond polygon boundaries", "تفعيل التكدس (Stacking)، والسماح بتقليص الخط (Font Reduction) حتى 6pt، والسماح بالتجاوز (Overrun) خارج الحدود"], ["Delete small parcels from the map view", "حذف قطع الأراضي الصغيرة من الخريطة"], ["Turn off the Maplex Label Engine and revert to the Standard engine", "إلغاء تفعيل محرك Maplex والعودة للمحرك القياسي القديم"], ["Rotate the map frame upside down", "قلب إطار الخريطة رأساً على عقب"]],
        "A",
        "Maplex provides ordered fitting strategies: Stacking splits text across multiple lines, Font Reduction scales text down to a specified minimum legibility limit, and Overrun allows text to extend slightly beyond polygon edges.",
        "يوفر محرك Maplex استراتيجيات ملاءمة تصاعدية: يقسم التكدس (Stacking) النص على عدة أسطر، ويقلص خيار Font Reduction حجم الخط تدريجياً لحد أدنى مقروء، ويسمح Overrun للنص بتجاوز حدود المضلع قليلاً لاستيعابه.",
        {"B": ["Deleting parcels corrupts legal cadastre representation.", "حذف الأراضي يدمر التمثيل العقاري."], "C": ["The Standard engine has inferior collision avoidance compared to Maplex.", "المحرك القديم أضعف بكثير من Maplex في حل النزاعات."], "D": ["Rotating frames does not resolve element density.", "تدوير الخريطة لا يحل مشكلة كثافة المعالم."]},
        "labeling"
    ),
    # 6: Symbology Masking for contour labels
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Symbology Masking"],
        "A topographic mapping specialist creates 10-foot elevation contour lines with elevation labels. Currently, the brown contour lines cut directly through the middle of the label numbers, reducing readability.",
        "أنشأ أخصائي خرائط تضاريسية خطوط كنتور بفاصل 10 أقدام مع تسميات رقمية للارتفاع؛ وتمر خطوط الكنتور البنية حالياً مباشرة عبر منتصف أرقام التسميات مما يعيق قراءتها.",
        "How can the specialist create clean visual cutouts in the contour lines behind the labels without physically breaking or deleting line features?",
        "كيف يمكن للأخصائي إنشاء تفريغ بصري نظيف في خطوط الكنتور خلف أرقام التسميات دون كسر أو حذف المعالم الخطية هندسياً؟",
        [["Configure Symbology Masking so the contour label class masks the contour line symbol layer", "تهيئة أقنعة الرموز (Symbology Masking) بحيث تحجب فئة تسميات الكنتور طبقة رموز الخطوط"], ["Use the Split tool to manually cut every contour line on either side of each label", "استخدام أداة Split لقطع كل خط كنتور يدوياً على جانبي التسميات"], ["Change the contour lines color to transparent", "تغيير لون خطوط الكنتور إلى اللون الشفاف"], ["Delete all contour lines that have labels", "حذف كافة خطوط الكنتور التي تحمل تسميات"]],
        "A",
        "Symbology Masking dynamically masks specified symbol layers behind labels or annotation, creating a crisp, non-destructive cartographic gap without splitting or altering the underlying vector geometry.",
        "تتيح ميزة أقنعة الرموز (Symbology Masking) حجب طبقات رموز معينة ديناميكياً خلف نصوص التسميات، مما ينشئ فراغاً بصرياً كارتوغرافياً نظيفاً دون الحاجة لقطع أو تشويه هندسة الخطوط الأصلية.",
        {"B": ["Manually cutting lines is destructive and permanently damages elevation line continuity.", "قطع الخطوط يدوياً مدمر لبيانات واستمرارية خطوط الكنتور."], "C": ["Transparent lines disappear entirely.", "الخطوط الشفافة تختفي كلياً."], "D": ["Deleting contours destroys contour data.", "حذف الكنتور يدمر البيانات التضاريسية."]},
        "symbology"
    ),
    # 7: Normalizing Choropleth map of crime incidents
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Conceptual", ["Symbology", "Normalization"],
        "A crime analyst creates a choropleth map of total burglaries by police precinct. Large suburban precincts with 100,000 residents show dark red (high crime), while dense downtown precincts with 10,000 residents show light yellow (low crime), even though downtown has a much higher crime rate per capita.",
        "أنشأ محلل جرائم خريطة كوربلث لإجمالي السرقات حسب أقسام الشرطة؛ فظهرت الأقسام الخارجية الكبيرة التي تضم 100,000 نسمة باللون الأحمر الداكن (جرائم مرتفعة)، بينما ظهرت الأقسام الحضرية المزدحمة التي تضم 10,000 نسمة باللون الأصفر الفاتح، رغم أن معدل الجريمة للفرد في وسط المدينة أعلى بكثير.",
        "How should the analyst adjust the Graduated Colors symbology to display an accurate, unbiased crime risk comparison?",
        "كيف يجب على المحلل تعديل رموز الألوان المتدرجة لعرض مقارنة دقيقة وغير متحيزة لمخاطر الجريمة؟",
        [["Normalize the burglary count field by the total population field to calculate burglaries per capita", "تطبيع (Normalize) حقل إجمالي السرقات بالقسمة على حقل إجمالي السكان لحساب معدل الجرائم لكل نسمة"], ["Switch from Graduated Colors to Unique Values", "التحويل من الألوان المتدرجة إلى القيم الفريدة (Unique Values)"], ["Increase the number of classes from 5 to 30", "زيادة عدد الفئات من 5 إلى 30 فئة"], ["Set all precinct boundaries to 0 line width", "ضبط سماكة خطوط حدود الأقسام على القيمة 0"]],
        "A",
        "Mapping raw counts across administrative zones with varying populations produces misleading maps because populous zones visually exaggerate totals. Normalizing raw counts by population produces true per-capita incidence rates.",
        "يؤدي تمثيل الأعداد الخام عبر مناطق إدارية متفاوتة السكان إلى خرائط مضللة بصرياً؛ ويعمل تطبيع الأعداد (قسمتها على عدد السكان) على حساب معدل الجريمة الحقيقي لكل فرد.",
        {"B": ["Unique Values is for qualitative categories, not numerical rates.", "القيم الفريدة للبيانات النوعية وليست للمعدلات الكمية."], "C": ["Increasing classes does not fix the raw count distortion.", "زيادة الفئات لا تعالج تشوه الأعداد الإجمالية."], "D": ["Line width is a border aesthetic.", "سماكة الحدود مظهر تجميلي."]},
        "symbology"
    ),
    # 8: Scale-based Display Filters for transportation network
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Display Filters"],
        "A regional highway department publishes a web-ready map. At regional scales (1:500,000), only Interstate freeways should be displayed; at city scales (1:50,000), both Interstates and Major Arterials should display; and at neighborhood scales (1:10,000), all roads including Local Streets must display. Crucially, all road records must remain accessible in the Attribute Table at every scale.",
        "تنشر إدارة طرق خريطة تفاعلية؛ ويجب عند مقياس 1:500,000 إظهار الطرق السريعة الدولية فقط، وعند 1:50,000 إظهار الطرق السريعة والشريانية معاً، وعند 1:10,000 إظهار كافة الطرق بما فيها المحلية، مع بقاء كافة الطرق متاحة في جدول البيانات في كل الأوقات.",
        "Which ArcGIS Pro layer capability satisfies this exact requirement?",
        "أي ميزة في طبقات ArcGIS Pro تلبي هذا المتطلب بدقة؟",
        [["Scale-based Display Filters", "فلاتر العرض المعتمدة على المقياس (Scale-based Display Filters)"], ["Definition Queries", "الاستعلامات التعريفية (Definition Queries)"], ["Delete Features tool", "أداة حذف المعالم (Delete Features)"], ["Spatial Join", "الضم المكاني (Spatial Join)"]],
        "A",
        "Scale-based Display Filters dynamically restrict which features draw at specified scale ranges using SQL clauses without filtering out features from attribute tables, selections, or analytical tools.",
        "تتحكم فلاتر العرض المعتمدة على المقياس (Display Filters) في رسم المعالم بصرياً وفق مقاييس واستعلامات SQL محددة دون استبعاد المعالم من جدول السمات أو أدوات التحليل أو التحديد.",
        {"B": ["Definition Queries filter data at the data source level, hiding records from attribute tables as well.", "يحجب الاستعلام التعريفي المعالم عن جدول البيانات وأدوات التحليل أيضاً."], "C": ["Deleting features permanently destroys road network data.", "حذف المعالم يدمر بيانات شبكة الطرق."], "D": ["Spatial Join appends attributes, it does not manage scale visibility.", "الضم المكاني يربط السمات ولا يدير الرؤية بالمقياس."]},
        "symbology"
    ),
    # 9: Select By Location flood damage assessment
    (
        "Given a scenario, apply a query", "Intermediate", "Tool-based", ["Select By Location"],
        "Following a hurricane storm surge, an emergency analyst has a polygon layer of inundated flood extents and a point layer of 45,000 residential building structures. The analyst needs to identify every building that experienced flooding, including buildings where water touched the property foundation boundary.",
        "بعد عاصفة إعصار، يمتلك محلل طوارئ طبقة مضلعات نطاق الفيضان وطبقة نقطية لـ 45,000 مبنى سكني؛ ويحتاج لتحديد كل مبنى تعرض للغمر بما في ذلك المباني التي لامست المياه أساساتها.",
        "Which spatial relationship rule in the Select By Location tool should be used with Input: Buildings and Selecting Features: Flood Extents?",
        "أي قاعدة علاقة مكانية في أداة Select By Location يجب استخدامها مع تحديد المدخلات: المباني، ومعالم التحديد: نطاق الفيضان؟",
        [["Intersect", "Intersect (تتقاطع)"], ["Are completely within", "Are completely within (تقع بالكامل داخل)"], ["Have their centroid in", "Have their centroid in (يقع مركزها في)"], ["Are identical to", "Are identical to (تتطابق مع)"]],
        "A",
        "The 'Intersect' relationship selects any feature that touches, crosses, or falls inside the selecting polygon boundary, capturing both fully inundated and edge-affected buildings.",
        "تحدد علاقة التقاطع (Intersect) أي معلم يلامس أو يقطع أو يقع داخل حدود مضلع التحديد، مما يشمل كافة المباني المغمورة بالكامل أو المتأثرة عند الحواف.",
        {"B": ["'Are completely within' misses edge buildings where water only touched part of the foundation.", "علاقة Completely within تهمل المباني الواقعة على حواف الغمر."], "C": ["Centroids may fall just outside the boundary for complex irregular footprints.", "المراكز قد تقع خارج النطاق للمباني غير المنتظمة."], "D": ["Points and polygons cannot have identical geometry.", "النقاط والمضلعات لا يمكن أن تتطابق هندسياً."]},
        "query"
    ),
    # 10: Compound SQL query for tax delinquent properties
    (
        "Given a scenario, apply a query", "Intermediate", "Technical", ["Select By Attributes"],
        "A county finance auditor needs to select commercial parcels where the property taxes are delinquent (DELINQUENT = 'Yes') AND the unpaid tax balance exceeds $25,000, OR where the property is currently under active tax foreclosure (FORECLOSURE = 'Active').",
        "يحتاج مدقق مالي لتحديد قطع الأراضي التجارية التي تأخر سداد ضرائبها (DELINQUENT = 'Yes') وتجاوزت المبالغ غير المسددة 25,000 دولار، أو العقارات الواقعة تحت الحجز الضريبي النشط (FORECLOSURE = 'Active').",
        "Which SQL clause enforces correct logical operator precedence for this selection?",
        "أي جملة SQL تفرض أسبقية العمليات المنطقية الصحيحة لهذا التحديد؟",
        [["(DELINQUENT = 'Yes' AND UNPAID_TAX > 25000) OR FORECLOSURE = 'Active'", "(DELINQUENT = 'Yes' AND UNPAID_TAX > 25000) OR FORECLOSURE = 'Active'"], ["DELINQUENT = 'Yes' OR UNPAID_TAX > 25000 AND FORECLOSURE = 'Active'", "DELINQUENT = 'Yes' OR UNPAID_TAX > 25000 AND FORECLOSURE = 'Active'"], ["DELINQUENT, FORECLOSURE = 'Yes', 'Active' > 25000", "DELINQUENT, FORECLOSURE = 'Yes', 'Active' > 25000"], ["SELECT WHERE TAXES DELINQUENT AND FORECLOSED", "SELECT WHERE TAXES DELINQUENT AND FORECLOSED"]],
        "A",
        "In SQL evaluation, parentheses explicitly group the AND conditions together, ensuring the OR condition correctly captures active foreclosures regardless of balance.",
        "في تقييم استعلامات SQL، تعمل الأقواس على تجميع شروط AND معاً بشكل صريح، مما يضمن تقييم شرط OR البديل بشكل صحيح ومستقل.",
        {"B": ["Without parentheses, AND binds more tightly than OR, producing unexpected evaluation logic.", "بدون أقواس، يرتبط المعامل AND بقوة أكبر من OR مما يعطي نتائج مغلوطة."], "C": ["SQL does not permit combined field syntax.", "لا تسمح SQL بدمج أسماء الحقول."], "D": ["This is natural language prose, not valid SQL.", "هذه لغة نصية عامة وليست استعلام SQL."]},
        "query"
    )
]



# Generate remaining 28 scenarios (VIZ-S-011 to VIZ-S-038) to reach 38 total
more_viz_scenarios = [
    # 11: 3D Extrusion base height vs height field
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Technical", ["Extrusion"],
        "An urban designer extrudes 2D building footprints in a 3D Local Scene. The building polygons currently float above the terrain or sink into the hillside.",
        "قام مصمم عمراني ببثق مساقط مبانٍ ثنائية الأبعاد في مشهد محلي؛ فظهرت المباني تطفو في الهواء أو تغوص داخل التلال.",
        "How should the layer's elevation properties be configured so that the bottom of each building anchors cleanly to the hillside terrain?",
        "كيف يجب ضبط خصائص ارتفاع الطبقة بحيث تستند قاعدة كل مبنى بثبات على سطح الأرض التضاريسي المنحدر؟",
        [["Set Elevation to 'On the ground' and Extrusion method to 'Base height'", "ضبط الارتفاع على 'On the ground' وطريقة البثق على 'Base height'"], ["Set Elevation to 'At an absolute height' of 0 meters", "ضبط الارتفاع على 'At an absolute height' بقيمة 0 متر"], ["Delete the hillshade surface", "حذف سطح التظليل التضاريسي"], ["Change the building color to green", "تغيير لون المباني إلى الأخضر"]],
        "A",
        "Draping the feature base 'On the ground' allows vertices to follow the terrain elevation surface, while extruding from 'Base height' projects vertical walls upward from the ground.",
        "تثبيت قاعدة المعلم على 'On the ground' يجعل القواعد تتبع سطح التضاريس، بينما يبثق خيار 'Base height' الجدران رأسياً من منسوب الأرض للأعلى.",
        {"B": ["Absolute height places all bases at a flat horizontal plane, cutting through hills.", "الارتفاع المطلق يضع المباني في مستوى أفقي مستوٍ فيخترق التلال."], "C": ["Deleting hillshade does not fix 3D elevation offsets.", "حذف التظليل لا يصلح أخطاء الارتفاع."], "D": ["Color changes do not alter 3D geometric elevations.", "تغيير الألوان لا يغير المناسيب ثلاثية الأبعاد."]},
        "scenes"
    ),
    # 12: Diverging color ramp for election margins
    (
        "Manage layer properties using the ribbon and dialog boxes", "Beginner", "Conceptual", ["Symbology"],
        "A political analyst visualizes presidential election victory margins by county, where positive percentages indicate Party A wins and negative percentages indicate Party B wins, with 0% representing an exact tie.",
        "يصمم محلل سياسي خريطة لفوارق نتائج الانتخابات الرئاسية حسب المقاطعات، حيث تمثل النسب الموجبة فوز الحزب أ والنسب السالبة فوز الحزب ب ونسبة 0% تمثل التعادل التام.",
        "Which type of color ramp is cartographically appropriate for this dataset?",
        "أي نوع من مدرجات الألوان هو الأنسب كارتوغرافياً لتمثيل هذه البيانات؟",
        [["A Diverging color ramp (e.g. Blue to Neutral Gray to Red centered at 0%)", "مدرج ألوان متباعد (Diverging) مثل أزرق - رمادي محايد - أحمر متمحور حول 0%"], ["A Sequential single-hue ramp from light yellow to dark yellow", "مدرج ألوان متسلسل أحادي اللون من الأصفر الفاتح إلى الداكن"], ["A random qualitative pastel palette", "بالتة ألوان نوعية عشوائية"], ["A solid black monochrome fill", "تعبئة أحادية باللون الأسود المصمت"]],
        "A",
        "Diverging color ramps emphasize values departing in two opposite directions from a critical central midpoint (such as zero, an average, or a tie threshold).",
        "تركز مدرجات الألوان المتباعدة (Diverging) على إبراز التباين في اتجاهين متعاكسين انطلاقاً من نقطة وسطية حرجة (كالصفر أو المتوسط أو التعادل).",
        {"B": ["Sequential ramps only show variation in a single direction without a midpoint.", "المدرجات المتسلسلة تعرض اتجاهاً واحداً دون نقطة تعادل."], "C": ["Qualitative palettes are for unranked nominal categories.", "البالتات النوعية للفئات الاسمية."], "D": ["Solid black obscures all data variation.", "اللون الأسود يخفي تباين البيانات."]},
        "symbology"
    ),
    # 13: Feature Blending for incident hotspots
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Feature Blending"],
        "A public safety department symbolizes 911 emergency calls as overlapping semi-transparent circles. The analyst wants areas with heavy concentrations of calls to visually intensify and glow brighter where circles overlap.",
        "يمثل قسم السلامة العامة بلاغات الطوارئ بدوائر نصف شفافة متداخلة؛ ويريد المحلل إبراز المناطق كثيفة البلاغات بصرياً لتتوهج وتزداد سطوعاً وكثافة مع تداخل الدوائر.",
        "Which layer visual effect should be configured?",
        "أي تأثير بصري للطبقة يجب تهيئته لتحقيق هذا التوهج التراكمي؟",
        [["Feature Blending (e.g. Screen or Lighten mode)", "دمج المعالم Feature Blending (بنمط Screen أو Lighten)"], ["Layer Blending Multiply mode", "نمط الدمج Multiply للطبقة"], ["Display Filter scale thresholds", "فلاتر العرض بالمقياس"], ["Definition Query on Call_ID", "استعلام تعريفي على حقل المعرف"]],
        "A",
        "Feature Blending blends overlapping features within the same layer together, allowing overlapping transparent elements to accumulate color density or light intensity into dynamic hotspots.",
        "يطبق دمج المعالم (Feature Blending) خوارزميات المزج اللوني بين المعالم المتداخلة داخل نفس الطبقة، مما يسمح للدوائر الشفافة بمراكمة الكثافة والتوهج في بؤر التركز.",
        {"B": ["Layer Blending blends between different layers, not between features of the same layer.", "دمج الطبقات يمزج بين طبقات مختلفة وليس بين معالم نفس الطبقة."], "C": ["Display filters hide features by scale.", "فلاتر العرض تخفي المعالم بالمقياس."], "D": ["Definition queries filter out records.", "الاستعلامات التعريفية تستبعد السجلات."]},
        "blending"
    ),
    # 14: Arcade Label expression with conditional logic
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical", ["Labeling", "Arcade"],
        "An analyst needs road labels to display the highway name in bold uppercase if it is an Interstate (e.g. '<BOL>' + Upper($feature.NAME) + '</BOL>'), but display ordinary title case text for local streets.",
        "يحتاج محلل لتسميات الطرق لعرض اسم الطريق السريع بخط عريض وحروف كبيرة إذا كان طريقاً دولياً، وعرضه بنص عادي للشوارع المحلية.",
        "What tool or capability allows writing conditional if/else expressions to author advanced labels?",
        "ما الأداة أو الإمكانية التي تتيح كتابة شروط if/else البرمجية لصياغة تسميات متقدمة؟",
        [["Arcade Label Expression in the Label Class properties", "تعبير تسمية Arcade في خصائص فئة التسمية (Label Class)"], ["Convert Labels to CAD tool", "أداة تحويل التسميات إلى CAD"], ["Spatial Join geoprocessing tool", "أداة الضم المكاني Spatial Join"], ["Calculate Geometry Attributes", "حساب السمات الهندسية"]],
        "A",
        "Arcade label expressions support full conditional logic (IIf, When, if/else blocks) and text formatting tags (such as `<BOL>`, `<CLR>`, `<FNT>`) to dynamically style labels based on attributes.",
        "تدعم تعبيرات التسمية بلغة Arcade الشروط المنطقية الكاملة (IIf, When, if/else) ووسوم التنسيق النصي (مثل `<BOL>` للعريض) لتنسيق التسميات ديناميكياً وفق سمات المعالم.",
        {"B": ["Converting to CAD exports static graphics.", "التحويل إلى CAD يصدر رسومات ثابتة."], "C": ["Spatial Join is a spatial overlay tool.", "الضم المكاني يربط البيانات."], "D": ["Calculate Geometry Attributes writes coordinates to tables.", "حساب السمات الهندسية يكتب إحداثيات في الجداول."]},
        "labeling"
    ),
    # 15: Maplex Label Stacking Separators
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical", ["Maplex Label Engine"],
        "In a layout, street labels like 'Martin Luther King Jr. Boulevard' are too long for one line. A cartographer wants Maplex to break long names onto multiple lines, but only at spaces or hyphens.",
        "في لوحة إخراج، كانت أسماء الشوارع الطويلة تتجاوز السطر الواحد؛ ويريد رسام الخرائط تجزئة الأسماء الطويلة على عدة أسطر عند المسافات أو الشرطات فقط.",
        "Which Maplex labeling strategy and parameter manages this multi-line splitting behavior?",
        "أي استراتيجية ملاءمة ومعامل في محرك Maplex يدير سلوك التجزئة على أسطر متعددة؟",
        [["Stack label (Stacking) with designated stacking separator characters", "تكدس التسميات (Stacking) مع تحديد أحرف فاصلة للتكدس"], ["Font Reduction to 1pt", "تقليص الخط إلى 1pt"], ["Key Numbering without legend", "ترقيم المفاتيح بدون جدول"], ["Remove all labels from the map", "حذف كافة التسميات من الخريطة"]],
        "A",
        "Label Stacking splits long labels across multiple lines based on defined separator characters (spaces, commas, hyphens) and maximum characters per line.",
        "تسمح خاصية تكدس التسميات (Label Stacking) بتقسيم النصوص الطويلة على أسطر متعددة بناءً على أحرف فصل محددة (المسافات والشرطات) والحد الأقصى لعدد المحارف في كل سطر.",
        {"B": ["1pt font is illegible to humans.", "خط 1pt غير مقروء إطلاقاً."], "C": ["Key numbering without a legend leaves numbers unexplained.", "الترقيم بلا مفتاح يفقد النص معناه."], "D": ["Removing labels defeats cartographic communication.", "حذف التسميات يلغي التواصل الكارتوغرافي."]},
        "labeling"
    ),
    # 16: Voxel Layer multidimensional slicing
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Advanced", "Conceptual", ["3D Scenes"],
        "An oceanographer visualizes a 4D NetCDF dataset containing ocean temperatures across latitude, longitude, depth, and time in an ArcGIS Pro Local Scene.",
        "يستعرض باحث علوم بحار بيانات NetCDF رباعية الأبعاد لدرجات حرارة المحيطات عبر خطوط الطول والعرض والعمق والزمن في مشهد محلي بـ ArcGIS Pro.",
        "Which tool or capability allows interactive slicing through the 3D volume to reveal internal temperature cores?",
        "ما الأداة أو الإمكانية التي تتيح إحداث قطاعات تفاعلية عبر الكتلة الحجمية ثلاثية الأبعاد لكشف بؤر الحرارة الداخلية؟",
        [["Voxel Layer with Slicing and Isosurface tools", "طبقة الفوكسل (Voxel Layer) باستخدام أدوات القطاع (Slicing) وأسطح التساوي (Isosurfaces)"], ["2D Contour geoprocessing tool", "أداة خطوط الكنتور ثنائية الأبعاد"], ["Near tool with search radius", "أداة Near بنصف قطر بحث"], ["Clip tool on a shapefile", "أداة Clip على ملف shapefile"]],
        "A",
        "Voxel layers represent volumetric multidimensional NetCDF data as 3D discrete voxels, supporting interactive cross-sections, slicing planes, and isosurfaces in 3D scenes.",
        "تمثل طبقات الفوكسل (Voxel layers) البيانات الحجمية متعددة الأبعاد كمجسمات ثلاثية الأبعاد، وتدعم إجراء قطاعات تفاعلية واستخراج أسطح التساوي (Isosurfaces) داخل المشاهد ثلاثية الأبعاد.",
        {"B": ["2D contours only generate flat isolines.", "الكنتور ثنائي الأبعاد ينتج خطوطاً مستوية."], "C": ["Near measures point distances.", "أداة Near تقيس المسافات."], "D": ["Clip operates on vector boundaries.", "أداة Clip للمتجهات."]},
        "scenes"
    ),
    # 17: Dot Density symbology mechanics
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Conceptual", ["Symbology"],
        "A demographer symbolizes an agricultural census using Dot Density symbology where 1 dot represents 1,000 sheep. When zooming in and out on the map, the positions of individual dots shift slightly.",
        "مثل باحث ديموغرافي تعداد الثروة الحيوانية برموز كثافة النقط (Dot Density) بحيث تمثل كل نقطة 1,000 رأس ماشية؛ وعند التكبير والتصغير على الخريطة، لاحظ تحرك مواضع النقاط قليلاً.",
        "What explains this shifting dot behavior?",
        "ما هو التفسير العلمي الكارتوغرافي لتحرك مواضع هذه النقاط؟",
        [["Dot Density places dots randomly within each polygon at each redraw to represent overall density, not exact surveyed GPS animal positions", "توزع طريقة Dot Density النقاط عشوائياً داخل المضلع مع كل إعادة رسم لتمثيل الكثافة الإجمالية، وليست مواقع GPS حقيقية مساحة للحيوانات"], ["The geodatabase is corrupted", "قاعدة البيانات تالفة"], ["The graphics card is overheating", "بطاقة الرسوميات تعاني من حرارة مرتفعة"], ["The coordinate system datum is drifting", "مرجع نظام الإحداثيات يتحرك وينزاح"]],
        "A",
        "Dot density symbology distributes dots pseudorandomly inside polygon boundaries to convey visual density. The dots represent statistical aggregations rather than real geographic coordinates of individual features.",
        "توزع طريقة كثافة النقط (Dot Density) النقاط عشوائياً داخل حدود كل مضلع لتعبر بصرياً عن الكثافة الإحصائية؛ وهي تعبير رمزي كمي وليست إحداثيات مكانية حقيقية لكل مفردة.",
        {"B": ["Dot density behavior is normal software design, not data corruption.", "سلوك طبيعي للترميز وليس تلفاً بالبيانات."], "C": ["Hardware graphics heat does not control dot algorithms.", "حرارة العتاد لا تتحكم بالخوارزمية."], "D": ["Datums are mathematically fixed definitions.", "المراجع الإسنادية ثابتة رياضياً."]},
        "symbology"
    ),
    # 18: Definition query compound OR trap
    (
        "Given a scenario, apply a query", "Intermediate", "Troubleshooting", ["Definition Query"],
        "An analyst configures a Definition Query to display active permits in District 5: `DISTRICT = 5 AND STATUS = 'Active' OR STATUS = 'Pending'`. In the map, active permits from Districts 1, 2, 3, and 4 also appear.",
        "ضبط محلل استعلاماً تعريفياً لعرض التراخيص النشطة في المنطقة 5: `DISTRICT = 5 AND STATUS = 'Active' OR STATUS = 'Pending'`. فظهرت على الخريطة تراخيص نشطة من المناطق 1 و 2 و 3 و 4 أيضاً.",
        "What logical error exists in this query clause?",
        "ما هو الخطأ المنطقي الموجود في صياغة هذا الاستعلام؟",
        [["Missing parentheses around the OR condition: `DISTRICT = 5 AND (STATUS = 'Active' OR STATUS = 'Pending')`", "غياب الأقواس حول شرط OR: والصحيح `DISTRICT = 5 AND (STATUS = 'Active' OR STATUS = 'Pending')`"], ["The field names are spelled in uppercase", "كتابة أسماء الحقول بأحرف كبيرة"], ["SQL does not support the word AND", "لغة SQL لا تدعم كلمة AND"], ["The layer must be converted to raster format", "يجب تحويل الطبقة إلى راستر"]],
        "A",
        "In SQL precedence, AND takes priority over OR. The original query evaluates as (District 5 AND Active) OR (Any Pending permit in any district). Adding parentheses groups the statuses together under District 5.",
        "في أسبقية عمليات SQL، يسبق المعامل AND المعامل OR في التقييم؛ فالاستعلام الأصلي يظهر أي ترخيص معلق (Pending) في أي منطقة كانت. وإضافة الأقواس تضمن قصر كلا الحالتين على المنطقة 5 حصراً.",
        {"B": ["Case formatting in SQL field names does not alter boolean logic.", "حالة الأحرف لا تغير المنطق البولياني."], "C": ["AND is a fundamental core SQL operator.", "المعامل AND عنصر أساسي في SQL."], "D": ["Vector definition queries do not require rasters.", "الاستعلامات للمتجهات لا تتطلب راستر."]},
        "query"
    ),
    # 19: Maplex Repeat Label for long highways
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Maplex Label Engine"],
        "On a statewide road map layout, long interstate highway lines run across several feet of the printed map. Currently, each highway is labeled only once at its western start point, leaving the rest of the line unlabeled.",
        "في لوحة خريطة طرق للولاية، تمتد خطوط الطرق السريعة الطويلة لعدة أقدام على الخريطة المطبوعة؛ وتظهر التسمية حالياً مرة واحدة فقط عند بداية الطريق غرباً، ويبقى بقية الخط دون أي تسمية توضيحية.",
        "Which Maplex placement setting ensures highway labels repeat at regular distance intervals along the length of the road?",
        "أي إعداد في محرك Maplex يضمن تكرار تسميات الطرق السريعة على فواصل مسافات منتظمة بطول مسار الطريق؟",
        [["Repeat label with a specified distance interval", "تكرار التسمية (Repeat label) بمسافة فاصلة محددة"], ["Remove duplicates globally", "إزالة التكرار عالمياً"], ["Set font size to 72pt", "ضبط حجم الخط على 72pt"], ["Convert road layer to a point layer", "تحويل طبقة الطرق إلى نقاط"]],
        "A",
        "The Repeat Label placement property in Maplex allows labels on long polyline features to repeat at specified distance increments (e.g. every 500 millimeters on page or 50 miles in ground units).",
        "تسمح خاصية تكرار التسمية (Repeat Label) في محرك Maplex بتكرار نصوص التسميات على المعالم الخطية الطويلة بفواصل مسافات منتظمة (مثل كل 50 ميلاً) لتسهيل قراءة الخريطة عبر امتدادها الواسع.",
        {"B": ["Remove duplicates suppresses repeated labels, the exact opposite of what is needed.", "إزالة التكرار تخفي التسميات المكررة وهو عكس المطلوب."], "C": ["72pt font is massive and clutters the map.", "خط 72 ضخم جداً ويشوه الخريطة."], "D": ["Converting to points breaks line cartography.", "التحويل لنقاط يفقد خواص الخطوط."]},
        "labeling"
    ),
    # 20: Quantile classification skewed outliers
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Conceptual", ["Symbology", "Classification"],
        "An economist maps city household wealth using Quantile classification with 5 classes. A small billionaire enclave with extreme wealth ($100M+) is grouped into the exact same top 20% class as middle-class households earning $120,000.",
        "رسم خبير اقتصادي خريطة لثروات الأسر في المدينة بتصنيف Quantile ذي 5 فئات؛ فوُضعت أسر المليارديرات ذات الثروات الفائقة (+100 مليون دولار) في نفس فئة الـ 20% الأعلى مع أسر الطبقة المتوسطة ذات الدخل 120,000 دولار.",
        "Why did the Quantile classification mask these extreme wealth outliers?",
        "لماذا أخفت طريقة تصنيف Quantile هذه القيم الشاذة المتطرفة للثروة؟",
        [["Because Quantile distributes equal counts of features into each class regardless of numerical magnitude or natural data gaps", "لأن تصنيف Quantile يوزع أعداداً متساوية من المعالم في كل فئة بغض النظر عن الفروق الرقمية أو الفجوات الطبيعية في البيانات"], ["Because Quantile only works on percentage data", "لأن Quantile تعمل على النسب المئوية فقط"], ["Because the attribute field was stored as Double", "لأن الحقل مخزن بنوع Double"], ["Because the map coordinate system was projected", "لأن نظام إحداثيات الخريطة كان مسقطاً"]],
        "A",
        "Quantile groups equal counts of records (20% per class). It completely ignores data magnitude gaps and clusters, grouping extreme outliers into the same quantile bucket as typical adjacent values.",
        "تقسم طريقة Quantile المعالم إلى أعداد متساوية (20% في كل فئة)؛ وهي تتجاهل الفجوات الرقمية والتجمعات الطبيعية، مما يدمج القيم الشاذة المتطرفة في نفس الفئة مع القيم العادية المجاورة لها في الترتيب.",
        {"B": ["Quantile works on any numeric values.", "تعمل Quantile على كافة القيم الرقمية."], "C": ["Double fields store floating-point numbers accurately.", "نوع Double يخزن الأرقام بدقة."], "D": ["Map projections do not alter statistical classification.", "الإسقاط لا يغير التصنيف الإحصائي."]},
        "classification"
    ),
    # 21: Standard Deviation classification anomaly detection
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Classification"],
        "A public health researcher wants to highlight census tracts that have infant mortality rates significantly above or below the national average.",
        "يريد باحث صحة عامة إبراز مناطق التعداد التي تسجل معدلات وفيات رضع أعلى أو أقل بشكل ملحوظ من المتوسط الوطني العام.",
        "Which classification method classifies data based on multiples of standard deviation above and below the arithmetic mean?",
        "أي طريقة تصنيف تقسم البيانات بالاعتماد على مضاعفات الانحراف المعياري أعلى وأدنى المتوسط الحسابي؟",
        [["Standard Deviation", "الانحراف المعياري (Standard Deviation)"], ["Equal Interval", "الفترات المتساوية (Equal Interval)"], ["Manual Interval", "الفترات اليدوية (Manual Interval)"], ["Natural Breaks", "الكسور الطبيعية (Natural Breaks)"]],
        "A",
        "The Standard Deviation classification method shows how much a feature's attribute value varies from the mean, creating class breaks at intervals of 1, 0.5, or 0.33 standard deviations.",
        "توضح طريقة تصنيف الانحراف المعياري مدى تباعد قيم المعالم عن المتوسط الحسابي العام، وتنشئ فواصل فئات بفواصل 1 أو 0.5 انحراف معياري لإبراز الشذوذ الإحصائي.",
        {"B": ["Equal interval divides range evenly.", "الفترات المتساوية تقسم المدى بالتساوي."], "C": ["Manual interval requires typing breaks.", "الفترات اليدوية تتطلب إدخال الفواصل."], "D": ["Natural breaks clusters variance.", "الكسور الطبيعية تجمع التباين."]},
        "classification"
    ),
    # 22: Dictionary symbology for military emergency
    (
        "Manage layer properties using the ribbon and dialog boxes", "Advanced", "Conceptual", ["Symbology"],
        "An emergency response task force visualizes joint military and civilian search-and-rescue teams according to the MIL-STD-2525D standard, where symbols depend on echelon, identity, affiliation, and equipment codes.",
        "تعرض فرقة طوارئ مواقع فرق الإنقاذ العسكرية والمدنية المشتركة وفق معيار MIL-STD-2525D، حيث ترتهن الرموز بأكواد التبعية والرتبة ونوع المعدات.",
        "Which symbology renderer in ArcGIS Pro supports generating complex standardized multi-attribute composite symbols from rule dictionaries?",
        "أي محرك رموز في ArcGIS Pro يدعم توليد رموز مركبة معيارية معقدة متعددة السمات من قواميس القواعد؟",
        [["Dictionary Symbology", "رموز القاموس (Dictionary Symbology)"], ["Unique Values", "القيم الفريدة (Unique Values)"], ["Single Symbol", "الرمز المنفرد (Single Symbol)"], ["Heat Map", "الخريطة الحرارية (Heat Map)"]],
        "A",
        "Dictionary Symbology uses an external symbol dictionary to parse multiple attribute fields and synthesize complex, standardized military or emergency management symbols automatically.",
        "تستخدم رموز القاموس (Dictionary Symbology) قاموس رموز خارجياً لقراءة حقول سمات متعددة وتوليد رموز عسكرية أو طوارئ مركبة ومعيارية بشكل آلي متكامل.",
        {"B": ["Unique values only categorizes on individual field lists.", "القيم الفريدة تصنف بحقول منفردة محدودة."], "C": ["Single symbol uses one identical style.", "الرمز المنفرد يطبق نمطاً موحداً."], "D": ["Heat map renders density rasters.", "الخريطة الحرارية لكثافة النقط."]},
        "symbology"
    ),
    # 23: On-the-fly projection datum mismatch warning
    (
        "Identify how to control the coordinate system and geographic transformation in ArcGIS Pro", "Beginner", "Troubleshooting", ["Geographic Transformation"],
        "When adding a historical landmark layer based on the NAD 1927 datum into a project map set to NAD 1983 State Plane, ArcGIS Pro displays a notification stating that a transformation is missing.",
        "عند إضافة طبقة معالم تاريخية تعتمد على مرجع NAD 1927 إلى خريطة مشروع مضبوطة على State Plane NAD 1983، ظهر إشعار يفيد بغياب تحويل المرجع (Transformation is missing).",
        "What consequence occurs if the user dismisses this notification without setting a transformation?",
        "ما النتيجة التي ستحدث إذا تجاهل المستخدم هذا الإشعار دون تحديد طريقة تحويل المرجع؟",
        [["Features will draw with a spatial offset error (datum shift) of several tens of meters", "ستُرسم المعالم بإزاحة مكانية خاطئة (إزاحة المرجع Datum shift) بمقدار عشرات الأمتار"], ["The computer operating system will crash", "سيتعطل نظام تشغيل الحاسوب"], ["The attribute table will be deleted", "سيتم حذف جدول البيانات السماتية"], ["The map will be converted to a 3D scene", "ستتحول الخريطة إلى مشهد ثلاثي الأبعاد"]],
        "A",
        "When underlying datums differ, coordinates reference different reference ellipsoids. Without a geographic transformation, ArcGIS Pro cannot align the features accurately, causing a visible datum shift.",
        "عند اختلاف المراجع الإسنادية، ترتكز الإحداثيات على مجسمات أرضية مختلفة؛ ودون تطبيق تحويل جغرافي للمرجع، لا يستطيع البرنامج مطابقة المعالم بدقة، مما يسبب إزاحة مكانية واضحة.",
        {"B": ["Software does not crash operating systems on missing datum transformations.", "البرنامج لا يعطل نظام التشغيل."], "C": ["Attribute data is unaffected.", "البيانات السماتية تظل محفوظة."], "D": ["View modes do not change automatically.", "أنماط العرض لا تتغير تلقائياً."]},
        "coord"
    ),
    # 24: Time Slider cumulative playback
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Tool-based", ["Time Slider"],
        "An analyst animates historical oil spill contamination incidents over a 50-year period. Rather than having old spills vanish as time advances, the analyst wants all past spills to remain visible on the map as new ones appear.",
        "يحتاج محلل لتحريك حوادث التلوث النفطي التاريخية على مدى 50 عاماً؛ وبدلاً من اختفاء البقع القديمة مع تقدم الزمن، يريد بقاء كافة البقع السابقة ظاهرة على الخريطة مع ظهور البقع الجديدة.",
        "What setting on the Time tab enables this cumulative temporal behavior?",
        "ما الإعداد في تبويب الوقت (Time) الذي يفعل هذا السلوك الزمني التراكمي؟",
        [["Check 'Start time: None' or check 'Show data cumulatively'", "تفعيل خيار العرض التراكمي للبيانات 'Show data cumulatively'"], ["Set layer transparency to 0%", "ضبط شفافية الطبقة على 0%"], ["Export to PNG", "التصدير إلى PNG"], ["Delete future time stamps", "حذف التواريخ المستقبلية"]],
        "A",
        "Enabling 'Show data cumulatively' (or unconstraining the start time) locks the start of the time window to the earliest record, accumulating features on screen as the slider moves forward.",
        "يؤدي اختيار 'Show data cumulatively' إلى تثبيت بداية النافذة الزمنية عند أقدم سجل تاريخي، مما يراكم المعالم على الشاشة باستمرار مع تقدم المنزلق الزمني للأمام.",
        {"B": ["Transparency does not govern temporal query spans.", "الشفافية لا تتحكم في النطاق الزمني."], "C": ["PNG is a static export.", "تصدير PNG صورة ثابتة."], "D": ["Deleting records destroys data.", "حذف التواريخ يدمر البيانات."]},
        "time"
    ),
    # 25: 3D Scene local clipping extent
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Intermediate", "Tool-based", ["3D Scenes"],
        "A geotechnical engineering team models a tunnel excavation in a 3D Local Scene. They need the scene view to clip sharply along a 500-meter rectangular project boundary, hiding the surrounding regional terrain.",
        "ينمذج فريق هندسة جيوتقنية حفر نفق في مشهد محلي ثلاثي الأبعاد؛ ويحتاج لقص عرض المشهد بصرامة عند حدود مستطيلة للمشروع بمسافة 500 متر لإخفاء التضاريس الإقليمية المحيطة.",
        "Where is this spatial boundary defined in a Local Scene?",
        "أين يتم تحديد هذا النطاق المكاني في المشهد المحلي؟",
        [["Scene Properties > Extent > 'Use a custom extent' with clipping enabled", "خصائص المشهد Scene Properties > تبويب Extent > اختيار 'Use a custom extent' مع تفعيل القص"], ["Layer Properties > Symbology", "خصائص الطبقة > الرموز"], ["Catalog Pane > Folder Connections", "نافذة الكتالوج > اتصالات المجلدات"], ["Edit Ribbon > Snapping", "شريط التحرير > الانجذاب"]],
        "A",
        "In a Local Scene, the Extent tab in Scene Properties allows defining a custom rectangular bounding box and checking 'Clip to extent', cutting the 3D ground surface and layers sharply to the project boundaries.",
        "في المشهد المحلي، يتيح تبويب Extent في خصائص المشهد تحديد مستطيل مخصص وتفعيل خيار 'Clip to extent'، مما يقتطع سطح الأرض ثلاثي الأبعاد والطبقات بصرامة عند حدود المشروع.",
        {"B": ["Symbology colors features.", "الترميز لتلوين المعالم."], "C": ["Catalog manages files.", "الكتالوج لإدارة الملفات."], "D": ["Snapping controls vertex edits.", "الانجذاب للتحرير."]},
        "scenes"
    ),
    # 26: Select By Attributes LIKE wildcards
    (
        "Given a scenario, apply a query", "Beginner", "Technical", ["Select By Attributes"],
        "An analyst needs to select all street centerlines in a city where the STREET_NAME contains the word 'Park' anywhere within the text string (e.g., 'Park Ave', 'South Park Road', 'Glenpark Drive').",
        "يحتاج محلل لتحديد كافة محاور الشوارع في المدينة التي يحتوي فيها حقل STREET_NAME على كلمة 'Park' في أي موضع داخل النص (مثل 'Park Ave' أو 'South Park Road' أو 'Glenpark Drive').",
        "Which SQL expression correctly retrieves all matching features?",
        "أي تعبير SQL يسترجع كافة المعالم المطابقة بشكل صحيح؟",
        [["STREET_NAME LIKE '%Park%'", "STREET_NAME LIKE '%Park%'"], ["STREET_NAME = 'Park'", "STREET_NAME = 'Park'"], ["STREET_NAME IN ('Park')", "STREET_NAME IN ('Park')"], ["STREET_NAME LIKE '_Park_'", "STREET_NAME LIKE '_Park_'"]],
        "A",
        "The percent sign (%) wildcard matches any number of characters. Wrapping 'Park' with wildcards on both sides (%Park%) matches the substring anywhere in the field.",
        "تطابق علامة النسبة المئوية (%) أي عدد من الحروف؛ ووضعها على جانبي الكلمة (%Park%) يضمن مطابقة الكلمة سواء وقعت في بداية النص أو وسطه أو نهايته.",
        {"B": ["Equality (=) only matches rows where the entire text is solely the four letters 'Park'.", "معامل المساواة يطابق الكلمة المنفردة فقط."], "C": ["IN ('Park') matches exact string equality only.", "معامل IN يطابق النص الدقيق فقط."], "D": ["Underscore (_) matches exactly one single character, not variable text strings.", "الشرطة السفلية تطابق حرفاً واحداً فقط."]},
        "query"
    ),
    # 27: Select By Location Completely Contains
    (
        "Given a scenario, apply a query", "Intermediate", "Tool-based", ["Select By Location"],
        "A wildlife conservation department has a layer of national parks and a layer of endangered species sighting points. The biologist wants to select ONLY parks that encompass all sightings of a specific herd within their borders.",
        "تمتلك إدارة حماية الحياة الفطرية طبقة للمتنزهات الوطنية وطبقة لنقاط رصد الأنواع المهددة؛ ويريد باحث الأحياء تحديد المتنزهات التي تحتوي كافة نقاط قطيع معين بالكامل داخل حدودها فقط.",
        "Which spatial relationship in Select By Location should be chosen with Input: Parks and Selecting Features: Herd Points?",
        "أي علاقة مكانية في أداة Select By Location يجب اختيارها مع تحديد المدخلات: المتنزهات، ومعالم التحديد: نقاط القطيع؟",
        [["Completely contains", "Completely contains (تحتوي بالكامل)"], ["Are within", "Are within (تقع داخل)"], ["Touch the boundary of", "Touch the boundary of (تلامس حدود)"], ["Are crossed by the outline of", "Are crossed by the outline of (تقطعها حدود)"]],
        "A",
        "When polygon parks are the Input Features and points are Selecting Features, 'Completely contains' selects polygons whose interior fully encloses the points.",
        "عندما تكون مضلعات المتنزهات هي معالم الإدخال والنقاط هي معالم التحديد، فإن علاقة 'Completely contains' تحدد المضلعات التي تضم النقاط بالكامل داخل حدودها.",
        {"B": ["'Are within' is the reverse relationship.", "علاقة Are within هي العلاقة العكسية."], "C": ["Touch boundary requires edge coincidence.", "تلامس الحدود يتطلب اشتراكاً بالحواف."], "D": ["Crossed by outline requires line intersections.", "تقطعها الحدود لتقاطع الخطوط."]},
        "query"
    ),
    # 28: Equal Interval skewed data pitfall
    (
        "Manage layer properties using the ribbon and dialog boxes", "Beginner", "Conceptual", ["Classification"],
        "An analyst uses Equal Interval with 5 classes to map city building values. A single landmark tower is valued at $500,000,000, while 99% of all other buildings are valued under $2,000,000. In the map, almost every building falls into Class 1, while Classes 2, 3, and 4 are completely empty.",
        "استخدم محلل طريقة الفترات المتساوية (Equal Interval) بـ 5 فئات لتمثيل قيم مباني المدينة؛ وتبين وجود برج استثماري بقيمة 500 مليون دولار، بينما 99% من المباني قيمتها أقل من مليوني دولار، فظهرت جميع المباني تقريباً في الفئة الأولى وبقيت بقية الفئات فارغة تماماً.",
        "What fundamental limitation of Equal Interval caused this cartographic failure?",
        "ما هو العيب الجوهري في طريقة الفترات المتساوية الذي تسبب في هذا الفشل الكارتوغرافي؟",
        [["Equal Interval divides the total numeric range evenly regardless of data clustering or extreme outliers", "تقسم طريقة الفترات المتساوية المدى الرقمي بالتساوي بغض النظر عن تركز البيانات أو وجود قيم شاذة متطرفة"], ["Equal Interval cannot handle integer numbers", "لا تدعم الفترات المتساوية الأرقام الصحيحة"], ["The map frame was not locked", "لم يتم قفل إطار الخريطة"], ["The layer lacked a spatial index", "كانت الطبقة تفتقر لفهرس مكاني"]],
        "A",
        "Equal interval divides the range (Max - Min) into equal numeric chunks. When extreme outliers exist, the wide ranges result in most features clustering into the lowest bucket while higher buckets remain empty.",
        "تقسم طريقة الفترات المتساوية المدى الكلي (الأعلى - الأدنى) إلى فترات رقمية متطابقة الطول؛ ومع وجود قيم متطرفة شاذة، يتسع طول الفترات فتتكدس أغلب المعالم في الفئة الأولى وتبقى الفئات العليا فارغة.",
        {"B": ["Equal Interval fully supports integers and floats.", "تدعم الطريقة الأرقام الصحيحة والعشرية."], "C": ["Map frame locking does not alter classification breaks.", "قفل الإطار لا يغير فواصل التصنيف."], "D": ["Spatial indexing optimizes search, not classification math.", "الفهرس المكاني لتسريع البحث."]},
        "classification"
    ),
    # 29: Natural Breaks Jenks within vs between variance
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical", ["Classification"],
        "A GIS demographer prepares a choropleth map of regional income distributions and wants to group data using Natural Breaks.",
        "يقوم باحث ديموغرافي بإعداد خريطة كوروبليث لتوزيعات الدخل الإقليمية ويريد تصنيف البيانات باستخدام طريقة الكسور الطبيعية (Natural Breaks).",
        "What mathematical objective function does the Natural Breaks (Jenks) optimization algorithm solve for?",
        "ما هي الدالة الهدفية الرياضية التي تسعى خوارزمية جينكس (Natural Breaks) لتحقيقها في البيانات؟",
        [["Minimizes variance within classes while maximizing variance between classes", "تقليل التباين الإحصائي داخل الفئة الواحدة لأدنى حد مع تعظيم التباين بين الفئات المختلفة لأقصى حد"], ["Forces every class to contain exactly 10 features", "إجبار كل فئة على احتواء 10 معالم بالضبط"], ["Calculates the geometric surface area of polygons", "حساب المساحة السطحية الهندسية للمضلعات"], ["Converts coordinates into polar space", "تحويل الإحداثيات إلى الفضاء القطبي"]],
        "A",
        "The Jenks optimization algorithm seeks to reduce the variance within each class (sum of squared deviations from the class mean) while maximizing the difference between separate classes.",
        "تسعى خوارزمية جينكس إلى تقليص التشتت والتباين الإحصائي الداخلي للقيم داخل كل فئة، مع زيادة الفروق والتباين بين الفئات المختلفة لإبراز الانقسامات والتجمعات الطبيعية في البيانات.",
        {"B": ["Equal count is the objective of Quantile classification.", "تساوي الأعداد هدف تصنيف Quantile."], "C": ["Classification does not alter geometric surface areas.", "التصنيف لا يعدل المساحات."], "D": ["Coordinate transformations are handled by projections.", "التحويلات الإسقاطية تديرها نظم الإحداثيات."]},
        "classification"
    ),
    # 30: Maplex Background label vs Normal label
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Technical", ["Maplex Label Engine"],
        "A cartographer needs water body labels (e.g. 'Lake Michigan') to draw in the background so that city labels and road numbers draw directly on top of the lake labels without being suppressed or displaced.",
        "يحتاج رسام خرائط لرسم تسميات المسطحات المائية (مثل 'بحيرة ميشيغان') في الخلفية، بحيث تُوضع تسميات المدن وأرقام الطرق فوقها مباشرة دون أن تُحجب أو تُزاح.",
        "Which Maplex label class setting treats lake labels as background text?",
        "أي إعداد لفئة التسميات في Maplex يجعل تسميات البحيرة تُعامل كنصوص خلفية؟",
        [["Set Label Class type to 'Background label'", "ضبط نوع فئة التسمية على تسمية خلفية (Background label)"], ["Set Feature Weight to 1000", "ضبط وزن المعلم على 1000"], ["Delete the city labels", "حذف تسميات المدن"], ["Convert the lake to a 3D building", "تحويل البحيرة لمبنى ثلاثي الأبعاد"]],
        "A",
        "Flagging a label class as a 'Background label' tells Maplex that other competing labels are permitted to draw directly over it without triggering conflict suppression.",
        "يؤدي تعيين فئة التسمية كـ 'Background label' إلى توجيه محرك Maplex للسماح للتسميات المتنافسة الأخرى بالرسم فوقها مباشرة دون اعتبار ذلك تصادماً يؤدي لحجب التسميات.",
        {"B": ["Feature Weight 1000 creates an impassable obstacle, blocking labels.", "وزن 1000 يمنع التسميات."], "C": ["Deleting labels destroys city names.", "حذف التسميات يدمر أسماء المدن."], "D": ["Lakes are water bodies, not 3D buildings.", "البحيرات مسطحات مائية وليست مباني."]},
        "labeling"
    ),
    # 31: Unmatched address rematch tie resolution
    (
        "Given a scenario, apply a query", "Intermediate", "Troubleshooting", ["Rematch Addresses"],
        "During address rematching in ArcGIS Pro, an address displays a 'Tied' status with two candidates scoring 98.4%: '100 North Main Street' and '100 South Main Street'.",
        "أثناء إعادة مطابقة العناوين، أظهر سجل حالة تعادل (Tied) مع مرشحين كلاهما بدرجة 98.4%: '100 North Main Street' و '100 South Main Street'.",
        "How must the technician resolve this candidate tie?",
        "كيف يجب على الفني حسم هذا التعادل بين المرشحين؟",
        [["Inspect reference data or source documents and manually pick the correct candidate match", "فحص البيانات المرجعية أو وثائق المصدر واختيار المرشح المطابق الصحيح يدوياً"], ["Let the computer randomly delete one candidate", "ترك الحاسوب يحذف أحد المرشحين عشوائياً"], ["Restart ArcGIS Pro", "إعادة تشغيل ArcGIS Pro"], ["Change the layer coordinate system", "تغيير نظام إحداثيات الطبقة"]],
        "A",
        "A Tied status indicates multiple candidates share the highest match score. The technician must review source records, pick the verified location in the Rematch pane, and click Match.",
        "تشير حالة التعادل (Tied) لتساوي مرشحين في أعلى درجة تطابق؛ ويجب على الفني مراجعة الوثائق وتحديد الموقع الصحيح في نافذة Rematch ثم النقر على تأكيد المطابقة (Match).",
        {"B": ["GIS software does not randomly delete data.", "البرنامج لا يحذف البيانات عشوائياً."], "C": ["Restarting does not resolve data ambiguity.", "إعادة التشغيل لا تحل غموض البيانات."], "D": ["Coordinate systems do not disambiguate street names.", "أنظمة الإحداثيات لا تفصل في أسماء الشوارع."]},
        "query"
    ),
    # 32: Vary Symbology By Attribute Rotation
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Symbology"],
        "An oceanographic researcher tracks marine buoy sensors recording wave height and wave direction. Each buoy point must display as an arrow whose size reflects wave height and whose orientation points in the direction of wave travel.",
        "يتابع باحث علوم بحار مجسات عائمات بحرية تسجل ارتفاع الموج واتجاهه؛ ويجب عرض كل نقطة كسهم يعبر حجمه عن ارتفاع الموج ويشير اتجاهه نحو مسار حركة الموج.",
        "Which symbology configuration in ArcGIS Pro achieves this dual-variable visualization?",
        "أي تهيئة للرموز في ArcGIS Pro تحقق هذا التمثيل البصري ثنائي المتغيرات؟",
        [["Use 'Vary symbology by attribute' to bind Size to WAVE_HEIGHT and Rotation to WAVE_DIRECTION", "استخدام 'Vary symbology by attribute' لربط الحجم بحقل WAVE_HEIGHT والتدوير بحقل WAVE_DIRECTION"], ["Create two duplicate feature classes and overlay them", "إنشاء فئتي معالم مكررتين وتركيبهما فوق بعض"], ["Set layer transparency to 80%", "ضبط شفافية الطبقة على 80%"], ["Export to AutoCAD DWG", "التصدير إلى أوتوكاد DWG"]],
        "A",
        "The 'Vary symbology by attribute' capability in the Symbology pane allows secondary attribute fields to drive visual variables (such as rotation angle and symbol size) independently on a single layer.",
        "تتيح ميزة 'Vary symbology by attribute' في نافذة الرموز ربط حقول سمات ثانوية للتحكم المستقل في المتغيرات البصرية (كزاوية التدوير وحجم الرمز) لنفس الطبقة.",
        {"B": ["Duplicating feature classes doubles storage redundantly.", "تكرار الطبقات يضاعف التخزين بلا مبرر."], "C": ["Transparency does not orient arrows.", "الشفافية لا توجه الأسهم."], "D": ["AutoCAD export is a file conversion.", "تصدير أوتوكاد تحويل ملفات."]},
        "symbology"
    ),
    # 33: Maplex Abbreviation Dictionary translation trap
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Conceptual", ["Maplex Label Engine"],
        "A municipal cartographer configures an Abbreviation Dictionary in the Maplex Label Engine to abbreviate long street suffixes like 'Avenue' to 'Ave' on an urban street map.",
        "يقوم رسام خرائط بلدي بتهيئة قاموس اختصارات في محرك Maplex لاختصار لواحق الشوارع الطويلة مثل 'Avenue' إلى 'Ave' في خريطة شوارع حضرية.",
        "What effect does the Maplex Abbreviation Dictionary have on the underlying geodatabase table attributes?",
        "ما هو تأثير قاموس اختصارات Maplex على سمات جدول قاعدة البيانات الجغرافية الأصلية؟",
        [["The underlying table attributes remain completely unchanged; abbreviation occurs only on the screen display", "تبقى سمات الجدول الأصلية دون أي تغيير إطلاقاً؛ وتحدث الاختصارات في العرض البصري على الشاشة فقط"], ["The table attributes are permanently abbreviated and overwritten on disk", "تُختصر سمات الجدول نهائياً وتُستبدل على القرص"], ["The table is converted to a CSV file", "يتحول الجدول إلى ملف CSV"], ["All text fields are converted to Short Integer", "تتحول كافة الحقول النصية إلى أرقام صحيحة"]],
        "A",
        "Maplex abbreviation dictionaries are dynamic cartographic presentation tools. They alter text strings strictly during label rendering on screen and layout, never touching source database records.",
        "تعد قواميس اختصارات Maplex أدوات عرض كارتوغرافي ديناميكي؛ وتختصر النصوص أثناء رسم التسميات على الشاشة واللوحة فقط، دون المساس بسجلات قاعدة البيانات الأصلية إطلاقاً.",
        {"B": ["Maplex never modifies source geodatabase tables.", "لا يعدل Maplex جداول البيانات الأصلية."], "C": ["Table format remains intact.", "تنسيق الجدول يظل ثابتاً."], "D": ["Field data types are not altered by labeling.", "أنواع الحقول لا تتغير بالتسميات."]},
        "labeling"
    ),
    # 34: 3D Scene Vertical Exaggeration
    (
        "Determine how to visualize temporal, ranged, or 3D data", "Beginner", "Tool-based", ["3D Scenes"],
        "In a flat coastal plain, subtle elevation changes of 5 to 10 feet are difficult to perceive in a 3D Scene.",
        "في سهل ساحلي مستوٍ، يصعب ملاحظة الفروق الطبوغرافية الطفيفة في الارتفاع (من 5 إلى 10 أقدام) في المشهد ثلاثي الأبعاد.",
        "Which setting in the 3D Scene properties multiplies the vertical elevation scale relative to the horizontal scale to emphasize subtle terrain variations?",
        "ما الإعداد في خصائص المشهد ثلاثي الأبعاد الذي يضاعف مقياس الارتفاع الرأسي بالنسبة للمقياس الأفقي لإبراز الفروق التضاريسية الطفيفة؟",
        [["Vertical Exaggeration", "المبالغة الرأسية (Vertical Exaggeration)"], ["Sun Azimuth", "سمت الشمس (Sun Azimuth)"], ["Field of View", "زاوية الرؤية (Field of View)"], ["Ambient Occlusion", "الانسداد المحيطي (Ambient Occlusion)"]],
        "A",
        "Vertical Exaggeration applies an artificial multiplier (e.g. 2x, 5x, 10x) to Z-elevations, enhancing visual perception of subtle topographic relief in relatively flat landscapes.",
        "تطبق المبالغة الرأسية (Vertical Exaggeration) معاملاً مضاعفاً (مثل 2x أو 5x) على الارتفاعات الرأسية Z، مما يبرز التباينات التضاريسية الطفيفة في المناطق السهلية والمستوية بصرياً.",
        {"B": ["Sun Azimuth controls solar lighting direction.", "سمت الشمس يحدد اتجاه الضوء."], "C": ["Field of View controls camera lens perspective.", "زاوية الرؤية لعدسة الكاميرا."], "D": ["Ambient occlusion adds contact shading.", "الانسداد المحيطي يضيف ظلال تلامس."]},
        "scenes"
    ),
    # 35: Definition Query Date queries
    (
        "Given a scenario, apply a query", "Intermediate", "Technical", ["Definition Query"],
        "An analyst needs to filter a city building permits feature layer to display only permits issued during the current calendar year (2025).",
        "يحتاج محلل إلى تصفية طبقة معالم تصاريح المباني بالمدينة لعرض التصاريح الصادرة خلال السنة الميلادية الحالية (2025) فقط.",
        "Which SQL expression in a Definition Query correctly isolates records where ISSUE_DATE falls between January 1, 2025 and December 31, 2025?",
        "أي تعبير SQL في الاستعلام التعريفي يعزل السجلات التي يقع فيها حقل ISSUE_DATE بين 1 يناير 2025 و 31 ديسمبر 2025 بشكل صحيح؟",
        [["ISSUE_DATE >= date '2025-01-01 00:00:00' AND ISSUE_DATE <= date '2025-12-31 23:59:59'", "ISSUE_DATE >= date '2025-01-01 00:00:00' AND ISSUE_DATE <= date '2025-12-31 23:59:59'"], ["ISSUE_DATE = '2025'", "ISSUE_DATE = '2025'"], ["YEAR(ISSUE_DATE) == 'THIS_YEAR'", "YEAR(ISSUE_DATE) == 'THIS_YEAR'"], ["SELECT PERMITS IN 2025", "SELECT PERMITS IN 2025"]],
        "A",
        "In ArcGIS Pro standard SQL, date literals are specified using the date prefix `date 'YYYY-MM-DD hh:mm:ss'`, allowing precise chronological bounding.",
        "في استعلامات SQL بـ ArcGIS Pro، تُكتب التواريخ باستخدام البادئة date بصيغة `date 'YYYY-MM-DD hh:mm:ss'`، مما يتيح تحديد النطاق الزمني بدقة متناهية.",
        {"B": ["Date fields cannot be compared to single four-digit text strings.", "حقول التاريخ لا تقارن بنص من 4 أرقام."], "C": ["THIS_YEAR is not standard SQL.", "THIS_YEAR ليست دالة قياسية."], "D": ["Natural language cannot be evaluated by query engines.", "اللغة النصية لا يفهمها محرك الاستعلام."]},
        "query"
    ),
    # 36: Apply Symbology From Layer field mapping
    (
        "Manage layer properties using the ribbon and dialog boxes", "Intermediate", "Tool-based", ["Apply Symbology From Layer"],
        "An analyst uses the Apply Symbology From Layer tool to copy complex graduated colors from a 2020 census layer to a 2025 census layer. However, the target layer's population field is named 'POP_2025' while the source layer's field was named 'TOT_POP'.",
        "استخدم محلل أداة Apply Symbology From Layer لنسخ ألوان متدرجة من طبقة تعداد 2020 إلى طبقة 2025؛ ولكن حقل السكان في طبقة الهدف اسمه 'POP_2025' بينما كان في المصدر 'TOT_POP'.",
        "What parameter in the tool dialog ensures the symbology maps to the correct attribute field?",
        "ما المعامل في نافذة الأداة الذي يضمن تطبيق الرموز على الحقل السماتي الصحيح؟",
        [["Symbology Fields (Source Field to Target Field mapping)", "حقول الرموز Symbology Fields (مطابقة حقل المصدر مع حقل الهدف)"], ["Cell Size", "حجم الخلية Cell Size"], ["Coordinate System", "نظام الإحداثيات"], ["Cluster Tolerance", "تسامح التجميع"]],
        "A",
        "The Apply Symbology From Layer tool provides a Symbology Fields mapping parameter where users match source classification fields to corresponding target layer fields when field names differ.",
        "توفر أداة Apply Symbology From Layer معاملاً لمطابقة الحقول (Symbology Fields) يتيح للمستخدم تحديد الحقل المقابل في الطبقة الهدف عند اختلاف مسميات الحقول بين الطبقتين.",
        {"B": ["Cell size is a raster parameter.", "حجم الخلية للراستر."], "C": ["Coordinate system handles projections.", "نظام الإحداثيات للإسقاط."], "D": ["Cluster tolerance belongs to topology.", "تسامح التجميع للطوبولوجيا."]},
        "symbology"
    ),
    # 37: Geometric Interval for highly skewed data
    (
        "Manage layer properties using the ribbon and dialog boxes", "Advanced", "Conceptual", ["Classification"],
        "A real estate analyst maps commercial lease rates across a metropolitan region. The data is continuous, highly non-normal, and spans extreme ranges from $10/sq ft in rural warehouses to $1,500/sq ft in prime financial district skyscrapers.",
        "يمثل محلل عقارات أسعار إيجارات العقارات التجارية؛ والبيانات مستمرة وشديدة الالتواء وتتفاوت بين 10 دولارات للقدم في المستودعات و 1500 دولار في ناطحات السحاب المركزية.",
        "Which classification method is mathematically designed specifically for continuous data that is not normally distributed, producing aesthetically pleasing class ranges based on a geometric progression?",
        "أي طريقة تصنيف مصممة رياضياً للبيانات المستمرة غير الموزعة طبيعياً، وتنتج فئات متناسقة تعتمد على متوالية هندسية؟",
        [["Geometric Interval", "الفترات الهندسية (Geometric Interval)"], ["Equal Interval", "الفترات المتساوية (Equal Interval)"], ["Standard Deviation", "الانحراف المعياري (Standard Deviation)"], ["Defined Interval", "الفترات المحددة (Defined Interval)"]],
        "A",
        "Geometric Interval creates class breaks based on a geometric series, minimizing sum of squares of elements per class and handling skewed continuous distributions gracefully.",
        "تنشئ طريقة الفترات الهندسية (Geometric Interval) فواصل تعتمد على متوالية هندسية، مما يقلل مجموع مربعات العناصر لكل فئة ويتعامل مع البيانات المستمرة شديدة الالتواء ببراعة.",
        {"B": ["Equal Interval produces empty classes when distributions are skewed.", "الفترات المتساوية تنتج فئات فارغة عند الالتواء."], "C": ["Standard Deviation requires normal bell-curve data.", "الانحراف المعياري يتطلب توزيعاً طبيعياً معتدلاً."], "D": ["Defined Interval requires fixed step increments.", "الفترات المحددة تتطلب خطوات ثابتة."]},
        "classification"
    ),
    # 38: Select By Attributes IS NOT NULL
    (
        "Given a scenario, apply a query", "Beginner", "Technical", ["Select By Attributes"],
        "A data cleanup specialist needs to select all road segments that have an assigned street name (excluding records where the NAME field was left empty or unpopulated).",
        "يحتاج أخصائي تنظيف بيانات لتحديد كافة أجزاء الطرق التي تم إدخال اسم شارع لها (مستبعداً السجلات التي تُرِك فيها حقل الاسم فارغاً أو غير مدخل).",
        "Which SQL clause correctly selects all records containing valid names?",
        "أي جملة SQL تحدد كافة السجلات التي تحتوي على أسماء صالحة بشكل صحيح؟",
        [["NAME IS NOT NULL AND NAME <> ''", "NAME IS NOT NULL AND NAME <> ''"], ["NAME != NULL", "NAME != NULL"], ["NAME = 'NOT NULL'", "NAME = 'NOT NULL'"], ["SELECT ALL POPULATED NAMES", "SELECT ALL POPULATED NAMES"]],
        "A",
        "In relational database SQL, testing for populated values requires `IS NOT NULL` to exclude database nulls, and `<> ''` to exclude blank empty text strings.",
        "في قواعد بيانات SQL، يتطلب فحص السجلات الممتلئة استخدام `IS NOT NULL` لاستبعاد القيم الفارغة برمجياً، و `<> ''` لاستبعاد النصوص البيضاء الخالية من الحروف.",
        {"B": ["`!= NULL` is invalid syntax in SQL for null testing.", "`!= NULL` صياغة غير صحيحة للتحقق من القيم الفارغة."], "C": ["`'NOT NULL'` in quotes searches for the literal word string.", "وضع الكلمة بين علامات تنصيص يبحث عن الكلمة كنص."], "D": ["Natural language cannot execute.", "اللغة الطبيعية لا تنفذ."]},
        "query"
    )
]

# Combine all visualization scenario datasets
all_viz_scenarios = viz_scenarios_data + more_viz_scenarios

for i, item in enumerate(all_viz_scenarios):
    qid = f"VIZ-S-{i+1:03d}"
    unpacked = unpack_item(item, qid)
    items.append(s(*unpacked))

print(f"Total Visualization Scenarios: {len(items)} (target 38)")

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Saved scenarios/visualization.json successfully.")
