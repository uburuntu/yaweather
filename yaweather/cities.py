"""
Latitudes and longitudes for top-1000 cities by population

Data provided by: https://simplemaps.com/data/world-cities
"""
from typing import Dict, Tuple


class CountryBase:
    @classmethod
    def name(cls) -> str:
        return cls.__name__

    @classmethod
    def cities(cls) -> Dict[str, Tuple[float, float]]:
        return {k: v for k, v in cls.__dict__.items() if isinstance(v, tuple)}


class Japan(CountryBase):
    Tokyo = (35.685, 139.7514)
    Osaka = (34.75, 135.4601)
    Yokohama = (35.32, 139.58)
    Nagoya = (35.155, 136.915)
    Fukuoka = (33.595, 130.41)
    Sapporo = (43.075, 141.34)
    Sendai = (38.2871, 141.0217)
    Hiroshima = (34.3878, 132.4429)
    Kyoto = (35.03, 135.75)
    Kobe = (34.68, 135.17)
    Kawanakajima = (35.53, 139.705)
    Kitaku = (33.8704, 130.82)
    Hamamatsu = (34.7181, 137.7327)
    Naha = (26.2072, 127.673)
    Okayama = (34.672, 133.9171)
    Kumamoto = (32.8009, 130.7006)
    Shizuoka = (34.9858, 138.3854)
    Utsunomiya = (36.55, 139.87)
    Nagano = (36.65, 138.17)
    Hachioji = (35.6577, 139.3261)
    Niigata = (37.92, 139.04)
    Kagoshima = (31.586, 130.5611)
    Kanazawa = (36.56, 136.64)


class UnitedStates(CountryBase):
    NewYork = (40.6943, -73.9249)
    LosAngeles = (34.1139, -118.4068)
    Chicago = (41.8373, -87.6862)
    Miami = (25.7839, -80.2102)
    Dallas = (32.7936, -96.7662)
    Philadelphia = (40.0077, -75.1339)
    Houston = (29.7869, -95.3905)
    Washington = (38.9047, -77.0163)
    Atlanta = (33.7627, -84.4225)
    Boston = (42.3188, -71.0846)
    Phoenix = (33.5722, -112.0891)
    Seattle = (47.6211, -122.3244)
    SanFrancisco = (37.7562, -122.443)
    Detroit = (42.3834, -83.1024)
    SanDiego = (32.8312, -117.1225)
    Minneapolis = (44.9635, -93.2678)
    Tampa = (27.9942, -82.4451)
    Denver = (39.7621, -104.8759)
    Brooklyn = (40.6501, -73.9496)
    Queens = (40.7498, -73.7976)
    Baltimore = (39.3051, -76.6144)
    Riverside = (33.9381, -117.3948)
    StLouis = (38.6358, -90.2451)
    LasVegas = (36.2333, -115.2654)
    Portland = (45.5371, -122.65)
    SanAntonio = (29.4658, -98.5254)
    Sacramento = (38.5667, -121.4683)
    SanJose = (37.3021, -121.8489)
    Orlando = (28.4772, -81.3369)
    Cleveland = (41.4767, -81.6805)
    Pittsburgh = (40.4396, -79.9763)
    Cincinnati = (39.1412, -84.506)
    Manhattan = (40.7834, -73.9662)
    Austin = (30.3006, -97.7517)
    KansasCity = (39.1239, -94.5541)
    Indianapolis = (39.7771, -86.1458)
    Columbus = (39.986, -82.9851)
    VirginiaBeach = (36.7335, -76.0435)
    Charlotte = (35.2079, -80.8304)
    Bronx = (40.8501, -73.8662)
    Milwaukee = (43.0642, -87.9673)
    Providence = (41.823, -71.4187)
    Jacksonville = (30.3322, -81.6749)
    SaltLakeCity = (40.7774, -111.93)
    Nashville = (36.1715, -86.7843)
    Memphis = (35.1046, -89.9773)
    Richmond = (37.5295, -77.4756)
    NewOrleans = (30.0687, -89.9288)
    Raleigh = (35.8324, -78.6438)
    Louisville = (38.1663, -85.6485)
    OklahomaCity = (35.4676, -97.5137)
    Bridgeport = (41.1918, -73.1953)
    Buffalo = (42.9017, -78.8487)
    Hartford = (41.7661, -72.6834)
    FortWorth = (32.7812, -97.3472)
    Tucson = (32.1545, -110.8782)
    ElPaso = (31.8479, -106.4309)
    Honolulu = (21.3294, -157.846)
    Omaha = (41.2628, -96.0498)
    McAllen = (26.2273, -98.2471)
    Albuquerque = (35.1053, -106.6464)
    Birmingham = (33.5277, -86.7987)
    Dayton = (39.7797, -84.1998)
    Rochester = (43.168, -77.6162)
    Sarasota = (27.3386, -82.543)
    Fresno = (36.7831, -119.7941)
    Allentown = (40.5961, -75.4755)
    Tulsa = (36.1284, -95.9043)
    Concord = (37.9722, -122.0016)
    CapeCoral = (26.6445, -81.9955)
    Springfield = (42.1155, -72.5395)
    ColoradoSprings = (38.8674, -104.7606)
    Charleston = (32.8151, -79.963)
    GrandRapids = (42.9615, -85.6557)
    MissionViejo = (33.6095, -117.655)
    Albany = (42.6664, -73.7987)
    Knoxville = (35.9692, -83.9496)
    BatonRouge = (30.4419, -91.131)
    Bakersfield = (35.353, -119.0359)
    Ogden = (41.228, -111.9677)
    NewHaven = (41.3112, -72.9246)
    Columbia = (34.0376, -80.9037)
    Akron = (41.0798, -81.5219)


class Mexico(CountryBase):
    MexicoCity = (19.4424, -99.131)
    Guadalajara = (20.67, -103.33)
    Monterrey = (25.67, -100.33)
    Puebla = (19.05, -98.2)
    Tijuana = (32.5, -117.08)
    Toluca = (19.3304, -99.67)
    LeondelosAldama = (21.15, -101.7)
    Juarez = (31.6904, -106.49)
    Torreon = (25.5701, -103.42)
    CiudadNezahualcoyotl = (19.41, -99.03)
    SanLuisPotosi = (22.17, -101.0)
    Merida = (20.9666, -89.6166)
    Queretaro = (20.63, -100.38)
    Mexicali = (32.65, -115.48)
    Aguascalientes = (21.8795, -102.2904)
    Tampico = (22.3, -97.87)
    Cuernavaca = (18.9211, -99.24)
    Culiacan = (24.83, -107.38)
    Chihuahua = (28.645, -106.085)
    Saltillo = (25.42, -101.005)
    AcapulcodeJuarez = (16.85, -99.916)
    Morelia = (19.7334, -101.1895)
    Hermosillo = (29.0989, -110.9541)
    Veracruz = (19.1773, -96.16)
    Cancun = (21.17, -86.83)
    HeroicaMatamoros = (25.88, -97.5)


