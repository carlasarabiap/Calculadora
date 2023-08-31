
function sumar(){
    num1=parseFloat(document.getElementById("num1").value);
    num2=parseFloat(document.getElementById("num2").value);
    resultado = num1 + num2;
    //console.log(num1);
    //console.log(num2);
    //console.log(resultado);
    document.getElementById("resultado").value=resultado;
}

function restar(){
    num1=parseFloat(document.getElementById("num1").value);
    num2=parseFloat(document.getElementById("num2").value);
    resultado = num1 - num2;
    document.getElementById("resultado").value=resultado;
}

function multiplicar(){
    num1=parseFloat(document.getElementById("num1").value);
    num2=parseFloat(document.getElementById("num2").value);
    resultado = num1 * num2;
    document.getElementById("resultado").value=resultado;
}

function dividir(){
    num1=parseFloat(document.getElementById("num1").value);
    num2=parseFloat(document.getElementById("num2").value);
    resultado = num1 / num2;
    document.getElementById("resultado").value=resultado;
}