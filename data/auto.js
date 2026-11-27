/*
  Parco auto Collinelli Auto — dati di partenza presi dal sito attuale (novembre 2026).
  Ogni oggetto corrisponde a una riga della futura tabella "auto" del pannello admin.
  foto: percorsi relativi a FOTO_BASE; la prima foto è la copertina.
  neopatentati: da confermare sul libretto (max 105 kW e 75 kW/t).
*/
window.FOTO_BASE = "https://www.collinelliauto.it/it/wp-content/uploads/";

window.AUTO = [
  {
    id: "peugeot-3008-puretech-130-eat8-allure",
    marca: "Peugeot", modello: "3008", versione: "PureTech 1.2 130 CV EAT8 Allure",
    prezzo: 23800, iva: false, km: 50, immatricolazione: "03/2023",
    carburante: "Benzina", cambio: "Automatico", marce: "EAT8, 8 rapporti", cv: 130, litri: "1.2",
    colore: "Blu Celebes metallizzato", proprietari: 1, carrozzeria: "Crossover",
    neopatentati: false, evidenza: true, inserita: "2026-11-24",
    dotazioni: ["Clima automatico bizona", "Navigatore", "Touchscreen 10\" con Apple CarPlay e Android Auto", "Head-up digital display 12,3\"", "Frenata automatica d'emergenza", "Mantenimento corsia attivo", "Cruise control", "Sensori di parcheggio anteriori e posteriori"],
    foto: ["2026/11/20261124_124645.jpg", "2026/11/20261124_124119.jpg", "2026/11/20261124_124058.jpg", "2026/11/20261124_124310.jpg", "2026/11/20261124_123759.jpg", "2026/11/20261124_123828.jpg", "2026/11/20261124_123849.jpg", "2026/11/20261124_123818.jpg"]
  },
  {
    id: "vw-tiguan-20-tdi-150-dsg-elegance",
    marca: "Volkswagen", modello: "Tiguan", versione: "2.0 TDI 150 CV DSG Elegance",
    prezzo: 28900, iva: false, ivaEsposta: true, km: 40200, immatricolazione: "11/2023",
    carburante: "Diesel", cambio: "Automatico", marce: "DSG, 7 rapporti con palette al volante", cv: 150, litri: "2.0",
    colore: "Blu Nightshade metallizzato", proprietari: 1, carrozzeria: "SUV",
    neopatentati: false, evidenza: true, inserita: "2026-10-10",
    dotazioni: ["Fari IQ.Light LED Matrix", "Digital Cockpit Pro 10,25\"", "Navigatore Discover Media", "Cruise adattivo ACC", "Front Assist, Lane Assist e Side Assist", "Telecamera 360°", "Clima automatico trizona", "Sedili sportivi in Alcantara", "Keyless e portellone con apertura a sensore", "Cerchi in lega 18\"", "Tagliandi documentati"],
    foto: ["2026/10/20261010_120253.jpg", "2026/10/20261010_115301.jpg", "2026/10/20261010_115252.jpg", "2026/10/20261010_115351.jpg", "2026/10/20261010_095234.jpg", "2026/10/20261010_095320.jpg", "2026/10/20261010_091521.jpg", "2026/10/20261010_095241.jpg"]
  },
  {
    id: "audi-a3-sportback-30-tfsi-business-advanced",
    marca: "Audi", modello: "A3 Sportback", versione: "30 TFSI 1.0 110 CV Business Advanced",
    prezzo: 23800, iva: false, km: 57300, immatricolazione: "04/2021",
    carburante: "Benzina", cambio: "Manuale", cv: 110, litri: "1.0",
    colore: "Nero Mito metallizzato", proprietari: 1, carrozzeria: "Berlina",
    neopatentati: true, evidenza: false, inserita: "2026-05-23",
    dotazioni: ["Clima automatico", "Cruise control", "Navigatore", "Sedili sportivi", "Fari LED", "Sensori di parcheggio", "Apple CarPlay e Android Auto", "Cerchi in lega"],
    foto: ["2026/05/20260523_103308.jpg", "2026/05/20260523_103025.jpg", "2026/05/20260523_103018.jpg", "2026/05/20260523_103111.jpg", "2026/05/20260523_082517.jpg", "2026/05/20260523_082600.jpg", "2026/05/20260523_082529.jpg", "2026/05/20260523_082541.jpg"]
  },
  {
    id: "mini-countryman-15-102-boost",
    marca: "Mini", modello: "Countryman", versione: "1.5 102 CV Boost",
    prezzo: 23000, iva: false, km: 36450, immatricolazione: "04/2022",
    carburante: "Benzina", cambio: "Manuale", cv: 102, litri: "1.5",
    colore: "Island Blue metallizzato", proprietari: 1, carrozzeria: "Crossover",
    neopatentati: true, evidenza: true, inserita: "2026-11-10",
    dotazioni: ["Fari full LED", "Clima automatico", "Cruise control", "Apple CarPlay", "Retrocamera", "Sensori di parcheggio posteriori", "Sedili sportivi riscaldabili", "Cerchi in lega 17\""],
    foto: ["2026/11/20261114_115424.jpg", "2026/11/20261114_114932.jpg", "2026/11/20261114_115021.jpg", "2026/11/20261114_114913.jpg", "2026/11/20261109_122616.jpg", "2026/11/20261109_122627.jpg", "2026/11/20261109_122859.jpg", "2026/11/20261109_122633.jpg"]
  },
  {
    id: "audi-q2-30-tfsi-110-advanced",
    marca: "Audi", modello: "Q2", versione: "30 TFSI 1.0 110 CV Advanced",
    prezzo: 22650, iva: false, km: 35000, immatricolazione: "04/2022",
    carburante: "Benzina", cambio: "Manuale", cv: 110, litri: "1.0",
    colore: "Nero brillante", proprietari: 1, carrozzeria: "Crossover",
    neopatentati: true, evidenza: false, inserita: "2026-07-30",
    dotazioni: ["Cruise adattivo", "Fari full LED", "Navigatore", "Retrocamera", "Sensori di parcheggio anteriori e posteriori", "Sedili anteriori riscaldabili", "Portellone elettrico", "Clima automatico"],
    foto: ["2024/03/20260730_101147.jpg", "2024/03/20260730_101015.jpg", "2024/03/20260730_101032.jpg", "2024/03/20260730_101046.jpg", "2024/03/20260728_081719.jpg", "2024/03/20260728_081500.jpg", "2024/03/20260728_081538.jpg", "2024/03/20260728_081805.jpg"]
  },
  {
    id: "audi-q2-30-tfsi-110-business",
    marca: "Audi", modello: "Q2", versione: "30 TFSI 1.0 110 CV Business",
    prezzo: 22000, iva: false, km: 61600, immatricolazione: "05/2022",
    carburante: "Benzina", cambio: "Manuale", cv: 110, litri: "1.0",
    colore: "Grigio Manhattan metallizzato", proprietari: 1, carrozzeria: "Crossover",
    neopatentati: true, evidenza: false, inserita: "2026-05-23",
    dotazioni: ["Cruise adattivo", "Fari full LED", "Navigatore", "Retrocamera", "Sensori di parcheggio anteriori e posteriori", "Sedili anteriori riscaldabili", "Clima automatico", "Cerchi in lega 17\""],
    foto: ["2026/05/20260523_103912.jpg", "2026/05/20260523_103543.jpg", "2026/05/20260523_103801.jpg", "2026/05/20260523_103721.jpg", "2026/05/20260523_081805.jpg", "2026/05/20260523_081823.jpg", "2026/05/20260523_081609.jpg", "2026/05/20260523_081832.jpg"]
  },
  {
    id: "vw-t-roc-10-tsi-life-110",
    marca: "Volkswagen", modello: "T-Roc", versione: "1.0 TSI Life 110 CV",
    prezzo: 21500, iva: false, km: 49000, immatricolazione: "04/2022",
    carburante: "Benzina", cambio: "Manuale", cv: 110, litri: "1.0",
    colore: "Indium Grey metallizzato", proprietari: 1, carrozzeria: "Crossover",
    neopatentati: true, evidenza: false, inserita: "2026-05-18",
    dotazioni: ["Digital Cockpit 8\"", "Navigatore", "Apple CarPlay e Android Auto", "Cruise adattivo ACC", "Lane Assist", "Park Assist", "Clima automatico bizona"],
    foto: ["2025/11/20260518_113308.jpg", "2025/11/20260518_112553.jpg", "2025/11/20260518_112716.jpg", "2025/11/20260518_112607.jpg", "2025/11/20260518_113443.jpg", "2025/11/20251101_112934-scaled.jpg", "2025/11/20251101_113012-scaled.jpg", "2025/11/20251101_113700-scaled.jpg"]
  },
  {
    id: "bmw-218i-active-tourer-business-automatica",
    marca: "BMW", modello: "218i Active Tourer", versione: "Advantage Business 136 CV automatica",
    prezzo: 19900, iva: false, km: 34800, immatricolazione: "06/2021",
    carburante: "Benzina", cambio: "Automatico", marce: "7 rapporti", cv: 136, litri: "1.5",
    colore: "Grigio Minerale metallizzato", proprietari: 1, carrozzeria: "Monovolume",
    neopatentati: false, evidenza: false, inserita: "2026-09-26",
    dotazioni: ["Fari full LED", "Navigatore", "Clima automatico", "Cruise control", "Sensori di parcheggio anteriori e posteriori", "Portellone elettrico", "Avviso anticollisione", "Cerchi in lega"],
    foto: ["2024/09/20260926_092227.jpg", "2024/09/20260926_091827-scaled.jpg", "2024/09/20260926_091847-scaled.jpg", "2024/09/20260926_091959-scaled.jpg", "2024/09/20260907_082312.jpg", "2024/09/20260907_082324.jpg", "2024/09/20260907_082531.jpg", "2024/09/20260907_082544.jpg"]
  },
  {
    id: "opel-mokka-12-turbo-136-edition",
    marca: "Opel", modello: "Mokka", versione: "1.2 Turbo 136 CV Edition",
    prezzo: 18500, iva: false, km: 550, immatricolazione: "03/2024",
    carburante: "Benzina", cambio: "Manuale", cv: 136, litri: "1.2",
    colore: "Karbon Black metallizzato", proprietari: 1, carrozzeria: "Crossover",
    neopatentati: false, evidenza: true, inserita: "2026-10-01",
    dotazioni: ["Fari Eco-LED", "Touchscreen 7\" con Apple CarPlay e Android Auto", "Cruise control con limitatore", "Mantenimento corsia attivo", "Retrocamera 180°", "Climatizzatore"],
    foto: ["2026/10/20260930_122202.jpg", "2026/10/20260930_122345.jpg", "2026/10/20260930_122335.jpg", "2026/10/20260930_122505.jpg", "2026/10/20260930_092527.jpg", "2026/10/20260930_092554.jpg", "2026/10/20260930_092958.jpg", "2026/10/20260930_122616.jpg"]
  },
  {
    id: "ford-puma-10-hybrid-125-st-line",
    marca: "Ford", modello: "Puma", versione: "1.0 Hybrid EcoBoost 125 CV ST-Line",
    prezzo: 18000, iva: false, km: 21500, immatricolazione: "01/2022",
    carburante: "Ibrida", cambio: "Manuale", cv: 125, litri: "1.0",
    colore: "Agate Black metallizzato", proprietari: 1, carrozzeria: "Crossover",
    neopatentati: false, evidenza: false, inserita: "2026-03-26",
    dotazioni: ["Fari full LED", "Navigatore", "Clima automatico", "Cruise control", "Sedili sportivi", "Avviamento keyless", "Sensori di parcheggio posteriori", "Cerchi in lega 17\""],
    foto: ["2026/03/20260926_105200.jpg", "2026/03/20260325_085127.jpg", "2026/03/20260325_085258.jpg", "2026/03/20260325_085115.jpg", "2026/03/20260325_084052.jpg", "2026/03/20260325_084106.jpg", "2026/03/20260325_083744.jpg", "2026/03/20260325_084059.jpg"]
  },
  {
    id: "renault-kadjar-15-blue-dci-115-edc-business",
    marca: "Renault", modello: "Kadjar", versione: "1.5 Blue dCi 115 CV EDC Business",
    prezzo: 17800, iva: false, km: 65000, immatricolazione: "09/2022",
    carburante: "Diesel", cambio: "Automatico", marce: "EDC doppia frizione, 7 rapporti", cv: 115, litri: "1.5",
    colore: "Nero metallizzato", proprietari: 1, carrozzeria: "Crossover",
    neopatentati: false, evidenza: false, inserita: "2026-02-21",
    dotazioni: ["Navigatore", "Clima automatico", "Cruise control", "Retrocamera", "Sensori di parcheggio", "Fendinebbia", "Cerchi in lega"],
    foto: ["2026/02/20260221_100011.jpg", "2026/02/20260221_095832.jpg", "2026/02/20260221_100317.jpg", "2026/02/20260221_095848.jpg", "2026/02/20260221_100754.jpg", "2026/02/20260221_100555-scaled.jpg", "2026/02/20260221_100745.jpg", "2026/02/20260221_100731.jpg"]
  },
  {
    id: "mercedes-e200-cabrio-sportline-1993",
    marca: "Mercedes-Benz", modello: "E 200 Cabrio", versione: "136 CV Sportline automatica",
    prezzo: 17500, iva: false, km: 178000, immatricolazione: "06/1993",
    carburante: "Benzina", cambio: "Automatico", marce: "4 rapporti", cv: 136, litri: "2.0",
    colore: "Nero", proprietari: null, carrozzeria: "Cabrio",
    neopatentati: false, evidenza: false, inserita: "2025-07-30",
    dotazioni: ["Interni in pelle", "Climatizzatore", "Vetri elettrici", "Chiusura centralizzata", "ABS", "Fendinebbia", "Cerchi in lega"],
    foto: ["2020/06/20250730_113714-scaled.jpg", "2020/06/20250730_100130-scaled.jpg", "2020/06/20250730_100148-scaled.jpg", "2020/06/20250730_100206-scaled.jpg", "2020/06/20250730_110211-scaled.jpg", "2020/06/20250730_110216-scaled.jpg", "2020/06/20250730_110059-scaled.jpg", "2020/06/20250730_110107-scaled.jpg"]
  },
  {
    id: "kia-stonic-10-t-gdi-mhev-100-style",
    marca: "Kia", modello: "Stonic", versione: "1.0 T-GDi MHEV 100 CV Style",
    prezzo: 17300, iva: false, km: 27500, immatricolazione: "07/2024",
    carburante: "Ibrida", cambio: "Manuale", cv: 100, litri: "1.0",
    colore: "Sporty Blue metallizzato", proprietari: 1, carrozzeria: "Crossover",
    neopatentati: true, evidenza: false, inserita: "2026-10-22",
    dotazioni: ["Fari full LED", "Touchscreen 8\" con DAB, Apple CarPlay e Android Auto", "Clima automatico", "Cruise control con limitatore", "Mantenimento corsia", "Frenata automatica d'emergenza", "Sensori di parcheggio anteriori e posteriori", "Cerchi in lega 17\""],
    foto: ["2026/10/20261022_120230.jpg", "2026/10/20261022_120706.jpg", "2026/10/20261022_120415.jpg", "2026/10/20261022_120648.jpg", "2026/10/20261022_114008.jpg", "2026/10/20261022_114038.jpg", "2026/10/20261022_113814.jpg", "2026/10/20261022_114051.jpg"]
  },
  {
    id: "mini-clubman-one-15-102-chili",
    marca: "Mini", modello: "Clubman", versione: "One 1.5 102 CV Chili",
    prezzo: 16900, iva: false, km: 52700, immatricolazione: "08/2018",
    carburante: "Benzina", cambio: "Manuale", cv: 102, litri: "1.5",
    colore: "Melting Silver metallizzato", proprietari: null, carrozzeria: "Station wagon",
    neopatentati: true, evidenza: false, inserita: "2026-11-20",
    dotazioni: ["Interni in pelle", "Sedili sportivi", "Navigatore", "Clima automatico", "Cruise control", "Fendinebbia", "Cerchi in lega"],
    foto: ["2026/11/20261120_104153.jpg", "2026/11/20261120_104722.jpg", "2026/11/20261120_104734.jpg", "2026/11/20261120_104859.jpg", "2026/11/20261120_105334.jpg", "2026/11/20261120_110251.jpg", "2026/11/20261120_105346.jpg", "2026/11/20261120_105016.jpg"]
  },
  {
    id: "dr-50-15-gpl-unica",
    marca: "DR", modello: "5.0", versione: "1.5 Unica GPL 117 CV",
    prezzo: 16300, iva: false, km: 23500, immatricolazione: "12/2024",
    carburante: "GPL", cambio: "Manuale", cv: 117, litri: "1.5",
    colore: "Grigio metallizzato", proprietari: 1, carrozzeria: "SUV",
    neopatentati: false, evidenza: false, inserita: "2026-10-26",
    dotazioni: ["Schermo touch 12,3\"", "Apple CarPlay e Android Auto wireless", "Apertura e avviamento keyless", "Cruise control", "Retrocamera", "Sensori di parcheggio posteriori", "Controllo discesa HDC"],
    foto: ["2020/05/20261026_102819.jpg", "2020/05/20261026_102353.jpg", "2020/05/20261026_102339.jpg", "2020/05/20261026_102450.jpg", "2020/05/20261026_103523.jpg", "2020/05/20261026_103537.jpg", "2020/05/20261026_103330.jpg", "2020/05/20261026_103622.jpg"]
  },
  {
    id: "opel-crossland-12-110-edition",
    marca: "Opel", modello: "Crossland", versione: "1.2 110 CV Edition",
    prezzo: 13600, iva: false, km: 52000, immatricolazione: "06/2022",
    carburante: "Benzina", cambio: "Manuale", cv: 110, litri: "1.2",
    colore: "Mineral Black", proprietari: 1, carrozzeria: "Crossover",
    neopatentati: true, evidenza: false, inserita: "2026-05-20",
    dotazioni: ["Fari Eco LED", "Apple CarPlay e Android Auto", "Bluetooth", "Cruise control", "Avviso superamento corsia", "Climatizzatore"],
    foto: ["2023/01/20260520_101919.jpg", "2023/01/20260520_102106.jpg", "2023/01/20260520_102153.jpg", "2023/01/20260520_102056.jpg", "2023/01/20260520_101201.jpg", "2023/01/20260520_101238.jpg", "2023/01/20260520_101247.jpg", "2023/01/20260520_101210.jpg"]
  },
  {
    id: "mini-countryman-cooper-16-122-all4-park-lane",
    marca: "Mini", modello: "Countryman", versione: "Cooper 1.6 122 CV ALL4 Park Lane",
    prezzo: 13500, iva: false, km: 64500, immatricolazione: "02/2016",
    carburante: "Benzina", cambio: "Manuale", cv: 122, litri: "1.6",
    colore: "Earl Grey metallizzato, tetto Oak Red", proprietari: null, carrozzeria: "Crossover",
    neopatentati: false, evidenza: false, inserita: "2026-11-20",
    dotazioni: ["Trazione integrale ALL4", "Interni in pelle", "Sedili anteriori riscaldabili", "Fari bi-xeno", "Clima automatico", "Cruise control", "Sensori di parcheggio posteriori", "Cerchi in lega"],
    foto: ["2022/04/20261120_100803.jpg", "2022/04/20261120_100932-scaled.jpg", "2022/04/20261120_101129.jpg", "2022/04/20261120_100958.jpg", "2022/04/20261120_091243.jpg", "2022/04/20261120_091302.jpg", "2022/04/20261120_091253.jpg", "2022/04/20261120_091203.jpg"]
  },
  {
    id: "lancia-ypsilon-10-firefly-hybrid-70-silver",
    marca: "Lancia", modello: "Ypsilon", versione: "1.0 FireFly Hybrid 70 CV Silver",
    prezzo: 11950, iva: false, km: 43500, immatricolazione: "01/2023",
    carburante: "Ibrida", cambio: "Manuale", cv: 70, litri: "1.0",
    colore: "Rosso pastello", proprietari: 1, carrozzeria: "Utilitaria",
    neopatentati: true, evidenza: false, inserita: "2026-03-25",
    dotazioni: ["Climatizzatore", "Volante multifunzione", "Radio", "Vetri elettrici", "Chiusura centralizzata", "Airbag laterali"],
    foto: ["2020/08/20260325_090426.jpg", "2020/08/20260325_090114.jpg", "2020/08/20260325_090209.jpg", "2020/08/20260325_090126.jpg", "2020/08/20260325_090531.jpg", "2020/08/20260325_090635.jpg", "2020/08/20260325_090726.jpg", "2020/08/20260325_090543.jpg"]
  },
  {
    id: "fiat-qubo-14-77-natural-power-easy",
    marca: "Fiat", modello: "Qubo", versione: "1.4 77 CV Natural Power Easy",
    prezzo: 11900, iva: false, km: 46500, immatricolazione: "11/2018",
    carburante: "Metano", cambio: "Manuale", cv: 77, litri: "1.4",
    colore: "Bianco Gelato", proprietari: 1, carrozzeria: "Monovolume",
    neopatentati: true, evidenza: false, inserita: "2026-04-08",
    dotazioni: ["Radio DAB touchscreen con Bluetooth", "Climatizzatore", "Sensori di parcheggio posteriori", "Airbag frontali e laterali", "ESP"],
    foto: ["2022/03/20260408_111906.jpg", "2022/03/20260408_111531.jpg", "2022/03/20260408_111636.jpg", "2022/03/20260408_111518.jpg", "2022/03/20260408_112327.jpg", "2022/03/20260408_112342.jpg", "2022/03/20260408_112352.jpg", "2022/03/20260408_112243.jpg"]
  },
  {
    id: "fiat-500-10-hybrid-70-cult",
    marca: "Fiat", modello: "500", versione: "1.0 Hybrid 70 CV Cult",
    prezzo: 11850, iva: false, km: 43350, immatricolazione: "09/2022",
    carburante: "Ibrida", cambio: "Manuale", cv: 70, litri: "1.0",
    colore: "Grigio Pompei metallizzato", proprietari: 1, carrozzeria: "Utilitaria",
    neopatentati: true, evidenza: false, inserita: "2026-11-20",
    dotazioni: ["Climatizzatore", "Vetri elettrici", "Chiusura centralizzata", "Airbag frontali e laterali", "ESP"],
    foto: ["2020/05/20261120_102128.jpg", "2020/05/20261120_102221.jpg", "2020/05/20261120_102232.jpg", "2020/05/20261120_102338.jpg", "2020/05/20261120_090606.jpg", "2020/05/20261120_090613.jpg", "2020/05/20261120_090547.jpg", "2020/05/20261120_090529.jpg"]
  },
  {
    id: "ford-fiesta-active-10-ecoboost-86",
    marca: "Ford", modello: "Fiesta Active", versione: "1.0 EcoBoost 86 CV",
    prezzo: 11800, iva: false, km: 64000, immatricolazione: "05/2019",
    carburante: "Benzina", cambio: "Manuale", cv: 86, litri: "1.0",
    colore: "Bianco Ghiaccio", proprietari: null, carrozzeria: "Crossover",
    neopatentati: true, evidenza: false, inserita: "2022-09-02",
    dotazioni: ["Apple CarPlay e Android Auto", "Sedili sportivi riscaldabili", "Avviso superamento corsia", "Partenza assistita in salita", "Sensori di parcheggio posteriori", "Climatizzatore"],
    foto: ["2023/08/20220902_104039-scaled.jpg", "2023/08/20220902_103119-scaled.jpg", "2023/08/20220902_103136-scaled.jpg", "2023/08/20220902_103839-scaled.jpg", "2023/08/20220902_104845-scaled.jpg", "2023/08/20220902_104909-scaled.jpg", "2023/08/20220902_104607-scaled.jpg", "2023/08/20220902_104306-scaled.jpg"]
  },
  {
    id: "fiat-panda-10-hybrid-70-5-posti",
    marca: "Fiat", modello: "Panda", versione: "1.0 70 CV Hybrid 5 posti",
    prezzo: 10250, iva: false, km: 64500, immatricolazione: "06/2021",
    carburante: "Ibrida", cambio: "Manuale", cv: 70, litri: "1.0",
    colore: "Bianco pastello", proprietari: 1, carrozzeria: "Utilitaria",
    neopatentati: true, evidenza: false, inserita: "2026-06-20",
    dotazioni: ["5 posti", "Climatizzatore", "Radio", "Vetri elettrici", "Chiusura centralizzata", "Airbag frontali e laterali"],
    foto: ["2019/05/20260620_115958.jpg", "2019/05/20260620_120722.jpg", "2019/05/20260620_120838.jpg", "2019/05/20260620_120713.jpg", "2019/05/20250829_100452-scaled.jpg", "2019/05/20250829_100533-scaled.jpg", "2019/05/20250829_100546-scaled.jpg", "2019/05/20250829_100500-scaled.jpg"]
  },
  {
    id: "fiat-doblo-cargo-14-t-jet-120-natural-power",
    marca: "Fiat", modello: "Doblò Cargo", versione: "1.4 T-Jet 120 CV Natural Power Lounge",
    prezzo: 9800, iva: true, km: 64000, immatricolazione: "10/2019",
    carburante: "Metano", cambio: "Manuale", cv: 120, litri: "1.4",
    colore: "Bianco", proprietari: 1, carrozzeria: "Furgone",
    neopatentati: false, evidenza: false, inserita: "2026-07-30",
    dotazioni: ["Climatizzatore", "Radio Bluetooth e USB con comandi al volante", "Computer di bordo", "Chiusura a distanza", "Sedile guida regolabile in altezza e lombare", "Fendinebbia", "Ruota di scorta"],
    foto: ["2016/04/20260730_095617.jpg", "2016/04/20260730_100103.jpg", "2016/04/20260730_100348.jpg", "2016/04/20260730_100056.jpg", "2016/04/20260730_094950.jpg", "2016/04/20260730_095011.jpg", "2016/04/20260730_094910.jpg", "2016/04/20260730_094903.jpg"]
  },
  {
    id: "fiat-fiorino-13-multijet-95-sx",
    marca: "Fiat", modello: "Fiorino", versione: "1.3 Multijet 95 CV SX",
    prezzo: 8900, iva: true, km: 103500, immatricolazione: "12/2020",
    carburante: "Diesel", cambio: "Manuale", cv: 95, litri: "1.3",
    colore: "Bianco", proprietari: 1, carrozzeria: "Furgone",
    neopatentati: false, evidenza: false, inserita: "2026-03-25",
    dotazioni: ["Radio DAB touchscreen 7\" con Bluetooth", "Climatizzatore", "Sensori di parcheggio posteriori", "Chiusura a distanza", "Airbag guida e passeggero", "ASR"],
    foto: ["2019/03/20260325_092347.jpg", "2019/03/20260325_093016.jpg", "2019/03/20260325_093052.jpg", "2019/03/20260325_093002.jpg", "2019/03/20260325_092452.jpg", "2019/03/20260325_092534.jpg", "2019/03/20260325_092442.jpg", "2019/03/20260325_092620.jpg"]
  }
];