class India(CountryBase):
    Mumbai = (19.017, 72.857)
    Delhi = (28.67, 77.23)
    Kolkata = (22.495, 88.3247)
    Chennai = (13.09, 80.28)
    Bengaluru = (12.97, 77.56)
    Hyderabad = (17.4, 78.48)
    Ahmadabad = (23.0301, 72.58)
    Haora = (22.5804, 88.3299)
    Pune = (18.53, 73.85)
    Surat = (21.2, 72.84)
    Cawnpore = (26.46, 80.32)
    Jaipur = (26.9211, 75.81)
    Lucknow = (26.855, 80.915)
    Nagpur = (21.17, 79.09)
    Patna = (25.625, 85.13)
    Indore = (22.7151, 75.865)
    Vadodara = (22.31, 73.18)
    Bhopal = (23.25, 77.41)
    Coimbatore = (11.0, 76.95)
    Ludhiana = (30.9278, 75.8723)
    Agra = (27.1704, 78.015)
    Kalyan = (19.2502, 73.1602)
    Vishakhapatnam = (17.73, 83.305)
    Kochi = (10.015, 76.2239)
    Nasik = (20.0004, 73.78)
    Meerut = (29.0004, 77.7)
    Faridabad = (28.4333, 77.3167)
    Varanasi = (25.33, 83.0)
    Ghaziabad = (28.6604, 77.4084)
    Asansol = (23.6833, 86.9833)
    Jamshedpur = (22.7875, 86.1975)
    Madura = (9.92, 78.12)
    Jabalpur = (23.1751, 79.9551)
    Rajkot = (22.31, 70.8)
    Dhanbad = (23.8004, 86.42)
    Amritsar = (31.64, 74.87)
    Warangal = (18.01, 79.58)
    Allahabad = (25.455, 81.84)
    Srinagar = (34.1, 74.815)
    Bezwada = (16.52, 80.63)
    Aurangabad = (19.8957, 75.3203)
    Bhilai = (21.2167, 81.4333)
    Solapur = (17.6704, 75.9)
    Ranchi = (23.37, 85.33)
    NewDelhi = (28.6, 77.2)
    Jodhpur = (26.2918, 73.0168)
    Guwahati = (26.16, 91.77)
    Chandigarh = (30.72, 76.78)
    Gwalior = (26.23, 78.1801)
    Thiruvananthapuram = (8.5, 76.95)
    Calicut = (11.2504, 75.77)
    Trichinopoly = (10.81, 78.69)
    Hubli = (15.36, 75.125)
    Mysore = (12.31, 76.66)
    Raipur = (21.235, 81.635)
    Salem = (11.67, 78.1801)
    Jalandhar = (31.3349, 75.569)
    Bhubaneshwar = (20.2704, 85.8274)
    Kota = (25.18, 75.835)
    Jhansi = (25.453, 78.5575)
    Bareilly = (28.3454, 79.42)
    Aligarh = (27.8922, 78.0618)
    Bhiwandi = (19.35, 73.13)
    Jammu = (32.7118, 74.8467)
    Moradabad = (28.8418, 78.7568)
    Mangalore = (12.9, 74.85)
    Kolhapur = (16.7, 74.22)
    Amravati = (20.95, 77.77)
    DehraDun = (30.3204, 78.05)
    Malegaon = (20.5604, 74.525)
    Nellore = (14.44, 79.9899)
    Gorakhpur = (26.7504, 83.38)
    Shimoga = (13.9304, 75.56)
    Tiruppur = (11.0804, 77.33)
    Raurkela = (22.2304, 84.83)
    Nanded = (19.17, 77.3)
    Belgaum = (15.865, 74.505)
    Sangli = (16.8604, 74.575)
    Chanda = (19.97, 79.3)
    Ajmer = (26.45, 74.64)
    Cuttack = (20.47, 85.8899)
    Bikaner = (28.0304, 73.3299)
    Bhavnagar = (21.7784, 72.13)
    Hisar = (29.17, 75.725)
    Bilaspur = (22.0904, 82.16)
    Tinnevelly = (8.7304, 77.69)


class Brazil(CountryBase):
    SaoPaulo = (-23.5587, -46.625)
    RiodeJaneiro = (-22.925, -43.225)
    BeloHorizonte = (-19.915, -43.915)
    PortoAlegre = (-30.05, -51.2)
    Brasilia = (-15.7833, -47.9161)
    Recife = (-8.0756, -34.9156)
    Fortaleza = (-3.75, -38.58)
    Salvador = (-12.97, -38.48)
    Curitiba = (-25.42, -49.32)
    Campinas = (-22.9, -47.1)
    Belem = (-1.45, -48.48)
    Goiania = (-16.72, -49.3)
    Manaus = (-3.1, -60.0)
    Santos = (-23.9537, -46.3329)
    Vitoria = (-20.324, -40.366)
    Niteroi = (-22.9, -43.1)
    VilaVelha = (-20.3676, -40.318)
    Maceio = (-9.62, -35.73)
    Natal = (-5.78, -35.24)
    SaoLuis = (-2.516, -44.266)
    Florianopolis = (-27.58, -48.52)
    Joinvile = (-26.32, -48.8399)
    JoaoPessoa = (-7.1011, -34.8761)
    Olinda = (-8.0, -34.85)
    Teresina = (-5.095, -42.78)
    NovoHamburgo = (-29.7096, -51.14)
    Iguacu = (-22.74, -43.47)
    Cuiaba = (-15.5696, -56.085)
    CampoGrande = (-20.45, -54.6166)
    SaoJosedosCampos = (-23.2, -45.8799)
    Jaboatao = (-8.11, -35.02)
    Aracaju = (-10.9, -37.12)
    SaoJosedosPinhais = (-25.57, -49.18)
    SantoAndre = (-23.6528, -46.5278)
    Canoas = (-29.92, -51.18)
    Uberlandia = (-18.9, -48.28)
    Sorocaba = (-23.49, -47.47)
    RibeiraoPreto = (-21.17, -47.83)


