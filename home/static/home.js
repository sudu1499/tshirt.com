// const burger=document.getElementById('burger')
// const links=document.getElementsByClassName('nav_links')[0]

// burger.addEventListener('click',()=>{
//     links.classList.toggle('active')
// })
// here 'acive' name is added and removed alternatively to change the class name 


let main = document.getElementsByClassName('individual')



function redirect(category) {
    window.location.href = window.location.href + 'product_list/' + category + '/'
}

for (let i = 0; i < main.length; i++) {
    const b1 = main[i].getElementsByClassName('b1')[0]
    const b2 = main[i].getElementsByClassName('b2')[0]
    const img = main[i].getElementsByClassName('ind_img')[0]

    main[i].addEventListener('mouseover', () => {
        b1.style.rotate = '10deg';
        b2.style.rotate = '-10deg';
        img.style.width = '101%';
        img.style.height = '101%';
        b1.style.zIndex = '-1';
        b2.style.zIndex = '-1';
        img.style.zIndex = '1000';
        b1.style.boxShadow = '0 0 10px 10px black';
        b2.style.boxShadow = '0 0 10px 10px black';
    })
    main[i].addEventListener('mouseleave', () => {
        b1.style.rotate = '0deg';
        b2.style.rotate = '0deg';
        img.style.width = '100%';
        img.style.height = '100%';
        b1.style.boxShadow = '0 0 black';
        b2.style.boxShadow = '0 0 black';
        b1.style.zIndex = '-1';
        b2.style.zIndex = '-1';
        img.style.zIndex = '1000';
    })

}

