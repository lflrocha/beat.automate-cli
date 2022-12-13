app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);


//função trocar texto
function TrocarTexto (nome_comp, nome_layer, novo_texto) {
        var texto = nome_comp.layer(nome_layer);
        texto.property("sourceText").setValue(novo_texto);
}

// Cria novo arquivo
var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";

// Importa projeto para o novo arquivo
var _io = new ImportOptions(File(baseFolder + "projetos/tvbr_radios_chamada.aep"));
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

var compDados = app.project.item(2)
TrocarTexto(compDados, "Controle_Radio", dados.emissora)
TrocarTexto(compDados, "NomedaFaixa", dados.nome)
TrocarTexto(compDados, "NomedaFaixa1", dados.nome)
TrocarTexto(compDados, "TextoFaixa", dados.sinopse)
TrocarTexto(compDados, "DiadaSemana", dados.dia)
TrocarTexto(compDados, "Horario", dados.hora)

novoArq = baseFolder + 'temp/' + dados.arq_imagem1
var auxArq = new File(novoArq)
app.project.item(3).replace(auxArq)

novoArq = baseFolder + 'temp/' + dados.arq_imagem2
var auxArq = new File(novoArq)
app.project.item(4).replace(auxArq)

novoArq = baseFolder + 'temp/' + dados.arq_imagem3
var auxArq = new File(novoArq)
app.project.item(5).replace(auxArq)

novoArq = baseFolder + 'temp/' + dados.arq_audio
var auxArq = new File(novoArq)
app.project.item(6).replace(auxArq)



app.endSuppressDialogs(false)
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
