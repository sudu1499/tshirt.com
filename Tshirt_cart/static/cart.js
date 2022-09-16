function func(str){
    let btn=document.getElementsByClassName(str)[0]
    btn.style.display='inline';
    btn.style.width='100px'
    btn.style.height='30px'

}

function update_db(str,id){
    let inp=document.getElementsByClassName(str)[0]
    $.ajax({
        type:'GET',
        url:'/cart/update_db/',
        data:{'updated_count':inp.value,'id':id}
    }).done((response)=>{
        console.log(response);
        let main=document.querySelector('.main')
        main.style.opacity='.3';
        setTimeout(blurrr,1000)
        function blurrr(){
            let main=document.querySelector('.main')
            main.style.opacity='1';
        }
    })
}