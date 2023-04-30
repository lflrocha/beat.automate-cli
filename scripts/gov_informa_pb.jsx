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
var _io = new ImportOptions(File(baseFolder + "projetos/gov_informa_pb.aep"));
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

TrocarTexto (compDados, "titulo", dados.titulo)
TrocarTexto (compDados, "texto", dados.texto)
TrocarTexto (compDados, "fonte", dados.fonte)

novaImagem = baseFolder + 'temp/' + dados.foto_arquivo
var arquivoImagem = new File(novaImagem)
app.project.item(3).replace(arquivoImagem)


var texto = compDados.layer("texto");
var altura = texto.sourceRectAtTime(10, true).height;
alert(altura)
var posicao = texto.property("position").value;
var novo_x = posicao[0]
var novo_y = 1017 - altura
texto.property("position").setValue([novo_x, novo_y]);

var titulo = compDados.layer("titulo");
var posicao = titulo.property("position").value;
var novo_x = posicao[0]
var novo_y = 757 - altura
titulo.property("position").setValue([novo_x, novo_y]);

app.endSuppressDialogs(false)
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
