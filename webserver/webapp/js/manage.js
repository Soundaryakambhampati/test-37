var xhr = new XMLHttpRequest();

xhr.onreadystatechange = function () {
    if (this.readyState != 4) return;
    if (this.status == 200) {
        if(this.responseText.includes("invalid token")){
            alert('Invalid Token')
            window.location.replace("/html/login.html");
        }else{
            document.getElementById('videos').innerHTML = this.responseText;
        }
    };
};

var cookie = document.cookie;
try{
   var token = cookie.split('session=')[1].split(';')[0];
   if(token == null){
        window.location.replace("/html/login.html");
   }else{
        xhr.open('GET', '/python/manage.py', true);
        xhr.send(null);
   };
}
catch(err){
   window.location.replace("/html/login.html");
}



