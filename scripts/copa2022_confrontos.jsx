app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

// Cria novo arquivo
var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";

// Importa projeto para o novo arquivo
var _io = new ImportOptions(File(baseFolder + "projetos/copa2022_confrontos.aep"));
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
TrocarTexto (compDados, "t_grupo", dados.grupo)
TrocarTexto (compDados, "t_rodada", dados.rodada)

jogo = dados['jogos'][0]

TrocarTexto (compDados, "t_data1", jogo.data_str)
TrocarTexto (compDados, "t_hora1", jogo.hora)

TrocarTexto (compDados, "t_time1_j1", jogo.nome_time1)
TrocarTexto (compDados, "t_bandeira1_j1", jogo.cod_time1)

TrocarTexto (compDados, "t_time2_j1", jogo.nome_time2)
TrocarTexto (compDados, "t_bandeira2_j1", jogo.cod_time2)

if (jogo.placar_time1 != null) {
  TrocarTexto (compDados, "t_placar_time1_j1", jogo.placar_time1)
  TrocarTexto (compDados, "t_placar_time2_j1", jogo.placar_time2)
} else {
  TrocarTexto (compDados, "t_placar_time1_j1", "")
  TrocarTexto (compDados, "t_placar_time2_j1", "")
}

if (jogo.penalti_time1 != null) {
  TrocarTexto (compDados, "t_penalti_time1_j1", jogo.penalti_time1)
  TrocarTexto (compDados, "t_penalti_time2_j1", jogo.penalti_time2)
} else {
  TrocarTexto (compDados, "t_penalti_time1_j1", "")
  TrocarTexto (compDados, "t_penalti_time2_j1", "")
}


jogo = dados['jogos'][1]
TrocarTexto (compDados, "t_data2", jogo.data_str)
TrocarTexto (compDados, "t_hora2", jogo.hora)
TrocarTexto (compDados, "t_time1_j2", jogo.nome_time1)
TrocarTexto (compDados, "t_bandeira1_j2", jogo.cod_time1)
TrocarTexto (compDados, "t_time2_j2", jogo.nome_time2)
TrocarTexto (compDados, "t_bandeira2_j2", jogo.cod_time2)

if (jogo.placar_time1 != null) {
  TrocarTexto (compDados, "t_placar_time1_j2", jogo.placar_time1)
  TrocarTexto (compDados, "t_placar_time2_j2", jogo.placar_time2)
} else {
  TrocarTexto (compDados, "t_placar_time1_j2", "")
  TrocarTexto (compDados, "t_placar_time2_j2", "")
}

if (jogo.penalti_time1 != null) {
  TrocarTexto (compDados, "t_penalti_time1_j2", jogo.penalti_time1)
  TrocarTexto (compDados, "t_penalti_time2_j2", jogo.penalti_time2)
} else {
  TrocarTexto (compDados, "t_penalti_time1_j2", "")
  TrocarTexto (compDados, "t_penalti_time2_j2", "")
}



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
