bl_info = {
    "name": "Add Hair",
    "author": "Christopher S. Francis",
    "version": (1, 3),
    "blender": (3, 5, 0),
    "location": "run script",
    "description": "Adds a new Hair Mesh",
    "warning": "",
    "wiki_url": "https://github.com/francis-chris5/blender-human-starter-mesh/wiki",
    "category": "Add Mesh",
}


import bpy
from mathutils import Vector



verts = [Vector((0.06140472739934921, 0.06629181653261185, 1.6284159421920776)), Vector((-0.0006937895668670535, -0.0864025354385376, 1.8185884952545166)), Vector((-0.0004298181738704443, 0.07797814905643463, 1.816551685333252)), Vector((0.04057801142334938, 0.0649740993976593, 1.8156565427780151)), Vector((0.038535092025995255, -0.0763571709394455, 1.8139979839324951)), Vector((0.00017690728418529034, 0.017183402553200722, 1.8370153903961182)), Vector((0.052747540175914764, 0.017264176160097122, 1.820552945137024)), Vector((0.07350002974271774, 0.08027392625808716, 1.6775957345962524)), Vector((0.0714946985244751, 0.08414697647094727, 1.725486397743225)), Vector((0.06399568170309067, 0.08021897077560425, 1.774043083190918)), Vector((-0.0010832044063135982, 0.06713946908712387, 1.6222295761108398)), Vector((1.977919600903988e-05, 0.10038644075393677, 1.6728626489639282)), Vector((-0.0002159327268600464, 0.10187778621912003, 1.71906578540802)), Vector((-0.000225879717618227, 0.09605873376131058, 1.7714052200317383)), Vector((0.07674244791269302, 0.018894623965024948, 1.6343255043029785)), Vector((0.09458478540182114, 0.017374590039253235, 1.6819376945495605)), Vector((0.09399530291557312, 0.017245853319764137, 1.7308216094970703)), Vector((0.08492708951234818, 0.01733158715069294, 1.7800261974334717)), Vector((-0.0005980238784104586, -0.031548164784908295, 1.8342598676681519)), Vector((0.052253372967243195, -0.02698626182973385, 1.8239967823028564)), Vector((0.0871722549200058, -0.04881080985069275, 1.7280094623565674)), Vector((0.07647323608398438, -0.042206019163131714, 1.7756755352020264)), Vector((-0.00039921212010085583, 0.04889786243438721, 1.8307993412017822)), Vector((0.04907241091132164, 0.04146961867809296, 1.8211524486541748)), Vector((0.07069741934537888, 0.04049102962017059, 1.6319752931594849)), Vector((0.08511599153280258, 0.047844331711530685, 1.6799122095108032)), Vector((0.08650050312280655, 0.049660470336675644, 1.728237271308899)), Vector((0.07551612704992294, 0.047906484454870224, 1.7772362232208252)), Vector((0.07198305428028107, 0.07867090404033661, 1.6641050577163696)), Vector((-0.0004898253828287125, 0.09647165983915329, 1.6587451696395874)), Vector((0.09261209517717361, 0.017843477427959442, 1.6690733432769775)), Vector((0.08348752558231354, 0.04684215784072876, 1.6667077541351318)), Vector((0.015258567407727242, -0.08390002697706223, 1.8169666528701782)), Vector((0.015010908246040344, 0.07429427653551102, 1.816917896270752)), Vector((0.01923433132469654, 0.017161371186375618, 1.8317590951919556)), Vector((0.021086543798446655, 0.0676792562007904, 1.6245545148849487)), Vector((0.02603161707520485, 0.09417656064033508, 1.6745426654815674)), Vector((0.02523953467607498, 0.09638917446136475, 1.7212207317352295)), Vector((0.022720973938703537, 0.09124152362346649, 1.772139072418213)), Vector((0.01836104318499565, -0.029802123084664345, 1.8312485218048096)), Vector((0.017600879073143005, 0.046003274619579315, 1.8279699087142944)), Vector((0.025112686678767204, 0.09107811003923416, 1.6606879234313965)), Vector((0.00018079299479722977, 0.0004930534050799906, 1.836059331893921)), Vector((-0.0003560050390660763, -0.015190948732197285, 1.8352270126342773)), Vector((0.05249181389808655, 0.0021356320939958096, 1.8218001127243042)), Vector((0.052455369383096695, -0.012091775424778461, 1.8228650093078613)), Vector((0.09162179380655289, -0.006607317365705967, 1.6812015771865845)), Vector((0.09172208607196808, -0.005943777970969677, 1.7296602725982666)), Vector((0.08946646004915237, -0.02733832225203514, 1.7287399768829346)), Vector((0.08204026520252228, -0.003703311551362276, 1.7786893844604492)), Vector((0.07933814078569412, -0.02284627966582775, 1.7770411968231201)), Vector((0.08984026312828064, -0.006667906418442726, 1.6691232919692993)), Vector((0.0191957987844944, 0.0013602100079879165, 1.8315526247024536)), Vector((0.018590744584798813, -0.013796558603644371, 1.831471562385559)), Vector((0.07036101818084717, 0.08376896381378174, 1.732191801071167)), Vector((-0.0002527865581214428, 0.10109759867191315, 1.7264612913131714)), Vector((0.09297154098749161, 0.017286965623497963, 1.736474871635437)), Vector((0.085886150598526, -0.04800712317228317, 1.7337900400161743)), Vector((0.08514144271612167, 0.04953162372112274, 1.7343864440917969)), Vector((0.024805013090372086, 0.09572157263755798, 1.7283892631530762)), Vector((0.0882832333445549, -0.026825588196516037, 1.7343010902404785)), Vector((0.09063098579645157, -0.005700094159692526, 1.7349588871002197)), Vector((7.7828299254179e-06, -0.002547911833971739, 1.8359190225601196)), Vector((0.052506569772958755, -0.0006260606460273266, 1.821990966796875)), Vector((0.08153870701789856, -0.007415942847728729, 1.7783249616622925)), Vector((0.019006822258234024, -0.0015776242362335324, 1.8315587043762207)), Vector((0.09018244594335556, -0.009810262359678745, 1.734151005744934)), Vector((0.07248196005821228, 0.08227121829986572, 1.7015526294708252)), Vector((-7.777311839163303e-05, 0.10117632150650024, 1.6958272457122803)), Vector((0.09432714432477951, 0.017307696864008904, 1.7069023847579956)), Vector((0.08658602833747864, -0.04932199418544769, 1.7037543058395386)), Vector((0.08584368228912354, 0.048747316002845764, 1.7042886018753052)), Vector((0.025662532076239586, 0.09531193226575851, 1.6977744102478027)), Vector((0.08915442228317261, -0.027723688632249832, 1.704746961593628)), Vector((0.09171635657548904, -0.006199799478054047, 1.7060095071792603)), Vector((-0.00013155164197087288, -0.008869192562997341, 1.835564374923706)), Vector((0.052474211901426315, -0.006357279140502214, 1.8224329948425293)), Vector((0.08042746037244797, -0.015130121260881424, 1.7777093648910522)), Vector((0.018841732293367386, -0.007687301374971867, 1.8315064907073975)), Vector((0.0892498642206192, -0.018323583528399467, 1.7338546514511108)), Vector((0.0731639564037323, 0.08094540238380432, 1.6854077577590942)), Vector((-1.6577541828155518e-06, 0.10068619251251221, 1.679891586303711)), Vector((0.09452405571937561, 0.01739398017525673, 1.6907453536987305)), Vector((0.08533771336078644, 0.04814915731549263, 1.688144326210022)), Vector((0.02593505196273327, 0.0945606604218483, 1.6817654371261597)), Vector((0.09167543053627014, -0.006441864650696516, 1.6899197101593018)), Vector((0.09052903950214386, -0.006666252855211496, 1.6789494752883911)), Vector((0.06955824792385101, 0.08270377665758133, 1.7442407608032227)), Vector((-0.0001366725191473961, 0.09961804747581482, 1.7396053075790405)), Vector((0.09386017918586731, 0.0173291377723217, 1.7490026950836182)), Vector((0.08541613817214966, -0.046340301632881165, 1.745928168296814)), Vector((0.08459314703941345, 0.04915151000022888, 1.7466434240341187)), Vector((0.020442333072423935, 0.09444700926542282, 1.7410906553268433)), Vector((0.08821559697389603, -0.025822646915912628, 1.746924877166748)), Vector((0.09103697538375854, -0.005301087163388729, 1.747733473777771)), Vector((0.09048397094011307, -0.009281205013394356, 1.7476290464401245)), Vector((0.08935462683439255, -0.01755104772746563, 1.747249960899353)), Vector((-0.000687478925101459, -0.05996982753276825, 1.829168677330017)), Vector((0.04799198731780052, -0.053831834346055984, 1.8199918270111084)), Vector((0.08302555233240128, -0.07986917346715927, 1.7272984981536865)), Vector((0.07315469533205032, -0.07102157920598984, 1.7735258340835571)), Vector((0.01681644842028618, -0.05788269266486168, 1.8268470764160156)), Vector((0.0818958431482315, -0.07857799530029297, 1.7323741912841797)), Vector((0.08111045509576797, -0.07630271464586258, 1.7441157102584839)), Vector((0.04986478388309479, 0.05309901386499405, 1.6380480527877808)), Vector((0.00011578819248825312, -0.07913213968276978, 1.8003299236297607)), Vector((-0.0001481771469116211, 0.06344720721244812, 1.8034791946411133)), Vector((0.031907711178064346, 0.05372782051563263, 1.8015729188919067)), Vector((0.0339084155857563, -0.06916332244873047, 1.7959191799163818)), Vector((-0.0007549072615802288, 0.015912959352135658, 1.817814588546753)), Vector((0.04100959002971649, 0.0159202478826046, 1.8044155836105347)), Vector((0.05961201339960098, 0.06603698432445526, 1.6797009706497192)), Vector((0.0584561824798584, 0.06903386116027832, 1.7242251634597778)), Vector((0.05175255984067917, 0.06591750681400299, 1.7672922611236572)), Vector((0.0005052081542089581, 0.05128303915262222, 1.6340610980987549)), Vector((-0.0005977805703878403, 0.08126667141914368, 1.6756988763809204)), Vector((-0.0003620607312768698, 0.08243993669748306, 1.7184323072433472)), Vector((-0.00035211420617997646, 0.07711409777402878, 1.7669873237609863)), Vector((0.058926232159137726, 0.014230224303901196, 1.6421246528625488)), Vector((0.07470161467790604, 0.015765152871608734, 1.6833760738372803)), Vector((0.07413512468338013, 0.015908779576420784, 1.7288761138916016)), Vector((0.06699550896883011, 0.015837939456105232, 1.7712953090667725)), Vector((2.001994289457798e-05, -0.029433734714984894, 1.8147584199905396)), Vector((0.04053519666194916, -0.02504679374396801, 1.807905673980713)), Vector((0.06753376126289368, -0.046370089054107666, 1.7251160144805908)), Vector((0.058286622166633606, -0.03940076380968094, 1.767841100692749)), Vector((-0.0001787850633263588, 0.043231092393398285, 1.8121068477630615)), Vector((0.03809061273932457, 0.03670002520084381, 1.8051321506500244)), Vector((0.0527716688811779, 0.035766810178756714, 1.6394819021224976)), Vector((0.06608323007822037, 0.04188099130988121, 1.681393027305603)), Vector((0.0675530657172203, 0.04350726678967476, 1.726467490196228)), Vector((0.058319296687841415, 0.04174651578068733, 1.769092321395874)), Vector((0.05891921743750572, 0.06491656601428986, 1.670441746711731)), Vector((-8.817599155008793e-05, 0.0787845328450203, 1.6671241521835327)), Vector((0.07327327877283096, 0.015294759534299374, 1.6734907627105713)), Vector((0.0649062991142273, 0.04152068495750427, 1.6718478202819824)), Vector((0.011163881048560143, -0.07665973156690598, 1.7987784147262573)), Vector((0.010545916855335236, 0.060689326375722885, 1.8029546737670898)), Vector((0.013822304084897041, 0.015966041013598442, 1.8125423192977905)), Vector((0.01814456284046173, 0.051084667444229126, 1.635323166847229)), Vector((0.020900677889585495, 0.07501567900180817, 1.6770987510681152)), Vector((0.020578201860189438, 0.07695038616657257, 1.7205836772918701)), Vector((0.018089234828948975, 0.07239890098571777, 1.7672910690307617)), Vector((0.014354098588228226, -0.028024619445204735, 1.811734914779663)), Vector((0.013130828738212585, 0.04120394587516785, 1.809075951576233)), Vector((0.02104049362242222, 0.07301240414381027, 1.668241024017334)), Vector((-0.0007587943691760302, 0.001243889331817627, 1.81683349609375)), Vector((-0.00022199773229658604, -0.014431527815759182, 1.8157286643981934)), Vector((0.04094246029853821, 0.002642964944243431, 1.805479645729065)), Vector((0.04065605625510216, -0.011535453610122204, 1.8067259788513184)), Vector((0.07186581939458847, -0.003867647610604763, 1.6826833486557007)), Vector((0.07193353772163391, -0.003680103225633502, 1.727846622467041)), Vector((0.06971435993909836, -0.02506406605243683, 1.7265760898590088)), Vector((0.06416141986846924, -0.001385933137498796, 1.7700304985046387)), Vector((0.061142630875110626, -0.02050173468887806, 1.7690770626068115)), Vector((0.07026158273220062, -0.0038151871412992477, 1.672045111656189)), Vector((0.013747007586061954, 0.0014491492183879018, 1.8123093843460083)), Vector((0.014238230884075165, -0.013712134212255478, 1.8119510412216187)), Vector((0.05776557698845863, 0.06850704550743103, 1.7292885780334473)), Vector((-0.00032520690001547337, 0.08178859949111938, 1.7239962816238403)), Vector((0.07307704538106918, 0.015869582071900368, 1.7349916696548462)), Vector((0.06625783443450928, -0.045430220663547516, 1.7309459447860718)), Vector((0.0663151666522026, 0.04318465292453766, 1.7320871353149414)), Vector((0.020369522273540497, 0.0763721615076065, 1.7259547710418701)), Vector((0.06849562376737595, -0.02441379427909851, 1.7326781749725342)), Vector((0.07078272849321365, -0.003341326955705881, 1.7342638969421387)), Vector((-0.0005857842043042183, -0.0017940490506589413, 1.8165982961654663)), Vector((0.04086511954665184, -0.0001017021422740072, 1.805736780166626)), Vector((0.06355400383472443, -0.0050896164029836655, 1.7698906660079956)), Vector((0.013913917355239391, -0.0014900540700182319, 1.812218189239502)), Vector((0.07033281773328781, -0.007411072961986065, 1.734636902809143)), Vector((0.05904949828982353, 0.06747466325759888, 1.7023470401763916)), Vector((-0.0005002203397452831, 0.08180910348892212, 1.6965255737304688)), Vector((0.0743812695145607, 0.015839489176869392, 1.7069834470748901)), Vector((0.06671200692653656, -0.04712064564228058, 1.704175591468811)), Vector((0.06678271293640137, 0.04269921034574509, 1.7046042680740356)), Vector((0.020712481811642647, 0.07595396786928177, 1.6986496448516846)), Vector((0.06928040087223053, -0.025522340089082718, 1.7051682472229004)), Vector((0.07185526937246323, -0.0038496237248182297, 1.7058910131454468)), Vector((-0.00044645066373050213, -0.008113027550280094, 1.8161721229553223)), Vector((0.04076734557747841, -0.005820217076689005, 1.8062262535095215)), Vector((0.0623592808842659, -0.012796664610505104, 1.769457459449768)), Vector((0.014033127576112747, -0.007600884884595871, 1.8120932579040527)), Vector((0.06939719617366791, -0.01590677537024021, 1.734028935432434)), Vector((0.059482425451278687, 0.06637749075889587, 1.6861768960952759)), Vector((-0.0005763357039541006, 0.08135943114757538, 1.6806161403656006)), Vector((0.07459206879138947, 0.015747956931591034, 1.6908252239227295)), Vector((0.06628197431564331, 0.0420832522213459, 1.688433289527893)), Vector((0.020833062008023262, 0.07524251192808151, 1.6826478242874146)), Vector((0.0718369334936142, -0.003907730337232351, 1.6898105144500732)), Vector((0.07095037400722504, -0.003813533578068018, 1.6818712949752808)), Vector((0.0566537119448185, 0.0677303746342659, 1.7411961555480957)), Vector((-0.0004413288552314043, 0.08035413920879364, 1.7372328042984009)), Vector((0.07408423721790314, 0.015831302851438522, 1.7464203834533691)), Vector((0.06592127680778503, -0.043547868728637695, 1.742442011833191)), Vector((0.0658978521823883, 0.042645782232284546, 1.7437866926193237)), Vector((0.01588549092411995, 0.07511072605848312, 1.7387791872024536)), Vector((0.06865748018026352, -0.02304932475090027, 1.7437961101531982)), Vector((0.07137176394462585, -0.0025546811521053314, 1.7453383207321167)), Vector((0.07085170596837997, -0.006525397300720215, 1.7449871301651)), Vector((0.06974976509809494, -0.014788239262998104, 1.7444185018539429)), Vector((0.00010947755072265863, -0.05452650040388107, 1.8102871179580688)), Vector((0.03768990561366081, -0.049134980887174606, 1.8035051822662354)), Vector((0.063791923224926, -0.07714291661977768, 1.7225408554077148)), Vector((0.054840974509716034, -0.06797335296869278, 1.7660883665084839)), Vector((0.012752345763146877, -0.052548598498106, 1.8080048561096191)), Vector((0.06237706542015076, -0.0758197158575058, 1.7289965152740479)), Vector((0.06160346418619156, -0.07347416132688522, 1.7407280206680298))]
edges = []
faces = [[27, 9, 3, 23], [49, 17, 6, 44], [40, 33, 2, 22], [52, 34, 5, 42], [38, 13, 2, 33], [41, 29, 11, 36], [72, 68, 12, 37], [92, 88, 13, 38], [51, 30, 15, 46, 86], [74, 69, 16, 47], [94, 89, 17, 49], [31, 28, 7, 25], [71, 67, 8, 26], [91, 87, 9, 27], [103, 90, 21, 100], [101, 39, 18, 97], [100, 21, 19, 98], [89, 91, 27, 17], [69, 71, 26, 16], [30, 31, 25, 15], [34, 40, 22, 5], [17, 27, 23, 6], [14, 24, 31, 30], [24, 0, 28, 31], [35, 10, 29, 41], [0, 35, 41, 28], [6, 23, 40, 34], [98, 19, 39, 101], [87, 92, 38, 9], [67, 72, 37, 8], [28, 41, 36, 7], [9, 38, 33, 3], [44, 6, 34, 52], [23, 3, 33, 40], [19, 45, 53, 39], [63, 44, 52, 65], [90, 93, 50, 21], [95, 94, 49, 64], [70, 73, 48, 20], [39, 53, 43, 18], [65, 52, 42, 62], [21, 50, 45, 19], [64, 49, 44, 63], [20, 48, 60, 57], [8, 37, 59, 54], [16, 26, 58, 56], [99, 20, 57, 102], [26, 8, 54, 58], [47, 16, 56, 61], [37, 12, 55, 59], [77, 64, 63, 76], [78, 65, 62, 75], [96, 95, 64, 77], [76, 63, 65, 78], [80, 84, 72, 67], [82, 83, 71, 69], [83, 80, 67, 71], [85, 82, 69, 74], [84, 81, 68, 72], [45, 76, 78, 53], [93, 96, 77, 50], [53, 78, 75, 43], [50, 77, 76, 45], [36, 11, 81, 84], [46, 15, 82, 85], [25, 7, 80, 83], [15, 25, 83, 82], [7, 36, 84, 80], [60, 79, 96, 93], [79, 66, 95, 96], [66, 61, 94, 95], [57, 60, 93, 90], [54, 59, 92, 87], [56, 58, 91, 89], [102, 57, 90, 103], [58, 54, 87, 91], [61, 56, 89, 94], [59, 55, 88, 92], [4, 98, 101, 32], [32, 101, 97, 1], [131, 127, 107, 113], [153, 148, 110, 121], [144, 126, 106, 137], [156, 146, 109, 138], [142, 137, 106, 117], [145, 140, 115, 133], [176, 141, 116, 172], [196, 142, 117, 192], [155, 190, 150, 119, 134], [178, 151, 120, 173], [198, 153, 121, 193], [135, 129, 111, 132], [175, 130, 112, 171], [195, 131, 113, 191], [207, 204, 125, 194], [205, 201, 122, 143], [204, 202, 123, 125], [193, 121, 131, 195], [173, 120, 130, 175], [134, 119, 129, 135], [138, 109, 126, 144], [121, 110, 127, 131], [118, 134, 135, 128], [128, 135, 132, 104], [139, 145, 133, 114], [104, 132, 145, 139], [110, 138, 144, 127], [202, 205, 143, 123], [191, 113, 142, 196], [171, 112, 141, 176], [132, 111, 140, 145], [113, 107, 137, 142], [148, 156, 138, 110], [127, 144, 137, 107], [123, 143, 157, 149], [167, 169, 156, 148], [194, 125, 154, 197], [199, 168, 153, 198], [174, 124, 152, 177], [143, 122, 147, 157], [169, 166, 146, 156], [125, 123, 149, 154], [168, 167, 148, 153], [124, 161, 164, 152], [112, 158, 163, 141], [120, 160, 162, 130], [203, 206, 161, 124], [130, 162, 158, 112], [151, 165, 160, 120], [141, 163, 159, 116], [181, 180, 167, 168], [182, 179, 166, 169], [200, 181, 168, 199], [180, 182, 169, 167], [184, 171, 176, 188], [186, 173, 175, 187], [187, 175, 171, 184], [189, 178, 173, 186], [188, 176, 172, 185], [149, 157, 182, 180], [197, 154, 181, 200], [157, 147, 179, 182], [154, 149, 180, 181], [140, 188, 185, 115], [150, 189, 186, 119], [129, 187, 184, 111], [119, 186, 187, 129], [111, 184, 188, 140], [164, 197, 200, 183], [183, 200, 199, 170], [170, 199, 198, 165], [161, 194, 197, 164], [158, 191, 196, 163], [160, 193, 195, 162], [206, 207, 194, 161], [162, 195, 191, 158], [165, 198, 193, 160], [163, 196, 192, 159], [108, 136, 205, 202], [136, 105, 201, 205], [2, 13, 117, 106], [22, 2, 106, 126], [24, 14, 118, 128], [29, 10, 114, 133], [14, 30, 134, 118], [4, 32, 136, 108], [10, 35, 139, 114], [18, 43, 147, 122], [30, 51, 155, 134], [55, 12, 116, 159], [60, 48, 152, 164], [62, 42, 146, 166], [12, 68, 172, 116], [70, 20, 124, 174], [73, 70, 174, 177], [75, 62, 166, 179], [79, 60, 164, 183], [68, 81, 185, 172], [85, 74, 178, 189], [86, 46, 150, 190], [97, 18, 122, 201], [98, 4, 108, 202], [20, 99, 203, 124], [100, 98, 202, 204], [103, 100, 204, 207], [88, 55, 159, 192], [0, 24, 128, 104], [35, 0, 104, 139], [48, 73, 177, 152], [5, 22, 126, 109], [11, 29, 133, 115], [32, 1, 105, 136], [42, 5, 109, 146], [102, 103, 207, 206], [47, 61, 165, 151], [61, 66, 170, 165], [74, 47, 151, 178], [43, 75, 179, 147], [81, 11, 115, 185], [51, 86, 190, 155], [13, 88, 192, 117], [1, 97, 201, 105], [99, 102, 206, 203], [46, 85, 189, 150], [66, 79, 183, 170]]


    
mesh = bpy.data.meshes.new(name="Hair")
mesh.from_pydata(verts, edges, faces)
hair = bpy.data.objects.new('hair', mesh)


    
man_collection = bpy.data.collections.new('man_collection')
bpy.context.scene.collection.children.link(man_collection)
man_collection.objects.link(hair)

