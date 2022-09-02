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
var _io = new ImportOptions(File(baseFolder + "projetos/tvbr_eleicoes2022_agenda.aep"));
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
var compDados = app.project.item(2)

TrocarTexto (compDados, "Cargo", dados.cargo)
TrocarTexto (compDados, "Data", dados.data)
TrocarTexto (compDados, "Nome", dados.nome)
TrocarTexto (compDados, "Partido", dados.partido)

TrocarTexto (compDados, "Hora1", dados.turno1)
TrocarTexto (compDados, "Hora6", dados.turno6)

// if (dados.turno1 != "") {
//   TrocarTexto (compDados, "Hora1", dados.turno1)
// } else {
//   var linha = compDados.layer("linha1");
//   var posicao = linha.property("position").value;
//   var novo_x = posicao[0]
//   var novo_y = posicao[1] - 30
//   linha.property("position").setValue([novo_x, novo_y]);
// }

if (dados.turno2 != "") {
  TrocarTexto (compDados, "Hora2", dados.turno2)
} else {
  var linha = compDados.layer("linha2");
  var posicao = linha.property("position").value;
  var novo_x = posicao[0]
  var novo_y = posicao[1] - 30
  linha.property("position").setValue([novo_x, novo_y]);
}

if (dados.turno3 != "") {
  TrocarTexto (compDados, "Hora3", dados.turno3)
} else {
  var linha = compDados.layer("linha3");
  var posicao = linha.property("position").value;
  var novo_x = posicao[0]
  var novo_y = posicao[1] - 30
  linha.property("position").setValue([novo_x, novo_y]);
}

if (dados.turno4 != "") {
  TrocarTexto (compDados, "Hora4", dados.turno4)
} else {
  var linha = compDados.layer("linha4");
  var posicao = linha.property("position").value;
  var novo_x = posicao[0]
  var novo_y = posicao[1] - 30
  linha.property("position").setValue([novo_x, novo_y]);
}

if (dados.turno5 != "") {
  TrocarTexto (compDados, "Hora5", dados.turno5)
} else {
  var linha = compDados.layer("linha5");
  var posicao = linha.property("position").value;
  var novo_x = posicao[0]
  var novo_y = posicao[1] - 30
  linha.property("position").setValue([novo_x, novo_y]);
}

if (dados.turno6 != "") {
  TrocarTexto (compDados, "Hora6", dados.turno6)
} else {
  var linha = compDados.layer("linha6");
  var posicao = linha.property("position").value;
  var novo_x = posicao[0]
  var novo_y = posicao[1] - 30
  linha.property("position").setValue([novo_x, novo_y]);
}


TrocarTexto (compDados, "Info1L1", dados.linha1)
TrocarTexto (compDados, "Info2L1", dados.linha2)
TrocarTexto (compDados, "Info3L1", dados.linha3)
TrocarTexto (compDados, "Info4L1", dados.linha4)
TrocarTexto (compDados, "Info5L1", dados.linha5)
TrocarTexto (compDados, "Info6L1", dados.linha6)

novaImagem = baseFolder + 'temp/' + dados.foto_arquivo
var arquivoImagem = new File(novaImagem)
app.project.item(3).replace(arquivoImagem)


app.endSuppressDialogs(false)
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
