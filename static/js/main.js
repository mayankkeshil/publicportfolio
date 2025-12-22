const allItems =  document.querySelectorAll("*");
const menuButton = document.getElementById("menu");
const menuView = document.getElementById("menu-view");
const pageWrapper = document.getElementById("page-wrapper");
const pageWrapperItems = pageWrapper.querySelectorAll("*:not(#copyright, footer)");
const changeColourButton = document.getElementById("change-colour"); 
const content = document.getElementById("content");
const allBoxes = document.querySelectorAll(".project-tile, #academics, #projects, #certifications");


if (!localStorage.getItem("theme")) {
    localStorage.setItem("theme", "light");
}

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


const applyTheme = () => {
    if (localStorage.getItem("theme") === "light") {
        pageWrapperItems.forEach(item => {
            item.style.backgroundColor = "black";
            item.style.color = "white";
            changeColourButton.textContent = "☀️ Light mode";
            console.log(`Dark mode: ${colour}`)
        })
        allBoxes.forEach(box => {
            box.style.background = "linear-gradient(black, black) padding-box, linear-gradient(45deg, #336dff, #33a2ff, #336dff) border-box";
        });
    } else {
        pageWrapperItems.forEach(item => {
            item.style.backgroundColor = "";
            item.style.color = "";
            changeColourButton.textContent = "🌙 Dark mode";
            console.log(`Dark mode: ${colour}`)
        })
        allBoxes.forEach(box => {
            box.style.background = "linear-gradient(white, white) padding-box, linear-gradient(45deg, #336dff, #33a2ff, #336dff) border-box";
        })
    }
};

changeColourButton.addEventListener("click", () => {
    localStorage.setItem("theme", localStorage.getItem("theme") === "light" ? "dark" : "light");
    applyTheme(); 
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
applyTheme();