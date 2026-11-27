/**
 * Ejemplo de función personalizada para Google Sheets
 * que consume la API HTTP local de ChuspaCalc.
 *
 * Requiere que ChuspaCalc esté ejecutándose localmente
 * con la API activada.
 */

function CHUSPACALC_CALCULAR(herramienta, parametros) {
  var url = "http://localhost:8000/calcular/" + herramienta;

  var opciones = {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify({
      parametros: parametros
    })
  };

  var respuesta = UrlFetchApp.fetch(url, opciones);

  var datos = JSON.parse(
    respuesta.getContentText()
  );

  return datos.resultado;
}
