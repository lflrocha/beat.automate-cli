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
    var nome_arquivo = "projetos/tvbr_tempo2023_5dias_tarde.aep"
} else {
    var nome_arquivo = "projetos/tvbr_tempo2023_5dias.aep"
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
var dia4 = dados['dia4']
var dia5 = dados['dia5']


var comp_tela = app.project.item(2);
TrocarTexto(comp_tela, "cidade", cidade);

TrocarTexto(comp_tela, "dia1-1", dia1['dia_semana']);
TrocarTexto(comp_tela, "dia1-2", dia2['dia_semana']);
TrocarTexto(comp_tela, "dia1-3", dia3['dia_semana']);
TrocarTexto(comp_tela, "dia1-4", dia4['dia_semana']);
TrocarTexto(comp_tela, "dia1-5", dia5['dia_semana']);

TrocarTexto(comp_tela, "dia2-1", dia1['dia_semana']);
TrocarTexto(comp_tela, "dia2-2", dia2['dia_semana']);
TrocarTexto(comp_tela, "dia2-3", dia3['dia_semana']);
TrocarTexto(comp_tela, "dia2-4", dia4['dia_semana']);
TrocarTexto(comp_tela, "dia2-5", dia5['dia_semana']);

TrocarTexto(comp_tela, "min1", dia1['minima']);
TrocarTexto(comp_tela, "min2", dia2['minima']);
TrocarTexto(comp_tela, "min3", dia3['minima']);
TrocarTexto(comp_tela, "min4", dia4['minima']);
TrocarTexto(comp_tela, "min5", dia5['minima']);

TrocarTexto(comp_tela, "max1", dia1['maxima']);
TrocarTexto(comp_tela, "max2", dia2['maxima']);
TrocarTexto(comp_tela, "max3", dia3['maxima']);
TrocarTexto(comp_tela, "max4", dia4['maxima']);
TrocarTexto(comp_tela, "max5", dia5['maxima']);

TrocarTexto(comp_tela, "chuva1", dia1['chuva']);
TrocarTexto(comp_tela, "chuva2", dia2['chuva']);
TrocarTexto(comp_tela, "chuva3", dia3['chuva']);
TrocarTexto(comp_tela, "chuva4", dia4['chuva']);
TrocarTexto(comp_tela, "chuva5", dia5['chuva']);

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

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + dia4['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_tela.layer('icone4').replaceSource(iconeImportado, false);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + dia5['icone'] + ".mov"));
var iconeImportado = app.project.importFile(importOptions);
comp_tela.layer('icone5').replaceSource(iconeImportado, false);




app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
