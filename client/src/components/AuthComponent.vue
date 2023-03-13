<template>
  <div id="container">
    <div class="swap-form-container">
      <button class="swap-form-btn" v-on:click="swap_form(2)">sing in</button>
      <button class="swap-form-btn" v-on:click="swap_form(1)">sing up</button>
    </div>
    <div class="container">
      <div class="sign_in" v-show="step===2">
        <div class="brand-title">SIGN IN</div>
        <div class="inputs">
          <label>LOGIN</label>
          <input type="login" placeholder="login" />
          <label>PASSWORD</label>
          <input type="password" placeholder="Min 6 charaters long" />
          <button class="submit" type="submit">SIGN IN</button>
        </div>
      </div>
      <div class="sign_in" v-show="step===1">
        <div class="brand-title">SIGN UP</div>
        <div class="inputs">
          <label>LOGIN</label>
          <input type="login" placeholder="login" />
          <label>PASSWORD</label>
          <input type="password" placeholder="Min 6 charaters long" />
          <input type="password" placeholder="Retry please" />
          <button class="submit" type="submit">SIGN UP</button>
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
        step: 1
      }
    },
    methods: {
      swap_form : function(n){
        this.step = n
      }
    }
  }
</script>
<style>
input {
  caret-color: red;
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
  font-family: poppins;
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