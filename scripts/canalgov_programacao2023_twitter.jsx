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
var _io = new ImportOptions(File(baseFolder + "projetos/canalgov_programacao2023_twitter.aep"));
if(_io.canImportAs(ImportAsType.PROJECT)){
    _io.importAs = ImportAsType.PROJECT;
}
var projetoImportado = app.project.importFile(_io);

// Abre o arquivo JSON
var caminhoDados = arqScript.path + "/" + nomeProjeto + ".json";
var arquivoJson = new File(caminhoDados)
if (arquivoJson.open("r")) {arquivoJson.encoding = "UTF-8";
    var meuJSON = arquivoJson.read();
    var dados = JSON.parse(meuJSON);
    arquivoJson.close();
}

nome_perfil = dados['nome_perfil']
usuario_perfil = dados['usuario_perfil']
biografia_perfil = dados['biografia_perfil']
arq_img_perfil = dados['foto_perfil']
arq_banner = dados['foto_topo']
dados_tweets = dados['dados_tweets']
dados_seguindo = dados['dados_seguindo']
dados_seguidores = dados['dados_seguidores']
dados_curtidas = dados['dados_curtidas']
msg = dados['texto']
midia = dados['midia']
media_type = dados['tipo_midia']
aspect = dados['aspecto']
legenda = dados['legenda']
data = dados['data']

var comp_principal = app.project.item(2);
var comp_contadores = app.project.item(3);
var comp_foto_perfil = app.project.item(4);
var comp_foto_topo = app.project.item(5);
var comp_dados = app.project.item(6);
var comp_post_pagina = app.project.item(7);
var comp_post_destaque = app.project.item(8);


comp_contadores.layer("tweets").property("sourceText").setValue(dados_tweets)
comp_contadores.layer("seguindo").property("sourceText").setValue(dados_seguindo)
comp_contadores.layer("seguidores").property("sourceText").setValue(dados_seguidores)
comp_contadores.layer("curtidas").property("sourceText").setValue(dados_curtidas)

comp_dados.layer("nome_perfil").property("sourceText").setValue(nome_perfil)
comp_dados.layer("usuario_perfil").property("sourceText").setValue(usuario_perfil)
comp_dados.layer("biografia_perfil").property("sourceText").setValue(biografia_perfil)

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "temp/" + arq_img_perfil));
var perfilImportado = app.project.importFile(importOptions);
comp_foto_perfil.layer('foto_perfil').replaceSource(perfilImportado, false);

var importOptions = new ImportOptions();
importOptions.file = new File(File(baseFolder + "temp/" + arq_banner));
var bannerImportado = app.project.importFile(importOptions);
comp_foto_topo.layer('foto_topo').replaceSource(bannerImportado, false);


comp_post_pagina.layer("nome_perfil").property("sourceText").setValue(nome_perfil)
comp_post_pagina.layer("usuario_perfil").property("sourceText").setValue("@" + usuario_perfil)
comp_post_pagina.layer("data").property("sourceText").setValue(data)

var largura_nome = comp_post_pagina.layer("nome_perfil").sourceRectAtTime(1, true).width;
comp_post_pagina.layer("usuario_perfil").property("position").setValueAtTime(1, [largura_nome + 80, 22.5]);
var largura_usuario = comp_post_pagina.layer("usuario_perfil").sourceRectAtTime(1, true).width;
comp_post_pagina.layer("data").property("position").setValueAtTime(1, [largura_usuario + 20 + largura_nome + 80, 22.5]);
comp_post_pagina.layer("texto_post").property("sourceText").setValue(msg)

comp_post_destaque.layer("nome_perfil").property("sourceText").setValue(nome_perfil)
comp_post_destaque.layer("usuario_perfil").property("sourceText").setValue("@" + usuario_perfil)
comp_post_destaque.layer("data").property("sourceText").setValue(data)
comp_post_destaque.layer("texto_post").property("sourceText").setValue(msg)


if  (media_type == "video" || media_type == "photo")  {
    var importOptions = new ImportOptions();
    importOptions.file = new File(File(baseFolder + "temp/" + midia));
    var midiaImportado = app.project.importFile(importOptions);
    comp_post_pagina.layer('midia').replaceSource(midiaImportado, false);

    midia_largura = comp_post_pagina.layer('midia').sourceRectAtTime(1, true).width;
    midia_altura = comp_post_pagina.layer('midia').sourceRectAtTime(1, true).height;
    // alert(midia_largura);
    // alert(midia_altura);
    percent = 500 * 100 / midia_largura

    aux_altura = midia_altura * (percent / 100)
    limite_altura = 540
    if (aux_altura > limite_altura) {
        percent = limite_altura * 100 / midia_altura
    }
    comp_post_pagina.layer('midia').property("scale").setValueAtTime(1, [percent, percent]);
    if (media_type == "video") {
      comp_post_pagina.layer('midia').audioEnabled = false;
    }


    var importOptions = new ImportOptions();
    importOptions.file = new File(File(baseFolder + "temp/" + midia));
    var midiaImportado = app.project.importFile(importOptions);
    comp_post_destaque.layer('midia').replaceSource(midiaImportado, false);
    midia_largura = comp_post_pagina.layer('midia').sourceRectAtTime(1, true).width;
    midia_altura = comp_post_pagina.layer('midia').sourceRectAtTime(1, true).height;
    percent = 1200 * 100 / midia_largura
    aux_altura = midia_altura * (percent / 100)
    limite_altura = 1300
    if (aux_altura > limite_altura) {
        percent = limite_altura * 100 / midia_altura
    }
    comp_post_destaque.layer('midia').property("scale").setValueAtTime(1, [percent, percent]);

}





app.endSuppressDialogs(false);
app.endUndoGroup();
app.project.removeUnusedFootage();
novoArquivo = new File(baseFolder + 'temp/' + nomeProjeto + ".aep");
app.project.save(novoArquivo);
app.project.close(CloseOptions.SAVE_CHANGES);
