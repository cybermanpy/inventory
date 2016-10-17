var dibujo, lienzo
function begin()
{
    dibujo = document.getElementById("dibujito");
    lienzo = dibujo.getContext("2d");
    lienzo.beginPath();
    lienzo.moveTo(68,120);
    lienzo.lineTo(68,70);
    lienzo.closePath();
    lienzo.strokeStyle = "#000";
    lienzo.stroke();

    lienzo.beginPath();
    lienzo.strokeStyle = "#1D548E";
    lienzo.fillStyle = "#1D548E";
    lienzo.arc(35,88,5, (Math.PI * 2), false);
    lienzo.closePath();
    lienzo.fill();
    lienzo.stroke();

    lienzo.beginPath();
    lienzo.strokeStyle = "#BF2D31";
    lienzo.fillStyle = "#BF2D31";
    lienzo.arc(50,100,15, (Math.PI * 2), false);
    lienzo.closePath();
    lienzo.fill();
    lienzo.stroke();

    lienzo.beginPath();
    // lienzo.strokeStyle = "#F2F2F2";
    // lienzo.fillStyle = "#FFFAFA";
    lienzo.strokeStyle = "#DCDCDC";
    lienzo.fillStyle = "#DCDCDC";
    lienzo.arc(20,95,10, (Math.PI * 2), false);
    lienzo.closePath();
    lienzo.fill();
    lienzo.stroke();

    lienzo.beginPath();
    lienzo.font = "10pt Verdana";
    lienzo.lineWidth = '1';
    lienzo.strokeStyle = '#000';
    lienzo.fillStyle = "#000";
    lienzo.closePath();
    lienzo.fillText("ANEAES",73,85);

    lienzo.beginPath();
    lienzo.font = "7pt Verdana";
    lienzo.lineWidth = '1';
    lienzo.strokeStyle = '#000';
    lienzo.fillStyle = "#000";
    lienzo.closePath();
    lienzo.fillText("Agencia Nacional de Evaluación y",73,95);

    lienzo.beginPath();
    lienzo.font = "7pt Verdana";
    lienzo.lineWidth = '1';
    lienzo.strokeStyle = '#000';
    lienzo.fillStyle = "#000";
    lienzo.closePath();
    lienzo.fillText("Acreditación de la Educación Superior",73,110);
}