class China(CountryBase):
    Shanghai = (31.2165, 121.4365)
    Beijing = (39.9289, 116.3883)
    Guangzhou = (23.145, 113.325)
    Shenzhen = (22.5524, 114.1221)
    Wuhan = (30.58, 114.27)
    Tianjin = (39.13, 117.2)
    Chongqing = (29.565, 106.595)
    Shenyang = (41.805, 123.45)
    Dongguan = (23.0489, 113.7447)
    Chengdu = (30.67, 104.07)
    Xian = (34.275, 108.895)
    Hechi = (23.0965, 109.6091)
    Nanjing = (32.05, 118.78)
    Guiyang = (26.58, 106.72)
    Harbin = (45.75, 126.65)
    Zhangzhou = (24.5204, 117.67)
    Changchun = (43.865, 125.34)
    Dalian = (38.9228, 121.6298)
    Zibo = (36.8, 118.05)
    Hangzhou = (30.25, 120.17)
    Kunming = (25.07, 102.68)
    Taiyuan = (37.875, 112.5451)
    Qingdao = (36.09, 120.33)
    Jinan = (36.675, 116.995)
    Zhengzhou = (34.755, 113.6651)
    Fuzhou = (26.08, 119.3)
    Changsha = (28.2, 112.97)
    Xiangtan = (27.8504, 112.9)
    Lanzhou = (36.056, 103.792)
    Xiamen = (24.45, 118.08)
    Lianshan = (40.7503, 120.83)
    Shijiazhuang = (38.05, 114.48)
    Jilin = (43.85, 126.55)
    Nanchang = (28.68, 115.88)
    Wenzhou = (28.02, 120.6501)
    Gaoping = (30.7804, 106.13)
    Nanning = (22.82, 108.32)
    Urumqi = (43.805, 87.575)
    Zaozhuang = (34.88, 117.57)
    Yantai = (37.5304, 121.4)
    Tongshan = (34.28, 117.18)
    Linyi = (35.08, 118.33)
    Haikou = (20.05, 110.32)
    Baotou = (40.6522, 109.822)
    Hefei = (31.85, 117.28)
    Suzhou = (33.6361, 116.9789)
    Nanyang = (33.0004, 112.53)
    Ningbo = (29.88, 121.55)
    Tangshan = (39.6243, 118.1944)
    Xiping = (40.08, 113.3)
    Shuyangzha = (34.1299, 118.7734)
    Shangqiu = (34.4504, 115.65)
    Wuxi = (31.58, 120.3)
    Hohhot = (40.82, 111.66)
    Luoyang = (34.68, 112.4701)
    Jingling = (30.6501, 113.16)
    Daqing = (46.58, 125.0)
    Luan = (31.7503, 116.48)
    Sanzhou = (30.82, 108.4)
    Qiqihar = (47.345, 123.99)
    Anshan = (41.115, 122.94)
    Handan = (36.58, 114.48)
    Taian = (36.2, 117.1201)
    Shantou = (23.37, 116.67)
    Zhanjiang = (21.2, 110.38)
    Xiantao = (30.3704, 113.44)
    Weifang = (36.7204, 119.1001)
    Xinyang = (32.1304, 114.07)
    Luzhou = (28.88, 105.38)
    Ganzhou = (25.92, 114.95)
    Liuzhou = (24.28, 109.25)
    Fushun = (41.8654, 123.87)
    Changde = (29.03, 111.68)
    Neijiang = (29.5804, 105.05)
    Quanzhou = (24.9, 118.58)
    Huainan = (32.63, 116.98)
    Suining = (30.5333, 105.5333)
    Mianyang = (31.47, 104.77)
    Maanshan = (31.7304, 118.48)
    Yiyang = (28.6004, 112.33)
    Heze = (35.23, 115.45)
    Changzhou = (31.78, 119.97)
    Chifeng = (42.27, 118.95)
    Huaiyin = (33.58, 119.03)
    Mudanjiang = (44.575, 129.59)
    Huzhou = (30.8704, 120.1)
    Beidao = (34.6, 105.92)
    Shuangshui = (26.5944, 104.8333)
    Gaozhou = (21.9204, 110.87)
    Jining = (35.4004, 116.55)
    Leshan = (29.5671, 103.7333)
    Shangrao = (28.4704, 117.97)
    Yulin = (22.63, 110.15)
    Xianyang = (34.3456, 108.7147)
    Baoding = (38.8704, 115.48)
    Zigong = (29.4, 104.78)
    Ankang = (32.68, 109.02)
    Jinhua = (29.12, 119.65)
    Zhuzhou = (27.83, 113.15)
    Xiangyang = (32.02, 112.13)
    Mizhou = (35.99, 119.3801)
    Xining = (36.62, 101.77)
    Zhangjiakou = (40.83, 114.93)
    Zhuhai = (22.2769, 113.5678)
    Jiamusi = (46.83, 130.35)
    Hengyang = (26.88, 112.59)
    Benxi = (41.3304, 123.75)
    Qinhuangdao = (39.9304, 119.62)
    Yongzhou = (26.2304, 111.62)
    Baoshan = (25.12, 99.15)
    Yinchuan = (38.468, 106.273)
    Jiaxing = (30.7704, 120.75)
    Guilin = (25.28, 110.28)
    Yichun = (27.8333, 114.4)
    Yangquan = (37.87, 113.57)
    Jixi = (45.3, 130.97)
    Xinan = (34.38, 118.35)
    Pingxiang = (27.62, 113.85)
    Jinzhou = (41.1204, 121.1)
    Nantong = (32.0304, 120.825)
    Foshan = (23.0301, 113.12)
    Huaibei = (33.9504, 116.75)
    Xinyu = (27.8, 114.93)
    Nangandao = (35.3204, 113.87)
    Yibin = (28.77, 104.57)
    Bengbu = (32.95, 117.33)
    Dengtalu = (36.08, 114.35)
    Tongliao = (43.62, 122.27)
    Xiaoxita = (30.7, 111.28)
    Yangjiang = (21.8504, 111.97)
    KaifengChengguanzhen = (34.85, 114.35)
    Dandong = (40.1436, 124.3936)
    Xuanzhou = (30.9525, 118.7553)
    Rizhao = (35.4304, 119.45)
    Jiaozuo = (35.25, 113.22)
    Zhenjiang = (32.22, 119.43)
    Pingdingshan = (33.7304, 113.3)
    Zunyi = (27.7, 106.92)
    Anshun = (26.2504, 105.93)
    Yuci = (37.6804, 112.73)
    Yancheng = (33.3856, 120.1253)
    Linfen = (36.0803, 111.52)
    Rongjiawan = (29.3801, 113.1)
    Xingyi = (25.0904, 104.89)
    Wuhu = (31.3504, 118.37)
    Langfang = (39.5204, 116.68)
    Zhaotong = (27.3204, 103.72)
    Lingyuan = (41.24, 119.4011)
    Baojishi = (34.38, 107.15)
    Yingkou = (40.6703, 122.28)
    Liaoyang = (41.28, 123.18)
    Shaoxing = (30.0004, 120.57)
    Fuyang = (30.0533, 119.9519)
    Fuxin = (42.0105, 121.66)
    Shiyan = (32.57, 110.78)
    Jincheng = (35.5004, 112.83)
    Hegang = (47.4, 130.37)
    Beihai = (21.4804, 109.1)
    Shaoguan = (24.8, 113.58)
    Xinpu = (34.6004, 119.17)
    Qingyuan = (23.7004, 113.0301)
    Changzhi = (36.1839, 113.1053)
    Huangshi = (30.22, 115.1)
    PuyangChengguanzhen = (35.7004, 114.98)
    Zhuozhou = (39.5401, 115.79)
    Changping = (40.2248, 116.1944)
    Taizhou = (32.4904, 119.9)
    Xingtai = (37.05, 114.5)
    Anqing = (30.5, 117.05)
    Shihezi = (44.3, 86.0299)
    Shuozhou = (39.3004, 112.42)
    Wusong = (30.9504, 117.78)
    Weihai = (37.5, 122.1)
    Siping = (43.17, 124.33)
    Jiujiang = (29.73, 115.98)
    Kashgar = (39.4763, 75.9699)
    Yangzhou = (32.4, 119.43)


