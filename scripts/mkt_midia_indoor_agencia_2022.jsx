app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);


// Cria novo arquivo
var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";


// Importa projeto para o novo arquivo
var _io = new ImportOptions(File(baseFolder + "projetos/mkt_midia_indoor_agencia_2022.aep"));
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
        var dados = JSON.parse(meuJSON)
        arquivoJson.close();
}


// Define as variáveis a partir dos dados do JSON
var editoria = dados.editoria
var titulo = dados.titulo
var imagem = dados.imagem
var credito = dados.credito


//função trocar texto
function TrocarTexto (nome_comp, nome_layer, novo_texto) {
        var texto = nome_comp.layer(nome_layer);
        texto.property("sourceText").setValue(novo_texto);

}

// texto1 = effect("Layer Control")("Layer").sourceRectAtTime();
// texto2 = effect("Layer Control 2")("Layer").sourceRectAtTime();
// ScaleX = effect("OffSet Horizontal")("Slider");
// ScaleY = effect("Altura")("Slider");
// [texto1.width + ScaleX, ScaleY]


// Define a variavel comp
// parâmetro de item é a ordem em que a comp está
// no projeto

var compDados = app.project.item(2)
TrocarTexto (compDados, "_titulo", dados.titulo)

var texto = compDados.layer("_titulo");
var altura = texto.sourceRectAtTime(1, true).height;
var delta_h = (220 - altura)/2
var posicao = texto.property("position").value;
var novo_x = posicao[0]
var novo_y = 522 + delta_h
texto.property("position").setValue([novo_x, novo_y]);
TrocarTexto (compDados, "_credito", dados.credito)


var compDados = app.project.item(3)
TrocarTexto (compDados, "_titulo", dados.titulo)

var texto = compDados.layer("_titulo");
var altura = texto.sourceRectAtTime(1, true).height;
var delta_h = (670 - altura)/2
var posicao = texto.property("position").value;
var novo_x = posicao[0]
var novo_y = 500 + delta_h
texto.property("position").setValue([novo_x, novo_y]);
TrocarTexto (compDados, "_credito", dados.credito)



// Importa a nova imagem e substitui uma existente
novaImagem = baseFolder + 'temp/' + imagem
var arquivoImagem = new File(novaImagem)
app.project.item(4).replace(arquivoImagem)



// Finaliza e salva

app.endSuppressDialogs(false)
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
