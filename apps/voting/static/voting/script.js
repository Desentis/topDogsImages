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
            wrapper = event.target.parentElement
            wrapper.classList.add("voted")
            votes = wrapper.getElementsByClassName("votes")[0]
            votes.innerHTML = parseInt(votes.innerHTML) + 1

            location.reload()
        }
    })
}