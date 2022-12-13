app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

// Cria novo arquivo
var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";

// Importa projeto para o novo arquivo
var _io = new ImportOptions(File(baseFolder + "projetos/mkt_midia_indoor_tvbrasil_2022.aep"));
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
var texto1 = dados.texto1
var texto2 = dados.texto2
var arq_qrcode = dados.arq_qrcode
var arq_video = dados.arq_video


var compDados = app.project.item(2)
TrocarTexto(compDados, "texto1", texto1)
TrocarTexto(compDados, "texto2", texto2)

novaImagem = baseFolder + 'temp/' + arq_qrcode
var arquivoImagem = new File(novaImagem)
app.project.item(3).replace(arquivoImagem)

novaImagem = baseFolder + 'temp/' + arq_video
var arquivoImagem = new File(novaImagem)
app.project.item(4).replace(arquivoImagem)

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
