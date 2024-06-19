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
var _io = new ImportOptions(File(baseFolder + "projetos/gov2024_onair_horarioalternativo.aep"));
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


var compHorarios = app.project.item(2)
TrocarTexto (compHorarios, "t_hora1", dados.horario_texto1)
TrocarTexto (compHorarios, "t_hora2", dados.horario_texto2)

if (dados.horario_id3 !== "selecione") {
   TrocarTexto (compHorarios, "t_hora3", dados.horario_texto3)
 } else {
   b_horario3 = compHorarios.layer("b_horario3")
   b_horario3.enabled = false;
   t_hora3 = compHorarios.layer("t_hora3")
   t_hora3.enabled = false;
}



var compDados = app.project.item(3)

TrocarTexto (compDados, "t_programa", dados.programa_nome)

// layer_aovivo = compDados.layer("b_ao_vivo")
// if (dados.aovivo == false) {
//   layer_aovivo.enabled = false;
// }

programa_id = dados.programa_id
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
