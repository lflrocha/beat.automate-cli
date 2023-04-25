var BancoTimes =  ["Escudo",
"AA Araguaia-MT","ABC-RN","Águia de Marabá-PA","Altos-PI","América-MG","América-PE","América-RN","Anápolis-GO","Aparecidense-GO","ARSENAL DE SARANDi","ASA-AL",
"Atlético Acreano-AC","Atlético-GO","Atlético-MG","Atletico Nacional-COL","Atlético-PR", "Atlético Tucumán-ARG","Audax-SP","Avaí-SC",
"Bahia-BA","Barcelona de Guayaquil","Baré-RR","Boa Esporte-MG","Boavista-RJ","boca_juniors","Botafogo-PB","Botafogo-RJ","Botafogo-SP","Bragantino-SP","Brasil de Pelotas-RS","Brusque-SP",
"Caldense-MG","Campinense-PB","Caucaia-CE","Caxias-RS","Ceará-CE","Ceilândia-DF","Central-PE","Centro Olimpico-SP","Cerro Porteño-PAR","Cesar Vallejo-PER ok","Chapecoense-SC","Club_Nacional_de_Football_s_logo","Comercial-MS","club_nanas",
"Confiança-SE","Colo Colo-CHI","Cordino-MA","Corinthians-SP","Coritiba-PR","Coruripe-AL","CRB-AL","Cresspom-DF","Criciúma-SC","Cruzeiro-MG","CSA-AL","Cuiabá-MT",
"Desportiva Ferroviária-ES","Deportes Iquique-CHI","Duque de Caxias-RJ","deportivo_Cali",
"Emelec-EQU","ESMAC-PA","Estudiantes-ARG",
"Fast Club-AM","Ferroviaria-SP","Figueirense-SC","Flamengo-RJ","Fluminense de Feira-BA","Fluminense-RJ","Fortaleza-CE","Foz Cataratas-PR",
"Genus-RO","Globo-RN","Godoy cruz-ARG","Goianésia-GO","Goiás-GO","Grêmio-RS","Guarani-PAR","Guarani de Juazeiro-CE","Guarani-SP","Guaratinguetá-SP","Gurupi-TO",
"Icasa-CE","Independiente del Valle-EQU","Independiente Medellín-COL","Inter de Lages-SC","Internacional-RS","Iranduba-AM","Itabaiana-SE","Ituano-SP","Itumbiara-GO",
"J.Malucelli-PR","Jacobina-BA","Joinville-SC","Jorge Wilstermann-BOL","Juazeirense-BA","Juventude-RS",
"Lanus-ARG","Londrina-PR","Luverdense-MT","Luziânia-DF",
"Macaé-RJ","Madureira-RJ","Maranhão-MA","Maringá-PR","melgar","Metropolitano-SC","Millonarios-COL","Mogi Mirim-SP","Montevideo Wanderers-URU","Moto Club-MA","Murici-AL","mirassol",
"Nacional-PAR","nacional _uruguai","Náutico-PE","Novo Hamburgo-RS","Novorizontino",
"Oeste-SP","Operário-PR","Oriente Petrolero-COL",
"Palmeiras-SP","Paraná-PR","Parnahyba-PI","Paysandu-PA","Pinheirense-PA","Ponte Preta-SP","Portuguesa-RJ","Portuguesa-SP","Potiguar de Mossoró-RN","Princesa de Solimões-AM","PSTC-PR",
"Racing-ARG","REAL-BRASILIA","Remo-PA","Rio Branco-AC","Rio Preto-SP","River-PI","River Plate-ARG","Rondoniense-RO","Rosario Central-ARG",
"Salgueiro-PE","Sampaio Corrêa-MA","Santa Cruz-PE","Santos-AC","Santos-SP","São Bento-SP","São Bernardo-SP","São Francisco-PA","São José-RS","São Paulo-RS","São Paulo-SP",
"San Lorenzo-ARG","Santa Fé-COL","SÃO-JOSE-SP","São Raimundo-PA","São Raimundo-RR","Sergipe-SE","Serra Talhada-PE","Sete de Dourados-MS","Sinop-MT","Sporting Cristal-PER","Sports Boys-BOL","Sousa-PB",
"Sport-PE",
"Tiradentes-PI","The Strongest-BOL","Tocantinópolis-TO","Tocantins de Miracema-TO","Tolima-COL","Tombense-MG","Trem-AP","Trujillanos-VEN","Tupi-MG",
"Uniclinic-CE","Universidad Católica-CHI","Universitario de Sucre-BOL","URT-MG",
"Vasco-RJ","Velez_Arg","Viana-MA","Vila Nova-GO","Vila Nova-MG","Vitória-BA","Vitória das Tabocas-PE","Volta Redonda-RJ",
"XV de Piracicaba-SP",
"Ypiranga-RS",
"Zamora-VEN","Zulia-VEN",
]; 
/*
Code for Import https://scriptui.joonas.me — (Triple click to select): 
{"activeId":38,"items":{"item-0":{"id":0,"type":"Dialog","parentId":false,"style":{"enabled":true,"varName":null,"windowType":"Dialog","creationProps":{"su1PanelCoordinates":false,"maximizeButton":false,"minimizeButton":false,"independent":false,"closeButton":true,"borderless":false,"resizeable":false},"text":"Dialog","preferredSize":[0,0],"margins":16,"orientation":"column","spacing":10,"alignChildren":["center","top"]}},"item-1":{"id":1,"type":"DropDownList","parentId":0,"style":{"enabled":true,"varName":"NumerodeJogos","text":"DropDownList","listItems":"2,3,4","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-2":{"id":2,"type":"StaticText","parentId":0,"style":{"enabled":true,"varName":null,"creationProps":{"truncate":"none","multiline":false,"scrolling":false},"softWrap":false,"text":"Número de jogos","justify":"left","preferredSize":[0,0],"alignment":null,"helpTip":null}},"item-3":{"id":3,"type":"DropDownList","parentId":0,"style":{"enabled":true,"varName":null,"text":"DropDownList","listItems":"Stadium,MundodaBola,Jornalismo","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-4":{"id":4,"type":"StaticText","parentId":0,"style":{"enabled":true,"varName":null,"creationProps":{"truncate":"none","multiline":false,"scrolling":false},"softWrap":false,"text":"Background","justify":"left","preferredSize":[0,0],"alignment":null,"helpTip":null}},"item-5":{"id":5,"type":"Divider","parentId":0,"style":{"enabled":true,"varName":null}},"item-7":{"id":7,"type":"EditText","parentId":0,"style":{"enabled":true,"varName":null,"creationProps":{"noecho":false,"readonly":false,"multiline":false,"scrollable":false,"borderless":false,"enterKeySignalsOnChange":false},"softWrap":false,"text":"Nome do Campeonato","justify":"left","preferredSize":[0,0],"alignment":null,"helpTip":null}},"item-8":{"id":8,"type":"EditText","parentId":0,"style":{"enabled":true,"varName":null,"creationProps":{"noecho":false,"readonly":false,"multiline":false,"scrollable":false,"borderless":false,"enterKeySignalsOnChange":false},"softWrap":false,"text":"Subtítulo","justify":"left","preferredSize":[0,0],"alignment":null,"helpTip":null}},"item-9":{"id":9,"type":"Divider","parentId":0,"style":{"enabled":true,"varName":null}},"item-10":{"id":10,"type":"Panel","parentId":0,"style":{"enabled":true,"varName":null,"creationProps":{"borderStyle":"etched","su1PanelCoordinates":false},"text":"Jogo 1","preferredSize":[82,0],"margins":10,"orientation":"row","spacing":10,"alignChildren":["left","top"],"alignment":null}},"item-11":{"id":11,"type":"DropDownList","parentId":10,"style":{"enabled":true,"varName":"EscudoTimeA1","text":"DropDownList","listItems":"BancoTimes","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-12":{"id":12,"type":"EditText","parentId":10,"style":{"enabled":true,"varName":"NomeTimeA1","creationProps":{"noecho":false,"readonly":false,"multiline":false,"scrollable":false,"borderless":false,"enterKeySignalsOnChange":false},"softWrap":false,"text":"Nome Time 1","justify":"left","preferredSize":[0,0],"alignment":null,"helpTip":null}},"item-13":{"id":13,"type":"DropDownList","parentId":10,"style":{"enabled":true,"varName":"PlacarTimeA1","text":"DropDownList","listItems":"1,2,3,4,5,6,7,8,9","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-14":{"id":14,"type":"DropDownList","parentId":10,"style":{"enabled":true,"varName":"PlacarTimeB1","text":"DropDownList","listItems":"1,2,3,4,5,6,7,8,9","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-15":{"id":15,"type":"EditText","parentId":10,"style":{"enabled":true,"varName":"NomeTimeB1","creationProps":{"noecho":false,"readonly":false,"multiline":false,"scrollable":false,"borderless":false,"enterKeySignalsOnChange":false},"softWrap":false,"text":"Nome Time 2","justify":"left","preferredSize":[0,0],"alignment":null,"helpTip":null}},"item-16":{"id":16,"type":"DropDownList","parentId":10,"style":{"enabled":true,"varName":"EscudoTimeB1","text":"DropDownList","listItems":"BancoTimes","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-17":{"id":17,"type":"Panel","parentId":0,"style":{"enabled":true,"varName":null,"creationProps":{"borderStyle":"etched","su1PanelCoordinates":false},"text":"Jogo 2","preferredSize":[82,0],"margins":10,"orientation":"row","spacing":10,"alignChildren":["left","top"],"alignment":null}},"item-18":{"id":18,"type":"DropDownList","parentId":17,"style":{"enabled":true,"varName":"EscudoTimeA1","text":"DropDownList","listItems":"BancoTimes","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-19":{"id":19,"type":"EditText","parentId":17,"style":{"enabled":true,"varName":"NomeTimeA1","creationProps":{"noecho":false,"readonly":false,"multiline":false,"scrollable":false,"borderless":false,"enterKeySignalsOnChange":false},"softWrap":false,"text":"Nome Time 1","justify":"left","preferredSize":[0,0],"alignment":null,"helpTip":null}},"item-20":{"id":20,"type":"DropDownList","parentId":17,"style":{"enabled":true,"varName":"PlacarTimeA1","text":"DropDownList","listItems":"1,2,3,4,5,6,7,8,9","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-21":{"id":21,"type":"DropDownList","parentId":17,"style":{"enabled":true,"varName":"PlacarTimeB1","text":"DropDownList","listItems":"1,2,3,4,5,6,7,8,9","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-22":{"id":22,"type":"EditText","parentId":17,"style":{"enabled":true,"varName":"NomeTimeB1","creationProps":{"noecho":false,"readonly":false,"multiline":false,"scrollable":false,"borderless":false,"enterKeySignalsOnChange":false},"softWrap":false,"text":"Nome Time 2","justify":"left","preferredSize":[0,0],"alignment":null,"helpTip":null}},"item-23":{"id":23,"type":"DropDownList","parentId":17,"style":{"enabled":true,"varName":"EscudoTimeB1","text":"DropDownList","listItems":"BancoTimes","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-24":{"id":24,"type":"Panel","parentId":0,"style":{"enabled":true,"varName":null,"creationProps":{"borderStyle":"etched","su1PanelCoordinates":false},"text":"Jogo 3","preferredSize":[82,0],"margins":10,"orientation":"row","spacing":10,"alignChildren":["left","top"],"alignment":null}},"item-25":{"id":25,"type":"DropDownList","parentId":24,"style":{"enabled":true,"varName":"EscudoTimeA1","text":"DropDownList","listItems":"BancoTimes","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-26":{"id":26,"type":"EditText","parentId":24,"style":{"enabled":true,"varName":"NomeTimeA1","creationProps":{"noecho":false,"readonly":false,"multiline":false,"scrollable":false,"borderless":false,"enterKeySignalsOnChange":false},"softWrap":false,"text":"Nome Time 1","justify":"left","preferredSize":[0,0],"alignment":null,"helpTip":null}},"item-27":{"id":27,"type":"DropDownList","parentId":24,"style":{"enabled":true,"varName":"PlacarTimeA1","text":"DropDownList","listItems":"1,2,3,4,5,6,7,8,9","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-28":{"id":28,"type":"DropDownList","parentId":24,"style":{"enabled":true,"varName":"PlacarTimeB1","text":"DropDownList","listItems":"1,2,3,4,5,6,7,8,9","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-29":{"id":29,"type":"EditText","parentId":24,"style":{"enabled":true,"varName":"NomeTimeB1","creationProps":{"noecho":false,"readonly":false,"multiline":false,"scrollable":false,"borderless":false,"enterKeySignalsOnChange":false},"softWrap":false,"text":"Nome Time 2","justify":"left","preferredSize":[0,0],"alignment":null,"helpTip":null}},"item-30":{"id":30,"type":"DropDownList","parentId":24,"style":{"enabled":true,"varName":"EscudoTimeB1","text":"DropDownList","listItems":"BancoTimes","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-31":{"id":31,"type":"Panel","parentId":0,"style":{"enabled":true,"varName":null,"creationProps":{"borderStyle":"etched","su1PanelCoordinates":false},"text":"Jogo 4","preferredSize":[82,0],"margins":10,"orientation":"row","spacing":10,"alignChildren":["left","top"],"alignment":null}},"item-32":{"id":32,"type":"DropDownList","parentId":31,"style":{"enabled":true,"varName":"EscudoTimeA1","text":"DropDownList","listItems":"BancoTimes","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-33":{"id":33,"type":"EditText","parentId":31,"style":{"enabled":true,"varName":"NomeTimeA1","creationProps":{"noecho":false,"readonly":false,"multiline":false,"scrollable":false,"borderless":false,"enterKeySignalsOnChange":false},"softWrap":false,"text":"Nome Time 1","justify":"left","preferredSize":[0,0],"alignment":null,"helpTip":null}},"item-34":{"id":34,"type":"DropDownList","parentId":31,"style":{"enabled":true,"varName":"PlacarTimeA1","text":"DropDownList","listItems":"1,2,3,4,5,6,7,8,9","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-35":{"id":35,"type":"DropDownList","parentId":31,"style":{"enabled":true,"varName":"PlacarTimeB1","text":"DropDownList","listItems":"1,2,3,4,5,6,7,8,9","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-36":{"id":36,"type":"EditText","parentId":31,"style":{"enabled":true,"varName":"NomeTimeB1","creationProps":{"noecho":false,"readonly":false,"multiline":false,"scrollable":false,"borderless":false,"enterKeySignalsOnChange":false},"softWrap":false,"text":"Nome Time 2","justify":"left","preferredSize":[0,0],"alignment":null,"helpTip":null}},"item-37":{"id":37,"type":"DropDownList","parentId":31,"style":{"enabled":true,"varName":"EscudoTimeB1","text":"DropDownList","listItems":"BancoTimes","preferredSize":[0,0],"alignment":null,"selection":0,"helpTip":null}},"item-38":{"id":38,"type":"Button","parentId":0,"style":{"enabled":true,"varName":null,"text":"OK","justify":"center","preferredSize":[0,0],"alignment":null,"helpTip":null}}},"order":[0,2,1,4,3,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38],"settings":{"importJSON":true,"indentSize":false,"cepExport":false,"includeCSSJS":true,"showDialog":true,"functionWrapper":false,"afterEffectsDockable":false,"itemReferenceList":"None"}}
*/ 

