app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

// Cria novo arquivo
var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";

// Importa projeto para o novo arquivo
var _io = new ImportOptions(File(baseFolder + "projetos/redes_tiktok_vertical.aep"));
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
var texto1 = dados.texto
var arq_midia = dados.arquivo
var arq_bg = dados.arq_background

var compDados = app.project.item(2)
var compVideo = app.project.item(3)
var arqVideo = app.project.item(4)
var arqBG = app.project.item(5)


TrocarTexto(compDados, "txt", texto1)

novaImagem = baseFolder + 'temp/' + arq_midia
var arquivoImagem = new File(novaImagem)
arqVideo.replace(arquivoImagem)

novaImagem = baseFolder + 'temp/' + arq_bg
var arquivoImagem = new File(novaImagem)
arqBG.replace(arquivoImagem)


var duracao = arqVideo.duration
if (duracao < 10) {
  duracao = 10
}

compDados.duration = duracao
compVideo.duration = duracao



//função trocar texto
function TrocarTexto (nome_comp, nome_layer, novo_texto) {
        var texto = nome_comp.layer(nome_layer);
        texto.property("sourceText").setValue(novo_texto);
}

// Finaliza e salva
app.endSuppressDialogs(false)
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
