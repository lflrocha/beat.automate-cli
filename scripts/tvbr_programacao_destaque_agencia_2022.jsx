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
var _io = new ImportOptions(File(baseFolder + "projetos/tvbr_programacao_destaque_agencia_2022.aep"));
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

var dados_json = []
var dados_noticias = dados['noticias']

for(var i = 0; i < dados_noticias.length; i++) {
    var obj = dados_noticias[i];
    // alert(obj.editoria);

    var compDados = app.project.item(i+3)
    // alert(compDados.name)
    TrocarTexto (compDados, "editoria", obj.editoria)
    TrocarTexto (compDados, "titulo", obj.titulo)
    TrocarTexto (compDados, "descricao", obj.descricao)

    novaImagem = baseFolder + 'temp/' + obj.imagem
    var arquivoImagem = new File(novaImagem)
    app.project.item(i+9).replace(arquivoImagem)
}



// var texto = compDados.layer("_titulo");
// var altura = texto.sourceRectAtTime(1, true).height;
// var delta_h = (220 - altura)/2
// var posicao = texto.property("position").value;
// var novo_x = posicao[0]
// var novo_y = 522 + delta_h
// texto.property("position").setValue([novo_x, novo_y]);
//
//
// TrocarTexto (compDados, "_credito", dados.credito)
//
//
//
//
// // Finaliza e salva
//
app.endSuppressDialogs(false)
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
