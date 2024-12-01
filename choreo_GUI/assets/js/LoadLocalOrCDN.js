
var IsLocal = (location.hostname === "localhost" || location.hostname === "127.0.0.1" || location.hostname === "")
// var IsLocal = false

async function LoadLocalOrCDN(local_src, cnd_src = "", after = [], async = false, LoadLocal = IsLocal) {

    await Promise.all(after)
    
    prom =  new Promise(function(resolve, reject) {

        var script = document.createElement('script')
        script.onload = resolve
        if (LoadLocal) {
            script.src = local_src
        } else {
            if (cnd_src == "") {
                script.src = local_src
            } else {
                script.src = cnd_src
            }
        }
        script.async = true
        document.head.appendChild(script)
    })

    if (async){
        return prom
    } else {
        await prom
    }

}