// DIALOG
// ======
var dialog = new Window("dialog"); 
    dialog.text = "Dialog"; 
    dialog.orientation = "column"; 
    dialog.alignChildren = ["center","top"]; 
    dialog.spacing = 10; 
    dialog.margins = 16; 

var statictext1 = dialog.add("statictext", undefined, undefined, {name: "statictext1"}); 
    statictext1.text = "Número de jogos"; 

var NumerodeJogos_array = ["2","3","4"]; 
var NumerodeJogos = dialog.add("dropdownlist", undefined, undefined, {name: "NumerodeJogos", items: NumerodeJogos_array}); 
    NumerodeJogos.selection = 0; 

var statictext2 = dialog.add("statictext", undefined, undefined, {name: "statictext2"}); 
    statictext2.text = "Background"; 

var dropdown1_array = ["Stadium","MundodaBola","Jornalismo"]; 
var dropdown1 = dialog.add("dropdownlist", undefined, undefined, {name: "dropdown1", items: dropdown1_array}); 
    dropdown1.selection = 0; 

var divider1 = dialog.add("panel", undefined, undefined, {name: "divider1"}); 
    divider1.alignment = "fill"; 

var edittext1 = dialog.add('edittext {properties: {name: "edittext1"}}'); 
    edittext1.text = "Nome do Campeonato"; 

