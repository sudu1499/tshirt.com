const pass1=document.getElementById('pass1')
const pass2=document.getElementById('pass2')
const btn=document.getElementById('btn')

pass2.addEventListener('keyup',()=>{
    if(pass1.value !== pass2.value){
        pass2.style.border='2px solid red';
        btn.disabled=true;
    }
    else{
        pass2.style.border='0px solid black';
        btn.disabled=false;


    }
})