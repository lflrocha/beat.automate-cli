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
var arquivoJson = new File(caminhoDados)
if (arquivoJson.open("r")) {arquivoJson.encoding = "UTF-8";
    var meuJSON = arquivoJson.read();
    var dados = JSON.parse(meuJSON);
    arquivoJson.close();
}

modelo = dados['modelo']
if (modelo == "Tarde") {
    var nome_arquivo = "projetos/tvbr_reporter2023_lista_tarde.aep"
} else {
    var nome_arquivo = "projetos/tvbr_reporter2023_lista.aep"
}

var _io = new ImportOptions(File(baseFolder + nome_arquivo));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);


var titulo = dados['titulo'];
var subtitulo = dados['subtitulo'];
var item1 = dados['item1'];
var item2 = dados['item2'];
var item3 = dados['item3'];
var item4 = dados['item4'];
var fonte = dados['fonte'];

var comp_tela = app.project.item(2);

TrocarTexto(comp_tela, "T_TITULO", titulo);
TrocarTexto(comp_tela, "T_SUBTITULO", subtitulo);
TrocarTexto(comp_tela, "T_TEXTO1", item1);

TrocarTexto(comp_tela, "T_FONTE", fonte);

if (item2.length > 0) {
    TrocarTexto(comp_tela, "T_TEXTO2", item2);
    layer_texto = comp_tela.layer("T_TEXTO2")
    layer_texto.enabled = true;

    layer_bullet = comp_tela.layer("T_BULLET2")
    layer_bullet.enabled = true;
    layer_bg = comp_tela.layer("T_BG_BULLET2")
    layer_bg.enabled = true;
    layer_linha = comp_tela.layer("T_LINHA2")
    layer_linha.enabled = true;
}

if (item3.length > 0) {
    TrocarTexto(comp_tela, "T_TEXTO3", item3);
    layer_texto = comp_tela.layer("T_TEXTO3")
    layer_texto.enabled = true;

    layer_bullet = comp_tela.layer("T_BULLET3")
    layer_bullet.enabled = true;
    layer_bg = comp_tela.layer("T_BG_BULLET3")
    layer_bg.enabled = true;
    layer_linha = comp_tela.layer("T_LINHA3")
    layer_linha.enabled = true;
} else {
  TrocarTexto(comp_tela, "T_TEXTO3", "");
}

if (item4.length > 0) {
    TrocarTexto(comp_tela, "T_TEXTO4", item4);
    layer_texto = comp_tela.layer("T_TEXTO4")
    layer_texto.enabled = true;

    layer_bullet = comp_tela.layer("T_BULLET4")
    layer_bullet.enabled = true;
    layer_bg = comp_tela.layer("T_BG_BULLET4")
    layer_bg.enabled = true;
} else {
  TrocarTexto(comp_tela, "T_TEXTO4", "");
}




app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
