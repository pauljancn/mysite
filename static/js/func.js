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

function vcode_blur(obj){
	if (obj.value.length>=4){
		regform.reg.disabled = false;
	}else{
		regform.reg.disabled = true;
	}
}

//注册、登录提交
var curURL =  window.location.host.replace(":8000","");
function reg_sub(){
	this.regform.action = "http://" + curURL + "/member/reg_deal_new.asp";
	document.getElementById("regform").submit();
}