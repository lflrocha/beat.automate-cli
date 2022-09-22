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
var _io = new ImportOptions(File(baseFolder + "projetos/tvbr_eleicoes2022_mapa_governador.aep"));
if(_io.canImportAs(ImportAsType.PROJECT)){
        _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);


// Abre o arquivo JSON
// var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
var arquivoJson = new File(caminhoDados)
if (arquivoJson.open("r")) {
        arquivoJson.encoding = "UTF-8";
        var meuJSON = arquivoJson.read();
        var dados = JSON.parse(meuJSON)
        arquivoJson.close();
}

// Define as variáveis a partir dos dados do JSON
var compDados = app.project.item(2)
TrocarTexto(compDados, "AC-dado", dados.AC_dado)
TrocarTexto(compDados, "AL-dado", dados.AL_dado)
TrocarTexto(compDados, "AP-dado", dados.AP_dado)
TrocarTexto(compDados, "AM-dado", dados.AM_dado)
TrocarTexto(compDados, "BA-dado", dados.BA_dado)
TrocarTexto(compDados, "CE-dado", dados.CE_dado)
TrocarTexto(compDados, "DF-dado", dados.DF_dado)
TrocarTexto(compDados, "ES-dado", dados.ES_dado)
TrocarTexto(compDados, "GO-dado", dados.GO_dado)
TrocarTexto(compDados, "MA-dado", dados.MA_dado)
TrocarTexto(compDados, "MT-dado", dados.MT_dado)
TrocarTexto(compDados, "MS-dado", dados.MS_dado)
TrocarTexto(compDados, "MG-dado", dados.MG_dado)
TrocarTexto(compDados, "PA-dado", dados.PA_dado)
TrocarTexto(compDados, "PB-dado", dados.PB_dado)
TrocarTexto(compDados, "PR-dado", dados.PR_dado)
TrocarTexto(compDados, "PE-dado", dados.PE_dado)
TrocarTexto(compDados, "PI-dado", dados.PI_dado)
TrocarTexto(compDados, "RJ-dado", dados.RJ_dado)
TrocarTexto(compDados, "RN-dado", dados.RN_dado)
TrocarTexto(compDados, "RS-dado", dados.RS_dado)
TrocarTexto(compDados, "RO-dado", dados.RO_dado)
TrocarTexto(compDados, "RR-dado", dados.RR_dado)
TrocarTexto(compDados, "SC-dado", dados.SC_dado)
TrocarTexto(compDados, "SP-dado", dados.SP_dado)
TrocarTexto(compDados, "SE-dado", dados.SE_dado)
TrocarTexto(compDados, "TO-dado", dados.TO_dado)

app.endSuppressDialogs(false)
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
