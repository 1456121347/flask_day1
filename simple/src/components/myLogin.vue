<template>
    <div class='login-wrapper'>
        <div class="login-mask" id='mask'></div>
        <div class="ui-dialog" id='dialogMove'>
            <div class="ui-dialog-title" id='dialogDrag'>
                用户名密码登录
                <a href="javascript:void(0)" class='ui-dialog-closebutton'>×</a>
            </div>
            <div class="ui-dialog-content">
                <div class='ui-dialog-content-item ui-dialog-username'>
                    <input class="ui-dialog-input" type="text" placeholder='手机号/邮箱'>
                </div>
                <div class='ui-dialog-content-item ui-dialog-password'>
                    <input class="ui-dialog-input" type="text" placeholder="密码">
                </div>
                <div class='ui-dialog-content-item ui-dialog-login'>
                    <a href="" class="ui-dialog-submit">登  录</a>
                </div>
                <div class='ui-dialog-content-item ui-dialog-forget'>
                    <a href="">忘记密码</a>
                </div>
                <div class='ui-dialog-content-item ui-dialog-register'>
                    <a href="">立即注册</a>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    
}
</script>

<style scoped>
    /* .login-wrapper{
        display: flexed;
        justify-content: center;
        align-items: center;
    } */
    .ui-dialog{
        width: 400px;
        height: auto;
        position: absolute;
        z-index: 9000;
        top:50%;
        left:50%;
        margin-top: -300px;
        margin-left: -200px;
        border: 1px solid #5e7c85;
        background: white;
        box-shadow: 0 0 30px #5e7c85;
    }
    .ui-dialog a{
        text-decoration: none;

    }
    .ui-dialog-title{
        height: 48px;
        line-height: 48px;
        padding: 0px 20px;
        color: #535353;
        font-size: 16px;
        border-bottom: 1px solid #efefef;
        background: #f5f5f5;
        cursor: move;
        user-select: none;
        text-align: center;
    }
    .ui-dialog-title a{
        font-size: 24px;
        color: teal;
        font-weight: bold;
        width: 16px;
        height: 16px;
        display: block;
        position: absolute;
        top:-5px;
        right: 20px;
    }
    .ui-dialog-title a:hover{
        color: rebeccapurple;
    }
    .ui-dialog-content{
        padding: 15px 20px;
    }
    .ui-dialog-content-item{
        height: 40px;
        line-height: 40px;
        text-align: right;
        margin-top: 20px;
    }
    .ui-dialog-input{
        width: 100%;
        height: 40px;
        border: 1px solid #d5d5d5;
        font-size: 16px;
        color: #c1c1c1;
        text-indent: 15px;
        outline: none;

    }
    .ui-dialog-submit{
        display: block;
        width: 100%;
        height: 45px;
        background: #5e7c85;
        border:none;
        color: #ffffff;   
        text-align: center;
        line-height: 45px;
        font-size: 20px;
        font-weight: bold;
    }
    .ui-dialog-submit:hover{
        background: rgb(11, 140, 226);
    }
    .login-mask{
        width: 100%;
        height: 100%;
        background: #000;
        position: absolute;
        top: 0;
        left: 0;
        z-index:7000;
        opacity: 0.5;
    }
</style>