var edittext2 = dialog.add('edittext {properties: {name: "edittext2"}}'); 
    edittext2.text = "Subtítulo"; 

var divider2 = dialog.add("panel", undefined, undefined, {name: "divider2"}); 
    divider2.alignment = "fill"; 

// PANEL1
// ======
var panel1 = dialog.add("panel", undefined, undefined, {name: "panel1"}); 
    panel1.text = "Jogo 1"; 
    panel1.preferredSize.width = 82; 
    panel1.orientation = "row"; 
    panel1.alignChildren = ["left","top"]; 
    panel1.spacing = 10; 
    panel1.margins = 10; 

var EscudoTimeA1_array = BancoTimes; 
var EscudoTimeA1 = panel1.add("dropdownlist", undefined, undefined, {name: "EscudoTimeA1", items: EscudoTimeA1_array}); 
    EscudoTimeA1.selection = 0; 

var NomeTimeA1 = panel1.add('edittext {properties: {name: "NomeTimeA1"}}'); 
    NomeTimeA1.text = "Nome Time 1"; 

var PlacarTimeA1_array = ["0","1","2","3","4","5","6","7","8","9"]; 
var PlacarTimeA1 = panel1.add("dropdownlist", undefined, undefined, {name: "PlacarTimeA1", items: PlacarTimeA1_array}); 
    PlacarTimeA1.selection = 0; 

