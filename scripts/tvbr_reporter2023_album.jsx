app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

function TrocarTexto(nome_comp, nome_layer, novo_texto) {
  var layer = nome_comp.layer(nome_layer);
  layer.property("sourceText").setValue(novo_texto);
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
    var nome_arquivo = "projetos/tvbr_reporter2023_album.aep"
} else {
    var nome_arquivo = "projetos/tvbr_reporter2023_album.aep"
}

var _io = new ImportOptions(File(baseFolder + nome_arquivo));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);


var fotos = dados['fotos'];
var comp_tela = app.project.item(2);






app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
