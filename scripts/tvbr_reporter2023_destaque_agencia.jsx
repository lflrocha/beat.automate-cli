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

var nome_arquivo = "projetos/tvbr_reporter2023_destaque_agencia_brasil.aep"

var _io = new ImportOptions(File(baseFolder + nome_arquivo));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);

var comp_bg = app.project.item(2)
layer_bg_noite = comp_bg.layer("background-noite")

if (dados['modelo'] == "Tarde") {
  layer_bg_noite.enabled = false;
}


var comp_tela = app.project.item(3);

var editoria = dados['editoria'];
TrocarTexto(comp_tela, "editoria", editoria);

var titulo = dados['titulo'];
TrocarTexto(comp_tela, "titulo", titulo);

var descricao = dados['descricao'];
TrocarTexto(comp_tela, "descricao", descricao);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "temp/" + dados['imagem']));
var nova_foto = app.project.importFile(importOptions);
comp_tela.layer('_img').replaceSource(nova_foto, false);


app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
