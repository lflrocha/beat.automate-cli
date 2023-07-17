app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

function TrocarTexto(nome_comp, nome_layer, novo_texto) {
  var texto = nome_comp.layer(nome_layer);
  texto.property("sourceText").setValue(novo_texto);
}


var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";

// Abre o arquivo JSON
var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
var arquivoJson = new File(caminhoDados)
if (arquivoJson.open("r")) {arquivoJson.encoding = "UTF-8";
    var meuJSON = arquivoJson.read();
    var dados = JSON.parse(meuJSON);
    arquivoJson.close();
}

modelo = dados['modelo']
if (modelo == "Tarde") {
    var nome_arquivo = "projetos/tvbr_reporter2023_focus_tarde.aep"
} else {
    var nome_arquivo = "projetos/tvbr_reporter2023_focus.aep"
}

var _io = new ImportOptions(File(baseFolder + nome_arquivo));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);
var comp_tela = app.project.item(2);


var data = dados['data'];
TrocarTexto(comp_tela, "DATA", data);

var t_ipca_hoje = dados['ipca_hoje'];
var t_ipca_1_semana = dados['ipca_1semana'];
var t_ipca_4_semanas = dados['ipca_4semanas'];
TrocarTexto(comp_tela, "T_IPCA_HOJE", t_ipca_hoje);
TrocarTexto(comp_tela, "T_IPCA_1_SEMANA", t_ipca_1_semana);
TrocarTexto(comp_tela, "T_IPCA_4_SEMANAS", t_ipca_4_semanas);

var t_pib_hoje = dados['pib_hoje'];
var t_pib_1_semana = dados['pib_1semana'];
var t_pib_4_semanas = dados['pib_4semanas'];
TrocarTexto(comp_tela, "T_PIB_HOJE", t_pib_hoje);
TrocarTexto(comp_tela, "T_PIB_1_SEMANA", t_pib_1_semana);
TrocarTexto(comp_tela, "T_PIB_4_SEMANAS", t_pib_4_semanas);

var t_dolar_hoje = dados['dolar_hoje'];
var t_dolar_1_semana = dados['dolar_1semana'];
var t_dolar_4_semanas = dados['dolar_4semanas'];
TrocarTexto(comp_tela, "T_DOLAR_HOJE", t_dolar_hoje);
TrocarTexto(comp_tela, "T_DOLAR_1_SEMANA", t_dolar_1_semana);
TrocarTexto(comp_tela, "T_DOLAR_4_SEMANAS", t_dolar_4_semanas);

var t_selic_hoje = dados['selic_hoje'];
var t_selic_1_semana = dados['selic_1semana'];
var t_selic_4_semanas = dados['selic_4semanas'];
TrocarTexto(comp_tela, "T_SELIC_HOJE", t_selic_hoje);
TrocarTexto(comp_tela, "T_SELIC_1_SEMANA", t_selic_1_semana);
TrocarTexto(comp_tela, "T_SELIC_4_SEMANAS", t_selic_4_semanas);

app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
