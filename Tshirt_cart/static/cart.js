function func(str) {
    let btn = document.getElementsByClassName(str)[0]
    btn.style.display = 'inline';
    btn.style.width = '100px'
    btn.style.height = '30px'

}

function update_db(str, id, sub_cart) {
    let inp = document.getElementsByClassName(str)[0]
    $.ajax({
        type: 'GET',
        url: '/cart/update_db/',
        data: { 'updated_count': inp.value, 'id': id }
    }).done((response) => {
        console.log(response);
        let main = document.getElementsByClassName(sub_cart)[0]
        main.style.opacity = '.3';
        setTimeout(blurrr, 1000)
        function blurrr() {
            let main = document.getElementsByClassName(sub_cart)[0]
            main.style.opacity = '1';
            $('#total_h1').load(location.href + ' #total_h1')
        }
    })
}
function delete_item(cart_id, sub_cart, hr) {
    $.ajax({
        type: 'GET',
        url: '/cart/delete_item/',
        data: { 'cart_id': cart_id }
    }).done((response) => {
        console.log(response);
        let main = document.getElementsByClassName(sub_cart)[0]
        let hrr = document.getElementsByClassName(hr)[0]
        main.remove()
        hrr.remove()
        $('#total_h1').load(location.href + ' #total_h1')
        if (response['remaining'] == 0) {
            let cart = document.getElementsByClassName('cart')[0]
            cart.style.display = 'none';
            $('.sub_main').load(location.href + ' .sub_main')
        }
    })
}