var PlacarTimeB1_array = ["0","1","2","3","4","5","6","7","8","9"]; 
var PlacarTimeB1 = panel1.add("dropdownlist", undefined, undefined, {name: "PlacarTimeB1", items: PlacarTimeB1_array}); 
    PlacarTimeB1.selection = 0; 

var NomeTimeB1 = panel1.add('edittext {properties: {name: "NomeTimeB1"}}'); 
    NomeTimeB1.text = "Nome Time 2"; 

var EscudoTimeB1_array = BancoTimes; 
var EscudoTimeB1 = panel1.add("dropdownlist", undefined, undefined, {name: "EscudoTimeB1", items: EscudoTimeB1_array}); 
    EscudoTimeB1.selection = 0; 

// PANEL2
// ======
var panel2 = dialog.add("panel", undefined, undefined, {name: "panel2"}); 
    panel2.text = "Jogo 2"; 
    panel2.preferredSize.width = 82; 
    panel2.orientation = "row"; 
    panel2.alignChildren = ["left","top"]; 
    panel2.spacing = 10; 
    panel2.margins = 10; 

var EscudoTimeA2_array = BancoTimes; 
var EscudoTimeA2 = panel2.add("dropdownlist", undefined, undefined, {name: "EscudoTimeA2", items: EscudoTimeA2_array}); 
    EscudoTimeA2.selection = 0; 

