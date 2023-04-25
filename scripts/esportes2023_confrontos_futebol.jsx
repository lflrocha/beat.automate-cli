app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

function TrocarTexto (nome_comp, nome_layer, novo_texto) {
  var texto = nome_comp.layer(nome_layer);
  texto.property("sourceText").setValue(novo_texto);
}

var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";
var _io = new ImportOptions(File(baseFolder + "projetos/esportes2023_confrontos_futebol.aep"));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);

// Abre o arquivo JSON
var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
// var caminhoDados = baseFolder + "/temp/jogos.json";
var arquivoJson = new File(caminhoDados)
if (arquivoJson.open("r")) {arquivoJson.encoding = "UTF-8";
    var meuJSON = arquivoJson.read();
    var dados = JSON.parse(meuJSON);
    arquivoJson.close();
}

// "Stadium", "MundodaBola", "Jornalismo"
var programa = dados['programa'];
var campeonato = dados['campeonato_nome'];
var campeonato_id = dados['campeonato_id'];
var jogos = dados['jogos'];

comp_2jogos = app.project.item(2);
comp_3jogos = app.project.item(3);
comp_4jogos = app.project.item(4);


var chunkSize = 4;
var telas = 0
for (var i = 0; i < jogos.length; i += chunkSize) {

    telas = telas + 1
    var chunk = jogos.slice(i, i + chunkSize);
    switch (chunk.length) {
      case 1:
        var comp_tela = comp_2jogos.duplicate();
        break;
      case 2:
        var comp_tela = comp_2jogos.duplicate();
        break;
      case 3:
        var comp_tela = comp_3jogos.duplicate();
        break;
      case 4:
        var comp_tela = comp_4jogos.duplicate();
        break;
    }

    comp_tela.layer(programa).property("opacity").setValue(100);
    comp_tela.name = "!render" + telas.toString();
    TrocarTexto(comp_tela, "titulo", campeonato);
    // TrocarTexto(comp_tela, "subtitulo", "Segunda fase");

    for (var j = 1; j <= chunk.length; j++) {
      nomeTimeA = chunk[j-1]['equipes']['mandante']['nome_popular']
      cod_timeA = ""
      placarTimeA = chunk[j-1]['placar_oficial_mandante']
      escudoTimeA = chunk[j-1]['equipes']['mandante']['sigla']

      nomeTimeB = chunk[j-1]['equipes']['visitante']['nome_popular']
      cod_timeB = ""
      placarTimeB = chunk[j-1]['placar_oficial_visitante']
      escudoTimeB = chunk[j-1]['equipes']['visitante']['sigla']

      TrocarTexto(comp_tela, "J" + j.toString() + "NomeTimeA", nomeTimeA);
      // TrocarTexto(aux, "J" + j.toString() + "EscudoTimeA", escudoTimeA);
      TrocarTexto(comp_tela, "J" + j.toString() + "PlacarTimeA", placarTimeA.toString());

      TrocarTexto(comp_tela, "J" + j.toString() + "NomeTimeB", nomeTimeB);
      // TrocarTexto(aux, "J" + j.toString() + "EscudoTimeB", escudoTimeB);
      TrocarTexto(comp_tela, "J" + j.toString() + "PlacarTimeB", placarTimeB.toString());


      var escudoLayerA = comp_tela.layer("J" + j.toString() + "EscudoTimeA")
      var importOptionsA = new ImportOptions();
      importOptionsA.file = new File(baseFolder + 'arquivos/escudos/'+ cod_timeA + '.png');
      var importedImageA = app.project.importFile(importOptionsA);
      escudoLayerA.replaceSource(importedImageA, false);

      var escudoLayerB = comp_tela.layer("J" + j.toString() + "EscudoTimeB")
      var importOptionsB = new ImportOptions();
      importOptionsB.file = new File(baseFolder + 'arquivos/escudos/'+ cod_timeB + '.png');
      var importedImageB = app.project.importFile(importOptionsB);
      escudoLayerB.replaceSource(importedImageB, false);

    }


}

// app.endSuppressDialogs(false);
// app.endUndoGroup();
// app.project.removeUnusedFootage();
// novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
// app.project.save(novoArquivo);
// app.project.close(CloseOptions.SAVE_CHANGES);