class Bangladesh(CountryBase):
    Dhaka = (23.7231, 90.4086)
    Chittagong = (22.33, 91.8)
    Khulna = (22.84, 89.56)
    Rajshahi = (24.375, 88.605)


class Argentina(CountryBase):
    BuenosAires = (-34.6025, -58.3975)
    Cordoba = (-31.4, -64.1823)
    Rosario = (-32.9511, -60.6663)
    Mendoza = (-32.8833, -68.8166)
    SanMigueldeTucuman = (-26.816, -65.2166)
    LaPlata = (-34.9096, -57.96)
    MardelPlata = (-38.0, -57.58)


class Pakistan(CountryBase):
    Karachi = (24.87, 66.99)
    Lahore = (31.56, 74.35)
    Faisalabad = (31.41, 73.11)
    SaiduSharif = (34.75, 72.35)
    Rawalpindi = (33.6, 73.04)
    Multan = (30.2, 71.455)
    Gujranwala = (32.1604, 74.185)
    HyderabadCity = (25.38, 68.375)
    Peshawar = (34.005, 71.535)
    Abbottabad = (34.1495, 73.1995)
    Islamabad = (33.7, 73.1666)
    Quetta = (30.22, 67.025)
    Bannu = (32.989, 70.5986)
    Bahawalpur = (29.39, 71.675)
    Sargodha = (32.0854, 72.675)


class Egypt(CountryBase):
    Cairo = (30.05, 31.25)
    Alexandria = (31.2, 29.95)
    Giza = (30.01, 31.19)
    Ismailia = (30.5903, 32.26)
    PortSaid = (31.26, 32.29)
    Luxor = (25.7, 32.65)
    Suhaj = (26.5504, 31.7)
    AlMansurah = (31.0504, 31.38)


class Philippines(CountryBase):
    Manila = (14.6042, 120.9822)
    QuezonCity = (14.6504, 121.03)
    Davao = (7.11, 125.63)
    CagayandeOro = (8.4508, 124.6853)
    GeneralSantos = (6.1108, 125.1747)
    Bacolod = (10.6317, 122.9817)
    CebuCity = (10.32, 123.9001)
    ZamboangaCity = (6.92, 122.08)
    NagaCity = (13.6192, 123.1814)


class Russia(CountryBase):
    Moscow = (55.7522, 37.6155)
    SaintPetersburg = (59.939, 30.316)
    Novosibirsk = (55.03, 82.96)
    Yekaterinburg = (56.85, 60.6)
    NizhniyNovgorod = (56.333, 44.0001)
    Samara = (53.195, 50.1513)
    Omsk = (54.99, 73.4)
    Kazan = (55.7499, 49.1263)
    Chelyabinsk = (55.155, 61.4387)
    RostovnaDonu = (47.2346, 39.7127)
    Ufa = (54.79, 56.04)
    Perm = (58.0, 56.25)
    Volgograd = (48.71, 44.5)
    Krasnoyarsk = (56.014, 92.866)
    Voronezh = (51.73, 39.27)
    Saratov = (51.58, 46.03)
    Tolyatti = (53.4804, 49.53)
    Krasnodar = (45.02, 39.0)
    Ulyanovsk = (54.33, 48.41)
    Izhevsk = (56.85, 53.23)
    Yaroslavl = (57.62, 39.87)
    Barnaul = (53.355, 83.745)
    Vladivostok = (43.13, 131.91)
    Irkutsk = (52.32, 104.245)
    Khabarovsk = (48.455, 135.12)
    Makhachkala = (42.98, 47.5)
    Orenburg = (51.78, 55.11)
    Novokuznetsk = (53.75, 87.115)


class Turkey(CountryBase):
    Istanbul = (41.105, 29.01)
    Ankara = (39.9272, 32.8644)
    Izmir = (38.4361, 27.1518)
    Bursa = (40.2, 29.07)
    Adana = (36.995, 35.32)
    Gaziantep = (37.075, 37.385)
    Konya = (37.875, 32.475)
    Tarsus = (36.9204, 34.88)
    Antalya = (36.89, 30.7)
    Trabzon = (40.98, 39.72)
    Diyarbakir = (37.9204, 40.23)
    Samsun = (41.28, 36.3437)
    Kayseri = (38.735, 35.49)


class France(CountryBase):
    Paris = (48.8667, 2.3333)
    Lyon = (45.77, 4.83)
    Marseille = (43.29, 5.375)
    Lille = (50.65, 3.08)
    Nice = (43.715, 7.265)
    Toulouse = (43.62, 1.4499)
    Bordeaux = (44.85, -0.595)


class KoreaSouth(CountryBase):
    Seoul = (37.5663, 126.9997)
    Busan = (35.0951, 129.01)
    Incheon = (37.4761, 126.6422)
    Daegu = (35.8668, 128.607)
    Daejeon = (36.3355, 127.425)
    Gwangju = (35.171, 126.9104)
    Changwon = (35.2191, 128.5836)
    Suwon = (37.2578, 127.0109)
    Ulsan = (35.5467, 129.317)
    Songnam = (37.4386, 127.1378)
    Goyang = (37.6527, 126.8372)
    Bucheon = (37.4989, 126.7831)
    Cheongju = (36.6439, 127.5012)
    Ansan = (37.3481, 126.8595)
    Jeonju = (35.8314, 127.1404)


class Nigeria(CountryBase):
    Lagos = (6.4433, 3.3915)
    Kano = (12.0, 8.52)
    Ibadan = (7.38, 3.93)
    Abuja = (9.0833, 7.5333)
    Kaduna = (10.52, 7.44)
    BeninCity = (6.3405, 5.62)
    Ikare = (7.5304, 5.76)
    PortHarcourt = (4.81, 7.01)
    Ogbomoso = (8.13, 4.24)
    Aba = (5.1004, 7.35)
    Maiduguri = (11.85, 13.16)
    Zaria = (11.08, 7.71)
    Warri = (5.52, 5.76)
    Jos = (9.93, 8.89)
    Ilorin = (8.49, 4.55)
    Oyo = (7.8504, 3.93)
    Sokoto = (13.06, 5.24)
    Enugu = (6.45, 7.5)
    Abeokuta = (7.1604, 3.35)
    Uyo = (5.008, 7.85)