var NomeTimeA2 = panel2.add('edittext {properties: {name: "NomeTimeA2"}}'); 
    NomeTimeA2.text = "Nome Time 1"; 

var PlacarTimeA2_array = ["0","1","2","3","4","5","6","7","8","9"]; 
var PlacarTimeA2 = panel2.add("dropdownlist", undefined, undefined, {name: "PlacarTimeA2", items: PlacarTimeA2_array}); 
    PlacarTimeA2.selection = 0; 

var PlacarTimeB2_array = ["0","1","2","3","4","5","6","7","8","9"]; 
var PlacarTimeB2 = panel2.add("dropdownlist", undefined, undefined, {name: "PlacarTimeB2", items: PlacarTimeB2_array}); 
    PlacarTimeB2.selection = 0; 

var NomeTimeB2 = panel2.add('edittext {properties: {name: "NomeTimeB2"}}'); 
    NomeTimeB2.text = "Nome Time 2"; 

var EscudoTimeB2_array = BancoTimes; 
var EscudoTimeB2 = panel2.add("dropdownlist", undefined, undefined, {name: "EscudoTimeB2", items: EscudoTimeB2_array}); 
    EscudoTimeB2.selection = 0; 

// PANEL3
// ======
var panel3 = dialog.add("panel", undefined, undefined, {name: "panel3"}); 
    panel3.text = "Jogo 3"; 
    panel3.preferredSize.width = 82; 
    panel3.orientation = "row"; 
    panel3.alignChildren = ["left","top"]; 
    panel3.spacing = 10; 
    panel3.margins = 10; 

var EscudoTimeA3_array = BancoTimes; 
var EscudoTimeA3 = panel3.add("dropdownlist", undefined, undefined, {name: "EscudoTimeA3", items: EscudoTimeA3_array}); 
    EscudoTimeA3.selection = 0; 

var NomeTimeA3 = panel3.add('edittext {properties: {name: "NomeTimeA3"}}'); 
    NomeTimeA3.text = "Nome Time 1"; 

