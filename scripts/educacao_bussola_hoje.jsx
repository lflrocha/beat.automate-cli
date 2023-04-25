app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";
var _io = new ImportOptions(File(baseFolder + "projetos/educacao_bussola_hoje.aep"));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);

// Abre o arquivo JSON
var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
var arquivoJson = new File(caminhoDados)
if (arquivoJson.open("r")) {
  arquivoJson.encoding = "UTF-8";
  var meuJSON = arquivoJson.read();
  var dados = JSON.parse(meuJSON);
  arquivoJson.close();
}

var comp_base = app.project.item(2)

comp_base.layer("Hora1").property("sourceText").setValue(dados['hora1'])
comp_base.layer("Hora2").property("sourceText").setValue(dados['hora2'])
comp_base.layer("Hora3").property("sourceText").setValue(dados['hora3'])
comp_base.layer("Hora4").property("sourceText").setValue(dados['hora4'])
comp_base.layer("Hora5").property("sourceText").setValue(dados['hora5'])

comp_base.layer("NomePrograma1").property("sourceText").setValue(dados['programa1'])
comp_base.layer("NomePrograma2").property("sourceText").setValue(dados['programa2'])
comp_base.layer("NomePrograma3").property("sourceText").setValue(dados['programa3'])
comp_base.layer("NomePrograma4").property("sourceText").setValue(dados['programa4'])
comp_base.layer("NomePrograma5").property("sourceText").setValue(dados['programa5'])


app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
