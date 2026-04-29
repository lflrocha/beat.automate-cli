app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

function TrocarTexto(nome_comp, nome_layer, novo_texto) {
  // alert(nome_layer);
  var texto = nome_comp.layer(nome_layer);
  texto.property("sourceText").setValue(novo_texto);
}


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


var nome_arquivo = "projetos/conasems_programacao.aep"

var _io = new ImportOptions(File(baseFolder + nome_arquivo));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);

var comp_tela = app.project.item(2);

var programa = dados['programa'];
var dia = dados['dia'];
var hora = dados['hora'];
var textoapoio = dados['textoapoio'];

var diahora = dia + " - " + hora;

var layer_textoalt = comp_tela.layer("V_Temporada");
var layer_diahora = comp_tela.layer("V_Dia_horario");
var layer_diahora_maior = comp_tela.layer("V_Dia_horario_maior");


TrocarTexto(comp_tela, "V_Dia_01", dia);
TrocarTexto(comp_tela, "V_Dia_02", dia);
TrocarTexto(comp_tela, "V_Programa_01", programa);
TrocarTexto(comp_tela, "V_Programa_02", programa);
TrocarTexto(comp_tela, "V_Dia_horario", diahora);
TrocarTexto(comp_tela, "V_Dia_horario_maior", diahora);

if (textoapoio) {
    TrocarTexto(comp_tela, "V_Temporada", textoapoio);
} else {
    layer_textoalt.enabled = false;
    layer_diahora.enabled = false;
    layer_diahora_maior.enabled = true;
}
TrocarTexto(comp_tela, "V_Horario", hora);


var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "temp/" + dados['img1']));
var nova_foto = app.project.importFile(importOptions);
comp_tela.layer('V_Imagem_01').replaceSource(nova_foto, false);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "temp/" + dados['img2']));
var nova_foto = app.project.importFile(importOptions);
comp_tela.layer('V_Imagem_02').replaceSource(nova_foto, false);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "temp/" + dados['img3']));
var nova_foto = app.project.importFile(importOptions);
comp_tela.layer('V_Imagem_03').replaceSource(nova_foto, false);


app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
