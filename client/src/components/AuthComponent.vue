<template>
  <div id="container">
    <div class="row">
      <form>
        <div class="auth" v-show="step===1">
          <div class="mb-3">
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="login">
          </div>
          <div class="mb-3">
            <input type="password" class="form-control" id="exampleInputPassword1" placeholder="password">
          </div>
          <button type="button" class="btn btn-primary" v-on:click="swap_form(2)">Submit</button>
        </div>
        <div class="reg" v-show="step===2">
          <div class="mb-3">
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="login">
          </div>
          <div class="mb-3">
            <input type="password" class="form-control" id="exampleInputPassword1" placeholder="password">
          </div>
          <div class="mb-3">
            <input type="password" class="form-control" id="exampleInputPassword1" placeholder="retry password">
          </div>
          <button type="button" class="btn btn-primary" v-on:click="swap_form(1)">Submit</button>
        </div>
      </form>
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
#container{
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>