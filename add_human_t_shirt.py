bl_info = {
    "name": "Add Human Shirt",
    "author": "Christopher S. Francis",
    "version": (1, 2),
    "blender": (3, 5, 0),
    "location": "run script",
    "description": "Adds a new shrit to go with the add Human Mesh script",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh",
}


import bpy
from mathutils import Vector


verts = [Vector((0.17938609421253204, -0.009688089601695538, 0.530148983001709)), Vector((0.17938609421253204, 0.08943720906972885, 0.5321760177612305)), Vector((-0.005664553493261337, -0.048360299319028854, 0.5696512460708618)), Vector((-0.005664553493261337, 0.09560315310955048, 0.5696512460708618)), Vector((0.16070888936519623, -0.034062448889017105, 0.4121440649032593)), Vector((0.14885112643241882, -0.06431848555803299, 0.2871222496032715)), Vector((0.14154283702373505, -0.06864875555038452, 0.054520368576049805)), Vector((0.16070888936519623, 0.06553113460540771, 0.39682018756866455)), Vector((0.14939287304878235, 0.039755262434482574, 0.27700209617614746)), Vector((0.14549122750759125, 0.03975527361035347, 0.09528958797454834)), Vector((-0.005664522759616375, -0.1445205807685852, 0.41632723808288574)), Vector((-0.005664553493261337, -0.13746939599514008, 0.2550116777420044)), Vector((-0.005664553493261337, -0.13037936389446259, 0.057466745376586914)), Vector((-0.0056645842269063, 0.1256793886423111, 0.43767333030700684)), Vector((-0.005664553493261337, 0.09904509037733078, 0.2449554204940796)), Vector((-0.005664553493261337, 0.10687148571014404, 0.09769201278686523)), Vector((0.16767500340938568, -0.0614316388964653, -0.0044820308685302734)), Vector((0.16767500340938568, 0.05996319279074669, -0.003215193748474121)), Vector((-0.005664553493261337, -0.11623815447092056, -0.0010805130004882812)), Vector((-0.0056645842269063, 0.10925334692001343, 0.00017654895782470703)), Vector((0.08686075359582901, 0.09642995893955231, 0.561819314956665)), Vector((0.08596574515104294, -0.04999793693423271, 0.583341121673584)), Vector((0.10757944732904434, -0.13130955398082733, 0.054520368576049805)), Vector((0.06565000861883163, -0.13833358883857727, 0.25360119342803955)), Vector((0.07752218097448349, -0.14556071162223816, 0.3696500062942505)), Vector((0.058844976127147675, 0.10759275406599045, 0.09505832195281982)), Vector((0.06564994901418686, 0.11573392152786255, 0.24346661567687988)), Vector((0.07752218097448349, 0.1428317278623581, 0.43768298625946045)), Vector((0.09009932726621628, 0.11847450584173203, -0.008102595806121826)), Vector((0.0651230588555336, -0.11705838143825531, -0.0044820308685302734)), Vector((0.18412959575653076, 0.04024967923760414, 0.5472633838653564)), Vector((0.14736168086528778, -0.014620909467339516, 0.07550501823425293)), Vector((0.15497180819511414, -0.01231361459940672, 0.28164398670196533)), Vector((0.16650253534317017, 0.03444835543632507, 0.39707958698272705)), Vector((0.17342853546142578, -0.0008961098501458764, -0.0027214884757995605)), Vector((0.09029410779476166, 0.024367203935980797, 0.5753111839294434)), Vector((0.15460889041423798, -0.06504018604755402, 0.025019168853759766)), Vector((0.15460889041423798, 0.049859222024679184, 0.04592156410217285)), Vector((-0.005664553493261337, -0.12330875545740128, 0.02819305658340454)), Vector((-0.005664553493261337, 0.11202481389045715, 0.04893428087234497)), Vector((0.06537806242704391, 0.11142939329147339, 0.04347783327102661)), Vector((0.09544537216424942, -0.12418395280838013, 0.025019168853759766)), Vector((0.16039514541625977, -0.007758509833365679, 0.03639179468154907)), Vector((0.1752745360136032, -0.029332062229514122, 0.48223447799682617)), Vector((0.1752745360136032, 0.09041188657283783, 0.47393786907196045)), Vector((-0.005664553493261337, -0.104533851146698, 0.4934351444244385)), Vector((-0.005664553493261337, 0.10964275896549225, 0.5048564672470093)), Vector((0.08125872164964676, -0.10526307672262192, 0.4736124277114868)), Vector((0.08125872164964676, 0.12667043507099152, 0.5006438493728638)), Vector((0.18932518362998962, -0.008699534460902214, 0.523635745048523)), Vector((0.18932518362998962, 0.09042580425739288, 0.5256627798080444)), Vector((0.17064803838729858, -0.033073894679546356, 0.41297101974487305)), Vector((0.17064803838729858, 0.06651969254016876, 0.3976471424102783)), Vector((0.19406868517398834, 0.04123825579881668, 0.5407501459121704)), Vector((0.17644168436527252, 0.020611803978681564, 0.39790642261505127)), Vector((0.1852136254310608, -0.028343504294753075, 0.48306119441986084)), Vector((0.1852136254310608, 0.09140042960643768, 0.47476470470428467)), Vector((0.25179147720336914, -0.013757281936705112, 0.4052177667617798)), Vector((0.19957786798477173, -0.008699532598257065, 0.5163276195526123)), Vector((0.19957786798477173, 0.09042580425739288, 0.5183545351028442)), Vector((0.1809007227420807, -0.033073894679546356, 0.41297101974487305)), Vector((0.17369572818279266, 0.06651969254016876, 0.3976471424102783)), Vector((0.20432136952877045, 0.04123825579881668, 0.5334419012069702)), Vector((0.17948931455612183, 0.020611809566617012, 0.39790642261505127)), Vector((0.1954663097858429, -0.028343509882688522, 0.48306119441986084)), Vector((0.1954663097858429, 0.09140042960643768, 0.47476470470428467)), Vector((0.25354671478271484, 0.09748532623052597, 0.4063303470611572)), Vector((0.1869448870420456, -0.04111120477318764, 0.35385966300964355)), Vector((0.1805383712053299, 0.05401953309774399, 0.34979820251464844)), Vector((0.26974931359291077, 0.042284976691007614, 0.41120362281799316)), Vector((0.18459485471248627, 0.019137131050229073, 0.34577643871307373)), Vector((0.235187828540802, -0.03580258786678314, 0.381868839263916)), Vector((0.22800341248512268, 0.09857907891273499, 0.3773142099380493)), Vector((0.17676478624343872, 0.021485839039087296, 0.3744847774505615)), Vector((0.1724613606929779, 0.04959766939282417, 0.3763784170150757)), Vector((0.23770271241664886, -0.008699527941644192, 0.46952319145202637)), Vector((0.20775921642780304, -0.028343504294753075, 0.43265771865844727)), Vector((0.17113476991653442, -0.033073894679546356, 0.38212788105010986)), Vector((0.23850814998149872, 0.09042581915855408, 0.4711517095565796)), Vector((0.20446257293224335, 0.09140042960643768, 0.425991415977478)), Vector((0.2483145296573639, 0.04123826324939728, 0.4813896417617798)), Vector((0.2120635062456131, 0.05616413801908493, 0.28207194805145264)), Vector((0.26087620854377747, 0.10543288290500641, 0.3005465269088745)), Vector((0.30314144492149353, 0.10422351956367493, 0.3232264518737793)), Vector((0.3216261863708496, 0.04318946599960327, 0.32588326930999756)), Vector((0.301004558801651, -0.01877552643418312, 0.3223118782043457)), Vector((0.269622802734375, -0.04315067082643509, 0.30429017543792725)), Vector((0.21548637747764587, 0.017595257610082626, 0.2771192789077759)), Vector((0.2198631465435028, -0.04902030527591705, 0.28541016578674316)), Vector((0.1817578375339508, 0.015280799008905888, 0.5387061834335327)), Vector((0.0881299301981926, -0.012815365567803383, 0.5793261528015137)), Vector((0.14891910552978516, 0.012567180208861828, 0.08568263053894043)), Vector((0.15218234062194824, 0.013720829971134663, 0.27932310104370117)), Vector((0.163605734705925, 0.049989741295576096, 0.39695000648498535)), Vector((0.17055177688598633, 0.029533542692661285, -0.0029683709144592285)), Vector((0.1575019806623459, 0.021050361916422844, 0.0411565899848938)), Vector((0.1916969269514084, 0.01626935973763466, 0.5321929454803467)), Vector((0.17354482412338257, 0.050978291779756546, 0.39777672290802)), Vector((0.2019496113061905, 0.01626935787498951, 0.524884819984436)), Vector((0.17659251391887665, 0.036153197288513184, 0.39777672290802)), Vector((0.26077041029930115, 0.014263846911489964, 0.40821075439453125)), Vector((0.18256661295890808, 0.036578334867954254, 0.34778738021850586)), Vector((0.24300865828990936, 0.016269363462924957, 0.4754563570022583)), Vector((0.17461304366588593, 0.035541750490665436, 0.3754316568374634)), Vector((0.21377494931221008, 0.03687969967722893, 0.27959561347961426)), Vector((0.3113153576850891, 0.012206971645355225, 0.3240976333618164)), Vector((0.16799171268939972, 0.07055896520614624, 0.4393419027328491)), Vector((-0.005664553493261337, 0.11766107380390167, 0.4712648391723633)), Vector((0.07939045131206512, 0.134751096367836, 0.4691634178161621)), Vector((0.1817578375339508, 0.06484344601631165, 0.5397195816040039)), Vector((0.08857740461826324, 0.060398586094379425, 0.5685652494430542)), Vector((0.17793086171150208, 0.0715475082397461, 0.44016873836517334)), Vector((0.1916969269514084, 0.06583202630281448, 0.5332064628601074)), Vector((0.1881834864616394, 0.0715475082397461, 0.44016873836517334)), Vector((0.2019496113061905, 0.06583202630281448, 0.5258982181549072)), Vector((0.20427092909812927, 0.07629930227994919, 0.3635561466217041)), Vector((0.26164790987968445, 0.06988515704870224, 0.4087669849395752)), Vector((0.19206449389457703, 0.08532413840293884, 0.3932594060897827)), Vector((0.2434113323688507, 0.06583204865455627, 0.4762706756591797)), Vector((0.3123837113380432, 0.0737065002322197, 0.3245549201965332)), Vector((0.23646984994411469, 0.08079851418733597, 0.2913092374801636)), Vector((0.026642225682735443, -0.04893768951296806, 0.574478030204773)), Vector((0.027849970385432243, -0.13070733845233917, 0.056427955627441406)), Vector((0.019479356706142426, -0.13777409493923187, 0.25451433658599854)), Vector((0.02366521954536438, -0.144887313246727, 0.3998699188232422)), Vector((0.019293541088700294, -0.11652734875679016, -0.002279818058013916)), Vector((0.026957731693983078, 0.09589466452598572, 0.5668898820877075)), Vector((0.017080068588256836, 0.10712578147649765, 0.0967634916305542)), Vector((0.0194792952388525, 0.10492918640375137, 0.2444305419921875)), Vector((0.023665156215429306, 0.1317269206047058, 0.43767666816711426)), Vector((0.021686851978302002, 0.1198204904794693, -0.0027425289154052734)), Vector((0.01938343048095703, 0.11181487143039703, 0.04701042175292969)), Vector((0.02357175573706627, -0.12361735105514526, 0.027073979377746582)), Vector((0.02498263120651245, 0.11564632505178452, 0.5033712387084961)), Vector((0.02498263120651245, -0.10479097068309784, 0.4864461421966553)), Vector((0.02432389371097088, 0.12368662655353546, 0.4705239534378052)), Vector((0.24477723240852356, 0.02459232695400715, 0.4774341583251953)), Vector((0.2465459406375885, 0.03291529417037964, 0.4794119596481323)), Vector((0.3147522509098053, 0.02253447286784649, 0.32469284534454346)), Vector((0.31818917393684387, 0.032861970365047455, 0.3252880573272705)), Vector((0.18333901464939117, 0.0319267176091671, 0.5444109439849854)), Vector((0.1825484335422516, 0.023603761568665504, 0.5415585041046143)), Vector((0.0895727127790451, 0.011973013170063496, 0.5766494274139404)), Vector((0.08885131776332855, -0.00042117704288102686, 0.5779879093170166)), Vector((0.19327810406684875, 0.03291529044508934, 0.5378977060317993)), Vector((0.19248750805854797, 0.02459232322871685, 0.5350452661514282)), Vector((0.20353078842163086, 0.03291529044508934, 0.5305894613265991)), Vector((0.20274019241333008, 0.0245923213660717, 0.527737021446228)), Vector((0.2667563259601593, 0.03294460102915764, 0.4102060794830322)), Vector((0.26376330852508545, 0.023604223504662514, 0.4092082977294922)), Vector((0.24620307981967926, 0.031301919370889664, 0.47902846336364746)), Vector((0.31752294301986694, 0.030860021710395813, 0.32517266273498535)), Vector((0.18318572640419006, 0.030313340947031975, 0.5438579320907593)), Vector((0.08943285793066025, 0.009570450522005558, 0.5769089460372925)), Vector((0.19312487542629242, 0.031301915645599365, 0.5373446941375732)), Vector((0.20337755978107452, 0.031301915645599365, 0.530036449432373)), Vector((0.26617616415023804, 0.031134000048041344, 0.4100126028060913)), Vector((0.18286707997322083, 0.02695855312049389, 0.542708158493042)), Vector((0.08914206176996231, 0.004574637860059738, 0.5774483680725098)), Vector((0.19280622899532318, 0.027947114780545235, 0.536194920539856)), Vector((0.2030588537454605, 0.027947114780545235, 0.5288866758346558)), Vector((0.26496970653533936, 0.02736910991370678, 0.4096105098724365)), Vector((0.2454901933670044, 0.027947120368480682, 0.4782313108444214)), Vector((0.3161376714706421, 0.026697248220443726, 0.3249328136444092)), Vector((0.13312339782714844, 0.09293358772993088, 0.5469976663589478)), Vector((0.11328252404928207, 0.08609595894813538, 0.09356534481048584)), Vector((0.11466421186923981, 0.09423712641000748, 0.2587015628814697)), Vector((0.11911550164222717, 0.09676887840032578, 0.4212144613265991)), Vector((0.12888716161251068, 0.08921884745359421, -0.005658924579620361)), Vector((0.1326759159564972, -0.029843013733625412, 0.556745171546936)), Vector((0.12456114590167999, -0.09997916221618652, 0.054520368576049805)), Vector((0.11412251740694046, -0.1091134250164032, 0.2688215970993042)), Vector((0.11911556869745255, -0.08981158584356308, 0.3908970355987549)), Vector((0.125493124127388, -0.0892450138926506, -0.0044820308685302734)), Vector((0.1372118443250656, 0.032308440655469894, 0.5612872838973999)), Vector((0.12502716481685638, -0.09461208432912827, 0.025019168853759766)), Vector((0.11908756196498871, 0.08064430207014084, 0.044699668884277344)), Vector((0.1282666027545929, -0.0672975704073906, 0.47792351245880127)), Vector((0.1282666027545929, 0.10854117572307587, 0.48729097843170166)), Vector((0.1349438577890396, 0.001232715556398034, 0.5590161085128784)), Vector((0.12369105219841003, 0.10265501588582993, 0.4542527198791504)), Vector((0.13516762852668762, 0.06262101978063583, 0.5541423559188843)), Vector((0.13569986820220947, 0.011591288261115551, 0.5597732067108154)), Vector((0.13645583391189575, 0.02194986492395401, 0.5605301856994629)), Vector((0.13630932569503784, 0.019941894337534904, 0.5603833198547363)), Vector((0.13600459694862366, 0.01576659083366394, 0.5600782632827759)), Vector((0.18057197332382202, 0.0027963535394519567, 0.5344275236129761)), Vector((0.08704780787229538, -0.03140665218234062, 0.5813336372375488)), Vector((0.1905110627412796, 0.0037849131040275097, 0.5279144048690796)), Vector((0.2007637470960617, 0.003784914268180728, 0.5206061601638794)), Vector((0.2562810182571411, 0.0002532819053158164, 0.40671420097351074)), Vector((0.24035565555095673, 0.0037849186919629574, 0.47248971462249756)), Vector((0.3061599135398865, -0.0032842764630913734, 0.32320475578308105)), Vector((0.1338099241256714, -0.014305150136351585, 0.5578806400299072))]
edges = []
faces = [[178, 164, 1, 44], [134, 121, 2, 45], [132, 122, 12, 38], [122, 123, 11, 12], [123, 124, 10, 11], [42, 31, 6, 36], [31, 32, 5, 6], [32, 33, 4, 5], [176, 165, 9, 37], [165, 166, 8, 9], [166, 167, 7, 8], [128, 129, 27, 26], [127, 128, 26, 25], [131, 127, 25, 40], [171, 172, 24, 23], [170, 171, 23, 22], [175, 170, 22, 41], [181, 164, 20, 110], [177, 169, 21, 47], [133, 126, 20, 48], [183, 174, 35, 142], [92, 93, 33, 32], [91, 92, 32, 31], [95, 91, 31, 42], [94, 95, 42, 34], [173, 175, 41, 29], [130, 131, 40, 28], [168, 176, 37, 17], [34, 42, 36, 16], [125, 132, 38, 18], [135, 133, 48, 108], [172, 177, 47, 24], [124, 134, 45, 10], [180, 178, 44, 106], [55, 51, 60, 64], [51, 54, 63, 60], [97, 52, 61, 99], [49, 55, 64, 58], [43, 55, 49, 0], [140, 144, 53, 30], [76, 77, 67, 71], [77, 73, 70, 67], [103, 74, 68, 101], [75, 76, 71, 57], [56, 50, 59, 65], [112, 53, 62, 114], [111, 56, 65, 113], [188, 49, 58, 189], [79, 78, 66, 72], [118, 80, 69, 116], [117, 79, 72, 115], [191, 75, 57, 190], [189, 58, 75, 191], [113, 65, 79, 117], [114, 62, 80, 118], [65, 59, 78, 79], [58, 64, 76, 75], [99, 61, 74, 103], [60, 63, 73, 77], [64, 60, 77, 76], [72, 66, 83, 82], [71, 67, 88, 86], [67, 70, 87, 88], [101, 68, 81, 104], [116, 69, 84, 119], [115, 72, 82, 120], [190, 57, 85, 192], [57, 71, 86, 85], [4, 51, 55, 43], [4, 33, 54, 51], [93, 7, 52, 97], [106, 44, 56, 111], [44, 1, 50, 56], [109, 112, 50, 1], [33, 93, 97, 54], [149, 100, 105, 138], [70, 101, 104, 87], [63, 99, 103, 73], [147, 98, 102, 136], [136, 102, 100, 149], [145, 96, 98, 147], [73, 103, 101, 70], [186, 188, 96, 89], [54, 97, 99, 63], [17, 37, 95, 94], [37, 9, 91, 95], [9, 8, 92, 91], [8, 7, 93, 92], [193, 179, 90, 187], [30, 53, 112, 109], [7, 106, 111, 52], [68, 115, 120, 81], [66, 116, 119, 83], [59, 114, 118, 78], [61, 113, 117, 74], [74, 117, 115, 68], [78, 118, 116, 66], [52, 111, 113, 61], [50, 112, 114, 59], [167, 180, 106, 7], [129, 135, 108, 27], [174, 181, 110, 35], [13, 107, 135, 129], [24, 47, 134, 124], [107, 46, 133, 135], [29, 41, 132, 125], [19, 39, 131, 130], [46, 3, 126, 133], [39, 15, 127, 131], [15, 14, 128, 127], [14, 13, 129, 128], [23, 24, 124, 123], [22, 23, 123, 122], [41, 22, 122, 132], [47, 21, 121, 134], [53, 144, 146, 62], [159, 145, 147, 160], [80, 137, 148, 69], [162, 136, 149, 161], [62, 146, 137, 80], [160, 147, 136, 162], [69, 148, 139, 84], [161, 149, 138, 163], [89, 96, 145, 141], [152, 154, 144, 140], [179, 182, 143, 90], [184, 183, 142, 153], [185, 184, 153, 158], [157, 159, 154, 152], [148, 156, 151, 139], [146, 155, 150, 137], [137, 150, 156, 148], [144, 154, 155, 146], [141, 145, 159, 157], [182, 185, 158, 143], [156, 161, 163, 151], [155, 160, 162, 150], [150, 162, 161, 156], [154, 159, 160, 155], [141, 157, 185, 182], [157, 152, 184, 185], [152, 140, 183, 184], [89, 141, 182, 179], [30, 109, 181, 174], [27, 108, 180, 167], [186, 89, 179, 193], [108, 48, 178, 180], [4, 43, 177, 172], [28, 40, 176, 168], [16, 36, 175, 173], [140, 30, 174, 183], [43, 0, 169, 177], [109, 1, 164, 181], [36, 6, 170, 175], [6, 5, 171, 170], [5, 4, 172, 171], [26, 27, 167, 166], [25, 26, 166, 165], [40, 25, 165, 176], [48, 20, 164, 178], [0, 186, 193, 169], [169, 193, 187, 21], [0, 49, 188, 186], [100, 190, 192, 105], [98, 189, 191, 102], [102, 191, 190, 100], [96, 188, 189, 98]]


    
mesh = bpy.data.meshes.new(name="Shirt")
mesh.from_pydata(verts, edges, faces)
shirt = bpy.data.objects.new('shirt', mesh)


shirt.location.z += 0.949356

#bpy.ops.object.modifier_add(type='MIRROR')

bpy.data.collections["char_collection"].objects.link(shirt)