class Indonesia(CountryBase):
    Jakarta = (-6.1744, 106.8294)
    Surabaya = (-7.2492, 112.7508)
    Bandung = (-6.95, 107.57)
    Bekasi = (-6.2173, 106.9723)
    Medan = (3.58, 98.65)
    Palembang = (-2.98, 104.75)
    Semarang = (-6.9666, 110.42)
    Makassar = (-5.14, 119.432)
    Cilacap = (-7.7188, 109.0154)
    Bogor = (-6.57, 106.75)
    BandarLampung = (-5.43, 105.27)
    Padang = (-0.96, 100.36)
    Malang = (-7.98, 112.61)
    Pekanbaru = (0.565, 101.425)
    Denpasar = (-8.65, 115.22)
    Yogyakarta = (-7.78, 110.375)
    Palu = (-0.907, 119.833)
    Pontianak = (-0.03, 109.32)
    Banjarmasin = (-3.33, 114.5801)
    Samarinda = (-0.5, 117.15)
    Binjai = (3.6204, 98.5001)
    Surakarta = (-7.565, 110.825)


class UnitedKingdom(CountryBase):
    London = (51.5, -0.1167)
    Birmingham = (52.475, -1.92)
    Manchester = (53.5004, -2.248)
    Leeds = (53.83, -1.58)
    Sheffield = (53.3667, -1.5)
    Glasgow = (55.8744, -4.2507)
    NewcastleuponTyne = (55.0004, -1.6)
    Caerdydd = (51.5, -3.225)
    Nottingham = (52.9703, -1.17)
    Liverpool = (53.416, -2.918)
    SouthendonSea = (51.55, 0.72)
    Bristol = (51.45, -2.5833)


class Peru(CountryBase):
    Lima = (-12.048, -77.0501)
    Callao = (-12.07, -77.135)
    Arequipa = (-16.42, -71.53)
    Trujillo = (-8.12, -79.02)
    Chiclayo = (-6.7629, -79.8366)


class Iran(CountryBase):
    Tehran = (35.6719, 51.4243)
    Mashhad = (36.27, 59.57)
    Esfahan = (32.7, 51.7)
    Karaj = (35.8004, 50.97)
    Tabriz = (38.0863, 46.3012)
    Shiraz = (29.63, 52.57)
    Ahvaz = (31.28, 48.72)
    Qom = (34.65, 50.95)
    Kermanshah = (34.38, 47.06)
    Zahedan = (29.5, 60.83)
    Rasht = (37.3, 49.63)
    Kerman = (30.3, 57.08)
    Orumiyeh = (37.53, 45.0)


class CongoKinshasa(CountryBase):
    Kinshasa = (-4.3297, 15.315)
    Lubumbashi = (-11.68, 27.48)
    MbujiMayi = (-6.15, 23.6)
    Kananga = (-5.89, 22.4)
    Kikwit = (-5.03, 18.85)
    Kisangani = (0.52, 25.22)


class Colombia(CountryBase):
    Bogota = (4.5964, -74.0833)
    Medellin = (6.275, -75.575)
    Cali = (3.4, -76.5)
    Barranquilla = (10.96, -74.8)
    Bucaramanga = (7.1301, -73.1259)
    Cartagena = (10.3997, -75.5144)
    Cucuta = (7.92, -72.52)
    Soledad = (10.92, -74.77)
    Pereira = (4.8104, -75.68)


class HongKong(CountryBase):
    HongKong = (22.305, 114.185)


class Taiwan(CountryBase):
    Taipei = (25.0358, 121.5683)
    Kaohsiung = (22.6333, 120.2666)
    Taichung = (24.1521, 120.6817)
    Tainan = (23.0, 120.2)
    Zhongli = (24.965, 121.2168)
    Hsinchu = (24.8168, 120.9767)
    Changhua = (24.0734, 120.5134)


class Thailand(CountryBase):
    Bangkok = (13.75, 100.5166)


class Chile(CountryBase):
    Santiago = (-33.45, -70.667)
    Concepcion = (-36.83, -73.05)
    Valparaiso = (-33.0478, -71.621)


class Spain(CountryBase):
    Madrid = (40.4, -3.6834)
    Barcelona = (41.3833, 2.1834)
    Sevilla = (37.405, -5.98)
    Bilbao = (43.25, -2.93)
    Valencia = (39.485, -0.4)
    Zaragoza = (41.65, -0.89)
    Malaga = (36.7204, -4.42)


class Vietnam(CountryBase):
    HoChiMinhCity = (10.78, 106.695)
    Hanoi = (21.0333, 105.85)
    Haiphong = (20.83, 106.6801)
    CanTho = (10.05, 105.77)
    QuangHa = (16.06, 108.25)
    Hue = (16.47, 107.58)
    QuyNhon = (13.78, 109.18)
    BienHoa = (10.97, 106.8301)
    Vinh = (18.7, 105.68)


class Canada(CountryBase):
    Toronto = (43.7, -79.42)
    Montreal = (45.5, -73.5833)
    Vancouver = (49.2734, -123.1216)
    Ottawa = (45.4167, -75.7)
    Calgary = (51.083, -114.08)
    Edmonton = (53.55, -113.5)
    Hamilton = (43.25, -79.83)
    Winnipeg = (49.883, -97.166)
    Quebec = (46.84, -71.2456)


class Singapore(CountryBase):
    Singapore = (1.293, 103.8558)


class Angola(CountryBase):
    Luanda = (-8.8383, 13.2344)
    Huambo = (-12.75, 15.76)


class Iraq(CountryBase):
    Baghdad = (33.3386, 44.3939)
    Mosul = (36.345, 43.145)
    Dahuk = (36.8667, 43.0)
    Erbil = (36.179, 44.0086)
    AlBasrah = (30.5135, 47.8136)
    AsSulaymaniyah = (35.5613, 45.4309)
    AnNajaf = (32.0003, 44.3354)
    Kirkuk = (35.4722, 44.3923)
    AlHillah = (32.4721, 44.4217)


class Sudan(CountryBase):
    Khartoum = (15.5881, 32.5342)
    Omdurman = (15.6167, 32.48)


class Australia(CountryBase):
    Sydney = (-33.92, 151.1852)
    Melbourne = (-37.82, 144.975)
    Brisbane = (-27.455, 153.0351)
    Perth = (-31.955, 115.84)
    Adelaide = (-34.935, 138.6)
    Newcastle = (-32.8453, 151.815)
    Canberra = (-35.283, 149.129)


class SaudiArabia(CountryBase):
    Riyadh = (24.6408, 46.7727)
    Jeddah = (21.5169, 39.2192)
    AdDammam = (26.4282, 50.0997)
    Mecca = (21.43, 39.82)
    Medina = (24.5, 39.58)
    AtTaif = (21.2622, 40.3823)
    AlHufuf = (25.3487, 49.5856)
    AlHillah = (23.4895, 46.7564)
    Tabuk = (28.3838, 36.555)


