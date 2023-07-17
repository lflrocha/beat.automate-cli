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
    var nome_arquivo = "projetos/tvbr_tempo2023_lista_tarde.aep"
} else {
    var nome_arquivo = "projetos/tvbr_tempo2023_lista.aep"
}

var _io = new ImportOptions(File(baseFolder + nome_arquivo));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);


var comp_cidade1 = app.project.item(3);
var comp_cidade2 = app.project.item(4);
var comp_cidade3 = app.project.item(5);
var comp_cidade4 = app.project.item(6);

var cidade1 = dados['cidade1'];
var cidade2 = dados['cidade2'];
var cidade3 = dados['cidade3'];
var cidade4 = dados['cidade4'];


TrocarTexto(comp_cidade1, "cidade", cidade1['nome']);
TrocarTexto(comp_cidade1, "minima", cidade1['minima']+'º');
TrocarTexto(comp_cidade1, "maxima", cidade1['maxima']+'º');
TrocarTexto(comp_cidade1, "chuva", cidade1['chuva']+'%');

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + cidade1['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_cidade1.layer('previsao').replaceSource(iconeImportado, false);

layer_cidade = comp_cidade1.layer("cidade")
altura = layer_cidade.sourceRectAtTime(1, true).height;
if (altura < 60) {
  novo_y = 80
  posicao = layer_cidade.property("position").value;
  layer_cidade.property("position").setValueAtTime(0, [posicao[0], novo_y]);
}


TrocarTexto(comp_cidade2, "cidade", cidade2['nome']);
TrocarTexto(comp_cidade2, "minima", cidade2['minima']+'º');
TrocarTexto(comp_cidade2, "maxima", cidade2['maxima']+'º');
TrocarTexto(comp_cidade2, "chuva", cidade2['chuva']+'%');

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + cidade2['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_cidade2.layer('previsao').replaceSource(iconeImportado, false);

layer_cidade = comp_cidade2.layer("cidade")
altura = layer_cidade.sourceRectAtTime(80, true).height;
if (altura < 60) {
  novo_y = 80
  posicao = layer_cidade.property("position").value;
  layer_cidade.property("position").setValueAtTime(0, [posicao[0], novo_y]);
}

TrocarTexto(comp_cidade3, "cidade", cidade3['nome']);
TrocarTexto(comp_cidade3, "minima", cidade3['minima']+'º');
TrocarTexto(comp_cidade3, "maxima", cidade3['maxima']+'º');
TrocarTexto(comp_cidade3, "chuva", cidade3['chuva']+'%');

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + cidade3['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_cidade3.layer('previsao').replaceSource(iconeImportado, false);

layer_cidade = comp_cidade3.layer("cidade")
altura = layer_cidade.sourceRectAtTime(80, true).height;
if (altura < 60) {
  novo_y = 80
  posicao = layer_cidade.property("position").value;
  layer_cidade.property("position").setValueAtTime(0, [posicao[0], novo_y]);
}

TrocarTexto(comp_cidade4, "cidade", cidade4['nome']);
TrocarTexto(comp_cidade4, "minima", cidade4['minima']+'º');
TrocarTexto(comp_cidade4, "maxima", cidade4['maxima']+'º');
TrocarTexto(comp_cidade4, "chuva", cidade4['chuva']+'%');

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + cidade4['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_cidade4.layer('previsao').replaceSource(iconeImportado, false);

layer_cidade = comp_cidade4.layer("cidade")
altura = layer_cidade.sourceRectAtTime(80, true).height;
if (altura < 60) {
  novo_y = 80
  posicao = layer_cidade.property("position").value;
  layer_cidade.property("position").setValueAtTime(0, [posicao[0], novo_y]);
}

app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
