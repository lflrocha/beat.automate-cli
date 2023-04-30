app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";
var _io = new ImportOptions(File(baseFolder + "projetos/educacao_bussola_assista.aep"));
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
var comp_base2 = app.project.item(3)

comp_base.layer("t_nome").property("sourceText").setValue(dados['programa'])
comp_base2.layer("t_nome").property("sourceText").setValue(dados['programa'])
comp_base2.layer("t_controle").property("sourceText").setValue(dados['canal'])


app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
