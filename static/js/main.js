const allItems =  document.querySelectorAll("*");
const menuButton = document.getElementById("menu");
const menuView = document.getElementById("menu-view");
const pageWrapper = document.getElementById("page-wrapper");
const pageWrapperItems = pageWrapper.querySelectorAll("*");
const changeColourButton = document.getElementById("change-colour"); 
const content = document.getElementById("content");

console.log(menuView);
let clicked = false;
let colour = false;

const handleResize = () => {
    if (window.innerWidth >= 1200) {
        if (clicked === true) {
            clicked = !clicked;
            menuView.style.display = "none";
        }
        pageWrapper.style.marginTop = "0";
    } 
}

changeColourButton.addEventListener("click", () => {
    colour = !colour;
    if (colour === true) {
        pageWrapperItems.forEach(item => {
            item.style.backgroundColor = "black";
            item.style.color = "white";
            changeColourButton.textContent = "☀️ Light mode";
            console.log(`Dark mode: ${colour}`)
        })
    } else {
        pageWrapperItems.forEach(item => {
            item.style.backgroundColor = "";
            item.style.color = "";
            changeColourButton.textContent = "🌙 Dark mode";
            console.log(`Dark mode: ${colour}`)
        })
    }

});

menuButton.addEventListener("click", () => {
    clicked = !clicked;
    if (clicked === true) {
        menuView.style.display = "flex";
        pageWrapper.style.marginTop = "175px";
        console.log(clicked)
    } else {
        pageWrapper.style.marginTop = "0";
        menuView.style.display = "none";
        console.log(clicked)
    };
});




window.addEventListener("resize", handleResize);