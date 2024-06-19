app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);


//função trocar texto
function TrocarTexto (nome_comp, nome_layer, novo_texto) {
        var texto = nome_comp.layer(nome_layer);
        texto.property("sourceText").setValue(novo_texto);
}

// Cria novo arquivo
var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";

// Importa projeto para o novo arquivo
var _io = new ImportOptions(File(baseFolder + "projetos/gov2024_onair_tempo.aep"));
if(_io.canImportAs(ImportAsType.PROJECT)){
        _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);


// Abre o arquivo JSON
var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
var scriptFile = new File(caminhoDados);
scriptFile.open('r');
var content = scriptFile.read();
scriptFile.close();
var dados = (new Function( "return " + content ))() ;

var compDados = app.project.item(2)

var compCidade1Hoje = app.project.item(3)
var compCidade1Amanha = app.project.item(4)
var compCidade2Hoje = app.project.item(5)
var compCidade2Amanha = app.project.item(6)
var compCidade3Hoje = app.project.item(7)
var compCidade3Amanha = app.project.item(8)

dados_cidade1 = dados[0]
dados_cidade2 = dados[1]
dados_cidade3 = dados[2]


TrocarTexto(compDados, "T_CIDADE1", dados_cidade1.cidade + '/' + dados_cidade1.uf);
TrocarTexto(compCidade1Hoje, "T_MIN", dados_cidade1.min_hoje + 'º');
TrocarTexto(compCidade1Hoje, "T_MAX", dados_cidade1.max_hoje + 'º');
TrocarTexto(compCidade1Hoje, "T_CHUVA", dados_cidade1.chuva_hoje + '%');
TrocarTexto(compCidade1Amanha, "T_MIN", dados_cidade1.min_amanha + 'º');
TrocarTexto(compCidade1Amanha, "T_MAX", dados_cidade1.max_amanha + 'º');
TrocarTexto(compCidade1Amanha, "T_CHUVA", dados_cidade1.chuva_amanha + '%');
var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/canalgov/tempo/" + dados_cidade1.icone_hoje + ".mov"));
var videoImportado = app.project.importFile(importOptions);
compCidade1Hoje.layer('T_ICONE').replaceSource(videoImportado, false);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/canalgov/tempo/" + dados_cidade1.icone_amanha + ".mov"));
var videoImportado = app.project.importFile(importOptions);
compCidade1Amanha.layer('T_ICONE').replaceSource(videoImportado, false);


TrocarTexto(compDados, "T_CIDADE2", dados_cidade2.cidade + '/' + dados_cidade2.uf);
TrocarTexto(compCidade2Hoje, "T_MIN", dados_cidade2.min_hoje + 'º');
TrocarTexto(compCidade2Hoje, "T_MAX", dados_cidade2.max_hoje + 'º');
TrocarTexto(compCidade2Hoje, "T_CHUVA", dados_cidade2.chuva_hoje + '%');
TrocarTexto(compCidade2Amanha, "T_MIN", dados_cidade2.min_amanha + 'º');
TrocarTexto(compCidade2Amanha, "T_MAX", dados_cidade2.max_amanha + 'º');
TrocarTexto(compCidade2Amanha, "T_CHUVA", dados_cidade2.chuva_amanha + '%');
var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/canalgov/tempo/" + dados_cidade2.icone_hoje + ".mov"));
var videoImportado = app.project.importFile(importOptions);
compCidade2Hoje.layer('T_ICONE').replaceSource(videoImportado, false);
var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/canalgov/tempo/" + dados_cidade2.icone_amanha + ".mov"));
var videoImportado = app.project.importFile(importOptions);
compCidade2Amanha.layer('T_ICONE').replaceSource(videoImportado, false);

TrocarTexto(compDados, "T_CIDADE3", dados_cidade3.cidade + '/' + dados_cidade3.uf);
TrocarTexto(compCidade3Hoje, "T_MIN", dados_cidade3.min_hoje + 'º');
TrocarTexto(compCidade3Hoje, "T_MAX", dados_cidade3.max_hoje + 'º');
TrocarTexto(compCidade3Hoje, "T_CHUVA", dados_cidade3.chuva_hoje + '%');
TrocarTexto(compCidade3Amanha, "T_MIN", dados_cidade3.min_amanha + 'º');
TrocarTexto(compCidade3Amanha, "T_MAX", dados_cidade3.max_amanha + 'º');
TrocarTexto(compCidade3Amanha, "T_CHUVA", dados_cidade3.chuva_amanha + '%');
var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/canalgov/tempo/" + dados_cidade3.icone_hoje + ".mov"));
var videoImportado = app.project.importFile(importOptions);
compCidade3Hoje.layer('T_ICONE').replaceSource(videoImportado, false);
var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/canalgov/tempo/" + dados_cidade3.icone_amanha + ".mov"));
var videoImportado = app.project.importFile(importOptions);
compCidade3Amanha.layer('T_ICONE').replaceSource(videoImportado, false);




app.endSuppressDialogs(false)
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
