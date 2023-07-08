bl_info = {
    "name": "Add Blouse",
    "author": "Christopher S. Francis",
    "version": (1, 3),
    "blender": (3, 5, 0),
    "location": "run script",
    "description": "Adds a new Blouse Mesh",
    "warning": "",
    "wiki_url": "https://github.com/francis-chris5/blender-human-starter-mesh/wiki",
    "category": "Add Mesh",
}


import bpy
from mathutils import Vector



verts = [Vector((0.16682475805282593, -0.008651836775243282, 0.51687091588974)), Vector((0.16682475805282593, 0.11166200786828995, 0.5196386575698853)), Vector((-0.0005506797460839152, 0.11560104787349701, 0.5523032546043396)), Vector((0.14721311628818512, -0.01767239347100258, 0.3636895716190338)), Vector((0.14619840681552887, -0.029211344197392464, 0.283385694026947)), Vector((0.15604224801063538, -0.07907482236623764, 0.04689784720540047)), Vector((0.14132246375083923, 0.06465184688568115, 0.31976979970932007)), Vector((0.10295888036489487, 0.05012623593211174, 0.24920548498630524)), Vector((0.15604224801063538, 0.08481429517269135, 0.04689784720540047)), Vector((-0.006184195633977652, -0.17093342542648315, 0.3938838541507721)), Vector((-0.0011521985288709402, -0.1383262723684311, 0.13887472450733185)), Vector((-0.0023852523881942034, -0.15822063386440277, 0.04689789190888405)), Vector((-0.0005506797460839152, 0.14322486519813538, 0.4159393310546875)), Vector((-0.0005506797460839152, 0.08846687525510788, 0.21681669354438782)), Vector((-0.0005506797460839152, 0.16030341386795044, 0.046897873282432556)), Vector((0.07091069966554642, 0.10217968374490738, 0.5442111492156982)), Vector((0.13074006140232086, -0.17380768060684204, 0.04689784720540047)), Vector((0.10623740404844284, -0.13151594996452332, 0.13698406517505646)), Vector((0.12912218272686005, 0.14735351502895355, 0.04689784720540047)), Vector((0.07904013246297836, 0.089614138007164, 0.21527846157550812)), Vector((0.09130684286355972, 0.14479787647724152, 0.41594934463500977)), Vector((0.17330177128314972, 0.05196038633584976, 0.5402393937110901)), Vector((0.16593870520591736, 0.0026064147241413593, 0.04689784720540047)), Vector((0.10897132009267807, 0.0023030447773635387, 0.25368669629096985)), Vector((0.15319931507110596, 0.03163578361272812, 0.35631340742111206)), Vector((0.16121071577072144, -0.03249480575323105, 0.4514470398426056)), Vector((0.16121071577072144, 0.11284501850605011, 0.44011861085891724)), Vector((-0.005099628120660782, -0.11715419590473175, 0.45185989141464233)), Vector((-0.0005506797460839152, 0.12849587202072144, 0.4853551685810089)), Vector((0.09516757726669312, -0.08306732028722763, 0.46815958619117737)), Vector((0.09516765177249908, 0.12995436787605286, 0.4810025691986084)), Vector((0.17729933559894562, 0.00041715046972967684, 0.5094183683395386)), Vector((0.17729933559894562, 0.1042933240532875, 0.5118078589439392)), Vector((0.15237422287464142, -0.0251254104077816, 0.36938899755477905)), Vector((0.1552811861038208, 0.06370581686496735, 0.36295345425605774)), Vector((0.1828913688659668, 0.05274833366274834, 0.5295941233634949)), Vector((0.1592041701078415, 0.031133314594626427, 0.36097294092178345)), Vector((0.17245231568813324, -0.02016831748187542, 0.4615857005119324)), Vector((0.17245231568813324, 0.10531466454267502, 0.45180514454841614)), Vector((0.2462487369775772, -0.0007130386075004935, 0.38741135597229004)), Vector((0.187989741563797, -0.0005563081940636039, 0.50221848487854)), Vector((0.187989741563797, 0.1057199090719223, 0.5046631693840027)), Vector((0.16031965613365173, -0.02668902650475502, 0.3665311634540558)), Vector((0.16031965613365173, 0.06419463455677032, 0.35760802030563354)), Vector((0.19371096789836884, 0.052983980625867844, 0.5228604078292847)), Vector((0.16730748116970062, 0.03086954914033413, 0.35792067646980286)), Vector((0.18303072452545166, -0.021617397665977478, 0.4620952010154724)), Vector((0.18303072452545166, 0.10676484555006027, 0.45208868384361267)), Vector((0.248191699385643, 0.10557088255882263, 0.3888951539993286)), Vector((0.17446647584438324, -0.026847630739212036, 0.318915992975235)), Vector((0.16737478971481323, 0.0640426054596901, 0.3134993314743042)), Vector((0.2661271095275879, 0.05283110961318016, 0.39539459347724915)), Vector((0.1718650460243225, 0.030715111643075943, 0.3081354796886444)), Vector((0.2278691530227661, -0.021775657311081886, 0.3562711775302887)), Vector((0.21991635859012604, 0.10661587864160538, 0.35019680857658386)), Vector((0.1660842001438141, 0.03213607147336006, 0.3411986827850342)), Vector((0.16104283928871155, 0.06141006574034691, 0.34341710805892944)), Vector((0.22903066873550415, 0.0007028146646916866, 0.4525332748889923)), Vector((0.19395281374454498, -0.01975325495004654, 0.40934649109840393)), Vector((0.15948882699012756, -0.024679189547896385, 0.3501523435115814)), Vector((0.22997422516345978, 0.10392605513334274, 0.4544411599636078)), Vector((0.19009089469909668, 0.10494096577167511, 0.4015372097492218)), Vector((0.24146214127540588, 0.0527050606906414, 0.46643441915512085)), Vector((0.2007666826248169, 0.06317835301160812, 0.25144314765930176)), Vector((0.24810189008712769, 0.10441557317972183, 0.27302801609039307)), Vector((0.28908786177635193, 0.10340336710214615, 0.2995260953903198)), Vector((0.30701303482055664, 0.05231872573494911, 0.3026302456855774)), Vector((0.2870156764984131, 0.00045489807962439954, 0.298457533121109)), Vector((0.2565838396549225, -0.0199467483907938, 0.27740180492401123)), Vector((0.20408594608306885, 0.0308967474848032, 0.24565674364566803)), Vector((0.20833024382591248, -0.024859536439180374, 0.2553434669971466)), Vector((0.17006325721740723, 0.02165427803993225, 0.528555154800415)), Vector((0.16099043190479279, 0.04371035844087601, 0.04689784720540047)), Vector((0.10596510022878647, 0.02621464431285858, 0.25144609808921814)), Vector((0.15020617842674255, 0.04590993374586105, 0.35617953538894653)), Vector((0.18009530007839203, 0.026582742109894753, 0.5195062756538391)), Vector((0.15869615972042084, 0.04741957038640976, 0.3631060719490051)), Vector((0.1908503919839859, 0.026213834062218666, 0.5125394463539124)), Vector((0.1638135313987732, 0.0475320927798748, 0.35776418447494507)), Vector((0.25618797540664673, 0.026059040799736977, 0.39140304923057556)), Vector((0.16961991786956787, 0.047378864139318466, 0.31081750988960266)), Vector((0.2352464348077774, 0.026703935116529465, 0.4594837725162506)), Vector((0.16356351971626282, 0.046773072332143784, 0.3423078954219818)), Vector((0.20242632925510406, 0.047037553042173386, 0.2485499531030655)), Vector((0.29701441526412964, 0.026386808604002, 0.3005439043045044)), Vector((0.15126663446426392, 0.08874843269586563, 0.392880380153656)), Vector((-0.0005506797460839152, 0.1358603686094284, 0.4506472647190094)), Vector((0.0932372435927391, 0.13737612962722778, 0.44847601652145386)), Vector((0.17006325721740723, 0.08181120455265045, 0.5299389362335205)), Vector((0.16386666893959045, 0.08451023697853088, 0.41102075576782227)), Vector((0.18009530007839203, 0.07852083444595337, 0.520700991153717)), Vector((0.17424680292606354, 0.085479736328125, 0.41036197543144226)), Vector((0.1908503919839859, 0.07935194671154022, 0.5137617588043213)), Vector((0.19364558160305023, 0.08532924205064774, 0.33184799551963806)), Vector((0.25715941190719604, 0.07920100539922714, 0.3921447694301605)), Vector((0.1755668818950653, 0.08317551761865616, 0.3724771738052368)), Vector((0.23571817576885223, 0.07831556349992752, 0.4604377746582031)), Vector((0.2980504631996155, 0.07786104083061218, 0.301078200340271)), Vector((0.22443433105945587, 0.08379697054624557, 0.2622356414794922)), Vector((0.05611831322312355, -0.17289720475673676, 0.04689784720540047)), Vector((0.044350672513246536, -0.13084927201271057, 0.13820812106132507)), Vector((0.03691598027944565, 0.10168806463479996, 0.5494500994682312)), Vector((0.08185116946697235, 0.14655664563179016, 0.04689784720540047)), Vector((0.03133507817983627, 0.07969042658805847, 0.21627439558506012)), Vector((0.03566001355648041, 0.13459855318069458, 0.4159427583217621)), Vector((0.0370212197303772, 0.11982917040586472, 0.48382052779197693)), Vector((0.0370212197303772, -0.09455284476280212, 0.44961050152778625)), Vector((0.03634065389633179, 0.12721386551856995, 0.4498816430568695)), Vector((0.23731833696365356, 0.035370975732803345, 0.4618006646633148)), Vector((0.23939023911952972, 0.04403802007436752, 0.46411770582199097)), Vector((0.30034729838371277, 0.0350307822227478, 0.3012394309043884)), Vector((0.3036801517009735, 0.04367475211620331, 0.3019348382949829)), Vector((0.17222222685813904, 0.04185835272073746, 0.5363447070121765)), Vector((0.1711427867412567, 0.031756315380334854, 0.5324497818946838)), Vector((0.18195931613445282, 0.044026464223861694, 0.5262314081192017)), Vector((0.181027352809906, 0.03530460596084595, 0.5228686928749084)), Vector((0.1927574723958969, 0.0440605953335762, 0.5194199681282043)), Vector((0.19180390238761902, 0.03513721376657486, 0.515979528427124)), Vector((0.26281407475471497, 0.04390708729624748, 0.3940640091896057)), Vector((0.25950101017951965, 0.034983064979314804, 0.3927334249019623)), Vector((0.23898856341838837, 0.04235794395208359, 0.46366843581199646)), Vector((0.30303409695625305, 0.04199914634227753, 0.3017999529838562)), Vector((0.17201295495033264, 0.03990010917186737, 0.5355894565582275)), Vector((0.18177863955497742, 0.04233577102422714, 0.5255795121192932)), Vector((0.19257262349128723, 0.04233083501458168, 0.5187530517578125)), Vector((0.2621718645095825, 0.042177196592092514, 0.3938060700893402)), Vector((0.17157787084579468, 0.035828206688165665, 0.5340195894241333)), Vector((0.18140298128128052, 0.03882018104195595, 0.524224042892456)), Vector((0.1921882927417755, 0.03873401880264282, 0.5173662304878235)), Vector((0.2608363926410675, 0.03858012706041336, 0.3932698369026184)), Vector((0.23815345764160156, 0.038864459842443466, 0.46273455023765564)), Vector((0.3016906976699829, 0.03851496800780296, 0.3015197813510895)), Vector((0.11871080845594406, 0.09896839410066605, 0.5288968086242676)), Vector((0.12853805720806122, 0.11066855490207672, 0.04689784720540047)), Vector((0.06611662358045578, 0.06987018883228302, 0.23224204778671265)), Vector((0.10423746705055237, 0.10249097645282745, 0.39893341064453125)), Vector((0.11824847012758255, -0.013797004707157612, 0.5389683246612549)), Vector((0.12716044485569, -0.12644125521183014, 0.04689784720540047)), Vector((0.09840375930070877, -0.06402713805437088, 0.20216597616672516)), Vector((0.12293510884046555, 0.04328662529587746, 0.5436614155769348)), Vector((0.11369264870882034, -0.04819751903414726, 0.4687221944332123)), Vector((0.11369264870882034, 0.11330334097146988, 0.46720585227012634)), Vector((0.12059178948402405, 0.01474481076002121, 0.5413146615028381)), Vector((0.10896502435207367, 0.10789715498685837, 0.43306970596313477)), Vector((0.1208229586482048, 0.0711275190114975, 0.5362789630889893)), Vector((0.12137292325496674, 0.024258749559521675, 0.5420969724655151)), Vector((0.12215404957532883, 0.03377268835902214, 0.5428792238235474)), Vector((0.12200263142585754, 0.031928446143865585, 0.5427274107933044)), Vector((0.12168777734041214, 0.028093598783016205, 0.5424121618270874)), Vector((0.16844400763511658, 0.006501218769699335, 0.5227131247520447)), Vector((0.17869728803634644, 0.013499945402145386, 0.5144622921943665)), Vector((0.18942007422447205, 0.012828762643039227, 0.507378876209259)), Vector((0.25121834874153137, 0.012672999873757362, 0.3894071877002716)), Vector((0.23213855922222137, 0.01370337512344122, 0.4560083746910095)), Vector((0.2920149564743042, 0.013420850969851017, 0.2995007038116455)), Vector((0.1194201335310936, 0.0004739020951092243, 0.5401414632797241)), Vector((0.08076953142881393, -0.12213321030139923, 0.4137822985649109)), Vector((0.09962092339992523, -0.09587912261486053, 0.41476187109947205)), Vector((0.025475630536675453, -0.14646776020526886, 0.4156339168548584)), Vector((0.04931725189089775, -0.12792418897151947, 0.4222656488418579)), Vector((0.13619016110897064, -0.06962502747774124, 0.4069203734397888)), Vector((0.10638730973005295, -0.09381900727748871, 0.2600032687187195)), Vector((0.09162627160549164, -0.11402548104524612, 0.22844484448432922)), Vector((0.12485900521278381, -0.07289621978998184, 0.3523944318294525)), Vector((0.0515650138258934, -0.17324797809123993, 0.3577435314655304)), Vector((0.09949846565723419, -0.1584554761648178, 0.3572425842285156)), Vector((0.04503601789474487, -0.1475095897912979, 0.2034624069929123)), Vector((0.08095401525497437, -0.14789651334285736, 0.2081020623445511)), Vector((0.09041134268045425, -0.16864937543869019, 0.35856837034225464)), Vector((0.025475559756159782, -0.17411957681179047, 0.35564854741096497)), Vector((0.025475559756159782, -0.17213772237300873, 0.20919926464557648)), Vector((0.07929489016532898, -0.1445709764957428, 0.3829636573791504)), Vector((0.10055408626794815, -0.12940149009227753, 0.38448265194892883)), Vector((0.03980205953121185, -0.16504916548728943, 0.38515084981918335)), Vector((0.05807262659072876, -0.15043824911117554, 0.392400860786438)), Vector((0.11762526631355286, -0.10433240234851837, 0.3784733712673187)), Vector((0.10174057632684708, -0.1228729709982872, 0.2617470622062683)), Vector((0.09063740074634552, -0.13835778832435608, 0.23986919224262238)), Vector((0.10894184559583664, -0.10683920234441757, 0.33668839931488037)), Vector((0.05479174852371216, -0.160406231880188, 0.22404895722866058)), Vector((0.0823167935013771, -0.16070273518562317, 0.2300814837217331)), Vector((0.03980198875069618, -0.1862395703792572, 0.33918237686157227)), Vector((0.03980198875069618, -0.18110939860343933, 0.23092234134674072)), Vector((0.06526130437850952, -0.17335014045238495, 0.3562239110469818)), Vector((0.10925541073083878, -0.1433732807636261, 0.35273775458335876)), Vector((0.09779267013072968, -0.15727201104164124, 0.26523521542549133)), Vector((0.08786459267139435, -0.16888001561164856, 0.25524404644966125)), Vector((0.10274601727724075, -0.14525246620178223, 0.32141411304473877)), Vector((0.09612508863210678, -0.16739940643310547, 0.3119186758995056)), Vector((0.0646725744009018, -0.18927882611751556, 0.3159288167953491)), Vector((0.06280189752578735, -0.18026578426361084, 0.250968873500824)), Vector((0.08343573659658432, -0.18048806488513947, 0.2505607604980469)), Vector((0.08874143660068512, -0.18395987153053284, 0.302423357963562)), Vector((0.0515650138258934, -0.1891331523656845, 0.32328367233276367)), Vector((0.0515650138258934, -0.18014474213123322, 0.2511911690235138)), Vector((0.17721407115459442, -0.08921370655298233, 0.0018302679527550936)), Vector((0.17721407115459442, 0.09668142348527908, 0.0018302679527550936)), Vector((-0.0017742959316819906, -0.18089082837104797, 0.0018303036922588944)), Vector((-0.0005506797460839152, 0.18040265142917633, 0.0018303036922588944)), Vector((0.14851444959640503, -0.19666670262813568, 0.0018302679527550936)), Vector((0.14264507591724396, 0.1676180213689804, 0.0018302679527550936)), Vector((0.18843935430049896, 0.00343518378213048, 0.0018302679527550936)), Vector((0.18282665312290192, 0.05005830153822899, 0.0018302679527550936)), Vector((0.05983868986368179, -0.19563394784927368, 0.0018302679527550936)), Vector((0.0689430683851242, 0.16671417653560638, 0.0018302679527550936)), Vector((0.14601680636405945, 0.12600724399089813, 0.0018302679527550936)), Vector((0.1444541960954666, -0.1429401934146881, 0.0018302679527550936))]
edges = []
faces = [[141, 132, 1, 26], [99, 100, 10, 11], [140, 29, 156, 157], [22, 23, 4, 5], [23, 24, 3, 4], [133, 134, 7, 8], [134, 135, 6, 7], [103, 104, 20, 19], [102, 103, 19, 18], [3, 25, 160, 163], [137, 138, 17, 16], [105, 101, 15, 30], [73, 74, 24, 23], [72, 73, 23, 22], [107, 105, 30, 87], [27, 9, 169, 158], [106, 27, 158, 159], [143, 141, 26, 85], [37, 33, 42, 46], [33, 36, 45, 42], [76, 34, 43, 78], [31, 37, 46, 40], [25, 37, 31, 0], [112, 114, 35, 21], [58, 59, 49, 53], [59, 55, 52, 49], [82, 56, 50, 80], [57, 58, 53, 39], [38, 32, 41, 47], [90, 35, 44, 92], [89, 38, 47, 91], [150, 31, 40, 151], [61, 60, 48, 54], [96, 62, 51, 94], [95, 61, 54, 93], [153, 57, 39, 152], [151, 40, 57, 153], [91, 47, 61, 95], [92, 44, 62, 96], [47, 41, 60, 61], [40, 46, 58, 57], [78, 43, 56, 82], [42, 45, 55, 59], [46, 42, 59, 58], [54, 48, 65, 64], [53, 49, 70, 68], [49, 52, 69, 70], [80, 50, 63, 83], [94, 51, 66, 97], [93, 54, 64, 98], [152, 39, 67, 154], [39, 53, 68, 67], [3, 33, 37, 25], [3, 24, 36, 33], [74, 6, 34, 76], [85, 26, 38, 89], [26, 1, 32, 38], [88, 90, 32, 1], [24, 74, 76, 36], [119, 79, 84, 110], [52, 80, 83, 69], [45, 78, 82, 55], [117, 77, 81, 108], [108, 81, 79, 119], [115, 75, 77, 117], [55, 82, 80, 52], [149, 150, 75, 71], [36, 76, 78, 45], [8, 7, 73, 72], [7, 6, 74, 73], [21, 35, 90, 88], [6, 85, 89, 34], [50, 93, 98, 63], [48, 94, 97, 65], [41, 92, 96, 60], [43, 91, 95, 56], [56, 95, 93, 50], [60, 96, 94, 48], [34, 89, 91, 43], [32, 90, 92, 41], [135, 143, 85, 6], [104, 107, 87, 20], [12, 86, 107, 104], [10, 100, 166, 170], [86, 28, 105, 107], [28, 2, 101, 105], [14, 13, 103, 102], [13, 12, 104, 103], [138, 4, 161, 162], [16, 17, 100, 99], [35, 114, 116, 44], [127, 115, 117, 128], [62, 109, 118, 51], [130, 108, 119, 129], [44, 116, 109, 62], [128, 117, 108, 130], [51, 118, 111, 66], [129, 119, 110, 131], [71, 75, 115, 113], [122, 123, 114, 112], [126, 127, 123, 122], [118, 125, 121, 111], [116, 124, 120, 109], [109, 120, 125, 118], [114, 123, 124, 116], [113, 115, 127, 126], [125, 129, 131, 121], [124, 128, 130, 120], [120, 130, 129, 125], [123, 127, 128, 124], [113, 126, 148, 145], [126, 122, 147, 148], [122, 112, 146, 147], [71, 113, 145, 142], [21, 88, 144, 139], [20, 87, 143, 135], [149, 71, 142, 155], [87, 30, 141, 143], [29, 106, 159, 156], [112, 21, 139, 146], [25, 0, 136, 140], [88, 1, 132, 144], [5, 4, 138, 137], [9, 10, 170, 169], [19, 20, 135, 134], [18, 19, 134, 133], [30, 15, 132, 141], [0, 149, 155, 136], [0, 31, 150, 149], [79, 152, 154, 84], [77, 151, 153, 81], [81, 153, 152, 79], [75, 150, 151, 77], [161, 163, 178, 176], [160, 157, 172, 175], [170, 166, 179, 182], [158, 169, 181, 173], [159, 158, 173, 174], [162, 161, 176, 177], [169, 170, 182, 181], [163, 160, 175, 178], [17, 138, 162, 167], [4, 3, 163, 161], [100, 17, 167, 166], [25, 140, 157, 160], [182, 179, 190, 194], [173, 181, 193, 164], [174, 173, 164, 183], [177, 176, 185, 186], [181, 182, 194, 193], [178, 175, 184, 187], [172, 171, 168, 165], [180, 177, 186, 191], [156, 159, 174, 171], [166, 167, 180, 179], [167, 162, 177, 180], [157, 156, 171, 172], [190, 189, 193, 194], [186, 188, 192, 191], [188, 165, 168, 192], [189, 183, 164, 193], [192, 168, 183, 189], [191, 192, 189, 190], [187, 184, 165, 188], [185, 187, 188, 186], [175, 172, 165, 184], [176, 178, 187, 185], [171, 174, 183, 168], [179, 180, 191, 190], [16, 99, 203, 199], [102, 18, 200, 204], [8, 72, 202, 196], [99, 11, 197, 203], [14, 102, 204, 198], [72, 22, 201, 202], [137, 16, 199, 206], [18, 133, 205, 200], [22, 5, 195, 201], [5, 137, 206, 195], [133, 8, 196, 205]]


    
mesh = bpy.data.meshes.new(name="Blouse")
mesh.from_pydata(verts, edges, faces)
blouse = bpy.data.objects.new('blouse', mesh)


    
blouse_collection = bpy.data.collections.new('blouse_collection')
bpy.context.scene.collection.children.link(blouse_collection)
blouse_collection.objects.link(blouse)