class Burma(CountryBase):
    Rangoon = (16.7834, 96.1667)
    Mandalay = (21.97, 96.085)
    NayPyiTaw = (19.7666, 96.1186)


class CoteDIvoire(CountryBase):
    Abidjan = (5.32, -4.04)
    Yamoussoukro = (6.8184, -5.2755)
    Bouake = (7.69, -5.03)


class SouthAfrica(CountryBase):
    Johannesburg = (-26.17, 28.03)
    CapeTown = (-33.92, 18.435)
    Benoni = (-26.1496, 28.3299)
    Durban = (-29.865, 30.98)
    Pretoria = (-25.7069, 28.2294)
    Vereeniging = (-26.6496, 27.96)
    PortElizabeth = (-33.97, 25.6)
    Bloemfontein = (-29.12, 26.2299)
    Pietermaritzburg = (-29.61, 30.39)


class Germany(CountryBase):
    Berlin = (52.5218, 13.4015)
    Stuttgart = (48.78, 9.2)
    Frankfurt = (50.1, 8.675)
    Mannheim = (49.5004, 8.47)
    Hamburg = (53.55, 10.0)
    Essen = (51.45, 7.0166)
    Duisburg = (51.43, 6.75)
    Munich = (48.1299, 11.575)
    Dusseldorf = (51.2204, 6.78)
    Cologne = (50.93, 6.95)
    Wuppertal = (51.25, 7.17)
    Saarbrucken = (49.2504, 6.97)
    Nuremberg = (49.45, 11.08)
    Bremen = (53.08, 8.8)
    Hannover = (52.367, 9.7167)
    Bonn = (50.7205, 7.08)
    Dresden = (51.05, 13.75)
    Wiesbaden = (50.0804, 8.25)
    Dortmund = (51.53, 7.45)
    Leipzig = (51.3354, 12.41)


class Algeria(CountryBase):
    Algiers = (36.7631, 3.0506)
    Oran = (35.71, -0.62)
    Constantine = (36.36, 6.5999)


class Italy(CountryBase):
    Rome = (41.896, 12.4833)
    Milan = (45.47, 9.205)
    Naples = (40.84, 14.245)
    Turin = (45.0704, 7.67)
    Florence = (43.78, 11.25)
    Salerno = (40.6804, 14.7699)
    Palermo = (38.125, 13.35)
    Catania = (37.5, 15.08)
    Genoa = (44.41, 8.93)


class KoreaNorth(CountryBase):
    Pyongyang = (39.0194, 125.7547)
    Nampo = (38.7669, 125.4524)
    Hamhung = (39.9101, 127.5454)
    Hungnam = (39.8231, 127.6232)
    Chongjin = (41.7846, 129.79)


class Afghanistan(CountryBase):
    Kabul = (34.5167, 69.1833)
    Kandahar = (31.61, 65.6949)
    Jalalabad = (34.4415, 70.4361)


class Greece(CountryBase):
    Athens = (37.9833, 23.7333)
    Thessaloniki = (40.6961, 22.885)


class Morocco(CountryBase):
    Casablanca = (33.6, -7.6164)
    Rabat = (34.0253, -6.8361)
    Fes = (34.0546, -5.0004)
    Marrakech = (31.63, -8.0)
    Agadir = (30.44, -9.62)
    Tangier = (35.7473, -5.8327)
    Meknes = (33.9004, -5.56)
    Kenitra = (34.2704, -6.58)


class Israel(CountryBase):
    TelAvivYafo = (32.08, 34.77)
    Jerusalem = (31.7784, 35.2066)
    Haifa = (32.8204, 34.98)


class Ethiopia(CountryBase):
    AddisAbaba = (9.0333, 38.7)


class Kenya(CountryBase):
    Nairobi = (-1.2833, 36.8167)
    Mombasa = (-4.04, 39.6899)


class Venezuela(CountryBase):
    Caracas = (10.501, -66.917)
    Maracaibo = (10.73, -71.66)
    Valencia = (10.23, -67.98)
    Barquisimeto = (10.05, -69.3)
    Maracay = (10.2469, -67.5958)
    CiudadGuayana = (8.37, -62.62)
    Barcelona = (10.1304, -64.72)
    PuertoLaCruz = (10.17, -64.68)


class Tanzania(CountryBase):
    DaresSalaam = (-6.8, 39.2683)
    Dodoma = (-6.1833, 35.75)
    Moshi = (-3.3396, 37.34)


class Portugal(CountryBase):
    Lisbon = (38.7227, -9.1449)
    Porto = (41.15, -8.62)
    Braga = (41.555, -8.4213)


class Poland(CountryBase):
    Katowice = (50.2604, 19.02)
    Warsaw = (52.25, 21.0)
    Lodz = (51.775, 19.4514)
    Krakow = (50.06, 19.96)
    Gdansk = (54.36, 18.64)
    Bytom = (50.35, 18.91)
    Wroclaw = (51.1104, 17.03)
    Poznan = (52.4058, 16.8999)


class Syria(CountryBase):
    Aleppo = (36.23, 37.17)
    Damascus = (33.5, 36.3)
    Homs = (34.73, 36.72)
    Latakia = (35.54, 35.78)


class Ukraine(CountryBase):
    Kyiv = (50.4334, 30.5166)
    Kharkiv = (50.0, 36.25)
    Dnipro = (48.48, 35.0)
    Odesa = (46.49, 30.71)
    Donetsk = (48.0, 37.83)
    Lviv = (49.835, 24.03)
    Zaporizhzhya = (47.8573, 35.1768)
    KryvyyRih = (47.9283, 33.345)


class Senegal(CountryBase):
    Dakar = (14.7158, -17.4731)


class Ecuador(CountryBase):
    Guayaquil = (-2.22, -79.92)
    Quito = (-0.215, -78.5001)


class Malaysia(CountryBase):
    GeorgeTown = (5.4136, 100.3294)
    KualaLumpur = (3.1667, 101.7)
    Klang = (3.0204, 101.55)
    JohorBahru = (1.48, 103.73)
    Butterworth = (5.4171, 100.4)
    Melaka = (2.2064, 102.2465)
    Ipoh = (4.6, 101.065)
    Kuching = (1.53, 110.33)


class Tunisia(CountryBase):
    Tunis = (36.8028, 10.1797)


class Austria(CountryBase):
    Vienna = (48.2, 16.3666)


class Libya(CountryBase):
    Tripoli = (32.8925, 13.18)
    Benghazi = (32.1167, 20.0667)