var PlacarTimeA3_array = ["0","1","2","3","4","5","6","7","8","9"]; 
var PlacarTimeA3 = panel3.add("dropdownlist", undefined, undefined, {name: "PlacarTimeA3", items: PlacarTimeA3_array}); 
    PlacarTimeA3.selection = 0; 

var PlacarTimeB3_array = ["0","1","2","3","4","5","6","7","8","9"]; 
var PlacarTimeB3 = panel3.add("dropdownlist", undefined, undefined, {name: "PlacarTimeB3", items: PlacarTimeB3_array}); 
    PlacarTimeB3.selection = 0; 

var NomeTimeB3 = panel3.add('edittext {properties: {name: "NomeTimeB3"}}'); 
    NomeTimeB3.text = "Nome Time 2"; 

var EscudoTimeB3_array = BancoTimes; 
var EscudoTimeB3 = panel3.add("dropdownlist", undefined, undefined, {name: "EscudoTimeB3", items: EscudoTimeB3_array}); 
    EscudoTimeB3.selection = 0; 

// PANEL4
// ======
var panel4 = dialog.add("panel", undefined, undefined, {name: "panel4"}); 
    panel4.text = "Jogo 4"; 
    panel4.preferredSize.width = 82; 
    panel4.orientation = "row"; 
    panel4.alignChildren = ["left","top"]; 
    panel4.spacing = 10; 
    panel4.margins = 10; 

var EscudoTimeA4_array = BancoTimes; 
var EscudoTimeA4 = panel4.add("dropdownlist", undefined, undefined, {name: "EscudoTimeA4", items: EscudoTimeA4_array}); 
    EscudoTimeA4.selection = 0; 

var NomeTimeA4 = panel4.add('edittext {properties: {name: "NomeTimeA4"}}'); 
    NomeTimeA4.text = "Nome Time 1"; 

var PlacarTimeA4_array = ["0","1","2","3","4","5","6","7","8","9"]; 
var PlacarTimeA4 = panel4.add("dropdownlist", undefined, undefined, {name: "PlacarTimeA4", items: PlacarTimeA4_array}); 
    PlacarTimeA4.selection = 0; 

var PlacarTimeB4_array = ["0","1","2","3","4","5","6","7","8","9"]; 
var PlacarTimeB4 = panel4.add("dropdownlist", undefined, undefined, {name: "PlacarTimeB4", items: PlacarTimeB4_array}); 
    PlacarTimeB4.selection = 0; 

var NomeTimeB4 = panel4.add('edittext {properties: {name: "NomeTimeB4"}}'); 
    NomeTimeB4.text = "Nome Time 2"; 

var EscudoTimeB4_array = BancoTimes; 
var EscudoTimeB4 = panel4.add("dropdownlist", undefined, undefined, {name: "EscudoTimeB4", items: EscudoTimeB4_array}); 
    EscudoTimeB4.selection = 0; 

// DIALOG
// ======
var button1 = dialog.add("button", undefined, undefined, {name: "button1"}); 
    button1.text = "OK"; 

