const handleloginsubmit = () => {
    const username = document.forms['loginform']['userName'].value; 
    const password = document.forms['loginform']['password'].value;

    const uerror = document.getElementById("username_errormessage");
    const perror = document.getElementById("password_errormessage");

    if (username == null || username == "") {
            uerror.innerHTML = "نام کاربری الزامی است";

    }

    if (password == null || password == "") {
            perror.innerHTML ="گذزواژه الزامی است";
            
    }
}

