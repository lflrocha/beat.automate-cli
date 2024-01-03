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
var scriptFile = new File(caminhoDados);
scriptFile.open('r');
var content = scriptFile.read();
scriptFile.close();
var dados = (new Function( "return " + content ))() ;


modelo = dados['modelo']
if (modelo == "Tarde") {
    var nome_arquivo = "projetos/tvbr_tempo2023_3dias_2cidades_tarde.aep"
} else {
    var nome_arquivo = "projetos/tvbr_tempo2023_3dias_2cidades.aep"
}

var _io = new ImportOptions(File(baseFolder + nome_arquivo));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);

var cidade1 = dados['cidade1'];
var c1dia1 = dados['c1dia1']
var c1dia2 = dados['c1dia2']
var c1dia3 = dados['c1dia3']

var cidade2 = dados['cidade2'];
var c2dia1 = dados['c2dia1']
var c2dia2 = dados['c2dia2']
var c2dia3 = dados['c2dia3']


var comp_tela = app.project.item(2);
TrocarTexto(comp_tela, "cidade", cidade1);

TrocarTexto(comp_tela, "dia1", c1dia1['dia_semana']);
TrocarTexto(comp_tela, "dia2", c1dia2['dia_semana']);
TrocarTexto(comp_tela, "dia3", c1dia3['dia_semana']);

TrocarTexto(comp_tela, "min1", c1dia1['minima']);
TrocarTexto(comp_tela, "min2", c1dia2['minima']);
TrocarTexto(comp_tela, "min3", c1dia3['minima']);

TrocarTexto(comp_tela, "max1", c1dia1['maxima']);
TrocarTexto(comp_tela, "max2", c1dia2['maxima']);
TrocarTexto(comp_tela, "max3", c1dia3['maxima']);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + c1dia1['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_tela.layer('icone1').replaceSource(iconeImportado, false);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + c1dia2['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_tela.layer('icone2').replaceSource(iconeImportado, false);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + c1dia3['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_tela.layer('icone3').replaceSource(iconeImportado, false);



TrocarTexto(comp_tela, "cidade2", cidade2);

TrocarTexto(comp_tela, "dia4", c2dia1['dia_semana']);
TrocarTexto(comp_tela, "dia5", c2dia2['dia_semana']);
TrocarTexto(comp_tela, "dia6", c2dia3['dia_semana']);

TrocarTexto(comp_tela, "min4", c2dia1['minima']);
TrocarTexto(comp_tela, "min5", c2dia2['minima']);
TrocarTexto(comp_tela, "min6", c2dia3['minima']);

TrocarTexto(comp_tela, "max4", c2dia1['maxima']);
TrocarTexto(comp_tela, "max5", c2dia2['maxima']);
TrocarTexto(comp_tela, "max6", c2dia3['maxima']);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + c2dia1['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_tela.layer('icone4').replaceSource(iconeImportado, false);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + c2dia2['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_tela.layer('icone5').replaceSource(iconeImportado, false);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + c2dia3['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_tela.layer('icone6').replaceSource(iconeImportado, false);




app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
