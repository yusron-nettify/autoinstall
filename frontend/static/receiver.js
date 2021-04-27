// Build Meeting API Object
// const api = new JitsiMeetExternalAPI(domain, options);


var bannerList = [{
    hideWelcomme: false, img: "https://convergence.blob.core.windows.net/captive/IDDPSMAYA/bg_4.jpg", timer: 10, useVideo: false
}];

var banner = fetch("http://localhost:8000/api/bannerList")
.then(response => response.json())
.then(res => bannerList = res["List"])

const castObj = document.getElementById("cast");
const msgObj = document.getElementById("message");
const msgDivObj = document.getElementById("message-div");
const wlcmObj = document.getElementById("welcome");
const bgObj = document.getElementById("bg");
const bgVid = document.getElementById("bgVideo");
const overlayObj = document.getElementById("overlay");
const cssObj = document.getElementById("css");

// const CHANNEL = 'urn:x-cast:com.google.cast.nettifybanner';
// const ctx = cast.framework.CastReceiverContext.getInstance();
// const options = new cast.framework.CastReceiverOptions();
let bannerCounter = 0;
let lastMsg = "";

// options.customNamespaces = Object.assign({});
// options.customNamespaces[CHANNEL] = cast.framework.system.MessageType.JSON;
// options.disableIdleTimeout = true;

function isElementOverflowing(element) {
    var overflowX = element.offsetWidth < element.scrollWidth;
    return (overflowX);
}

//function isElementOverflowing2(element, child) {
//    if (child.classList.contains("marquee") == false) {
//        return ( element.offsetWidth < element.scrollWidth);
//    }
//    else {
//        let diff = (element.scrollWidth - element.offsetWidth);
//        return ( diff > element.offsetWdidth);
//    }
//}

function setMarqueeTick() {
    console.log("marquee tick");
    if (isElementOverflowing(msgDivObj)) {
        msgObj.classList.add("marquee");

        let aniSpeed = Math.floor(msgObj.offsetWidth / msgDivObj.offsetWidth) * 15;
        msgObj.style.animationDuration = aniSpeed + "s";
    }
    else {
        console.log("element NOT overflowing");
    }
}


function timerTick() {
    console.log("timer tick" + " bc: " + bannerCounter);
    console.log("Banner length "+ bannerList.length)
    try {
        if (bannerCounter >= bannerList.length) bannerCounter = 0;
        var data = bannerList[bannerCounter];
        console.log("bc:" + bannerCounter + " data: " + JSON.stringify(data));
        if (data) {
            if (data.useVideo) {
                bgVid.onended = function () {
                    timerTick();
                };
                bgVid.onerror = function () {
                    timerTick();
                };
                bgVid.src = data.img;
                bgVid.play()
                bgVid.hidden = false;
                bgObj.hidden = true;
            }

            else {
                window.setTimeout(timerTick, data.timer * 1000);
                console.log("Check this " + data.img);
                bgObj.src = data.img;
                bgObj.hidden = false;
                bgVid.hidden = true;
            }


            if (data.hideWelcomme) {
                overlayObj.style.display = "none";
            }

            else {
                overlayObj.style.display = "block";
            }

        }

        else {
            console.log("noData");
            window.setTimeout(timerTick, 10 * 1000, 0);
        }

    }

    catch (err) {
        console.log(err);
        window.setTimeout(timerTick, 10 * 1000, 0);
    }

    finally {
        if (bannerList.length <= 1) {
            bannerCounter = 0;
        }

        else {
            bannerCounter = (bannerCounter + 1) % bannerList.length;
        }

    }
}

timerTick();
setMarqueeTick()
// ctx.start(options);

