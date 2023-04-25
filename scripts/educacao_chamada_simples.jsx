app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";
var _io = new ImportOptions(File(baseFolder + "projetos/educacao_chamada_simples.aep"));
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
var comp_video = app.project.item(3)

alert(dados)

comp_base.layer("Controle").property("sourceText").setValue(dados['canal'])
comp_base.layer("DiaHora1").property("sourceText").setValue(dados['dia_hora'])
comp_base.layer("NomePrograma1A").property("sourceText").setValue(dados['programa'])
comp_base.layer("NomePrograma1").property("sourceText").setValue(dados['programa'])
comp_base.layer("Subtitulo").property("sourceText").setValue(dados['subtitulo'])

comp_base.layer("NomePrograma1B").property("sourceText").setValue(dados['programa'])
comp_base.layer("DiaHora1_Alternativo1").property("sourceText").setValue(dados['dia_hora_alt1'])
comp_base.layer("DiaHora1_Alternativo2").property("sourceText").setValue(dados['dia_hora_alt2'])
comp_base.layer("DiaHora1_Alternativo3").property("sourceText").setValue(dados['dia_hora_alt3'])
comp_base.layer("DiaHora1_Alternativo4").property("sourceText").setValue(dados['dia_hora_alt4'])


var videoLayer = comp_video.layer("Video1")
var importOptionsA = new ImportOptions();
importOptionsA.file = new File(baseFolder + 'temp/'+ dados['video']);
var importedImageA = app.project.importFile(importOptionsA);
videoLayer.replaceSource(importedImageA, false);




app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
