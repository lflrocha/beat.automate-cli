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


var nome_arquivo = "projetos/conasems-congresso2026.aep"

var _io = new ImportOptions(File(baseFolder + nome_arquivo));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);

var comp_tela = app.project.item(2);

var hora = dados['hora'];
var data = dados['data'];
var dia = dados['dia'];
var texto_tipo = dados['texto_tipo'];
var evento = dados['evento'];
var local = dados['local'];

TrocarTexto(comp_tela, "V_HORARIO", hora);
TrocarTexto(comp_tela, "V_DATA", data);
TrocarTexto(comp_tela, "V_DIA", dia);
TrocarTexto(comp_tela, "V_TIPO", texto_tipo);
TrocarTexto(comp_tela, "V_EVENTO", evento);
TrocarTexto(comp_tela, "V_LOCAL", local);


app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
