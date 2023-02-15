<template>
    <div class="root">
        <div id="information">
        <div id="players_count_div">Count of players: <a id="players_count">0</a></div>
        <div id="current_player_div">Current player: <a id="current_player">-</a></div>
        <div id="self_div">You play by: <a id="self">-</a></div>
    </div>
    <div id="board_container">
        <table id="board">
            <tr>
                <td id="1" v-on:click="updateCell()"></td>
                <td id="2" v-on:click="updateCell()"></td>
                <td id="3" v-on:click="updateCell()"></td>
            </tr>
            <tr>
                <td id="4" v-on:click="updateCell()"></td>
                <td id="5" v-on:click="updateCell()"></td>
                <td id="6" v-on:click="updateCell()"></td>
            </tr>
            <tr>
                <td id="7" v-on:click="updateCell()"></td>
                <td id="8" v-on:click="updateCell()"></td>
                <td id="9" v-on:click="updateCell()"></td>
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
        text:"hello"
    }
  },
  methods:{
    // cellClick(id){
    //     if(cell.innerHTML == '' & player==currentPlayer){
    //         updateCell(id, 'X')
    //     }
    //     else {
    //         other_information.innerHTML = "This cell can't be choosed!"
    //     }
    // },
    updateCell(){
        this.message = 'X';
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