class Uzbekistan(CountryBase):
    Tashkent = (41.3117, 69.2949)
    Fargona = (40.39, 71.78)
    Namangan = (41.0, 71.67)
    Samarkand = (39.67, 66.945)
    Andijon = (40.79, 72.34)


class Cuba(CountryBase):
    Havana = (23.132, -82.3642)
    SantiagodeCuba = (20.025, -75.8213)


class DominicanRepublic(CountryBase):
    SantoDomingo = (18.4701, -69.9001)
    Santiago = (19.5, -70.67)


class Azerbaijan(CountryBase):
    Baku = (40.3953, 49.8622)


class Ghana(CountryBase):
    Accra = (5.55, -0.2167)
    Kumasi = (6.69, -1.63)


class Bolivia(CountryBase):
    SantaCruz = (-17.7539, -63.226)
    LaPaz = (-16.498, -68.15)
    Sucre = (-19.041, -65.2595)
    Cochabamba = (-17.41, -66.17)


class Kuwait(CountryBase):
    KuwaitCity = (29.3697, 47.9783)


class Yemen(CountryBase):
    Sanaa = (15.3547, 44.2066)
    Aden = (12.7797, 45.0095)
    AlHudaydah = (14.7979, 42.953)
    Taizz = (13.6045, 44.0394)


class Haiti(CountryBase):
    PortauPrince = (18.541, -72.336)


class Romania(CountryBase):
    Bucharest = (44.4334, 26.0999)


class Cameroon(CountryBase):
    Douala = (4.0604, 9.71)
    Yaounde = (3.8667, 11.5167)


class Paraguay(CountryBase):
    Asuncion = (-25.2964, -57.6415)


class Lebanon(CountryBase):
    Beirut = (33.872, 35.5097)


class Belarus(CountryBase):
    Minsk = (53.9, 27.5666)


class Belgium(CountryBase):
    Brussels = (50.8333, 4.3333)
    Antwerp = (51.2204, 4.415)
    Liege = (50.63, 5.58)


class Madagascar(CountryBase):
    Antananarivo = (-18.9166, 47.5166)


class Hungary(CountryBase):
    Budapest = (47.5, 19.0833)


class Zimbabwe(CountryBase):
    Harare = (-17.8178, 31.0447)
    Bulawayo = (-20.17, 28.58)


class Uruguay(CountryBase):
    Montevideo = (-34.858, -56.1711)


class Mali(CountryBase):
    Bamako = (12.65, -8.0)


class Guinea(CountryBase):
    Conakry = (9.5315, -13.6802)


class Cambodia(CountryBase):
    PhnomPenh = (11.55, 104.9166)


class Togo(CountryBase):
    Lome = (6.1319, 1.2228)


class Qatar(CountryBase):
    Doha = (25.2866, 51.533)


class Mozambique(CountryBase):
    Maputo = (-25.9553, 32.5892)
    Matola = (-25.9696, 32.46)


class ElSalvador(CountryBase):
    SanSalvador = (13.71, -89.203)


class Uganda(CountryBase):
    Kampala = (0.3167, 32.5833)


class Netherlands(CountryBase):
    TheHague = (52.08, 4.27)
    Amsterdam = (52.35, 4.9166)
    Rotterdam = (51.92, 4.48)
    Utrecht = (52.1003, 5.12)


class UnitedArabEmirates(CountryBase):
    Dubai = (25.23, 55.28)
    Sharjah = (25.3714, 55.4065)
    AbuDhabi = (24.4667, 54.3666)


class NewZealand(CountryBase):
    Auckland = (-36.8481, 174.763)
    Wellington = (-41.3, 174.7833)


class CongoBrazzaville(CountryBase):
    Brazzaville = (-4.2592, 15.2847)
    PointeNoire = (-4.77, 11.88)


class Zambia(CountryBase):
    Lusaka = (-15.4166, 28.2833)


class CostaRica(CountryBase):
    SanJose = (9.935, -84.0841)


class Panama(CountryBase):
    PanamaCity = (8.968, -79.533)


class Sweden(CountryBase):
    Stockholm = (59.3508, 18.0973)
    Goteborg = (57.75, 12.0)


class Switzerland(CountryBase):
    Geneva = (46.21, 6.14)
    Zurich = (47.38, 8.55)
    Bern = (46.9167, 7.467)
    Basel = (47.5804, 7.59)


class Kazakhstan(CountryBase):
    Almaty = (43.325, 76.915)
    NurSultan = (51.1811, 71.4278)


class Bulgaria(CountryBase):
    Sofia = (42.6833, 23.3167)


class Czechia(CountryBase):
    Prague = (50.0833, 14.466)


class BurkinaFaso(CountryBase):
    Ouagadougou = (12.3703, -1.5247)


class Finland(CountryBase):
    Helsinki = (60.1756, 24.9341)


class Armenia(CountryBase):
    Yerevan = (40.1812, 44.5136)


class Somalia(CountryBase):
    Mogadishu = (2.0667, 45.3667)


class Georgia(CountryBase):
    Tbilisi = (41.725, 44.7908)


class Serbia(CountryBase):
    Belgrade = (44.8186, 20.468)


class Tajikistan(CountryBase):
    Dushanbe = (38.56, 68.7739)


class Denmark(CountryBase):
    Copenhagen = (55.6786, 12.5635)


class Jordan(CountryBase):
    Amman = (31.95, 35.9333)
    AzZarqa = (32.07, 36.1)
    Irbid = (32.55, 35.85)


class Ireland(CountryBase):
    Dublin = (53.3331, -6.2489)


class Liberia(CountryBase):
    Monrovia = (6.3106, -10.8048)


class Guatemala(CountryBase):
    GuatemalaCity = (14.6211, -90.527)
    Quetzaltenango = (14.83, -91.52)


class Chad(CountryBase):
    NDjamena = (12.1131, 15.0491)


class Honduras(CountryBase):
    Tegucigalpa = (14.102, -87.2175)
    SanPedroSula = (15.5, -88.03)


class Jamaica(CountryBase):
    Kingston = (17.9771, -76.7674)


class Djibouti(CountryBase):
    Djibouti = (11.595, 43.148)


class Nicaragua(CountryBase):
    Managua = (12.153, -86.2685)


class Niger(CountryBase):
    Niamey = (13.5167, 2.1167)


class Albania(CountryBase):
    Tirana = (41.3275, 19.8189)


class Nepal(CountryBase):
    Kathmandu = (27.7167, 85.3166)


class Mongolia(CountryBase):
    Ulaanbaatar = (47.9167, 106.9166)


class Rwanda(CountryBase):
    Kigali = (-1.9536, 30.0605)


class Kyrgyzstan(CountryBase):
    Bishkek = (42.8731, 74.5852)


class Norway(CountryBase):
    Oslo = (59.9167, 10.75)


class CentralAfricanRepublic(CountryBase):
    Bangui = (4.3666, 18.5583)


class SierraLeone(CountryBase):
    Freetown = (8.47, -13.2342)


