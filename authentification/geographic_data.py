# geographic_data.py

REGIONS_CHOICES = [
  {
    "id_region": 1,
    "nom_region": "Kayes"
  },
  {
    "id_region": 2,
    "nom_region": "Kita"
  },
  {
    "id_region": 3,
    "nom_region": "Nioro"
  },
  {
    "id_region": 4,
    "nom_region": "Koulikoro"
  },
  {
    "id_region": 5,
    "nom_region": "Dioila"
  },
  {
    "id_region": 6,
    "nom_region": "Nara"
  },
  {
    "id_region": 7,
    "nom_region": "Sikasso"
  },
  {
    "id_region": 8,
    "nom_region": "Bougouni"
  },
  {
    "id_region": 9,
    "nom_region": "Koutiala"
  },
  {
    "id_region": 10,
    "nom_region": "Segou"
  },
  {
    "id_region": 11,
    "nom_region": "San"
  },
  {
    "id_region": 12,
    "nom_region": "Mopti"
  },
  {
    "id_region": 13,
    "nom_region": "Bandiagara"
  },
  {
    "id_region": 14,
    "nom_region": "Douentza"
  },
  {
    "id_region": 15,
    "nom_region": "Tombouctou"
  },
  {
    "id_region": 16,
    "nom_region": "Gao"
  },
  {
    "id_region": 17,
    "nom_region": "Kidal"
  }
]

CERCLES_CHOICES = [
  {
    "id_cercle": 101,
    "id_region": 1,
    "nom_cercle": "Kayes"
  },
  {
    "id_cercle": 102,
    "id_region": 1,
    "nom_cercle": "Diamou"
  },
  {
    "id_cercle": 103,
    "id_region": 1,
    "nom_cercle": "Aourou"
  },
  {
    "id_cercle": 104,
    "id_region": 1,
    "nom_cercle": "Ambidedi"
  },
  {
    "id_cercle": 105,
    "id_region": 1,
    "nom_cercle": "Segala"
  },
  {
    "id_cercle": 106,
    "id_region": 1,
    "nom_cercle": "Sadiola"
  },
  {
    "id_cercle": 107,
    "id_region": 1,
    "nom_cercle": "Bafoulabe"
  },
  {
    "id_cercle": 108,
    "id_region": 1,
    "nom_cercle": "Oussoubidiagna"
  },
  {
    "id_cercle": 109,
    "id_region": 1,
    "nom_cercle": "Kenieba"
  },
  {
    "id_cercle": 110,
    "id_region": 1,
    "nom_cercle": "Yelimane"
  },
  {
    "id_cercle": 201,
    "id_region": 2,
    "nom_cercle": "Kita"
  },
  {
    "id_cercle": 202,
    "id_region": 2,
    "nom_cercle": "Sagabari"
  },
  {
    "id_cercle": 203,
    "id_region": 2,
    "nom_cercle": "Sefeto"
  },
  {
    "id_cercle": 204,
    "id_region": 2,
    "nom_cercle": "Sebekoro"
  },
  {
    "id_cercle": 205,
    "id_region": 2,
    "nom_cercle": "Sirakoro"
  },
  {
    "id_cercle": 206,
    "id_region": 2,
    "nom_cercle": "Toukoto"
  },
  {
    "id_cercle": 301,
    "id_region": 3,
    "nom_cercle": "Diema"
  },
  {
    "id_cercle": 302,
    "id_region": 3,
    "nom_cercle": "Bema"
  },
  {
    "id_cercle": 303,
    "id_region": 3,
    "nom_cercle": "Diangounte Camara"
  },
  {
    "id_cercle": 304,
    "id_region": 3,
    "nom_cercle": "Sandare"
  },
  {
    "id_cercle": 305,
    "id_region": 3,
    "nom_cercle": "Nioro"
  },
  {
    "id_cercle": 306,
    "id_region": 3,
    "nom_cercle": "Troungoumbe"
  },
  {
    "id_cercle": 401,
    "id_region": 4,
    "nom_cercle": "Koulikoro"
  },
  {
    "id_cercle": 402,
    "id_region": 4,
    "nom_cercle": "Nyamina"
  },
  {
    "id_cercle": 403,
    "id_region": 4,
    "nom_cercle": "Banamba"
  },
  {
    "id_cercle": 404,
    "id_region": 4,
    "nom_cercle": "Kangaba"
  },
  {
    "id_cercle": 405,
    "id_region": 4,
    "nom_cercle": "Kati"
  },
  {
    "id_cercle": 406,
    "id_region": 4,
    "nom_cercle": "Neguela"
  },
  {
    "id_cercle": 407,
    "id_region": 4,
    "nom_cercle": "Siby"
  },
  {
    "id_cercle": 408,
    "id_region": 4,
    "nom_cercle": "Kolokani"
  },
  {
    "id_cercle": 501,
    "id_region": 5,
    "nom_cercle": "Dioila"
  },
  {
    "id_cercle": 502,
    "id_region": 5,
    "nom_cercle": "Banco"
  },
  {
    "id_cercle": 503,
    "id_region": 5,
    "nom_cercle": "Beleko"
  },
  {
    "id_cercle": 504,
    "id_region": 5,
    "nom_cercle": "Fana"
  },
  {
    "id_cercle": 505,
    "id_region": 5,
    "nom_cercle": "Mena"
  },
  {
    "id_cercle": 506,
    "id_region": 5,
    "nom_cercle": "Massigui"
  },
  {
    "id_cercle": 601,
    "id_region": 6,
    "nom_cercle": "Nara"
  },
  {
    "id_cercle": 602,
    "id_region": 6,
    "nom_cercle": "Balle"
  },
  {
    "id_cercle": 603,
    "id_region": 6,
    "nom_cercle": "Dilly"
  },
  {
    "id_cercle": 604,
    "id_region": 6,
    "nom_cercle": "Fallou"
  },
  {
    "id_cercle": 605,
    "id_region": 6,
    "nom_cercle": "Guire"
  },
  {
    "id_cercle": 606,
    "id_region": 6,
    "nom_cercle": "Mourdiah"
  },
  {
    "id_cercle": 701,
    "id_region": 7,
    "nom_cercle": "Sikasso"
  },
  {
    "id_cercle": 702,
    "id_region": 7,
    "nom_cercle": "Niena"
  },
  {
    "id_cercle": 703,
    "id_region": 7,
    "nom_cercle": "Danderesso"
  },
  {
    "id_cercle": 704,
    "id_region": 7,
    "nom_cercle": "Kignan"
  },
  {
    "id_cercle": 705,
    "id_region": 7,
    "nom_cercle": "Klela"
  },
  {
    "id_cercle": 706,
    "id_region": 7,
    "nom_cercle": "Lobougoula"
  },
  {
    "id_cercle": 707,
    "id_region": 7,
    "nom_cercle": "Kadiolo"
  },
  {
    "id_cercle": 708,
    "id_region": 7,
    "nom_cercle": "Loulouni"
  },
  {
    "id_cercle": 801,
    "id_region": 8,
    "nom_cercle": "Selingue"
  },
  {
    "id_cercle": 802,
    "id_region": 8,
    "nom_cercle": "Ouelessebougou"
  },
  {
    "id_cercle": 803,
    "id_region": 8,
    "nom_cercle": "Bougouni"
  },
  {
    "id_cercle": 804,
    "id_region": 8,
    "nom_cercle": "Koumantou"
  },
  {
    "id_cercle": 805,
    "id_region": 8,
    "nom_cercle": "Garalo"
  },
  {
    "id_cercle": 806,
    "id_region": 8,
    "nom_cercle": "Dogo"
  },
  {
    "id_cercle": 807,
    "id_region": 8,
    "nom_cercle": "Kolondieba"
  },
  {
    "id_cercle": 808,
    "id_region": 8,
    "nom_cercle": "Fakola"
  },
  {
    "id_cercle": 809,
    "id_region": 8,
    "nom_cercle": "Kadiana"
  },
  {
    "id_cercle": 810,
    "id_region": 8,
    "nom_cercle": "Yanfolila"
  },
  {
    "id_cercle": 901,
    "id_region": 9,
    "nom_cercle": "Koutiala"
  },
  {
    "id_cercle": 902,
    "id_region": 9,
    "nom_cercle": "Konseguela"
  },
  {
    "id_cercle": 903,
    "id_region": 9,
    "nom_cercle": "Zangasso"
  },
  {
    "id_cercle": 904,
    "id_region": 9,
    "nom_cercle": "Kouniana"
  },
  {
    "id_cercle": 905,
    "id_region": 9,
    "nom_cercle": "Molobala"
  },
  {
    "id_cercle": 906,
    "id_region": 9,
    "nom_cercle": "M�Pessoba"
  },
  {
    "id_cercle": 907,
    "id_region": 9,
    "nom_cercle": "Yorosso"
  },
  {
    "id_cercle": 908,
    "id_region": 9,
    "nom_cercle": "Koury"
  },
  {
    "id_cercle": 1001,
    "id_region": 10,
    "nom_cercle": "Segou"
  },
  {
    "id_cercle": 1002,
    "id_region": 10,
    "nom_cercle": "Markala"
  },
  {
    "id_cercle": 1003,
    "id_region": 10,
    "nom_cercle": "Dioro"
  },
  {
    "id_cercle": 1004,
    "id_region": 10,
    "nom_cercle": "Farako"
  },
  {
    "id_cercle": 1005,
    "id_region": 10,
    "nom_cercle": "Baroueli"
  },
  {
    "id_cercle": 1006,
    "id_region": 10,
    "nom_cercle": "Bla"
  },
  {
    "id_cercle": 1007,
    "id_region": 10,
    "nom_cercle": "Macina"
  },
  {
    "id_cercle": 1008,
    "id_region": 10,
    "nom_cercle": "Niono"
  },
  {
    "id_cercle": 1009,
    "id_region": 10,
    "nom_cercle": "Sokolo"
  },
  {
    "id_cercle": 1010,
    "id_region": 10,
    "nom_cercle": "Nampala"
  },
  {
    "id_cercle": 1101,
    "id_region": 11,
    "nom_cercle": "Yangasso"
  },
  {
    "id_cercle": 1102,
    "id_region": 11,
    "nom_cercle": "San"
  },
  {
    "id_cercle": 1103,
    "id_region": 11,
    "nom_cercle": "Kimparana"
  },
  {
    "id_cercle": 1104,
    "id_region": 11,
    "nom_cercle": "Sy"
  },
  {
    "id_cercle": 1105,
    "id_region": 11,
    "nom_cercle": "Tominian"
  },
  {
    "id_cercle": 1106,
    "id_region": 11,
    "nom_cercle": "Mandiakuy"
  },
  {
    "id_cercle": 1107,
    "id_region": 11,
    "nom_cercle": "Fangasso"
  },
  {
    "id_cercle": 1201,
    "id_region": 12,
    "nom_cercle": "Mopti"
  },
  {
    "id_cercle": 1202,
    "id_region": 12,
    "nom_cercle": "Konna"
  },
  {
    "id_cercle": 1203,
    "id_region": 12,
    "nom_cercle": "Korientze"
  },
  {
    "id_cercle": 1204,
    "id_region": 12,
    "nom_cercle": "Djenne"
  },
  {
    "id_cercle": 1205,
    "id_region": 12,
    "nom_cercle": "Sofara"
  },
  {
    "id_cercle": 1206,
    "id_region": 12,
    "nom_cercle": "Tenenkou"
  },
  {
    "id_cercle": 1207,
    "id_region": 12,
    "nom_cercle": "Youwarou"
  },
  {
    "id_cercle": 1301,
    "id_region": 13,
    "nom_cercle": "Bandiagara"
  },
  {
    "id_cercle": 1302,
    "id_region": 13,
    "nom_cercle": "Ningari"
  },
  {
    "id_cercle": 1303,
    "id_region": 13,
    "nom_cercle": "Kendie"
  },
  {
    "id_cercle": 1304,
    "id_region": 13,
    "nom_cercle": "Sangha"
  },
  {
    "id_cercle": 1305,
    "id_region": 13,
    "nom_cercle": "Kani"
  },
  {
    "id_cercle": 1306,
    "id_region": 13,
    "nom_cercle": "Bankass"
  },
  {
    "id_cercle": 1307,
    "id_region": 13,
    "nom_cercle": "Diallassagou"
  },
  {
    "id_cercle": 1308,
    "id_region": 13,
    "nom_cercle": "Sokoura"
  },
  {
    "id_cercle": 1309,
    "id_region": 13,
    "nom_cercle": "Koro"
  },
  {
    "id_cercle": 1401,
    "id_region": 14,
    "nom_cercle": "Douentza"
  },
  {
    "id_cercle": 1402,
    "id_region": 14,
    "nom_cercle": "Bore"
  },
  {
    "id_cercle": 1403,
    "id_region": 15,
    "nom_cercle": "Tombouctou"
  },
  {
    "id_cercle": 1501,
    "id_region": 15,
    "nom_cercle": "Ber"
  },
  {
    "id_cercle": 1502,
    "id_region": 15,
    "nom_cercle": "Dire"
  },
  {
    "id_cercle": 1503,
    "id_region": 15,
    "nom_cercle": "Goundam"
  },
  {
    "id_cercle": 1504,
    "id_region": 15,
    "nom_cercle": "Bintagoungou"
  },
  {
    "id_cercle": 1505,
    "id_region": 15,
    "nom_cercle": "Gargando"
  },
  {
    "id_cercle": 1506,
    "id_region": 15,
    "nom_cercle": "Tonka"
  },
  {
    "id_cercle": 1507,
    "id_region": 15,
    "nom_cercle": "Gourma-Rharous"
  },
  {
    "id_cercle": 1508,
    "id_region": 15,
    "nom_cercle": "Bambara-Maoude"
  },
  {
    "id_cercle": 1509,
    "id_region": 15,
    "nom_cercle": "Niafunke"
  },
  {
    "id_cercle": 1510,
    "id_region": 15,
    "nom_cercle": "Sarafere"
  },
  {
    "id_cercle": 1511,
    "id_region": 15,
    "nom_cercle": "Lere"
  },
  {
    "id_cercle": 1601,
    "id_region": 16,
    "nom_cercle": "Gao"
  },
  {
    "id_cercle": 1602,
    "id_region": 16,
    "nom_cercle": "Gabero"
  },
  {
    "id_cercle": 1603,
    "id_region": 16,
    "nom_cercle": "Djebock"
  },
  {
    "id_cercle": 1604,
    "id_region": 16,
    "nom_cercle": "Soni Aliber"
  },
  {
    "id_cercle": 1605,
    "id_region": 16,
    "nom_cercle": "Ansongo"
  },
  {
    "id_cercle": 1606,
    "id_region": 16,
    "nom_cercle": "Tessit"
  },
  {
    "id_cercle": 1607,
    "id_region": 16,
    "nom_cercle": "Bourem"
  },
  {
    "id_cercle": 1608,
    "id_region": 16,
    "nom_cercle": "Bamba"
  },
  {
    "id_cercle": 1701,
    "id_region": 17,
    "nom_cercle": "Kidal"
  },
  {
    "id_cercle": 1702,
    "id_region": 17,
    "nom_cercle": "Anefif"
  },
  {
    "id_cercle": 1703,
    "id_region": 17,
    "nom_cercle": "Abeibara"
  },
  {
    "id_cercle": 1704,
    "id_region": 17,
    "nom_cercle": "Tessalit"
  },
  {
    "id_cercle": 1705,
    "id_region": 17,
    "nom_cercle": "Aguel-Hoc"
  },
  {
    "id_cercle": 1706,
    "id_region": 17,
    "nom_cercle": "Tin-Essako"
  },
  {
    "id_cercle": 1801,
    "id_region": 18,
    "nom_cercle": "Taoudenni"
  },
  {
    "id_cercle": 1802,
    "id_region": 18,
    "nom_cercle": "Achouratt"
  },
  {
    "id_cercle": 1803,
    "id_region": 18,
    "nom_cercle": "Al-Ourche"
  },
  {
    "id_cercle": 1804,
    "id_region": 18,
    "nom_cercle": "Araouane"
  },
  {
    "id_cercle": 1805,
    "id_region": 18,
    "nom_cercle": "Bou-Djebeha"
  },
  {
    "id_cercle": 1806,
    "id_region": 18,
    "nom_cercle": "Foum-Elba"
  },
  {
    "id_cercle": 1901,
    "id_region": 19,
    "nom_cercle": "Menaka"
  },
  {
    "id_cercle": 1902,
    "id_region": 19,
    "nom_cercle": "Anderamboukane"
  },
  {
    "id_cercle": 1903,
    "id_region": 19,
    "nom_cercle": "Inekar"
  },
  {
    "id_cercle": 1904,
    "id_region": 19,
    "nom_cercle": "Inlamawane"
  },
  {
    "id_cercle": 1905,
    "id_region": 19,
    "nom_cercle": "Tidermene"
  },
  {
    "id_cercle": 9001,
    "id_region": 90,
    "nom_cercle": "Bamako"
  }
]

