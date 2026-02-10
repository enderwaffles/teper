
<script>
export default {
    data() {
        return {
            city: "",
            error: ""
        }
    },
    methods: {

    
        getWeather() {
            if(this.city.trim().length < 2) {
                this.error = "aa";
                return false;            
            }
            this.error = "";
        }
    }
    
}
</script>

<template>
    <div class="wrapper">
        <h1>Pogodnoye prilojenie</h1>
        <p>Uznat pogodu v {{ city == "" ? "vashem gorode" : "gorode " + city }}</p>
        <input type="text" v-on:input="this.city = $event.target.value" placeholder="Vvedite gorod">
        <button v-show="city != ''" v-on:click="getWeather()">Get weather</button>
        <p class="error">{{ error }}</p>
    </div>
</template>




<style scoped>

.error {
    color: red;
}

.wrapper {
    width: 900px;
    height: 500px;
    border-radius: 50px;
    padding: 20px;
    background: rgb(28, 28, 28);
    text-align: center;
    color: white;
}
.wrapper p {
    margin-top: 20px;
}
.wrapper input {
    margin-top: 30px;
    background: transparent;
    border: 0;
    border-bottom: 2px solid rgb(28, 28, 28);
    color: white;
    font-size: 14px;
    padding: 5px 8px;
    outline: none;
}
.wrapper input:focus {
    border-bottom-color: green;
}
.wrapper button {
    background: green;
    color:  white;
    border-radius: 10px;
    border: 2px solid green;
    padding: 10px 15px;
    margin-left: 20px;
    cursor: pointer;
    transition: transform 500ms ease;
    }
.wrapper button:hover {
    transform: scale(1.1) translateY(-5px);
} 
</style>
