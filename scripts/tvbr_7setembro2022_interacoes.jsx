app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

// Cria novo arquivo
var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";

// Importa projeto para o novo arquivo
var _io = new ImportOptions(File(baseFolder + "projetos/tvbr_7setembro2022_interacoes.aep"));
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
var rede = dados.rede
var nome = dados.nome
var cidade = dados.cidade
var imagem = dados.foto_arquivo

//função trocar texto
function TrocarTexto (nome_comp, nome_layer, novo_texto) {
        var texto = nome_comp.layer(nome_layer);
        texto.property("sourceText").setValue(novo_texto);
}

var compDados = app.project.item(2)
TrocarTexto(compDados, "Logo", dados.rede)
TrocarTexto(compDados, "perfil", dados.nome)
TrocarTexto(compDados, "local", dados.cidade)

novaImagem = baseFolder + 'temp/' + imagem
var arquivoImagem = new File(novaImagem)
app.project.item(8).replace(arquivoImagem)
var compFoto = app.project.item(6)

var compArquivo = app.project.item(8)
var duracao = compArquivo.duration

compDados.duration = duracao + 2

h = compFoto.layer("foto").height
w = compFoto.layer("foto").width

reduzir1 = (800 / h)
reduzir2 = (1270 / w)

if (reduzir1 < reduzir2) {
  reduzir = reduzir1
} else {
  reduzir = reduzir2
}
reduzir_prop = reduzir * 100
compFoto.layer("foto").property("scale").setValue([reduzir_prop, reduzir_prop])

h1 = h * reduzir
w1 = w * reduzir
var bordaFoto = compDados.layer("fotoBorda");
bordaFoto.property("Contents").property("Rectangle 1").property("Contents").property("Rectangle Path 1").property("Size").setValue([w1+10, h1+10])

// Finaliza e salva
app.endSuppressDialogs(false)
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
