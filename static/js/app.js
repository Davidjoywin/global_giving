const activate_menu_bttn = (user_menu_bttn, menu_dropdown) => {
    menu_dropdown.style.display = 'none';
    user_menu_bttn.addEventListener('click', () => {
        if (menu_dropdown.style.display === "block") {
            menu_dropdown.style.display = 'none';
        } else {
            menu_dropdown.style.display = 'block';
        }
    })
}

document.addEventListener('DOMContentLoaded', () => {

    let menu_dropdown = document.getElementById("menu"); // menu drop down
    let user_menu_bttn = document.getElementById("user-menu-button");   // user icon button

    let mobile_menu = document.getElementById("mobile-menu");
    let mobile_user_menu_bttn = document.getElementById("mobile-user-menu-button")

    activate_menu_bttn(user_menu_bttn, menu_dropdown)
    activate_menu_bttn(mobile_user_menu_bttn, mobile_menu)
})