COMMUNES_CHOICES = [
  {
    "id_commune": 2,
    "id_cercle": 101,
    "nom_commune": "Kayes"
  },
  {
    "id_commune": 3,
    "id_cercle": 101,
    "nom_commune": "Bangassi"
  },
  {
    "id_commune": 4,
    "id_cercle": 101,
    "nom_commune": "Colimbine"
  },
  {
    "id_commune": 5,
    "id_cercle": 102,
    "nom_commune": "Diamou"
  },
  {
    "id_commune": 6,
    "id_cercle": 103,
    "nom_commune": "Djelebou"
  },
  {
    "id_commune": 7,
    "id_cercle": 104,
    "nom_commune": "Fegui"
  },
  {
    "id_commune": 8,
    "id_cercle": 101,
    "nom_commune": "Gory Gopela"
  },
  {
    "id_commune": 9,
    "id_cercle": 101,
    "nom_commune": "Goumera"
  },
  {
    "id_commune": 10,
    "id_cercle": 103,
    "nom_commune": "Karakoro"
  },
  {
    "id_commune": 11,
    "id_cercle": 104,
    "nom_commune": "Kemene Tambo"
  },
  {
    "id_commune": 12,
    "id_cercle": 101,
    "nom_commune": "Khouloum"
  },
  {
    "id_commune": 13,
    "id_cercle": 105,
    "nom_commune": "Kouniakary"
  },
  {
    "id_commune": 14,
    "id_cercle": 103,
    "nom_commune": "Koussane"
  },
  {
    "id_commune": 15,
    "id_cercle": 101,
    "nom_commune": "Liberte Dembaya"
  },
  {
    "id_commune": 16,
    "id_cercle": 105,
    "nom_commune": "Marena Diombougou"
  },
  {
    "id_commune": 17,
    "id_cercle": 105,
    "nom_commune": "Marintoumania"
  },
  {
    "id_commune": 18,
    "id_cercle": 106,
    "nom_commune": "Sadiola"
  },
  {
    "id_commune": 19,
    "id_cercle": 101,
    "nom_commune": "Same Diongoma"
  },
  {
    "id_commune": 20,
    "id_cercle": 105,
    "nom_commune": "Segala"
  },
  {
    "id_commune": 21,
    "id_cercle": 101,
    "nom_commune": "Sero Diamanou"
  },
  {
    "id_commune": 22,
    "id_cercle": 101,
    "nom_commune": "Somankidy"
  },
  {
    "id_commune": 23,
    "id_cercle": 104,
    "nom_commune": "Sony"
  },
  {
    "id_commune": 24,
    "id_cercle": 107,
    "nom_commune": "Bafoulabe"
  },
  {
    "id_commune": 25,
    "id_cercle": 107,
    "nom_commune": "Bamafele"
  },
  {
    "id_commune": 26,
    "id_cercle": 108,
    "nom_commune": "Diakon"
  },
  {
    "id_commune": 27,
    "id_cercle": 108,
    "nom_commune": "Diallan"
  },
  {
    "id_commune": 28,
    "id_cercle": 107,
    "nom_commune": "Gounfan"
  },
  {
    "id_commune": 29,
    "id_cercle": 108,
    "nom_commune": "Kontela"
  },
  {
    "id_commune": 30,
    "id_cercle": 107,
    "nom_commune": "Koundian"
  },
  {
    "id_commune": 31,
    "id_cercle": 107,
    "nom_commune": "Mahina"
  },
  {
    "id_commune": 32,
    "id_cercle": 108,
    "nom_commune": "Sidibela"
  },
  {
    "id_commune": 33,
    "id_cercle": 108,
    "nom_commune": "Tomora"
  },
  {
    "id_commune": 34,
    "id_cercle": 109,
    "nom_commune": "Kenieba"
  },
  {
    "id_commune": 35,
    "id_cercle": 109,
    "nom_commune": "Baye"
  },
  {
    "id_commune": 36,
    "id_cercle": 109,
    "nom_commune": "Dabia"
  },
  {
    "id_commune": 37,
    "id_cercle": 106,
    "nom_commune": "Dialafara"
  },
  {
    "id_commune": 38,
    "id_cercle": 109,
    "nom_commune": "Dombia"
  },
  {
    "id_commune": 39,
    "id_cercle": 109,
    "nom_commune": "Falea"
  },
  {
    "id_commune": 40,
    "id_cercle": 109,
    "nom_commune": "Guenegore"
  },
  {
    "id_commune": 41,
    "id_cercle": 109,
    "nom_commune": "Kassama"
  },
  {
    "id_commune": 42,
    "id_cercle": 109,
    "nom_commune": "Sagalo"
  },
  {
    "id_commune": 43,
    "id_cercle": 109,
    "nom_commune": "Sitakilly"
  },
  {
    "id_commune": 44,
    "id_cercle": 110,
    "nom_commune": "Guidime"
  },
  {
    "id_commune": 45,
    "id_cercle": 110,
    "nom_commune": "Fanga"
  },
  {
    "id_commune": 46,
    "id_cercle": 110,
    "nom_commune": "Kirane Kaniaga"
  },
  {
    "id_commune": 47,
    "id_cercle": 110,
    "nom_commune": "Soumpou"
  },
  {
    "id_commune": 48,
    "id_cercle": 110,
    "nom_commune": "Toya"
  },
  {
    "id_commune": 49,
    "id_cercle": 201,
    "nom_commune": "Kita"
  },
  {
    "id_commune": 50,
    "id_cercle": 201,
    "nom_commune": "Badia"
  },
  {
    "id_commune": 51,
    "id_cercle": 201,
    "nom_commune": "Bendougouba"
  },
  {
    "id_commune": 52,
    "id_cercle": 201,
    "nom_commune": "Benkady Founia"
  },
  {
    "id_commune": 53,
    "id_cercle": 202,
    "nom_commune": "Bougaribaya"
  },
  {
    "id_commune": 54,
    "id_cercle": 203,
    "nom_commune": "Didenko"
  },
  {
    "id_commune": 55,
    "id_cercle": 201,
    "nom_commune": "Djidian"
  },
  {
    "id_commune": 56,
    "id_cercle": 203,
    "nom_commune": "Djougoun"
  },
  {
    "id_commune": 57,
    "id_cercle": 202,
    "nom_commune": "Gadougou 1"
  },
  {
    "id_commune": 58,
    "id_cercle": 203,
    "nom_commune": "Guemoukouraba"
  },
  {
    "id_commune": 59,
    "id_cercle": 204,
    "nom_commune": "Kassaro"
  },
  {
    "id_commune": 60,
    "id_cercle": 201,
    "nom_commune": "Kita Nord"
  },
  {
    "id_commune": 61,
    "id_cercle": 201,
    "nom_commune": "Kita Ouest"
  },
  {
    "id_commune": 62,
    "id_cercle": 202,
    "nom_commune": "Kokofata"
  },
  {
    "id_commune": 63,
    "id_cercle": 204,
    "nom_commune": "Kotouba"
  },
  {
    "id_commune": 64,
    "id_cercle": 202,
    "nom_commune": "Koulou"
  },
  {
    "id_commune": 65,
    "id_cercle": 203,
    "nom_commune": "Kourouninkoto"
  },
  {
    "id_commune": 66,
    "id_cercle": 204,
    "nom_commune": "Madina"
  },
  {
    "id_commune": 67,
    "id_cercle": 205,
    "nom_commune": "Makono"
  },
  {
    "id_commune": 68,
    "id_cercle": 201,
    "nom_commune": "Namala Guimbala"
  },
  {
    "id_commune": 69,
    "id_cercle": 206,
    "nom_commune": "Niantanso"
  },
  {
    "id_commune": 70,
    "id_cercle": 204,
    "nom_commune": "Sebekoro"
  },
  {
    "id_commune": 71,
    "id_cercle": 203,
    "nom_commune": "Sefeto Nord"
  },
  {
    "id_commune": 72,
    "id_cercle": 203,
    "nom_commune": "Sefeto Ouest"
  },
  {
    "id_commune": 73,
    "id_cercle": 202,
    "nom_commune": "Tambaga"
  },
  {
    "id_commune": 74,
    "id_cercle": 206,
    "nom_commune": "Toukoto"
  },
  {
    "id_commune": 75,
    "id_cercle": 301,
    "nom_commune": "Diema"
  },
  {
    "id_commune": 76,
    "id_cercle": 302,
    "nom_commune": "Bema"
  },
  {
    "id_commune": 77,
    "id_cercle": 303,
    "nom_commune": "Diangounte Camara"
  },
  {
    "id_commune": 78,
    "id_cercle": 301,
    "nom_commune": "Dianguirde"
  },
  {
    "id_commune": 79,
    "id_cercle": 303,
    "nom_commune": "Dieoura"
  },
  {
    "id_commune": 80,
    "id_cercle": 302,
    "nom_commune": "Fassoudebe"
  },
  {
    "id_commune": 81,
    "id_cercle": 303,
    "nom_commune": "Fatao"
  },
  {
    "id_commune": 82,
    "id_cercle": 301,
    "nom_commune": "Gomitradougou"
  },
  {
    "id_commune": 83,
    "id_cercle": 302,
    "nom_commune": "Groumera"
  },
  {
    "id_commune": 84,
    "id_cercle": 302,
    "nom_commune": "Guedebine"
  },
  {
    "id_commune": 85,
    "id_cercle": 304,
    "nom_commune": "Lakamane"
  },
  {
    "id_commune": 86,
    "id_cercle": 303,
    "nom_commune": "Lambidou"
  },
  {
    "id_commune": 87,
    "id_cercle": 301,
    "nom_commune": "Madiga Sacko"
  },
  {
    "id_commune": 88,
    "id_cercle": 304,
    "nom_commune": "Sansankide"
  },
  {
    "id_commune": 89,
    "id_cercle": 305,
    "nom_commune": "Nioro"
  },
  {
    "id_commune": 90,
    "id_cercle": 306,
    "nom_commune": "Diabigue"
  },
  {
    "id_commune": 91,
    "id_cercle": 306,
    "nom_commune": "Diarra"
  },
  {
    "id_commune": 92,
    "id_cercle": 305,
    "nom_commune": "Diaye Coura"
  },
  {
    "id_commune": 93,
    "id_cercle": 305,
    "nom_commune": "Gavinane"
  },
  {
    "id_commune": 94,
    "id_cercle": 305,
    "nom_commune": "Gogui"
  },
  {
    "id_commune": 95,
    "id_cercle": 305,
    "nom_commune": "Guetema"
  },
  {
    "id_commune": 96,
    "id_cercle": 305,
    "nom_commune": "Gadiaba Kadiel"
  },
  {
    "id_commune": 97,
    "id_cercle": 306,
    "nom_commune": "Korera Kore"
  },
  {
    "id_commune": 98,
    "id_cercle": 305,
    "nom_commune": "Nioro Tougoune Rangabe"
  },
  {
    "id_commune": 99,
    "id_cercle": 304,
    "nom_commune": "Sandare"
  },
  {
    "id_commune": 100,
    "id_cercle": 305,
    "nom_commune": "Simbi"
  },
  {
    "id_commune": 101,
    "id_cercle": 306,
    "nom_commune": "Troungoumbe"
  },
  {
    "id_commune": 102,
    "id_cercle": 305,
    "nom_commune": "Yerere"
  },
  {
    "id_commune": 103,
    "id_cercle": 305,
    "nom_commune": "Youri"
  },
  {
    "id_commune": 104,
    "id_cercle": 401,
    "nom_commune": "Koulikoro"
  },
  {
    "id_commune": 105,
    "id_cercle": 401,
    "nom_commune": "Dinandougou"
  },
  {
    "id_commune": 106,
    "id_cercle": 401,
    "nom_commune": "Koula"
  },
  {
    "id_commune": 107,
    "id_cercle": 402,
    "nom_commune": "Nyamina"
  },
  {
    "id_commune": 108,
    "id_cercle": 401,
    "nom_commune": "Sirakorola"
  },
  {
    "id_commune": 109,
    "id_cercle": 402,
    "nom_commune": "Tougouni"
  },
  {
    "id_commune": 110,
    "id_cercle": 403,
    "nom_commune": "Banamba"
  },
  {
    "id_commune": 111,
    "id_cercle": 403,
    "nom_commune": "Boron"
  },
  {
    "id_commune": 112,
    "id_cercle": 403,
    "nom_commune": "Duguwolowula"
  },
  {
    "id_commune": 113,
    "id_cercle": 403,
    "nom_commune": "Madina-Sacko"
  },
  {
    "id_commune": 114,
    "id_cercle": 403,
    "nom_commune": "Toubacoro"
  },
  {
    "id_commune": 115,
    "id_cercle": 403,
    "nom_commune": "Toukoroba"
  },
  {
    "id_commune": 116,
    "id_cercle": 404,
    "nom_commune": "Minidian"
  },
  {
    "id_commune": 117,
    "id_cercle": 404,
    "nom_commune": "Balan Bakama"
  },
  {
    "id_commune": 118,
    "id_cercle": 404,
    "nom_commune": "Benkadi"
  },
  {
    "id_commune": 119,
    "id_cercle": 404,
    "nom_commune": "Karan"
  },
  {
    "id_commune": 120,
    "id_cercle": 404,
    "nom_commune": "Maramandougou"
  },
  {
    "id_commune": 121,
    "id_cercle": 404,
    "nom_commune": "Narena"
  },
  {
    "id_commune": 122,
    "id_cercle": 404,
    "nom_commune": "Nouga"
  },
  {
    "id_commune": 123,
    "id_cercle": 405,
    "nom_commune": "Kati"
  },
  {
    "id_commune": 124,
    "id_cercle": 405,
    "nom_commune": "Baguineda-Camp"
  },
  {
    "id_commune": 125,
    "id_cercle": 406,
    "nom_commune": "Bossofala"
  },
  {
    "id_commune": 126,
    "id_cercle": 405,
    "nom_commune": "Diago"
  },
  {
    "id_commune": 127,
    "id_cercle": 405,
    "nom_commune": "Dialakoroba"
  },
  {
    "id_commune": 128,
    "id_cercle": 405,
    "nom_commune": "Dombila"
  },
  {
    "id_commune": 129,
    "id_cercle": 405,
    "nom_commune": "Kambila"
  },
  {
    "id_commune": 130,
    "id_cercle": 405,
    "nom_commune": "Mande"
  },
  {
    "id_commune": 131,
    "id_cercle": 405,
    "nom_commune": "Mountougoula"
  },
  {
    "id_commune": 132,
    "id_cercle": 405,
    "nom_commune": "N'Gouraba"
  },
  {
    "id_commune": 133,
    "id_cercle": 405,
    "nom_commune": "Sanankoroba"
  },
  {
    "id_commune": 134,
    "id_cercle": 407,
    "nom_commune": "Siby"
  },
  {
    "id_commune": 135,
    "id_cercle": 407,
    "nom_commune": "Sobra"
  },
  {
    "id_commune": 136,
    "id_cercle": 405,
    "nom_commune": "Tiele"
  },
  {
    "id_commune": 137,
    "id_cercle": 405,
    "nom_commune": "Yelekebougou"
  },
  {
    "id_commune": 138,
    "id_cercle": 408,
    "nom_commune": "Kolokani"
  },
  {
    "id_commune": 139,
    "id_cercle": 408,
    "nom_commune": "Didieni"
  },
  {
    "id_commune": 140,
    "id_cercle": 408,
    "nom_commune": "Guihoyo"
  },
  {
    "id_commune": 141,
    "id_cercle": 408,
    "nom_commune": "Massantola"
  },
  {
    "id_commune": 142,
    "id_cercle": 408,
    "nom_commune": "Nonkon"
  },
  {
    "id_commune": 143,
    "id_cercle": 408,
    "nom_commune": "Nossombougou"
  },
  {
    "id_commune": 144,
    "id_cercle": 408,
    "nom_commune": "Sagabala"
  },
  {
    "id_commune": 145,
    "id_cercle": 408,
    "nom_commune": "Sebekoro 1"
  },
  {
    "id_commune": 146,
    "id_cercle": 408,
    "nom_commune": "Tioribougou"
  },
  {
    "id_commune": 147,
    "id_cercle": 501,
    "nom_commune": "Kaladougou"
  },
  {
    "id_commune": 148,
    "id_cercle": 502,
    "nom_commune": "Banco"
  },
  {
    "id_commune": 149,
    "id_cercle": 503,
    "nom_commune": "Benkadi"
  },
  {
    "id_commune": 150,
    "id_cercle": 504,
    "nom_commune": "Binko"
  },
  {
    "id_commune": 151,
    "id_cercle": 501,
    "nom_commune": "Degnekoro"
  },
  {
    "id_commune": 152,
    "id_cercle": 505,
    "nom_commune": "Diebe"
  },
  {
    "id_commune": 153,
    "id_cercle": 503,
    "nom_commune": "Diedougou"
  },
  {
    "id_commune": 154,
    "id_cercle": 504,
    "nom_commune": "Diouman"
  },
  {
    "id_commune": 155,
    "id_cercle": 503,
    "nom_commune": "Dolendougou"
  },
  {
    "id_commune": 156,
    "id_cercle": 504,
    "nom_commune": "Guegneka"
  },
  {
    "id_commune": 157,
    "id_cercle": 501,
    "nom_commune": "Keme-Kafo"
  },
  {
    "id_commune": 158,
    "id_cercle": 504,
    "nom_commune": "Kerela"
  },
  {
    "id_commune": 159,
    "id_cercle": 501,
    "nom_commune": "Kilidougou"
  },
  {
    "id_commune": 160,
    "id_cercle": 506,
    "nom_commune": "Massigui"
  },
  {
    "id_commune": 161,
    "id_cercle": 505,
    "nom_commune": "N'Dlondougou"
  },
  {
    "id_commune": 162,
    "id_cercle": 501,
    "nom_commune": "N'Garadougou"
  },
  {
    "id_commune": 163,
    "id_cercle": 502,
    "nom_commune": "N'Golobougou"
  },
  {
    "id_commune": 164,
    "id_cercle": 504,
    "nom_commune": "Nangola"
  },
  {
    "id_commune": 165,
    "id_cercle": 506,
    "nom_commune": "Niantjila"
  },
  {
    "id_commune": 166,
    "id_cercle": 504,
    "nom_commune": "Tenindougou"
  },
  {
    "id_commune": 167,
    "id_cercle": 501,
    "nom_commune": "Wacoro"
  },
  {
    "id_commune": 168,
    "id_cercle": 504,
    "nom_commune": "Zan Coulibaly"
  },
  {
    "id_commune": 169,
    "id_cercle": 601,
    "nom_commune": "Nara"
  },
  {
    "id_commune": 170,
    "id_cercle": 602,
    "nom_commune": "Allahina"
  },
  {
    "id_commune": 171,
    "id_cercle": 602,
    "nom_commune": "Dabo"
  },
  {
    "id_commune": 172,
    "id_cercle": 603,
    "nom_commune": "Dilly"
  },
  {
    "id_commune": 173,
    "id_cercle": 602,
    "nom_commune": "Dogofry"
  },
  {
    "id_commune": 174,
    "id_cercle": 604,
    "nom_commune": "Digan"
  },
  {
    "id_commune": 175,
    "id_cercle": 604,
    "nom_commune": "Fallou"
  },
  {
    "id_commune": 176,
    "id_cercle": 601,
    "nom_commune": "Gueneibe"
  },
  {
    "id_commune": 177,
    "id_cercle": 605,
    "nom_commune": "Guire"
  },
  {
    "id_commune": 178,
    "id_cercle": 603,
    "nom_commune": "Koronga"
  },
  {
    "id_commune": 179,
    "id_cercle": 606,
    "nom_commune": "Niamana"
  },
  {
    "id_commune": 180,
    "id_cercle": 606,
    "nom_commune": "Madina-Kagoro"
  },
  {
    "id_commune": 181,
    "id_cercle": 601,
    "nom_commune": "Ouagadou"
  },
  {
    "id_commune": 182,
    "id_cercle": 701,
    "nom_commune": "Sikasso"
  },
  {
    "id_commune": 183,
    "id_cercle": 702,
    "nom_commune": "Benkadi"
  },
  {
    "id_commune": 184,
    "id_cercle": 702,
    "nom_commune": "Blendio"
  },
  {
    "id_commune": 185,
    "id_cercle": 703,
    "nom_commune": "Danderesso"
  },
  {
    "id_commune": 186,
    "id_cercle": 702,
    "nom_commune": "Dembela"
  },
  {
    "id_commune": 187,
    "id_cercle": 704,
    "nom_commune": "Dialakoro"
  },
  {
    "id_commune": 188,
    "id_cercle": 704,
    "nom_commune": "Dogoni"
  },
  {
    "id_commune": 189,
    "id_cercle": 704,
    "nom_commune": "Doumanaba"
  },
  {
    "id_commune": 190,
    "id_cercle": 705,
    "nom_commune": "Fama"
  },
  {
    "id_commune": 191,
    "id_cercle": 701,
    "nom_commune": "Finkolo"
  },
  {
    "id_commune": 192,
    "id_cercle": 702,
    "nom_commune": "Finkolo Ganadougou"
  },
  {
    "id_commune": 193,
    "id_cercle": 705,
    "nom_commune": "Gongasso"
  },
  {
    "id_commune": 194,
    "id_cercle": 701,
    "nom_commune": "Kaboila"
  },
  {
    "id_commune": 195,
    "id_cercle": 701,
    "nom_commune": "Dalle"
  },
  {
    "id_commune": 196,
    "id_cercle": 701,
    "nom_commune": "Kafouziela"
  },
  {
    "id_commune": 197,
    "id_cercle": 701,
    "nom_commune": "Kapala"
  },
  {
    "id_commune": 198,
    "id_cercle": 701,
    "nom_commune": "Kapolondougou"
  },
  {
    "id_commune": 199,
    "id_cercle": 704,
    "nom_commune": "Kignan"
  },
  {
    "id_commune": 200,
    "id_cercle": 705,
    "nom_commune": "Klela"
  },
  {
    "id_commune": 201,
    "id_cercle": 705,
    "nom_commune": "Kouoro"
  },
  {
    "id_commune": 202,
    "id_cercle": 704,
    "nom_commune": "Kourouma"
  },
  {
    "id_commune": 203,
    "id_cercle": 706,
    "nom_commune": "Lobougoula"
  },
  {
    "id_commune": 204,
    "id_cercle": 701,
    "nom_commune": "Natien"
  },
  {
    "id_commune": 205,
    "id_cercle": 702,
    "nom_commune": "Niena"
  },
  {
    "id_commune": 206,
    "id_cercle": 703,
    "nom_commune": "Nongo-Souala"
  },
  {
    "id_commune": 207,
    "id_cercle": 701,
    "nom_commune": "Pimperna"
  },
  {
    "id_commune": 208,
    "id_cercle": 702,
    "nom_commune": "Wateni"
  },
  {
    "id_commune": 209,
    "id_cercle": 701,
    "nom_commune": "Zangaradougou"
  },
  {
    "id_commune": 210,
    "id_cercle": 707,
    "nom_commune": "Kadiolo"
  },
  {
    "id_commune": 211,
    "id_cercle": 707,
    "nom_commune": "Dioumatene"
  },
  {
    "id_commune": 212,
    "id_cercle": 707,
    "nom_commune": "Fourou"
  },
  {
    "id_commune": 213,
    "id_cercle": 708,
    "nom_commune": "Kai"
  },
  {
    "id_commune": 214,
    "id_cercle": 708,
    "nom_commune": "Loulouni"
  },
  {
    "id_commune": 215,
    "id_cercle": 707,
    "nom_commune": "Misseni"
  },
  {
    "id_commune": 216,
    "id_cercle": 708,
    "nom_commune": "Nimbougou"
  },
  {
    "id_commune": 217,
    "id_cercle": 707,
    "nom_commune": "Zegoua"
  },
  {
    "id_commune": 218,
    "id_cercle": 801,
    "nom_commune": "Selefougou"
  },
  {
    "id_commune": 219,
    "id_cercle": 802,
    "nom_commune": "Faraba"
  },
  {
    "id_commune": 220,
    "id_cercle": 801,
    "nom_commune": "Kourouba"
  },
  {
    "id_commune": 221,
    "id_cercle": 802,
    "nom_commune": "Ouelessebougou"
  },
  {
    "id_commune": 222,
    "id_cercle": 802,
    "nom_commune": "Sanankoro-Djitoumou"
  },
  {
    "id_commune": 223,
    "id_cercle": 801,
    "nom_commune": "Tiakadougou-Dialakoro"
  },
  {
    "id_commune": 224,
    "id_cercle": 803,
    "nom_commune": "Bougouni"
  },
  {
    "id_commune": 225,
    "id_cercle": 804,
    "nom_commune": "Debelin"
  },
  {
    "id_commune": 226,
    "id_cercle": 804,
    "nom_commune": "Domba"
  },
  {
    "id_commune": 227,
    "id_cercle": 803,
    "nom_commune": "Faradiele"
  },
  {
    "id_commune": 228,
    "id_cercle": 805,
    "nom_commune": "Garalo"
  },
  {
    "id_commune": 229,
    "id_cercle": 803,
    "nom_commune": "Keleya"
  },
  {
    "id_commune": 230,
    "id_cercle": 804,
    "nom_commune": "Koumantou"
  },
  {
    "id_commune": 231,
    "id_cercle": 806,
    "nom_commune": "Meridiela"
  },
  {
    "id_commune": 232,
    "id_cercle": 804,
    "nom_commune": "Sanso"
  },
  {
    "id_commune": 233,
    "id_cercle": 805,
    "nom_commune": "Sibirila"
  },
  {
    "id_commune": 234,
    "id_cercle": 803,
    "nom_commune": "Syentoula"
  },
  {
    "id_commune": 235,
    "id_cercle": 803,
    "nom_commune": "Tiemala Banimonotie"
  },
  {
    "id_commune": 236,
    "id_cercle": 804,
    "nom_commune": "Wola"
  },
  {
    "id_commune": 237,
    "id_cercle": 803,
    "nom_commune": "Zantiebougou"
  },
  {
    "id_commune": 238,
    "id_cercle": 807,
    "nom_commune": "Kolondieba"
  },
  {
    "id_commune": 239,
    "id_cercle": 808,
    "nom_commune": "Bougoula"
  },
  {
    "id_commune": 240,
    "id_cercle": 808,
    "nom_commune": "Fakola"
  },
  {
    "id_commune": 241,
    "id_cercle": 809,
    "nom_commune": "Kadiana"
  },
  {
    "id_commune": 242,
    "id_cercle": 807,
    "nom_commune": "Kebila"
  },
  {
    "id_commune": 243,
    "id_cercle": 807,
    "nom_commune": "Kolosso"
  },
  {
    "id_commune": 244,
    "id_cercle": 807,
    "nom_commune": "Mena"
  },
  {
    "id_commune": 245,
    "id_cercle": 809,
    "nom_commune": "Nangalasso"
  },
  {
    "id_commune": 246,
    "id_cercle": 807,
    "nom_commune": "N'Golodiana"
  },
  {
    "id_commune": 247,
    "id_cercle": 809,
    "nom_commune": "Tiongui"
  },
  {
    "id_commune": 248,
    "id_cercle": 810,
    "nom_commune": "Wassoulou-Balle"
  },
  {
    "id_commune": 249,
    "id_cercle": 801,
    "nom_commune": "Baya"
  },
  {
    "id_commune": 250,
    "id_cercle": 810,
    "nom_commune": "Gouanan"
  },
  {
    "id_commune": 251,
    "id_cercle": 810,
    "nom_commune": "Gouandiaka"
  },
  {
    "id_commune": 252,
    "id_cercle": 810,
    "nom_commune": "Koussan"
  },
  {
    "id_commune": 253,
    "id_cercle": 810,
    "nom_commune": "Sere Moussa Ani Samou de"
  },
  {
    "id_commune": 254,
    "id_cercle": 801,
    "nom_commune": "Tagandougou"
  },
  {
    "id_commune": 255,
    "id_cercle": 810,
    "nom_commune": "Yallankoro Soloba"
  },
  {
    "id_commune": 256,
    "id_cercle": 901,
    "nom_commune": "Koutiala"
  },
  {
    "id_commune": 257,
    "id_cercle": 902,
    "nom_commune": "Diedougou"
  },
  {
    "id_commune": 258,
    "id_cercle": 903,
    "nom_commune": "Fagui"
  },
  {
    "id_commune": 259,
    "id_cercle": 904,
    "nom_commune": "Gouadji Kao"
  },
  {
    "id_commune": 260,
    "id_cercle": 905,
    "nom_commune": "Gouadie Sougouna"
  },
  {
    "id_commune": 261,
    "id_cercle": 905,
    "nom_commune": "Kapala"
  },
  {
    "id_commune": 262,
    "id_cercle": 905,
    "nom_commune": "Kolonigue"
  },
  {
    "id_commune": 263,
    "id_cercle": 902,
    "nom_commune": "Konina"
  },
  {
    "id_commune": 264,
    "id_cercle": 905,
    "nom_commune": "Koningue"
  },
  {
    "id_commune": 265,
    "id_cercle": 902,
    "nom_commune": "Konseguela"
  },
  {
    "id_commune": 266,
    "id_cercle": 904,
    "nom_commune": "Koromo"
  },
  {
    "id_commune": 267,
    "id_cercle": 904,
    "nom_commune": "Kouniana"
  },
  {
    "id_commune": 268,
    "id_cercle": 901,
    "nom_commune": "Logouana"
  },
  {
    "id_commune": 269,
    "id_cercle": 906,
    "nom_commune": "Miena"
  },
  {
    "id_commune": 270,
    "id_cercle": 906,
    "nom_commune": "M�Pessoba"
  },
  {
    "id_commune": 271,
    "id_cercle": 901,
    "nom_commune": "Nafanga"
  },
  {
    "id_commune": 272,
    "id_cercle": 901,
    "nom_commune": "Nampe"
  },
  {
    "id_commune": 273,
    "id_cercle": 901,
    "nom_commune": "N'Golonianasso"
  },
  {
    "id_commune": 274,
    "id_cercle": 901,
    "nom_commune": "N'Goutjina"
  },
  {
    "id_commune": 275,
    "id_cercle": 904,
    "nom_commune": "Niantaga"
  },
  {
    "id_commune": 276,
    "id_cercle": 906,
    "nom_commune": "N'Tossoni"
  },
  {
    "id_commune": 277,
    "id_cercle": 901,
    "nom_commune": "Sincina"
  },
  {
    "id_commune": 278,
    "id_cercle": 901,
    "nom_commune": "Songo-Doubacore"
  },
  {
    "id_commune": 279,
    "id_cercle": 906,
    "nom_commune": "Tao"
  },
  {
    "id_commune": 280,
    "id_cercle": 904,
    "nom_commune": "Zanfigue"
  },
  {
    "id_commune": 281,
    "id_cercle": 903,
    "nom_commune": "Zangasso"
  },
  {
    "id_commune": 282,
    "id_cercle": 906,
    "nom_commune": "Zanina"
  },
  {
    "id_commune": 283,
    "id_cercle": 901,
    "nom_commune": "Zebala"
  },
  {
    "id_commune": 284,
    "id_cercle": 907,
    "nom_commune": "Yorosso"
  },
  {
    "id_commune": 285,
    "id_cercle": 907,
    "nom_commune": "Boura"
  },
  {
    "id_commune": 286,
    "id_cercle": 907,
    "nom_commune": "Karangana"
  },
  {
    "id_commune": 287,
    "id_cercle": 907,
    "nom_commune": "Kiffosso 1"
  },
  {
    "id_commune": 288,
    "id_cercle": 908,
    "nom_commune": "Koury"
  },
  {
    "id_commune": 289,
    "id_cercle": 907,
    "nom_commune": "Mahou"
  },
  {
    "id_commune": 290,
    "id_cercle": 907,
    "nom_commune": "Menamba 1"
  },
  {
    "id_commune": 291,
    "id_cercle": 908,
    "nom_commune": "Ourikela"
  },
  {
    "id_commune": 292,
    "id_cercle": 901,
    "nom_commune": "Diaramana"
  },
  {
    "id_commune": 293,
    "id_cercle": 1001,
    "nom_commune": "Segou"
  },
  {
    "id_commune": 294,
    "id_cercle": 1002,
    "nom_commune": "Boussin"
  },
  {
    "id_commune": 295,
    "id_cercle": 1001,
    "nom_commune": "Cinzana"
  },
  {
    "id_commune": 296,
    "id_cercle": 1003,
    "nom_commune": "Diedougou"
  },
  {
    "id_commune": 297,
    "id_cercle": 1003,
    "nom_commune": "Dioro"
  },
  {
    "id_commune": 298,
    "id_cercle": 1002,
    "nom_commune": "Dougabougou"
  },
  {
    "id_commune": 299,
    "id_cercle": 1003,
    "nom_commune": "Farakou Massa"
  },
  {
    "id_commune": 300,
    "id_cercle": 1001,
    "nom_commune": "Fatine"
  },
  {
    "id_commune": 301,
    "id_cercle": 1001,
    "nom_commune": "Katiena"
  },
  {
    "id_commune": 302,
    "id_cercle": 1001,
    "nom_commune": "Konodimini"
  },
  {
    "id_commune": 303,
    "id_cercle": 1002,
    "nom_commune": "Markala"
  },
  {
    "id_commune": 304,
    "id_cercle": 1001,
    "nom_commune": "N'Gara"
  },
  {
    "id_commune": 305,
    "id_cercle": 1001,
    "nom_commune": "Pelengana"
  },
  {
    "id_commune": 306,
    "id_cercle": 1002,
    "nom_commune": "Sansanding"
  },
  {
    "id_commune": 307,
    "id_cercle": 1001,
    "nom_commune": "Sebougou"
  },
  {
    "id_commune": 308,
    "id_cercle": 1002,
    "nom_commune": "Sibila"
  },
  {
    "id_commune": 309,
    "id_cercle": 1004,
    "nom_commune": "Souba"
  },
  {
    "id_commune": 310,
    "id_cercle": 1005,
    "nom_commune": "Baroueli"
  },
  {
    "id_commune": 311,
    "id_cercle": 1005,
    "nom_commune": "Boidie"
  },
  {
    "id_commune": 312,
    "id_cercle": 1005,
    "nom_commune": "Kalake"
  },
  {
    "id_commune": 313,
    "id_cercle": 1005,
    "nom_commune": "Konobougou"
  },
  {
    "id_commune": 314,
    "id_cercle": 1005,
    "nom_commune": "Sanando"
  },
  {
    "id_commune": 315,
    "id_cercle": 1005,
    "nom_commune": "Tamani"
  },
  {
    "id_commune": 316,
    "id_cercle": 1005,
    "nom_commune": "Tesserela"
  },
  {
    "id_commune": 317,
    "id_cercle": 1006,
    "nom_commune": "Bla"
  },
  {
    "id_commune": 318,
    "id_cercle": 1006,
    "nom_commune": "Beguene"
  },
  {
    "id_commune": 319,
    "id_cercle": 1006,
    "nom_commune": "Diena"
  },
  {
    "id_commune": 320,
    "id_cercle": 1006,
    "nom_commune": "Falo"
  },
  {
    "id_commune": 321,
    "id_cercle": 1006,
    "nom_commune": "Kemeni"
  },
  {
    "id_commune": 322,
    "id_cercle": 1006,
    "nom_commune": "Somasso"
  },
  {
    "id_commune": 323,
    "id_cercle": 1006,
    "nom_commune": "Touna"
  },
  {
    "id_commune": 324,
    "id_cercle": 1007,
    "nom_commune": "Macina"
  },
  {
    "id_commune": 325,
    "id_cercle": 1007,
    "nom_commune": "Boky Were"
  },
  {
    "id_commune": 326,
    "id_cercle": 1002,
    "nom_commune": "Folomana"
  },
  {
    "id_commune": 327,
    "id_cercle": 1007,
    "nom_commune": "Kokry Centre"
  },
  {
    "id_commune": 328,
    "id_cercle": 1007,
    "nom_commune": "Monimpebougou"
  },
  {
    "id_commune": 329,
    "id_cercle": 1002,
    "nom_commune": "Saloba"
  },
  {
    "id_commune": 330,
    "id_cercle": 1007,
    "nom_commune": "Sana"
  },
  {
    "id_commune": 331,
    "id_cercle": 1002,
    "nom_commune": "Souleye"
  },
  {
    "id_commune": 332,
    "id_cercle": 1008,
    "nom_commune": "Niono"
  },
  {
    "id_commune": 333,
    "id_cercle": 1009,
    "nom_commune": "Diabaly"
  },
  {
    "id_commune": 334,
    "id_cercle": 1008,
    "nom_commune": "Kala Siguida"
  },
  {
    "id_commune": 335,
    "id_cercle": 1008,
    "nom_commune": "Siribala"
  },
  {
    "id_commune": 336,
    "id_cercle": 1008,
    "nom_commune": "Sirifila Boundy"
  },
  {
    "id_commune": 337,
    "id_cercle": 1009,
    "nom_commune": "Sokolo"
  },
  {
    "id_commune": 338,
    "id_cercle": 1008,
    "nom_commune": "Yeredon Saniona"
  },
  {
    "id_commune": 339,
    "id_cercle": 1010,
    "nom_commune": "Kareri"
  },
  {
    "id_commune": 340,
    "id_cercle": 1010,
    "nom_commune": "Diguicire"
  },
  {
    "id_commune": 341,
    "id_cercle": 1101,
    "nom_commune": "Fani"
  },
  {
    "id_commune": 342,
    "id_cercle": 1101,
    "nom_commune": "Kazangasso"
  },
  {
    "id_commune": 343,
    "id_cercle": 1101,
    "nom_commune": "Korodougou"
  },
  {
    "id_commune": 344,
    "id_cercle": 1101,
    "nom_commune": "Koulandougou"
  },
  {
    "id_commune": 345,
    "id_cercle": 1101,
    "nom_commune": "Yangasso"
  },
  {
    "id_commune": 346,
    "id_cercle": 1102,
    "nom_commune": "San"
  },
  {
    "id_commune": 347,
    "id_cercle": 1102,
    "nom_commune": "Baramandougou"
  },
  {
    "id_commune": 348,
    "id_cercle": 1103,
    "nom_commune": "Dah"
  },
  {
    "id_commune": 349,
    "id_cercle": 1103,
    "nom_commune": "Diakourouna"
  },
  {
    "id_commune": 350,
    "id_cercle": 1101,
    "nom_commune": "Dieli"
  },
  {
    "id_commune": 351,
    "id_cercle": 1103,
    "nom_commune": "Kaniegue"
  },
  {
    "id_commune": 352,
    "id_cercle": 1103,
    "nom_commune": "Kassorola"
  },
  {
    "id_commune": 353,
    "id_cercle": 1103,
    "nom_commune": "Kava"
  },
  {
    "id_commune": 354,
    "id_cercle": 1103,
    "nom_commune": "Moribila"
  },
  {
    "id_commune": 355,
    "id_cercle": 1102,
    "nom_commune": "N'Goa"
  },
  {
    "id_commune": 356,
    "id_cercle": 1101,
    "nom_commune": "Niamana"
  },
  {
    "id_commune": 357,
    "id_cercle": 1102,
    "nom_commune": "Niasso"
  },
  {
    "id_commune": 358,
    "id_cercle": 1104,
    "nom_commune": "Ouolon"
  },
  {
    "id_commune": 359,
    "id_cercle": 1104,
    "nom_commune": "Siadougou"
  },
  {
    "id_commune": 360,
    "id_cercle": 1103,
    "nom_commune": "Sourountouna"
  },
  {
    "id_commune": 361,
    "id_cercle": 1102,
    "nom_commune": "Tene"
  },
  {
    "id_commune": 362,
    "id_cercle": 1103,
    "nom_commune": "Tourakolomba"
  },
  {
    "id_commune": 363,
    "id_cercle": 1103,
    "nom_commune": "Waki"
  },
  {
    "id_commune": 364,
    "id_cercle": 1105,
    "nom_commune": "Tominian"
  },
  {
    "id_commune": 365,
    "id_cercle": 1105,
    "nom_commune": "Benena"
  },
  {
    "id_commune": 366,
    "id_cercle": 1106,
    "nom_commune": "Diora"
  },
  {
    "id_commune": 367,
    "id_cercle": 1105,
    "nom_commune": "Koula"
  },
  {
    "id_commune": 368,
    "id_cercle": 1105,
    "nom_commune": "Lanfiala"
  },
  {
    "id_commune": 369,
    "id_cercle": 1106,
    "nom_commune": "Mafoune"
  },
  {
    "id_commune": 370,
    "id_cercle": 1106,
    "nom_commune": "Mandiakuy"
  },
  {
    "id_commune": 371,
    "id_cercle": 1107,
    "nom_commune": "Ouan"
  },
  {
    "id_commune": 372,
    "id_cercle": 1106,
    "nom_commune": "Sanekuy"
  },
  {
    "id_commune": 373,
    "id_cercle": 1107,
    "nom_commune": "Timissa"
  },
  {
    "id_commune": 374,
    "id_cercle": 1105,
    "nom_commune": "Yasso"
  },
  {
    "id_commune": 375,
    "id_cercle": 1201,
    "nom_commune": "Mopti"
  },
  {
    "id_commune": 376,
    "id_cercle": 1201,
    "nom_commune": "Bassirou"
  },
  {
    "id_commune": 377,
    "id_cercle": 1201,
    "nom_commune": "Fatoma"
  },
  {
    "id_commune": 378,
    "id_cercle": 1202,
    "nom_commune": "Konna"
  },
  {
    "id_commune": 379,
    "id_cercle": 1202,
    "nom_commune": "Kontza"
  },
  {
    "id_commune": 380,
    "id_cercle": 1203,
    "nom_commune": "Korombana"
  },
  {
    "id_commune": 381,
    "id_cercle": 1203,
    "nom_commune": "Gouloumbou"
  },
  {
    "id_commune": 382,
    "id_cercle": 1203,
    "nom_commune": "Doko"
  },
  {
    "id_commune": 383,
    "id_cercle": 1201,
    "nom_commune": "Sio"
  },
  {
    "id_commune": 384,
    "id_cercle": 1201,
    "nom_commune": "Socoura"
  },
  {
    "id_commune": 385,
    "id_cercle": 1204,
    "nom_commune": "Djenne"
  },
  {
    "id_commune": 386,
    "id_cercle": 1204,
    "nom_commune": "Dandougou Fakala"
  },
  {
    "id_commune": 387,
    "id_cercle": 1205,
    "nom_commune": "Fakala"
  },
  {
    "id_commune": 388,
    "id_cercle": 1204,
    "nom_commune": "Femaye"
  },
  {
    "id_commune": 389,
    "id_cercle": 1204,
    "nom_commune": "Madiama"
  },
  {
    "id_commune": 390,
    "id_cercle": 1204,
    "nom_commune": "Nema Badenyakafo"
  },
  {
    "id_commune": 391,
    "id_cercle": 1204,
    "nom_commune": "Pondori"
  },
  {
    "id_commune": 392,
    "id_cercle": 1206,
    "nom_commune": "Tenenkou"
  },
  {
    "id_commune": 393,
    "id_cercle": 1206,
    "nom_commune": "Diafarabe"
  },
  {
    "id_commune": 394,
    "id_cercle": 1206,
    "nom_commune": "Diaka"
  },
  {
    "id_commune": 395,
    "id_cercle": 1206,
    "nom_commune": "Diondiori"
  },
  {
    "id_commune": 396,
    "id_cercle": 1206,
    "nom_commune": "Ouro Ardo"
  },
  {
    "id_commune": 397,
    "id_cercle": 1206,
    "nom_commune": "Ouro Guire"
  },
  {
    "id_commune": 398,
    "id_cercle": 1206,
    "nom_commune": "Sougoulbe"
  },
  {
    "id_commune": 399,
    "id_cercle": 1207,
    "nom_commune": "Youwarou"
  },
  {
    "id_commune": 400,
    "id_cercle": 1207,
    "nom_commune": "Bimbere Tama"
  },
  {
    "id_commune": 401,
    "id_cercle": 1207,
    "nom_commune": "Deboye"
  },
  {
    "id_commune": 402,
    "id_cercle": 1207,
    "nom_commune": "Dirma"
  },
  {
    "id_commune": 403,
    "id_cercle": 1207,
    "nom_commune": "Dongo"
  },
  {
    "id_commune": 404,
    "id_cercle": 1207,
    "nom_commune": "Farimake"
  },
  {
    "id_commune": 405,
    "id_cercle": 1207,
    "nom_commune": "N'Dodjiga"
  },
  {
    "id_commune": 406,
    "id_cercle": 1301,
    "nom_commune": "Bandiagara"
  },
  {
    "id_commune": 407,
    "id_cercle": 1302,
    "nom_commune": "Diamnati"
  },
  {
    "id_commune": 408,
    "id_cercle": 1301,
    "nom_commune": "Dourou"
  },
  {
    "id_commune": 409,
    "id_cercle": 1303,
    "nom_commune": "Kende"
  },
  {
    "id_commune": 410,
    "id_cercle": 1303,
    "nom_commune": "Kendie"
  },
  {
    "id_commune": 411,
    "id_cercle": 1302,
    "nom_commune": "Metoumou"
  },
  {
    "id_commune": 412,
    "id_cercle": 1304,
    "nom_commune": "Sangha"
  },
  {
    "id_commune": 413,
    "id_cercle": 1304,
    "nom_commune": "Ireli"
  },
  {
    "id_commune": 414,
    "id_cercle": 1302,
    "nom_commune": "Segue Ire"
  },
  {
    "id_commune": 415,
    "id_cercle": 1301,
    "nom_commune": "Soroly"
  },
  {
    "id_commune": 416,
    "id_cercle": 1305,
    "nom_commune": "Wadouba"
  },
  {
    "id_commune": 417,
    "id_cercle": 1305,
    "nom_commune": "Ouroli"
  },
  {
    "id_commune": 418,
    "id_cercle": 1305,
    "nom_commune": "Menthely"
  },
  {
    "id_commune": 419,
    "id_cercle": 1306,
    "nom_commune": "Bankass"
  },
  {
    "id_commune": 420,
    "id_cercle": 1307,
    "nom_commune": "Diallassagou"
  },
  {
    "id_commune": 421,
    "id_cercle": 1306,
    "nom_commune": "Dimbal Habbe"
  },
  {
    "id_commune": 422,
    "id_cercle": 1306,
    "nom_commune": "Kani-Bonzon"
  },
  {
    "id_commune": 423,
    "id_cercle": 1307,
    "nom_commune": "Lessagou Habe"
  },
  {
    "id_commune": 424,
    "id_cercle": 1306,
    "nom_commune": "Segue"
  },
  {
    "id_commune": 425,
    "id_cercle": 1308,
    "nom_commune": "Sokoura"
  },
  {
    "id_commune": 426,
    "id_cercle": 1307,
    "nom_commune": "Soubala"
  },
  {
    "id_commune": 427,
    "id_cercle": 1307,
    "nom_commune": "Tori"
  },
  {
    "id_commune": 428,
    "id_cercle": 1309,
    "nom_commune": "Koro"
  },
  {
    "id_commune": 429,
    "id_cercle": 1309,
    "nom_commune": "Barapireli"
  },
  {
    "id_commune": 430,
    "id_cercle": 1309,
    "nom_commune": "Bondo"
  },
  {
    "id_commune": 431,
    "id_cercle": 1309,
    "nom_commune": "Dougoutene 1"
  },
  {
    "id_commune": 432,
    "id_cercle": 1309,
    "nom_commune": "Dougoutene 2"
  },
  {
    "id_commune": 433,
    "id_cercle": 1309,
    "nom_commune": "Koporo Pen"
  },
  {
    "id_commune": 434,
    "id_cercle": 1309,
    "nom_commune": "Koporokendie Na"
  },
  {
    "id_commune": 435,
    "id_cercle": 1309,
    "nom_commune": "Madougou"
  },
  {
    "id_commune": 436,
    "id_cercle": 1309,
    "nom_commune": "Pel Maoude"
  },
  {
    "id_commune": 437,
    "id_cercle": 1309,
    "nom_commune": "Youdiou"
  },
  {
    "id_commune": 438,
    "id_cercle": 1401,
    "nom_commune": "Douentza"
  },
  {
    "id_commune": 439,
    "id_cercle": 1401,
    "nom_commune": "Debere"
  },
  {
    "id_commune": 440,
    "id_cercle": 1402,
    "nom_commune": "Dangol-Bore"
  },
  {
    "id_commune": 441,
    "id_cercle": 1402,
    "nom_commune": "N'Doumpa"
  },
  {
    "id_commune": 442,
    "id_cercle": 1402,
    "nom_commune": "Doumbara"
  },
  {
    "id_commune": 443,
    "id_cercle": 1401,
    "nom_commune": "Dianwely"
  },
  {
    "id_commune": 444,
    "id_cercle": 1401,
    "nom_commune": "Korarou"
  },
  {
    "id_commune": 445,
    "id_cercle": 1401,
    "nom_commune": "Koubewel Koundia"
  },
  {
    "id_commune": 446,
    "id_cercle": 1401,
    "nom_commune": "Petaka"
  },
  {
    "id_commune": 447,
    "id_cercle": 1401,
    "nom_commune": "Tedie"
  },
  {
    "id_commune": 448,
    "id_cercle": 1403,
    "nom_commune": "Tombouctou"
  },
  {
    "id_commune": 449,
    "id_cercle": 1403,
    "nom_commune": "Alafia"
  },
  {
    "id_commune": 450,
    "id_cercle": 1501,
    "nom_commune": "Ber"
  },
  {
    "id_commune": 451,
    "id_cercle": 1501,
    "nom_commune": "Zarho"
  },
  {
    "id_commune": 452,
    "id_cercle": 1403,
    "nom_commune": "Lafia"
  },
  {
    "id_commune": 453,
    "id_cercle": 1502,
    "nom_commune": "Dire"
  },
  {
    "id_commune": 454,
    "id_cercle": 1502,
    "nom_commune": "Arham"
  },
  {
    "id_commune": 455,
    "id_cercle": 1502,
    "nom_commune": "Binga"
  },
  {
    "id_commune": 456,
    "id_cercle": 1502,
    "nom_commune": "Dangha"
  },
  {
    "id_commune": 457,
    "id_cercle": 1502,
    "nom_commune": "Garbakoira"
  },
  {
    "id_commune": 458,
    "id_cercle": 1502,
    "nom_commune": "Haibongo"
  },
  {
    "id_commune": 459,
    "id_cercle": 1502,
    "nom_commune": "Kondi"
  },
  {
    "id_commune": 460,
    "id_cercle": 1502,
    "nom_commune": "Sareyamou"
  },
  {
    "id_commune": 461,
    "id_cercle": 1502,
    "nom_commune": "Tienkour"
  },
  {
    "id_commune": 462,
    "id_cercle": 1502,
    "nom_commune": "Tindirma"
  },
  {
    "id_commune": 463,
    "id_cercle": 1503,
    "nom_commune": "Goundam"
  },
  {
    "id_commune": 464,
    "id_cercle": 1504,
    "nom_commune": "Bintagoungou"
  },
  {
    "id_commune": 465,
    "id_cercle": 1503,
    "nom_commune": "Douekire"
  },
  {
    "id_commune": 466,
    "id_cercle": 1503,
    "nom_commune": "Essakane"
  },
  {
    "id_commune": 467,
    "id_cercle": 1505,
    "nom_commune": "Gargando"
  },
  {
    "id_commune": 468,
    "id_cercle": 1504,
    "nom_commune": "Issa Bery"
  },
  {
    "id_commune": 469,
    "id_cercle": 1504,
    "nom_commune": "M'Bouna"
  },
  {
    "id_commune": 470,
    "id_cercle": 1505,
    "nom_commune": "Raz-El-Ma"
  },
  {
    "id_commune": 471,
    "id_cercle": 1503,
    "nom_commune": "Tele"
  },
  {
    "id_commune": 472,
    "id_cercle": 1505,
    "nom_commune": "Tilemsi"
  },
  {
    "id_commune": 473,
    "id_cercle": 1506,
    "nom_commune": "Tonka"
  },
  {
    "id_commune": 474,
    "id_cercle": 1503,
    "nom_commune": "Tonka"
  },
  {
    "id_commune": 475,
    "id_cercle": 1507,
    "nom_commune": "Rharous"
  },
  {
    "id_commune": 476,
    "id_cercle": 1508,
    "nom_commune": "Bambara-Maoude"
  },
  {
    "id_commune": 477,
    "id_cercle": 1508,
    "nom_commune": "Haribomo"
  },
  {
    "id_commune": 478,
    "id_cercle": 1507,
    "nom_commune": "Serere"
  },
  {
    "id_commune": 479,
    "id_cercle": 1509,
    "nom_commune": "Soboundou"
  },
  {
    "id_commune": 480,
    "id_cercle": 1510,
    "nom_commune": "Banikane Narhawa"
  },
  {
    "id_commune": 481,
    "id_cercle": 1511,
    "nom_commune": "Dianke"
  },
  {
    "id_commune": 482,
    "id_cercle": 1510,
    "nom_commune": "Fittouga"
  },
  {
    "id_commune": 483,
    "id_cercle": 1510,
    "nom_commune": "Koumaira"
  },
  {
    "id_commune": 484,
    "id_cercle": 1511,
    "nom_commune": "Lere"
  },
  {
    "id_commune": 485,
    "id_cercle": 1510,
    "nom_commune": "N'Gorkou"
  },
  {
    "id_commune": 486,
    "id_cercle": 1509,
    "nom_commune": "Soumpi"
  },
  {
    "id_commune": 487,
    "id_cercle": 1601,
    "nom_commune": "Gao"
  },
  {
    "id_commune": 488,
    "id_cercle": 1602,
    "nom_commune": "Gabero"
  },
  {
    "id_commune": 489,
    "id_cercle": 1602,
    "nom_commune": "Zinda"
  },
  {
    "id_commune": 490,
    "id_cercle": 1601,
    "nom_commune": "Gounzoureye"
  },
  {
    "id_commune": 491,
    "id_cercle": 1603,
    "nom_commune": "Tacharane"
  },
  {
    "id_commune": 492,
    "id_cercle": 1604,
    "nom_commune": "Magnadaoue"
  },
  {
    "id_commune": 493,
    "id_cercle": 1604,
    "nom_commune": "Soni Aliber"
  },
  {
    "id_commune": 494,
    "id_cercle": 1605,
    "nom_commune": "Ansongo"
  },
  {
    "id_commune": 495,
    "id_cercle": 1606,
    "nom_commune": "Aroun"
  },
  {
    "id_commune": 496,
    "id_cercle": 1606,
    "nom_commune": "Tessit"
  },
  {
    "id_commune": 497,
    "id_cercle": 1605,
    "nom_commune": "Tin-Hamma"
  },
  {
    "id_commune": 498,
    "id_cercle": 1607,
    "nom_commune": "Bourem"
  },
  {
    "id_commune": 499,
    "id_cercle": 1608,
    "nom_commune": "Bamba"
  },
  {
    "id_commune": 500,
    "id_cercle": 1607,
    "nom_commune": "Taboye"
  },
  {
    "id_commune": 501,
    "id_cercle": 1608,
    "nom_commune": "Temera"
  },
  {
    "id_commune": 502,
    "id_cercle": 1701,
    "nom_commune": "Kidal"
  },
  {
    "id_commune": 503,
    "id_cercle": 1701,
    "nom_commune": "Agharous"
  },
  {
    "id_commune": 504,
    "id_cercle": 1702,
    "nom_commune": "Anefif"
  },
  {
    "id_commune": 505,
    "id_cercle": 1701,
    "nom_commune": "Essouk"
  },
  {
    "id_commune": 506,
    "id_cercle": 1703,
    "nom_commune": "Abeibara"
  },
  {
    "id_commune": 507,
    "id_cercle": 1703,
    "nom_commune": "Boghassa"
  },
  {
    "id_commune": 508,
    "id_cercle": 1703,
    "nom_commune": "Tinzawatene"
  },
  {
    "id_commune": 509,
    "id_cercle": 1704,
    "nom_commune": "Tessalit"
  },
  {
    "id_commune": 510,
    "id_cercle": 1705,
    "nom_commune": "Aguel-Hoc"
  },
  {
    "id_commune": 511,
    "id_cercle": 1704,
    "nom_commune": "Timtaghene"
  },
  {
    "id_commune": 512,
    "id_cercle": 1706,
    "nom_commune": "Tin-Essako"
  },
  {
    "id_commune": 513,
    "id_cercle": 1801,
    "nom_commune": "Taoudenni"
  },
  {
    "id_commune": 514,
    "id_cercle": 1801,
    "nom_commune": "Alougla"
  },
  {
    "id_commune": 515,
    "id_cercle": 1801,
    "nom_commune": "Teghaza"
  },
  {
    "id_commune": 516,
    "id_cercle": 1801,
    "nom_commune": "Zouelya"
  },
  {
    "id_commune": 517,
    "id_cercle": 1802,
    "nom_commune": "Almatla"
  },
  {
    "id_commune": 518,
    "id_cercle": 1803,
    "nom_commune": "Al-Ourche"
  },
  {
    "id_commune": 519,
    "id_cercle": 1803,
    "nom_commune": "Diaba"
  },
  {
    "id_commune": 520,
    "id_cercle": 1803,
    "nom_commune": "Nibkit-El Elk"
  },
  {
    "id_commune": 521,
    "id_cercle": 1803,
    "nom_commune": "Oum-Laazam"
  },
  {
    "id_commune": 522,
    "id_cercle": 1803,
    "nom_commune": "Tamagounite"
  },
  {
    "id_commune": 523,
    "id_cercle": 1803,
    "nom_commune": "Touwal"
  },
  {
    "id_commune": 524,
    "id_cercle": 1804,
    "nom_commune": "Araouane"
  },
  {
    "id_commune": 525,
    "id_cercle": 1804,
    "nom_commune": "Achamour"
  },
  {
    "id_commune": 526,
    "id_cercle": 1804,
    "nom_commune": "M'Back-Samna"
  },
  {
    "id_commune": 527,
    "id_cercle": 1804,
    "nom_commune": "Tineguelhadj"
  },
  {
    "id_commune": 528,
    "id_cercle": 1805,
    "nom_commune": "Bou-Djebeha"
  },
  {
    "id_commune": 529,
    "id_cercle": 1805,
    "nom_commune": "Erg-Lakhal"
  },
  {
    "id_commune": 530,
    "id_cercle": 1805,
    "nom_commune": "Limgassim"
  },
  {
    "id_commune": 531,
    "id_cercle": 1806,
    "nom_commune": "Foum-Elba"
  },
  {
    "id_commune": 532,
    "id_cercle": 1806,
    "nom_commune": "Bougwera"
  },
  {
    "id_commune": 533,
    "id_cercle": 1806,
    "nom_commune": "Lamhaimide"
  },
  {
    "id_commune": 534,
    "id_cercle": 1901,
    "nom_commune": "Menaka"
  },
  {
    "id_commune": 535,
    "id_cercle": 1901,
    "nom_commune": "Assakaraye"
  },
  {
    "id_commune": 536,
    "id_cercle": 1901,
    "nom_commune": "Inazole"
  },
  {
    "id_commune": 537,
    "id_cercle": 1901,
    "nom_commune": "Infoukaretane"
  },
  {
    "id_commune": 538,
    "id_cercle": 1901,
    "nom_commune": "Iziguirete"
  },
  {
    "id_commune": 539,
    "id_cercle": 1901,
    "nom_commune": "Tabankort"
  },
  {
    "id_commune": 540,
    "id_cercle": 1901,
    "nom_commune": "Tin Abaw"
  },
  {
    "id_commune": 541,
    "id_cercle": 1902,
    "nom_commune": "Anderamboukane"
  },
  {
    "id_commune": 542,
    "id_cercle": 1902,
    "nom_commune": "Azawak"
  },
  {
    "id_commune": 543,
    "id_cercle": 1903,
    "nom_commune": "Inekar"
  },
  {
    "id_commune": 544,
    "id_cercle": 1903,
    "nom_commune": "Inlamawane"
  },
  {
    "id_commune": 545,
    "id_cercle": 1904,
    "nom_commune": "Inlamawane"
  },
  {
    "id_commune": 546,
    "id_cercle": 1903,
    "nom_commune": "Tadriante"
  },
  {
    "id_commune": 547,
    "id_cercle": 1903,
    "nom_commune": "Tissouakh"
  },
  {
    "id_commune": 548,
    "id_cercle": 1905,
    "nom_commune": "Tidermene"
  },
  {
    "id_commune": 549,
    "id_cercle": 1905,
    "nom_commune": "Chiman"
  },
  {
    "id_commune": 550,
    "id_cercle": 1905,
    "nom_commune": "Inhinita"
  },
  {
    "id_commune": 551,
    "id_cercle": 1905,
    "nom_commune": "Intadeyne"
  },
  {
    "id_commune": 552,
    "id_cercle": 1905,
    "nom_commune": "Teguerert"
  },
  {
    "id_commune": 553,
    "id_cercle": 9001,
    "nom_commune": "Commune 6"
  },
  {
    "id_commune": 554,
    "id_cercle": 9001,
    "nom_commune": "Commune 1"
  },
  {
    "id_commune": 555,
    "id_cercle": 9001,
    "nom_commune": "Commune 4"
  },
  {
    "id_commune": 556,
    "id_cercle": 9001,
    "nom_commune": "Commune 7"
  },
  {
    "id_commune": 557,
    "id_cercle": 9001,
    "nom_commune": "Commune 2"
  },
  {
    "id_commune": 558,
    "id_cercle": 9001,
    "nom_commune": "Commune 3"
  },
  {
    "id_commune": 559,
    "id_cercle": 9001,
    "nom_commune": "Commune 5"
  }
]
