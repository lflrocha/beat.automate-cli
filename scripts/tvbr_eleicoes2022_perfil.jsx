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
var _io = new ImportOptions(File(baseFolder + "projetos/tvbr_eleicoes2022_perfil.aep"));
if(_io.canImportAs(ImportAsType.PROJECT)){
        _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);


// Abre o arquivo JSON
// var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
var arquivoJson = new File(caminhoDados)
if (arquivoJson.open("r")) {
        arquivoJson.encoding = "UTF-8";
        var meuJSON = arquivoJson.read();
        var dados = JSON.parse(meuJSON)
        arquivoJson.close();
}


// Define as variáveis a partir dos dados do JSON
var compDados = app.project.item(2)

TrocarTexto (compDados, "cargo", dados.cargo)
TrocarTexto (compDados, "nome", dados.nome)
TrocarTexto (compDados, "partido", dados.partido)

if (dados.estado != "Brasil") {
  TrocarTexto (compDados, "estado", dados.estado)
} else {
  TrocarTexto (compDados, "estado", "")
}

TrocarTexto (compDados, "naturalidade", dados.naturalidade)
TrocarTexto (compDados, "idade", dados.idade)
TrocarTexto (compDados, "profissao", dados.profissao)
TrocarTexto (compDados, "perfil", dados.perfil)

novaImagem = dados.foto
var arquivoImagem = new File(novaImagem)
app.project.item(3).replace(arquivoImagem)


// h = compDados.layer("nome").height
var altura = compDados.layer("nome").sourceRectAtTime(1, true).height;
var delta_h = altura - 36
// alert(altura)
// alert(delta_h)

var posicao = compDados.layer("partido").property("position").value;
var novo_x = posicao[0]
var novo_y = posicao[1] + delta_h
compDados.layer("partido").property("position").setValue([novo_x, novo_y]);


app.endSuppressDialogs(false)
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
