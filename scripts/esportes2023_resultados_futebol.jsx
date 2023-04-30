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
var _io = new ImportOptions(File(baseFolder + "projetos/esportes2023_resultados_futebol.aep"));
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
var txt_subtitulo = dados['subtitulo'];
var telas = dados['jogos'];

comp_1jogo = app.project.item(2);
comp_2jogos = app.project.item(3);
comp_3jogos = app.project.item(4);
comp_4jogos = app.project.item(5);

for (var i = 0; i < telas.length; i++) {

    jogos = telas[i]
    switch (jogos.length) {
      case 1:
        var comp_tela = comp_1jogo.duplicate();
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
    comp_tela.name = "!render_" + i.toString();
    TrocarTexto(comp_tela, "titulo", campeonato);
    TrocarTexto(comp_tela, "subtitulo", txt_subtitulo);

    if (jogos.length > 2) {
        altura = comp_tela.layer("titulo").sourceRectAtTime(5, true).height
        delta = altura - 55

        linha = comp_tela.layer("linha_titulo")
        aux = linha.property("position").value;
        var novo_x = aux[0]
        var novo_y = aux[1] + delta + 10
        linha.property("position").setValue([novo_x, novo_y]);

        subtitulo = comp_tela.layer("subtitulo")
        aux = subtitulo.property("position").value;
        var novo_x = aux[0]
        var novo_y = aux[1] + delta + 20
        subtitulo.transform.yPosition.setValueAtKey(2, novo_y);
    }


    for (var j = 1; j <= jogos.length; j++) {
      nomeTimeA = jogos[j-1]['nome_time1']
      siglaTimeA = jogos[j-1]['sigla_time1']
      placarTimeA = jogos[j-1]['placar_time1']

      nomeTimeB = jogos[j-1]['nome_time2']
      siglaTimeB = jogos[j-1]['sigla_time2']
      placarTimeB = jogos[j-1]['placar_time2']

      TrocarTexto(comp_tela, "J" + j.toString() + "NomeTimeA", nomeTimeA);
      TrocarTexto(comp_tela, "J" + j.toString() + "PlacarTimeA", placarTimeA.toString());

      TrocarTexto(comp_tela, "J" + j.toString() + "NomeTimeB", nomeTimeB);
      TrocarTexto(comp_tela, "J" + j.toString() + "PlacarTimeB", placarTimeB.toString());

      var escudoLayerA = comp_tela.layer("J" + j.toString() + "EscudoTimeA")
      var importOptionsA = new ImportOptions();
      importOptionsA.file = new File(baseFolder + 'arquivos/escudos/'+ siglaTimeA + '.png');
      var importedImageA = app.project.importFile(importOptionsA);
      escudoLayerA.replaceSource(importedImageA, false);

      var escudoLayerB = comp_tela.layer("J" + j.toString() + "EscudoTimeB")
      var importOptionsB = new ImportOptions();
      importOptionsB.file = new File(baseFolder + 'arquivos/escudos/'+ siglaTimeB + '.png');
      var importedImageB = app.project.importFile(importOptionsB);
      escudoLayerB.replaceSource(importedImageB, false);

      if (programa == "Stadium") {
         obj = comp_tela.layer("tarja" + j.toString())
         obj.effect("COR").property("Color").setValue([2/255,67/255,129/255])
      }
      if (programa == "Mundo da Bola") {
         obj = comp_tela.layer("tarja" + j.toString())
         obj.effect("COR").property("Color").setValue([0/255,39/255,37/255])
      }
      if (programa == "Repórter Brasil") {
        obj = comp_tela.layer("tarja" + j.toString())
        obj.effect("COR").property("Color").setValue([2/255,67/255,129/255])
      }

    }
}

app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
