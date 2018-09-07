//ajax调用处理------------------
//function ignoreError() {
//  return true;
//}
var xmlHttp = false;
try {
	xmlHttp = new XMLHttpRequest();
} catch (trymicrosoft) {
  try {
    xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
  } catch (othermicrosoft) {
    try {
      xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
    } catch (failed) {
      xmlHttp = false;
    }
  }
}
if (!xmlHttp)
	  alert("Error initializing XMLHttpRequest!");

function test() {
	var icode = (Math.floor(Math.random()*(9999-1000))+1000);
	xmlHttp.open("GET", "http://bj.efwang.com/member/setVCode.asp?mob=11&code=" + icode, true);
	xmlHttp.setRequestHeader('Content-Type','text/html');
	xmlHttp.onreadystatechange = test2;
	xmlHttp.send(null);
}
function test2(){
	if (xmlHttp.readyState == 4) {
		if(xmlHttp.status==200){
	  		var response = xmlHttp.responseText;
	  		alert(response);
		}else if(xmlHttp.status==404){
			alert("Request URL does not exist");
		}else{
			return;
		}
	}
}
//获取登录验证码
var countdown=60; 
function settime(val) { 
	if (countdown == 0) { 
		val.removeAttribute("disabled");    
		val.value="获取验证码"; 
		countdown = 60; 
		if(countdown==60){return;}
	} else { 
		val.setAttribute("disabled", true); 
      	val.value="重新发送(" + countdown + ")"; 
		countdown--; 
	} 
   
	setTimeout(function() { 
		settime(val)},1000) 
} 

//注册、登录提交
var curURL =  window.location.host.replace(":8000","");
function reg_sub(){
	this.regform.action = "http://" + curURL + "/member/reg_deal_new.asp";
	//document.getElementById("regform").submit();
}