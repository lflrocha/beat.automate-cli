app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

function TrocarTexto(nome_comp, nome_layer, novo_texto) {
  var texto = nome_comp.layer(nome_layer);
  texto.property("sourceText").setValue(novo_texto);
}


var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";

// Abre o arquivo JSON
var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
var arquivoJson = new File(caminhoDados)
if (arquivoJson.open("r")) {arquivoJson.encoding = "UTF-8";
    var meuJSON = arquivoJson.read();
    var dados = JSON.parse(meuJSON);
    arquivoJson.close();
}

modelo = dados['modelo']
if (modelo == "Tarde") {
    var nome_arquivo = "projetos/tvbr_tempo2023_box_tarde.aep"
} else {
    var nome_arquivo = "projetos/tvbr_tempo2023_box.aep"
}

var _io = new ImportOptions(File(baseFolder + nome_arquivo));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);


var data = dados['data'];
var cidade1 = dados['cidade1'];
var cidade2 = dados['cidade2'];

var comp_tela = app.project.item(2);

var comp_cidade1 = app.project.item(3);
TrocarTexto(comp_cidade1, "cidade", cidade1['nome']);
TrocarTexto(comp_cidade1, "temperatura_minima", cidade1['minima'] + 'º');
TrocarTexto(comp_cidade1, "temperatura_maxima", cidade1['maxima'] + 'º');
TrocarTexto(comp_cidade1, "probabilidade_chuva", cidade1['chuva'] + '%');
TrocarTexto(comp_cidade1, "umidade_minima", cidade1['umidade_min'] + '%');
TrocarTexto(comp_cidade1, "umidade_maxima", cidade1['umidade_max'] + '%');

var comp_cidade2 = app.project.item(4);
TrocarTexto(comp_cidade2, "cidade", cidade2['nome']);
TrocarTexto(comp_cidade2, "temperatura_minima", cidade2['minima'] + 'º');
TrocarTexto(comp_cidade2, "temperatura_maxima", cidade2['maxima'] + 'º');
TrocarTexto(comp_cidade2, "probabilidade_chuva", cidade2['chuva'] + '%');
TrocarTexto(comp_cidade2, "umidade_minima", cidade2['umidade_min'] + '%');
TrocarTexto(comp_cidade2, "umidade_maxima", cidade2['umidade_max'] + '%');


layer_cidade = comp_cidade1.layer("cidade")
altura = layer_cidade.sourceRectAtTime(80, true).height;
novo_y = 160
if (altura > 60) { novo_y = 140 }
if (altura > 100) { novo_y = 120 }
posicao = layer_cidade.property("position").value;
layer_cidade.property("position").setValueAtTime(0, [posicao[0], novo_y]);


layer_cidade = comp_cidade2.layer("cidade")
altura = layer_cidade.sourceRectAtTime(80, true).height;
novo_y = 160
if (altura > 60) { novo_y = 140 }
if (altura > 100) { novo_y = 120 }
posicao = layer_cidade.property("position").value;
layer_cidade.property("position").setValueAtTime(0, [posicao[0], novo_y]);


var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/amarelo/" + cidade1['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_cidade1.layer('icone').replaceSource(iconeImportado, false);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/amarelo/" + cidade2['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_cidade2.layer('icone').replaceSource(iconeImportado, false);

// for (var i = 0; i < arquivos.length; i++) {
//     var arquivo = arquivos[i]
//     var numero = i.toString()
//     var mapaAlertaLayer = comp_tela.layer("mapa-alerta-"+numero);
//
//     var importOptions = new ImportOptions();
//     importOptions.file = new File(arquivo);
//     var mapaImportado = app.project.importFile(importOptions);
//     mapaAlertaLayer.replaceSource(mapaImportado, false);
// }

app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
