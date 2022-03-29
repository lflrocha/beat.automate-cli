app.project.close(CloseOptions.DO_NOT_SAVE_CHANGES);
app.beginSuppressDialogs()
app.setSavePreferencesOnQuit(false);

//função trocar texto
function TrocarTexto (nome_comp, nome_layer, novo_texto) {
        var texto = nome_comp.layer(nome_layer)
        texto.property("sourceText").setValue(novo_texto)
}

// Cria novo arquivo
var arqScript = new File($.fileName);
var nomeProjeto = arqScript.name.split(".")[0];
var baseFolder = arqScript.parent.path + "/";

// Importa projeto para o novo arquivo
var _io = new ImportOptions(File(baseFolder + "projetos/tvbr_programacao_chamadas_2022.aep"));
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


// Define as variáveis a partir dos dados do JSON
var dia = dados.dia
var hora = dados.hora
var programa = dados.programa

for(var x = 1; x <= 7; x++) {
        var compDados = app.project.item(x + 1)
        TrocarTexto(compDados, "Hora", hora);
        TrocarTexto(compDados, "NomeProgramaLinha", programa);
        if ((x == 1) || (x == 3) || (x == 5)) {
                TrocarTexto(compDados, "Dia", dia);
        }

        if ((x == 1) || (x == 2)) {
          var texto = compDados.layer("NomeProgramaLinha");
          var altura = texto.sourceRectAtTime(80, true).height;
          if (altura < 100) {
            var posicao = texto.property("position").value;
            var novo_x = posicao[0]
            var novo_y = posicao[1] + 87
            texto.property("position").setValueAtTime(0, [novo_x, novo_y]);
            texto.property("position").setValueAtKey(2, [novo_x, novo_y]);
            texto.property("position").setValueAtKey(3, [novo_x, novo_y]);
          }
        }

        if ((x == 3) || (x == 4)) {
          var texto = compDados.layer("NomeProgramaLinha");
          var altura = texto.sourceRectAtTime(80, true).height;
          if (altura < 100) {
            var posicao = texto.property("position").value;
            var novo_x = posicao[0]
            var novo_y = posicao[1] + 105
            texto.property("position").setValueAtTime(0, [novo_x, novo_y]);
            texto.property("position").setValueAtKey(2, [novo_x, novo_y]);
            texto.property("position").setValueAtKey(3, [novo_x, novo_y]);
          }
        }

        if ((x == 5) || (x == 6) || (x == 7)) {
          var texto = compDados.layer("NomeProgramaLinha");
          var altura = texto.sourceRectAtTime(80, true).height;
          if (altura < 60) {
            var posicao = texto.property("position").value;
            var novo_x = posicao[0]
            var novo_y = posicao[1] + 66
            texto.property("position").setValueAtTime(0, [novo_x, novo_y]);
            texto.property("position").setValueAtKey(2, [novo_x, novo_y]);
            texto.property("position").setValueAtKey(3, [novo_x, novo_y]);
          }
        }
}

// Finaliza e salva
app.endSuppressDialogs(false)
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
