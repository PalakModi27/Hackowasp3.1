let fm= document.forms.myform;
let Mes =document.getElementById("mes");
fm.onsubmit = function()
{console.log("k");
    if( fm.name.value < 90 )
    {
        Mes.innerHTML="please see a doctor immidiately";
        return false;
    }
    else
    {
        Mes.innerHTML ="<a href='sym.html'>NEXT</a>";
        return true;
    }
};
function s()
{   console.log(fm.name.vaue)
    console.log(fm.name.value);
    console.log(fm.color.value);
};
setTimeout(s,10000)