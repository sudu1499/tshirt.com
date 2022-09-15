const burger=document.getElementById('burger')
const links=document.getElementsByClassName('nav_links')[0]

burger.addEventListener('click',()=>{
    links.classList.toggle('active')
})
// here 'acive' name is added and removed alternatively to change the class name 