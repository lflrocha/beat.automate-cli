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



var nome_arquivo = "projetos/tvbr_reporter2023_album.aep"

var _io = new ImportOptions(File(baseFolder + nome_arquivo));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);

var fotos = dados['fotos'];
var comp_tela = app.project.item(2);

var modelo = dados['modelo'];

layer_bg_tarde = comp_tela.layer("background_rbt");
if (dados['modelo'] == "Tarde") {
  layer_bg_tarde.enabled = true;
}

for (i = 0; i < fotos.length; i++) {
    foto = fotos[i][0];
    legenda = fotos[i][1];
    indice = i + 1;
    // alert(foto);
    var importOptions = new ImportOptions();
    importOptions.file = new File(File(baseFolder + "temp/" + foto));
    var fotoImportada = app.project.importFile(importOptions);
    aux = 'layerFoto'+indice
    comp_tela.layer(aux).replaceSource(fotoImportada, false);
    aux2 = 'layerLegenda' + indice
    TrocarTexto (comp_tela, aux2, legenda)

}


comp_tela.duration = fotos.length * 6


app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
