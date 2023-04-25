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
var _io = new ImportOptions(File(baseFolder + "projetos/esportes2023_tabela_futebol.aep"));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);

// Abre o arquivo JSON
var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
// var caminhoDados = baseFolder + "/temp/tabela.json";
var arquivoJson = new File(caminhoDados)
if (arquivoJson.open("r")) {
  arquivoJson.encoding = "UTF-8";
  var meuJSON = arquivoJson.read();
  var dados = JSON.parse(meuJSON);
  arquivoJson.close();
}


var q1 = [ 25/255, 229/255,  68/255] // Classificacao 1
var q1 = [ 25/255, 229/255,  68/255] // Classificacao 1
var q2 = [236/255, 138/255,   0/255] // Classificacao 2
var q3 = [255/255, 202/255,  40/255] // Classificacao 3
var q4 = [204/255, 204/255, 204/255] // Classificacao 4
var q5 = [217/255,  41/255,  28/255] // Classificacao 5



// "Stadium", "MundodaBola", "Jornalismo"
var programa = dados['programa'];
var campeonato = dados['campeonato_nome'];
var telas = dados['telas'];

comp_base = app.project.item(2);
comp_linha = app.project.item(3);

for (var i = 0; i < telas.length; i++) {

  var comp_tela = comp_base.duplicate();
  comp_tela.layer(programa).property("opacity").setValue(100);
  comp_tela.name = "!render_" + i.toString();
  TrocarTexto(comp_tela, "NCampeonato", campeonato);

  dados_tela = telas[i];
  for (var j = 0; j < dados_tela.length; j++) {

    delta_y = 270 + (j * 70);
    dados_time = dados_tela[j];
    var aux = comp_linha.duplicate();
    aux.layer('bg').effect("Cor_Destaque").property("Color").setValue(eval(dados_time['bg']));
    TrocarTexto(aux, "time", dados_time['time']);
    TrocarTexto(aux, "pos", dados_time['pos'].toString());
    TrocarTexto(aux, "pon", dados_time['pon'].toString());
    TrocarTexto(aux, "jog", dados_time['jog'].toString());
    TrocarTexto(aux, "vit", dados_time['vit'].toString());
    TrocarTexto(aux, "sg", dados_time['sg'].toString());
    linha = comp_tela.layers.add(aux);
    linha.property("position").setValue([865, delta_y]);
    linha.startTime = 0.5 + (j * 0.07);
    linha.name = "time_" + j.toString();
  }
}

app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
