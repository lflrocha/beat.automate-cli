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
var _io = new ImportOptions(File(baseFolder + "projetos/gov2024_onair_bussola2.aep"));
if(_io.canImportAs(ImportAsType.PROJECT)){
        _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);


// Abre o arquivo JSON
var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
var scriptFile = new File(caminhoDados);
scriptFile.open('r');
var content = scriptFile.read();
scriptFile.close();
var dados = (new Function( "return " + content ))() ;


var compDados = app.project.item(3)
TrocarTexto(compDados, "t_programa", dados.programa_nome1)
TrocarTexto(compDados, "t_hora", dados.horario_texto1)

layer_aovivo = compDados.layer("b_ao_vivo")
if (dados.aovivo1 == false) {
  layer_aovivo.enabled = false;
}

programa_id = dados.programa_id1
programa_id = "video"
var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/canalgov/programas/" + programa_id + "_434x669.mp4"));
var videoImportado = app.project.importFile(importOptions);
compDados.layer('a_video').replaceSource(videoImportado, false);



var compDados = app.project.item(4)
TrocarTexto(compDados, "t_programa", dados.programa_nome2)
TrocarTexto(compDados, "t_hora", dados.horario_texto2)

layer_aovivo = compDados.layer("b_ao_vivo")
if (dados.aovivo2 == false) {
  layer_aovivo.enabled = false;
}

programa_id = dados.programa_id2
programa_id = "video"
var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "arquivos/canalgov/programas/" + programa_id + "_434x669.mp4"));
var videoImportado = app.project.importFile(importOptions);
compDados.layer('a_video').replaceSource(videoImportado, false);


app.endSuppressDialogs(false)
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