class Benin(CountryBase):
    Cotonou = (6.4, 2.52)
    PortoNovo = (6.4833, 2.6166)


class Laos(CountryBase):
    Vientiane = (17.9667, 102.6)


class Latvia(CountryBase):
    Riga = (56.95, 24.1)


class Mauritania(CountryBase):
    Nouakchott = (18.0864, -15.9753)


class Oman(CountryBase):
    Muscat = (23.6133, 58.5933)


class Turkmenistan(CountryBase):
    Ashgabat = (37.95, 58.3833)


class Croatia(CountryBase):
    Zagreb = (45.8, 16.0)


class BosniaAndHerzegovina(CountryBase):
    Sarajevo = (43.85, 18.383)


class Moldova(CountryBase):
    Chisinau = (47.005, 28.8577)


class Malawi(CountryBase):
    Lilongwe = (-13.9833, 33.7833)
    Blantyre = (-15.79, 34.9899)


class Eritrea(CountryBase):
    Asmara = (15.3333, 38.9333)


class Mauritius(CountryBase):
    PortLouis = (-20.1666, 57.5)


class Gabon(CountryBase):
    Libreville = (0.3854, 9.458)


class Bahrain(CountryBase):
    Manama = (26.2361, 50.5831)


class Lithuania(CountryBase):
    Vilnius = (54.6834, 25.3166)


class Macedonia(CountryBase):
    Skopje = (42.0, 21.4335)


class Slovakia(CountryBase):
    Bratislava = (48.15, 17.117)


class GuineaBissau(CountryBase):
    Bissau = (11.865, -15.5984)


class Estonia(CountryBase):
    Tallinn = (59.4339, 24.728)


class Malta(CountryBase):
    Valletta = (35.8997, 14.5147)


class Lesotho(CountryBase):
    Maseru = (-29.3167, 27.4833)


class Burundi(CountryBase):
    Bujumbura = (-3.3761, 29.36)
    Gitega = (-3.4271, 29.9246)


class Slovenia(CountryBase):
    Ljubljana = (46.0553, 14.515)


class Brunei(CountryBase):
    BandarSeriBegawan = (4.8833, 114.9333)


class TrinidadAndTobago(CountryBase):
    PortofSpain = (10.652, -61.517)


class PapuaNewGuinea(CountryBase):
    PortMoresby = (-9.4647, 147.1925)


class Namibia(CountryBase):
    Windhoek = (-22.57, 17.0835)


class Guyana(CountryBase):
    Georgetown = (6.802, -58.167)


class Suriname(CountryBase):
    Paramaribo = (5.835, -55.167)


class TimorLeste(CountryBase):
    Dili = (-8.5594, 125.5795)


class Bahamas(CountryBase):
    Nassau = (25.0834, -77.35)


class Cyprus(CountryBase):
    Nicosia = (35.1667, 33.3666)


class SriLanka(CountryBase):
    Colombo = (6.932, 79.8578)
    SriJayewardenepuraKotte = (6.9, 79.95)


class Botswana(CountryBase):
    Gaborone = (-24.6463, 25.9119)


class Barbados(CountryBase):
    Bridgetown = (13.102, -59.6165)


class Fiji(CountryBase):
    Suva = (-18.133, 178.4417)


class Iceland(CountryBase):
    Reykjavik = (64.15, -21.95)


class EquatorialGuinea(CountryBase):
    Malabo = (3.75, 8.7833)


class Curacao(CountryBase):
    Willemstad = (12.2004, -69.02)


class Montenegro(CountryBase):
    Podgorica = (42.466, 19.2663)


class Comoros(CountryBase):
    Moroni = (-11.7042, 43.2402)


class CaboVerde(CountryBase):
    Praia = (14.9167, -23.5167)


class Maldives(CountryBase):
    Male = (4.1667, 73.4999)


class SouthSudan(CountryBase):
    Juba = (4.83, 31.58)


class Luxembourg(CountryBase):
    Luxembourg = (49.6117, 6.13)


class Bhutan(CountryBase):
    Thimphu = (27.473, 89.639)


class Swaziland(CountryBase):
    Mbabane = (-26.3167, 31.1333)
    Lobamba = (-26.4667, 31.2)


class SaoTomeAndPrincipe(CountryBase):
    SaoTome = (0.3334, 6.7333)


class SolomonIslands(CountryBase):
    Honiara = (-9.438, 159.9498)


class Aruba(CountryBase):
    Oranjestad = (12.5304, -70.029)


class Samoa(CountryBase):
    Apia = (-13.8415, -171.7386)


class Andorra(CountryBase):
    AndorralaVella = (42.5, 1.5165)


class SaintVincentAndTheGrenadines(CountryBase):
    Kingstown = (13.1483, -61.2121)


class Vanuatu(CountryBase):
    PortVila = (-17.7334, 168.3166)


class Gambia(CountryBase):
    Banjul = (13.4539, -16.5917)


class Tonga(CountryBase):
    Nukualofa = (-21.1385, -175.2206)


class SaintLucia(CountryBase):
    Castries = (14.002, -61.0)


class Monaco(CountryBase):
    Monaco = (43.7396, 7.4069)


class Liechtenstein(CountryBase):
    Vaduz = (47.1337, 9.5167)


class AntiguaAndBarbuda(CountryBase):
    SaintJohns = (17.118, -61.85)


class Grenada(CountryBase):
    SaintGeorges = (12.0526, -61.7416)


class Seychelles(CountryBase):
    Victoria = (-4.6166, 55.45)


class SanMarino(CountryBase):
    SanMarino = (43.9172, 12.4667)


class Kiribati(CountryBase):
    Tarawa = (1.3382, 173.0176)


class MarshallIslands(CountryBase):
    Majuro = (7.103, 171.38)


class Dominica(CountryBase):
    Roseau = (15.301, -61.387)


class SaintKittsAndNevis(CountryBase):
    Basseterre = (17.302, -62.717)


class Belize(CountryBase):
    Belmopan = (17.252, -88.7671)


class AmericanSamoa(CountryBase):
    PagoPago = (-14.274, -170.7046)


class Tuvalu(CountryBase):
    Funafuti = (-8.5167, 179.2166)


class Micronesia(CountryBase):
    Palikir = (6.9166, 158.15)


class NorthernMarianaIslands(CountryBase):
    CapitolHill = (15.2137, 145.7546)


class Guam(CountryBase):
    Hagta = (13.4745, 144.7504)


class WestBank(CountryBase):
    AlQuds = (31.7764, 35.2269)


class SintMaarten(CountryBase):
    Philipsburg = (18.0255, -63.045)


class Kosovo(CountryBase):
    Pristina = (42.6666, 21.1724)


class Palau(CountryBase):
    Ngerulmud = (7.5, 134.6242)


class Macau(CountryBase):
    Macau = (22.203, 113.545)
