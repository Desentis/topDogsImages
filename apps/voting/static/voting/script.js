window.onload = () => {
    Array.from(document.getElementsByClassName("image")).forEach((element) => {
        element.onclick = event => {
            event.target.onclick = null
            fetch("127.0.0.1", {
                method: "POST",
                body: JSON.stringify({
                    "link": event.target.getAttribute("src")
                }),
                headers: {
                    "Content-type": "application/json; charset=UTF-8"
                }
            })
        }
    })
}