app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";

// Abre o arquivo JSON
var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
var scriptFile = new File(caminhoDados);
scriptFile.open('r');
var content = scriptFile.read();
scriptFile.close();
var dados = (new Function( "return " + content ))() ;


modelo = dados['modelo']
if (modelo == "Tarde") {
    var nome_arquivo = "projetos/tvbr_tempo2023_mapa_tarde.aep"
} else {
    var nome_arquivo = "projetos/tvbr_tempo2023_mapa.aep"
}

var _io = new ImportOptions(File(baseFolder + nome_arquivo));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);

var tipo_mapa = dados['tipo_mapa'];
var dados_tempo = dados['dados_tempo'];
var regiao = dados['regiao'];
var arquivo = dados['arquivo'];


if (tipo_mapa == 'tempo') {

  switch (regiao) {
      case "brasil":
          var comp_tela = app.project.item(3);
          break;
      case "norte":
          var comp_tela = app.project.item(7);
          break;
      case "nordeste":
          var comp_tela = app.project.item(9);
          break;
      case "centro-oeste":
          var comp_tela = app.project.item(5);
          break;
      case "sudeste":
          var comp_tela = app.project.item(13);
          break;
      case "sul":
          var comp_tela = app.project.item(11);
          break;
  }

  for (var key in dados_tempo) {
    if ((regiao == "brasil") ||
       ((regiao == "nordeste") && ((key == "AL") || (key == "BA") || (key == "CE") || (key == "MA") || (key == "PB") || (key == "PE") || (key == "PI") || (key == "RN") || (key == "SE"))) ||
       ((regiao == "norte") && ((key == "AC") || (key == "AP") || (key == "AM") || (key == "PA") || (key == "RO") || (key == "RR") || (key == "TO"))) ||
       ((regiao == "centro-oeste") && ((key == "DF") || (key == "GO") || (key == "MT") || (key == "MS"))) ||
       ((regiao == "sudeste") && ((key == "MG") || (key == "SP") || (key == "RJ") || (key == "ES"))) ||
       ((regiao == "sul") && ((key == "RS") || (key == "SC") || (key == "PR")))) {

      layer_uf = comp_tela.layer("T_" + key)
      layer_uf.enabled = true;

      layer_bg = comp_tela.layer("BG_" + key)
      layer_bg.enabled = true;

      var importOptions = new ImportOptions();
      importOptions.file = new File(File(baseFolder + "arquivos/previsao-tempo/icones/azul/" + dados_tempo[key] + ".mov"));
      var iconeImportado = app.project.importFile(importOptions);
      layer_uf.replaceSource(iconeImportado, false);
    }
  }

} else {

  switch (regiao) {
      case "brasil":
          var comp_tela = app.project.item(2);
          break;
      case "norte":
          var comp_tela = app.project.item(6);
          break;
      case "nordeste":
          var comp_tela = app.project.item(8);
          break;
      case "centro-oeste":
          var comp_tela = app.project.item(4);
          break;
      case "sudeste":
          var comp_tela = app.project.item(12);
          break;
      case "sul":
          var comp_tela = app.project.item(10);
          break;
  }

  for (var key in dados_tempo) {

    if ((regiao == "brasil") ||
       ((regiao == "nordeste") && ((key == "AL") || (key == "BA") || (key == "CE") || (key == "MA") || (key == "PB") || (key == "PE") || (key == "PI") || (key == "RN") || (key == "SE"))) ||
       ((regiao == "norte") && ((key == "AC") || (key == "AP") || (key == "AM") || (key == "PA") || (key == "RO") || (key == "RR") || (key == "TO"))) ||
       ((regiao == "centro-oeste") && ((key == "DF") || (key == "GO") || (key == "MT") || (key == "MS"))) ||
       ((regiao == "sudeste") && ((key == "MG") || (key == "SP") || (key == "RJ") || (key == "ES"))) ||
       ((regiao == "sul") && ((key == "RS") || (key == "SC") || (key == "PR")))) {

      layer_uf = comp_tela.layer("T_" + key)
      layer_uf.enabled = true;
      layer_uf.property("sourceText").setValue(dados_tempo[key]);

      layer_bg = comp_tela.layer("BG_" + key)
      layer_bg.enabled = true;

    }
  }
}

var importOptions = new ImportOptions();
importOptions.file = new File(arquivo);
var mapaImportado = app.project.importFile(importOptions);
var mapaLayer = comp_tela.layer("T_MAPA");
mapaLayer.replaceSource(mapaImportado, false);


app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
