function visual_menu() {
    if ($('.m-header-burger').hasClass('active') && $('.m-header-menu').hasClass('active')) {
        $('.m-header-burger,.m-header-menu').toggleClass('active');
        $('body').toggleClass('lock');
    }
}

$(document).ready(function() {
    $('.m-header-burger').click(function(event) {
        $('.m-header-burger,.m-header-menu').toggleClass('active');
        $('body').toggleClass('lock');

        let menu_list = document.querySelectorAll('.m-header-link');
        console.log(menu_list);
        for (let link of menu_list) {
            link.addEventListener('click', visual_menu);
        }
    });

    let modal = document.getElementById('myModal');
    let btn = document.getElementById('myBtn')
    let span = document.querySelector('.close');

    btn.onclick = function() {
        modal.style.display = 'block';
    }
    span.onclick = function() {
        modal.style.display = 'none';
    }
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }

});

function visual_button(event) {
    let but = event.currentTarget.querySelector('.h-button');
    but.classList.remove('invisible-button')
    but.classList.add('visual-button');
}

function invisible_button() {
    let but = event.currentTarget.querySelector('.h-button');
    but.classList.remove('visual-button')
    but.classList.add('invisible-button');
}

function ready() {
    let buttons = event.currentTarget.querySelectorAll('.h-button');
    for (let but of buttons) {
        but.classList.add('invisible-button');
    }
    let lists = document.querySelectorAll('.h-list')
    for (let list of lists) {
        list.addEventListener('mouseover', visual_button);
        list.addEventListener('mouseout', invisible_button);
    }

}

document.addEventListener("DOMContentLoaded", ready);