dialog.show();

 try{
var MinhaComp = app.project.item(Number(NumerodeJogos.selection)+1)
var NovaComp = MinhaComp.duplicate()
NovaComp.name = edittext1.text
var TrocarFundo = NovaComp.layer(dropdown1.selection).property("opacity").setValue(100)

var Titulo =  NovaComp.layer("titulo").property("sourceText").setValue(edittext1.text)
var Subtitulo =  NovaComp.layer("subtitulo").property("sourceText").setValue(edittext2.text)


//jogo1
var J1EscudoTimeA = obterEscudo1PeloNome(EscudoTimeA1.selection.toString())
var J1NovoEscudoA = NovaComp.layer("J1escudo01").replaceSource(J1EscudoTimeA,true)

var J1EscudoTimeB = obterEscudo1PeloNome(EscudoTimeB1.selection.toString())
var J1NovoEscudoB = NovaComp.layer("J1escudo02").replaceSource(J1EscudoTimeB,true)

var J1NomeTimeA =  NovaComp.layer("J1NomeTime1").property("sourceText").setValue(NomeTimeA1.text)
var J1NomeTimeB =  NovaComp.layer("J1NomeTime2").property("sourceText").setValue(NomeTimeB1.text)

var J1PlacarTimeA =  NovaComp.layer("J1PlacarTimeA").property("sourceText").setValue(PlacarTimeA1.selection.toString())
var J1PlacarTimeB =  NovaComp.layer("J1PlacarTimeB").property("sourceText").setValue(PlacarTimeB1.selection.toString())

//jogo2
var J2EscudoTimeA = obterEscudo1PeloNome(EscudoTimeA2.selection.toString())
var J2NovoEscudoA = NovaComp.layer("J2escudo01").replaceSource(J2EscudoTimeA,true)

var J2EscudoTimeB = obterEscudo1PeloNome(EscudoTimeB2.selection.toString())
var J2NovoEscudoB = NovaComp.layer("J2escudo02").replaceSource(J2EscudoTimeB,true)

var J2NomeTimeA =  NovaComp.layer("J2NomeTime1").property("sourceText").setValue(NomeTimeA2.text)
var J2NomeTimeB =  NovaComp.layer("J2NomeTime2").property("sourceText").setValue(NomeTimeB2.text)

var J2PlacarTimeA =  NovaComp.layer("J2PlacarTimeA").property("sourceText").setValue(PlacarTimeA2.selection.toString())
var J2PlacarTimeB =  NovaComp.layer("J2PlacarTimeB").property("sourceText").setValue(PlacarTimeB2.selection.toString())

//jogo3
var J3EscudoTimeA = obterEscudo1PeloNome(EscudoTimeA3.selection.toString())
var J3NovoEscudoA = NovaComp.layer("J3escudo01").replaceSource(J3EscudoTimeA,true)

var J3EscudoTimeB = obterEscudo1PeloNome(EscudoTimeB3.selection.toString())
var J3NovoEscudoB = NovaComp.layer("J3escudo02").replaceSource(J3EscudoTimeB,true)

var J3NomeTimeA =  NovaComp.layer("J3NomeTime1").property("sourceText").setValue(NomeTimeA3.text)
var J3NomeTimeB =  NovaComp.layer("J3NomeTime2").property("sourceText").setValue(NomeTimeB3.text)

var J3PlacarTimeA =  NovaComp.layer("J3PlacarTimeA").property("sourceText").setValue(PlacarTimeA3.selection.toString())
var J3PlacarTimeB =  NovaComp.layer("J3PlacarTimeB").property("sourceText").setValue(PlacarTimeB3.selection.toString())

//jogo4
var J4EscudoTimeA = obterEscudo1PeloNome(EscudoTimeA4.selection.toString())
var J4NovoEscudoA = NovaComp.layer("J4escudo01").replaceSource(J4EscudoTimeA,true)

var J4EscudoTimeB = obterEscudo1PeloNome(EscudoTimeB4.selection.toString())
alert(J4EscudoTimeB.name)
var J4NovoEscudoB = NovaComp.layer("J4escudo02").replaceSource(J4EscudoTimeB,true)

var J4NomeTimeA =  NovaComp.layer("J4NomeTime1").property("sourceText").setValue(NomeTimeA4.text)
var J4NomeTimeB =  NovaComp.layer("J4NomeTime2").property("sourceText").setValue(NomeTimeB4.text)

var J4PlacarTimeA =  NovaComp.layer("J4PlacarTimeA").property("sourceText").setValue(PlacarTimeA4.selection.toString())
var J4PlacarTimeB =  NovaComp.layer("J4PlacarTimeB").property("sourceText").setValue(PlacarTimeB4.selection.toString())
 
 
 
 
 
 }catch(error){}

var listaRender = ["Animation_Alpha","Apple_ProRes","JPG","PNG_Alpha"]
var formatoRender = listaRender[1]

var caminhoSaidaRender = Folder.selectDialog("Selecione Caminho de OUTPUT")
//var caminhoSaidaRender = "D:/Arquivos/ID_TV_Brasil_2021/Chamada_Especial_BrasilVistoCima/Render"
var theRender = app.project.renderQueue.items.add(NovaComp)
        app.project.renderQueue.item(1).outputModule(1).file = new File(caminhoSaidaRender.toString() + "/" + NovaComp.name);
        app.project.renderQueue.item(1).outputModule(1).applyTemplate(formatoRender);

function obterEscudo1PeloNome(nomeFootage) {
    
    for (var i = 1; i <= app.project.numItems; i++) {
        if ((app.project.item(i).name == nomeFootage)) {
            Escudo1_ = app.project.item(i)
            break
        } else {
            Escudo1_ = null
        }
    }
    return  Escudo1_
 }
