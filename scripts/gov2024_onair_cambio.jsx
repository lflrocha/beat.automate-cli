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
var _io = new ImportOptions(File(baseFolder + "projetos/gov2024_onair_cambio.aep"));
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

var compDados = app.project.item(2)

TrocarTexto (compDados, "T_DOLAR_DATA", dados.data)
TrocarTexto (compDados, "T_DOLAR_COMPRA", dados.dolar_compra.substring(0, 2))
TrocarTexto (compDados, "T_DOLAR_COMPRA2", dados.dolar_compra.substring(2))
TrocarTexto (compDados, "T_DOLAR_VENDA", dados.dolar_venda.substring(0, 2))
TrocarTexto (compDados, "T_DOLAR_VENDA2", dados.dolar_venda.substring(2))
TrocarTexto (compDados, "T_EURO_DATA", dados.data)
TrocarTexto (compDados, "T_EURO_COMPRA", dados.euro_compra.substring(0, 2))
TrocarTexto (compDados, "T_EURO_COMPRA2", dados.euro_compra.substring(2))
TrocarTexto (compDados, "T_EURO_VENDA", dados.euro_venda.substring(0, 2))
TrocarTexto (compDados, "T_EURO_VENDA2", dados.euro_venda.substring(2))


app.endSuppressDialogs(false)
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
