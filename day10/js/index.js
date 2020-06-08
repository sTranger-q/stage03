// $().ready(function(){
//     $('.grade a').on('click',function(){
//         $('.grade a').removeClass('text-danger');
//         $(this).addClass('text-danger');
//     })
//     $('.campus a').on('click',function(){
//         $('.campus a').removeClass('text-danger');
//         $(this).addClass('text-danger');
//     })
// })
$().ready(function () {
    $('nav a').on('click', function () {
        // 找祖先元素
        var parents=$(this).parents('.grade');
        if (parents.length) {
                $('.grade a').removeClass('text-danger');
        }else{
            $('.campus a').removeClass('text-danger');
        }
        $(this).addClass('text-danger');
    })
})