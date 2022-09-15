// const burger=document.getElementById('burger')
// const links=document.getElementsByClassName('nav_links')[0]

// burger.addEventListener('click',()=>{
//     links.classList.toggle('active')
// })
// here 'acive' name is added and removed alternatively to change the class name 


const individual=document.querySelectorAll('.individual')
const dumm1=document.getElementsByClassName('dumm1')[0]
const dumm2=document.getElementsByClassName('dumm2')[0]
// const individual_class=document.getElementsByClassName('individual')[0]


for(let i=0;i<individual.length;i++)
{   
    
    let category=individual[i].getElementsByTagName('h1')[0].innerHTML
    individual[i].addEventListener('click',()=>{
        window.location.href=window.location.href+'product_list/'+category+'/'
    })

}
function animate(){
    alert('hay')
}
