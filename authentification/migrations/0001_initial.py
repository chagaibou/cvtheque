# Generated by Django 5.1.6 on 2025-03-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("date_de_naissance", models.DateField()),
                (
                    "genre",
                    models.CharField(
                        choices=[("HOMME", "Homme"), ("FEMME", "Femme")], max_length=5
                    ),
                ),
                (
                    "situation_matrimoniale",
                    models.CharField(
                        choices=[
                            ("celibataire", "Célibataire sans enfants"),
                            ("marie", "Marié(e)"),
                            ("veuf", "Veuf/Veuve"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "nationalite",
                    models.CharField(
                        choices=[("Malien", "Malien"), ("Autres", "Autres")],
                        max_length=50,
                    ),
                ),
                ("residence_legale", models.CharField(max_length=100)),
                (
                    "disponibilite",
                    models.CharField(
                        choices=[
                            ("disponible", "Disponible"),
                            ("non_disponible", "Non disponible"),
                        ],
                        max_length=20,
                    ),
                ),
                ("telephone", models.CharField(max_length=15, unique=True)),
                ("date_ajout", models.DateTimeField(auto_now_add=True)),
                (
                    "region",
                    models.CharField(
                        choices=[
                            ("1", "Kayes"),
                            ("2", "Kita"),
                            ("3", "Nioro"),
                            ("4", "Koulikoro"),
                            ("5", "Dioila"),
                            ("6", "Nara"),
                            ("7", "Sikasso"),
                            ("8", "Bougouni"),
                            ("9", "Koutiala"),
                            ("10", "Segou"),
                            ("11", "San"),
                            ("12", "Mopti"),
                            ("13", "Bandiagara"),
                            ("14", "Douentza"),
                            ("15", "Tombouctou"),
                            ("16", "Gao"),
                            ("17", "Kidal"),
                            ("18", "Taoudenni"),
                            ("19", "Menaka"),
                            ("90", "Bamako"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "cercle",
                    models.CharField(
                        choices=[
                            ("101", "Kayes"),
                            ("102", "Diamou"),
                            ("103", "Aourou"),
                            ("104", "Ambidedi"),
                            ("105", "Segala"),
                            ("106", "Sadiola"),
                            ("107", "Bafoulabe"),
                            ("108", "Oussoubidiagna"),
                            ("109", "Kenieba"),
                            ("110", "Yelimane"),
                            ("201", "Kita"),
                            ("202", "Sagabari"),
                            ("203", "Sefeto"),
                            ("204", "Sebekoro"),
                            ("205", "Sirakoro"),
                            ("206", "Toukoto"),
                            ("301", "Diema"),
                            ("302", "Bema"),
                            ("303", "Diangounte Camara"),
                            ("304", "Sandare"),
                            ("305", "Nioro"),
                            ("306", "Troungoumbe"),
                            ("401", "Koulikoro"),
                            ("402", "Nyamina"),
                            ("403", "Banamba"),
                            ("404", "Kangaba"),
                            ("405", "Kati"),
                            ("406", "Neguela"),
                            ("407", "Siby"),
                            ("408", "Kolokani"),
                            ("501", "Dioila"),
                            ("502", "Banco"),
                            ("503", "Beleko"),
                            ("504", "Fana"),
                            ("505", "Mena"),
                            ("506", "Massigui"),
                            ("601", "Nara"),
                            ("602", "Balle"),
                            ("603", "Dilly"),
                            ("604", "Fallou"),
                            ("605", "Guire"),
                            ("606", "Mourdiah"),
                            ("701", "Sikasso"),
                            ("702", "Niena"),
                            ("703", "Danderesso"),
                            ("704", "Kignan"),
                            ("705", "Klela"),
                            ("706", "Lobougoula"),
                            ("707", "Kadiolo"),
                            ("708", "Loulouni"),
                            ("801", "Selingue"),
                            ("802", "Ouelessebougou"),
                            ("803", "Bougouni"),
                            ("804", "Koumantou"),
                            ("805", "Garalo"),
                            ("806", "Dogo"),
                            ("807", "Kolondieba"),
                            ("808", "Fakola"),
                            ("809", "Kadiana"),
                            ("810", "Yanfolila"),
                            ("901", "Koutiala"),
                            ("902", "Konseguela"),
                            ("903", "Zangasso"),
                            ("904", "Kouniana"),
                            ("905", "Molobala"),
                            ("906", "M’Pessoba"),
                            ("907", "Yorosso"),
                            ("908", "Koury"),
                            ("1001", "Segou"),
                            ("1002", "Markala"),
                            ("1003", "Dioro"),
                            ("1004", "Farako"),
                            ("1005", "Baroueli"),
                            ("1006", "Bla"),
                            ("1007", "Macina"),
                            ("1008", "Niono"),
                            ("1009", "Sokolo"),
                            ("1010", "Nampala"),
                            ("1101", "Yangasso"),
                            ("1102", "San"),
                            ("1103", "Kimparana"),
                            ("1104", "Sy"),
                            ("1105", "Tominian"),
                            ("1106", "Mandiakuy"),
                            ("1107", "Fangasso"),
                            ("1201", "Mopti"),
                            ("1202", "Konna"),
                            ("1203", "Korientze"),
                            ("1204", "Djenne"),
                            ("1205", "Sofara"),
                            ("1206", "Tenenkou"),
                            ("1207", "Youwarou"),
                            ("1301", "Bandiagara"),
                            ("1302", "Ningari"),
                            ("1303", "Kendie"),
                            ("1304", "Sangha"),
                            ("1305", "Kani"),
                            ("1306", "Bankass"),
                            ("1307", "Diallassagou"),
                            ("1308", "Sokoura"),
                            ("1309", "Koro"),
                            ("1401", "Douentza"),
                            ("1402", "Bore"),
                            ("1403", "Tombouctou"),
                            ("1501", "Ber"),
                            ("1502", "Dire"),
                            ("1503", "Goundam"),
                            ("1504", "Bintagoungou"),
                            ("1505", "Gargando"),
                            ("1506", "Tonka"),
                            ("1507", "Gourma-Rharous"),
                            ("1508", "Bambara-Maoude"),
                            ("1509", "Niafunke"),
                            ("1510", "Sarafere"),
                            ("1511", "Lere"),
                            ("1601", "Gao"),
                            ("1602", "Gabero"),
                            ("1603", "Djebock"),
                            ("1604", "Soni Aliber"),
                            ("1605", "Ansongo"),
                            ("1606", "Tessit"),
                            ("1607", "Bourem"),
                            ("1608", "Bamba"),
                            ("1701", "Kidal"),
                            ("1702", "Anefif"),
                            ("1703", "Abeibara"),
                            ("1704", "Tessalit"),
                            ("1705", "Aguel-Hoc"),
                            ("1706", "Tin-Essako"),
                            ("1801", "Taoudenni"),
                            ("1802", "Achouratt"),
                            ("1803", "Al-Ourche"),
                            ("1804", "Araouane"),
                            ("1805", "Bou-Djebeha"),
                            ("1806", "Foum-Elba"),
                            ("1901", "Menaka"),
                            ("1902", "Anderamboukane"),
                            ("1903", "Inekar"),
                            ("1904", "Inlamawane"),
                            ("1905", "Tidermene"),
                            ("9001", "Bamako"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "commune",
                    models.CharField(
                        choices=[
                            ("2", "Kayes"),
                            ("3", "Bangassi"),
                            ("4", "Colimbine"),
                            ("5", "Diamou"),
                            ("6", "Djelebou"),
                            ("7", "Fegui"),
                            ("8", "Gory Gopela"),
                            ("9", "Goumera"),
                            ("10", "Karakoro"),
                            ("11", "Kemene Tambo"),
                            ("12", "Khouloum"),
                            ("13", "Kouniakary"),
                            ("14", "Koussane"),
                            ("15", "Liberte Dembaya"),
                            ("16", "Marena Diombougou"),
                            ("17", "Marintoumania"),
                            ("18", "Sadiola"),
                            ("19", "Same Diongoma"),
                            ("20", "Segala"),
                            ("21", "Sero Diamanou"),
                            ("22", "Somankidy"),
                            ("23", "Sony"),
                            ("24", "Bafoulabe"),
                            ("25", "Bamafele"),
                            ("26", "Diakon"),
                            ("27", "Diallan"),
                            ("28", "Gounfan"),
                            ("29", "Kontela"),
                            ("30", "Koundian"),
                            ("31", "Mahina"),
                            ("32", "Sidibela"),
                            ("33", "Tomora"),
                            ("34", "Kenieba"),
                            ("35", "Baye"),
                            ("36", "Dabia"),
                            ("37", "Dialafara"),
                            ("38", "Dombia"),
                            ("39", "Falea"),
                            ("40", "Guenegore"),
                            ("41", "Kassama"),
                            ("42", "Sagalo"),
                            ("43", "Sitakilly"),
                            ("44", "Guidime"),
                            ("45", "Fanga"),
                            ("46", "Kirane Kaniaga"),
                            ("47", "Soumpou"),
                            ("48", "Toya"),
                            ("49", "Kita"),
                            ("50", "Badia"),
                            ("51", "Bendougouba"),
                            ("52", "Benkady Founia"),
                            ("53", "Bougaribaya"),
                            ("54", "Didenko"),
                            ("55", "Djidian"),
                            ("56", "Djougoun"),
                            ("57", "Gadougou 1"),
                            ("58", "Guemoukouraba"),
                            ("59", "Kassaro"),
                            ("60", "Kita Nord"),
                            ("61", "Kita Ouest"),
                            ("62", "Kokofata"),
                            ("63", "Kotouba"),
                            ("64", "Koulou"),
                            ("65", "Kourouninkoto"),
                            ("66", "Madina"),
                            ("67", "Makono"),
                            ("68", "Namala Guimbala"),
                            ("69", "Niantanso"),
                            ("70", "Sebekoro"),
                            ("71", "Sefeto Nord"),
                            ("72", "Sefeto Ouest"),
                            ("73", "Tambaga"),
                            ("74", "Toukoto"),
                            ("75", "Diema"),
                            ("76", "Bema"),
                            ("77", "Diangounte Camara"),
                            ("78", "Dianguirde"),
                            ("79", "Dieoura"),
                            ("80", "Fassoudebe"),
                            ("81", "Fatao"),
                            ("82", "Gomitradougou"),
                            ("83", "Groumera"),
                            ("84", "Guedebine"),
                            ("85", "Lakamane"),
                            ("86", "Lambidou"),
                            ("87", "Madiga Sacko"),
                            ("88", "Sansankide"),
                            ("89", "Nioro"),
                            ("90", "Diabigue"),
                            ("91", "Diarra"),
                            ("92", "Diaye Coura"),
                            ("93", "Gavinane"),
                            ("94", "Gogui"),
                            ("95", "Guetema"),
                            ("96", "Gadiaba Kadiel"),
                            ("97", "Korera Kore"),
                            ("98", "Nioro Tougoune Rangabe"),
                            ("99", "Sandare"),
                            ("100", "Simbi"),
                            ("101", "Troungoumbe"),
                            ("102", "Yerere"),
                            ("103", "Youri"),
                            ("104", "Koulikoro"),
                            ("105", "Dinandougou"),
                            ("106", "Koula"),
                            ("107", "Nyamina"),
                            ("108", "Sirakorola"),
                            ("109", "Tougouni"),
                            ("110", "Banamba"),
                            ("111", "Boron"),
                            ("112", "Duguwolowula"),
                            ("113", "Madina-Sacko"),
                            ("114", "Toubacoro"),
                            ("115", "Toukoroba"),
                            ("116", "Minidian"),
                            ("117", "Balan Bakama"),
                            ("118", "Benkadi"),
                            ("119", "Karan"),
                            ("120", "Maramandougou"),
                            ("121", "Narena"),
                            ("122", "Nouga"),
                            ("123", "Kati"),
                            ("124", "Baguineda-Camp"),
                            ("125", "Bossofala"),
                            ("126", "Diago"),
                            ("127", "Dialakoroba"),
                            ("128", "Dombila"),
                            ("129", "Kambila"),
                            ("130", "Mande"),
                            ("131", "Mountougoula"),
                            ("132", "N'Gouraba"),
                            ("133", "Sanankoroba"),
                            ("134", "Siby"),
                            ("135", "Sobra"),
                            ("136", "Tiele"),
                            ("137", "Yelekebougou"),
                            ("138", "Kolokani"),
                            ("139", "Didieni"),
                            ("140", "Guihoyo"),
                            ("141", "Massantola"),
                            ("142", "Nonkon"),
                            ("143", "Nossombougou"),
                            ("144", "Sagabala"),
                            ("145", "Sebekoro 1"),
                            ("146", "Tioribougou"),
                            ("147", "Kaladougou"),
                            ("148", "Banco"),
                            ("149", "Benkadi"),
                            ("150", "Binko"),
                            ("151", "Degnekoro"),
                            ("152", "Diebe"),
                            ("153", "Diedougou"),
                            ("154", "Diouman"),
                            ("155", "Dolendougou"),
                            ("156", "Guegneka"),
                            ("157", "Keme-Kafo"),
                            ("158", "Kerela"),
                            ("159", "Kilidougou"),
                            ("160", "Massigui"),
                            ("161", "N'Dlondougou"),
                            ("162", "N'Garadougou"),
                            ("163", "N'Golobougou"),
                            ("164", "Nangola"),
                            ("165", "Niantjila"),
                            ("166", "Tenindougou"),
                            ("167", "Wacoro"),
                            ("168", "Zan Coulibaly"),
                            ("169", "Nara"),
                            ("170", "Allahina"),
                            ("171", "Dabo"),
                            ("172", "Dilly"),
                            ("173", "Dogofry"),
                            ("174", "Digan"),
                            ("175", "Fallou"),
                            ("176", "Gueneibe"),
                            ("177", "Guire"),
                            ("178", "Koronga"),
                            ("179", "Niamana"),
                            ("180", "Madina-Kagoro"),
                            ("181", "Ouagadou"),
                            ("182", "Sikasso"),
                            ("183", "Benkadi"),
                            ("184", "Blendio"),
                            ("185", "Danderesso"),
                            ("186", "Dembela"),
                            ("187", "Dialakoro"),
                            ("188", "Dogoni"),
                            ("189", "Doumanaba"),
                            ("190", "Fama"),
                            ("191", "Finkolo"),
                            ("192", "Finkolo Ganadougou"),
                            ("193", "Gongasso"),
                            ("194", "Kaboila"),
                            ("195", "Dalle"),
                            ("196", "Kafouziela"),
                            ("197", "Kapala"),
                            ("198", "Kapolondougou"),
                            ("199", "Kignan"),
                            ("200", "Klela"),
                            ("201", "Kouoro"),
                            ("202", "Kourouma"),
                            ("203", "Lobougoula"),
                            ("204", "Natien"),
                            ("205", "Niena"),
                            ("206", "Nongo-Souala"),
                            ("207", "Pimperna"),
                            ("208", "Wateni"),
                            ("209", "Zangaradougou"),
                            ("210", "Kadiolo"),
                            ("211", "Dioumatene"),
                            ("212", "Fourou"),
                            ("213", "Kai"),
                            ("214", "Loulouni"),
                            ("215", "Misseni"),
                            ("216", "Nimbougou"),
                            ("217", "Zegoua"),
                            ("218", "Selefougou"),
                            ("219", "Faraba"),
                            ("220", "Kourouba"),
                            ("221", "Ouelessebougou"),
                            ("222", "Sanankoro-Djitoumou"),
                            ("223", "Tiakadougou-Dialakoro"),
                            ("224", "Bougouni"),
                            ("225", "Debelin"),
                            ("226", "Domba"),
                            ("227", "Faradiele"),
                            ("228", "Garalo"),
                            ("229", "Keleya"),
                            ("230", "Koumantou"),
                            ("231", "Meridiela"),
                            ("232", "Sanso"),
                            ("233", "Sibirila"),
                            ("234", "Syentoula"),
                            ("235", "Tiemala Banimonotie"),
                            ("236", "Wola"),
                            ("237", "Zantiebougou"),
                            ("238", "Kolondieba"),
                            ("239", "Bougoula"),
                            ("240", "Fakola"),
                            ("241", "Kadiana"),
                            ("242", "Kebila"),
                            ("243", "Kolosso"),
                            ("244", "Mena"),
                            ("245", "Nangalasso"),
                            ("246", "N'Golodiana"),
                            ("247", "Tiongui"),
                            ("248", "Wassoulou-Balle"),
                            ("249", "Baya"),
                            ("250", "Gouanan"),
                            ("251", "Gouandiaka"),
                            ("252", "Koussan"),
                            ("253", "Sere Moussa Ani Samou de"),
                            ("254", "Tagandougou"),
                            ("255", "Yallankoro Soloba"),
                            ("256", "Koutiala"),
                            ("257", "Diedougou"),
                            ("258", "Fagui"),
                            ("259", "Gouadji Kao"),
                            ("260", "Gouadie Sougouna"),
                            ("261", "Kapala"),
                            ("262", "Kolonigue"),
                            ("263", "Konina"),
                            ("264", "Koningue"),
                            ("265", "Konseguela"),
                            ("266", "Koromo"),
                            ("267", "Kouniana"),
                            ("268", "Logouana"),
                            ("269", "Miena"),
                            ("270", "M’Pessoba"),
                            ("271", "Nafanga"),
                            ("272", "Nampe"),
                            ("273", "N'Golonianasso"),
                            ("274", "N'Goutjina"),
                            ("275", "Niantaga"),
                            ("276", "N'Tossoni"),
                            ("277", "Sincina"),
                            ("278", "Songo-Doubacore"),
                            ("279", "Tao"),
                            ("280", "Zanfigue"),
                            ("281", "Zangasso"),
                            ("282", "Zanina"),
                            ("283", "Zebala"),
                            ("284", "Yorosso"),
                            ("285", "Boura"),
                            ("286", "Karangana"),
                            ("287", "Kiffosso 1"),
                            ("288", "Koury"),
                            ("289", "Mahou"),
                            ("290", "Menamba 1"),
                            ("291", "Ourikela"),
                            ("292", "Diaramana"),
                            ("293", "Segou"),
                            ("294", "Boussin"),
                            ("295", "Cinzana"),
                            ("296", "Diedougou"),
                            ("297", "Dioro"),
                            ("298", "Dougabougou"),
                            ("299", "Farakou Massa"),
                            ("300", "Fatine"),
                            ("301", "Katiena"),
                            ("302", "Konodimini"),
                            ("303", "Markala"),
                            ("304", "N'Gara"),
                            ("305", "Pelengana"),
                            ("306", "Sansanding"),
                            ("307", "Sebougou"),
                            ("308", "Sibila"),
                            ("309", "Souba"),
                            ("310", "Baroueli"),
                            ("311", "Boidie"),
                            ("312", "Kalake"),
                            ("313", "Konobougou"),
                            ("314", "Sanando"),
                            ("315", "Tamani"),
                            ("316", "Tesserela"),
                            ("317", "Bla"),
                            ("318", "Beguene"),
                            ("319", "Diena"),
                            ("320", "Falo"),
                            ("321", "Kemeni"),
                            ("322", "Somasso"),
                            ("323", "Touna"),
                            ("324", "Macina"),
                            ("325", "Boky Were"),
                            ("326", "Folomana"),
                            ("327", "Kokry Centre"),
                            ("328", "Monimpebougou"),
                            ("329", "Saloba"),
                            ("330", "Sana"),
                            ("331", "Souleye"),
                            ("332", "Niono"),
                            ("333", "Diabaly"),
                            ("334", "Kala Siguida"),
                            ("335", "Siribala"),
                            ("336", "Sirifila Boundy"),
                            ("337", "Sokolo"),
                            ("338", "Yeredon Saniona"),
                            ("339", "Kareri"),
                            ("340", "Diguicire"),
                            ("341", "Fani"),
                            ("342", "Kazangasso"),
                            ("343", "Korodougou"),
                            ("344", "Koulandougou"),
                            ("345", "Yangasso"),
                            ("346", "San"),
                            ("347", "Baramandougou"),
                            ("348", "Dah"),
                            ("349", "Diakourouna"),
                            ("350", "Dieli"),
                            ("351", "Kaniegue"),
                            ("352", "Kassorola"),
                            ("353", "Kava"),
                            ("354", "Moribila"),
                            ("355", "N'Goa"),
                            ("356", "Niamana"),
                            ("357", "Niasso"),
                            ("358", "Ouolon"),
                            ("359", "Siadougou"),
                            ("360", "Sourountouna"),
                            ("361", "Tene"),
                            ("362", "Tourakolomba"),
                            ("363", "Waki"),
                            ("364", "Tominian"),
                            ("365", "Benena"),
                            ("366", "Diora"),
                            ("367", "Koula"),
                            ("368", "Lanfiala"),
                            ("369", "Mafoune"),
                            ("370", "Mandiakuy"),
                            ("371", "Ouan"),
                            ("372", "Sanekuy"),
                            ("373", "Timissa"),
                            ("374", "Yasso"),
                            ("375", "Mopti"),
                            ("376", "Bassirou"),
                            ("377", "Fatoma"),
                            ("378", "Konna"),
                            ("379", "Kontza"),
                            ("380", "Korombana"),
                            ("381", "Gouloumbou"),
                            ("382", "Doko"),
                            ("383", "Sio"),
                            ("384", "Socoura"),
                            ("385", "Djenne"),
                            ("386", "Dandougou Fakala"),
                            ("387", "Fakala"),
                            ("388", "Femaye"),
                            ("389", "Madiama"),
                            ("390", "Nema Badenyakafo"),
                            ("391", "Pondori"),
                            ("392", "Tenenkou"),
                            ("393", "Diafarabe"),
                            ("394", "Diaka"),
                            ("395", "Diondiori"),
                            ("396", "Ouro Ardo"),
                            ("397", "Ouro Guire"),
                            ("398", "Sougoulbe"),
                            ("399", "Youwarou"),
                            ("400", "Bimbere Tama"),
                            ("401", "Deboye"),
                            ("402", "Dirma"),
                            ("403", "Dongo"),
                            ("404", "Farimake"),
                            ("405", "N'Dodjiga"),
                            ("406", "Bandiagara"),
                            ("407", "Diamnati"),
                            ("408", "Dourou"),
                            ("409", "Kende"),
                            ("410", "Kendie"),
                            ("411", "Metoumou"),
                            ("412", "Sangha"),
                            ("413", "Ireli"),
                            ("414", "Segue Ire"),
                            ("415", "Soroly"),
                            ("416", "Wadouba"),
                            ("417", "Ouroli"),
                            ("418", "Menthely"),
                            ("419", "Bankass"),
                            ("420", "Diallassagou"),
                            ("421", "Dimbal Habbe"),
                            ("422", "Kani-Bonzon"),
                            ("423", "Lessagou Habe"),
                            ("424", "Segue"),
                            ("425", "Sokoura"),
                            ("426", "Soubala"),
                            ("427", "Tori"),
                            ("428", "Koro"),
                            ("429", "Barapireli"),
                            ("430", "Bondo"),
                            ("431", "Dougoutene 1"),
                            ("432", "Dougoutene 2"),
                            ("433", "Koporo Pen"),
                            ("434", "Koporokendie Na"),
                            ("435", "Madougou"),
                            ("436", "Pel Maoude"),
                            ("437", "Youdiou"),
                            ("438", "Douentza"),
                            ("439", "Debere"),
                            ("440", "Dangol-Bore"),
                            ("441", "N'Doumpa"),
                            ("442", "Doumbara"),
                            ("443", "Dianwely"),
                            ("444", "Korarou"),
                            ("445", "Koubewel Koundia"),
                            ("446", "Petaka"),
                            ("447", "Tedie"),
                            ("448", "Tombouctou"),
                            ("449", "Alafia"),
                            ("450", "Ber"),
                            ("451", "Zarho"),
                            ("452", "Lafia"),
                            ("453", "Dire"),
                            ("454", "Arham"),
                            ("455", "Binga"),
                            ("456", "Dangha"),
                            ("457", "Garbakoira"),
                            ("458", "Haibongo"),
                            ("459", "Kondi"),
                            ("460", "Sareyamou"),
                            ("461", "Tienkour"),
                            ("462", "Tindirma"),
                            ("463", "Goundam"),
                            ("464", "Bintagoungou"),
                            ("465", "Douekire"),
                            ("466", "Essakane"),
                            ("467", "Gargando"),
                            ("468", "Issa Bery"),
                            ("469", "M'Bouna"),
                            ("470", "Raz-El-Ma"),
                            ("471", "Tele"),
                            ("472", "Tilemsi"),
                            ("473", "Tonka"),
                            ("474", "Tonka"),
                            ("475", "Rharous"),
                            ("476", "Bambara-Maoude"),
                            ("477", "Haribomo"),
                            ("478", "Serere"),
                            ("479", "Soboundou"),
                            ("480", "Banikane Narhawa"),
                            ("481", "Dianke"),
                            ("482", "Fittouga"),
                            ("483", "Koumaira"),
                            ("484", "Lere"),
                            ("485", "N'Gorkou"),
                            ("486", "Soumpi"),
                            ("487", "Gao"),
                            ("488", "Gabero"),
                            ("489", "Zinda"),
                            ("490", "Gounzoureye"),
                            ("491", "Tacharane"),
                            ("492", "Magnadaoue"),
                            ("493", "Soni Aliber"),
                            ("494", "Ansongo"),
                            ("495", "Aroun"),
                            ("496", "Tessit"),
                            ("497", "Tin-Hamma"),
                            ("498", "Bourem"),
                            ("499", "Bamba"),
                            ("500", "Taboye"),
                            ("501", "Temera"),
                            ("502", "Kidal"),
                            ("503", "Agharous"),
                            ("504", "Anefif"),
                            ("505", "Essouk"),
                            ("506", "Abeibara"),
                            ("507", "Boghassa"),
                            ("508", "Tinzawatene"),
                            ("509", "Tessalit"),
                            ("510", "Aguel-Hoc"),
                            ("511", "Timtaghene"),
                            ("512", "Tin-Essako"),
                            ("513", "Taoudenni"),
                            ("514", "Alougla"),
                            ("515", "Teghaza"),
                            ("516", "Zouelya"),
                            ("517", "Almatla"),
                            ("518", "Al-Ourche"),
                            ("519", "Diaba"),
                            ("520", "Nibkit-El Elk"),
                            ("521", "Oum-Laazam"),
                            ("522", "Tamagounite"),
                            ("523", "Touwal"),
                            ("524", "Araouane"),
                            ("525", "Achamour"),
                            ("526", "M'Back-Samna"),
                            ("527", "Tineguelhadj"),
                            ("528", "Bou-Djebeha"),
                            ("529", "Erg-Lakhal"),
                            ("530", "Limgassim"),
                            ("531", "Foum-Elba"),
                            ("532", "Bougwera"),
                            ("533", "Lamhaimide"),
                            ("534", "Menaka"),
                            ("535", "Assakaraye"),
                            ("536", "Inazole"),
                            ("537", "Infoukaretane"),
                            ("538", "Iziguirete"),
                            ("539", "Tabankort"),
                            ("540", "Tin Abaw"),
                            ("541", "Anderamboukane"),
                            ("542", "Azawak"),
                            ("543", "Inekar"),
                            ("544", "Inlamawane"),
                            ("545", "Inlamawane"),
                            ("546", "Tadriante"),
                            ("547", "Tissouakh"),
                            ("548", "Tidermene"),
                            ("549", "Chiman"),
                            ("550", "Inhinita"),
                            ("551", "Intadeyne"),
                            ("552", "Teguerert"),
                            ("553", "Commune 6"),
                            ("554", "Commune 1"),
                            ("555", "Commune 4"),
                            ("556", "Commune 7"),
                            ("557", "Commune 2"),
                            ("558", "Commune 3"),
                            ("559", "Commune 5"),
                        ],
                        max_length=100,
                    ),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
