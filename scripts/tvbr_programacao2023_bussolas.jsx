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
var _io = new ImportOptions(File(baseFolder + "projetos/tvbr_programacao2023_bussolas.aep"));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);

// Abre o arquivo JSON
var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
var arquivoJson = new File(caminhoDados)
if (arquivoJson.open("r")) {arquivoJson.encoding = "UTF-8";
    var meuJSON = arquivoJson.read();
    var dados = JSON.parse(meuJSON);
    arquivoJson.close();
}

var programa = dados['programa'];
var modelo = dados['modelo'];



var comp_tela = app.project.item(2);
var layer_modelo = comp_tela.layer("T_CONTROLE");
layer_modelo.property("sourceText").setValue(modelo);

var layer_texto = comp_tela.layer("T_PROGRAMA");
layer_texto.property("sourceText").setValue(programa);
var largura = layer_texto.sourceRectAtTime(90, true).width;
var textoProp = layer_texto.property("Source Text");
var textoDocument = textoProp.value;

tamFonte = 160
while (largura > 1400) {
    tamFonte = tamFonte - 2
    textoDocument.fontSize = tamFonte;
    textoProp.setValue(textoDocument);
    largura = layer_texto.sourceRectAtTime(90, true).width;
}

var altura = layer_texto.sourceRectAtTime(90, true).height;
if (altura < 150) {
  posicao = layer_texto.property("position").value;
  layer_texto.property("position").setValueAtTime(90, [posicao[0], 85]);
}



var comp_tela = app.project.item(3);
var layer_modelo = comp_tela.layer("T_CONTROLE");
layer_modelo.property("sourceText").setValue(modelo);

var layer_texto = comp_tela.layer("T_PROGRAMA");
layer_texto.property("sourceText").setValue(programa);
var textoProp = layer_texto.property("Source Text");
var textoDocument = textoProp.value;
textoDocument.fontSize = tamFonte;
textoProp.setValue(textoDocument);

var altura = layer_texto.sourceRectAtTime(125, true).height;
if (altura < 150) {
  posicao = layer_texto.property("position").value;
  layer_texto.property("position").setValueAtTime(125, [posicao[0], 85]);
}


// textoDocument.fontSize = 40; // Tamanho da fonte desejado em pixels
//   textoProp.setValue(textoDocument);

// var tam_fonte = layer_texto.text.fontSize


// while (largura > 1400) {
//     tam_fonte = layer_texto.text.fontSize
//     tam_fonte = tam_fonte - 2
//     // var largura = texto.sourceRectAtTime(1, true).width;
// }

// text.fontSize = 40
// var comp_tela = app.project.item(3);
// TrocarTexto(comp_tela, "T_PROGRAMA", programa);


app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
