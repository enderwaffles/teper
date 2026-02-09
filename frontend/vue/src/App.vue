<template>
    <h1>{{ info }}</h1>
    <p>{{ info2 }}</p>
    <button type="button" v-on:click="userData()">Send</button> <br> <br>

    <!-- <input type="text" v-on:input="insertData($event.target.value)" placeholder="Imya"> -->
    <input type="text" v-model="imya" placeholder="Imya">
    <input type="text" v-model="familya" placeholder="Familya"> <br> <br>
    <button type="button" v-on:click="sendUser()">Send</button>
    <h1>{{ imya }}</h1>
 
    <User :users="users" :deleteUser="deleteUser"/>
</template>

<script>
import User from "./components/User.vue"
export default {
    components : { User },
    data() {
        return {
            users: [],
            info: "Title",
            info2: "Anons",
            imya: "",
            familya: "",
        }
    },
    
    methods: {
        userData() {
            this.info = 'Bruh';
        },
        insertData(value) {
            this.imya = value;
        },
        deleteUser() {
            console.log("delete")
        },
        sendUser() {
            if(this.imya == "" && this.familya == ""){
                this.imya = "error";
            }
            else {

            
                this.users.push({
                    imya: this.imya,
                    familya: this.familya,
                })
            }
        }

    }
}
</script>

<style>
body {
    background-color: black;
} 
h1 {
    color: coral;
}
p {
    color: white;
}
</style>
