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
    var nome_arquivo = "projetos/tvbr_tempo2023_3dias_tarde.aep"
} else {
    var nome_arquivo = "projetos/tvbr_tempo2023_3dias.aep"
}

var _io = new ImportOptions(File(baseFolder + nome_arquivo));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);

var cidade = dados['cidade'];

var dia1 = dados['dia1']
var dia2 = dados['dia2']
var dia3 = dados['dia3']


var comp_tela = app.project.item(2);
TrocarTexto(comp_tela, "cidade", cidade);

TrocarTexto(comp_tela, "dia1", dia1['dia_semana']);
TrocarTexto(comp_tela, "dia2", dia2['dia_semana']);
TrocarTexto(comp_tela, "dia3", dia3['dia_semana']);

TrocarTexto(comp_tela, "min1", dia1['minima']);
TrocarTexto(comp_tela, "min2", dia2['minima']);
TrocarTexto(comp_tela, "min3", dia3['minima']);

TrocarTexto(comp_tela, "max1", dia1['maxima']);
TrocarTexto(comp_tela, "max2", dia2['maxima']);
TrocarTexto(comp_tela, "max3", dia3['maxima']);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + dia1['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_tela.layer('icone1').replaceSource(iconeImportado, false);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + dia2['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_tela.layer('icone2').replaceSource(iconeImportado, false);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + dia3['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_tela.layer('icone3').replaceSource(iconeImportado, false);

app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
