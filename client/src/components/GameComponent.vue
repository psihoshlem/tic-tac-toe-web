<template>
    <div class="root">
        <div id="information">
        <div id="players_count_div">Count of players: {{players_count}}/2</div>
        <div id="current_player_div">Current player: {{current_player}}</div>
        <div id="self_div">You play by: {{self}}</div>
    </div>
    <div id="board_container">
        <table id="board">
            <tr>
                <td id="1" v-on:click="cellClick(1)"></td>
                <td id="2" v-on:click="cellClick(2)"></td>
                <td id="3" v-on:click="cellClick(3)"></td>
            </tr>
            <tr>
                <td id="4" v-on:click="cellClick(4)"></td>
                <td id="5" v-on:click="cellClick(5)"></td>
                <td id="6" v-on:click="cellClick(6)"></td>
            </tr>
            <tr>
                <td id="7" v-on:click="cellClick(7)"></td>
                <td id="8" v-on:click="cellClick(8)"></td>
                <td id="9" v-on:click="cellClick(9)"></td>
            </tr>
        </table>
    </div>
    <div id="other_information"></div>
    </div>
</template>
<script>
export default {
  name: 'GameComponent',
  data(){
    return{
        players_count: 0,
        current_player: '-',
        self: '-'
    }
  },
  methods:{
    cellClick: function(id){
        console.log(this.players_count)
        console.log(id)
    }
  },
  created: function() {
    console.log("Starting connection to WebSocket Server")
    this.connection = new WebSocket("ws://127.0.0.1:8000/ws")

    this.connection.onmessage = function(event) {
      var response = JSON.parse(event.data)
      console.log(response)
      if (response["stage"] == "init"){
          console.log("ok")
          this.players_count = response["players_count"];
          console.log(response["players_count"])
          this.self = response["self"];
          if(response["players_count"]==2){
            //   other_information.innerHTML = "Game has been started";
              this.current_player = 'X';
          }
      }
        // if (response["stage"] == "active"){
        //     updateCell(response["cell"], response["sign"]);
        //     current_player.innerHTML = response["current_player"];
        //     currentPlayer = response["current_player"];
        // }
        // if (response["stage"] == "end"){
        //     updateCell(response["cell"], response["sign"]);
        //     currentPlayer = null;
        //     current_player.innerHTML = ""
        //     other_information.innerHTML = "Game over! Winner is " + response["winner"];
        // }
    }

    this.connection.onopen = function(event) {
      console.log(event)
      console.log("Successfully connected to the echo websocket server...")
    }

  }

}
</script>
<style>
    #board{
        width: 600px;
        height: 600px;
        text-align:center;
    }
    td{
        border: 1px solid black;
        width: 197.86px;
        height: 197.86px;
        font-size: 100px;
    }
    #information
    {
        text-align:center;
    }
    #players_count_div, #current_player_div, #self_div
    {
        display:inline;
        font-size: 20px;
        margin-right: 35px;
    }
    #board_container{
        display: flex;
        align-items: center;
        justify-content: center;
    }
    #other_information{
        text-align: center;
        font-size: 40px;
    }
</style>