// javascript to resolve the issue of displaced footer

function adjustFooter() {
    const body = document.body;
    const html = document.documentElement;
    const footer = document.querySelector("footer");

    // Get total document height
    let contentHeight = body.offsetHeight;
    let viewportHeight = window.innerHeight;

    if (contentHeight < viewportHeight) {
        footer.style.position = "absolute";
        footer.style.bottom = "0";
    } else {
        footer.style.position = "relative";
    }
}

// Run function on load and resize
window.onload = adjustFooter;
window.onresize = adjustFooter;