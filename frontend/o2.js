let fm= document.forms.myform;
let Mes =document.getElementById("mes");

//let sp=fm.abc.value;

fm.onsubmit = function()
{console.log(fm.name.value);
    if( fm.name.value<92)
    {
        Mes.innerHTML="Serious! You need to consult a doctor!";
        return false;
    }
     else
     {
        Mes.innerHTML ="All good! Just keep exercising!";
       return false;
     }
};
