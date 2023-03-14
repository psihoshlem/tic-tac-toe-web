<template>
  <div id="container">
    <div class="swap-form-container">
      <button class="swap-form-btn" v-on:click="swap_form(1)">sing in</button>
      <button class="swap-form-btn" v-on:click="swap_form(2)">sing up</button>
    </div>
    <div class="container">
      <div class="sign_in" v-show="step===1">
        <div class="brand-title">SIGN IN</div>
        <div class="inputs">
          <label>LOGIN</label>
          <input v-model="login" type="login" placeholder="login" />
          <label>PASSWORD</label>
          <input v-model="password" type="password" placeholder="password" />
          <button class="submit" type="submit" v-on:click="sign_in()">SIGN IN</button>
        </div>
      </div>
      <div class="sign_in" v-show="step===2">
        <div class="brand-title">SIGN UP</div>
        <div class="inputs">
          <label>LOGIN</label>
          <input v-model="login" type="login" placeholder="login" />
          <label>PASSWORD</label>
          <input v-model="password" type="password" placeholder="Min 6 charaters long" />
          <input v-model="retried_password" type="password" placeholder="Retry please" />
          <button class="submit" type="submit" v-on:click="sign_up()">SIGN UP</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        name: 'AuthComponent',
        step: 1,
        login: "",
        password: "",
        retried_password: "",
        auth: false
      }
    },
    methods: {
      swap_form: function(n){
        this.step = n
        console.log(this.auth)
      },
      sign_in: function(){
        console.log("login")
        var xhr = new XMLHttpRequest();

        var json_user_data = JSON.stringify({
            login: this.login,
            password: this.password
        });

        xhr.open("POST", 'http://127.0.0.1:8000/log', true)
        xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');
        xhr.onreadystatechange = function () {
          if (this.readyState==this.DONE){
            this.auth = (xhr.responseText == "true")
            console.log(this.auth)
          }
        }
        xhr.send(json_user_data);
      },
      sign_up: function(){
        console.log("reg")
        var xhr = new XMLHttpRequest();

        var json_user_data = JSON.stringify({
          login: this.login,
          password: this.password
        });

        xhr.open("POST", 'http://127.0.0.1:8000/reg', true)
        xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');
        xhr.onreadystatechange = function () {
          console.log(xhr.responseText)
        }
        xhr.send(json_user_data);
        console.log(this.auth)
      }
    }
  }
</script>
<style>
input {
  caret-color: black;
}

body {
  margin: 0;
  width: 100vw;
  height: 100vh;
  background: #ecf0f3;
  display: flex;
  align-items: center;
  text-align: center;
  justify-content: center;
  place-items: center;
  overflow: hidden;
  /* font-family: poppins; */
}

.container {
  position: relative;
  width: 350px;
  height: 500px;
  border-radius: 20px;
  padding: 40px;
  box-sizing: border-box;
  background: #ecf0f3;
  box-shadow: 14px 14px 20px #cbced1, -14px -14px 20px white;
}

.brand-logo {
  height: 100px;
  width: 100px;
  background: url("https://img.icons8.com/color/100/000000/twitter--v2.png");
  margin: auto;
  border-radius: 50%;
  box-sizing: border-box;
  box-shadow: 7px 7px 10px #cbced1, -7px -7px 10px white;
}

.brand-title {
  margin-top: 10px;
  font-weight: 900;
  font-size: 1.8rem;
  color: #1DA1F2;
  letter-spacing: 1px;
}

.inputs {
  text-align: left;
  margin-top: 30px;
}

label, input, button {
  display: block;
  width: 100%;
  padding: 0;
  border: none;
  outline: none;
  box-sizing: border-box;
}

label {
  margin-bottom: 4px;
}

label:nth-of-type(2) {
  margin-top: 12px;
}

input::placeholder {
  color: gray;
}

input {
  background: #ecf0f3;
  padding: 10px;
  padding-left: 20px;
  height: 50px;
  font-size: 14px;
  border-radius: 50px;
  box-shadow: inset 6px 6px 6px #cbced1, inset -6px -6px 6px white;
}

.submit {
  color: white;
  margin-top: 20px;
  background: #1DA1F2;
  height: 40px;
  border-radius: 20px;
  cursor: pointer;
  font-weight: 900;
  box-shadow: 6px 6px 6px #cbced1, -6px -6px 6px white;
  transition: 0.5s;
}

button:hover {
  box-shadow: none;
}

a {
  position: absolute;
  font-size: 8px;
  bottom: 4px;
  right: 4px;
  text-decoration: none;
  color: black;
  background: yellow;
  border-radius: 10px;
  padding: 2px;
}

h1 {
  position: absolute;
  top: 0;
  left: 0;
}
</style>