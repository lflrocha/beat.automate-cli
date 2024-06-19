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
var _io = new ImportOptions(File(baseFolder + "projetos/gov2024_onair_citacao.aep"));
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
var dados = (new Function( "return " + content ))();


var compDados = app.project.item(2);
TrocarTexto(compDados, "T_CREDITO", dados.cargo);
TrocarTexto(compDados, "T_NOME", dados.nome);
TrocarTexto(compDados, "T_TEXTO_LONGO", dados.texto);
var textRect = compDados.layer('T_TEXTO_LONGO').sourceRectAtTime(7, false);
var textHeight = textRect.height;

var currentPositionT = compDados.layer('T_TEXTO_LONGO').property("Position").value;
var currentPositionA = compDados.layer('P_ASPAS_LONGO').property("Position").value;



var textProp = compDados.layer('T_TEXTO_LONGO').property("Source Text");
var textDocument = textProp.value;
var increaseAmount = 9; // Set the amount to increase the font size
textDocument.fontSize += increaseAmount;

if (textHeight < 60) {
  var newPositionT = [currentPositionT[0], currentPositionT[1] + 200];
  var newPositionA = [currentPositionA[0], currentPositionA[1] + 200];
  textProp.setValue(textDocument);
  compDados.layer('T_TEXTO_LONGO').property("Position").setValue(newPositionT)
  compDados.layer('P_ASPAS_LONGO').property("Position").setValue(newPositionA)
}

if (textHeight >= 60 && textHeight < 120) {
    var newPositionT = [currentPositionT[0], currentPositionT[1] + 150];
    var newPositionA = [currentPositionA[0], currentPositionA[1] + 150];
    textProp.setValue(textDocument);
    compDados.layer('T_TEXTO_LONGO').property("Position").setValue(newPositionT)
    compDados.layer('P_ASPAS_LONGO').property("Position").setValue(newPositionA)
}

if (textHeight >= 120 && textHeight < 180) {
    var newPositionT = [currentPositionT[0], currentPositionT[1] + 100];
    var newPositionA = [currentPositionA[0], currentPositionA[1] + 100];
    textProp.setValue(textDocument);
    compDados.layer('T_TEXTO_LONGO').property("Position").setValue(newPositionT)
    compDados.layer('P_ASPAS_LONGO').property("Position").setValue(newPositionA)
}

if (textHeight >= 180 && textHeight < 240) {
    var newPositionT = [currentPositionT[0], currentPositionT[1] + 100];
    var newPositionA = [currentPositionA[0], currentPositionA[1] + 100];
    compDados.layer('T_TEXTO_LONGO').property("Position").setValue(newPositionT)
    compDados.layer('P_ASPAS_LONGO').property("Position").setValue(newPositionA)
}

if (textHeight >= 240 && textHeight < 300) {
    var newPositionT = [currentPositionT[0], currentPositionT[1] + 50];
    var newPositionA = [currentPositionA[0], currentPositionA[1] + 50];
    compDados.layer('T_TEXTO_LONGO').property("Position").setValue(newPositionT)
    compDados.layer('P_ASPAS_LONGO').property("Position").setValue(newPositionA)
}

var compFonte = app.project.item(3);
TrocarTexto(compFonte, "T_FONTE", dados.fonte);

var textRect = compFonte.layer('T_FONTE').sourceRectAtTime(1, false);
var textWidth = textRect.width;

tamanhoBox = compFonte.layer('S_BOX').width;
novoTamanhoBox = textWidth + 20
deltaTamanho = (novoTamanhoBox / tamanhoBox) * 100

compFonte.layer('S_BOX').property("Scale").setValue([deltaTamanho, 100]);


var compFoto = app.project.item(4);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "temp/" + dados.arquivo));
var videoImportado = app.project.importFile(importOptions);
compFoto.layer('A_FOTO').replaceSource(videoImportado, false);


app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
