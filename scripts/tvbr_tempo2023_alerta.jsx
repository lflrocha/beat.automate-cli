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
    var nome_arquivo = "projetos/tvbr_tempo2023_alerta_tarde.aep"
} else {
    var nome_arquivo = "projetos/tvbr_tempo2023_alerta.aep"
}

var _io = new ImportOptions(File(baseFolder + nome_arquivo));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);


var titulo = dados['titulo'];
var arquivos = dados['arquivos'];

var comp_tela = app.project.item(2);
TrocarTexto(comp_tela, "titulo", titulo);

for (var i = 0; i < arquivos.length; i++) {
    var arquivo = arquivos[i]
    var numero = i.toString()
    var mapaAlertaLayer = comp_tela.layer("mapa-alerta-"+numero);

    var importOptions = new ImportOptions();
    importOptions.file = new File(arquivo);
    var mapaImportado = app.project.importFile(importOptions);
    mapaAlertaLayer.replaceSource(mapaImportado, false);
}

app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
