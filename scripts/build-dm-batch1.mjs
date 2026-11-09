// Generator for public/data/questions/data-management.json (batch 1: coordinate systems). Run: node scripts/build-dm-batch1.mjs
import { writeFileSync } from 'node:fs';
const DP = { title: 'Define Projection (Data Management), Esri ArcGIS Pro documentation', url: 'https://pro.arcgis.com/en/pro-app/tool-reference/data-management/define-projection.htm', kind: 'official' };
const PR = { title: 'Project (Data Management), ArcGIS Pro 3.3 documentation', url: 'https://pro.arcgis.com/en/pro-app/3.3/tool-reference/data-management/project.htm', kind: 'official' };
const OBJ = 'Manage coordinate systems to preserve the desired spatial properties';
const IDS = ['A','B','C','D'];
// [id, difficulty, type, tools, qEn, qAr, options[[en,ar]x4], answerIndex, expEn, expAr, whyWrong[[en,ar]x3 in option order skipping correct], refs]
const S = [
['DM-001','Beginner','Tool-based',['Define Projection','Project'],
 'A shapefile has an "Unknown" coordinate system, but you know its coordinates are in NAD 1983 UTM Zone 12N. What should you do first?',
 'ملف شيب (shapefile) نظام إحداثياته "Unknown"، لكنك تعلم أن إحداثياته بنظام NAD 1983 UTM Zone 12N. ما الذي يجب فعله أولاً؟',
 [['Run Project to NAD 1983 UTM Zone 12N','شغّل أداة Project إلى NAD 1983 UTM Zone 12N'],['Run Define Projection and assign NAD 1983 UTM Zone 12N','شغّل أداة Define Projection وعيّن NAD 1983 UTM Zone 12N'],['Delete the .prj file and re-add the layer','احذف ملف .prj وأعد إضافة الطبقة'],['Change the map coordinate system only','غيّر نظام إحداثيات الخريطة فقط']],1,
 'Define Projection assigns coordinate system information to a dataset whose coordinate system is unknown or incorrect, without changing the geometry. Because the real coordinates are already in the known system, only the definition is missing.',
 'تعيّن أداة Define Projection معلومات نظام الإحداثيات لبيانات نظامها غير معروف أو غير صحيح، دون تغيير الهندسة. بما أن الإحداثيات الفعلية موجودة أصلاً بالنظام المعروف، فالمفقود هو التعريف فقط.',
 [['Project transforms coordinate values and needs a correctly defined input system; with an unknown input it cannot start from the right place.','تحوّل Project قيم الإحداثيات وتحتاج إلى نظام إدخال معرَّف بشكل صحيح؛ مع نظام غير معروف لا تنطلق من الأساس الصحيح.'],['Deleting the .prj removes the definition without fixing anything.','حذف ملف .prj يزيل التعريف دون إصلاح أي شيء.'],['The map coordinate system controls display only and does not store a definition on the dataset.','نظام إحداثيات الخريطة يؤثر في العرض فقط ولا يخزن تعريفاً في البيانات.']],[DP,PR]],
['DM-002','Beginner','Conceptual',['Define Projection','Project'],
 'Which statement correctly distinguishes Project from Define Projection?',
 'أي عبارة تميّز بشكل صحيح بين Project وDefine Projection؟',
 [['Both tools change coordinate values','كلتا الأداتين تغيّر قيم الإحداثيات'],['Define Projection transforms geometry; Project only edits metadata','Define Projection تحوّل الهندسة؛ وProject تعدّل البيانات الوصفية فقط'],['Project transforms data into a new coordinate system; Define Projection only overwrites the stored definition','Project تحوّل البيانات إلى نظام إحداثيات جديد؛ وDefine Projection تستبدل التعريف المخزن فقط'],['Project can only be used on rasters','يمكن استخدام Project على الراستر فقط']],2,
 'Project projects spatial data from one coordinate system to another and writes a new output. Define Projection overwrites the coordinate system information stored with a dataset and does not modify geometry.',
 'تقوم Project بإسقاط البيانات المكانية من نظام إحداثيات إلى آخر وتكتب مخرجاً جديداً. أما Define Projection فتستبدل معلومات نظام الإحداثيات المخزنة مع البيانات ولا تعدّل الهندسة.',
 [['Only Project changes coordinate values.','Project وحدها تغيّر قيم الإحداثيات.'],['This reverses the two tools.','هذه العبارة تعكس وظيفتي الأداتين.'],['Rasters are not supported by Project at all; Project Raster is the raster tool.','Project لا تدعم الراستر أصلاً؛ أداة Project Raster هي المخصصة له.']],[DP,PR]],
['DM-003','Intermediate','Technical',['Project','Geographic Transformation'],
 'You project a feature class from GCS_North_American_1983 to NAD_1983_UTM_Zone_12N. Is a geographic (datum) transformation required?',
 'تسقط فئة معالم من GCS_North_American_1983 إلى NAD_1983_UTM_Zone_12N. هل يلزم تحويل جغرافي (datum transformation)؟',
 [['Yes, always, whenever the projection changes','نعم، دائماً عند تغيير الإسقاط'],['No, both systems use the same NAD 1983 datum','لا، فكلا النظامين يستخدمان نفس مرجع NAD 1983'],['Yes, because one system is geographic and one is projected','نعم، لأن أحدهما جغرافي والآخر مسقط'],['No, transformations only apply to rasters','لا، التحويلات تنطبق على الراستر فقط']],1,
 'A geographic transformation is needed only when the input and output coordinate systems use different datums. Both of these use NAD 1983, so the Geographic Transformation parameter is left blank.',
 'يلزم التحويل الجغرافي فقط عندما يختلف المرجع (datum) بين نظام الإدخال والإخراج. كلاهما يستخدم NAD 1983، لذا يبقى معامل Geographic Transformation فارغاً.',
 [['Transformations are required only when datums differ, not on every projection change.','التحويلات مطلوبة فقط عند اختلاف المرجع، وليس مع كل تغيير للإسقاط.'],['Geographic versus projected is not the criterion; the datum is.','الفرق بين جغرافي ومسقط ليس المعيار؛ المعيار هو المرجع.'],['Transformations apply to vector and other data when datums differ.','التحويلات تنطبق على البيانات الاتجاهية وغيرها عند اختلاف المرجع.']],[PR]],
['DM-004','Intermediate','Technical',['Project','Geographic Transformation'],
 'Which projection requires a geographic transformation?',
 'أي عملية إسقاط تتطلب تحويلاً جغرافياً؟',
 [['GCS_North_American_1983 to NAD_1983_UTM_Zone_12N','من GCS_North_American_1983 إلى NAD_1983_UTM_Zone_12N'],['GCS_North_American_1983 to WGS_1984_UTM_Zone_12N','من GCS_North_American_1983 إلى WGS_1984_UTM_Zone_12N'],['NAD_1983_UTM_Zone_12N to NAD_1983_UTM_Zone_13N','من NAD_1983_UTM_Zone_12N إلى NAD_1983_UTM_Zone_13N'],['NAD_1983_UTM_Zone_12N to GCS_North_American_1983','من NAD_1983_UTM_Zone_12N إلى GCS_North_American_1983']],1,
 'The input uses the NAD 1983 datum and the output uses WGS 1984, so a datum change is involved and a geographic transformation is required. The other options stay within NAD 1983.',
 'المدخل يستخدم مرجع NAD 1983 والمخرج يستخدم WGS 1984، فهناك تغيير في المرجع ويلزم تحويل جغرافي. بقية الخيارات تبقى ضمن NAD 1983.',
 [['Same datum on both sides.','نفس المرجع في الطرفين.'],['Both use NAD 1983; only the projection changes.','كلاهما NAD 1983؛ يتغير الإسقاط فقط.'],['Same datum on both sides.','نفس المرجع في الطرفين.']].map((x,i)=>x),[PR]],
['DM-005','Intermediate','Troubleshooting',['Project','Copy Features'],
 'You select five features in a layer and run Project, but the output contains every feature in the source dataset. Why, and what is a recommended fix?',
 'حددت خمسة معالم في طبقة وشغّلت Project، لكن المخرج يحتوي على كل معالم مصدر البيانات. لماذا، وما الحل الموصى به؟',
 [['The selection was cleared; reselect and rerun','أُلغي التحديد؛ أعد التحديد وأعد التشغيل'],['Project ignores selections and definition queries; use Copy Features first, then project the copy','Project تتجاهل التحديدات واستعلامات التعريف؛ استخدم Copy Features أولاً ثم أسقط النسخة'],['Project only honors selections when the output is a shapefile','Project تحترم التحديد فقط عندما يكون المخرج shapefile'],['Increase Maximum Offset Deviation','زد قيمة Maximum Offset Deviation']],1,
 'Selections and definition queries on layers are ignored by Project; all features of the referenced dataset are projected. To project only selected features, use Copy Features to create a temporary dataset and project that.',
 'تتجاهل Project التحديدات واستعلامات التعريف على الطبقات؛ تُسقَط كل معالم مجموعة البيانات المرجعية. لإسقاط المعالم المحددة فقط استخدم Copy Features لإنشاء بيانات مؤقتة ثم أسقطها.',
 [['The tool does not honor selections, so reselecting changes nothing.','الأداة لا تحترم التحديد، لذا إعادة التحديد لا تغيّر شيئاً.'],['Output format does not make Project honor selections.','صيغة المخرج لا تجعل Project تحترم التحديد.'],['That parameter controls added vertices, not which features are processed.','هذا المعامل يتحكم في الرؤوس المضافة وليس في المعالم المعالجة.']],[PR]],
['DM-006','Beginner','Tool-based',['Project','Project Raster'],
 'Which tool should you use to change the coordinate system of a raster dataset?',
 'أي أداة تستخدم لتغيير نظام إحداثيات بيانات راستر؟',
 [['Project','Project'],['Define Projection','Define Projection'],['Project Raster','Project Raster'],['Copy Features','Copy Features']],2,
 'Raster datasets are not supported as input to the Project tool. Use Project Raster to project rasters.',
 'مجموعات الراستر غير مدعومة كمدخل لأداة Project. استخدم Project Raster لإسقاط الراستر.',
 [['Project does not accept raster input.','Project لا تقبل راستر كمدخل.'],['It only relabels the definition; it does not reproject pixels.','تغيّر التعريف فقط ولا تعيد إسقاط الخلايا.'],['Copy Features works on vector features.','Copy Features تعمل على المعالم الاتجاهية.']],[PR]],
['DM-007','Advanced','Troubleshooting',['Project','Repair Geometry','Check Geometry'],
 'After projecting a polygon feature class, some output features have null shapes because they fell completely outside the horizon of the output coordinate system. What is the appropriate cleanup?',
 'بعد إسقاط فئة معالم مضلعة، أصبحت بعض المعالم في المخرج بشكل فارغ (null) لأنها وقعت بالكامل خارج أفق نظام الإحداثيات المخرج. ما التنظيف المناسب؟',
 [['Run Define Projection again','شغّل Define Projection مرة أخرى'],['Run Repair Geometry to delete the null-shape features','شغّل Repair Geometry لحذف المعالم ذات الشكل الفارغ'],['Enable Preserve Shape and rerun','فعّل Preserve Shape وأعد التشغيل'],['Nothing; null features are valid and expected','لا شيء؛ المعالم الفارغة صحيحة ومتوقعة']],1,
 'Features completely outside the output horizon are written with a null shape, and Repair Geometry can delete them. Consider whether the output coordinate system suits the extent of your data.',
 'تُكتب المعالم الواقعة كلياً خارج أفق المخرج بشكل فارغ، ويمكن لـ Repair Geometry حذفها. ينبغي أيضاً التحقق من ملاءمة نظام الإحداثيات المخرج لامتداد بياناتك.',
 [['Define Projection does not alter geometry, so null shapes remain.','Define Projection لا تغيّر الهندسة، فتبقى الأشكال الفارغة.'],['Preserve Shape adds vertices; it does not bring features inside the horizon.','Preserve Shape تضيف رؤوساً ولا تُدخل المعالم إلى الأفق.'],['Null shapes are a data-quality problem to clean up, not an expected deliverable.','الأشكال الفارغة مشكلة جودة بيانات يجب تنظيفها وليست مخرجاً متوقعاً.']],[PR]],
['DM-008','Advanced','Workflow-based',['Project','Feature Dataset'],
 'You need to project a feature class that lives inside a feature dataset to a new coordinate system. Where can the output be written?',
 'تريد إسقاط فئة معالم داخل مجموعة بيانات معالم (feature dataset) إلى نظام إحداثيات جديد. أين يمكن كتابة المخرج؟',
 [['Into the same feature dataset','داخل نفس مجموعة بيانات المعالم'],['Into the same feature dataset if the geodatabase is a file geodatabase','داخل نفس مجموعة البيانات إذا كانت قاعدة البيانات ملفية'],['Anywhere except the same feature dataset, because all feature classes in a feature dataset share one coordinate system','في أي مكان عدا نفس مجموعة البيانات، لأن كل فئات المعالم في المجموعة تشترك في نظام إحداثيات واحد'],['Nowhere; feature classes in a feature dataset cannot be projected','لا مكان؛ لا يمكن إسقاط فئات المعالم داخل مجموعة بيانات']],2,
 'Feature classes in a feature dataset must all have the same coordinate system, so the Project output cannot be written to the same feature dataset. It is written to the geodatabase containing the feature dataset, for example.',
 'يجب أن تشترك كل فئات المعالم في مجموعة البيانات بنفس نظام الإحداثيات، لذا لا يمكن كتابة مخرج Project في نفس المجموعة. يُكتب مثلاً في قاعدة البيانات التي تحوي المجموعة.',
 [['The output system differs from the dataset system, so it cannot live there.','نظام المخرج يختلف عن نظام المجموعة فلا يمكن أن يوضع فيها.'],['Geodatabase type does not change the same-coordinate-system rule.','نوع قاعدة البيانات لا يغيّر قاعدة تساوي نظام الإحداثيات.'],['They can be projected; only the output location is restricted.','يمكن إسقاطها؛ القيد على موقع المخرج فقط.']],[PR]],
];
const out = S.map(([id, difficulty, type, tools, qen, qar, opts, ans, een, ear, why, refs]) => {
  const wrong = IDS.filter((_, i) => i !== ans);
  return { id, kind: 'mcq', domain: 'Data Management', objective: OBJ, difficulty, type, tools,
    question: { en: qen, ar: qar },
    options: opts.map((o, i) => ({ id: IDS[i], text: { en: o[0], ar: o[1] } })),
    correctAnswer: IDS[ans], explanation: { en: een, ar: ear },
    incorrectOptionsExplanation: { en: Object.fromEntries(wrong.map((w, i) => [w, why[i][0]])), ar: Object.fromEntries(wrong.map((w, i) => [w, why[i][1]])) },
    references: refs };
});
writeFileSync('public/data/questions/data-management.json', JSON.stringify(out, null, 2));
console.log('wrote', out.length);
