// Handle submit on form lobby.html
function handleSubmit(event) {
    event.preventDefault();
    const data = new FormData(event.target);
    let value = {
        "meetingRoomName": data.get("mrname"),
        "displayName": data.get("displayName"),
        "email": data.get("email")
        };
        console.log({ value });
        fetch("/api/startMeeting", {
        method: "post",
        body: JSON.stringify(value)
        }).then(resp => resp.text()).then(html => document.body.innerHTML = html)
    }
    const form = document.querySelector('form');
    form.addEventListener('submit', handleSubmit);
    
    // Change thing imported from zoom-client project, maybe won't be useful here
    function chnageThing(url) {
            fetch(url)
        }
    
    // Toggle password input form in the control.html
    function toggleOverlay() {
        let overlayDiv = document.querySelector(".overlay");
        console.log(overlayDiv.style.opacity);
        if (overlayDiv.style.opacity === '0')
            overlayDiv.style.opacity = 1;
        else
            overlayDiv.style.opacity = 0;
        }